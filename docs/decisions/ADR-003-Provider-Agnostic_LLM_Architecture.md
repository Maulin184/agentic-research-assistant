# ADR-003: Provider-Agnostic LLM Architecture

## Status

Accepted

---

## Context

The Agentic Research Assistant must interact with Large Language Models (LLMs) throughout the research workflow.

Future requirements include:

* Supporting multiple LLM providers (Groq, OpenAI, Ollama, OpenRouter, etc.)
* Switching providers without modifying business logic
* Isolating provider-specific SDKs from the rest of the application
* Supporting deterministic testing without external API calls
* Maintaining clean separation between application logic and infrastructure

Allowing agents or workflow nodes to communicate directly with provider SDKs would tightly couple the application to specific vendors and significantly increase future maintenance costs.

---

## Decision

Introduce a provider-agnostic LLM architecture.

The architecture consists of:

* A centralized `LLMService` responsible for all language model interactions.
* An abstract `LLMProvider` interface defining a common provider contract.
* Provider-specific implementations (currently Groq and Mock).
* A `ProviderFactory` responsible for provider instantiation.
* Configuration-driven provider selection.
* Standardized request and response models shared across all providers.

The resulting architecture is:

```text
Application
      │
LLMService
      │
ProviderFactory
      │
LLMProvider
 ┌────┴─────┐
 │          │
Groq      Mock
```

---

## Alternatives Considered

### Direct SDK Usage

Allow every component to use provider SDKs directly.

**Rejected**

This tightly couples business logic to external providers and makes future migration difficult.

---

### Generic HTTP Client

Implement providers using raw HTTP requests.

**Rejected**

Although flexible, this approach increases maintenance effort and duplicates functionality already provided by official SDKs.

---

### Framework-Specific Abstractions

Rely on abstractions provided by external frameworks.

**Rejected**

The project aims to remain independent of orchestration and LLM frameworks wherever practical.

---

## Rationale

This architecture provides several long-term benefits:

* Provider independence
* Easier experimentation with different models
* Improved maintainability
* Better unit testing through mock providers
* Clear separation between business logic and infrastructure
* Simplified future provider integration

Using the official Groq SDK also reduces implementation complexity while improving compatibility with future SDK updates.

---

## Consequences

### Positive

* Business logic remains provider-independent.
* New providers can be added with minimal changes.
* Mock providers enable deterministic testing.
* Configuration controls provider selection.
* Infrastructure becomes easier to maintain and extend.

### Negative

* Slight increase in architectural complexity.
* Additional abstraction layer to maintain.

The long-term flexibility gained outweighs the small increase in implementation complexity.

---

## Future Considerations

The current architecture allows future additions without modifying application logic, including:

* OpenAI Provider
* Ollama Provider
* OpenRouter Provider
* Anthropic Provider
* Gemini Provider
* Streaming responses
* Asynchronous providers
* Automatic fallback between providers
* Load balancing and provider routing
* Cost-aware provider selection

These capabilities can be introduced incrementally while preserving the existing application architecture.
