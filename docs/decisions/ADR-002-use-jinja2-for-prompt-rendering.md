# ADR-001: Use Jinja2 for Prompt Rendering

## Status

Accepted

## Context

The project requires a flexible way to render prompt templates with runtime variables while remaining independent of any LLM framework.

## Decision

Use Jinja2 as the prompt rendering engine.

## Alternatives Considered

- Python `str.format()`
- LangChain PromptTemplate

## Rationale

Jinja2 provides conditional logic, loops, template inheritance, and mature tooling while remaining framework-agnostic.

## Consequences

The Prompt Service remains reusable regardless of the orchestration or LLM framework adopted by the project.