"""
Main module for Advent of Code 2020
"""

import argparse
import os
from typing import Callable


def run_day(day_index: int, part: int) -> Callable:
    """'
    Programmatically run the challenge for the given day and part.
    """

    # check that the module exists
    if not os.path.exists(f"src/day_{day_index}.py"):
        raise ValueError(f"Day {day_index} module not found.")

    module = __import__(f"day_{day_index}")
    if part == 1:
        return module.part_1
    elif part == 2:
        return module.part_2
    else:
        raise ValueError("Invalid part selected.")


if __name__ == "__main__":
    argsparse = argparse.ArgumentParser()
    argsparse.add_argument(
        "--day", type=int, help="The day of the challenge to run.", required=True
    )
    argsparse.add_argument(
        "--test",
        help="Run the test cases for the challenge.",
        action="store_true",
    )
    argsparse.add_argument(
        "--part", type=int, help="The part of the challenge to run.", required=True
    )

    args = argsparse.parse_args()
    day = args.day
    part = args.part
    test = args.test

    file_path = f"inputs/day_{day}_input" + ("_test" if test else "") + ".txt"

    if not os.path.exists(file_path):
        raise ValueError(f"File not found: {file_path}")

    print(run_day(day, part)(file_path))
