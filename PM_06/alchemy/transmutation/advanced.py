def philosophers_stone() -> str:
    """Creates the Philosopher's Stone by combining lead transmutation
    and a healing potion."""

    from .basic import lead_to_gold
    from ..potions import healing_potion

    lead_to_gold_result = lead_to_gold()
    healing_potion_result = healing_potion()

    return (
        f"Philosopher’s stone created using {lead_to_gold_result} "
        f"and {healing_potion_result}"
    )


def elixir_of_life() -> str:
    """Creates the Elixir of Life."""

    return "Elixir of life: eternal youth achieved!"
