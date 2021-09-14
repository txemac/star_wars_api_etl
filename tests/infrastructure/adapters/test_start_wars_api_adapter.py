from typing import List

from src.domain.character import Character
from src.domain.start_wars_repository import StartWarsRepository
from tests.utils import assert_lists


def test_sort_characters_by_appearances_ok(
    start_wars_repository: StartWarsRepository,
    list_characters: List[Character],
) -> None:
    result = start_wars_repository.sort_characters_by_appearances(characters=list_characters)
    expected = [list_characters[2], list_characters[1], list_characters[0]]
    assert_lists(original=result, expected=expected)


def test_sort_characters_by_appearances_with_limit(
    start_wars_repository: StartWarsRepository,
    list_characters: List[Character],
) -> None:
    result = start_wars_repository.sort_characters_by_appearances(characters=list_characters, limit=2)
    expected = [list_characters[2], list_characters[1]]
    assert_lists(original=result, expected=expected)
