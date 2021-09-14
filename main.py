from src.infrastructure.adapters.start_wars_api_adapter import StartWarsAPIAdapter

start_wars_api = StartWarsAPIAdapter()

print("Hello! Welcome to Start Wars API ETL\n")

print("Step 0: Get all characters from external API -> Starting...")
characters = start_wars_api.get_characters()
print(f"Step 0: Finish. Total characters: {len(characters)}\n")

print("Step 1: Find the ten characters who appear in the most Star Wars films -> Starting...")
characters_sorted_by_appearances = start_wars_api.sort_characters_by_appearances(
    characters=characters,
    limit=10,
)
print(f"Step 1: Finish. Winner: {characters_sorted_by_appearances[0].name}")
