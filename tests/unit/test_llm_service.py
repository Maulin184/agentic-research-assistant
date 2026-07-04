import pytest

from src.services.llm import (
    ChatMessage,
    LLMRequest,
    MessageRole,
    ProviderError,
)
from src.services.llm.service import LLMService
from src.services.llm.providers import (
    LLMProvider,
    MockLLMProvider,
)


def test_service_generate():

    provider = MockLLMProvider()

    service = LLMService(provider)

    request = LLMRequest(
        messages=[
            ChatMessage(
                role=MessageRole.USER,
                content="Hello",
            )
        ]
    )

    response = service.generate(request)

    assert response.content == "Mock response"


class BrokenProvider(LLMProvider):

    def generate(self, request):

        raise RuntimeError("Boom")


def test_provider_error():

    service = LLMService(BrokenProvider())

    request = LLMRequest(
        messages=[
            ChatMessage(
                role=MessageRole.USER,
                content="Hi",
            )
        ]
    )

    with pytest.raises(ProviderError):

        service.generate(request)