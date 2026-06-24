from pathlib import Path

import yaml


CONFIG_DIR = Path("configs")


def load_yaml_config(filename: str) -> dict:
    """
    Load YAML configuration file.
    """

    config_path = CONFIG_DIR / filename

    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )

    with open(
        config_path,
        "r",
        encoding="utf-8",
    ) as file:
        return yaml.safe_load(file)