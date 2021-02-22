from dataclasses import dataclass
from typing import List, Callable


@dataclass
class Format:
    """Reformat your code."""

    __name__ = 'format'

    formatters: List[Callable[[], None]]

    def __call__(self):
        """Run them all."""
        for formatter in self.formatters:
            formatter()
