from pathlib import Path
from typing import TypeVar

from yaml import safe_load

T = TypeVar("T")


def get_file(path_to_file: Path, schema: type[T]) -> T:
    with open(path_to_file, "r") as file:
        return schema(**safe_load(file))
