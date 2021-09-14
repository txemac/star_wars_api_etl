from typing import Dict
from typing import Optional

from src.domain.character import Character
from src.domain.specie import Specie
from src.domain.transform import Transform


class StartWarsAPICharacterTransform(Transform):

    @classmethod
    def transform(
        cls,
        start_wars_api_character: Optional[Dict],
    ) -> Optional[Character]:
        specie = None
        if len(start_wars_api_character["species"]) > 0:
            specie = Specie(
                id=int(start_wars_api_character["species"][0][-2:-1]),
            )

        try:
            height = int(start_wars_api_character["height"])
        except ValueError:
            height = None

        return Character(
            name=start_wars_api_character["name"],
            appearances=len(start_wars_api_character["films"]),
            height=height,
            specie=specie,
        ) if start_wars_api_character is not None else None
