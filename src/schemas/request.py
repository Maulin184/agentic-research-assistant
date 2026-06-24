from pydantic import BaseModel

from src.schemas.enums import ReportType


class ResearchRequest(BaseModel):
    """
    User research request.
    """

    topic: str
    report_type: ReportType = ReportType.NORMAL