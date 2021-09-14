from typing import Dict
from typing import List

import pytest as pytest

from src.domain.character import Character
from src.domain.specie import Specie
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
        Character(name='Luke Skywalker', appearances=4, height=172, specie=None),
        Character(name='C-3PO', appearances=6, height=167, specie=Specie(id=2, name=None)),
        Character(name='R2-D2', appearances=6, height=96, specie=Specie(id=2, name=None)),
        Character(name='Darth Vader', appearances=4, height=202, specie=None),
        Character(name='Leia Organa', appearances=4, height=150, specie=None),
        Character(name='Owen Lars', appearances=3, height=178, specie=None),
        Character(name='Beru Whitesun lars', appearances=3, height=165, specie=None),
        Character(name='R5-D4', appearances=1, height=97, specie=Specie(id=2, name=None)),
        Character(name='Biggs Darklighter', appearances=1, height=183, specie=None),
        Character(name='Obi-Wan Kenobi', appearances=6, height=182, specie=None),
        Character(name='Anakin Skywalker', appearances=3, height=188, specie=None),
        Character(name='Wilhuff Tarkin', appearances=2, height=180, specie=None),
        Character(name='Chewbacca', appearances=4, height=228, specie=Specie(id=3, name=None)),
        Character(name='Han Solo', appearances=3, height=180, specie=None),
        Character(name='Greedo', appearances=1, height=173, specie=Specie(id=4, name=None)),
        Character(name='Jabba Desilijic Tiure', appearances=3, height=175, specie=Specie(id=5, name=None)),
        Character(name='Wedge Antilles', appearances=3, height=170, specie=None),
        Character(name='Jek Tono Porkins', appearances=1, height=180, specie=None),
        Character(name='Yoda', appearances=5, height=66, specie=Specie(id=6, name=None)),
        Character(name='Palpatine', appearances=5, height=170, specie=None),
        Character(name='Boba Fett', appearances=3, height=183, specie=None),
        Character(name='IG-88', appearances=1, height=200, specie=Specie(id=2, name=None)),
        Character(name='Bossk', appearances=1, height=190, specie=Specie(id=7, name=None)),
        Character(name='Lando Calrissian', appearances=2, height=177, specie=None),
        Character(name='Lobot', appearances=1, height=175, specie=None),
        Character(name='Ackbar', appearances=1, height=180, specie=Specie(id=8, name=None)),
        Character(name='Mon Mothma', appearances=1, height=150, specie=None),
        Character(name='Arvel Crynyd', appearances=1, height=None, specie=None),
        Character(name='Wicket Systri Warrick', appearances=1, height=88, specie=Specie(id=9, name=None)),
        Character(name='Nien Nunb', appearances=1, height=160, specie=Specie(id=0, name=None)),
        Character(name='Qui-Gon Jinn', appearances=1, height=193, specie=None),
        Character(name='Nute Gunray', appearances=3, height=191, specie=Specie(id=1, name=None)),
        Character(name='Finis Valorum', appearances=1, height=170, specie=None),
        Character(name='Padmé Amidala', appearances=3, height=185, specie=None),
        Character(name='Jar Jar Binks', appearances=2, height=196, specie=Specie(id=2, name=None)),
        Character(name='Roos Tarpals', appearances=1, height=224, specie=Specie(id=2, name=None)),
        Character(name='Rugor Nass', appearances=1, height=206, specie=Specie(id=2, name=None)),
        Character(name='Ric Olié', appearances=1, height=183, specie=None),
        Character(name='Watto', appearances=2, height=137, specie=Specie(id=3, name=None)),
        Character(name='Sebulba', appearances=1, height=112, specie=Specie(id=4, name=None)),
        Character(name='Quarsh Panaka', appearances=1, height=183, specie=None),
        Character(name='Shmi Skywalker', appearances=2, height=163, specie=None),
        Character(name='Darth Maul', appearances=1, height=175, specie=Specie(id=2, name=None)),
        Character(name='Bib Fortuna', appearances=1, height=180, specie=Specie(id=5, name=None)),
        Character(name='Ayla Secura', appearances=3, height=178, specie=Specie(id=5, name=None)),
        Character(name='Ratts Tyerel', appearances=1, height=79, specie=Specie(id=6, name=None)),
        Character(name='Dud Bolt', appearances=1, height=94, specie=Specie(id=7, name=None)),
        Character(name='Gasgano', appearances=1, height=122, specie=Specie(id=8, name=None)),
        Character(name='Ben Quadinaros', appearances=1, height=163, specie=Specie(id=9, name=None)),
        Character(name='Mace Windu', appearances=3, height=188, specie=None),
        Character(name='Ki-Adi-Mundi', appearances=3, height=198, specie=Specie(id=0, name=None)),
        Character(name='Kit Fisto', appearances=3, height=196, specie=Specie(id=1, name=None)),
        Character(name='Eeth Koth', appearances=2, height=171, specie=Specie(id=2, name=None)),
        Character(name='Adi Gallia', appearances=2, height=184, specie=Specie(id=3, name=None)),
        Character(name='Saesee Tiin', appearances=2, height=188, specie=Specie(id=4, name=None)),
        Character(name='Yarael Poof', appearances=1, height=264, specie=Specie(id=5, name=None)),
        Character(name='Plo Koon', appearances=3, height=188, specie=Specie(id=6, name=None)),
        Character(name='Mas Amedda', appearances=2, height=196, specie=Specie(id=7, name=None)),
        Character(name='Gregar Typho', appearances=1, height=185, specie=None),
        Character(name='Cordé', appearances=1, height=157, specie=None),
        Character(name='Cliegg Lars', appearances=1, height=183, specie=None),
        Character(name='Poggle the Lesser', appearances=2, height=183, specie=Specie(id=8, name=None)),
        Character(name='Luminara Unduli', appearances=2, height=170, specie=Specie(id=9, name=None)),
        Character(name='Barriss Offee', appearances=1, height=166, specie=Specie(id=9, name=None)),
        Character(name='Dormé', appearances=1, height=165, specie=Specie(id=1, name=None)),
        Character(name='Dooku', appearances=2, height=193, specie=Specie(id=1, name=None)),
        Character(name='Bail Prestor Organa', appearances=2, height=191, specie=Specie(id=1, name=None)),
        Character(name='Jango Fett', appearances=1, height=183, specie=None),
        Character(name='Zam Wesell', appearances=1, height=168, specie=Specie(id=0, name=None)),
        Character(name='Dexter Jettster', appearances=1, height=198, specie=Specie(id=1, name=None)),
        Character(name='Lama Su', appearances=1, height=229, specie=Specie(id=2, name=None)),
        Character(name='Taun We', appearances=1, height=213, specie=Specie(id=2, name=None)),
        Character(name='Jocasta Nu', appearances=1, height=167, specie=Specie(id=1, name=None)),
        Character(name='R4-P17', appearances=2, height=96, specie=None),
        Character(name='Wat Tambor', appearances=1, height=193, specie=Specie(id=3, name=None)),
        Character(name='San Hill', appearances=1, height=191, specie=Specie(id=4, name=None)),
        Character(name='Shaak Ti', appearances=2, height=178, specie=Specie(id=5, name=None)),
        Character(name='Grievous', appearances=1, height=216, specie=Specie(id=6, name=None)),
        Character(name='Tarfful', appearances=1, height=234, specie=Specie(id=3, name=None)),
        Character(name='Raymus Antilles', appearances=2, height=188, specie=None),
        Character(name='Sly Moore', appearances=2, height=178, specie=None),
        Character(name='Tion Medon', appearances=1, height=206, specie=Specie(id=7, name=None))
    ]


@pytest.fixture
def characters_sorted_by_appearances() -> List[Character]:
    return [
        Character(name='C-3PO', appearances=6, height=167, specie=Specie(id=2, name=None)),
        Character(name='R2-D2', appearances=6, height=96, specie=Specie(id=2, name=None)),
        Character(name='Obi-Wan Kenobi', appearances=6, height=182, specie=None),
        Character(name='Yoda', appearances=5, height=66, specie=Specie(id=6, name=None)),
        Character(name='Palpatine', appearances=5, height=170, specie=None),
        Character(name='Luke Skywalker', appearances=4, height=172, specie=None),
        Character(name='Darth Vader', appearances=4, height=202, specie=None),
        Character(name='Leia Organa', appearances=4, height=150, specie=None),
        Character(name='Chewbacca', appearances=4, height=228, specie=Specie(id=3, name=None)),
        Character(name='Owen Lars', appearances=3, height=178, specie=None)
    ]


@pytest.fixture
def characters_sorted_by_appearances_and_height() -> List[Character]:
    return [
        Character(name='Chewbacca', appearances=4, height=228, specie=Specie(id=3, name=None)),
        Character(name='Darth Vader', appearances=4, height=202, specie=None),
        Character(name='Obi-Wan Kenobi', appearances=6, height=182, specie=None),
        Character(name='Owen Lars', appearances=3, height=178, specie=None),
        Character(name='Luke Skywalker', appearances=4, height=172, specie=None),
        Character(name='Palpatine', appearances=5, height=170, specie=None),
        Character(name='C-3PO', appearances=6, height=167, specie=Specie(id=2, name=None)),
        Character(name='Leia Organa', appearances=4, height=150, specie=None),
        Character(name='R2-D2', appearances=6, height=96, specie=Specie(id=2, name=None)),
        Character(name='Yoda', appearances=5, height=66, specie=Specie(id=6, name=None))
    ]


@pytest.fixture
def characters_to_csv() -> List[Character]:
    return [
        Character(name='Chewbacca', appearances=4, height=228, specie=Specie(id=3, name='Wookie')),
        Character(name='Darth Vader', appearances=4, height=202, specie=None),
        Character(name='Obi-Wan Kenobi', appearances=6, height=182, specie=None),
        Character(name='Owen Lars', appearances=3, height=178, specie=None),
        Character(name='Luke Skywalker', appearances=4, height=172, specie=None),
        Character(name='Palpatine', appearances=5, height=170, specie=None),
        Character(name='C-3PO', appearances=6, height=167, specie=Specie(id=2, name='Droid')),
        Character(name='Leia Organa', appearances=4, height=150, specie=None),
        Character(name='R2-D2', appearances=6, height=96, specie=Specie(id=2, name='Droid')),
        Character(name='Yoda', appearances=5, height=66, specie=Specie(id=6, name="Yoda's species"))
    ]


@pytest.fixture
def csv_file_text() -> str:
    return "name,species,height,appearances\n" \
           "Chewbacca,Wookie,228,4\n" \
           "Darth Vader,,202,4\n" \
           "Obi-Wan Kenobi,,182,6\n" \
           "Owen Lars,,178,3\n" \
           "Luke Skywalker,,172,4\n" \
           "Palpatine,,170,5\n" \
           "C-3PO,Droid,167,6\n" \
           "Leia Organa,,150,4\n" \
           "R2-D2,Droid,96,6\n" \
           "Yoda,Yoda's species,66,5\n"
