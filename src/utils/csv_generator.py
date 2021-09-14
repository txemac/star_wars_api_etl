import csv
from typing import Dict
from typing import List


def create(
    path: str,
    headers: List[str],
    items: List[Dict]
) -> None:
    """
    Generate a CSV file.

    :param path: path of the file
    :param headers: headers at CSV
    :param items: rows
    :return: True if OK
    """
    with open(path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(items)
