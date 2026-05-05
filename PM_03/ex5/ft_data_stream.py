from typing import Generator
import random


def gen_event(list_players: list[str], list_events: list[str]) -> Generator:

    while True:
        yield (random.choice(list_players), random.choice(list_events))


def consume_event(built_list: list[tuple[str, str]]) -> Generator:

    while built_list:
        yield (built_list.pop(random.randrange(0, len(built_list))))


def main() -> None:
    print("=== Game Data Stream Processor ===")
    print()

    players = ["alice", "bob", "charlie", "dylan"]
    events = ["climb", "grab", "move", "release",
              "run", "sleep", "swim", "use"]

    generator_one = gen_event(players, events)

    for action in range(1000):
        player, event = next(generator_one)
        print(f"Event {action}: Player {player} did action {event}")

    print()

    list_one: list[tuple[str, str]] = []
    for _ in range(1, 11):
        list_one.append(next(generator_one))

    print(f"Built list of 10 events: {list_one}")
    print()

    for event in consume_event(list_one):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_one}")


if __name__ == "__main__":
    main()
