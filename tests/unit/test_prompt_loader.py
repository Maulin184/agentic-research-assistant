from pathlib import Path

import pytest

from src.services.prompt import (
    PromptNotFoundError,
    PromptType,
    PromptRole
)
from src.services.prompt.loader import PromptLoader


def test_load_prompt(tmp_path: Path):

    planner = tmp_path / "planner"

    planner.mkdir()

    prompt = planner / "system.md"

    prompt.write_text(
        "Hello",
        encoding="utf-8",
    )

    loader = PromptLoader(tmp_path)

    result = loader.load(
        PromptType.PLANNER,
        PromptRole.SYSTEM,
    )

    assert result == "Hello"


def test_missing_prompt(tmp_path: Path):

    loader = PromptLoader(tmp_path)

    with pytest.raises(
        PromptNotFoundError
    ):

        loader.load(
            PromptType.PLANNER,
            PromptRole.SYSTEM,
        )