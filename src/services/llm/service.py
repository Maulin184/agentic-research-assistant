"""
Provider-agnostic LLM service.
"""

from __future__ import annotations

import logging

from src.services.llm.exceptions import (
    InvalidResponseError,
    LLMError,
    ProviderError,
)
from src.services.llm.models import (
    LLMRequest,
    LLMResponse,
)
from src.services.llm.providers import LLMProvider


class LLMService:
    """
    Public entry point for LLM generation.
    """

    def __init__(
        self,
        provider: LLMProvider,
        logger: logging.Logger | None = None,
    ) -> None:

        self._provider = provider

        self._logger = logger or logging.getLogger(__name__)

    def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        self._logger.info(
            "Generating LLM response.",
            extra={
                "message_count": len(request.messages),
            },
        )

        try:

            response = self._provider.generate(request)

        except LLMError:

            raise

        except Exception as exc:

            raise ProviderError(str(exc)) from exc

        if not isinstance(response, LLMResponse):

            raise InvalidResponseError(
                "Provider returned an invalid response."
            )

        self._logger.info(
            "LLM response generated.",
            extra={
                "model": response.model,
                "finish_reason": response.finish_reason.value,
            },
        )

        return response