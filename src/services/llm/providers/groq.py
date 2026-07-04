"""
Groq provider implementation.
"""

from __future__ import annotations

from groq import Groq

from src.config.config_models import ProviderConfig
from src.services.llm.exceptions import (
    AuthenticationError,
    InvalidResponseError,
    ProviderError,
    RateLimitError,
)
from src.services.llm.models import (
    ChatMessage,
    FinishReason,
    LLMRequest,
    LLMResponse,
    TokenUsage,
)

from .base import LLMProvider


class GroqProvider(LLMProvider):
    """
    Groq implementation of the provider interface.
    """

    def __init__(
        self,
        config: ProviderConfig,
        api_key: str,
    ) -> None:

        self._config = config

        self._client = Groq(
            api_key=api_key,
            base_url=config.api_base,
            timeout=config.timeout,
        )

    def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        try:
            if request.model is None:
                raise ProviderError(
                    "LLMRequest.model must be provided."
                )
            
            response = self._client.chat.completions.create(
                model=request.model,
                messages=[
                    {
                        "role": message.role.value,
                        "content": message.content,
                    }
                    for message in request.messages
                ],
                temperature=request.temperature,
                max_completion_tokens=request.max_tokens,
                top_p=request.top_p,
                stream=request.stream,
            )

        except Exception as exc:
            # We'll improve provider-specific exception mapping later.
            raise ProviderError(str(exc)) from exc

        if not response.choices:
            raise InvalidResponseError(
                "No completion returned."
            )

        choice = response.choices[0]

        usage = TokenUsage()

        if response.usage:

            usage = TokenUsage(
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
            )

        finish_reason = FinishReason.STOP

        if choice.finish_reason == "length":
            finish_reason = FinishReason.LENGTH

        return LLMResponse(
            content=choice.message.content or "",
            finish_reason=finish_reason,
            usage=usage,
            model=response.model,
            raw_response=response.model_dump(),
        )