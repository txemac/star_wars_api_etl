# Star Wars API ETL

Task using the Star Wars API (swapi)

[![CI](https://github.com/txemac/star_wars_api_etl/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/txemac/star_wars_api_etl/actions/workflows/ci.yml)

# Run

- generate virtual environment

```shell
python3 -m venv env
```

- activate environment

```shell
source env/bin/activate
```

- update and install requirements

```shell
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install -r test-requirements.txt
```

- run

```shell
python3 main.py
```

## Output

```text
Hello! Welcome to Star Wars API ETL

Step 0: Get all characters from external API -> Starting...
Step 0: Finish. Total characters: 82

Step 1: Find the ten characters who appear in the most Star Wars films -> Starting...
Step 1: Finish. Winner: C-3PO

Step 2: Sort those ten characters by height in descending order (i.e., tallest first) -> Starting...
Step 2: Finish. Taller between most appearances: Chewbacca

Step 3: Produce a CSV with the following columns: name, species, height, appearances -> preparing data...
Step 3: Generating csv...
Step 3: CSV file generated

Step 4: Send the CSV to httpbin.org -> Sending...
Step 4: Upload CSV file success
```

## Tests

```shell
pytest -vvv
```

```text
(env) % pytest -vvv
============================= test session starts ==============================
collecting ... collected 9 items

test_main.py::test_sort_by_appearances PASSED                            [ 11%]
test_main.py::test_sort_by_height PASSED                                 [ 22%]
test_main.py::test_csv_file PASSED                                       [ 33%]
infrastructure/adapters/test_start_wars_api_adapter.py::test_sort_characters_by_appearances_ok PASSED [ 44%]
infrastructure/adapters/test_start_wars_api_adapter.py::test_sort_characters_by_appearances_with_limit PASSED [ 55%]
infrastructure/adapters/test_start_wars_api_adapter.py::test_sort_characters_taller_ok PASSED [ 66%]
infrastructure/adapters/test_start_wars_api_adapter.py::test_sort_characters_taller_with_limit PASSED [ 77%]
infrastructure/serializers/test_character_serializer.py::test_character_serializer PASSED [ 88%]
infrastructure/transforms/test_start_wars_api_character.py::test_transform PASSED [100%]

============================== 9 passed in 0.04s ===============================
```
