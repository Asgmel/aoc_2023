from __future__ import annotations
from pathlib import Path
from typing import Optional

from aoc.utils.parse_input import get_input_to_use, read_input_as_list_of_strings


def run(input_path: Optional[Path]) -> None:
    input_to_use = get_input_to_use(day=2, input_path=input_path)
    puzzle_input = read_input_as_list_of_strings(input_path=input_to_use)

    task_one(input_data=puzzle_input)
    task_two(input_data=puzzle_input)


def task_one(input_data: list[str]) -> None:
    games = [Game(input_row) for input_row in input_data]
    print(f"Task one: {sum([game.id for game in games if game.check_game_validity(blue=14, red=12, green=13)])}")


def task_two(input_data: list[str]) -> None:
    games = [Game(input_row) for input_row in input_data]
    print(f"Task two: {sum([game.get_least_cube_power() for game in games])}")


class Round:
    blue = 0
    red = 0
    green = 0

    def __init__(self, blue: int = 0, red: int = 0, green: int = 0) -> None:
        self.blue = blue
        self.red = red
        self.green = green

    @staticmethod
    def get_rounds_from_string(input_string: str) -> list[Round]:
        rounds = []
        for game_round in input_string.split("; "):
            round_dict = {}
            for value in game_round.split(", "):
                value, color = value.split(" ")
                round_dict[color] = int(value)
            rounds.append(Round(**round_dict))
        return rounds


class Game:
    def __init__(self, input_row: str) -> None:
        self.id = int(input_row.split(":")[0].split(" ")[1])
        self.rounds = Round.get_rounds_from_string(input_string=input_row.split(": ")[1])

    def check_game_validity(self, blue: int, red: int, green: int) -> bool:
        for game_round in self.rounds:
            if game_round.blue > blue or game_round.red > red or game_round.green > green:
                return False
        return True

    def get_least_cube_power(self) -> int:
        blue = 0
        red = 0
        green = 0

        for game_round in self.rounds:
            blue = game_round.blue if game_round.blue > blue else blue
            red = game_round.red if game_round.red > red else red
            green = game_round.green if game_round.green > green else green

        return blue * red * green


if __name__ == "__main__":
    run(input_path=None)
