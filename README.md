# Start Wars API ETL

Task using the Star Wars API (swapi)

[![CI](https://github.com/txemac/start_wars_api_etl/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/txemac/start_wars_api_etl/actions/workflows/ci.yml)

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
Hello! Welcome to Start Wars API ETL

Step 0: Get all characters from external API -> Starting...
Step 0: Finish. Total characters: 82

Step 1: Find the ten characters who appear in the most Star Wars films -> Starting...
Step 1: Finish. Winner: C-3PO
```

## Tests

```shell
pytest -vvv
```

```text
(env) % pytest -vvv
============================= test session starts ==============================
collecting ... collected 7 items

test_main.py::test_sort_by_appearances PASSED                            [ 14%]
test_main.py::test_sort_by_height PASSED                                 [ 28%]
infrastructure/adapters/test_start_wars_api_adapter.py::test_sort_characters_by_appearances_ok PASSED [ 42%]
infrastructure/adapters/test_start_wars_api_adapter.py::test_sort_characters_by_appearances_with_limit PASSED [ 57%]
infrastructure/adapters/test_start_wars_api_adapter.py::test_sort_characters_taller_ok PASSED [ 71%]
infrastructure/adapters/test_start_wars_api_adapter.py::test_sort_characters_taller_with_limit PASSED [ 85%]
infrastructure/transforms/test_start_wars_api_character.py::test_transform PASSED [100%]

============================== 7 passed in 0.02s ===============================
```
