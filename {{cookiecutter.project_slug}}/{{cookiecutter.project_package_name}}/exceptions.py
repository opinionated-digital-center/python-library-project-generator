"""All package specific exceptions"""


class {{ cookiecutter.project_package_name.capitalize() }}Error(Exception):
    """
    Base exception for errors raised by
    {{ cookiecutter.project_package_name }}
    """
