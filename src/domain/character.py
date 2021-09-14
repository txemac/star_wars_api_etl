from dataclasses import dataclass
from typing import Optional


@dataclass
class Character:
    name: str
    appearances: int
    height: Optional[int] = None

    def __getitem__(self, item):
        return getattr(self, item)
