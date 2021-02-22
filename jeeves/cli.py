from typing import Type

import typer
from dependencies import Injector, value

from jeeves.commands.find_packages import FindPackages
from jeeves.commands.flakehell import FlakeHell
from jeeves.commands.format import Format
from jeeves.commands.isort import Isort
from jeeves.commands.lint import Lint


class Jeeves(Injector):
    """Default Jeeves configuration."""

    # Helpers
    directories = FindPackages

    # Concrete tools
    isort = Isort
    flakehell = FlakeHell

    # Grouped tools
    lint = Lint
    format = Format

    # noinspection PyMethodParameters
    @value
    def linters(flakehell):
        return [flakehell]

    # noinspection PyMethodParameters
    @value
    def formatters(isort):
        return [isort]

    cli_commands = ['lint', 'format']


def create_app(injector: Type[Injector]):
    """Construct an app and register all commands."""
    typer_app = typer.Typer()

    # Get all registered attributes of the injector class.
    attributes = injector.cli_commands

    for attribute in attributes:
        cls = getattr(injector, attribute)
        if hasattr(cls, '__name__'):
            typer_app.command()(cls)

    return typer_app


app = create_app(Jeeves)


if __name__ == '__main__':
    app()
