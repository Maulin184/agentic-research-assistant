"""
LLM domain models.

These models define the provider-agnostic interface used
throughout the application.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class MessageRole(str, Enum):
    """Supported chat message roles."""

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class FinishReason(str, Enum):
    """Reasons why generation finished."""

    STOP = "stop"
    LENGTH = "length"
    ERROR = "error"


class ChatMessage(BaseModel):
    """
    Single chat message.
    """

    role: MessageRole

    content: str = Field(
        min_length=1,
    )


class TokenUsage(BaseModel):
    """
    Token usage statistics.
    """

    prompt_tokens: int = 0

    completion_tokens: int = 0

    total_tokens: int = 0


class LLMRequest(BaseModel):
    """
    Standardized request sent to any provider.
    """

    messages: list[ChatMessage]
    model: str | None = None

    temperature: float = Field(
        default=0.2,
        ge=0.0,
        le=2.0,
    )

    max_tokens: int = Field(
        default=4096,
        gt=0,
    )

    top_p: float = Field(
        default=1.0,
        gt=0.0,
        le=1.0,
    )

    stream: bool = False


class LLMResponse(BaseModel):
    """
    Standardized provider response.
    """

    content: str

    finish_reason: FinishReason

    usage: TokenUsage = Field(
        default_factory=TokenUsage,
    )

    model: str

    raw_response: dict | None = None