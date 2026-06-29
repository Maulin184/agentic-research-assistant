from pathlib import Path

from src.services.prompt import PromptType
from src.services.prompt.service import PromptService


def test_get_system_prompt(tmp_path: Path):

    planner = tmp_path / "planner"

    planner.mkdir()

    (planner / "system.md").write_text(
        "Hello {{ name }}",
        encoding="utf-8",
    )

    service = PromptService(tmp_path)

    output = service.get_system_prompt(
        PromptType.PLANNER,
        {
            "name": "Maulin",
        },
    )

    assert output == "Hello Maulin"


def test_prompt_is_cached(tmp_path: Path):

    planner = tmp_path / "planner"

    planner.mkdir()

    prompt = planner / "system.md"

    prompt.write_text(
        "Hello {{ name }}",
        encoding="utf-8",
    )

    service = PromptService(tmp_path)

    service.get_system_prompt(
        PromptType.PLANNER,
        {
            "name": "One",
        },
    )

    prompt.write_text(
        "Modified",
        encoding="utf-8",
    )

    output = service.get_system_prompt(
        PromptType.PLANNER,
        {
            "name": "Two",
        },
    )

    assert output == "Hello Two"