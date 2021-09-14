from typing import List

import requests

from src import settings
from src.domain.character import Character
from src.domain.specie import Specie
from src.domain.start_wars_repository import StartWarsRepository
from src.infrastructure.transforms.start_wars_api_character_transform import StartWarsAPICharacterTransform


class StartWarsAPIAdapter(StartWarsRepository):

    def get_characters(
        self,
    ) -> List[Character]:
        response_json = requests.get(
            url=f"{settings.START_WARS_API_URL}/people",
        ).json()

        result = response_json["results"]

        while response_json["next"]:
            response_json = requests.get(
                url=response_json["next"],
            ).json()
            result += response_json["results"]

        return StartWarsAPICharacterTransform.transform_list(item_list=result)

    def sort_characters_by_appearances(
        self,
        characters: List[Character],
        limit: int = 10,
    ) -> List[Character]:
        result = sorted(characters, key=lambda c: int(c["appearances"]), reverse=True)

        return result[:limit]

    def sort_characters_taller(
        self,
        characters: List[Character],
        limit: int = 10,
    ) -> List[Character]:
        result = sorted(characters, key=lambda c: int(c["height"]), reverse=True)

        return result[:limit]

    def get_specie_name_by_id(
        self,
        specie_id: int,
    ) -> Specie:
        response_json = requests.get(
            url=f"{settings.START_WARS_API_URL}/species/{specie_id}",
        ).json()

        return response_json["name"]
