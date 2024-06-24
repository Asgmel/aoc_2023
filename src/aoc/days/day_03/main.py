from __future__ import annotations
from pathlib import Path
from typing import Optional

from aoc.utils.parse_input import get_input_to_use, read_input_as_two_dimensional_array


def run(input_path: Optional[Path]) -> None:
    input_to_use = get_input_to_use(day=3, input_path=input_path)
    puzzle_input = read_input_as_two_dimensional_array(input_path=input_to_use)

    task_one(input_data=puzzle_input)
    task_two(input_data=puzzle_input)


def task_one(input_data: list[list[str]]) -> None:
    print(summarize_part_numbers(part_matrix=input_data))


def task_two(input_data: list[list[str]]) -> None:
    print(input_data)


def summarize_part_numbers(part_matrix: list[list[str]]) -> int:
    part_sum = 0
    current_number = ""

    for row_index, row in enumerate(part_matrix):
        for column_index, letter in enumerate(row):
            if letter.isdigit():
                current_number += letter
            if not letter.isdigit() or column_index == len(row) - 1:
                if current_number != "" and number_adjacent_to_symbol(
                    part_matrix=part_matrix,
                    current_row_index=row_index,
                    column_index_start=column_index - len(current_number),
                    column_index_end=column_index - 1
                ):
                    part_sum += int(current_number)
                current_number = ""

    return part_sum


def number_adjacent_to_symbol(
    part_matrix: list[list[str]],
    current_row_index: int,
    column_index_start: int,
    column_index_end: int,
) -> bool:
    row_index_range = range(
        current_row_index - 1 if current_row_index != 0 else current_row_index,
        current_row_index + 2 if current_row_index < len(part_matrix) - 1 else current_row_index + 1
    )

    column_index_range = range(
        column_index_start - 1 if column_index_start != 0 else column_index_start,
        column_index_end + 2 if column_index_end != len(part_matrix[current_row_index]) - 1 else column_index_end + 1
    )

    for row_index in row_index_range:
        for column_index in column_index_range:
            if part_matrix[row_index][column_index] != "." and not part_matrix[row_index][column_index].isdigit():
                return True
    return False


if __name__ == "__main__":
    run(input_path=None)
