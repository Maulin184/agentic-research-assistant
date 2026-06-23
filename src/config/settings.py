from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Centralized application settings.

    Values are loaded from environment variables
    and validated by Pydantic.
    """

    app_env: str = Field(
        default="development",
        description="Application environment",
    )

    debug: bool = Field(
        default=True,
        description="Enable debug mode",
    )

    log_level: str = Field(
        default="INFO",
        description="Application log level",
    )

    groq_api_key: str = Field(
        default="",
        description="Groq API key",
    )

    openrouter_api_key: str = Field(
        default="",
        description="OpenRouter API key",
    )

    langsmith_api_key: str = Field(
        default="",
        description="LangSmith API key",
    )

    langsmith_tracing: bool = Field(
        default=False,
        description="Enable LangSmith tracing",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Singleton settings instance.

    Prevents reloading environment variables
    multiple times during application lifetime.
    """
    return Settings()


settings = get_settings()