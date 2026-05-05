import random


def data_alchemist() -> None:
    """Demonstrate data transformations using
    list and dictionary comprehensions."""

    print("=== Game Data Alchemist ===")
    print()

    origin_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                   'Gregory', 'john', 'kevin', 'Liam']

    print(f"Initial list of players: {origin_list}")

    capitalize_all = [name.capitalize() for name in origin_list]
    print(f"New list with all names capitalized: {capitalize_all}")

    select_already_capitalized = [
        name for name in origin_list if name[0].isupper()]
    print(f"New list of capitalized names only: {select_already_capitalized}")
    print()

    initial_dict = {
        player: random.randint(1, 1000) for player in capitalize_all}
    print(f"Score dict: {initial_dict}")
    print()

    avg_value = round(sum(initial_dict.values()) / len(
        initial_dict), 2) if len(initial_dict) != 0 else 0
    print(f"Score average is {avg_value if avg_value else 0}")
    print()

    high_score_dict = {
        player: initial_dict[player] for player in initial_dict
        if initial_dict[player] >= avg_value}
    print(f"High scores: {high_score_dict}")
    print()


if __name__ == "__main__":
    data_alchemist()
