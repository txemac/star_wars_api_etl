from infrastructure.adapters.start_wars_api_adapter import StartWarsAPIAdapter

start_wars_api = StartWarsAPIAdapter()

print("Hello! Welcome to Start Wars API ETL")

print("Step 0: Get all characters from external API -> Starting...")
characters = start_wars_api.get_characters()
print(f"Step 0: Finish. Total characters: {len(characters)}")
