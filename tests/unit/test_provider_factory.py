import pytest

from src.services.llm.exceptions import ProviderError
from src.services.llm.factory import ProviderFactory


def test_unknown_provider():

    with pytest.raises(ProviderError):
        ProviderFactory.create("unknown")


def test_missing_api_key(monkeypatch):

    from src.config import settings

    monkeypatch.setattr(
        settings,
        "groq_api_key",
        "",
    )

    with pytest.raises(ProviderError):
        ProviderFactory.create("groq")