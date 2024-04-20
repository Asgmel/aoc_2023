import importlib
from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

day_modules = []

#  Import all day modules to the day_modules list

for i in range(1, 25):
    module_name = f"day_0{i}" if i < 10 else f"day_{i}"
    day_modules.append(importlib.import_module(f"aoc.days.{module_name}.main"))

app = typer.Typer()


@app.command()
def run(
    day: Annotated[
        int,
        typer.Argument(
            min=1, max=24, help="Day of AOC to run. Must be between 1 and 24."
        ),
    ],
    input: Annotated[
        Optional[Path],
        typer.Option(help="Path to the file with the input data."),
    ] = None,
):
    day_modules[day - 1].run(input=input)


@app.command()
def test():
    print("This is a test function")


if __name__ == "__main__":
    app()
