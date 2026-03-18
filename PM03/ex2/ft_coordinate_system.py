#!/usr/bin/env python3

import sys
import math


def calculate_distance(
        one: tuple[float, float, float],
        two: tuple[float, float, float]
) -> float:
    """Compute the Euclidean distance between two 3D points."""
    x1, y1, z1 = one
    x2, y2, z2 = two

    result = math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )

    return result


def parse_coordinates(
    coord: list[str],
) -> tuple[
    tuple[float, float, float],
    tuple[float, float, float],
]:
    """Parse command-line arguments into two 3D points."""

    splited_coord: list[str] = []

    for elem in coord:
        transite_coord: list[str] = elem.split()
        for new in transite_coord:
            splited_coord.append(new)

    try:
        values = [float(x) for x in splited_coord]
    except ValueError as error:
        raise ValueError(f"{error}")

    if len(values) not in (3, 6):
        raise ValueError("invalid number of coordinates, "
                         "please enter 3 or 6 numeric values")

    if len(values) == 3:
        start = tuple([0.0, 0.0, 0.0])
        end = tuple(values)
    else:
        start = tuple([values[0], values[1], values[2]])
        end = tuple([values[3], values[4], values[5]])

    return start, end


def game_coordinate() -> None:
    """Entry point for the coordinate distance calculator."""

    print("=== Game Coordinate System ===")
    print()

    arguments: list[str] = sys.argv[1:]

    if not arguments:
        print("Error: missing coordinates, "
              "please enter 3 or 6 numeric values")
        return

    try:
        start, end = parse_coordinates(arguments)
    except ValueError as error:
        print(f"Error: parsing invalid coordinates: {arguments}")
        print(f"{error}")
        return

    print()
    print(f"Parsing coordinates {arguments}")
    print()
    print(f"Parse position one: {start}")
    print(f"Parse position two: {end}")
    print()

    distance = calculate_distance(start, end)

    print(f"Distance between position one and position two: {distance:.2f}")

    print()
    print()

    print("Unpacking demonstration:")
    print()
    print(f"Player at x={start[0]:.2f}, y={start[1]:.2f}, z={start[2]:.2f}")
    print(f"Coordinates: X={end[0]:.2f}, Y={end[1]:.2f}, Z={end[2]:.2f}")
    print()


if __name__ == "__main__":
    game_coordinate()
