---
name: 'Task Complexity Tiering: Quick Task, Campaign, Deep Build'
summary: Three-tier task classification that determines agent planning depth and session architecture. Quick tasks run inline; campaigns break into subtasks with multiple deliverables; deep builds invoke
  full phase-based planning with many output files.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- stop-using-claude-code-in-terminal.md
date_discovered: '2026-04-07'
last_updated: 2026-04-08
related_findings:
- file: agent-architecture-layer-impermanence.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---

## What It Is

A three-tier classification system for agent tasks that determines the planning depth and execution architecture for each goal. Documented by Simon Scrapes as part of a command center built on top of an "Agentic OS":

1. **Quick Task** -- Single-turn or short iterative exchange. Agent handles it inline with minimal planning overhead. Example: "Write a LinkedIn post about X."
2. **Campaign** -- Multiple deliverables requiring subtask decomposition. Agent breaks the goal into component tasks that may run in parallel. Example: "Build a content repurposing system."
3. **Deep Build** -- Full phase-based planning with extensive output files, phase execution gates, and detailed architecture. Example: "Build a lead generation system from scratch."

The user selects the tier when submitting a goal. The system then adjusts agent behavior accordingly -- how much planning to do, whether to break into subtasks, and how many files/phases to produce.

## Why It Matters

Without tiering, agents either under-plan simple tasks (wasting tokens on unnecessary architecture) or under-plan complex tasks (producing shallow outputs). The tier selection is a form of intent engineering -- it signals to the agent what level of depth is expected. This maps to the existing "Context Enrichment for Task Clarity" finding but adds an explicit structural mechanism.

## Why People Are Using It

Practitioners running multiple agents concurrently need predictable execution profiles. A quick task should complete in minutes with minimal review. A deep build might run for hours across multiple phases. Knowing which tier a task falls into helps the human operator allocate attention and set expectations for turnaround time.

## Potential Improvements

Auto-detection of task complexity based on goal description could eliminate the manual selection step. Tier-specific token budgets could enforce cost discipline. Integration with the GSD skill's phase system would be a natural implementation path for MetaSystem.

## Potential Failure Modes

Users may default to "Quick Task" for everything to avoid planning overhead, leading to shallow outputs on complex goals. Conversely, over-specifying "Deep Build" for simple tasks wastes tokens on unnecessary planning. The tier boundaries are subjective and may not generalize across different domains.
