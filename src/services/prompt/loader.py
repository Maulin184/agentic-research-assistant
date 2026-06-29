"""
Prompt template loader.

Responsibilities
----------------
- Locate prompt template files.
- Read Markdown prompt templates.
- Return raw template text.

This module must never:
- Render templates.
- Cache templates.
- Call an LLM.
"""

from pathlib import Path

from .exceptions import PromptNotFoundError
from .models import PromptType, PromptRole


class PromptLoader:
    """
    Loads prompt templates from disk.
    """

    def __init__(self, prompts_root: Path) -> None:
        self._prompts_root = prompts_root

    def load(
        self,
        prompt_type: PromptType,
        prompt_role: PromptRole,
    ) -> str:
        """
        Load a prompt template.

        Parameters
        ----------
        prompt_type:
            Prompt category.

        template_name:
            Usually 'system' or 'user'.

        Returns
        -------
        str
            Raw markdown template.
        """

        path = (
            self._prompts_root
            / prompt_type.value
            / f"{prompt_role.value}.md"
        )

        if not path.exists():
            raise PromptNotFoundError(
                f"Prompt not found: {path}"
            )

        return path.read_text(
            encoding="utf-8"
        )