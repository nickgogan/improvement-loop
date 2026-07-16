---
name: Recurrence Threshold Gates Autonomy, Not Direction
summary: 'A lesson becomes eligible for promotion to a system change only after N recurrences (CareerBuddy: N=2 normal severity, N=1 for high severity). Crossing the threshold makes the agent allowed to
  draft a proposal — it never weakens the human gate. The inverse also holds: explicit operator direction can promote below threshold, because the threshold exists to gate agent autonomy, not to constrain
  the human.'
implementation_notes: How this could apply to the MetaSystem engine — Phase 2 of its restructure program will size a second-brain-for-operations against this store model; IB-172 (layered memory architecture)
  is the related backlog item. Nick's standing "3+ recurrences before mechanism" rule is the same shape with a different N; CareerBuddy shows N is an operator-set parameter with recorded rationale (low
  session volume + human gate filters noise → N=2), not a constant.
category: Governance
evidence_strength: Medium (practitioner-documented, single production system with live store evidence)
adoption_status: Not Yet Started
priority: P1 (Direct Adoption)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-ops-self-improve.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: synthesized
consumed_by:
- agent-governance-and-trust.md
tags:
- recurrence-threshold
- human-gate
- self-improvement
- autonomy
---

# Recurrence Threshold Gates Autonomy, Not Direction

## Why It Matters

Self-improving systems face two opposite failure modes: acting on every one-off observation (mechanism spam, noise codified into rules) and requiring the human to notice everything (the human stays the bottleneck). A recurrence threshold splits the difference — but only if everyone is clear about *what the threshold gates*. CareerBuddy's formulation is the durable part: **"threshold gates autonomy, not direction."** The agent needs N occurrences before it may push a change proposal; the human needs zero.

## What It Is

In CareerBuddy's promotion rules (operator-set 2026-07-07):

- **Normal severity: N=2 occurrences.** Recorded rationale: "session volume is low and the human gate filters noise — waiting for a third recurrence delays learning more than it protects quality."
- **High severity: N=1.** Data loss, governance breach, or user-visible failure earns a proposal on first observation.
- Crossing the threshold makes a lesson *eligible* — promotion still runs the full pipeline (sandbox, separate-context grading, per-proposal human gate). "Nothing about the threshold weakens the gate."

## How It Works

- The threshold is checked deterministically: the store checker counts dates in each open lesson's Occurrences list and emits a `PROMOTE` flag at threshold (`N=2 normal, 1 high` are constants in `store_check.py`).
- **Direction overrides threshold.** The proposal log repeatedly records "operator-directed promotion below threshold (allowed: threshold gates autonomy, not direction)" — P-2, P-6, P-11, P-16 were all applied at one occurrence because the operator asked. The threshold never blocks the human.
- **Severity is the second axis.** A high-severity lesson (e.g. CareerBuddy's L-6: a workspace rename silently stranding all repo memory) doesn't wait for a repeat of a data-loss event.
- The threshold is a *tuned parameter with a paper trail*: the value, the date it was set, and the rationale live in the promotion-rules reference — so a future operator can retune it against observed session volume instead of cargo-culting it.
- Live calibration evidence: of 20 lessons, those promoted at threshold (L-1, L-3 at 2 occurrences) and those promoted on direction at 1 occurrence both flowed through the identical downstream gate; L-2 and L-13 sit open below threshold, correctly untouched.

## How It Could Fail

- N tuned for one session cadence misfires at another: N=2 in a high-volume system would flood the gate; N=3+ in a low-volume system means lessons rot before acting (CareerBuddy's explicit reason for choosing 2).
- If the threshold is read as gating the *human*, urgent operator-directed fixes get bureaucratically deferred — the anti-pattern the formulation exists to prevent.
- Severity inflation: if everything is marked `high` to skip the wait, the threshold stops filtering; CareerBuddy pins `high` to three named conditions and forbids silent lowering.
