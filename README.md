# Agentic Research Assistant

> **A production-grade Agentic AI Research Assistant built with LangGraph, designed using modern software engineering principles, provider-agnostic LLM architecture, and production-ready AI workflows.**

---

# Project Vision

The goal of this project is to build a complete end-to-end **Agentic AI Research Assistant** capable of transforming a simple research request into a professionally written report through autonomous multi-agent collaboration.

The assistant is being developed not only as a functional application but also as a **learning-first, portfolio-grade, and production-oriented project** that demonstrates real-world AI engineering practices.

The final system will support:

- Intelligent research planning
- Multi-step autonomous research execution
- Parallel section-wise research
- Source collection and synthesis
- AI-powered review and refinement
- High-quality report generation
- PDF export
- Interactive Streamlit interface
- FastAPI backend
- Evaluation and observability

---

# Current Project Status

**Development Stage:** Active Development

**Current Phase:** Core Infrastructure & Workflow Foundation

### Current Progress

| Component | Status |
|-----------|--------|
| Project Foundation | ✅ Completed |
| Configuration Management | ✅ Completed |
| Structured Logging | ✅ Completed |
| Typed Configuration Models | ✅ Completed |
| Research State Models | ✅ Completed |
| Prompt Management System | ✅ Completed |
| Provider-Agnostic LLM Layer | ✅ Completed |
| LangGraph Workflow | 🚧 In Progress |
| Agent Layer | ⏳ Planned |
| Node Implementations | ⏳ Planned |
| Evaluation Framework | ⏳ Planned |
| PDF Generation | ⏳ Planned |
| Streamlit UI | ⏳ Planned |
| FastAPI Service | ⏳ Planned |

---

# Current Features

## Configuration System

- Environment-based settings
- YAML-driven configuration
- Strongly typed configuration models
- Pydantic validation
- Provider configuration support

---

## Prompt Management

- Framework-agnostic Prompt Service
- Prompt Loader
- Jinja2 Prompt Renderer
- Prompt Cache
- Dependency Injection support
- Template management

---

## LLM Infrastructure

Production-ready provider abstraction including:

- Provider-agnostic architecture
- Abstract Provider Interface
- LLM Service
- Provider Factory
- Mock Provider
- Groq Provider
- Configuration-driven provider selection
- Token usage tracking
- Unified request/response models
- Custom exception hierarchy

---

## Research State

Strongly typed workflow state including:

- Research request models
- Section models
- Source models
- Review models
- Report models
- Workflow state validation

---

## Observability

- Structured logging
- Environment-aware logging configuration
- Centralized logger configuration

---

# High-Level Workflow

```text
User Request
      │
      ▼
Planner Node
      │
      ▼
Global Research Node
      │
      ▼
Parallel Section Research
      │
      ▼
Parallel Section Review
      │
      ▼
Writer Node
      │
      ▼
Final Review
      │
      ▼
PDF Generation
      │
      ▼
Completed Research Report
```

---

# High-Level Architecture

```text
                User Request
                      │
                      ▼
              LangGraph Workflow
                      │
        ┌─────────────┼─────────────┐
        │             │             │
    Planner      Researcher     Reviewer
        │             │             │
        └─────────────┼─────────────┘
                      │
                   Writer
                      │
                      ▼
                Final Report
                      │
             Provider-Agnostic
                LLM Service
                      │
               Provider Factory
                      │
      ┌───────────────┴───────────────┐
      │                               │
   Groq Provider                Mock Provider
```

---

# Testing

Current automated test coverage includes:

- Configuration
- Settings
- Prompt Service
- Prompt Rendering
- Prompt Loading
- Prompt Models
- LLM Models
- LLM Service
- Provider Factory
- Base Provider
- Mock Provider
- Groq Provider
- Logging
- Research State Models

**Current Test Status**

- ✅ 36 Unit Tests
- ✅ All Tests Passing

---

# Tech Stack

## Core

- Python 3.11
- LangGraph *(upcoming workflow integration)*
- Pydantic v2
- Jinja2

## LLM

- Groq SDK
- Provider-Agnostic Architecture

## Configuration

- YAML
- python-dotenv
- pydantic-settings

## Observability

- Structlog

## Testing

- Pytest
- unittest.mock

## Code Quality

- Ruff

---

# Repository Structure

```text
configs/
docs/
prompts/
reports/
scripts/
src/
tests/
```

---

# Development Philosophy

This project is built around the following engineering principles:

- Learn deeply rather than build quickly
- Architecture before implementation
- Strong typing wherever practical
- Test-driven development where appropriate
- Modular and maintainable code
- Provider independence
- Production-oriented engineering practices
- Continuous documentation
- Incremental, well-tested development

---

# Roadmap

## Foundation

- ✅ Project Setup
- ✅ Configuration System
- ✅ Logging
- ✅ Prompt Service
- ✅ LLM Infrastructure

## Workflow

- 🚧 LangGraph Integration
- ⏳ Agent Implementations
- ⏳ Node Implementations

## Product

- ⏳ Evaluation Framework
- ⏳ PDF Export
- ⏳ FastAPI
- ⏳ Streamlit UI

---

# Learning Goals

This project is intentionally designed to gain practical expertise in:

- Agentic AI
- Generative AI Engineering
- LangGraph
- Multi-Agent Systems
- LLM Application Architecture
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- Production Software Engineering
- Testing AI Systems
- Observability
- System Design

---

# License

This project is being developed as a learning, research, and portfolio project.