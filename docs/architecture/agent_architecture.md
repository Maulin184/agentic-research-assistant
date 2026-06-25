# Agent Architecture Design

## Overview

Agents are responsible for AI-specific behavior within the Agentic AI Research Assistant.

An agent's primary responsibilities are:

- Construct prompts
- Invoke Large Language Models (LLMs)
- Validate structured outputs
- Return typed results

Agents are intentionally kept independent from workflow orchestration and state management.

---

# Architecture Layers

```text
LangGraph Workflow
        ↓
       Nodes
        ↓
      Agents
        ↓
   LLM Service
        ↓
     Provider
```

## Layer Responsibilities

### LangGraph

Responsible for:

- Workflow orchestration
- Execution flow
- Conditional routing
- Parallel execution

### Nodes

Responsible for:

- Receiving workflow state
- Calling agents
- Validation
- State updates
- Retries
- Logging
- Error handling

### Agents

Responsible for:

- Prompt construction
- LLM invocation
- Structured output generation

### LLM Service

Responsible for:

- Provider abstraction
- Model invocation
- Response handling

### Provider

Examples:

- Groq
- OpenAI
- Anthropic
- Gemini
- Ollama
- OpenRouter

---

# Design Principles

## Single Responsibility Principle

Agents should focus only on AI reasoning tasks.

Examples:

- Planning
- Research
- Reviewing
- Writing

Agents should not perform:

- Workflow orchestration
- State mutation
- Retry handling
- Logging orchestration

These responsibilities belong to nodes.

---

## Provider Agnostic Design

Agents must never directly interact with provider-specific SDKs.

Avoid:

```python
ChatGroq(...)
ChatOpenAI(...)
ChatAnthropic(...)
```

Preferred:

```text
Agent
 ↓
LLM Service
 ↓
Provider
```

Benefits:

- Easy provider switching
- Reduced coupling
- Easier testing
- Better maintainability

---

## Structured Outputs

Agents should return strongly typed Pydantic models.

Avoid:

```python
str
dict
```

Prefer:

```python
PlanningResult
ResearchResult
ReviewResult
WritingResult
FinalReviewResult
```

Benefits:

- Validation
- Type safety
- Better IDE support
- Easier testing
- Predictable contracts

---

## Async First Design

All agents should expose asynchronous interfaces.

Reason:

The workflow includes:

- Parallel section research
- Parallel section review

Using async from the beginning avoids future refactoring.

---

# Base Agent Contract

All agents should implement a common interface.

Conceptual Design:

```python
class BaseAgent:
    async def run(...):
        ...
```

Requirements:

- Public entry point must be `run()`
- Return typed outputs
- Remain provider agnostic
- Remain independent from workflow state

---

# Agent Inventory

## Planner Agent

### Purpose

Generate a structured research plan from a user topic.

### Inputs

- Topic
- Report Type

### Outputs

- PlanningResult

### Responsibilities

- Identify major sections
- Define section descriptions
- Determine research scope
- Create report structure

### Non-Responsibilities

- Research
- Reviewing
- Report writing

---

## Research Agent

### Purpose

Research an individual report section.

### Inputs

- Topic
- Global Context
- Section Information

### Outputs

- ResearchResult

### Responsibilities

- Gather information
- Synthesize findings
- Produce section content
- Attach supporting sources

### Non-Responsibilities

- Workflow state updates
- Review decisions
- Report assembly

---

## Reviewer Agent

### Purpose

Evaluate the quality of a section.

### Inputs

- Section Content
- Sources

### Outputs

- ReviewResult

### Responsibilities

- Evaluate completeness
- Assess relevance
- Assess factual grounding
- Identify weaknesses
- Recommend improvements

### Non-Responsibilities

- Rewriting content
- State updates
- Workflow decisions

---

## Writer Agent

### Purpose

Merge approved sections into a coherent report.

### Inputs

- Approved Sections

### Outputs

- WritingResult

### Responsibilities

- Improve readability
- Improve narrative flow
- Connect sections
- Remove duplication
- Preserve report structure

### Non-Responsibilities

- Research
- Review
- Fact verification

---

## Final Reviewer Agent

### Purpose

Evaluate the complete report.

### Inputs

- Draft Report

### Outputs

- FinalReviewResult

### Responsibilities

- Assess coverage
- Assess consistency
- Assess completeness
- Assess readability
- Assess logical flow

### Non-Responsibilities

- Report generation
- Research
- Workflow orchestration

---

# Agent Independence

Agents should remain completely independent from:

- LangGraph
- ResearchState
- Node implementations

Preferred:

```python
research_agent.run(
    topic=topic,
    global_context=context,
    section=section,
)
```

Avoid:

```python
research_agent.run(state)
```

Reason:

This improves:

- Reusability
- Testability
- Framework independence
- Maintainability

---

# Error Handling Strategy

Agents should raise meaningful exceptions when failures occur.

Agents should NOT:

- Retry requests
- Suppress errors
- Update workflow state

Retries and recovery belong to nodes.

---

# Observability Considerations

Agents should expose enough metadata for observability.

Examples:

- Model used
- Provider used
- Execution duration
- Token usage
- Request identifiers

Collection and persistence of observability data should be handled outside the agent layer.

---

# Future Agent Expansion

Potential future agents:

- FactCheckingAgent
- CitationVerificationAgent
- SourceRankingAgent
- EvaluationAgent
- ResearchExpansionAgent

These are intentionally excluded from V1 to maintain manageable complexity.

---

# Key Architectural Decisions

## Decision 1: Provider Agnostic Agents

Selected because:

- Easier provider replacement
- Better maintainability
- Cleaner architecture

---

## Decision 2: Structured Outputs

Selected because:

- Validation
- Type safety
- Predictable contracts

---

## Decision 3: Async First Design

Selected because:

- Supports parallel workflows
- Aligns with LangGraph capabilities
- Avoids future refactoring

---

## Decision 4: Agent-State Separation

Selected because:

- Better testing
- Better reusability
- Reduced coupling
- Framework independence

---

# Summary

Agents are responsible only for AI reasoning.

Nodes are responsible for orchestration.

State is responsible for communication.

LLM services are responsible for provider interaction.

This separation keeps the system modular, testable, maintainable, and production-ready.