## Milestone: Logging Foundation

We implemented a centralized logging system so that every future AI agent and workflow can be monitored and debugged consistently.

# Milestone: Designing the Research Workflow

Before building AI agents, we designed the information structure that the entire system will use.

We created models for:

- Research requests
- Research sections
- Sources
- Reviews
- Reports

This may seem like a small step, but it ensures that all future AI agents speak the same language and share information consistently.

One important lesson from this milestone was that designing data structures early prevents major refactoring later.

# Milestone: Designing How the AI Thinks

At this stage, we stopped writing code and focused on designing the system properly.

Instead of immediately building AI agents, we first defined:

- What each part of the system should do
- How information should flow
- How different AI agents should communicate
- How prompts should be managed

We designed several important components:

### Node Architecture

We divided the workflow into specialized stages:

- Planning
- Global Research
- Section Research
- Section Review
- Writing
- Final Review
- PDF Generation

Each stage has a clear responsibility.

### Agent Architecture

We defined different AI agents that will handle specific tasks:

- Planner Agent
- Research Agent
- Reviewer Agent
- Writer Agent
- Final Reviewer Agent

This makes the system modular and easier to improve later.

### Prompt Architecture

One important lesson from many AI projects is that prompts become difficult to manage when they are hidden inside code.

To avoid this problem, prompts will live in dedicated files and will be managed through a dedicated Prompt Service.

### What We Learned

Good architecture takes time.

Although this phase produced very little executable code, it reduced a large amount of future complexity and technical debt.

### Next Step

Design the LLM Service layer that will allow us to switch between different AI providers without changing agent code.

# Milestone: Designing the AI Communication Layer

In this phase, we designed how the AI parts of the system will communicate with different language models.

Instead of allowing every AI agent to directly talk to a specific provider, we introduced an intermediate layer called the LLM Service.

This layer acts as a central communication hub between our agents and the underlying AI providers.

### Why This Matters

Without this design, changing providers later would require modifying many parts of the codebase.

With the new architecture:

- Agents remain independent
- Providers can be swapped easily
- Configuration controls model selection
- Future experimentation becomes simpler

### What We Designed

We defined:

- A provider-agnostic LLM Service
- Provider adapter architecture
- Configuration-driven model selection
- Structured output support
- Token usage tracking
- Observability requirements

### What We Learned

Good software architecture creates flexibility before it becomes necessary.

By separating AI providers from the business logic, we reduce future maintenance costs and make experimentation easier.

### Next Step

Begin implementing the Prompt Service, which will load and render prompts for all AI agents.

### Sprint 3.0 – Prompt Service

- Framework-agnostic Prompt Service
- Prompt Loader
- Prompt Renderer (Jinja2)
- In-memory Prompt Cache
- Dependency Injection support
- Prompt template management
- Prompt Service unit tests
