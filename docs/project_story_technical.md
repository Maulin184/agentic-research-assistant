 ## Logging Architecture

Implemented structured logging using Structlog.

Rationale:
- Consistent event logging
- Future support for LangGraph tracing
- Easier observability and debugging

Future Extensions:
- Execution IDs
- Request IDs
- Token tracking
- Performance metrics

# Sprint 1.5 – State Schema Architecture

## Objective

Design the domain state model before implementing LangGraph workflows.

## Architectural Decision

Business state models were designed independently from LangGraph.

This avoids coupling core business entities to a specific orchestration framework.

## Implemented Models

- ResearchRequest
- Source
- ReviewFeedback
- Section
- ResearchReport
- ResearchState

## Key Decisions

### Rich Section State

Sections store:

- Research content
- Sources
- Review history
- Revision metadata

This enables:

- Evaluation
- Observability
- Review loops
- Quality analysis

### Review History Preservation

Instead of storing only the latest review result, a section stores all review feedback.

Benefits:

- Auditability
- Debugging
- Evaluation of revision effectiveness

### Timezone-Aware Timestamps

All timestamps use timezone-aware UTC datetimes.

Reason:

- Avoid naive datetime issues
- Improve production readiness
- Align with modern Python recommendations

## Lessons Learned

State-first design significantly simplifies future graph design because node responsibilities become clear and explicit.

# Milestone: Architecture Design Phase

## Objective

Establish the core architecture before implementing any AI workflow components.

The goal was to avoid premature implementation and reduce future refactoring costs.

---

## Node Architecture

Defined the workflow as a collection of state-driven nodes:

1. Planner Node
2. Global Research Node
3. Section Research Node
4. Section Review Node
5. Writer Node
6. Final Review Node
7. PDF Generation Node

Key decisions:

- Nodes own retries
- Nodes own state mutation
- Nodes own logging and error handling
- Nodes communicate only through workflow state

---

## Agent Architecture

Defined a provider-agnostic agent layer.

Planned agents:

- PlannerAgent
- ResearchAgent
- ReviewerAgent
- WriterAgent
- FinalReviewerAgent

Key decisions:

- Async-first design
- Structured outputs via Pydantic models
- Agents independent from LangGraph state
- Agents communicate through typed contracts

---

## Prompt Architecture

Prompts were elevated to first-class project assets.

Key decisions:

- External prompt files
- Separate system and user prompts
- Dedicated Prompt Service
- Python template formatting for V1
- Provider-independent prompt design

Benefits:

- Better maintainability
- Easier experimentation
- Improved testing
- Cleaner agent implementations

---

## Architectural Outcome

The current architecture is:

LangGraph
↓
Nodes
↓
Agents
↓
Prompt Service + LLM Service
↓
Prompt Files + Providers

This establishes clear separation of concerns and supports future provider replacement with minimal code changes.

---

## Lessons Learned

The biggest lesson during this phase was that architecture decisions become significantly harder to change after implementation begins.

Investing time in design before coding reduces long-term complexity and improves maintainability.

---

## Next Milestone

LLM Service Architecture Design

Goals:

- Provider abstraction
- Model routing
- Structured output integration
- Token usage tracking
- Future observability support

# Milestone: LLM Service Architecture Design

## Objective

Design a provider-agnostic language model interaction layer before implementing any agent logic.

The goal was to prevent provider-specific SDKs from leaking into the agent layer and to support future provider replacement with minimal code changes.

---

## Architectural Decision

Selected architecture:

LLM Service
↓
Provider Adapter
↓
Provider SDK

Agents interact only with the LLM Service.

Provider-specific implementations remain isolated behind adapters.

---

## Key Decisions

### Provider Abstraction

Agents remain unaware of:

- Groq
- OpenAI
- Gemini
- Anthropic
- Ollama
- OpenRouter

This reduces coupling and improves maintainability.

---

### Configuration-Driven Model Selection

Model and provider selection are controlled through configuration files rather than hardcoded values.

Benefits:

- Easier experimentation
- Environment flexibility
- No code modifications for model changes

---

### Structured Output Strategy

The LLM layer was designed around typed Pydantic outputs.

Planned outputs include:

- PlanningResult
- ResearchResult
- ReviewResult
- WritingResult
- FinalReviewResult

This improves validation and reliability.

---

### Observability Support

The architecture requires collection of:

- Provider
- Model
- Execution duration
- Token usage
- Error information

This information will later support evaluation and monitoring.

---

## Architectural Outcome

The system architecture now becomes:

LangGraph
↓
Nodes
↓
Agents
↓
Prompt Service + LLM Service
↓
Prompt Files + Providers

This establishes clear responsibility boundaries throughout the system.

---

## Lessons Learned

Provider independence is easiest to achieve before implementation begins.

Designing abstraction layers early significantly reduces future refactoring effort.

---

## Next Milestone

Sprint 3.0 – Prompt Service Implementation

Goals:

- Prompt loading
- Prompt rendering
- Variable validation
- Prompt caching
- Prompt service testing

## Sprint 3.0 – Giving the AI Its Instructions

Until now, we had built the foundation of the project. In this sprint, we created the system responsible for managing every prompt used by our AI agents.

Instead of hardcoding prompts inside Python files, every prompt now lives as a separate Markdown template. The Prompt Service loads these templates, fills in the required information using Jinja2, and returns the final prompt to the agent.

This approach keeps prompts easy to read, easy to improve, and completely independent of the application's code. It also prepares us for future prompt engineering without modifying the software architecture.