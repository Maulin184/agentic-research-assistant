from datetime import datetime, UTC
from uuid import uuid4

from pydantic import BaseModel, Field

from src.schemas.enums import ResearchStatus
from src.schemas.report import ResearchReport
from src.schemas.request import ResearchRequest
from src.schemas.section import Section


class ResearchState(BaseModel):
    """
    Global workflow state.
    """

    request: ResearchRequest

    sections: list[Section] = []

    report: ResearchReport | None = None

    execution_id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    status: ResearchStatus = (
        ResearchStatus.PENDING
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )