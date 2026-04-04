import sys
from typing import List, Dict, Any


artifacts: List[Dict[str, Any]] = [
    {'name': 'Storm Crown', 'power': 119, 'type': 'armor'},
    {'name': 'Shadow Blade', 'power': 67, 'type': 'accessory'},
    {'name': 'Wind Cloak', 'power': 101, 'type': 'armor'},
    {'name': 'Storm Crown', 'power': 101, 'type': 'weapon'}]

mages: List[Dict[str, Any]] = [
    {'name': 'Riley', 'power': 71, 'element': 'fire'},
    {'name': 'Phoenix', 'power': 85, 'element': 'ice'},
    {'name': 'Jordan', 'power': 78, 'element': 'earth'},
    {'name': 'Casey', 'power': 96, 'element': 'ice'},
    {'name': 'Nova', 'power': 83, 'element': 'ice'}]

spells: List[str] = ['tornado', 'shield', 'fireball', 'darkness']


def artifact_sorter(artifacts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Sort artifacts by power in descending order."""

    return sorted(
        artifacts, key=lambda artifact: artifact['power'], reverse=True)


def test_artifact_sorter() -> None:
    """Test artifact sorting functionality."""

    print("=" * 42)
    print("*", " " * 5, "Testing artifact sorter...", " " * 5, "*")
    print("=" * 42)

    print()
    print()

    print("Artifacts unsorted:")
    print()
    for artifact in artifacts:
        print(artifact)
    print()
    print()

    print("Artifacts sorted by power in reverse order:")
    print()

    sorted_artifacts = artifact_sorter(artifacts)

    for artifact in sorted_artifacts:
        print(
            f" - {artifact['name']}, {artifact['power']}, {artifact['type']}")

    print()


def power_filter(
        mages: List[Dict[str, Any]], min_power: int) -> List[Dict[str, Any]]:
    """Filter mages based on a minimum power threshold."""

    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def test_power_filter() -> None:
    """Test mage filtering by power."""

    print("=" * 42)
    print("*", " " * 7, "Testing power filter...", " " * 6, "*")
    print("=" * 42)

    print()
    print()

    print("All mages:")
    print()
    for mage in mages:
        print(mage)
    print()
    print()

    min_power = 80
    filtered = power_filter(mages, min_power)

    print(f"Only powerful mages (>= {min_power}):")
    print()
    for mage in filtered:
        print(f" - {mage['name']}, {mage['power']}, {mage['element']}")

    print()


def spell_transformer(spells: List[str]) -> List[str]:
    """Transform spells into an enhanced display format."""

    return list(map(lambda spell: f"* {spell} *", spells))


def test_spell_transformer() -> None:
    """Test spell transformation."""

    print("=" * 42)
    print("*", " " * 4, "Testing spell transformer...", " " * 4, "*")
    print("=" * 42)

    print()
    print()

    print("Basic spells:")
    print()
    for spell in spells:
        print(spell)
    print()
    print()

    print("Enhanced spells:")
    print()
    transformed = spell_transformer(spells)
    for spell in transformed:
        print(spell)

    print()


def mage_stats(mages: List[Dict[str, Any]]) -> Dict[str, float]:
    """Compute statistics on mage power levels."""

    if not mages:
        raise ValueError("Mage list cannot be empty")

    powers = list(map(lambda mage: mage['power'], mages))

    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


def test_mage_stats() -> None:
    """Test mage statistics computation."""

    print("=" * 42)
    print("*", " " * 5, "Testing mage statistics...", " " * 5, "*")
    print("=" * 42)

    print()
    print()

    print("Mages list:")
    print()

    for mage in mages:
        print(mage)

    print()
    print()
    print("Stats acquired:")
    print()
    statistics = mage_stats(mages)
    for key, value in statistics.items():
        print(f"{key} = {value}")

    print()


def main() -> None:
    """Run all tests with error handling."""

    print()
    try:
        test_artifact_sorter()
        print()
    except Exception as error:
        print(f"Error in test_artifact_sorter: {error}", file=sys.stderr)
        sys.exit()
    print()

    print()
    try:
        test_power_filter()
        print()
    except Exception as error:
        print(f"Error in test_power_filter: {error}", file=sys.stderr)
        sys.exit()
    print()

    print()
    try:
        test_spell_transformer()
        print()
    except Exception as error:
        print(f"Error in test_spell_transformer: {error}", file=sys.stderr)
        sys.exit()
    print()

    print()
    try:
        test_mage_stats()
        print()
    except Exception as error:
        print(f"Error in test_mage_stats: {error}", file=sys.stderr)
        sys.exit()
    print()


if __name__ == "__main__":
    main()
