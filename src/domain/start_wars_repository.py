from abc import ABC
from abc import abstractmethod
from typing import List

from domain.character import Character


class StartWarsRepository(ABC):
    @abstractmethod
    def get_characters(self) -> List[Character]:
        """
        Get all character from Start Wars API

        :return: list of character
        """
        pass
