import sys
from enum import Enum
from datetime import datetime
from typing import Optional

from pydantic import Field, BaseModel, model_validator, ValidationError


class Rank(Enum):
    """
    Enumeration of possible crew ranks within a space mission.
    """

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """
    Model representing an individual crew member.

    Includes personal data, rank, specialization, and activity status.
    """

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """
    Model representing a space mission with its crew and constraints.

    Includes mission metadata and enforces complex validation rules
    on crew composition and mission feasibility.
    """

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(strict=True)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: Optional[str] = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_validation(self) -> "SpaceMission":
        """
        Validate mission-level business rules after field validation.

        Rules enforced:
        - Mission ID must start with 'M'
        - At least one Captain or Commander must be present
        - Long missions (> 365 days) require at least 50% experienced crew
        - All crew members must be active

        Raises:
            ValueError: If any validation rule is violated.
        """

        if not self.mission_id.startswith("M"):
            raise ValueError("ID Error detected.")

        team_leader: bool = False
        for member in self.crew:
            if member.rank in [Rank.CAPTAIN, Rank.COMMANDER]:
                team_leader = True
        if not team_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain."
            )

        if self.duration_days > 365:
            newbies: bool = True
            nbr_veteran: int = 0

            for member in self.crew:
                if member.years_experience >= 5:
                    nbr_veteran += 1

            if nbr_veteran >= (len(self.crew) / 2):
                newbies = False

            if newbies:
                raise ValueError("Mission requires more experienced members.")

        active_team: bool = all(member.is_active for member in self.crew)
        if not active_team:
            raise ValueError("Inactive members detected.")

        return self


def success() -> None:
    """
    Demonstrate a valid space mission configuration.
    """

    connor: CrewMember = CrewMember(
        member_id="sconnor",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=62,
        specialization="Mission Command",
        years_experience=43,
        is_active=True
    )

    smith: CrewMember = CrewMember(
        member_id="jsmith",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=53,
        specialization="Navigation",
        years_experience=27,
        is_active=True
    )

    johnson: CrewMember = CrewMember(
        member_id="ajohnson",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=70,
        specialization="Engineering",
        years_experience=47,
        is_active=True
    )

    good_team: SpaceMission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=900,
        crew=[connor, smith, johnson],
        budget_millions=2500.0
    )

    print("Valid mission created:")
    print()
    print(f"Mission: {good_team.mission_name}")
    print(f"ID: {good_team.mission_id}")
    print(f"Destination: {good_team.destination}")
    print(f"Duration: {good_team.duration_days} days")
    print(f"Budget: ${good_team.budget_millions}M")
    print(f"Crew size: {len(good_team.crew)}")
    print("Crew members:")
    for member in good_team.crew:
        print(
            f"- {member.name} ({member.rank.value}) "
            f"- {member.specialization}"
        )


def failure() -> None:
    """
    Demonstrate an invalid mission configuration triggering validation errors.
    """

    gairaud: CrewMember = CrewMember(
        member_id="qgairaud",
        name="Quentin Gairaud",
        rank=Rank.CADET,
        age=16,
        specialization="Physiotherapist",
        years_experience=12,
        is_active=True
    )

    smith: CrewMember = CrewMember(
        member_id="jsmith",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=53,
        specialization="Navigation",
        years_experience=27,
        is_active=True
    )

    johnson: CrewMember = CrewMember(
        member_id="ajohnson",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=70,
        specialization="Engineering",
        years_experience=47,
        is_active=True
    )

    bad_team: SpaceMission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=900,
        crew=[gairaud, smith, johnson],
        budget_millions=2500.0
    )

    print("Valid mission created:")
    print(f"Mission: {bad_team.mission_name}")
    print(f"ID: {bad_team.mission_id}")
    print(f"Destination: {bad_team.destination}")
    print(f"Duration: {bad_team.duration_days} days")
    print(f"Budget: ${bad_team.budget_millions}M")
    print(f"Crew size: {len(bad_team.crew)}")
    print("Crew members:")
    for member in bad_team.crew:
        print(
            f"- {member.name} ({member.rank.value}) "
            f"- {member.specialization}"
        )


def main() -> None:
    """
    Entry point of the program.

    Executes both valid and invalid mission scenarios and
    displays validation results.
    """

    print()
    print("Space Mission Crew Validation")
    print()
    print("=" * 40)
    print()

    try:
        success()
    except ValidationError as error:
        print("Expected validation error:", file=sys.stderr)
        print()
        first_error = error.errors()[0]
        print(first_error["msg"], file=sys.stderr)

    print()
    print("=" * 40)
    print()

    try:
        failure()
    except ValidationError as error:
        print("Expected validation error:", file=sys.stderr)
        print()
        errors = error.errors()
        msg = errors[0]["msg"]

        if msg.startswith("Value error, "):
            msg = msg.replace("Value error, ", "", 1)

        print(msg, file=sys.stderr)


if __name__ == "__main__":
    main()
