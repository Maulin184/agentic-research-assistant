# ADR-001: Technology Stack Selection

## Status

Accepted

## Context

The Agentic Research Assistant requires a technology stack that balances learning, maintainability, production-readiness, and portfolio value.

## Decisions

### Python
Chosen: Python 3.11

Reason:
- Stable ecosystem
- Excellent support for LangGraph, FastAPI, and GenAI tooling

Alternative:
- Python 3.12

Tradeoff:
- Slightly older runtime, but more mature compatibility.

---

### Dependency Management
Chosen: pip + venv

Reason:
- Simplicity
- Familiar workflow
- Lower learning overhead

Alternative:
- UV

Tradeoff:
- Slower package installation.

---

### Agent Framework
Chosen: LangGraph

Reason:
- Explicit workflow orchestration
- State management
- Production-grade agent design

Alternative:
- CrewAI
- AutoGen

Tradeoff:
- Slightly steeper learning curve.

---

### Backend
Chosen: FastAPI

Reason:
- Async support
- Strong typing
- Production-ready architecture

---

### Frontend
Chosen: Streamlit

Reason:
- Rapid iteration
- Focus remains on AI architecture

---

### LLM Access Layer
Chosen: LiteLLM

Reason:
- Provider abstraction
- Model routing support

---

### Logging
Chosen: Structlog

Reason:
- Structured logging
- Better observability

---

### Testing
Chosen: Pytest

Reason:
- Industry standard
- Excellent ecosystem