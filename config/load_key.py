import configparser
from pathlib import Path

_CONFIG_PATH = Path(__file__).parent / "config.ini"


def load_key(section: str, key: str) -> str:
    if not _CONFIG_PATH.exists():
        raise RuntimeError(f"Config file not found: {_CONFIG_PATH}")

    config = configparser.ConfigParser()
    config.read(_CONFIG_PATH)

    if section not in config:
        raise RuntimeError(f"Section [{section}] not found in config.ini")

    if key not in config[section]:
        raise RuntimeError(f"Key '{key}' not found in section [{section}]")

    return config[section][key]
