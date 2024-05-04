import inspect
from pathlib import Path
from typing import Optional

import aoc


def get_input_to_use(input_path: Optional[Path], day: int) -> Path:
    return input_path if input_path else get_input_path_from_day(day=day)


def get_input_path_from_day(day: int) -> Path:
    if day < 1 or day > 24:
        raise ValueError(
            f"Parameter 'day' to 'get_input_path_from_day' must be between 1 and 24. Value '{day}' not supported."
        )

    root_module_file_path = Path(inspect.getfile(aoc)).parent
    folder_name = f"day_0{day}" if day < 10 else f"day_{day}"
    return root_module_file_path / f"days/{folder_name}/input.txt"


def read_input_as_string(input_path: Path) -> str:
    with open(input_path, "r", encoding="utf-8") as file:
        file_contents = file.read()

    return file_contents


def read_input_as_list_of_strings(input_path: Path) -> list[str]:
    string_input = read_input_as_string(input_path=input_path)
    return string_input.split("\n")
