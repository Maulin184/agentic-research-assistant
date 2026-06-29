"""
Prompt template cache.

Responsibilities
----------------
- Cache raw prompt templates.
- Avoid repeated disk reads.

This cache stores raw templates only.
Rendering is handled separately.
"""

from __future__ import annotations

from .models import PromptRole, PromptType


class PromptCache:
    """
    In-memory cache for raw prompt templates.
    """

    def __init__(self) -> None:
        self._cache: dict[tuple[PromptType, PromptRole], str] = {}

    def get(
        self,
        prompt_type: PromptType,
        prompt_role: PromptRole,
    ) -> str | None:
        """
        Retrieve a cached template.

        Returns None if not cached.
        """
        return self._cache.get((prompt_type, prompt_role))

    def set(
        self,
        prompt_type: PromptType,
        prompt_role: PromptRole,
        template: str,
    ) -> None:
        """
        Store a template in the cache.
        """
        self._cache[(prompt_type, prompt_role)] = template

    def clear(self) -> None:
        """
        Remove all cached templates.
        """
        self._cache.clear()