.. highlight:: shell

============
Installation
============


Stable release
--------------

To install {{ cookiecutter.project_title }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

This is the preferred method to install {{ cookiecutter.project_title }}, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ cookiecutter.project_title }} can be downloaded
from the `{{cookiecutter.hosting}} repo`_.

Clone the public repository:

.. code-block:: console

    $ git clone {{ cookiecutter.hosting_repo_url }}.git

Then install it with:

.. code-block:: console

    $ cd {{ cookiecutter.project_slug }}
    $ POETRY_VIRTUALENVS_CREATE=FALSE poetry install


.. _{{ cookiecutter.hosting }} repo: {{ cookiecutter.hosting_repo_url }}
