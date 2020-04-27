from cookiecutter.main import cookiecutter
from hamcrest import assert_that, empty, is_, not_

IGNORED_FILES = [
    ".DS_Store",
    ".flake8",
    ".pre-commit-config.yaml",
    "mypy.ini",
    "scripts/install_pyenv.sh",
    "scripts/install_poetry.sh",
    "behave4cmd0/README.txt",
    "tests/test_generated_python_project_gitlab.py",
]
IGNORED_CONTENT = [
    "github.com/pyenv/",
    "githubusercontent.com/sdispater/",
    "github.com/python-poetry/",
    "github.com/lumengxi/",
    "github.com/thejohnfreeman/",
    "github.com/python/",
    "github.com/psf/",
    "github.com/audreyr/",
    "github.com/opinionated-digital-center/python-library-project-generator",
    "github.com/conventional-changelog",
]


def test_no_github_in_gitlab_generated_project(tmp_path):
    project_title = "Generated Python Project GitLab"
    project_slug = project_title.lower().replace(" ", "-")

    cookiecutter(
        ".",
        extra_context={"project_title": project_title},
        no_input=True,
        default_config=True,
        overwrite_if_exists=True,
        output_dir=tmp_path,
    )

    project_path = tmp_path / project_slug

    files_to_test = [path for path in project_path.glob("**/*") if path.is_file()]
    assert_that(files_to_test, not_(empty()))

    files_to_test = filter_out_ignored_files(files_to_test, project_path)

    files_containing_github = extract_files_containing_github(files_to_test,
                                                              project_path)

    assert_that(files_containing_github, empty())
    assert_that((project_path / ".github").exists(), is_(False))


def filter_out_ignored_files(files_to_test, project_path):
    files_to_test = [
        path for path in files_to_test
        if str(path.relative_to(project_path)) not in IGNORED_FILES and
           path.is_file()
    ]
    return files_to_test


def extract_files_containing_github(paths_to_test, project_path):
    files_containing_github = []

    for file in paths_to_test:
        with file.open() as f:
            file_content = f.read()

        for ignored_content_item in IGNORED_CONTENT:
            file_content = file_content.replace(ignored_content_item, "")

        if "github" in file_content.lower():
            files_containing_github.append(str(file.relative_to(project_path)))

    return files_containing_github
