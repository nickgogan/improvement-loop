---
name: Graceful Degradation Modes for Agent Failure
summary: 'When agents fail, they should degrade gracefully rather than hallucinate or crash. Four degradation modes: (1) answer with retrieval-only when planning fails; (2) request clarification instead
  of hallucinating; (3) escalate ambiguous cases to human review; (4) return partial answers with explicit uncertainty markers. Combined with hard budget enforcement (max tool calls, token budgets, wall-clock
  limits).'
implementation_notes: MetaSystem agents currently either succeed or fail with no intermediate states. Adding explicit degradation modes to skills would improve reliability. The 'request clarification' mode
  is most immediately applicable -- skills that encounter ambiguity should ask rather than guess (aligns with global preference in CLAUDE.md).
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- ai-agents-in-production-2026-nick-gupta-linkedin.md
related_findings:
- file: agent-cost-blowup-mitigation-strategies.md
  rel: same-problem
- file: stop-rules-as-execution-boundaries.md
  rel: same-problem
- file: gsd-stall-detection-revision-loop-escalation.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- production-agent-execution.md
- autonomous-scheduled-agent-operation.md
---

# Graceful Degradation Modes for Agent Failure

## What It Is

A set of fallback behaviors for when agent systems encounter failures, rather than allowing hallucination, infinite loops, or crashes:

1. **Retrieval-only fallback:** When planning fails, skip the planning phase and answer directly from retrieved evidence. Lower quality but still grounded.
2. **Clarification request:** When inputs are ambiguous or evidence is insufficient, ask for clarification instead of guessing. Requires the agent to recognize its own uncertainty.
3. **Human escalation:** When the agent's confidence is below threshold or the decision exceeds its autonomy tier, escalate to human review with full context.
4. **Partial answer with uncertainty:** Return what the agent can answer with confidence, explicitly mark what it cannot answer, and explain why.

These are paired with **hard budget enforcement**: maximum tool calls per run, token budget per phase, wall-clock time limits, max context size, approval thresholds for privileged actions. When budgets are exceeded, the agent enters a degradation mode rather than continuing to spend.

## Why It Matters

Most agent failures in production are not binary (works/doesn't work) -- they are degraded states where the agent produces plausible but incorrect output. Explicit degradation modes make failure visible and controlled rather than silent and compounding. The alternative -- agents that hallucinate when they're stuck -- is the most common production failure pattern.

## Why People Are Using It

Nick Gupta documents these as reliability patterns for production agent systems. The patterns draw from established resilience engineering concepts: circuit breakers, fallback strategies, and graceful degradation in distributed systems. The approach treats agent systems as distributed services that must handle partial failure.

## Potential Improvements

Adaptive degradation: the system learns which degradation mode produces the best outcomes for each failure type. Degradation telemetry: track how often each mode is triggered and whether human escalations result in different decisions than the agent would have made.

## Potential Failure Modes

Agents may trigger degradation too eagerly (over-cautious) or too rarely (overconfident). Clarification requests that are too frequent create user fatigue. Partial answers that are misleadingly confident about the parts they do answer.
