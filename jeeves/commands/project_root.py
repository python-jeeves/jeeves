from dataclasses import dataclass
from pathlib import Path

from documented import DocumentedError

PYPROJECT_TOML = 'pyproject.toml'


@dataclass
class ProjectRootNotFound(DocumentedError):
    """
    Cannot find project root directory.

    Project root directory must contain {self.pyproject_toml} file in it. Jeeves
    looks for this file in current directory and in each of its ancestors.

    Please check {self.current_directory} for being a valid project directory.
    """

    current_directory: Path
    pyproject_toml: str = PYPROJECT_TOML


@dataclass
class ProjectRoot:
    def __call__(self) -> Path:
        """Directory with pyproject.toml."""
        directory = Path.cwd()

        while str(directory) != '/':
            pyproject_toml_path = directory / PYPROJECT_TOML
            if pyproject_toml_path.exists():
                return directory

            directory = directory.parent

        raise ProjectRootNotFound(
            current_directory=Path.cwd(),
        )
