# Prompt Architecture Design

## Overview

Prompts are first-class assets within the Agentic AI Research Assistant.

Prompts significantly influence:

- Research quality
- Report quality
- Structured output reliability
- Review effectiveness
- Evaluation performance

Therefore prompts should not be embedded directly inside agent implementations.

Instead, prompts should be treated as version-controlled project assets.

---

# Goals

The prompt architecture should provide:

- Separation of concerns
- Reusability
- Maintainability
- Version control
- Testability
- Provider independence

---

# Design Principles

## Prompts Are Assets

Prompts are part of the system's behavior.

Changes to prompts can alter system outputs as much as code changes.

Prompts should therefore:

- Live in dedicated files
- Be reviewed
- Be version controlled
- Be tested

---

## Separation of Concerns

Agents should focus on:

- Business reasoning
- LLM invocation
- Structured output handling

Agents should not:

- Store prompt text
- Load prompt files
- Render templates

Prompt management belongs to the Prompt Service layer.

---

## Provider Independence

Prompt definitions should remain independent from any specific provider.

Avoid provider-specific prompt formats whenever possible.

This allows switching between:

- Groq
- OpenAI
- Anthropic
- Gemini
- Ollama
- OpenRouter

without rewriting prompts.

---

# Architecture Layers

```text
Agent
 ↓
Prompt Service
 ↓
Prompt Files
```

Responsibilities:

Prompt Files:
    Store prompt templates

Prompt Service:
    Load templates
    Render templates
    Validate variables
    Cache prompt content

Agent:
    Supply input variables
    Receive rendered prompts
    Invoke LLM

---

# Prompt Directory Structure

prompts/
├── planner/
│   ├── system.txt
│   └── user.txt
│
├── researcher/
│   ├── system.txt
│   └── user.txt
│
├── reviewer/
│   ├── system.txt
│   └── user.txt
│
├── writer/
│   ├── system.txt
│   └── user.txt
│
└── final_reviewer/
    ├── system.txt
    └── user.txt

---

# System Prompt Strategy

System prompts define:

- Agent identity
- Responsibilities
- Rules
- Constraints
- Output expectations

Example:

"You are an expert research planner."

System prompts should remain relatively stable.

---

# User Prompt Strategy

User prompts contain dynamic information.

Examples:

- Topic
- Section title
- Global context
- Research content
- Review feedback

User prompts are rendered using templates.

---

# Template Rendering Strategy

Prompt templates should support placeholders.

Example:

Topic:
{topic}

Section:
{section_title}

Global Context:
{global_context}

Templates will be rendered at runtime.

---

# Template Engine Selection

## Option A

Python string formatting

Example:

```python
template.format(...)
```

## Option B

Jinja2

Example:

```jinja2
{{ topic }}
```

### Selected Option

Python string formatting.

Reason:

- Simpler
- Fewer dependencies
- Easier debugging
- Sufficient for V1

Jinja2 may be introduced later if prompt complexity increases.

---

# Prompt Service Responsibilities

Future component:

src/services/prompt_service.py

Responsibilities:

- Load prompt files
- Cache prompt content
- Render templates
- Validate variables
- Provide rendered prompts to agents

The Prompt Service should become the single entry point for prompt access.

---

# Variable Management

Prompt variables should be explicit and predictable.

Examples:

- topic
- report_type
- section_title
- section_description
- global_context
- research_content
- review_feedback

Avoid implicit or hidden variables.

---

# Error Handling

Prompt rendering failures should fail fast.

Examples:

- Missing variables
- Missing prompt files
- Invalid template formatting

Errors should be surfaced immediately rather than silently ignored.

---

# Testing Strategy

Prompt testing should be implemented early.

Tests should verify:

- Prompt files exist
- Templates load correctly
- Required variables render correctly
- Missing variables raise errors

Future test file:

tests/unit/test_prompt_service.py

---

# Observability Considerations

Prompt operations should be observable.

Track:

- Prompt loaded
- Prompt rendered
- Render duration
- Missing variables
- Rendering failures

Prompt content itself should not be logged in production.

Only metadata should be logged.

---

# Future Enhancements

Potential future capabilities:

- Prompt versioning
- Prompt metadata
- Prompt evaluation
- Prompt A/B testing
- Dynamic prompt selection
- Multi-language prompts

These capabilities are intentionally excluded from V1.

---

# Key Architectural Decisions

## Decision 1: External Prompt Files

Selected because:

- Easier maintenance
- Better version control
- Cleaner agent code

---

## Decision 2: Dedicated Prompt Service

Selected because:

- Centralized prompt management
- Reduced duplication
- Better testing

---

## Decision 3: Python Template Formatting

Selected because:

- Simple
- Lightweight
- Sufficient for current requirements

---

## Decision 4: Separate System and User Prompts

Selected because:

- Better provider compatibility
- Clear separation of responsibilities
- Easier prompt management

---

# Summary

Prompts are treated as first-class project assets.

Prompt files remain separate from agent implementations.

A dedicated Prompt Service manages loading and rendering.

This approach improves maintainability, testing, version control, and long-term scalability.