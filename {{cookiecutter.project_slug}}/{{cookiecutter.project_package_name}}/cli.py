"""Console script for {{cookiecutter.project_package_name}}."""

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'cleo' %}

import cleo

from . import __version__
{%- elif cookiecutter.command_line_interface|lower == 'click' %}

import click
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'cleo' %}
class HelloCommand(cleo.Command):
    """
    First Command

    hello
    """

    def handle(self):
        self.line(
            "Replace this message by putting your code into "
            "{{ cookiecutter.project_package_name }}.cli.main)"
        )
        self.line("See cleo documentation at https://cleo.readthedocs.io/en/latest/")

class Application(cleo.Application):
    def __init__(self):
        super().__init__("{{ cookiecutter.project_name }}", __version__)

        self.add(HelloCommand())

def main(args=None):
    return Application().run()
{% elif cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_package_name}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_package_name}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    """Console script for {{cookiecutter.project_package_name}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.project_package_name}}.cli.main")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
