===========================================
Opinionated Python Library Project Template
===========================================

.. image:: https://gitlab.com/opinionated-digital-center/cookiecutter-pypackage/badges/master/pipeline.svg
    :target: https://gitlab.com/opinionated-digital-center/cookiecutter-pypackage/pipelines
    :alt: Linux build status on GitLab CI

* {{ cookiecutter.hosting }} repo: {{ cookiecutter.hosting_repo_url }}
* Free software: MIT license

Features
--------
Fully working scaffold with the following out-of-the-box and running features (although
external environments like GitLab-CI_, PyPI_ and `Read the Docs`_ require to be set up
separately):

* Pytest_: Unit tests
* Behave_: BDD/Functional tests
* Flake8_: Linting/Style guide enforcement
* Black_ & isort_: Uncompromising formatting and automated import sorting
* Mypy_: Static typing
* Coverage_: Code coverage
* Poetry_: Easy packaging and dependency management, set up to isolate the different
  test dependencies (unit tests, bdd, ...) for speedy test runs
* Pyenv_: Simple Python version management to install multiple versions on your host
* Make_: Used as single doorway to all your tasks:

  * For setup (development environment and machine, CI/CD pipeline job environments)
  * For test tasks
  * For the whole development and release lifecycle

* Tox_ testing: Set up to easily test for Python 3.6, 3.7, 3.8 and used as single source
  for all your test invocations
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_
* GitLab-CI_: CI-CD pipeline with:

  * Test phase running all tests in parallel jobs
  * Release phase (see semantic-release below)

* Semantic-release_: Pre-configured version bumping, changelog generation, auto-release
  to PyPI_ and GitLab (yes... not a Python written tool... but works *really* well and
  has way more advanced features than any of the existing Python tools)
* Command line interface (optional) using Cleo_ (default), Click_ or Argparse_


Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher; see the `installation doc
<https://cookiecutter.readthedocs.io/en/latest/installation.html>`_ for more details)::

    # On macOS
    $ brew install cookiecutter

    # On linux and other systems
    $ pip install -U cookiecutter

Generate a Python package project (follow the instructions)::

    $ cd your/projects/root/dir
    $ cookiecutter https://github.com/opinionated-digital-center/cookiecutter-pypackage.git

Then:

* Move to your newly created project's directory, initialise its `git` repo. Here
  we also commit the generated code::

    $ cd <your-project>
    $ git init .
    $ git add .
    $ git commit -m 'chore: initial commit'

* If you have not installed Pyenv_ and Poetry_ on your machine yet, you can use the
  following ``make`` target to do so::

    $ make setup-dev-host

  Don't forget to restart your shell or source your shell configuration file.
  For example for Bash::

    $ source ~/.bashrc

  You might want to tell Poetry to create your virtualenvs in your project directory
  (makes it easier to add the virtualenv to your IDE)::

    $ poetry config virtualenvs.in-project true

* Set up you development environment::

    # Minimal setup

    $ make setup-dev-env-minimal

    # OR alternatively, full setup (allows for IDE completion)

    $ make setup-dev-env-full

* Create a repo on GitHub or GitLab (cloud or hosted) and push your local repo to it.
* If you did not use GitLab for hosting your project, you need to
  `create a pipeline on GitLab.com
  <https://docs.gitlab.com/ee/ci/ci_cd_for_external_repos/>`_.

.. |ss| raw:: html

   <strike>

.. |se| raw:: html

   </strike>

* Configure your `GitLab CI project environment variables <https://docs.gitlab.com/ee/ci/variables/#types-of-variables>`_ with the following variables:

  * For GitLab publishing, follow the `doc for @semantic-release/gitlab <https://github.com/semantic-release/gitlab#configuration>`_, and set:

    * ``GITLAB_TOKEN``: Don't forget to `mask
      <https://docs.gitlab.com/ee/ci/variables/#masked-variables>`_ it.
    * ``GITLAB_URL`` (optional - see doc).
    * ``GITLAB_PREFIX`` (optional - see doc).

  * For Pypi_ publishing (requires you to `register your project with PyPI`_ first or
    with any other equivalent Python package repository):

    * ``PYPI_REPOSITORY_NAME`` (only needed if you are using a repository other
      than ``pypi``): ``name`` for your Python package repository.

      ``name`` can only contain alphanumerical characters, "``.``", "``-``"
      and "``_``" (for example: ``my-repository`` or ``my.repository`` or
      ``my_repository``).

      In the remaining environment variables, ``<NAME>`` is to be replaced by
      this repository's name, in uppercase, with "``.``" and "``-``"
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

.. _register your project with PyPI: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives


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
make my own packaging experience better.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter/
.. _Pytest: https://docs.pytest.org/en/latest/
.. _Behave: https://behave.readthedocs.io/en/latest/
.. _Flake8: https://flake8.pycqa.org/en/latest/
.. _Black: https://black.readthedocs.io/en/stable/
.. _isort: https://timothycrosley.github.io/isort/
.. _Mypy: http://mypy-lang.org/
.. _Coverage: https://coverage.readthedocs.io/en/latest/
.. _Make: https://www.gnu.org/software/make/
.. _Poetry: https://python-poetry.org/
.. _Pyenv: https://github.com/pyenv/pyenv/wiki
.. _GitLab-CI: https://docs.gitlab.com/ee/ci/
.. _Travis-CI: http://travis-ci.org/
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
