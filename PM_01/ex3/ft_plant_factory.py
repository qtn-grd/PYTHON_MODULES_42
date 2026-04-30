class Plant:
    """Represents a plant with a name, height (in cm), and age (in days)."""

    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a Plant instance."""

        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> str:
        """Return the plant's current information."""

        return (f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def plant_factory(name: str, height: float, age: int) -> Plant:
    """Create and return a Plant instance."""

    return Plant(name, height, age)


def main() -> None:
    """Create multiple plants using the factory and display them."""

    new = [
        ("rose", 25.0, 30),
        ("oak", 200.0, 365),
        ("cactus", 5.0, 90),
        ("sunflower", 80.0, 45),
        ("fern", 15.0, 120)
    ]

    for p_name, p_height, p_age in new:
        plant = plant_factory(p_name, p_height, p_age)
        print("Created:", plant.show())


if __name__ == "__main__":
    main()
