RED = "\033[31m"
RESET = "\033[0m"


class GardenError(Exception):
    """Base exception for all garden-related errors.
    This class serves as the parent for more specific garden exceptions,
    allowing grouped exception handling when needed."""

    def __init__(self, message="Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Exceptions raised for plant-related issues."""

    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Exceptions raised for watering-related issues."""

    def __init__(self, message="Unknown water error") -> None:
        super().__init__(message)


class Plant:
    """Represents a plant with health and water level."""

    def __init__(self, name: str, health: int, water: int) -> None:
        """Initialize a Plant instance."""

        self._name = name
        self._health = health
        self._water = water

    def check_stats(self) -> None:
        """Validate the plant's health and water levels."""

        if self._health <= 0:
            raise PlantError(f"The {self._name} plant is wilting!")

        elif self._water <= 0:
            raise WaterError("Not enough water in the tank!")


def main() -> None:
    """Entry point of the program."""

    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        tomato = Plant("tomato", -10, 5)
        tomato.check_stats()
    except PlantError as error:
        print(f"Caught {RED}PlantError{RESET}: {error}")
    print()

    print("Testing WaterError...")
    try:
        tomato = Plant("tomato", 10, -5)
        tomato.check_stats()
    except WaterError as error:
        print(f"Caught {RED}WaterError{RESET}: {error}")
    print()

    print("Testing catching all garden errors...")
    try:
        tomato = Plant("tomato", -10, 5)
        tomato.check_stats()
    except GardenError as error:
        print(f"Caught {RED}GardenError{RESET}: {error}")
    try:
        lettuce = Plant("lettuce", 10, -5)
        lettuce.check_stats()
    except GardenError as error:
        print(f"Caught {RED}GardenError{RESET}: {error}")
    print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
