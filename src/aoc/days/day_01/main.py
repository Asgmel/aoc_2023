from pathlib import Path
from typing import Optional

from aoc.utils.parse_input import get_input_to_use, read_input_as_list_of_strings


def run(input_path: Optional[Path]) -> None:
    input_to_use = get_input_to_use(day=1, input_path=input_path)
    puzzle_input = read_input_as_list_of_strings(input_path=input_to_use)

    task_one(input_data=puzzle_input)
    task_two(input_data=puzzle_input)


def task_one(input_data: list[str]) -> None:
    numbers = get_string_numbers_from_input(input_data=input_data)
    numbers_sum = get_sum_from_string_numbers(numbers=numbers)

    print(f"Task one puzzle answer is: {numbers_sum}")


def task_two(input_data: list[str]) -> None:
    transformed_input_data = [replace_text_numbers(row=row) for row in input_data]
    numbers = get_string_numbers_from_input(input_data=transformed_input_data)
    numbers_sum = get_sum_from_string_numbers(numbers=numbers)

    print(f"Task one puzzle answer is: {numbers_sum}")


def get_sum_from_string_numbers(numbers: list[list[str]]) -> int:
    if len(numbers) == 0:
        raise ValueError("Invalid input data. Unable to handle row without numbers")

    return sum([int(row[0] + row[-1]) for row in numbers])


def get_string_numbers_from_input(input_data: list[str]) -> list[list[str]]:
    return [[number for number in row if number.isdigit()] for row in input_data]


def replace_text_numbers(row: str) -> str:
    # Replacing the number with TextNumberText so that we do not break any adjacent text numbers.
    # I.e. TwOne will become two2twone1one, so we do not miss out on the 2 after we replace the one.
    text_numbers = {"one": "one1one", "two": "two2two", "three": "three3three", "four": "four4four",
                    "five": "five5five", "six": "six6six", "seven": "seven7seven",
                    "eight": "eight8eight", "nine": "nine9nine"}

    return_string = row

    for key in text_numbers.keys():
        return_string = return_string.replace(key, text_numbers[key])

    return return_string


if __name__ == "__main__":
    run(input_path=None)
