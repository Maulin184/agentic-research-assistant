from src.services.llm import (
    ChatMessage,
    LLMRequest,
    MessageRole,
)

from src.services.llm.providers.mock import MockLLMProvider


def test_mock_provider():

    provider = MockLLMProvider()

    request = LLMRequest(
        messages=[
            ChatMessage(
                role=MessageRole.USER,
                content="Hello",
            )
        ]
    )

    response = provider.generate(request)

    assert response.content == "Mock response"