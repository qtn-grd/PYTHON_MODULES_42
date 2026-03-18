def record_spell(spell_name: str, ingredients: str) -> str:
    """Records a spell if its ingredients pass validation."""

    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)

    if "INVALID" in validation_result:
        return f"Spell rejected: {spell_name} ({validation_result})"

    return f"Spell recorded: {spell_name} ({validation_result})"
