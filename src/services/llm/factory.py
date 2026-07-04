"""
Factory for constructing LLM providers.
"""

from __future__ import annotations

from src.config import (
    providers_config,
    settings,
)
from src.services.llm.exceptions import ProviderError
from src.services.llm.providers import (
    GroqProvider,
    LLMProvider,
)


class ProviderFactory:
    """
    Creates configured LLM provider instances.
    """

    @staticmethod
    def create(
        provider_name: str,
    ) -> LLMProvider:
        """
        Create an LLM provider instance.
        """

        if provider_name not in providers_config.root:
            raise ProviderError(
                f"Unknown provider: {provider_name}"
            )

        provider_config = providers_config.root[provider_name]

        if provider_name == "groq":

            if not settings.groq_api_key:
                raise ProviderError(
                    "Missing GROQ API key."
                )

            return GroqProvider(
                config=provider_config,
                api_key=settings.groq_api_key,
            )

        raise ProviderError(
            f"Provider '{provider_name}' is not implemented."
        )