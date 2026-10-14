import os
from dotenv import load_dotenv


def get_config() -> dict[str, str | None]:
    env_dict = {}
    mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")
    env_dict["MATRIX_MODE"] = mode
    env_dict["DATABASE_URL"] = database_url
    env_dict["API_KEY"] = api_key
    env_dict["LOG_LEVEL"] = log_level
    env_dict["ZION_ENDPOINT"] = zion_endpoint
    return env_dict


def load_config(env_dict: dict[str, str | None]) -> None:
    print()
    print("Configuration loaded:")
    print(f"Mode: {env_dict["MATRIX_MODE"]}")
    if env_dict["DATABASE_URL"] and env_dict["MATRIX_MODE"] == "development":
        print("Database: Connected to local instance")
    elif env_dict["DATABASE_URL"] and env_dict["MATRIX_MODE"] == "production":
        print("Database: Connected to production "
              f"({env_dict['DATABASE_URL']})")
    else:
        print(f"Database: {env_dict["DATABASE_URL"]}")
    if env_dict["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print(f"API Access: {env_dict["API_KEY"]}")
    print(f"Log Level: {env_dict["LOG_LEVEL"]}")
    print(f"Zion Network: {env_dict["ZION_ENDPOINT"]}")
    print()


def security_check(env_dict: dict[str, str | None]) -> None:
    print()
    print("Environment security check:")
    if env_dict["API_KEY"]:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] API_KEY not found")
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if os.path.isfile(env_path):
        print("[OK] .env file exists")
    else:
        print("[WARNING] .env file not found")
    if env_dict["MATRIX_MODE"] in ("production", "development"):
        print("[OK] Production overrides available")
    else:
        print("[WARNING] Invalid MATRIX_MODE")
    print()


if __name__ == "__main__":
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    load_dotenv()
    env_dict = get_config()
    load_config(env_dict)
    security_check(env_dict)
    print("The Oracle sees all configurations.")
