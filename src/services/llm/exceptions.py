"""
LLM service exceptions.
"""


class LLMError(Exception):
    """Base exception for all LLM errors."""


class ProviderError(LLMError):
    """Provider execution failed."""


class InvalidResponseError(LLMError):
    """Provider returned an invalid response."""


class ContextWindowExceededError(LLMError):
    """Request exceeded the model context window."""


class RateLimitError(LLMError):
    """Rate limit exceeded."""


class AuthenticationError(LLMError):
    """Authentication failed."""