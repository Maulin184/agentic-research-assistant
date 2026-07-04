import pytest

from src.services.llm import (
    AuthenticationError,
    ContextWindowExceededError,
    InvalidResponseError,
    LLMError,
    ProviderError,
    RateLimitError,
)


def test_exceptions_are_llm_errors():

    exceptions = [
        ProviderError(),
        InvalidResponseError(),
        ContextWindowExceededError(),
        RateLimitError(),
        AuthenticationError(),
    ]

    for exc in exceptions:
        assert isinstance(exc, LLMError)


def test_raise_provider_error():

    with pytest.raises(ProviderError):
        raise ProviderError("Failure")