---
notion_id: 32b1e08b-9b34-81b9-aa1e-e9d3c0da6754
name: Context-Aware Routing Skill (Classifier → Sub-Skill Dispatch)
summary: A dedicated routing skill classifies incoming context (e.g., ticket type) and dispatches to specialized isolated sub-skills, rather than having one monolithic skill handle all cases. Enables modular
  skill composition.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- Perplexity Skills
adopted_in: []
sources:
- most-people-build-claude-skills-wrong-heres-what-w.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: tiered-context-injection-over-monolithic-files.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Context-Aware Routing Skill (Classifier -> Sub-Skill Dispatch)

## What It Is
An intake skill receives raw input (e.g., a customer support ticket), classifies it into one of N predefined categories, adds a routing tag, and exits. Separate, purpose-built skills exist for each category (FAQ lookup, escalation, RMA processing, etc.). The routing skill's only job is classification; the category-specific skills contain all execution logic. This mirrors the software engineering principle of separation of concerns — each skill does one thing well.

## Why It Matters
A single monolithic skill that handles all ticket types becomes fragile as complexity grows. Isolated skills are independently testable, easier to update without breaking other paths, and can use different tools or knowledge bases per category.

## Why People Are Using It
Bart explicitly demonstrates this for customer support: a router identifies ticket type and tags it, then FAQ/escalation/RMA skills each run independently. The pattern directly mirrors how real customer support teams organize specialists.

## Potential Alternatives
Single large skill with internal conditional branching. Rule-based keyword routing without LLM classification.

## Potential Improvements
Adding a confidence score to the routing output so low-confidence classifications can be flagged for human review rather than auto-dispatched.

## Potential Failure Modes
Classification errors at the routing layer cascade into incorrect sub-skill invocations with no recovery path. Boundary cases that don't fit any defined category fall through without handling.
