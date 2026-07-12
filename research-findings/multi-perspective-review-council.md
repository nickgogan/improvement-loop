---
name: "Multi-Perspective Review Council (Specialized Critics + Orchestrator)"
summary: |-
  Replace the single review agent with a council of specialized critics, each covering
  one review dimension: a factual-correctness critic equipped with web-search tools to
  ground itself in real sources, a domain-relevance checker, a safety critic (sensitive
  content, security risks, policy violations), and a style critic. An orchestrate
  command coordinates all four across multiple rounds — the main agent applies round-1
  fixes, then respins the full council. The orchestrator (rather than direct
  agent-to-agent debate) is chosen because one agent must hold cross-round context.
  Rationale: review is inherently multi-perspective, and one agent covering every aspect
  misses blind spots.
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "IL (review/assessment design)"
  - "General"
adopted_in: []
sources:
  - "5-insane-claude-loops.md"
related_findings:
  - file: "role-voting-for-autonomous-design-decisions.md"
    rel: "same-problem"
  - file: "generator-assessor-separation-in-skill-iteration.md"
    rel: "extends"
  - file: "persona-clone-review-board.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

A review loop where the assessor side is decomposed by dimension instead of unified in
one agent. AI LABS' concrete instantiation uses four critics — factual correctness (with
web-search tools so claims are checked against real sources), domain relevance (is the
reviewed thing actually on-goal), safety (sensitive content, security, policy), and
style (clarity, fit to target voice) — tied together by an `orchestrate` command
containing the coordination instructions and the handling of each critic's feedback.
Rounds repeat: fixes from round N are applied before the council respins for round N+1.
They explicitly compared it to Karpathy's LLM-council idea and to direct agent-teams
communication, choosing the orchestrator variant because one coordinating agent needs to
retain the context of previous rounds. Works for non-code outputs as well as code.

## Why It Matters for Us

The engine's rule-10 stance already separates generator from assessor; this pattern is
the next decomposition — separating assessors from each other by dimension. The
per-critic tool grants are the notable implementation detail (only the factual critic
gets web search), which keeps each critic narrow and auditable. Relevant background for
how /assess-* skills or /audit-artifacts could fan out review dimensions, if
multi-dimension coverage gaps ever show up in practice.

## Why People Are Using It

AI LABS (2026-07-09) built it after finding a single review agent "covering every aspect
on its own" missed blind spots; they run it for both code and content. Converges with
existing KB findings on role-based multi-perspective deliberation (gstack role voting,
deep-plan exploration) from an independent practitioner.

## Potential Alternatives

- **Single reviewer with a multi-dimension rubric**: cheaper, one context; loses the
  independence that catches blind spots.
- **Agent-teams direct debate** (LLM-council style): richer interaction, but no single
  agent holds cross-round memory, and coordination cost rises.

## Potential Improvements

- Verdict reconciliation rules for when critics conflict (style vs safety).
- Dimension selection per artifact type instead of always running all four.

## Potential Failure Modes

- Token multiplication: every round runs N critics; multi-round runs get expensive fast.
- Feedback collisions: fixes satisfying one critic can regress another, oscillating
  across rounds without a reconciliation rule.
- False coverage: four named dimensions feel exhaustive but are just four; the
  unassigned dimension is still nobody's job.
