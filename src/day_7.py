"""
--- Day 7: Bridge Repair ---
The Historians take you to a familiar rope bridge over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and stole all the operators from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).

For example:

190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.

Operators are always evaluated left-to-right, not according to precedence rules. Furthermore, numbers in the equations cannot be rearranged. Glancing into the jungle, you can see elephants holding two different types of operators: add (+) and multiply (*).

Only three of the above equations can be made true by inserting operators:

190: 10 19 has only one position that accepts an operator: between 10 and 19. Choosing + would give 29, but choosing * would give the test value (10 * 19 = 190).
3267: 81 40 27 has two positions for operators. Of the four possible configurations of the operators, two cause the right side to match the test value: 81 + 40 * 27 and 81 * 40 + 27 both equal 3267 (when evaluated left-to-right)!
292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.
The engineers just need the total calibration result, which is the sum of the test values from just the equations that could possibly be true. In the above example, the sum of the test values for the three equations listed above is 3749.

Determine which equations could possibly be true. What is their total calibration result?

--- Part Two ---
The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.

The concatenation operator (||) combines the digits from its left and right inputs into a single number. For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.

Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:

156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
192: 17 8 14 can be made true using 17 || 8 + 14.
Adding up all six test values (the three that could be made before using only + and * plus the new three that can now be made by also using ||) produces the new total calibration result of 11387.

Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their total calibration result?
"""

import argparse


def part_1(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = file.readlines()

    total = 0
    for line in lines:
        line = line.strip().split(":")
        test_value = int(line[0])
        numbers = list(map(int, line[1].split()))

        n_operators = len(numbers) - 1

        for i in range(2**n_operators):
            operators = [0] * n_operators
            for j in range(n_operators):
                if i & (1 << j):
                    operators[j] = 1

            result = numbers[0]
            for j in range(n_operators):
                if operators[j] == 0:
                    result += numbers[j + 1]
                else:
                    result *= numbers[j + 1]

            if result == test_value:
                total += test_value
                break

    return total


def part_2(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = file.readlines()

    total = 0
    for line in lines:
        line = line.strip().split(":")
        test_value = int(line[0])
        numbers = list(map(int, line[1].split()))

        n_operators = len(numbers) - 1

        for i in range(3**n_operators):
            operators = [0] * n_operators
            for j in range(n_operators):
                operators[j] = i // (3**j) % 3

            result = numbers[0]
            for j in range(n_operators):
                if operators[j] == 0:
                    result += numbers[j + 1]
                elif operators[j] == 1:
                    result *= numbers[j + 1]
                else:
                    result = int(str(result) + str(numbers[j + 1]))

            if result == test_value:
                total += test_value
                break

    return total


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

    if part == 1:
        print(part_1(file_path))
    elif part == 2:
        print(part_2(file_path))
    else:
        print("No valid option selected.")
