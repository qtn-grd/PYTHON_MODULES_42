#!/usr/bin/env python3


def achievement_tracker() -> None:
    """Analyze player achievements using set operations."""

    print("=== Achievement Tracker System ===")
    print()

    alice_set: set[str] = {
        'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob_set: set[str] = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie_set: set[str] = {
        'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
        'perfectionist'
    }

    print(f"Player alice achievements: {alice_set}")
    print(f"Player bob achievements: {bob_set}")
    print(f"Player charlie achievements: {charlie_set}")

    print()
    print("=== Achievement Analytics ===")
    print()

    union_set: set[str] = alice_set.union(bob_set, charlie_set)
    total_intersection_set: set[str] = alice_set.intersection(
        bob_set, charlie_set)

    alice_bob_intersection_set: set[str] = alice_set.intersection(bob_set)
    alice_charlie_intersection_set: set[str] = alice_set.intersection(
        charlie_set)
    bob_charlie_intersection_set: set[str] = bob_set.intersection(
        charlie_set)

    alice_bob_difference_set: set[str] = alice_set.difference(bob_set)
    bob_alice_difference_set: set[str] = bob_set.difference(alice_set)

    shared_by_any_two: set[str] = (
        alice_bob_intersection_set
        .union(alice_charlie_intersection_set)
        .union(bob_charlie_intersection_set)
    )

    rarity_set: set[str] = union_set.difference(shared_by_any_two)

    print(f"All unique achievements: {union_set}")
    print(f"Total unique achievements: {len(union_set)}")
    print()

    print(f"Common to all players: {total_intersection_set}")
    print(f"Rare achievements (1 player): {rarity_set}")
    print()

    print(f"Alice vs Bob common: {alice_bob_intersection_set}")
    print(f"Alice unique: {alice_bob_difference_set}")
    print(f"Bob unique: {bob_alice_difference_set}")


if __name__ == "__main__":
    achievement_tracker()
