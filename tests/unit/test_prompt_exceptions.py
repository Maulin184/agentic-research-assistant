from src.services.prompt import (
    MissingPromptVariableError,
    PromptError,
    PromptNotFoundError,
    PromptRenderingError,
)


def test_prompt_not_found_error_is_prompt_error() -> None:
    assert issubclass(PromptNotFoundError, PromptError)


def test_prompt_rendering_error_is_prompt_error() -> None:
    assert issubclass(PromptRenderingError, PromptError)


def test_missing_prompt_variable_error_is_rendering_error() -> None:
    assert issubclass(
        MissingPromptVariableError,
        PromptRenderingError,
    )