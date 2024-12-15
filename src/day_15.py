"""
--- Day 15: Warehouse Woes ---
You appear back inside your own mini submarine! Each Historian drives their mini submarine in a different direction; maybe the Chief has his own submarine down here somewhere as well?

You look up to see a vast school of lanternfish swimming past you. On closer inspection, they seem quite anxious, so you drive your mini submarine over to see if you can help.

Because lanternfish populations grow rapidly, they need a lot of food, and that food needs to be stored somewhere. That's why these lanternfish have built elaborate warehouse complexes operated by robots!

These lanternfish seem so anxious because they have lost control of the robot that operates one of their most important warehouses! It is currently running amok, pushing around boxes in the warehouse with no regard for lanternfish logistics or lanternfish inventory management strategies.

Right now, none of the lanternfish are brave enough to swim up to an unpredictable robot so they could shut it off. However, if you could anticipate the robot's movements, maybe they could find a safe option.

The lanternfish already have a map of the warehouse and a list of movements the robot will attempt to make (your puzzle input). The problem is that the movements will sometimes fail as boxes are shifted around, making the actual movements of the robot difficult to predict.

For example:

##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
As the robot (@) attempts to move, if there are any boxes (O) in the way, the robot will also attempt to push those boxes. However, if this action would cause the robot or a box to move into a wall (#), nothing moves instead, including the robot. The initial positions of these are shown on the map at the top of the document the lanternfish gave you.

The rest of the document describes the moves (^ for up, v for down, < for left, > for right) that the robot will attempt to make, in order. (The moves form a single giant sequence; they are broken into multiple lines just to make copy-pasting easier. Newlines within the move sequence should be ignored.)

Here is a smaller example to get started:

########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
Were the robot to attempt the given sequence of moves, it would push around the boxes as follows:

Initial state:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move <:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#..@O..#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#...@O.#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#....@O#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########
The larger example has many more moves; after the robot has finished those moves, the warehouse would look like this:

##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########
The lanternfish use their own custom Goods Positioning System (GPS for short) to track the locations of the boxes. The GPS coordinate of a box is equal to 100 times its distance from the top edge of the map plus its distance from the left edge of the map. (This process does not stop at wall tiles; measure all the way to the edges of the map.)

So, the box shown below has a distance of 1 from the top edge of the map and 4 from the left edge of the map, resulting in a GPS coordinate of 100 * 1 + 4 = 104.

#######
#...O..
#......
The lanternfish would like to know the sum of all boxes' GPS coordinates after the robot finishes moving. In the larger example, the sum of all boxes' GPS coordinates is 10092. In the smaller example, the sum is 2028.

Predict the motion of the robot and boxes in the warehouse. After the robot is finished moving, what is the sum of all boxes' GPS coordinates?

--- Part Two ---
The lanternfish use your information to find a safe moment to swim in and turn off the malfunctioning robot! Just as they start preparing a festival in your honor, reports start coming in that a second warehouse's robot is also malfunctioning.

This warehouse's layout is surprisingly similar to the one you just helped. There is one key difference: everything except the robot is twice as wide! The robot's list of movements doesn't change.

To get the wider warehouse's map, start with your original map and, for each tile, make the following changes:

If the tile is #, the new map contains ## instead.
If the tile is O, the new map contains [] instead.
If the tile is ., the new map contains .. instead.
If the tile is @, the new map contains @. instead.
This will produce a new warehouse map which is twice as wide and with wide boxes that are represented by []. (The robot does not change size.)

The larger example from before would now look like this:

####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################
Because boxes are now twice as wide but the robot is still the same size and speed, boxes can be aligned such that they directly push two other boxes at once. For example, consider this situation:

#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
After appropriately resizing this map, the robot would push around these boxes as follows:

Initial state:
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############

Move <:
##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############

Move ^:
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############
This warehouse also uses GPS to locate the boxes. For these larger boxes, distances are measured from the edge of the map to the closest edge of the box in question. So, the box shown below has a distance of 1 from the top edge of the map and 5 from the left edge of the map, resulting in a GPS coordinate of 100 * 1 + 5 = 105.

##########
##...[]...
##........
In the scaled-up version of the larger example from above, after the robot has finished all of its moves, the warehouse would look like this:

####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################
The sum of these boxes' GPS coordinates is 9021.

Predict the motion of the robot and boxes in this new, scaled-up warehouse. What is the sum of all boxes' final GPS coordinates?
"""

import re

from loguru import logger


class Style:
    RED = "\033[31m"  # Red
    GREEN = "\033[32m"  # Green
    YELLOW = "\033[33m"  # Yellow
    BLUE = "\033[34m"  # Blue
    PURPLE = "\033[35m"  # Purple
    CYAN = "\033[36m"  # Cyan
    WHITE = "\033[37m"  # White

    RESET = "\033[0m"


class Position:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))


class Box:
    position: Position

    def __init__(self, x: int, y: int):
        self.position = Position(x, y)

    def plot(self):
        return Style.RED + "#" + Style.RESET

    def __hash__(self):
        return hash((self.position.x, self.position.y))

    def __str__(self):
        return f"Box({self.position.x}, {self.position.y})"

    def __repr__(self):
        return f"Box({self.position.x}, {self.position.y})"

    def __eq__(self, value):
        return (
            self.position.x == value.position.x and self.position.y == value.position.y
        )

    def get_score(self):
        return 100 * self.position.y + self.position.x


class Wall:
    position: Position

    def __init__(self, x: int, y: int):
        self.position = Position(x, y)

    def plot(self):
        return Style.BLUE + "#" + Style.RESET


class Robot:
    position: Position

    def __init__(self, x: int, y: int):
        self.position = Position(x, y)

    def plot(self):
        return Style.YELLOW + "@" + Style.RESET


class Movements:
    LEFT = "<"
    RIGHT = ">"
    UP = "^"
    DOWN = "v"
    sequence: list[str]

    def __init__(self, sequence: str):
        self.sequence = [x for x in sequence]

    @classmethod
    def get_dx_dy(cls, move: str):
        motions = {
            cls.LEFT: (-1, 0),
            cls.RIGHT: (1, 0),
            cls.UP: (0, -1),
            cls.DOWN: (0, 1),
        }
        return motions[move]


class Warehouse:
    width: int
    height: int
    boxes: list[Box]
    robot: Robot
    walls: list[Wall]
    movements: Movements

    def __init__(
        self,
        width: int,
        height: int,
        boxes: list,
        robot: Robot,
        walls: list,
        movements: Movements,
    ):
        self.width = width
        self.height = height
        self.boxes = boxes
        self.robot = robot
        self.walls = walls
        self.movements = movements

    def plot(self):
        warehouse = [["." for _ in range(self.width)] for _ in range(self.height)]
        for box in self.boxes:
            warehouse[box.position.y][box.position.x] = box.plot()
        warehouse[self.robot.position.y][self.robot.position.x] = self.robot.plot()
        for wall in self.walls:
            warehouse[wall.position.y][wall.position.x] = wall.plot()

        for row in warehouse:
            print("".join(row))
        print()

    def is_empty_at(self, x: int, y: int) -> bool:
        for box in self.boxes:
            if box.position.x == x and box.position.y == y:
                return False
        for wall in self.walls:
            if wall.position.x == x and wall.position.y == y:
                return False
        return True

    def is_wall_at(self, x: int, y: int) -> bool:
        for wall in self.walls:
            if wall.position.x == x and wall.position.y == y:
                return True
        return False

    def is_box_at(self, x: int, y: int) -> bool:
        for box in self.boxes:
            if box.position.x == x and box.position.y == y:
                return True
        return False

    def get_boxes_along(self, movement: str) -> list[Box]:
        dx, dy = Movements.get_dx_dy(movement)
        boxes = []
        increment = 1
        while True:
            new_x, new_y = (
                self.robot.position.x + dx * increment,
                self.robot.position.y + dy * increment,
            )

            if self.is_box_at(new_x, new_y):
                boxes.append(Box(new_x, new_y))
            elif self.is_wall_at(new_x, new_y):
                raise Exception("Wall in the way")
            elif self.is_empty_at(new_x, new_y):
                break
            else:
                raise Exception("Unknown object in the way")

            increment += 1

        return boxes

    def move_boxes(self, boxes_to_move: list[Box], movement: str):
        dx, dy = Movements.get_dx_dy(movement)
        moved_boxes = []
        for box in self.boxes:
            if box in boxes_to_move:
                new_x, new_y = box.position.x + dx, box.position.y + dy
                logger.debug(f"Moving box {box} to {new_x}, {new_y}")
                box.position.x = new_x
                box.position.y = new_y
                moved_boxes.append(box)
            else:
                logger.debug(f"Box {box} not moved, not found in {boxes_to_move}")
                moved_boxes.append(box)

        self.boxes = moved_boxes

    def move_robot(self, movement: str):
        dx, dy = Movements.get_dx_dy(movement)
        new_x, new_y = self.robot.position.x + dx, self.robot.position.y + dy
        self.robot.position.x = new_x
        self.robot.position.y = new_y
        logger.debug(f"Moving robot to {new_x}, {new_y}")

    @classmethod
    def from_input_file(cls, file_path: str):
        boxes = []
        robot = None
        walls = []
        movements = Movements("")
        with open(file_path, "r") as file:
            lines = file.readlines()
            width = len(lines[0].strip())
            height = 0
            for y, line in enumerate(lines):
                if line[0] == "#":
                    for x, char in enumerate(line.strip()):
                        if char == "O":
                            boxes.append(Box(x, y))
                        elif char == "@":
                            robot = Robot(x, y)
                        elif char == "#":
                            walls.append(Wall(x, y))
                    height += 1

                elif line == "":
                    # skip empty line
                    continue

                elif re.match(r"^[<v^>]+$", line.strip()):
                    movements.sequence += line.strip()

        assert robot is not None
        assert len(boxes) > 0
        assert len(walls) > 0
        assert len(movements.sequence) > 0

        return cls(width, height, boxes, robot, walls, movements)

    def run_simulation(self):
        while self.movements.sequence:
            move = self.movements.sequence.pop(0)
            logger.debug(f"Move: {move}")
            recursively_push(self, move)


def is_move_valid(warehouse: Warehouse, move: str):
    """
    Check that there is an empty space between the robot
    and the first wall in the direction of the move.
    """

    is_valid = False
    robot = warehouse.robot
    dx, dy = Movements.get_dx_dy(move)

    logger.debug(f"Robot position: {robot.position.x}, {robot.position.y}")
    logger.debug(f"Move: {move}")

    increment = 1

    while True:
        logger.debug(f"Checking increment {increment}")
        new_x, new_y = (
            robot.position.x + dx * increment,
            robot.position.y + dy * increment,
        )

        if warehouse.is_empty_at(new_x, new_y):
            is_valid = True
            break

        logger.debug(f"New position not empty: {new_x}, {new_y}")

        if (
            new_x < 0
            or new_x >= warehouse.width
            or new_y < 0
            or new_y >= warehouse.height
        ):
            raise Exception("Out of bounds")

        if warehouse.is_wall_at(new_x, new_y):
            is_valid = False
            break

        increment += 1

    return is_valid


def recursively_push(warehouse: Warehouse, move: str):
    if not is_move_valid(warehouse, move):
        logger.debug(f"Invalid move {move}")
        return None

    boxes_to_push = warehouse.get_boxes_along(move)
    logger.debug(f"Found {len(boxes_to_push)} boxes to push {boxes_to_push}")
    warehouse.move_boxes(boxes_to_push, move)
    warehouse.move_robot(move)

    # only plot if the global environment variable is set
    if "DEBUG" in globals():
        warehouse.plot()


# Path: src/day_15.py
# --- Part One ---


def part_1(file_path: str) -> int:
    """
    Read the input file and return the solution.
    """

    warehouse = Warehouse.from_input_file(file_path)

    warehouse.plot()

    warehouse.run_simulation()

    scores = [box.get_score() for box in warehouse.boxes]
    logger.debug(f"Scores: {scores}")

    warehouse.plot()

    return sum(scores)


# --- Part Two ---


def part_2(file_path: str) -> int:
    """
    Read the input file and return the solution.
    """

    return 0
