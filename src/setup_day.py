import argparse
import os


def setup_day(day: int) -> None:
    """
    Setup the day by creating the input file and the module file.
    """
    day_str = str(day)
    module_file = f"src/day_{day_str}.py"
    input_file = f"inputs/day_{day_str}_input.txt"
    test_file = f"inputs/day_{day_str}_input_test.txt"

    if os.path.exists(module_file):
        print(f"Day {day} already exists.")
        return

    # create the files
    with open(module_file, "w") as file:
        file.write(f"# Path: src/day_{day_str}.py\n")
        file.write("# --- Part One ---\n\n")
        file.write("def part_1(file_path: str) -> int:\n")
        file.write('    """\n')
        file.write("    Read the input file and return the solution.\n")
        file.write('    """\n\n')
        file.write("    return 0\n\n")
        file.write("# --- Part Two ---\n\n")
        file.write("def part_2(file_path: str) -> int:\n")
        file.write('    """\n')
        file.write("    Read the input file and return the solution.\n")
        file.write('    """\n\n')
        file.write("    return 0\n")

    with open(input_file, "w") as file:
        file.write("")

    with open(test_file, "w") as file:
        file.write("")

    print(f"Day {day} created.")


if __name__ == "__main__":
    argsparse = argparse.ArgumentParser()
    argsparse.add_argument(
        "--day", type=int, help="The day of the challenge to setup.", required=True
    )
    day = argsparse.parse_args().day
    setup_day(day)
