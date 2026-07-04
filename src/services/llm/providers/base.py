"""
Base interface for all LLM providers.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from src.services.llm.models import (
    LLMRequest,
    LLMResponse,
)


class LLMProvider(ABC):
    """
    Abstract interface implemented by every provider.
    """

    @abstractmethod
    def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:
        """
        Generate a response for the supplied request.
        """
        raise NotImplementedError