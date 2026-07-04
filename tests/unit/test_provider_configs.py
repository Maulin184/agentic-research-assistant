import pytest
from pydantic import ValidationError

from src.config.config_models import (
    ProviderConfig,
)


def test_provider_config():

    config = ProviderConfig(
        api_base="https://example.com",
        timeout=60,
        max_retries=2,
    )

    assert config.api_base == "https://example.com"
    assert config.timeout == 60
    assert config.max_retries == 2


def test_timeout_validation():

    with pytest.raises(ValidationError):

        ProviderConfig(
            api_base="https://example.com",
            timeout=0,
            max_retries=2,
        )


def test_retry_validation():

    with pytest.raises(ValidationError):

        ProviderConfig(
            api_base="https://example.com",
            timeout=60,
            max_retries=-1,
        )