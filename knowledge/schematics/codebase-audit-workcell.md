---
title: "Codebase-Audit Workcell"
id: "codebase-audit-workcell"
type: "schematic"
category: "system-design"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-06-18"
updated: "2026-06-18"
author: "claude"
altitude: "top"
maturity: "seed"
grounded_in:
  - "ultra-review-multi-agent-bug-hunting-fleet"
  - "gstack-review-army-parallel-specialist-dispatch"
  - "llm-as-judge-pattern-for-verification-agents"
  - "subagent-isolation-contract"
  - "independent-eval-and-scoped-authority-commandments"
  - "agent-self-reporting-unreliability-independent-eval"
composed_of:
  - "systems/improvement-loop/.claude/skills/audit-system"
  - "systems/improvement-loop/.claude/skills/assess-skill"
  - "systems/improvement-loop/.claude/skills/assess-agent"
  - "systems/improvement-loop/.claude/skills/assess-prompt"
source_dd:
  - "DD-107"
tags:
  - "schematic"
  - "audit"
aliases:
  - "Audit Workcell"
  - "Whole-System Audit Fleet"
---

# Codebase-Audit Workcell

> Point a read-only fleet at a folder; it discovers the agentic artifacts inside, fans them out to
> independent assessors in isolated contexts, and returns a structured findings report — changing
> nothing.

This schematic captures the engine's own top-altitude composition (`/audit-system` dispatching the
per-artifact `/assess-*` skills) as a reusable configuration — the recurring shape of
"independently evaluate every artifact in a system, in parallel, without trusting any of them to
grade itself."

## Demand

| Axis | Value |
|------|-------|
| **Function** | audit |
| **Scope / lifespan** | project-bound (one run per target system; no standing state) |
| **Non-functionals** | data boundary: read-only on the audited system; reliability: high — coverage must be complete and the report must not hallucinate findings; autonomy need: high during the run, zero authority to change anything; cost: scales with artifact count (parallel subagents) |

Reach for this when you have an agentic system (skills, agents, prompts) and need a trustworthy,
comprehensive quality read that no single context could hold — and you want the evaluation done by
something other than the thing being evaluated.

## Configuration

### Capability + memory core

Discover artifacts by shape (skills, agents, prompts via globs), size them, and dispatch each to
the matching IL assessor (`/assess-skill|agent|prompt`). **No persistent memory** — each run is
stateless: it reads the target system plus the engine's KB-grounded assessment criteria, emits
artifacts (structural manifest, per-artifact findings, whole-system summary), and forgets. The
reusable core is "discover → bin-pack → dispatch to independent assessor → aggregate."

### Coordination / architecture

**Multi-agent fan-out (orchestrator–worker).** The orchestrator bin-packs artifacts into parallel
Librarian subagents under a per-subagent token ceiling (~250k); each subagent runs in an **isolated
fresh context** (no shared conversation state) and dispatches its artifacts to the appropriate
`/assess-*` skill. Results aggregate into one summary. Isolation is load-bearing: it prevents
cross-contamination between assessments and lets coverage scale past one context window.

### Autonomy

**observer** — read-only on the audited system by contract. The workcell produces findings and
recommendations and has **zero authority** to modify the target. The highest-autonomy *operation*
(parallel dispatch) is paired with the lowest-authority *scope* (change nothing) — deliberately.

### Deployment surface

Claude Code harness, using its parallel-subagent primitive. Runs in-session against a local folder;
no external runtime, no provider-API hosting.

## Evaluation & feedback

- **How it's evaluated:** the audit **is** independent evaluation. Each artifact is judged by a
  *separate* assessor invocation (LLM-as-judge — [[llm-as-judge-pattern-for-verification-agents]]),
  never by itself, in a fresh context that sees the artifact and the criteria but not the author's
  reasoning. This directly answers agent self-report unreliability
  ([[agent-self-reporting-unreliability-independent-eval]]).
- **Feedback mechanism:** **external + human.** External: the three emitted artifacts return to the
  system's owner as the feedback signal (what's well-formed, what's in debt). Human: Nick reviews
  the follow-up list and gates any remediation (the workcell never remediates). For the engine
  auditing *itself*, this feedback also flows back to producers via the consumer→producer principle.

## Grounding & composition

- **`grounded_in`** — the evidence:
  - [[ultra-review-multi-agent-bug-hunting-fleet]] — 5–20 parallel sub-agents from different
    positions + a verification pipeline; the canonical multi-agent audit-fleet shape.
  - [[gstack-review-army-parallel-specialist-dispatch]] — parallel specialist dispatch with
    cross-review dedup; grounds the bin-pack-and-dispatch coordination.
  - [[llm-as-judge-pattern-for-verification-agents]] — an independent judge sees only output +
    criteria; grounds the per-artifact assessor as a separate invocation.
  - [[subagent-isolation-contract]] — fresh context, explicit skills, no nesting; grounds the
    isolation that makes parallel assessment trustworthy and bounded.
  - [[independent-eval-and-scoped-authority-commandments]] — build independent eval from day one and
    scope authority with guardrails; grounds the observer (read-only) autonomy choice.
  - [[agent-self-reporting-unreliability-independent-eval]] — never trust agent self-reports;
    grounds the entire "evaluate from outside" premise.
- **`composed_of`** — what it's built from:
  - `/audit-system` — the orchestrator (discover, bin-pack, dispatch, aggregate).
  - `/assess-skill`, `/assess-agent`, `/assess-prompt` — the per-artifact independent assessors.

## Risk & maturity

- **Known risks / failure modes:** (1) incomplete discovery — a non-standard artifact shape escapes
  the globs and is silently uncovered (coverage must be reported, not assumed); (2) cross-subagent
  blind spots — whole-system invariants that no single per-artifact assessor catches (the v1
  workcell is composition-only, empty whole-system invariants per Rule 11); (3) token-ceiling
  mis-packing under-utilizing or overflowing a subagent.
- **Maturity:** seed — the composition is real and runs (`/audit-system` v1), but it has not been
  exercised against a *foreign* system at scale, and its whole-system-invariant layer is
  intentionally empty pending demand.
- **Revisit when:** whole-system invariants earn their keep (a recurring cross-artifact defect class
  appears), the workcell is run against a non-engine codebase, or any `grounded_in` finding moves.
