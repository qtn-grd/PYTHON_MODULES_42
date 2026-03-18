def validate_ingredients(ingredients: str) -> str:
    """Validates that the provided ingredients contain at least one
    recognized elemental component."""

    valid_elements = {"fire", "water", "earth", "air"}

    words = ingredients.split()

    if any(word in valid_elements for word in words):
        return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
