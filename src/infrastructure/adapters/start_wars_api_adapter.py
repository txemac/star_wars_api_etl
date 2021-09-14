from typing import List

import requests

import settings
from domain.character import Character
from domain.start_wars_repository import StartWarsRepository
from infrastructure.transforms.start_wars_api_character_transform import StartWarsAPICharacterTransform


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
