from typing import List

from src.domain.character import Character
from src.domain.star_wars_repository import StarWarsRepository
from tests.utils import assert_lists


def test_sort_characters_by_appearances_ok(
    star_wars_repository: StarWarsRepository,
    list_characters: List[Character],
) -> None:
    result = star_wars_repository.sort_characters_by_appearances(characters=list_characters)
    expected = [list_characters[2], list_characters[1], list_characters[0]]
    assert_lists(original=result, expected=expected)


def test_sort_characters_by_appearances_with_limit(
    star_wars_repository: StarWarsRepository,
    list_characters: List[Character],
) -> None:
    result = star_wars_repository.sort_characters_by_appearances(characters=list_characters, limit=2)
    expected = [list_characters[2], list_characters[1]]
    assert_lists(original=result, expected=expected)


def test_sort_characters_taller_ok(
    star_wars_repository: StarWarsRepository,
    list_characters: List[Character],
) -> None:
    result = star_wars_repository.sort_characters_taller(characters=list_characters)
    expected = [list_characters[0], list_characters[2], list_characters[1]]
    assert_lists(original=result, expected=expected)


def test_sort_characters_taller_with_limit(
    star_wars_repository: StarWarsRepository,
    list_characters: List[Character],
) -> None:
    result = star_wars_repository.sort_characters_taller(characters=list_characters, limit=2)
    expected = [list_characters[0], list_characters[2]]
    assert_lists(original=result, expected=expected)
