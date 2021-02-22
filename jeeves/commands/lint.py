from dataclasses import dataclass
from typing import List, Callable


@dataclass
class Lint:
    """Check your code for compliance to standards."""

    __name__ = 'lint'

    linters: List[Callable[[], None]]

    def __call__(self):
        """Run them all."""
        for linter in self.linters:
            linter()
