# Agentic Research Assistant

Production-grade Agentic AI Research Assistant built with LangGraph.

---

## Project Goal

Build a production-grade Agentic AI Research Assistant capable of:

* Research planning
* Multi-step research execution
* Source collection and synthesis
* Section-level quality review
* Full report generation
* PDF export

The system is designed to demonstrate:

* Agentic AI
* LangGraph workflows
* Multi-agent orchestration
* State management
* Evaluation frameworks
* Observability
* Production engineering practices

---

## Current Status

**Phase:** Architecture & Design

**Current Sprint:** Sprint 2.2 – Prompt Architecture Design

**Next Sprint:** Sprint 2.3 – LLM Service Architecture Design

---

## Completed Milestones

### Sprint 1.1 – Project Foundation

* Repository setup
* Development workflow
* Dependency management

### Sprint 1.2 – Configuration Layer

* Environment-based settings
* Pydantic validation
* YAML configuration loading

### Sprint 1.3 – Logging Foundation

* Structured logging architecture
* Environment-aware logging design
* Logging tests

### Sprint 1.4 – Typed Configuration Models

* YAML-driven application configuration
* Strongly typed configuration objects
* Configuration validation tests

### Sprint 1.5 – State Schema Design

* Research domain models
* Workflow state models
* Source tracking
* Review tracking
* Report models
* State validation tests

### Sprint 2.0 – Node Architecture Design

* Workflow node inventory
* Node responsibilities
* State ownership rules
* Retry strategy design
* Observability requirements
* Workflow execution design

### Sprint 2.1 – Agent Architecture Design

* Provider-agnostic agent architecture
* BaseAgent contract design
* Structured output strategy
* Async-first design
* Agent responsibility boundaries

### Sprint 2.2 – Prompt Architecture Design

* Prompt management strategy
* Prompt directory structure
* System/User prompt separation
* Prompt rendering strategy
* Prompt service architecture
* Prompt testing strategy

---

## Architecture Progress

### Completed

* Project Foundation
* Configuration Layer
* Logging Layer
* Typed Configuration Layer
* State Architecture
* Node Architecture
* Agent Architecture
* Prompt Architecture

### Planned

* LLM Service Architecture
* Provider Layer
* Prompt Service
* Agent Implementations
* Node Implementations
* LangGraph Workflow
* Evaluation Framework
* Observability Dashboard
* PDF Generation
* Streamlit UI
* FastAPI Service

---

## High-Level Workflow

User Request
↓
Planner Node
↓
Global Research Node
↓
Section Research Nodes (Parallel)
↓
Section Review Nodes (Parallel)
↓
Writer Node
↓
Final Review Node
↓
PDF Generation Node
↓
Completed Report

---

## Current Repository Structure

```text
app/
artifacts/
configs/
docs/
prompts/
reports/
scripts/
src/
tests/
```

---

## Development Philosophy

This project prioritizes:

* Learning over speed
* Architecture before implementation
* Evaluation before feature expansion
* Production readiness
* Maintainability
* Deep understanding of Agentic AI systems

### Sprint 2.3 – LLM Service Architecture Design

* Provider-agnostic LLM architecture
* Provider adapter strategy
* Configuration-driven model selection
* Structured output support design
* Token usage tracking design
* Observability requirements
* Async-first LLM interaction strategy
