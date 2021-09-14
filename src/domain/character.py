from dataclasses import dataclass


@dataclass
class Character:
    name: str
    appearances: int

    def __getitem__(self, item):
        return getattr(self, item)
