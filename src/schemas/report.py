from pydantic import BaseModel


class ResearchReport(BaseModel):
    """
    Final report.
    """

    title: str

    content: str

    summary: str