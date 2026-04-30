def garden_intro(name: str, height: int, age: int) -> None:
    """Display a simple introduction message for a plant."""

    print("=== Welcome to my garden ===")

    print("Plant:", name)
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    garden_intro("Rose", 25, 30)
