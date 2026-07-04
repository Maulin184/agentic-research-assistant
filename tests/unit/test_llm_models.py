from src.services.llm import (
    ChatMessage,
    FinishReason,
    LLMRequest,
    LLMResponse,
    MessageRole,
)


def test_chat_message():

    message = ChatMessage(
        role=MessageRole.USER,
        content="Hello",
    )

    assert message.role == MessageRole.USER
    assert message.content == "Hello"


def test_request_defaults():

    request = LLMRequest(
        messages=[
            ChatMessage(
                role=MessageRole.USER,
                content="Hello",
            )
        ]
    )

    assert request.temperature == 0.2
    assert request.max_tokens == 4096


def test_response():

    response = LLMResponse(
        content="Hi!",
        finish_reason=FinishReason.STOP,
        model="test-model",
    )

    assert response.content == "Hi!"