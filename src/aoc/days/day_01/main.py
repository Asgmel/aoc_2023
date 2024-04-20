from pathlib import Path
from typing import Optional

from aoc.utils.parse_input import read_input_as_list_of_strings


def run(input: Optional[Path]):
    puzzle_input = read_input_as_list_of_strings(input=input)
    print(puzzle_input[0])
