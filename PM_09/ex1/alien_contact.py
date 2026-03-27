import sys
from enum import Enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(Enum):
    """
    Enumeration of possible alien contact types.
    """

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """
    Model representing an alien contact report with validation rules.
    """

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(strict=True)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact(self) -> "AlienContact":
        """
        Apply business validation rules for alien contact.
        """

        if not self.contact_id.startswith("AC"):
            raise ValueError("ID Error")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type == ContactType.TELEPATHIC
           and self.witness_count < 3):
            raise ValueError("Telepathic contact requires at least "
                             "3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must include a message")

        return self


def main() -> None:
    """
    Demonstrates alien contact validation.
    """

    print()
    print("Alien Contact Log Validation")
    print()
    print("=" * 40)
    print()

    try:
        valid_contact: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contact_type=ContactType.RADIO,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )

        print("Valid contact report:")
        print()
        print(f"ID: {valid_contact.contact_id}")
        print(f"Type: {valid_contact.contact_type.value}")
        print(f"Location: {valid_contact.location}")
        print(f"Signal: {valid_contact.signal_strength}/10")
        print(f"Duration: {valid_contact.duration_minutes} minutes")
        print(f"Witnesses: {valid_contact.witness_count}")
        print(f"Message: '{valid_contact.message_received}'")

    except ValidationError as error:
        print()
        print("Expected validation error:", file=sys.stderr)
        print()
        first_error = error.errors()[0]
        print(first_error["msg"], file=sys.stderr)

    print()
    print("=" * 40)

    try:
        invalid_contact: AlienContact = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            contact_type=ContactType.TELEPATHIC,
            location="Atlantis",
            signal_strength=9.7,
            duration_minutes=45,
            witness_count=2,
            message_received="Hungry..."
        )

        print("Valid contact report:")
        print()
        print(f"ID: {invalid_contact.contact_id}")
        print(f"Type: {invalid_contact.contact_type.value}")
        print(f"Location: {invalid_contact.location}")
        print(f"Signal: {invalid_contact.signal_strength}/10")
        print(f"Duration: {invalid_contact.duration_minutes} minutes")
        print(f"Witnesses: {invalid_contact.witness_count}")
        print(f"Message: '{invalid_contact.message_received}'")

    except ValidationError as error:
        print()
        print("Expected validation error:", file=sys.stderr)
        print()

        errors = error.errors()
        msg = errors[0]["msg"]

        if msg.startswith("Value error, "):
            msg = msg.replace("Value error, ", "", 1)

        print(msg, file=sys.stderr)


if __name__ == "__main__":
    main()
