from typing import List

from src.domain.character import Character
from src.domain.star_wars_repository import StarWarsRepository
from src.infrastructure.serializers.character_serializer import CharacterSerializer
from src.utils import csv_generator
from tests.utils import assert_lists


def test_sort_by_appearances(
    star_wars_repository: StarWarsRepository,
    all_characters: List[Character],
    characters_sorted_by_appearances: List[Character],
) -> None:
    result = star_wars_repository.sort_characters_by_appearances(characters=all_characters, limit=10)
    assert_lists(original=result, expected=characters_sorted_by_appearances)


def test_sort_by_height(
    star_wars_repository: StarWarsRepository,
    characters_sorted_by_appearances: List[Character],
    characters_sorted_by_appearances_and_height: List[Character],
) -> None:
    result = star_wars_repository.sort_characters_taller(characters=characters_sorted_by_appearances, limit=10)
    assert_lists(original=result, expected=characters_sorted_by_appearances_and_height)


def test_csv_file(
    characters_to_csv: List[Character],
    csv_file_text: str,
) -> None:
    path = "file-test.csv"
    csv_generator.create(
        path=path,
        headers=["name", "species", "height", "appearances"],
        items=CharacterSerializer.serialize_list(item_list=characters_to_csv),
    )

    with open(path, "r") as file:
        text = file.read()

    assert text == csv_file_text
