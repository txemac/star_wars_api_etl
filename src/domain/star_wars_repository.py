from abc import ABC
from abc import abstractmethod
from typing import List

from src.domain.character import Character


class StarWarsRepository(ABC):
    @abstractmethod
    def get_characters(self) -> List[Character]:
        """
        Get all character from Star Wars API

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

    @abstractmethod
    def get_specie_name_by_id(
        self,
        specie_id: int,
    ) -> str:
        """
        Get a persisted specie name by specie ID from Star Wars API

        :param specie_id: ID of the specie
        :return: specie name
        """
        pass
