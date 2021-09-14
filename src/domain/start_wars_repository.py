from abc import ABC
from abc import abstractmethod
from typing import List

from src.domain.character import Character


class StartWarsRepository(ABC):
    @abstractmethod
    def get_characters(self) -> List[Character]:
        """
        Get all character from Start Wars API

        :return: list of character
        """
        pass

    @abstractmethod
    def sort_characters_by_appearances(
        self,
        characters: List[Character],
        limit: int = 10,
    ) -> List[Character]:
        """
        Sort a list of characters by number of films.
        Order by most number of films.

        :param characters: characters
        :param limit: max of items at result
        :return: list of characters
        """
        pass

    @abstractmethod
    def sort_characters_taller(
        self,
        characters: List[Character],
        limit: int = 10,
    ) -> List[Character]:
        """
        Sort a list of characters by height.
        Order by taller.

        :param characters: characters
        :param limit: max of items at result
        :return: list of characters
        """
        pass
