import pytest

from src.services.llm.providers.base import LLMProvider


def test_base_provider_is_abstract():

    with pytest.raises(TypeError):
        LLMProvider()