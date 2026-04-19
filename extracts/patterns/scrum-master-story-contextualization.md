---
title: "Scrum Master Story Contextualization"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "scrum-master-story-contextualization"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Multiple source documents exist (architecture docs, coding standards, tech stack, prior stories). A task dispatch mechanism sends work to executor agents. The executor agent operates within a bounded context window."
  invariants: "The executor agent receives a self-contained task file and never searches for supplementary information. The curator agent reads broadly but writes only the task file. Task files include acceptance criteria, implementation steps, and all referenced context inline."
  governance: "Curator output is reviewed before dispatch to executor. Source documents are versioned so stale context is detectable. Story status gates (draft -> approved) prevent premature execution."
  recovery: "If the executor fails due to missing context, the failure is routed back to the curator for context enrichment, not to the executor for search. If source documents change after story creation, affected stories are flagged for re-curation."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Scrum Master Story Contextualization

**Source:** [[scrum-master-story-contextualization]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Executor agents waste tokens and produce lower-quality output when they must search for their own context. Without a dedicated context curation step, executors load irrelevant information, miss relevant information, or hallucinate implementation details. The context window fills with noise instead of signal, and the executor's output quality degrades proportionally.

## Forces

- **Context completeness vs. context overload:** Including too little context causes the executor to guess; including too much wastes tokens and dilutes attention on the relevant material.
- **Curation cost vs. execution quality:** Adding a curation step introduces overhead (a second agent pass), which may be unnecessary for trivial tasks but critical for complex ones.
- **Source freshness vs. embedding stability:** Embedding context directly into the task file makes the executor self-contained but creates a staleness risk if the source documents change after curation.
- **Generality vs. task-specificity:** The executor needs both always-loaded general context (coding standards, tech stack) and story-specific context (relevant architecture sections, data models). Balancing these two layers is the curator's core challenge.

## Solution

Interpose a **context curator agent** between planning and execution. The curator reads broadly across project documentation and produces a self-contained task file that the executor consumes without any supplementary search.

The curator's responsibilities:

1. **Read the always-loaded baseline.** A fixed set of files the executor needs for every task: coding standards, tech stack, source tree, conventions. These are listed in a config (e.g., `dev-load-always-files`) and included in every task file.

2. **Select story-specific context.** Read the epic, architecture docs, data models, and directory structure. Extract only the sections relevant to this specific task. Embed them directly into the task file -- no references, no links, no "see also."

3. **Carry forward cross-story context.** When tasks have dependencies on prior work, include notes from previous stories. This prevents the executor from repeating solved problems or contradicting established decisions.

4. **Structure the task file for execution.** The file includes: acceptance criteria, step-by-step implementation tasks, embedded context sections, and placeholder sections for dev and QA notes. The executor reads this file and builds -- nothing else.

5. **Gate execution on approval.** Stories start in `draft` status. A human reviews the curated story and sets it to `approved` before the executor agent will process it. This prevents executing on incomplete or incorrect curation.

The key insight is that context engineering is a first-class concern that deserves its own agent role -- "giving the agent exactly what it needs to build its little piece of the kingdom."

## Consequences

**Positive:**
- Executor agents start with a focused, complete context window -- no searching, no guessing
- Token usage is minimized because only relevant context is loaded
- Implementation accuracy improves because the context window contains signal, not noise
- The pattern is composable: multiple executors can receive differently curated stories from the same source material
- The human gate on story approval catches curation errors before they propagate to execution

**Negative:**
- Two-agent overhead (curator + executor) may be unnecessary for trivial tasks
- The curator may include too much or too little context -- curation quality is itself a skill that requires tuning
- Embedded context becomes stale if architecture docs change after story creation
- The curator must understand the executor's needs well enough to select relevant sections, which requires knowledge of both the project and the executor's capabilities

## Known Uses

- BMad Method v6 multi-agent SDLC -- the Scrum Master agent explicitly curates developer stories with embedded context from architecture docs, tech stack, and prior stories
- MetaSystem skill files -- each SKILL.md is self-contained with embedded context, partially implementing this pattern without a dedicated curator agent
- Context engineering practices documented in ACE (Agentic Context Engineering) playbooks -- the principle of "minimum viable context" for agent execution
- Document sharding strategies that break large docs into task-relevant fragments for agent consumption

## Contract

### Preconditions
Multiple source documents exist that an executor agent would otherwise need to search (architecture docs, coding standards, tech stack, prior task outputs). A task dispatch mechanism sends work to executor agents. The executor agent operates within a bounded context window where irrelevant content degrades output quality.

### Invariants
The executor agent receives a self-contained task file and never searches for supplementary information during execution. The curator agent reads broadly across source documents but writes only the curated task file. Every task file includes acceptance criteria, implementation steps, and all referenced context inline -- no external references that require lookup. The always-loaded baseline and story-specific context are clearly separated within the task file.

### Governance
Curator output is reviewed by a human before dispatch to the executor (draft -> approved gate). Source documents are versioned so stale embedded context is detectable. Curation quality is assessed by tracking executor failures attributable to missing or incorrect context. The always-loaded file list is maintained centrally and updated when project conventions change.

### Recovery
If the executor fails due to missing context, the failure is routed back to the curator for context enrichment -- the executor does not search on its own. If source documents change after story creation, affected in-flight stories are flagged for re-curation before execution proceeds. If curation consistently includes irrelevant context (token waste), audit the curator's selection criteria and tighten the relevance filter.
