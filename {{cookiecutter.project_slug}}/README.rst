{% set is_open_source = cookiecutter.open_source_license != "Not open source" -%}

==============={% for _ in cookiecutter.project_title %}={% endfor %}
Introdution to {{ cookiecutter.project_title }}
==============={% for _ in cookiecutter.project_title %}={% endfor %}

{% if cookiecutter.hosting == "GitLab" -%}
.. image:: {{ cookiecutter.hosting_repo_url }}/badges/master/pipeline.svg
    :target: {{ cookiecutter.hosting_repo_url }}/pipelines

{% endif -%}
{% if is_open_source -%}
{% if cookiecutter.pypi_hosting == "PyPi" -%}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.org/project/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.org/project/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.org/project/{{ cookiecutter.project_slug }}

{% endif -%}
.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

{% if cookiecutter.pypi_hosting == "TestPyPi" -%}
Project `published on TestPyPi <https://test.pypi.org/project/{{ cookiecutter.project_slug }}>`_.

{% endif -%}
{% endif -%}

{{ cookiecutter.project_short_description }}

{% if is_open_source -%}
* Free software license: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug}}.readthedocs.io
{%- endif %}

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the
`opinionated-digital-center/python-library-project-generator`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`opinionated-digital-center/python-library-project-generator`: https://github.com/opinionated-digital-center/python-library-project-generator
