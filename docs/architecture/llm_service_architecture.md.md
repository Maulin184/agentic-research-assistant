# LLM Service Architecture Design

## Overview

The LLM Service layer provides a provider-agnostic interface for interacting with Large Language Models.

Its primary purpose is to isolate agents from provider-specific implementations and configuration details.

Agents should never directly interact with:

* Groq SDK
* OpenAI SDK
* Gemini SDK
* Ollama SDK
* OpenRouter SDK

Instead, all model interactions should flow through the LLM Service layer.

---

# Architecture Layers

```text
Agent
 ↓
LLM Service
 ↓
Provider Adapter
 ↓
Provider SDK
```

---

# Layer Responsibilities

## Agent Layer

Responsible for:

* Preparing prompts
* Supplying response schemas
* Consuming structured outputs

Agents should not:

* Select models
* Select providers
* Manage provider SDKs
* Handle provider-specific logic

---

## LLM Service Layer

Responsible for:

* Provider selection
* Model selection
* LLM invocation
* Structured output handling
* Token usage collection
* Execution metadata collection

The LLM Service should become the single entry point for all model interactions.

---

## Provider Adapter Layer

Responsible for:

* Translating requests into provider-specific formats
* Calling provider SDKs
* Normalizing responses

Each provider implementation should conform to a common contract.

---

## Provider SDK Layer

Responsible for:

* Network communication
* Authentication
* Model execution

Examples:

* Groq SDK
* OpenAI SDK
* Gemini SDK
* Ollama SDK
* OpenRouter SDK

---

# Design Principles

## Provider Agnostic Design

Agents must remain unaware of provider implementations.

Preferred:

Agent
↓
LLM Service
↓
Provider

Avoid:

Agent
↓
Provider

Benefits:

* Easier provider replacement
* Better maintainability
* Cleaner testing
* Reduced coupling

---

## Configuration-Driven Model Selection

Model selection should be controlled through configuration.

Example:

models.yaml

planner:
provider: groq
model: llama-model

researcher:
provider: groq
model: llama-model

reviewer:
provider: groq
model: qwen-model

Agents should not hardcode models.

Benefits:

* Easier experimentation
* No code changes for model swaps
* Environment flexibility

---

## Structured Output Support

The LLM Service should support structured outputs through Pydantic models.

Example:

PlanningResult

ResearchResult

ReviewResult

WritingResult

FinalReviewResult

Benefits:

* Validation
* Type safety
* Predictable contracts
* Better testing

---

## Async First Design

All LLM interactions should be asynchronous.

Reason:

Future workflow includes:

* Parallel section research
* Parallel section review

Async design supports efficient concurrency and aligns with LangGraph capabilities.

---

# Proposed Service Flow

```text
Agent
 ↓
Load Prompt
 ↓
Render Prompt
 ↓
LLM Service
 ↓
Provider Adapter
 ↓
Provider SDK
 ↓
Response
 ↓
Structured Output Validation
 ↓
Agent
```

---

# LLM Service Responsibilities

Future component:

src/services/llm/service.py

Responsibilities:

* Resolve model configuration
* Resolve provider configuration
* Route requests to providers
* Validate structured outputs
* Collect execution metadata
* Return typed results

---

# Provider Adapter Responsibilities

Future location:

src/services/llm/providers/

Responsibilities:

* Provider-specific request formatting
* Provider-specific response parsing
* Authentication handling
* Error normalization

Each adapter should expose a common interface.

---

# Configuration Strategy

Model configuration should remain externalized.

Example configuration:

planner:
provider: groq
model: model_name

researcher:
provider: groq
model: model_name

reviewer:
provider: groq
model: model_name

writer:
provider: groq
model: model_name

final_reviewer:
provider: groq
model: model_name

This allows model changes without code modifications.

---

# Response Metadata Collection

Every LLM invocation should collect metadata.

Examples:

* Provider
* Model
* Execution duration
* Prompt tokens
* Completion tokens
* Total tokens

This information supports observability and future evaluation.

---

# Error Handling Strategy

The LLM Service should raise meaningful exceptions.

Examples:

* Provider unavailable
* Invalid configuration
* Authentication failure
* Timeout
* Structured output validation failure

The service should not silently suppress errors.

---

# Retry Strategy

Retries should not be implemented inside provider adapters.

Retries belong to workflow nodes.

Reason:

Nodes own:

* Execution control
* Error handling
* Retry policies

Keeping retries outside the LLM layer prevents duplicated retry logic.

---

# Testing Strategy

Future tests should verify:

* Provider selection
* Configuration loading
* Structured output validation
* Error handling
* Metadata collection

Potential test locations:

tests/unit/test_llm_service.py

tests/unit/test_provider_factory.py

---

# Observability Requirements

Every invocation should emit:

* Start event
* Completion event
* Execution duration
* Provider information
* Model information
* Error events

Prompt content should never be logged.

Only metadata should be logged.

---

# Future Provider Expansion

Potential future providers:

* OpenAI
* Anthropic
* Gemini
* Ollama
* OpenRouter

The architecture should support expansion without modifying agent implementations.

---

# Key Architectural Decisions

## Decision 1: Provider Agnostic Service Layer

Selected because:

* Reduced coupling
* Easier provider replacement
* Cleaner architecture

---

## Decision 2: Configuration-Driven Model Selection

Selected because:

* No hardcoded models
* Easier experimentation
* Better maintainability

---

## Decision 3: Structured Outputs

Selected because:

* Validation
* Type safety
* Reliable contracts

---

## Decision 4: Async First Design

Selected because:

* Supports parallel execution
* Aligns with LangGraph
* Avoids future refactoring

---

## Decision 5: Metadata Collection

Selected because:

* Observability
* Evaluation support
* Performance monitoring

---

# Summary

The LLM Service becomes the single entry point for all model interactions.

Agents remain focused on reasoning tasks.

Provider-specific logic remains isolated inside adapters.

This architecture enables maintainability, observability, provider flexibility, and production readiness.
