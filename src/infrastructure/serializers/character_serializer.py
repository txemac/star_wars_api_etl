from typing import Dict

from src.domain.character import Character
from src.domain.serializer import Serializer


class CharacterSerializer(Serializer):

    @classmethod
    def serialize(
        cls,
        character: Character,
    ) -> Dict:
        return dict(
            name=character.name,
            height=character.height,
            appearances=character.appearances,
            species=character.specie.name if character.specie else None,
        )
