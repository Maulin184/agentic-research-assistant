"""
Prompt service exceptions.

This module defines the custom exception hierarchy for the Prompt
Service.

Using domain-specific exceptions improves:

- Debugging
- Error handling
- Log readability
- Future extensibility

All prompt-related exceptions inherit from PromptError.
"""


class PromptError(Exception):
    """
    Base exception for all Prompt Service errors.
    """


class PromptNotFoundError(PromptError):
    """
    Raised when a prompt template file cannot be found.
    """


class PromptRenderingError(PromptError):
    """
    Raised when template rendering fails.
    """


class MissingPromptVariableError(PromptRenderingError):
    """
    Raised when one or more required template variables
    are missing during rendering.
    """