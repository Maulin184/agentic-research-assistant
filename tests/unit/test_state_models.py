from src.schemas.enums import (
    ReportType,
    ResearchStatus,
)
from src.schemas.request import ResearchRequest
from src.schemas.state import ResearchState


def test_research_request_defaults():
    request = ResearchRequest(
        topic="Quantum Computing"
    )

    assert (
        request.report_type
        == ReportType.NORMAL
    )


def test_state_creation():
    request = ResearchRequest(
        topic="Quantum Computing"
    )

    state = ResearchState(
        request=request
    )

    assert (
        state.status
        == ResearchStatus.PENDING
    )

    assert len(state.sections) == 0


def test_execution_id_generated():
    request = ResearchRequest(
        topic="AI Agents"
    )

    state = ResearchState(
        request=request
    )

    assert state.execution_id is not None

def test_global_context_default():
    request = ResearchRequest(
        topic="Quantum Computing"
    )

    state = ResearchState(
        request=request
    )

    assert state.global_context == ""    