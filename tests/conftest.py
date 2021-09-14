from typing import Dict
from typing import List

import pytest as pytest

from src.domain.character import Character
from src.domain.start_wars_repository import StartWarsRepository
from src.infrastructure.adapters.start_wars_api_adapter import StartWarsAPIAdapter


@pytest.fixture
def start_wars_repository() -> StartWarsRepository:
    return StartWarsAPIAdapter()


@pytest.fixture
def start_wars_api_character_1() -> Dict:
    return {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "homeworld": "https://swapi.dev/api/planets/1/",
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/6/"
        ],
        "species": [],
        "vehicles": [
            "https://swapi.dev/api/vehicles/14/",
            "https://swapi.dev/api/vehicles/30/"
        ],
        "starships": [
            "https://swapi.dev/api/starships/12/",
            "https://swapi.dev/api/starships/22/"
        ],
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-20T21:17:56.891000Z",
        "url": "https://swapi.dev/api/people/1/"
    }


@pytest.fixture
def list_characters() -> List[Character]:
    return [
        Character(
            name="Char 1",
            appearances=10,
        ),
        Character(
            name="Char 1",
            appearances=20,
        ),
        Character(
            name="Char 1",
            appearances=30,
        ),
    ]


@pytest.fixture
def all_characters() -> List[Character]:
    return [
        Character(name='Luke Skywalker', appearances=4),
        Character(name='C-3PO', appearances=6),
        Character(name='R2-D2', appearances=6),
        Character(name='Darth Vader', appearances=4),
        Character(name='Leia Organa', appearances=4),
        Character(name='Owen Lars', appearances=3),
        Character(name='Beru Whitesun lars', appearances=3),
        Character(name='R5-D4', appearances=1),
        Character(name='Biggs Darklighter', appearances=1),
        Character(name='Obi-Wan Kenobi', appearances=6),
        Character(name='Anakin Skywalker', appearances=3),
        Character(name='Wilhuff Tarkin', appearances=2),
        Character(name='Chewbacca', appearances=4),
        Character(name='Han Solo', appearances=3),
        Character(name='Greedo', appearances=1),
        Character(name='Jabba Desilijic Tiure', appearances=3),
        Character(name='Wedge Antilles', appearances=3),
        Character(name='Jek Tono Porkins', appearances=1),
        Character(name='Yoda', appearances=5),
        Character(name='Palpatine', appearances=5),
        Character(name='Boba Fett', appearances=3),
        Character(name='IG-88', appearances=1),
        Character(name='Bossk', appearances=1),
        Character(name='Lando Calrissian', appearances=2),
        Character(name='Lobot', appearances=1),
        Character(name='Ackbar', appearances=1),
        Character(name='Mon Mothma', appearances=1),
        Character(name='Arvel Crynyd', appearances=1),
        Character(name='Wicket Systri Warrick', appearances=1),
        Character(name='Nien Nunb', appearances=1),
        Character(name='Qui-Gon Jinn', appearances=1),
        Character(name='Nute Gunray', appearances=3),
        Character(name='Finis Valorum', appearances=1),
        Character(name='Padmé Amidala', appearances=3),
        Character(name='Jar Jar Binks', appearances=2),
        Character(name='Roos Tarpals', appearances=1),
        Character(name='Rugor Nass', appearances=1),
        Character(name='Ric Olié', appearances=1),
        Character(name='Watto', appearances=2),
        Character(name='Sebulba', appearances=1),
        Character(name='Quarsh Panaka', appearances=1),
        Character(name='Shmi Skywalker', appearances=2),
        Character(name='Darth Maul', appearances=1),
        Character(name='Bib Fortuna', appearances=1),
        Character(name='Ayla Secura', appearances=3),
        Character(name='Ratts Tyerel', appearances=1),
        Character(name='Dud Bolt', appearances=1),
        Character(name='Gasgano', appearances=1),
        Character(name='Ben Quadinaros', appearances=1),
        Character(name='Mace Windu', appearances=3),
        Character(name='Ki-Adi-Mundi', appearances=3),
        Character(name='Kit Fisto', appearances=3),
        Character(name='Eeth Koth', appearances=2),
        Character(name='Adi Gallia', appearances=2),
        Character(name='Saesee Tiin', appearances=2),
        Character(name='Yarael Poof', appearances=1),
        Character(name='Plo Koon', appearances=3),
        Character(name='Mas Amedda', appearances=2),
        Character(name='Gregar Typho', appearances=1),
        Character(name='Cordé', appearances=1),
        Character(name='Cliegg Lars', appearances=1),
        Character(name='Poggle the Lesser', appearances=2),
        Character(name='Luminara Unduli', appearances=2),
        Character(name='Barriss Offee', appearances=1),
        Character(name='Dormé', appearances=1),
        Character(name='Dooku', appearances=2),
        Character(name='Bail Prestor Organa', appearances=2),
        Character(name='Jango Fett', appearances=1),
        Character(name='Zam Wesell', appearances=1),
        Character(name='Dexter Jettster', appearances=1),
        Character(name='Lama Su', appearances=1),
        Character(name='Taun We', appearances=1),
        Character(name='Jocasta Nu', appearances=1),
        Character(name='R4-P17', appearances=2),
        Character(name='Wat Tambor', appearances=1),
        Character(name='San Hill', appearances=1),
        Character(name='Shaak Ti', appearances=2),
        Character(name='Grievous', appearances=1),
        Character(name='Tarfful', appearances=1),
        Character(name='Raymus Antilles', appearances=2),
        Character(name='Sly Moore', appearances=2),
        Character(name='Tion Medon', appearances=1),
    ]


@pytest.fixture
def characters_sorted_by_appearances() -> List[Character]:
    return [
        Character(name='C-3PO', appearances=6),
        Character(name='R2-D2', appearances=6),
        Character(name='Obi-Wan Kenobi', appearances=6),
        Character(name='Yoda', appearances=5),
        Character(name='Palpatine', appearances=5),
        Character(name='Luke Skywalker', appearances=4),
        Character(name='Darth Vader', appearances=4),
        Character(name='Leia Organa', appearances=4),
        Character(name='Chewbacca', appearances=4),
        Character(name='Owen Lars', appearances=3),
    ]
