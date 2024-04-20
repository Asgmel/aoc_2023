from pathlib import Path
from typing import Optional


def read_input_as_string(input: Optional[Path]) -> str:
    with open(input if input else "input.txt", "r", encoding="utf-8") as file:
        file_contents = file.read()

    return file_contents


def read_input_as_list_of_strings(input: Path) -> list[str]:
    string_input = read_input_as_string(input=input)
    return string_input.split("\n")
