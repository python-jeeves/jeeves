import subprocess
from dataclasses import dataclass

from jeeves.commands.find_packages import FindPackages


@dataclass
class FlakeHell:
    """Find issues in code with flakehell."""

    __name__ = 'flakehell'

    # FIXME remove this dependency
    directories: FindPackages

    def __call__(self):
        """Run flahekell."""
        subprocess.run(['flakehell', 'lint', ] + self.directories())
