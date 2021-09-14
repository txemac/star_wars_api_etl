from typing import List

from src.domain.character import Character
from src.domain.start_wars_repository import StartWarsRepository
from tests.utils import assert_lists


def test_sort_by_appearances(
    start_wars_repository: StartWarsRepository,
    all_characters: List[Character],
    characters_sorted_by_appearances: List[Character],
) -> None:
    result = start_wars_repository.sort_characters_by_appearances(characters=all_characters, limit=10)
    assert_lists(original=result, expected=characters_sorted_by_appearances)


def test_sort_by_height(
    start_wars_repository: StartWarsRepository,
    characters_sorted_by_appearances: List[Character],
    characters_sorted_by_appearances_and_height: List[Character],
) -> None:
    result = start_wars_repository.sort_characters_taller(characters=characters_sorted_by_appearances, limit=10)
    assert_lists(original=result, expected=characters_sorted_by_appearances_and_height)
