---
title: "Effort Scaling Rules Embedded in Orchestrator"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "effort-scaling-rules-embedded-in-orchestrator"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "System has a lead/orchestrator agent that can spawn subagents; query complexity is classifiable into discrete tiers; token/cost budgets are enforceable per query."
  invariants: "Resource allocation is always proportional to assessed task complexity. The orchestrator never delegates resource allocation decisions to subagents."
  governance: "Scaling tiers and their resource caps are reviewed quarterly or when model pricing/capabilities change materially. Tier boundaries are calibrated against historical cost data."
  recovery: "When a query exhausts its tier budget without resolution: escalate to the next tier up (with human approval if crossing a cost threshold). When a simple query is over-allocated: log the waste, tighten the tier classification rule."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Effort Scaling Rules Embedded in Orchestrator

**Source:** [[effort-scaling-rules-embedded-in-orchestrator]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Multi-agent orchestrators without explicit resource allocation rules default to naive strategies — typically spawning as many subagents as possible regardless of task complexity. This produces two symmetric failures: massive overinvestment in simple queries (50 subagents for a factual lookup) and underinvestment in complex research (one subagent for a multi-source comparison). Token usage, which drives 80% of performance variance in multi-agent systems, becomes unpredictable and wasteful.

## Forces

- **Cost vs. thoroughness.** Simple queries need minimal resources but complex queries demand deep, parallel investigation. A single allocation strategy cannot serve both.
- **Model judgment is unreliable for self-budgeting.** Without explicit rules, models tend to over-allocate (they default to "be thorough" heuristics rather than cost-aware ones).
- **Static rules vs. dynamic complexity.** Any fixed tier system will mis-classify edge cases — a seemingly simple query may require deep investigation, and vice versa.
- **Calibration drift.** As model capabilities and costs change, the right resource allocation per tier shifts. Rules that were optimal with one model may waste resources with the next.
- **Simplicity vs. adaptability.** Simple tier rules are easy to implement and debug but cannot handle the full spectrum of query complexity.

## Solution

Embed **explicit, tiered resource allocation rules** directly in the orchestrator's prompt. Each tier specifies the maximum number of subagents, tool calls, and token budget.

**Reference tiers (from Anthropic's production system):**

| Tier | Query Type | Subagents | Tool Calls | Example |
|------|-----------|-----------|------------|---------|
| 1 | Simple factual | 1 | 3-10 | "What is X's API rate limit?" |
| 2 | Comparison / synthesis | 2-4 | 10-15 | "Compare X and Y on dimensions A, B, C" |
| 3 | Complex multi-source research | 10+ | Divided roles | "Survey the landscape of approach Z across 5 domains" |

**Implementation rules:**

1. The orchestrator classifies each incoming query into a tier before spawning any subagents.
2. Tier classification criteria are explicit in the prompt (not left to model judgment).
3. Resource caps are hard limits — the orchestrator enforces them, subagents cannot override.
4. Each tier specifies not just quantity but role differentiation (Tier 3 subagents get divided responsibilities, not duplicated ones).

## Consequences

**Positive:**
- Predictable, controllable token costs per query type.
- Eliminates the "cost blowup" failure mode (identified as the #2 production killer in multi-agent systems).
- Makes resource allocation decisions auditable and debuggable.
- Prevents the "50 subagents for a factual lookup" anti-pattern.

**Negative:**
- Static tiers will mis-classify some queries, leading to under- or over-allocation at the margins.
- Tier boundaries require empirical calibration and periodic recalibration.
- Adding tiers increases orchestrator prompt complexity.
- Overly rigid rules prevent the system from adapting when a seemingly simple query requires deep investigation.

## Known Uses

- **Anthropic multi-agent research system:** Production deployment with the three-tier structure described above. Early versions without scaling rules routinely spawned 50 subagents for trivial queries.
- **MetaSystem research-loop:** Currently does not embed explicit scaling rules — this pattern would apply directly to orchestrator skills that spawn subagents.

## Contract

### Preconditions
- The system has a lead/orchestrator agent capable of spawning subagents.
- Query complexity is classifiable into discrete tiers (at minimum: simple, moderate, complex).
- Token and cost budgets are enforceable per query (the orchestrator can cap subagent spawning).

### Invariants
- Resource allocation is always proportional to assessed task complexity — never uniform regardless of query type.
- The orchestrator retains exclusive authority over resource allocation. Subagents cannot self-replicate or spawn additional subagents beyond their allocation.
- Every query is classified before any subagent is spawned.

### Governance
- Scaling tiers and their resource caps are reviewed quarterly or when model pricing/capabilities change materially.
- Tier boundaries are calibrated against historical cost-per-query data — not set once and forgotten.
- Mis-classification rates are tracked (queries that exhausted their tier budget or completed with significant unused budget).

### Recovery
- When a query exhausts its tier budget without resolution: escalate to the next tier (with human approval if crossing a cost threshold). Do not silently exceed the budget.
- When a simple query is over-allocated: log the waste, review the tier classification rule for that query pattern.
- When a new query type does not fit existing tiers: default to Tier 2 (moderate) and flag for tier system review.
