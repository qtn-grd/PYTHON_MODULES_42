class Plant:
    """Represents a plant with a name, height (in cm), and age (in days)."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new Plant instance."""

        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        """Display the plant's information in a formatted string."""

        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """Create several Plant instances and display their information."""

    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)

    garden: list[Plant] = [rose, sunflower, cactus]

    print("=== Garden Plant Registry ===")
    for plant in garden:
        plant.show()


if __name__ == "__main__":
    main()
