"""
Mock LLM provider used for testing.
"""

from __future__ import annotations

from src.services.llm.models import (
    FinishReason,
    LLMRequest,
    LLMResponse,
)

from .base import LLMProvider


class MockLLMProvider(LLMProvider):
    """
    Simple provider that always returns a fixed response.
    """

    def __init__(
        self,
        response: str = "Mock response",
    ) -> None:
        self._response = response

    def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        return LLMResponse(
            content=self._response,
            finish_reason=FinishReason.STOP,
            model="mock-provider",
        )