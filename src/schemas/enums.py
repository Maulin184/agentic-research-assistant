from enum import Enum


class ReportType(str, Enum):
    """
    Supported report types.
    """

    SHORT = "short"
    NORMAL = "normal"
    DEEP = "deep"


class ResearchStatus(str, Enum):
    """
    Workflow execution status.
    """

    PENDING = "pending"
    PLANNING = "planning"
    RESEARCHING = "researching"
    REVIEWING = "reviewing"
    WRITING = "writing"
    FINAL_REVIEW = "final_review"
    COMPLETED = "completed"
    FAILED = "failed"