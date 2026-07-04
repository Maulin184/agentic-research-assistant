"""
Configuration package.

Loads and exposes validated configuration models.
"""

from .config_loader import load_yaml_config
from .config_models import (
    ModelsConfig,
    ProvidersConfig,
)
from .settings import (
    Settings,
    get_settings,
    settings,
)

models_config = ModelsConfig.model_validate(
    load_yaml_config("models.yaml")
)

providers_config = ProvidersConfig.model_validate(
    load_yaml_config("providers.yaml")
)

__all__ = [
    "Settings",
    "get_settings",
    "settings",
    "models_config",
    "providers_config",
]