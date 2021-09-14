from typing import Dict

from src.domain.character import Character
from src.infrastructure.transforms.star_wars_api_character_transform import StarWarsAPICharacterTransform
from tests.utils import assert_dicts


def test_transform(
    star_wars_api_character_1: Dict,
) -> None:
    result = StarWarsAPICharacterTransform.transform(star_wars_api_character=star_wars_api_character_1)
    assert isinstance(result, Character)
    expected = dict(
        name="Luke Skywalker",
        appearances=4,
        height=172,
    )
    assert_dicts(original=result.__dict__, expected=expected)
