import random


def gen_player_achievements(achievements_pool: list[str]) -> set[str]:
    """Generate a random set of unique achievements for a player.
    A random number of achievements is selected from a predefined pool,
    ensuring no duplicates using random sampling."""

    return set(random.sample(
        achievements_pool, random.randrange(1, len(achievements_pool) + 1)))


def main() -> None:
    """Run the achievement tracking system."""

    print("=== Achievement Tracker System ===")
    print()

    achievements_pool = [
        'Crafting Genius', 'Strategist', 'World Savior',
        'Speed Runner', 'Survivor', 'Master Explorer',
        'Treasure Hunter', 'Unstoppable', 'First Steps',
        'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer']

    all_achievements = set(achievements_pool)
    alice = gen_player_achievements(achievements_pool)
    bob = gen_player_achievements(achievements_pool)
    charlie = gen_player_achievements(achievements_pool)
    dylan = gen_player_achievements(achievements_pool)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print()

    print(f"All distinct achievements: {all_achievements}")

    print()

    common_achievements = alice & bob & charlie & dylan
    print(f"Common achievements: {common_achievements}")

    print()

    print(f"Only Alice has: {alice.difference(bob | charlie | dylan)}")
    print(f"Only Bob has: {bob.difference(alice | charlie | dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice | bob | dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice | bob | charlie)}")

    print()

    print(f"Alice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")


if __name__ == "__main__":
    main()
