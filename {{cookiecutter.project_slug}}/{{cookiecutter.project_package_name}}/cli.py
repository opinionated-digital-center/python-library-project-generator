"""Console script for {{cookiecutter.project_package_name}}."""

import sys
{% if cookiecutter.command_line_interface|lower == "cleo" %}
import cleo
{% elif cookiecutter.command_line_interface|lower == "click" %}
import click
{% endif -%}

{% if cookiecutter.command_line_interface|lower == "cleo" %}
from . import __version__
{%- endif %}
from .core import hello_world

{%- if cookiecutter.command_line_interface|lower == "cleo" %}


class HelloCommand(cleo.Command):
    """
    First Command

    hello
    """

    def handle(self):
        self.line(hello_world())


class Application(cleo.Application):
    def __init__(self):
        super().__init__("{{ cookiecutter.project_title }}", __version__)

        self.add(HelloCommand())


def main(args=None):
    return Application().run()
{%- elif cookiecutter.command_line_interface|lower == "click" %}


@click.group()
def main(args=None):
    """Console script for a_generated_python_project."""
    return 0


@main.command()
def hello():
    click.echo(hello_world())
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
