===========================================
Opinionated Python Library Project Template
===========================================

.. image:: https://github.com/opinionated-digital-center/python-library-project-generator/workflows/Test%20and%20make%20release/badge.svg
    :target: https://github.com/opinionated-digital-center/python-library-project-generator/actions?query=workflow%3A%22Test+and+make+release%22

.. image:: https://github.com/opinionated-digital-center/python-library-project-generator/workflows/Test%20GitLab%20Pipeline/badge.svg
    :target: https://github.com/opinionated-digital-center/python-library-project-generator/actions?query=workflow%3A%22Test+GitLab+Pipeline%22

* GitHub repo: https://github.com/opinionated-digital-center/python-library-project-generator .
* Free software: MIT license.

The "Opinionated Python Library Project Template" is a fully tested, feature rich
`Cookiecutter`_ scaffold to kick start your Python library and command line interface
development.

It is "opinionated" as it reflects strong structural and tooling choices,
which we believe help developers being more effective within Digital Centers. It can
however seamlessly be used for Open Source development (works also out-of-the-box with
`gitlab.com <https://gitlab.com>`_, `github.com <https://github.com>`_,
`pypi.org <https://pypi.org>`_ and `readthedocs.org <https://readthedocs.org>`_,
as a standalone project).

In addition to the intrinsic features offered by the template (see `Features list`_
below), the specific features that make it suitable and effective for Digital Centers
are the abilities to:

* Use self-hosted GitLab and GitHub.
* Publish to self-hosted package repositories.
* Reuse centralised and optimised "toolbox" items, such as:

  * GitLab-CI `pipeline templates <https://gitlab.com/opinionated-digital-center/gitlab-ci-templates/python-library/-/tree/master/templates>`_.
  * Centralised (and expandable) `Make`_ targets. (available soon)

The argumentation behind the Opinionated Digital Center's choices (for this and other
projects) are/will be gradually documented as Architecture Decision Records, either
on `ODC's ADR repository <https://github.com/opinionated-digital-center/architecture-decision-record>`_
for transversal decisions, or on each individual repository's ``docs/adr`` directory
(`here <docs/adr>`_ for this project) for project related decisions.


Fully tested features
---------------------
All the features of this template are fully tested through CI/CD pipelines, including:

* The `Test and make release <https://github.com/opinionated-digital-center/python-library-project-generator/actions?query=workflow%3A%22Test+and+make+release%22>`_
  pipeline, which does:

  * Generate projects for each options of the template.
  * Run the project's built-in tests and checks for each option specifically.

* The `Test GitLab Pipeline <https://github.com/opinionated-digital-center/python-library-project-generator/actions?query=workflow%3A%22Test+GitLab+Pipeline%22>`_
  pipeline (GitHub available soon), which does:

  * Generate a project with the default options.
  * Push the result to the
    `pipeline test project on gitlab.com <https://gitlab.com/opinionated-digital-center/testing-area/python-library-project-generator-gitlab-pipeline-test>`_.
  * Create a Merge Request.
  * Verify the Merge Request's pipeline runs successfully, validating the project's
    tests and checks.
  * Merge the Merge Request.
  * Verify that the post-merge pipeline successfully creates and publishes a release,
    which includes:

    * Automatically bump the package's version following
      `ADR-0003: Use Semantic Versioning <https://github.com/opinionated-digital-center/architecture-decision-record/blob/master/docs/adr/0003-use-semantic-versioning.md>`_,
      based on commit messages following
      `ADR-0005: Use Conventional Commits <https://github.com/opinionated-digital-center/architecture-decision-record/blob/master/docs/adr/0005-use-conventional-commits.md>`_.
    * Generate the `release notes <https://gitlab.com/opinionated-digital-center/testing-area/python-library-project-generator-gitlab-pipeline-test/-/blob/master/CHANGELOG.md>`_.
    * Publish the `release on GitLab <https://gitlab.com/opinionated-digital-center/testing-area/python-library-project-generator-gitlab-pipeline-test/-/releases>`_.
    * Publish the `released package to the TestPyPI package repository <https://test.pypi.org/project/python-library-project-generator-gitlab-pipeline-test/>`_.
    * (Also published but not tested: the project's `generated doc on Read The Docs <https://python-library-project-generator-gitlab-pipeline-test.readthedocs.io/>`_).

* The Test GitHub Actions workflow (available soon).


Features list
-------------
Projects initialised with the template will benefit straight away from the following
out-of-the-box and ready to use features (*Note:* external environments like
GitLab-CI_, the Python package repository and the documentation host will require to be
set up separately):

* Packaging and dependency management with Poetry_.
* Local, multi-version testing automation with Tox_.
* Unit testing with Pytest_ (default) or UnitTest_.
* BDD/Functional testing with Behave_ (includes functional cli testing with
  `Behave4cli`_).
* Linting/Style guide enforcement with Flake8_.
* "Uncompromising" formatting with Black_
* Automated import sorting with isort_.
* Static typing with Mypy_.
* Code coverage with Coverage_.
* Task management centralisation with Make_, for all your tasks:

  * For setup (development host, project environment, CI/CD pipeline jobs).
  * For test and CI/CD job tasks.
  * For the whole development and release lifecycle.

* Pre-commit hooks for enforcing specific checks before committing with
  `pre-commit`_.
* CI-CD pipeline with GitLab-CI_ and `GitHub Actions`_ (available soon), including:

  * A test stage running all tests in parallel jobs.
  * A release stage (see Release cycle immediately below).
  * Caching (available soon).

* Release cycle with Semantic-release_, including:

  * Automatically bump the package's version following
    `ADR-0003: Use Semantic Versioning <https://github.com/opinionated-digital-center/architecture-decision-record/blob/master/docs/adr/0003-use-semantic-versioning.md>`_,
    based on commit messages following
    `ADR-0005: Use Conventional Commits <https://github.com/opinionated-digital-center/architecture-decision-record/blob/master/docs/adr/0005-use-conventional-commits.md>`_).
  * Generate the release notes.
  * Publish the release on the chosen hosting (GitLab or GitHub, cloud or self-hosted).
  * Publish the released package to the chosen Python package repository.

* Command line interface (optional), with testing, using Cleo_ (default) or Click_.
* Documentation generation with Sphinx_.
* Documentation publishing to `Read the Docs`_ (publishing to GitLab and GitHub Pages
  planned).

On our development machines, we use Pyenv_ to install and manage multiple versions of
Python (``make`` target available to facilitate installation).


Quickstart
----------

Prerequisites
~~~~~~~~~~~~~

Cookiecutter installation
+++++++++++++++++++++++++

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher; see the `installation doc
<https://cookiecutter.readthedocs.io/en/latest/installation.html>`_ for more details)::

    # On macOS
    $ brew install cookiecutter

    # On linux and other systems
    $ pip install -U cookiecutter

PyEnv and Poetry installation
+++++++++++++++++++++++++++++

* If you have not installed Pyenv_ and Poetry_ on your machine yet, you can use the
  following ``make`` target to do so::

    $ make setup-dev-host

  Don't forget to restart your shell or source your shell configuration file.
  For example for Bash::

    $ source ~/.bashrc


* You might want to tell Poetry to create virtual environments in the project
  directories (makes it easier to add the virtualenv to your IDE)::

    $ poetry config virtualenvs.in-project true

Project initialisation and development setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Generate a project scaffold from the template::

    $ cd your/projects/root/dir
    $ cookiecutter https://github.com/opinionated-digital-center/python-library-project-generator
    # Follow the prompts
    [..]

* Move to your newly created project's directory, initialise its ``git`` repo and
  commit the generated code::

    $ cd <your-project>
    $ git init .
    $ git add --all .
    $ git commit -m 'chore: initial commit'

* Create an initial release tag, which will be used as a basis to bump upcoming
  releases. By convention, we use ``v0.0.0``::

    $ git tag v0.0.0

* Set up your project's environment::

    # Full setup (installs ``tox`` and all testing and checking libraries)
    $ make setup-dev-env-full


    # Or alternatively, minimal setup (installs ``tox`` and formatting libraries only)
    $ make setup-dev-env-minimal

* Set up pre-commit hooks to enforce minimal formatting checks before committing
  (which will otherwise cause the CI/CD pipeline to fail)::

    $ make setup-pre-commit-hooks

Hosting and pipeline setup
~~~~~~~~~~~~~~~~~~~~~~~~~~

Hosting setup
+++++++++++++

* Create a repo on GitHub or GitLab (cloud or self-hosted).
* Push your local repo to it::

    $ git remote add origin https://<hosting-domain>/<your-namespace>/<your-project>.git
    $ git push -u origin master

    # Also push the previously created tag
    $ git push --tags

GitLab CI specific setup
++++++++++++++++++++++++

.. |ss| raw:: html

   <strike>

.. |se| raw:: html

   </strike>

* Configure your
  `GitLab project environment variables <https://docs.gitlab.com/ee/ci/variables/#custom-environment-variables>`_
  with the following variables:

  * For release publishing to GitLab, follow
    `@semantic-release/gitlab's doc <https://github.com/semantic-release/gitlab#configuration>`_,
    and set:

    * ``GITLAB_TOKEN`` (don't forget to `mask
      <https://docs.gitlab.com/ee/ci/variables/#masked-variables>`_ it).
    * ``GITLAB_URL`` (optional - see doc).
    * ``GITLAB_PREFIX`` (optional - see doc).

  * For Python package publishing to your designated repository, set:

    * ``PYPI_REPOSITORY_NAME`` (only needed if you are using a repository other
      than ``pypi``): ``name`` for your Python package repository.

      ``name`` can only contain alphanumerical characters, "``.``", "``-``"
      and "``_``" (valid: ``my.foo-bar_repository``).

      In the remaining environment variables, ``<NAME>`` is to be replaced by
      this repository's name, in UPPERCASE, with "``.``" and "``-``"
      replaced by "``_``" (for instance ``my.foo-bar_repository`` becomes
      ``MY_FOO_BAR_REPOSITORY``).

    * ``POETRY_REPOSITORIES_<NAME>_URL`` (required if repository is not ``pypi``): URL of
      the repository.

    * One of the following credential mechanism has to be set (http basic will take
      precedence if set):

      * Http basic credential:

        * ``POETRY_HTTP_BASIC_<NAME>_USERNAME``: username credential for repository
          ``name``.
        * ``POETRY_HTTP_BASIC_<NAME>_PASSWORD``: password credential for repository
          ``name``.

      * API token credential :

        * |ss| ``POETRY_PYPI_TOKEN_<NAME>``: API token credential for repository
          ``name``. |se| =>
          `there is currently an issue <https://github.com/python-poetry/poetry/issues/2210>`_
          with setting API tokens through environment variables. As a workaround,
          use:

          * ``POETRY_HTTP_BASIC_<NAME>_USERNAME=__token__``.
          * ``POETRY_HTTP_BASIC_<NAME>_PASSWORD=<your_api_token>``.

* Release your first package by
  `running a manual pipeline on your master branch <https://docs.gitlab.com/ee/ci/pipelines/#run-a-pipeline-manually>`_.

GitHub Actions specific setup
+++++++++++++++++++++++++++++

(available soon)

Read The Docs setup
+++++++++++++++++++

* Follow the
  `Webhooks setup doc <https://docs.readthedocs.io/en/stable/webhooks.html>`_.


Usage
-----

Once you are all set up, you can use ``make`` targets to test and check your work
before pushing and opening a pull/merge request.

Here are a few useful, day-to-day targets::

    # Display help for targets
    $ make

    # Full project setup (installs ``tox`` and all testing and checking libraries)
    $ make setup-dev-env-full

    # Minimal project setup (installs ``tox`` and formatting libraries only)
    $ make setup-dev-env-minimal

    # Setup pre-commit hooks
    $ make setup-pre-commit-hooks

    # Run unit tests
    $ make test

    # Run bdd tests
    $ make bdd

    # Enforce correct format with black and isort
    $ make format

    # Check style with flake8
    $ make lint

    # Check Python typing
    $ make type

    # Run all tests and checks with tox
    $ make tox

    # Run tox target in parallel mode
    $ make tox-p

    # Generate Sphinx HTML documentation
    $ make docs

Contributing
------------

We accept pull requests on this, if they're small, atomic, and if they
make the packaging experience better (in our opinionated way, which can be discussed
and argued... :) ).


.. _Cookiecutter: https://github.com/audreyr/cookiecutter/
.. _Semantic Versioning: https://semver.org/
.. _Angular Commit Message Guideline: https://github.com/angular/angular/blob/13495c6/CONTRIBUTING.md#-commit-message-guidelines
.. _Conventional Commits specification: https://www.conventionalcommits.org/en/v1.0.0/
.. _Pytest: https://docs.pytest.org/en/latest/
.. _UnitTest: https://docs.python.org/3/library/unittest.html
.. _Behave: https://behave.readthedocs.io/en/latest/
.. _Behave4cli: https://gitlab.com/opinionated-digital-center/behave4cli
.. _Flake8: https://flake8.pycqa.org/en/latest/
.. _Black: https://black.readthedocs.io/en/stable/
.. _isort: https://timothycrosley.github.io/isort/
.. _Mypy: http://mypy-lang.org/
.. _Coverage: https://coverage.readthedocs.io/en/latest/
.. _Make: https://www.gnu.org/software/make/
.. _pre-commit: https://pre-commit.com/
.. _Poetry: https://python-poetry.org/
.. _Pyenv: https://github.com/pyenv/pyenv/wiki
.. _GitLab-CI: https://docs.gitlab.com/ee/ci/
.. _GitHub Actions: https://github.com/features#ci-cd
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _Read the Docs: https://readthedocs.io/
.. _Semantic-release: https://semantic-release.gitbook.io/
.. _Cleo: https://cleo.readthedocs.io/en/latest/
.. _Click: https://click.palletsprojects.com/
.. _Punch: https://github.com/lgiordani/punch
.. _PyPi: https://pypi.python.org/pypi
.. _Windows Subsystem for Linux: https://docs.microsoft.com/en-us/windows/wsl/about

.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _`tony/cookiecutter-pypackage-pythonic`: https://github.com/tony/cookiecutter-pypackage-pythonic
.. _`ardydedase/cookiecutter-pypackage`: https://github.com/ardydedase/cookiecutter-pypackage
.. _`lgiordani/cookiecutter-pypackage`: https://github.com/lgiordani/cookiecutter-pypackage
.. _`briggySmalls/cookiecutter-pypackage`: https://github.com/briggySmalls/cookiecutter-pypackage
.. _github comparison view: https://github.com/tony/cookiecutter-pypackage-pythonic/compare/audreyr:master...master
.. _`network`: https://github.com/audreyr/cookiecutter-pypackage/network
.. _`family tree`: https://github.com/audreyr/cookiecutter-pypackage/network/members
