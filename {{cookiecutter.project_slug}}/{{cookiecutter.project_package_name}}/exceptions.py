"""All package specific exceptions."""


class {% for x in cookiecutter.project_package_name.split("_") -%}
{{ x.capitalize() }}
{%- endfor %}Error(Exception):
    """
    Base exception for errors raised by
    {{ cookiecutter.project_package_name }}.
    """
