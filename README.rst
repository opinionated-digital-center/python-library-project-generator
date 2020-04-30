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

  * `GitLab-CI`_ pipeline elements. (available soon)
  * `Make`_ targets. (available soon)

The argumentation behind the Opinionated Digital Center's choices (for this and other
projects) are/will be gradually documented as Architecture Decision Records, either
on `ODC's ADR repository <https://github.com/opinionated-digital-center/architecture-decision-record>`_
for transversal decisions, or on each individual repository's ``docs/adr`` directory
(`here <docs/adr>`_ for this project) for project related decisions.


Fully tested features
---------------------
All the features of this template are fully tested through CI/CD pipelines, including:

* The `Test and make release <https://github.com/opinionated-digital-center/python-library-project-generator/actions?query=workflow%3A%22Test+and+make+release%22>`_
  pipeline to:

  * Generate projects for each options of the template.
  * Run the project's built-in tests and checks for each option specifically.
  * Upon success, release a new version of the template.

* The `Test GitLab Pipeline <https://github.com/opinionated-digital-center/python-library-project-generator/actions?query=workflow%3A%22Test+GitLab+Pipeline%22>`_
  pipeline (GitHub available soon) to:

  * Generate a project with the default options.
  * Test that the generated project's GitLab pipeline runs successfully, including:

    * Run the project's built-in tests and checks on the project's pipeline.
    * Automatically bump the package's version following
      `ADR-0003: Use Semantic Versioning <https://github.com/opinionated-digital-center/architecture-decision-record/blob/master/docs/adr/0003-use-semantic-versioning.md>`_,
      based on commit messages following
      `ADR-0005: Use Conventional Commits <https://github.com/opinionated-digital-center/architecture-decision-record/blob/master/docs/adr/0005-use-conventional-commits.md>`_).
    * Generate the release notes.
    * Publish the release on GitLab.
    * Publish the released package to the package repository.


Features list
-------------
Projects initialised with the template will benefit straight away from the following
out-of-the-box and ready to use features: (note: external environments like
GitLab-CI_, the package repository and documentation host will require to be set up
separately)

* Unit testing with Pytest_ (default) or UnitTest_.
* BDD/Functional testing with Behave_ (includes functional cli testing with
  `Behave4cli`_).
* Linting/Style guide enforcement with Flake8_.
* "Uncompromising" formatting and automated import sorting with Black_ & isort_.
* Static typing with Mypy_.
* Code coverage with Coverage_.
* Packaging and dependency management with Poetry_.
* Python versions management to install multiple versions on your host with Pyenv_.
* Task management centralisation with Make_, for all your tasks:

  * For setup (development environment and machine, CI/CD pipeline job and tasks
    launch).
  * For test tasks.
  * For the whole development and release lifecycle.

* Local, multi-version testing automation with Tox_.
* CI-CD pipeline with GitLab-CI_ and `GitHub Actions`_ (available soon), including:

  * A test phase running all tests in parallel jobs.
  * A release phase (see Release cycle below).
  * Caching (available soon).

* Release cycle with Semantic-release_, including:

  * Automatically bump the package's version following
    `ADR-0003: Use Semantic Versioning <https://github.com/opinionated-digital-center/architecture-decision-record/blob/master/docs/adr/0003-use-semantic-versioning.md>`_,
    based on commit messages following
    `ADR-0005: Use Conventional Commits <https://github.com/opinionated-digital-center/architecture-decision-record/blob/master/docs/adr/0005-use-conventional-commits.md>`_).
  * Generate the release notes.
  * Publish the release on GitLab/GitHub.
  * Publish the released package to the package repository.

* Command line interface (optional), with testing, using Cleo_ (default), Click_ or
  Argparse_.
* Documentation generation with Sphinx_.
* Documentation publishing to `Read the Docs`_ (publishing to GitLab and GitHub Pages
  avaible soon).


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

* Generate a Python package project for the template::

    $ cd your/projects/root/dir
    $ cookiecutter https://github.com/opinionated-digital-center/python-library-project-generator


* Move to your newly created project's directory, initialise its ``git`` repo. Here
  we also commit the generated code::

    $ cd <your-project>
    $ git init .
    $ git add --all .
    $ git commit -m 'chore: initial commit'

* Set up you development environment::

    # Full setup (installs all testing and check libraries and allows for IDE completion)
    $ make setup-dev-env-full


    # Or alternatively, minimal setup (installs ``tox`` and formatting libraries only)
    $ make setup-dev-env-minimal

Hosting and pipeline setup
~~~~~~~~~~~~~~~~~~~~~~~~~~

Hosting setup
+++++++++++++

* Create a repo on GitHub or GitLab (cloud or sefl-hosted).
* Push your local repo to it::

    $ git remote add origin https://<hosting-domain>/<your-namespace>/<your-project>.git
    $ git push -u origin master

GitLab CI specific setup
++++++++++++++++++++++++

.. |ss| raw:: html

   <strike>

.. |se| raw:: html

   </strike>

* Configure your GitLab CI project environment variables
  (`doc <https://docs.gitlab.com/ee/ci/variables/#types-of-variables>`_)
  with the following variables:

  * For GitLab publishing, follow the `doc for @semantic-release/gitlab <https://github.com/semantic-release/gitlab#configuration>`_, and set:

    * ``GITLAB_TOKEN`` (don't forget to `mask
      <https://docs.gitlab.com/ee/ci/variables/#masked-variables>`_ it).
    * ``GITLAB_URL`` (optional - see doc).
    * ``GITLAB_PREFIX`` (optional - see doc).

  * For package publishing:

    * ``PYPI_REPOSITORY_NAME`` (only needed if you are using a repository other
      than ``pypi``): ``name`` for your Python package repository.

      ``name`` can only contain alphanumerical characters, "``.``", "``-``"
      and "``_``" (for example: ``my-repository`` or ``my.repository`` or
      ``my_repository``).

      In the remaining environment variables, ``<NAME>`` is to be replaced by
      this repository's name, in UPPERCASE, with "``.``" and "``-``"
      replaced by "``_``" (for instance ``my-repository`` or ``my.repository`` or
      ``my_repository`` all become ``MY_REPOSITORY``).

    * ``POETRY_REPOSITORIES_<NAME>_URL`` (required if repository is not ``pypi``): URL of
      the repository.

    * One of the following credential mechanism has to be set (http basic will take
      precedence if set):

      * Http basic credential:

        * ``POETRY_HTTP_BASIC_<NAME>_USERNAME``: username credential for repository
          ``name``
        * ``POETRY_HTTP_BASIC_<NAME>_PASSWORD``: password credential for repository
          ``name``

      * API token credential :

        * ``POETRY_PYPI_TOKEN_<NAME>``: |ss| API token credential for repository
          ``name``. |se| =>
          `there is currently an issue <https://github.com/python-poetry/poetry/issues/2210>`_
          with setting API tokens through environment variables. As a workaround,
          use:

          * ``POETRY_HTTP_BASIC_<NAME>_USERNAME=__token__``
          * ``POETRY_HTTP_BASIC_<NAME>_PASSWORD=<your_api_token>``.

* Release your package by
  `running a manual pipeline on your master branch <https://docs.gitlab.com/ee/ci/pipelines/#manually-executing-pipelines>`_.

GitHub Actions specific setup
+++++++++++++++++++++++++++++

COMING SOON.

Python package repository
+++++++++++++++++++++++++

* Follow the doc for your specific package repository (self-hosted, PyPi, TestPyPi,
  other).
* Set up the environment variables as described in pipelines setup instructions above.

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, we encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

We also accept pull requests on this, if they're small, atomic, and if they
make our own packaging experience better.


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
.. _Argparse: https://docs.python.org/3/library/argparse.html
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
