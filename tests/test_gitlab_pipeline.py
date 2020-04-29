import json
import os
import urllib.request

import gitlab
from gitlab.v4.objects import Project, ProjectPipeline, ProjectMergeRequest
from cookiecutter.main import cookiecutter
from pathlib import Path

from datetime import datetime
import time
from git import GitCommandError, Repo, Reference
from hamcrest import assert_that, empty, not_, none, equal_to, is_not, \
    all_of, has_item
from loguru import logger

GITLAB_CONFIG_ERROR_MESSAGE = """

##### GITLAB credentials not setup/configured #####

# When running from Github Actions

You need to setup a `GITLAB_TOKEN` secret key.

# When running from your development machine (assuming you have access to the project's GitLab testing repos)

Please refer to https://python-gitlab.readthedocs.io/en/stable/cli.html#content
for more info.

Here is the approach we used:

- Credentials must be written in the `secrets/gitlab-python.cfg` file (which has
been added to the `.gitignore` file so it is excluded from the repo).

- The server used is the one declared as `default`.

- Here is an example of `secrets/gitlab-python.cfg` file:
```
[global]
default = gitlab_com
ssl_verify = true
timeout = 5

[gitlab_com]
url = https://gitlab.com
private_token = YOUR_ACCESS_TOKEN
```

"""

GIT_CONFIG_ERROR_MESSAGE = """

##### GIT credentials not setup/configured #####

# When running from Github Actions

You need to setup a `GITLAB_TOKEN` secret key.

# When running from your development machine (assuming you have access to the project's GitLab testing repos)

Please refer to https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage
for more info.

Here is the approach we used:

- use the 'store' mode by running the command line:
```
$ git config --global credential.helper 'store --file ~/.git-credentials'
```

- update your `~/.git-credentials` with: `https://YOUR_USERNAME:YOUR_ACCESS_TOKEN@gitlab.com`

"""


def test_gitlab_pipeline(tmp_path):
    gitlab_client = initialise_gitlab_client()

    hosting_namespace = "opinionated-digital-center/testing-area"
    project_long_title = "Python library project generator GitLab pipeline test"
    project_slug = project_long_title.lower().replace(" ", "-")

    gitlab_project = gitlab_client.projects.get(f"{hosting_namespace}/{project_slug}")
    logger.debug(f"Working with GitLab project {gitlab_project.web_url}")
    repo = initialise_git_repo(gitlab_project.http_url_to_repo, tmp_path / project_slug)

    start_time = datetime.now()
    start_time_str = start_time.strftime("%y-%m-%d_%Hh%M-%S_%f")

    branch = pull_and_prepare_branch(repo, start_time_str)

    cookiecutter(
        ".",
        extra_context={
            "project_title": "Generated Python Project GitLab",
            "project_slug": project_slug,
            "hosting_namespace": hosting_namespace,
            "pypi_hosting": "TestPyPi",
        },
        no_input=True,
        default_config=True,
        overwrite_if_exists=True,
        output_dir=tmp_path,
    )

    commit_changes_and_push(repo, branch, start_time_str)

    merge_request = gitlab_project.mergerequests.create(
        {
            "source_branch": branch.name,
            "target_branch": "master",
            "title": f"Test on {start_time.strftime('%Y-%m-%d %H:%M:%S.%f')}",
        }
    )

    mr_pipeline_id = verify_merge_request_pipeline_created(merge_request)

    verify_pipeline_succeeded(gitlab_project.pipelines.get(mr_pipeline_id))

    merge_request.merge()

    pipeline_id = verify_post_merge_pipeline_created(gitlab_project, merge_request)

    pipeline = gitlab_project.pipelines.get(pipeline_id)
    verify_pipeline_succeeded(pipeline)

    release_number = verify_release_created(gitlab_project, pipeline)

    verify_package_published_to_pypi(project_slug, release_number)


def initialise_gitlab_client() -> gitlab.Gitlab:
    gitlab_client = None
    try:
        gitlab_client = gitlab.Gitlab("https://gitlab.com",
                                      private_token=os.environ["GITLAB_TOKEN"])
    except KeyError:
        logger.debug("Environment variable GITLAB_TOKEN not present")
        try:
            local_config_file = Path("secrets", "gitlab-python.cfg")
            gitlab_client = gitlab.Gitlab.from_config(
                config_files=[local_config_file]
            )
        except gitlab.config.GitlabConfigMissingError:
            logger.debug(
                f"File '{local_config_file}' non existant"
            )
            try:
                gitlab_client = gitlab.Gitlab.from_config()
            except gitlab.config.GitlabConfigMissingError:
                logger.debug("No GitLab config file found")
            else:
                logger.debug(f"GitLab configured with system config file")
        else:
            logger.debug(
                f"GitLab configured with local config file at"
                f" '{local_config_file.absolute()}'"
            )
    else:
        logger.debug(
            f"GitLab configured with environment variable "
            f"GITLAB_TOKEN={os.environ['GITLAB_TOKEN']}"
        )

    assert_that(gitlab_client, not_(none()), GITLAB_CONFIG_ERROR_MESSAGE)

    return gitlab_client


def initialise_git_repo(repo_url: str, path: Path) -> Repo:
    repo = Repo.clone_from(repo_url, path)

    try:
        repo.git.config(
            "credential.helper",
            "!f() { "
            "sleep 1; "
            f"echo \"username={os.environ['PIPELINE_GIT_NAME']}\"; "
            f"echo \"password={os.environ['PIPELINE_GIT_PASSWORD']}\"; "
            "}; f",
            local=True,
        )
    except KeyError:
        logger.debug(
            "Environment variable PIPELINE_GIT_NAME and/or "
            "PIPELINE_GIT_PASSWORD not present"
        )

        local_config_file = Path("secrets", ".git-credentials")
        if not local_config_file.exists():
            logger.debug(
                f"Local Git credential file not present either at "
                f"'{local_config_file.absolute()}' "
                f"=> no way to set up Git credentials"
            )
            assert False

        repo.git.config(
            "credential.helper",
            f"store --file {local_config_file.absolute()}",
            local=True,
        )
        logger.debug(
            f"GitLab configured with local config file at "
            f"'{local_config_file.absolute()}'"
        )
    else:
        logger.debug(
            f"Local git credentials configured with environment variables "
            f"PIPELINE_GIT_NAME={os.environ['PIPELINE_GIT_NAME']} and "
            f"PIPELINE_GIT_PASSWORD={os.environ['PIPELINE_GIT_PASSWORD']}"
        )

    return repo


def pull_and_prepare_branch(repo: Repo, start_time_str: str) -> Reference:
    branch_name = f"b_{start_time_str}"
    logger.debug(f"Working with branch name '{branch_name}'")
    branch = repo.create_head(branch_name)

    branch.checkout()
    repo.git.rm("-r", ".", ":!CHANGELOG.md")
    repo.index.commit("remove all")

    return branch


def commit_changes_and_push(repo: Repo, branch, start_time_str: str) -> None:
    # add all file to index
    repo.git.add(all=True)
    repo.index.commit("added new")

    # squash the commits
    repo.git.reset("HEAD~2", soft=True)
    repo.index.commit(f"feat: {start_time_str}")

    # push
    try:
        repo.git.push("--set-upstream", "origin", branch.name)
    except GitCommandError as e:
        if e.status == 128:
            assert False, GIT_CONFIG_ERROR_MESSAGE
        else:
            raise e


def verify_pipeline_succeeded(pipeline: ProjectPipeline) -> None:
    while pipeline.finished_at is None:
        time.sleep(5.)
        pipeline.refresh()
        assert_that([job.status for job in pipeline.jobs.list()],
                    all_of(not_(has_item("failed")), not_(has_item("canceled"))))

    assert_that(pipeline.status, equal_to('success'))


def verify_merge_request_pipeline_created(merge_request: ProjectMergeRequest) -> int:
    pipelines = []
    start_time = time.time()
    timeout = 10

    while not pipelines and time.time() < start_time + timeout:
        time.sleep(5.)
        pipelines = merge_request.pipelines()

    assert_that(pipelines, is_not(empty()),
                f"No pipelines found for merge request "
                f"after a timeout of {timeout} seconds.")

    return pipelines[0]["id"]


def verify_post_merge_pipeline_created(gitlab_project: Project,
                                       merge_request: ProjectMergeRequest) -> int:
    commit_sha = merge_request.merge_commit_sha
    if commit_sha is None:
        commit_sha = merge_request.squash_commit_sha
    if commit_sha is None:
        commit_sha = merge_request.sha

    pipelines = []
    start_time = time.time()
    timeout = 10

    while not pipelines and time.time() < start_time + timeout:
        time.sleep(5.)
        pipelines = gitlab_project.pipelines.list(ref="master", sha=commit_sha)

    assert_that(pipelines, is_not(empty()),
                f"No pipelines found for ref 'master' and sha '{commit_sha}' "
                f"after a timeout of {timeout} seconds.")

    return pipelines[0].id


def verify_release_created(gitlab_project: Project, pipeline: ProjectPipeline) -> str:
    release_number = None

    for release in gitlab_project.releases.list():
        if release.name.startswith("v") \
            and pipeline.created_at < release.released_at < pipeline.updated_at:
            release_number = release.tag_name[1:]
            break
    assert_that(release_number, not_(none()))
    return release_number


def verify_package_published_to_pypi(pypi_name: str, release_number: str) -> None:
    testpypi_package_version = ""
    start_time = time.time()
    timeout = 30

    while testpypi_package_version != release_number and time.time() < start_time + timeout:
        time.sleep(2.)
        testpypi_package_info = urllib.request.urlopen(
            f"https://test.pypi.org/pypi/{pypi_name}/json"
        ).read()
        testpypi_package_version = json.loads(testpypi_package_info)['info']['version']

    assert_that(testpypi_package_version, equal_to(release_number))
