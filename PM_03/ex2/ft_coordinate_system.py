import math


def calculate_distance(
        one: tuple[float, float, float],
        two: tuple[float, float, float],
) -> float:
    """Compute the Euclidean distance between two 3D points."""

    X1, Y1, Z1 = one
    X2, Y2, Z2 = two

    return math.sqrt(
        (X1 - X2) ** 2 +
        (Y1 - Y2) ** 2 +
        (Z1 - Z2) ** 2
    )


def get_player_pos() -> tuple[float, float, float]:
    """Prompt the user to input 3D coordinates until valid input is provided.
    The expected format is 'x,y,z'. Each value must be convertible to float.
    Displays appropriate error messages for invalid syntax or values."""

    while True:

        coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': ")

        parts = coordinates.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            X = float(parts[0].strip())
            Y = float(parts[1].strip())
            Z = float(parts[2].strip())
            return X, Y, Z

        except ValueError as error:
            for elem in parts:
                try:
                    float(elem.strip())
                except ValueError:
                    print(f"Error on parameter {elem}: {error}")
                    break


def main() -> None:
    """Run the 3D coordinate system program."""

    print("=== Game Coordinate System ===")
    print()

    center = (0.0, 0.0, 0.0)

    print("Get a first set of coordinates")

    x1, y1, z1 = get_player_pos()
    first_set = (x1, y1, z1)

    print(f"Got a first tuple: {first_set}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    print("Distance to center: "
          f"{round(calculate_distance(first_set, center), 4)}")
    print()

    print("Get a second set of coordinates")

    x2, y2, z2 = get_player_pos()
    second_set = (x2, y2, z2)

    print("Distance between the 2 sets of coordinates: "
          f"{round(calculate_distance(second_set, first_set), 4)}")


if __name__ == "__main__":
    main()
