---
name: GStack Spec Team — Parallel Research Agents for Spec Gray Areas
summary: After a design doc is approved, 5 parallel specialist agents (Backend Architect, Frontend Designer, QA Strategist, Product Manager, Devil's Advocate) simultaneously research and surface concerns
  on spec gray areas — open decisions not resolved by the design doc. Results feed the spec before any persona-based review.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- gstack-planning-multi-persona-spec-review.md
related_findings:
- file: gstack-review-army-parallel-specialist-dispatch.md
  rel: same-problem
- file: specialized-parallel-agent-roles.md
  rel: same-problem
- file: gstack-specialist-role-architecture.md
  rel: enabled-by
- file: autoplan-auto-decision-pipeline.md
  rel: feeds-into
- file: capability-saturation-threshold-45-percent.md
  rel: contradicts
- file: claude-code-12-agent-primitives.md
  rel: enabled-by
- file: competitive-module-development-parallel-teams.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-04-20'
pipeline_status: raw
consumed_by: []
---

# GStack Spec Team — Parallel Research Agents for Spec Gray Areas

## What It Is

GStack's `/spec-team` skill operates after the design doc is approved and before the multi-persona spec review (auto-plan). It has two phases:

**Phase A — Gray Area Elicitation:** The agent surfaces design decisions not resolved by the design doc and asks the human to select which areas to explore (e.g., chat UI placement, LLM provider choice, conversation context window size, aggregation approach, credit pricing model, edge cases). Human selects areas of concern.

**Phase B — Parallel Specialist Dispatch:** 5 specialist agents are spawned in parallel, each researching the selected gray areas from a different angle:
- **Backend Architect** — infrastructure, database patterns, scalability, service layer design
- **Frontend Designer** — UI placement, component design, user interaction flow
- **QA Strategist** — edge cases, failure modes, test coverage gaps
- **Product Manager** — scope, user value, monetization model
- **Devil's Advocate** — challenges every assumption, surfaces risks the other agents missed

Each agent returns findings independently. The spec is updated with decisions derived from their combined output before proceeding to the auto-plan phase.

Token cost for Spec Team phase: ~200k tokens.

## Why It Matters

Design docs inevitably leave gray areas — decisions that weren't resolved in the discovery phase. Addressing gray areas with a single generalist agent introduces perspective bias: the agent naturally gravitates toward backend-centric or implementation-centric reasoning. Parallel specialist dispatch ensures each gray area is evaluated from multiple angles simultaneously, with no single perspective dominating.

The devil's advocate role is structurally important: it is explicitly tasked with challenging the other four agents' conclusions. Without this role, the system produces a consensus that may paper over legitimate concerns.

Unlike `gstack-review-army-parallel-specialist-dispatch` (which covers code review after implementation), this pattern operates on the spec before any code is written — its purpose is to complete the spec rather than evaluate code quality.

## Why People Are Using It

Demonstrated live on BookZero AI chat feature. Gray areas addressed included: dedicated page vs. slide-out panel vs. floating widget (UI), conversation context window size (5 vs. 10 vs. session), PostgreSQL RPC vs. ORM-style backend service layer (aggregation), credit pricing model, and cross-currency handling. Each decision was made before spec finalization, preventing design ambiguity from propagating into implementation.

## Potential Improvements

The 5-role taxonomy (Backend, Frontend, QA, PM, Devil's Advocate) is fixed in GStack. For domain-specific applications, roles like Security Architect, Compliance Officer, or Accessibility Specialist might be more relevant. The devil's advocate role could be strengthened by requiring it to explicitly enumerate what each other agent got wrong rather than producing independent critique. Output from parallel agents could be synthesized by a meta-agent rather than being processed by the human.

## Potential Failure Modes

Parallel dispatch of 5 agents costs ~200k tokens for spec research alone — before any review or implementation. Devil's advocate role may produce redundant pushback on already-resolved questions if it lacks visibility into what was decided in the design doc phase. Gray area selection by the human introduces survivorship bias — only the areas the human notices get specialist attention. The spec may still contain undiscovered gray areas that none of the five specialists surface.
