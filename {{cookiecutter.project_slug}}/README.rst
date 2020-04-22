{% set is_open_source = cookiecutter.open_source_license != "Not open source" -%}
{% for _ in cookiecutter.project_title %}={% endfor %}
{{ cookiecutter.project_title }}
{% for _ in cookiecutter.project_title %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.hosting_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.com/{{ cookiecutter.hosting_username }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

{% if cookiecutter.add_pyup_badge == "y" %}
.. image:: https://pyup.io/repos/{{ cookiecutter.hosting.lower() }}/{{ cookiecutter.hosting_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/{{ cookiecutter.hosting.lower() }}/{{ cookiecutter.hosting_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates
[{% endif %}
]

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software license: {{ cookiecutter.open_source_license }}
{% endif %}* Documentation: https://{{ cookiecutter.project_slug}}.readthedocs.io

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `opinionated-digital-center/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`opinionated-digital-center/cookiecutter-pypackage`: https://github.com/opinionated-digital-center/python-library-project-generator
