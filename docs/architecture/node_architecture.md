# Node Architecture Design

## Overview

The Agentic AI Research Assistant is designed as a state-driven workflow.

Nodes are responsible for orchestrating business logic while agents are responsible for producing AI-generated outputs.

A node:

* Receives workflow state
* Executes a specific business operation
* Validates outputs
* Updates state
* Handles retries and failures
* Emits logs and observability events

Nodes should remain focused on a single responsibility.

---

# Workflow Overview

User Request
↓
Planner Node
↓
Global Research Node
↓
Section Research Node (Parallel)
↓
Section Review Node (Parallel)
↓
Writer Node
↓
Final Review Node
↓
PDF Generation Node
↓
Completed

---

# Node Design Principles

## Single Responsibility

Each node should perform exactly one business function.

Good:

* Planner creates a plan
* Researcher performs research
* Reviewer evaluates quality

Bad:

* Planner performs research
* Reviewer rewrites content
* Writer performs web searches

---

## State-Driven Execution

Nodes communicate only through workflow state.

Nodes should never communicate directly with each other.

All information exchange must occur through the ResearchState object.

---

## Controlled State Mutation

Each node may modify only the fields it owns.

This prevents accidental corruption of workflow state.

---

## Retry Ownership

Retries belong to nodes.

Agents should not implement retry logic.

Nodes are responsible for:

* retries
* validation
* logging
* error handling

---

# Planner Node

## Purpose

Convert a research topic into a structured research plan.

## Inputs

* request.topic
* request.report_type

## Outputs

* sections

## Allowed State Mutations

* state.sections
* state.status

## Forbidden State Mutations

* state.report
* state.global_context

## Failure Handling

Retry up to 2 times.

If planning fails after retries:

* mark workflow as failed
* emit error logs

---

# Global Research Node

## Purpose

Create a shared understanding of the topic before section-level research begins.

## Inputs

* request.topic

## Outputs

* global_context

## Allowed State Mutations

* state.global_context
* state.status

## Benefits

Provides common context to all section researchers.

Reduces duplicated content and conflicting statements.

---

# Section Research Node

## Purpose

Research an individual report section.

## Inputs

* section.title
* section.description
* request.topic
* global_context

## Outputs

* section.research_content
* section.sources

## Allowed State Mutations

* section.research_content
* section.sources
* section.revision_count

## Forbidden State Mutations

* state.report
* global_context

## Parallel Execution

Multiple section research tasks may execute concurrently.

Maximum parallelism is controlled through configuration.

---

# Section Review Node

## Purpose

Evaluate quality of section research.

## Inputs

* section.research_content
* section.sources

## Outputs

* ReviewFeedback

## Allowed State Mutations

* section.reviews

## Review Criteria

* completeness
* relevance
* source quality
* factual grounding
* clarity

## Revision Loop

If a section is not approved:

Research
↓
Review
↓
Research
↓
Review

until:

* approved
  or
* maximum revision count reached

---

# Writer Node

## Purpose

Combine approved sections into a coherent report.

## Inputs

* state.sections

## Outputs

* state.report

## Responsibilities

* create narrative flow
* connect sections
* remove duplication
* improve readability
* maintain report structure

## Non-Responsibilities

* research
* fact verification
* web search

---

# Final Review Node

## Purpose

Evaluate the report as a complete document.

## Inputs

* state.report

## Outputs

* updated state.report

## Evaluation Areas

* coverage
* consistency
* completeness
* structure
* readability
* logical flow

## Allowed State Mutations

* state.report
* state.status

---

# PDF Generation Node

## Purpose

Convert the final report into a portable document.

## Inputs

* state.report

## Outputs

* PDF artifact

## Storage Location

reports/

## Non-Responsibilities

* report writing
* research
* review

---

# Observability Requirements

Every node should emit:

* node start event
* node completion event
* execution duration
* error events
* retry events

---

# Future Enhancements

Potential future nodes:

* Citation Verification Node
* Fact Checking Node
* Research Expansion Node
* Source Ranking Node
* Evaluation Node

These are intentionally excluded from V1 to keep workflow complexity manageable.
