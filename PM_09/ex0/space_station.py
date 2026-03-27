import sys
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """
    Model representing a space station with validated operational data.
    """

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(strict=True)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    """
    Demonstrates validation of space station data.
    """

    print()
    print("Space Station Data Validation")
    print()
    print("=" * 40)
    print()

    try:
        good_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
        )

        print("Valid station created:")
        print()
        print(f"ID: {good_station.station_id}")
        print(f"Name: {good_station.name}")
        print(f"Crew: {good_station.crew_size} people")
        print(f"Power: {good_station.power_level}%")
        print(f"Oxygen: {good_station.oxygen_level}%")
        print("Status: Operational" if good_station.is_operational
              else "Status: Offline")

    except ValidationError as error:
        print()
        print("Expected validation error:", file=sys.stderr)
        print()
        first_error = error.errors()[0]
        print(first_error["msg"], file=sys.stderr)

    print()
    print("=" * 40)

    try:
        bad_station: SpaceStation = SpaceStation(
            station_id="BAD001",
            name="Broken Station",
            crew_size=50,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
        )

        print("Valid station created:")
        print()
        print(f"ID: {bad_station.station_id}")
        print(f"Name: {bad_station.name}")
        print(f"Crew: {bad_station.crew_size} people")
        print(f"Power: {bad_station.power_level}%")
        print(f"Oxygen: {bad_station.oxygen_level}%")
        print("Status: Operational" if bad_station.is_operational
              else "Status: Offline")

    except ValidationError as error:
        print()
        print("Expected validation error:", file=sys.stderr)
        print()
        for e in error.errors():
            print(e["msg"], file=sys.stderr)


if __name__ == "__main__":
    main()
