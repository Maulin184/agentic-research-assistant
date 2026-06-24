from datetime import datetime, UTC

from pydantic import BaseModel, Field


class ReviewFeedback(BaseModel):
    """
    Review result for a section.
    """

    reviewer_comments: str

    quality_score: float = Field(
        ge=0.0,
        le=10.0,
    )

    approved: bool

    improvement_suggestions: list[str] = Field(
    default_factory=list
    )

    reviewed_at: datetime = Field(default_factory=lambda: datetime.now(UTC))