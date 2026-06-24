from pydantic import BaseModel, Field

from src.schemas.review import ReviewFeedback
from src.schemas.source import Source


class Section(BaseModel):
    """
    Research section.
    """

    title: str

    description: str | None = None

    research_content: str = ""

    sources: list[Source] = Field(
    default_factory=list
    )

    reviews: list[ReviewFeedback] = Field(
    default_factory=list
    )

    revision_count: int = Field(
        default=0,
        ge=0,
    )