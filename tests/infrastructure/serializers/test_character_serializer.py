from typing import Dict

from src.domain.character import Character
from src.domain.specie import Specie
from src.infrastructure.serializers.character_serializer import CharacterSerializer
from tests.utils import assert_contains_all


def test_character_serializer() -> None:
    new_character = Character(
        name="Espinete",
        height=180,
        appearances=0,
        specie=Specie(
            id=17,
            name="Erizo gigante",
        ),
    )
    result = CharacterSerializer.serialize(character=new_character)
    assert isinstance(result, Dict)
    assert_contains_all(
        original=result,
        expected=["name", "height", "appearances", "species"]
    )
