from typing import Dict
from typing import Optional

from domain.character import Character
from domain.transform import Transform


class StartWarsAPICharacterTransform(Transform):

    @classmethod
    def transform(
        cls,
        start_wars_api_character: Optional[Dict],
    ) -> Optional[Character]:
        return Character(
            name=start_wars_api_character["name"],
            appearances=len(start_wars_api_character["films"]),
        ) if start_wars_api_character is not None else None
