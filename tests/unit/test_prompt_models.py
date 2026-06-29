from src.services.prompt import PromptType


def test_prompt_type_values() -> None:
    """Prompt types should expose the expected directory names."""

    assert PromptType.PLANNER.value == "planner"
    assert PromptType.RESEARCHER.value == "researcher"
    assert PromptType.REVIEWER.value == "reviewer"
    assert PromptType.WRITER.value == "writer"
    assert PromptType.FINAL_REVIEWER.value == "final_reviewer"