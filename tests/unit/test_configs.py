from src.config.config_loader import load_yaml_config
from src.config.config_models import (
    LoggingConfig,
    ModelsConfig,
    ResearchWorkflowConfig,
)


def test_models_config_validation():
    data = load_yaml_config("models.yaml")

    config = ModelsConfig.model_validate(data)

    assert config.planner.provider == "groq"


def test_research_config_validation():
    data = load_yaml_config("research.yaml")

    config = ResearchWorkflowConfig.model_validate(data)

    assert config.planning.max_sections > 0


def test_logging_config_validation():
    data = load_yaml_config("logging.yaml")

    config = LoggingConfig.model_validate(data)

    assert config.development.renderer == "console"