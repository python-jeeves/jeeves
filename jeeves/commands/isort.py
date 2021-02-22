import subprocess
from dataclasses import dataclass

from jeeves.commands.find_packages import FindPackages


@dataclass
class Isort:
    """Format imports with isort."""

    # This attribute is used as command name. FIXME not very usable.
    __name__ = 'isort'

    # FIXME remove this dependency on FindPackages type
    directories: FindPackages

    def __call__(self):
        """Run isort."""
        subprocess.run(['isort', ] + self.directories())
