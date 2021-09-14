from dataclasses import dataclass
from typing import Optional

from src.domain.specie import Specie


@dataclass
class Character:
    name: str
    appearances: int
    height: Optional[int] = None
    specie: Optional[Specie] = None

    def __getitem__(self, item):
        return getattr(self, item)
