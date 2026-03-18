#!/usr/bin/env python3

from typing import Generator
import time


def game_event_stream(n: int) -> Generator[tuple[str, int, str], None, None]:
    """Generate a stream of game events for multiple players with individual
    levels."""

    level: int = 1
    players: list[str] = ["alice", "bob", "charlie"]
    player_iter = iter(players)

    for x in range(1, n + 1):

        try:
            player = next(player_iter)
        except StopIteration:
            player_iter = iter(players)
            player = next(player_iter)

        if x % 5 == 0:
            action = "leveled up!"
            level += 1
        elif x % 3 == 1:
            action = "found treasure!"
        else:
            action = "killed monster!"

        yield player, level, action


def fibonacci(limit: int) -> Generator[int, None, None]:
    """Generate Fibonacci sequence up to `limit` numbers."""

    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def prime_numbers(count: int) -> Generator[int, None, None]:
    """Generate the first `count` prime numbers."""

    num_found = 0
    candidate = 2

    while num_found < count:
        prime = True
        for i in range(2, int(candidate**0.5) + 1):
            if candidate % i == 0:
                prime = False
                break
        if prime:
            yield candidate
            num_found += 1
        candidate += 1


def stream_wizard(number: int) -> None:
    """Main function to process game events and show analytics."""

    print("=== Game Data Stream Processor ===")

    event_number = 0
    high_level = 0
    treasure = 0
    exp = 0

    print()
    print(f"Processing {number} game events...")
    print()
    for player, level, action in game_event_stream(number):

        event_number += 1

        if level >= 10:
            high_level += 1

        if action == "found treasure!":
            treasure += 1
        elif action == "leveled up!":
            exp += 1

        print(f"Event {event_number}: "
              f"Player {player} (level {level}) {action}")

    print()

    print("=== Stream Analytics ===")
    print()

    print(f"Total events processed: {number}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {exp}")


def main() -> None:
    """Run stream wizard and generator demonstrations."""

    print()
    number: int = 1000

    start: float = time.perf_counter()
    stream_wizard(number)
    end: float = time.perf_counter()

    print()
    elapsed_time: float = end - start

    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {elapsed_time:.4f} seconds")
    print()

    print("=== Generator Demonstrations ===")

    number = 10
    print(f"Fibonacci sequence (first {number}): ", end="")
    first = True
    for value in fibonacci(number):
        if not first:
            print(", ", end="")
        print(value, end="")
        first = False
    print()

    number = 5
    print(f"Prime numbers (first {number}): ", end="")
    first = True
    for value in prime_numbers(number):
        if not first:
            print(", ", end="")
        print(value, end="")
        first = False
    print()


if __name__ == "__main__":
    main()
