from unittest.mock import MagicMock
from unittest.mock import patch

from src.config.config_models import ProviderConfig
from src.services.llm.models import (
    ChatMessage,
    LLMRequest,
    MessageRole,
)
from src.services.llm.providers.groq import GroqProvider


@patch("src.services.llm.providers.groq.Groq")
def test_generate(mock_groq):

    # -------------------------
    # Mock SDK response
    # -------------------------

    mock_choice = MagicMock()

    mock_choice.message.content = "Hello from Groq"

    mock_choice.finish_reason = "stop"

    mock_usage = MagicMock()

    mock_usage.prompt_tokens = 10
    mock_usage.completion_tokens = 20
    mock_usage.total_tokens = 30

    mock_response = MagicMock()

    mock_response.choices = [mock_choice]

    mock_response.usage = mock_usage

    mock_response.model = "llama"

    mock_response.model_dump.return_value = {}

    mock_client = MagicMock()

    mock_client.chat.completions.create.return_value = mock_response

    mock_groq.return_value = mock_client

    # -------------------------
    # Provider
    # -------------------------

    provider = GroqProvider(
        config=ProviderConfig(
            api_base="https://api.groq.com",
            timeout=60,
            max_retries=2,
        ),
        api_key="dummy-key",
    )

    request = LLMRequest(
        model="llama",
        messages=[
            ChatMessage(
                role=MessageRole.USER,
                content="Hello",
            )
        ],
    )

    response = provider.generate(request)

    assert response.content == "Hello from Groq"

    assert response.model == "llama"

    assert response.usage.total_tokens == 30