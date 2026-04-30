class Plant:
    """Represents a plant with a name, height (in cm), and age (in days)."""

    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a new Plant instance."""

        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        """Print the plant's current information."""

        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self, growing: float) -> None:
        """Increase the plant's height."""

        self.height += growing

    def grow_older(self, aging: int) -> None:
        """Increase the plant's age."""

        self.age += aging


def main() -> None:
    """Simulate the growth of a plant over several days."""

    rose = Plant("rose", 25.0, 30)

    print("=== Garden Plant Growth ===")
    rose.show()

    days: int = 7
    growing: float = 0.8

    for day in range(1, days + 1):
        print(f"=== Day {day} ===")
        rose.grow(growing)
        rose.grow_older(1)
        rose.show()

    print(f"Growth this week: {days * growing:.1f}cm")


if __name__ == "__main__":
    main()
