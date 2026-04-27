---
title: "Tier-Based Orchestrator Effort Scaling Rules"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "effort-scaling-rules-embedded-in-orchestrator"
identification_report: "session-persistence-and-memory.harvest-queue.md::effort-scaling-rules-embedded-in-orchestrator::rule::tier-based-orchestrator-effort-scaling-rules"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
    - "lead/orchestrator agents that spawn subagents to handle user queries"
    - "research and synthesis pipelines where query complexity varies widely across requests"
    - "any agent system where token-budget overrun has been observed or is a foreseeable failure mode"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — remove or revise the tier table in the orchestrator prompt; no migration cost"
  auditability: "high when orchestrator logs capture tier classification and spawn counts per query; medium when only aggregate spend metrics are retained"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Pattern is production-deployed at the source organization; no formal adoption in the extracting system at extraction time."
contract:
  preconditions: "An orchestrator/lead agent that spawns subagents and issues tool calls. The orchestrator handles multiple query complexity classes. Subagent spawn count and per-subagent tool-call budget are configurable at spawn time. The orchestrator's system prompt or skill definition can be modified to embed allocation rules."
  invariants: "Before each subagent spawn, the orchestrator declares a tier classification, names the tier's subagent and tool-call budget, and confirms the planned spawn fits within that budget. Tier thresholds are concrete numbers in the prompt, not deferred to model judgment. Mid-task tier upgrades are explicit and recorded, not silent."
  governance: "Owner: Whoever maintains the orchestrator's system prompt or skill definition. Tier thresholds are reviewed and recalibrated periodically as model capabilities and per-call costs change. Any skill or agent that orchestrates subagents must declare its tier table — orchestrating-skill audit tooling validates presence. Mid-task tier upgrades require recorded rationale."
  recovery: "If the orchestrator spawns beyond budget without justification, halt and re-classify. If a tier proves systematically insufficient for its query class, recalibrate the tier thresholds (do not simply accept overruns). If a query genuinely does not fit the tier table, treat as a signal that a new tier or sub-tier is needed. If model capabilities/costs shift materially, schedule a tier-table review."
tags:
  - "extracted-artifact"
  - "rule"
---

# Tier-Based Orchestrator Effort Scaling Rules

**Source:** [[effort-scaling-rules-embedded-in-orchestrator]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A lead/orchestrator agent receives a query whose execution may involve spawning subagents and issuing tool calls against external resources. Multiple complexity classes of query are routinely served by the same orchestrator (factual lookups, comparisons, and deep multi-source research). Without explicit allocation guidance, the orchestrator's default behavior trends toward over-spawning subagents on simple queries (token waste) or under-spawning on complex ones (incomplete answers).

## Action

**Required:** The orchestrator's prompt embeds an explicit, tiered resource-allocation table consulted before every subagent spawn. A canonical three-tier shape:
- **Tier 1 — Simple factual query:** 1 subagent, 3-10 tool calls.
- **Tier 2 — Comparison/synthesis query:** 2-4 subagents, 10-15 tool calls.
- **Tier 3 — Complex multi-source research:** 10+ subagents with explicitly divided roles.

The orchestrator classifies the incoming query into a tier first, then allocates within that tier's budget. Tier thresholds are written into the prompt as concrete numbers, not left to model judgment.

**Forbidden:** Spawning subagents without a declared tier classification. Exceeding tier budgets without a recorded justification. Using a single "spawn as many as possible" default. Leaving the allocation policy implicit ("the model knows what's reasonable") — that is the failure mode this rule exists to prevent.

## Boundary

Enforced at the orchestrator's spawn-decision boundary — the moment the lead agent decides how many subagents to dispatch and how many tool calls each may issue. Lives in the orchestrator's system prompt (or skill definition for orchestrating skills). Applies for the duration of the orchestrated task; tier may be revised mid-task only with explicit justification (e.g., a Tier-1 query reveals unexpected complexity warranting Tier-2 expansion).

## Enforcement

- **Mechanism:** Explicit tier table in the orchestrator's prompt. Spawn-time check requires the orchestrator to (1) name the tier, (2) state the budget, (3) confirm the planned spawn fits the budget.
- **Check (deterministic):** `(tier_declared == true) AND (subagent_count <= tier_max) AND (tool_calls_per_subagent <= tier_max)`. Reviewable from orchestrator logs.
- **Violation response:** If the orchestrator exceeds budget without recorded justification, halt the spawn and re-classify. If a Tier-1 classification proves insufficient mid-task, explicitly upgrade to Tier-2/3 with a recorded rationale rather than silently expanding. Periodically recalibrate tier thresholds as model capabilities and costs evolve.

## Rationale

Token usage explains roughly 80% of performance variance in multi-agent systems (per practitioner analyses). Effort-scaling rules are the primary controllable lever on token budget. Without them, lead agents default to over-allocation on simple queries (early production systems were observed spawning 50 subagents for a single factual question) and under-allocation on complex ones. Explicit tiered rules transform the orchestrator from a naive maximizer into a deliberate resource allocator — matching investment to query complexity. The rule is the positive-space reformulation: instead of enumerating cost-blowup failure modes, declare the budget tiers up front.

## Failure Modes

- **Static tiers under-allocate for unusually complex Tier-1 instances.** A "simple factual" query that turns out to require multi-source verification gets only 1 subagent and 3-10 calls. Mitigation: allow explicit mid-task tier upgrades with recorded rationale; do not silently exceed budget.
- **Over-rigid tier table prevents adaptive scaling.** Orchestrator refuses to expand even when initial Tier-1 results are clearly insufficient. Mitigation: pair static tiers with an adaptive escalation path (start small, expand on signal) rather than treating tier as immutable per query.
- **Tier thresholds drift from current model capabilities and pricing.** Numbers calibrated to one model generation become wrong when costs or capabilities change materially. Mitigation: schedule periodic tier-table reviews; treat thresholds as governance-versioned, not eternal.
- **Implicit allocation re-emerges through prompt erosion.** Successive prompt revisions blur the explicit numbers back into vague guidance ("use judgment"). Mitigation: orchestrating-skill audit tooling validates the tier table is present with concrete numbers, not soft language.
- **Tier classification itself becomes the bottleneck.** Orchestrator spends disproportionate effort classifying simple queries. Mitigation: keep tier definitions short and pattern-matchable; default to Tier 1 on ambiguity.

## Contract

### Preconditions
An orchestrator/lead agent that spawns subagents and issues tool calls. The orchestrator handles multiple query complexity classes. Subagent spawn count and per-subagent tool-call budget are configurable at spawn time. The orchestrator's system prompt or skill definition can be modified to embed allocation rules.

### Invariants
Before each subagent spawn, the orchestrator declares a tier classification, names the tier's subagent and tool-call budget, and confirms the planned spawn fits within that budget. Tier thresholds are concrete numbers in the prompt, not deferred to model judgment. Mid-task tier upgrades are explicit and recorded, not silent.

### Governance
Owner: Whoever maintains the orchestrator's system prompt or skill definition. Tier thresholds are reviewed and recalibrated periodically as model capabilities and per-call costs change. Any skill or agent that orchestrates subagents must declare its tier table — orchestrating-skill audit tooling validates presence. Mid-task tier upgrades require recorded rationale.

### Recovery
If the orchestrator spawns beyond budget without justification, halt and re-classify. If a tier proves systematically insufficient for its query class, recalibrate the tier thresholds (do not simply accept overruns). If a query genuinely does not fit the tier table, treat as a signal that a new tier or sub-tier is needed. If model capabilities/costs shift materially, schedule a tier-table review.
