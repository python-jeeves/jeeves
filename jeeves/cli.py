import types
from typing import Type, Optional, Iterable

import typer
from dependencies import Injector, value

from jeeves.commands.find_packages import FindPackages
from jeeves.commands.flakehell import FlakeHell
from jeeves.commands.format import Format
from jeeves.commands.isort import Isort
from jeeves.commands.lint import Lint
from jeeves.commands.mypy import Mypy
from jeeves.commands.project_root import ProjectRoot
from jeeves.models import Command
from jeeves_terraform.main import JeevesTerraform


class Jeeves(Injector):
    """Default Jeeves configuration."""

    project_root = ProjectRoot

    # Helpers
    directories = FindPackages

    # Concrete tools
    isort = Isort
    flakehell = FlakeHell
    mypy = Mypy

    # Grouped tools
    lint = Lint
    format = Format

    # noinspection PyMethodParameters
    @value
    def linters(flakehell, mypy):
        """Return list of linters."""
        return [flakehell, mypy]

    # noinspection PyMethodParameters
    @value
    def formatters(isort):
        """Return list of formatters."""
        return [isort]

    cli_commands = ['lint', 'format']


def is_build_data_spec(factory) -> bool:
    return (
        isinstance(factory, types.LambdaType) and
        '_build_data_spec' in str(factory)
    )


def wrap_command(injector, name):
    def _wrap():
        print(injector.install())

    return _wrap


def injector_member_names(injector: Type[Injector]) -> Iterable[str]:
    """List of public injector members."""
    for name in injector.__dependencies__.specs.keys():
        if not name.startswith('__'):
            yield name


def create_typer_from_injector(injector: Type[Injector], name: Optional[str] = None) -> typer.Typer:
    """Construct an app and register all commands."""
    typer_app = typer.Typer(
        name=name,
    )

    for name in injector_member_names(injector):
        member = getattr(injector, name)

        if isinstance(member, type) and issubclass(member, Injector):
            sub_app = create_typer_from_injector(
                injector=member,
                name=name,
            )
            typer_app.add_typer(sub_app, name=name)

        elif isinstance(member, Command):
            typer_app.command(name=name)(member)

    return typer_app


app = create_typer_from_injector(Jeeves & JeevesTerraform)


if __name__ == '__main__':
    app()
