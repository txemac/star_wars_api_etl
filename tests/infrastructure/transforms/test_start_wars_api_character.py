from typing import Dict

from domain.character import Character
from infrastructure.transforms.start_wars_api_character_transform import StartWarsAPICharacterTransform
from tests.utils import assert_dicts


def test_transform(
    start_wars_api_character_1: Dict,
) -> None:
    result = StartWarsAPICharacterTransform.transform(start_wars_api_character=start_wars_api_character_1)
    assert isinstance(result, Character)
    expected = dict(
        name="Luke Skywalker",
        appearances=4,
    )
    assert_dicts(original=result.__dict__, expected=expected)
