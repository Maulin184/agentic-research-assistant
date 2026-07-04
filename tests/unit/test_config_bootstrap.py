from src.config import (
    models_config,
    providers_config,
)


def test_models_loaded():

    assert models_config.planner.provider == "groq"


def test_provider_loaded():

    assert "groq" in providers_config.root