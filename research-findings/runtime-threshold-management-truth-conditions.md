---
name: "Runtime Threshold Management and Truth Conditions Framework"
summary: "Steps 9-10 of the governed build order: a threshold management layer acts as a pressure valve that escalates or contains behaviors based on live signals, verified by a truth conditions framework that checks three distinct levels — semantic correctness, procedural soundness, and historical accuracy."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "11-step-governance-build-order-multi-agent-systems.md"
related_findings:
  - file: governed-dependency-chain-build-order.md
    rel: part-of
  - file: tool-model-io-contracts-with-preconditions.md
    rel: depends-on
  - file: agent-identity-governance-enforcement-layer.md
    rel: same-problem
  - file: budget-governance-with-hard-stop.md
    rel: same-problem
  - file: stop-rules-as-execution-boundaries.md
    rel: same-problem
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
pipeline_status: "raw"
---

## What It Is

Steps 9 and 10 of the 11-step governed multi-agent build order. This is the live containment layer — defined only after all structural reference models are established, because runtime controls must validate against the structures they protect.

**Two components:**

**Step 9 — Threshold Management:**
Acts as a "pressure valve" defining when a behavior must be escalated or contained based on live signals. Unlike static preconditions (Step 7), thresholds respond to runtime conditions:
- Volume signals (is the system processing more events than expected?)
- Error rate signals (are failures accumulating?)
- Authority signals (is an actor approaching or exceeding its authority ceiling?)
- Temporal signals (has the system been in a state longer than permitted?)

When a threshold is crossed, the system either escalates (notifies a human or higher-level orchestrator) or contains (pauses, limits, or terminates the behavior).

**Step 10 — Truth Conditions Framework:**
A verification layer that checks whether an action is valid across three independent dimensions:
1. **Semantically correct** — does the action conform to the ontology and event schema? (Validates against Layers 1-2)
2. **Procedurally sound** — is the action permitted given the current state machine position, actor passport, and policy layer? (Validates against Layers 3-6)
3. **Historically accurate** — is the action consistent with the provenance trail? Does it reference events and states that actually occurred? (Validates against Layer 8)

Validating all three distinct levels of truth is what "proves the system governable." A system that only checks semantic correctness may allow procedurally invalid actions. A system that only checks procedural soundness may allow actions based on fabricated history.

## Why It Matters

Most agent governance focuses on entry-point controls (who can act, what tools are available). Runtime thresholds address a different failure mode: behaviors that start within bounds but accumulate into out-of-bounds states through individually valid steps. A cascade of small decisions, each locally valid, can produce globally invalid outcomes without threshold management to detect the accumulation pattern.

The three-level truth conditions framework is particularly distinctive: it requires proof at all three levels simultaneously. This prevents a common failure mode where agents satisfy the observable governance checks (semantic and procedural) while relying on hallucinated or fabricated historical context (the third level).

## Why People Are Using It

Practitioner-documented in the 11-step governance build order. The three-level truth conditions framework echoes formal verification concepts from computer science — specifically the combination of syntax (semantic), semantics (procedural), and consistency (historical) checking. Applied to multi-agent systems, it provides a structured proof of governability rather than just a claim of compliance.

## Potential Improvements

- Adaptive thresholds: learn normal operating ranges from historical data and set thresholds dynamically rather than statically
- Cross-agent threshold aggregation: thresholds that monitor behavior across all agents in a system, not just individual agent instances, to catch distributed accumulation patterns
- Truth condition audit: log which truth conditions were checked and their results for each action, not just whether the action was ultimately permitted or denied

## Potential Failure Modes

- **Threshold over-triggering**: Thresholds set too conservatively generate excessive escalations, training human operators to ignore them (alert fatigue)
- **Truth condition ordering effects**: Checking conditions in different orders may produce different results if the checks themselves have side effects
- **Historical accuracy spoofing**: If the provenance trail (Layer 8) itself can be tampered with, the historical accuracy check fails to detect fabricated history
- **Threshold gaming by patient actors**: Actors that stay just below individual thresholds while accumulating impact over time may evade detection
- **Performance at scale**: Running three independent truth condition checks per action adds latency that may not be acceptable for high-throughput systems
