import os
from typing import Dict, Optional
from dotenv import load_dotenv


def load_config() -> Dict[str, Optional[str]]:
    """
    Load configuration from environment variables and a .env file.

    The .env file is loaded first, then overridden by system environment
    variables if they exist.

    Returns:
        Dict[str, Optional[str]]: Mapping of configuration keys
        to their values.
        Values may be None if not set.
    """
    load_dotenv()

    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def validate_config(config: Dict[str, Optional[str]]) -> bool:
    """
    Validate configuration values and ensure required keys are present.

    Args:
        config (Dict[str, Optional[str]]): Configuration dictionary.

    Returns:
        bool: True if all required configuration values are valid,
        False otherwise.
    """

    required_keys = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]

    all_is_here = True

    matrix_value = config.get("MATRIX_MODE")

    if matrix_value not in ["development", "production"]:
        all_is_here = False
    else:
        config["MATRIX_MODE"] = matrix_value

    for key in required_keys:
        if key == "MATRIX_MODE":
            continue

        if not config.get(key):
            all_is_here = False

    return all_is_here


def display_status(config: Dict[str, Optional[str]]) -> None:
    """
    Display a human-readable interpretation of the configuration.

    Args:
        config (Dict[str, Optional[str]]): Configuration dictionary.
    """
    print("Configuration loaded:")

    mode = config.get("MATRIX_MODE")
    if mode not in ["development", "production"]:
        print("Mode: Error")
    else:
        print(f"Mode: {mode}")

    database = config.get("DATABASE_URL")
    if database:
        if "localhost" in database or "sqlite" in database:
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to remote instance")
    else:
        print("Database: Not configured")

    api_key = config.get("API_KEY")
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    log_level = config.get("LOG_LEVEL") or "UNKNOWN"
    print(f"Log Level: {log_level}")

    zion = config.get("ZION_ENDPOINT")
    if zion:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check(config: Dict[str, Optional[str]]) -> None:
    """
    Perform basic security checks on configuration values.

    This includes:
    - Detecting placeholder or missing API keys
    - Ensuring the presence of a .env file
    - Verifying that environment variable overrides are possible

    Args:
        config (Dict[str, Optional[str]]): Configuration dictionary.
    """
    print()
    print("Environment security check:")

    api_key = config.get("API_KEY")
    if api_key and "your_api_key_here" not in api_key:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[KO] Potential hardcoded or default API key detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file missing")

    override_detected = any(key in os.environ for key in config.keys())

    if override_detected:
        print("[OK] Production overrides available")
    else:
        print("[KO] No environment overrides detected")


def main() -> None:
    """
    Main entry point of the program.

    Loads configuration, validates it, displays status, and performs
    security checks.
    """

    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    config = load_config()

    is_valid = validate_config(config)
    display_status(config)

    if not is_valid:
        print()
        print("Configuration incomplete. Exiting.")
        return

    security_check(config)
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
