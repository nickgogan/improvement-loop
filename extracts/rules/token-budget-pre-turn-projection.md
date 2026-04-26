---
title: "Token Budget Tracking with Pre-Turn Projection Checks"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "token-budget-pre-turn-projection"
extraction_date: "2026-04-19"
last_change_session: 44
last_change_sl: "session-44-codifier-extraction-run"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic execution loops with configured token or turn budget parameters"
    - "agent harness implementations that manage API call orchestration"
    - "long-running or cost-sensitive automated agent workflows"
  platform_coupling: "agnostic"
  autonomy: "autonomous-only"
  stage: "operate"
  reversibility: "trivial — pre-turn projection is additive logic in the execution loop; removal reverts to post-hoc budget enforcement with no data loss"
  auditability: "high — projection checks and their outcomes (proceed vs. degrade) are loggable at the execution loop layer; overage events produce explicit log entries"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Anthropic production Claude Code applies this pattern in its execution loop configuration; no equivalent budget projection mechanism deployed in this workspace as of extraction date."
contract:
  preconditions: "An agentic execution loop is running with at least one configured budget parameter. A projection mechanism exists in the loop implementation."
  invariants: "No API call is issued without a preceding projection check. Budget thresholds are static for the duration of a run. A degradation path is always reachable."
  governance: "Owner: MetaSystem / Claude Build system. Budget parameters are set per-agent in configuration; changes to projection logic require a DD."
  recovery: "If post-hoc overage detected: terminate run immediately, preserve state, log overage with projected vs. actual counts, audit and patch projection algorithm."
tags:
  - "extracted-artifact"
  - "rule"
---

# Token Budget Tracking with Pre-Turn Projection Checks

**Source:** [[token-budget-pre-turn-projection]]
**Form:** rule
**Extraction date:** 2026-04-19

## Condition

Before every API call in an agentic execution loop where token budgets (max_turns, max_tokens, compaction_threshold) are configured.

## Action

The system MUST project the estimated token cost of the next API call before issuing it. If the projected usage would exceed any configured budget threshold, execution MUST stop before the call is made — not after. Graceful degradation must be triggered at the pre-call gate.

## Boundary

Enforced at the agent execution loop layer, before each outbound API call. Applies to all agentic runs with configured budget parameters.

## Enforcement

- Execution loop must include a projection step before each API call.
- Budget configuration must specify max_turns, max_tokens, and compaction_threshold explicitly — no implicit defaults.
- If projection exceeds threshold, a degradation path (not a hard crash) must be defined and reachable.
- Anti-pattern flag: Any loop that checks token usage only after receiving a response is non-compliant.

## Rationale

Without pre-turn checks, agents exceed budgets by the margin of a single expensive call. Post-hoc limits waste the final call's cost and can leave the agent in a partially-committed state. Anthropic's production Claude Code configuration applies this pattern.

## Contract

### Preconditions
An agentic execution loop is running with at least one configured budget parameter. A projection mechanism exists in the loop implementation.

### Invariants
No API call is issued without a preceding projection check. Budget thresholds are static for the duration of a run. A degradation path is always reachable.

### Governance
Owner: MetaSystem / Claude Build system. Budget parameters are set per-agent in configuration; changes to projection logic require a DD.

### Recovery
If post-hoc overage detected: terminate run immediately, preserve state, log overage with projected vs. actual counts, audit and patch projection algorithm.
