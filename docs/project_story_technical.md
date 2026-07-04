# Project Story (Technical)

## Building the Engineering Foundation

The project began by establishing the engineering infrastructure before implementing any AI functionality.

Configuration management was centralized using environment variables, YAML configuration files, and strongly typed Pydantic models. This ensured that application behavior could be controlled through configuration rather than hardcoded values.

At the same time, a structured logging foundation was introduced using Structlog.

### Architectural Decisions

* Centralized configuration management
* Environment-aware settings
* Strongly typed configuration validation
* Structured logging across the entire application

### Expected Benefits

* Consistent application behavior
* Easier debugging
* Future observability support
* Production readiness

---

# Designing the Domain Before the Workflow

Rather than beginning with LangGraph, the project first defined the business domain.

The objective was to create stable business entities that would remain independent of any workflow engine.

The following domain models were implemented:

* ResearchRequest
* Source
* ReviewFeedback
* Section
* ResearchReport
* ResearchState

### Architectural Decisions

Business models remain completely independent of LangGraph.

Workflow orchestration should adapt to the business domain—not the other way around.

### Rich Section State

Each research section stores:

* Generated content
* Source references
* Review history
* Revision metadata

This enables:

* Evaluation
* Review loops
* Quality analysis
* Future observability

### Review History

Instead of overwriting review results, every review iteration is preserved.

Benefits include:

* Auditability
* Debugging
* Revision analysis

### Time Handling

All timestamps use timezone-aware UTC datetimes to avoid common production issues associated with naive datetime objects.

### Lessons Learned

Designing the domain first significantly simplified later architectural decisions because every future component shares the same business vocabulary.

---

# Designing the Workflow Architecture

With the business domain established, attention shifted to workflow orchestration.

Instead of immediately implementing LangGraph nodes, the workflow was designed conceptually first.

The research process was divided into specialized stages:

1. Planner
2. Global Research
3. Section Research
4. Section Review
5. Writer
6. Final Review
7. PDF Generation

### Architectural Decisions

Nodes are responsible for:

* State mutation
* Retry handling
* Logging
* Error handling

Nodes communicate exclusively through the shared workflow state.

This minimizes coupling between workflow stages.

### Lessons Learned

Clearly defined node responsibilities dramatically simplify workflow implementation and debugging.

---

# Designing the Agent Layer

The workflow architecture naturally led to defining specialized AI agents.

Rather than relying on a single general-purpose AI interaction, the project adopted a multi-agent architecture.

Planned agents include:

* PlannerAgent
* ResearchAgent
* ReviewerAgent
* WriterAgent
* FinalReviewerAgent

### Architectural Decisions

* Provider-independent agents
* Async-first architecture
* Typed Pydantic outputs
* Separation from LangGraph state

This keeps agent logic reusable outside any specific orchestration framework.

---

# Prompt Management Architecture

Prompt engineering was treated as an engineering discipline rather than embedding prompts directly into Python source code.

Prompts became first-class project assets.

### Architectural Decisions

* External Markdown prompt templates
* Separation of system and user prompts
* Dedicated Prompt Service
* Jinja2 template rendering
* Framework-independent prompt management

### Benefits

* Easier prompt iteration
* Cleaner application code
* Better testing
* Improved maintainability

---

# Implementing the Prompt Service

After defining the prompt architecture, the first reusable infrastructure component was implemented.

The Prompt Service became responsible for:

* Loading prompt templates
* Rendering templates with Jinja2
* In-memory caching
* Dependency injection support
* Variable validation
* Centralized prompt management

Comprehensive unit tests were added to validate each component independently.

This established a reusable prompt pipeline for every future AI agent.

---

# Designing and Implementing the LLM Layer

One of the most significant architectural milestones was introducing a provider-agnostic language model layer.

The primary objective was to ensure that the rest of the application remains completely independent of individual LLM providers.

### Architecture

```text
LLM Service
      │
Provider Factory
      │
LLM Provider
 ┌────┴────┐
 │         │
Groq     Mock
```

The application interacts only with the LLM Service.

Provider-specific SDKs remain isolated behind provider implementations.

### Implemented Components

* Unified request models
* Unified response models
* Provider interface
* Mock Provider
* Groq Provider
* Provider Factory
* LLM Service
* Provider configuration
* Exception hierarchy
* Token usage tracking

### Architectural Decisions

#### Provider Abstraction

Every provider implements a common interface.

Business logic never imports provider SDKs directly.

#### Factory Pattern

Provider creation is centralized through a dedicated factory.

This isolates provider selection from application logic.

#### Configuration-Driven Providers

Provider metadata is divided into three responsibilities:

* `models.yaml` defines model assignments
* `providers.yaml` defines provider behavior
* `.env` stores secrets

This separation allows environments and providers to change without modifying application code.

#### Mock Provider

A dedicated mock implementation enables deterministic unit testing without network access.

This significantly improves test reliability and execution speed.

#### Official SDK Adoption

The official Groq SDK was selected instead of custom HTTP requests.

Advantages include:

* Better long-term maintainability
* SDK compatibility
* Reduced implementation complexity
* Easier future upgrades

### Current Architecture

```text
LangGraph
      │
      ▼
Nodes
      │
      ▼
Agents
      │
      ▼
Prompt Service
      │
LLM Service
      │
Provider Factory
      │
LLM Providers
```

Each layer communicates only with its immediate dependency, creating clear separation of concerns.

### Testing

The LLM infrastructure is supported by comprehensive automated tests covering:

* Provider interface
* Mock provider
* Groq provider
* Provider factory
* LLM service
* Configuration loading
* Request and response models
* Exception hierarchy

At the completion of this milestone, the project contained **36 passing unit tests**, providing confidence that the infrastructure is stable before higher-level workflow development begins.

### Lessons Learned

Several architectural principles became increasingly clear during this milestone:

* Stable abstractions reduce future refactoring.
* Provider independence should be established before application logic grows.
* Configuration should own deployment concerns, not business logic.
* Comprehensive testing enables confident architectural evolution.

---

# Current Architectural Snapshot

```text
Application
      │
LangGraph Workflow
      │
Nodes
      │
Agents
      │
Prompt Service
      │
LLM Service
      │
Provider Factory
      │
LLM Providers
```

The project now possesses a complete, provider-independent infrastructure capable of supporting the remaining workflow implementation.

The next phase shifts focus from building infrastructure to orchestrating intelligent behavior through LangGraph and specialized AI agents.
