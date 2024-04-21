from pathlib import Path
from typing import Optional

from aoc.utils.parse_input import get_input_to_use, read_input_as_list_of_strings


def run(input: Optional[Path]) -> None:
    input_to_use = get_input_to_use(day=1, input=input)
    puzzle_input = read_input_as_list_of_strings(input=input_to_use)

    task_one(input=puzzle_input)


def task_one(input: list[str]) -> None:
    numbers = map(lambda row: list(filter(lambda y: y.isdigit(), row)), input)

    print(f"Puzzle answer is: { sum([row[0] + row[-1] for row in numbers]) }")
