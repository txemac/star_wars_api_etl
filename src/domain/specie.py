from dataclasses import dataclass
from typing import Optional


@dataclass
class Specie:
    id: int
    name: Optional[str] = None
