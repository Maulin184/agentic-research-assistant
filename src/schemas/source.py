from datetime import datetime, UTC

from pydantic import BaseModel, Field


class Source(BaseModel):
    """
    Research source metadata.
    """

    title: str
    url: str

    snippet: str | None = None

    source_type: str

    search_query: str | None = None

    retrieved_at: datetime = Field(default_factory=lambda: datetime.now(UTC))