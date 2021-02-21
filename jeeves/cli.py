import subprocess
from dataclasses import dataclass
from typing import List

import setuptools
import typer
from dependencies import Injector

app = typer.Typer()


@dataclass
class FindPackages:
    """Find Python packages in current directory."""

    def __call__(self) -> List[str]:
        """Use Setuptools."""
        return setuptools.find_packages()


@dataclass
class Isort:
    """Format imports with isort."""

    __name__ = 'isort'

    # FIXME remove this dependency
    directories: FindPackages

    def __call__(self):
        """Run isort."""
        subprocess.run(['isort', ] + self.directories())


@dataclass
class FlakeHell:
    """Find issues in code with flakehell."""

    __name__ = 'flakehell'

    # FIXME remove this dependency
    directories: FindPackages

    def __call__(self):
        """Run flahekell."""
        subprocess.run(['flakehell', 'lint', ] + self.directories())


class Jeeves(Injector):
    """Default Jeeves configuration."""

    directories = FindPackages
    isort = Isort
    flakehell = FlakeHell


app.command()(Jeeves.flakehell)
app.command()(Jeeves.isort)


if __name__ == '__main__':
    app()
