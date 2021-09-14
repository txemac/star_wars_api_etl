from src.infrastructure.adapters.httpbin_adapter import HTTPBinAdapter
from src.infrastructure.adapters.star_wars_api_adapter import StarWarsAPIAdapter
from src.infrastructure.serializers.character_serializer import CharacterSerializer
from src.utils import csv_generator

start_wars_api = StarWarsAPIAdapter()
httpbin_api = HTTPBinAdapter()

print("Hello! Welcome to Star Wars API ETL\n")

print("Step 0: Get all characters from external API -> Starting...")
characters = start_wars_api.get_characters()
print(f"Step 0: Finish. Total characters: {len(characters)}\n")

print("Step 1: Find the ten characters who appear in the most Star Wars films -> Starting...")
characters_sorted_by_appearances = start_wars_api.sort_characters_by_appearances(
    characters=characters,
    limit=10,
)
print(f"Step 1: Finish. Winner: {characters_sorted_by_appearances[0].name}\n")

print("Step 2: Sort those ten characters by height in descending order (i.e., tallest first) -> Starting...")
characters_sorted_by_height = start_wars_api.sort_characters_taller(
    characters=characters_sorted_by_appearances,
    limit=10,
)
print(f"Step 2: Finish. Taller between most appearances: {characters_sorted_by_height[0].name}\n")

print("Step 3: Produce a CSV with the following columns: name, species, height, appearances -> preparing data...")
for character in characters_sorted_by_height:
    if character.specie:
        character.specie.name = start_wars_api.get_specie_name_by_id(specie_id=character.specie.id)

print("Step 3: Generating csv...")
csv_generator.create(
    path="file.csv",
    headers=["name", "species", "height", "appearances"],
    items=CharacterSerializer.serialize_list(item_list=characters_sorted_by_height),
)
print("Step 3: CSV file generated\n")

print("Step 4: Send the CSV to httpbin.org -> Sending...")
send_file = httpbin_api.send_file(path="file.csv")
if send_file is True:
    print("Step 4: Upload CSV file success")
else:
    print("Step 4: ERROR uploading CSV file")
