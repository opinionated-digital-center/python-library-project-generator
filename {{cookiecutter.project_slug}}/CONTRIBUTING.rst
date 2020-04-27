{% set merge_or_pull = "merge" if cookiecutter.hosting == "GitLab" else "pull" -%}
{% set issues_suffix = "-/issues" if cookiecutter.hosting == "GitLab" else "issues" -%}
.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at {{ cookiecutter.hosting_repo_url }}/{{ issues_suffix }}.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the {{ cookiecutter.hosting }} issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the {{ cookiecutter.hosting }} issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

{{ cookiecutter.project_title }} could always use more documentation, whether as part of the
official {{ cookiecutter.project_title }} docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
{{ cookiecutter.hosting_repo_url }}/{{ issues_suffix }}.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up ``{{ cookiecutter.project_slug }}`` for local development on a Mac.

Prerequisite
~~~~~~~~~~~~

* python 3.6, 3.7 and 3.8 with `pyenv <https://github.com/pyenv/pyenv>`_

* `poetry <https://poetry.eustace.io/>`_

* `pre-commit <https://pre-commit.com/>`_ (optional but useful)

Setup (for Mac)
~~~~~~~~~~~~~~~

1. Fork the ``{{ cookiecutter.project_slug }}`` repo on {{ cookiecutter.hosting }}.
2. Clone your fork locally::

    $ git clone {{ cookiecutter.hosting_repo_url }}.git

3. Assuming you have the prerequisites installed, this is how you set up your fork for local development::

    $ cd {{ cookiecutter.project_slug }}/
    $ make setup-dev-env-full

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass typing, linting, formatting, unit tests
   (for all versions of Python) and functional (bdd) tests::

    $ make tox

.. note::

    See the Makefile help for all available targets.


6. Commit your changes and push your branch to {{ cookiecutter.hosting }}::

    $ git add .
    $ git commit -m "[feat|fix|chore|...]: your detailed description of your changes"
    $ git push --set-upstream origin name-of-your-bugfix-or-feature

7. Submit a {{ merge_or_pull }} request through the {{ cookiecutter.hosting }} website.

{{ merge_or_pull }} Request Guidelines
{% for _ in merge_or_pull %}-{% endfor %}-------------------

Before you submit a {{ merge_or_pull.capitalize() }} request, check that it meets these guidelines:

1. The {{ merge_or_pull }} request should include tests.
2. If the {{ merge_or_pull }} request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The {{ merge_or_pull }} request should pass on all tests and checks of the pipeline.
