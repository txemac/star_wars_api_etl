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
            height=30,
        ),
        Character(
            name="Char 1",
            appearances=20,
            height=10,
        ),
        Character(
            name="Char 1",
            appearances=30,
            height=20,
        ),
    ]


@pytest.fixture
def all_characters() -> List[Character]:
    return [
        Character(name='Luke Skywalker', appearances=4, height=172),
        Character(name='C-3PO', appearances=6, height=167),
        Character(name='R2-D2', appearances=6, height=96),
        Character(name='Darth Vader', appearances=4, height=202),
        Character(name='Leia Organa', appearances=4, height=150),
        Character(name='Owen Lars', appearances=3, height=178),
        Character(name='Beru Whitesun lars', appearances=3, height=165),
        Character(name='R5-D4', appearances=1, height=97),
        Character(name='Biggs Darklighter', appearances=1, height=183),
        Character(name='Obi-Wan Kenobi', appearances=6, height=182),
        Character(name='Anakin Skywalker', appearances=3, height=188),
        Character(name='Wilhuff Tarkin', appearances=2, height=180),
        Character(name='Chewbacca', appearances=4, height=228),
        Character(name='Han Solo', appearances=3, height=180),
        Character(name='Greedo', appearances=1, height=173),
        Character(name='Jabba Desilijic Tiure', appearances=3, height=175),
        Character(name='Wedge Antilles', appearances=3, height=170),
        Character(name='Jek Tono Porkins', appearances=1, height=180),
        Character(name='Yoda', appearances=5, height=66),
        Character(name='Palpatine', appearances=5, height=170),
        Character(name='Boba Fett', appearances=3, height=183),
        Character(name='IG-88', appearances=1, height=200),
        Character(name='Bossk', appearances=1, height=190),
        Character(name='Lando Calrissian', appearances=2, height=177),
        Character(name='Lobot', appearances=1, height=175),
        Character(name='Ackbar', appearances=1, height=180),
        Character(name='Mon Mothma', appearances=1, height=150),
        Character(name='Arvel Crynyd', appearances=1, height=None),
        Character(name='Wicket Systri Warrick', appearances=1, height=88),
        Character(name='Nien Nunb', appearances=1, height=160),
        Character(name='Qui-Gon Jinn', appearances=1, height=193),
        Character(name='Nute Gunray', appearances=3, height=191),
        Character(name='Finis Valorum', appearances=1, height=170),
        Character(name='Padmé Amidala', appearances=3, height=185),
        Character(name='Jar Jar Binks', appearances=2, height=196),
        Character(name='Roos Tarpals', appearances=1, height=224),
        Character(name='Rugor Nass', appearances=1, height=206),
        Character(name='Ric Olié', appearances=1, height=183),
        Character(name='Watto', appearances=2, height=137),
        Character(name='Sebulba', appearances=1, height=112),
        Character(name='Quarsh Panaka', appearances=1, height=183),
        Character(name='Shmi Skywalker', appearances=2, height=163),
        Character(name='Darth Maul', appearances=1, height=175),
        Character(name='Bib Fortuna', appearances=1, height=180),
        Character(name='Ayla Secura', appearances=3, height=178),
        Character(name='Ratts Tyerel', appearances=1, height=79),
        Character(name='Dud Bolt', appearances=1, height=94),
        Character(name='Gasgano', appearances=1, height=122),
        Character(name='Ben Quadinaros', appearances=1, height=163),
        Character(name='Mace Windu', appearances=3, height=188),
        Character(name='Ki-Adi-Mundi', appearances=3, height=198),
        Character(name='Kit Fisto', appearances=3, height=196),
        Character(name='Eeth Koth', appearances=2, height=171),
        Character(name='Adi Gallia', appearances=2, height=184),
        Character(name='Saesee Tiin', appearances=2, height=188),
        Character(name='Yarael Poof', appearances=1, height=264),
        Character(name='Plo Koon', appearances=3, height=188),
        Character(name='Mas Amedda', appearances=2, height=196),
        Character(name='Gregar Typho', appearances=1, height=185),
        Character(name='Cordé', appearances=1, height=157),
        Character(name='Cliegg Lars', appearances=1, height=183),
        Character(name='Poggle the Lesser', appearances=2, height=183),
        Character(name='Luminara Unduli', appearances=2, height=170),
        Character(name='Barriss Offee', appearances=1, height=166),
        Character(name='Dormé', appearances=1, height=165),
        Character(name='Dooku', appearances=2, height=193),
        Character(name='Bail Prestor Organa', appearances=2, height=191),
        Character(name='Jango Fett', appearances=1, height=183),
        Character(name='Zam Wesell', appearances=1, height=168),
        Character(name='Dexter Jettster', appearances=1, height=198),
        Character(name='Lama Su', appearances=1, height=229),
        Character(name='Taun We', appearances=1, height=213),
        Character(name='Jocasta Nu', appearances=1, height=167),
        Character(name='R4-P17', appearances=2, height=96),
        Character(name='Wat Tambor', appearances=1, height=193),
        Character(name='San Hill', appearances=1, height=191),
        Character(name='Shaak Ti', appearances=2, height=178),
        Character(name='Grievous', appearances=1, height=216),
        Character(name='Tarfful', appearances=1, height=234),
        Character(name='Raymus Antilles', appearances=2, height=188),
        Character(name='Sly Moore', appearances=2, height=178),
        Character(name='Tion Medon', appearances=1, height=206),
    ]


@pytest.fixture
def characters_sorted_by_appearances() -> List[Character]:
    return [
        Character(name='C-3PO', appearances=6, height=167),
        Character(name='R2-D2', appearances=6, height=96),
        Character(name='Obi-Wan Kenobi', appearances=6, height=182),
        Character(name='Yoda', appearances=5, height=66),
        Character(name='Palpatine', appearances=5, height=170),
        Character(name='Luke Skywalker', appearances=4, height=172),
        Character(name='Darth Vader', appearances=4, height=202),
        Character(name='Leia Organa', appearances=4, height=150),
        Character(name='Chewbacca', appearances=4, height=228),
        Character(name='Owen Lars', appearances=3, height=178),
    ]


@pytest.fixture
def characters_sorted_by_appearances_and_height() -> List[Character]:
    return [
        Character(name='Chewbacca', appearances=4, height=228),
        Character(name='Darth Vader', appearances=4, height=202),
        Character(name='Obi-Wan Kenobi', appearances=6, height=182),
        Character(name='Owen Lars', appearances=3, height=178),
        Character(name='Luke Skywalker', appearances=4, height=172),
        Character(name='Palpatine', appearances=5, height=170),
        Character(name='C-3PO', appearances=6, height=167),
        Character(name='Leia Organa', appearances=4, height=150),
        Character(name='R2-D2', appearances=6, height=96),
        Character(name='Yoda', appearances=5, height=66),
    ]
