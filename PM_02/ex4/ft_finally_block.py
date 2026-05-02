GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"


class PlantError(Exception):
    """Exceptions raised for plant-related errors."""

    def __init__(self, message="Unknown PlantError") -> None:
        super().__init__(message)


class Plant:
    """Represents a plant with a name and health value."""

    def __init__(self, name: str, health: int) -> None:
        """Initialize a plant instance"""

        self._name = name
        self._health = health


def water_plant(plant_name: str) -> None:
    """Attempt to water a plant.
    The operation succeeds only if the plant name is correctly capitalized.
    Otherwise, a PlantError is raised."""

    if plant_name.capitalize() == plant_name:
        print(f"Watering {YELLOW}{plant_name}{RESET}: {GREEN}[OK]{RESET}")
    else:
        raise PlantError(f"{RED}Invalid plant name to water{RESET}:"
                         f"{YELLOW}{plant_name}{RESET}")


def test_watering_system() -> None:
    """Test the watering system with valid and invalid plant names."""

    valid_list = [
        Plant("Tomato", 12),
        Plant("Lettuce", 10),
        Plant("Carrots", 15)
        ]
    invalid_list = [
        Plant("Onion", 12),
        Plant("lettuce", 10),
        Plant("Salad", 7)
        ]

    print("Testing valid plants...")
    print()
    print("Opening watering system")

    try:
        for plant in valid_list:
            water_plant(plant._name)
    except PlantError:
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

    print()
    print()

    print("Testing invalid plants...")
    print()
    print("Opening watering system")

    try:
        for plant in invalid_list:
            water_plant(plant._name)
    except PlantError as error:
        print(f"Caught {RED}PlantError{RESET}: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    """Entry point of the program."""

    print("=== Garden Watering System ===")
    print()
    print()

    test_watering_system()

    print()
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
