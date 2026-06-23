from src.config.settings import settings


def test_settings_loaded():
    assert settings.app_env is not None
    assert settings.log_level is not None