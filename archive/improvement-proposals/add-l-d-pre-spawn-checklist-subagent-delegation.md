---
notion_id: "32c1e08b-9b34-812d-8ea8-ea65695fd096"
name: "Add L > D Pre-Spawn Checklist for Subagent Delegation"
proposal: "Add a mandatory pre-spawn validation checklist to all subagent delegation points. Before any agent spawns a subagent, it must verify: (1) Is the task parallelizable? (2) Is information loss tolerable? (3) Has the context window actually been exhausted? If any answer is 'no,' keep execution single-agent. Also embed this checklist into the research-proposer skill workflow so it is applied when matching proposals to system components."
rationale: "L > D Hypothesis (Strong evidence): Information loss across agent boundaries typically exceeds context degradation. Google's empirical study (arxiv 2512.08296) shows independent agents amplify errors 17.2x, centralized 4.4x. Sequential tasks degrade 39-70% with multi-agent. Validates single-agent preference but needs formalization."
status: "Not started"
target_system: "General / Cross-System"
priority: "P1 (Implement Now)"
risk_level: "Low"
implementation_complexity: "Low"
effort: "Low (< 1 hour)"
door_type: "Two-Way"
ops_impact: "Reduces Ops Burden"
conflicts: false
conflict_group: null
findings: []
date_proposed: "2026-03-23"
date_resolved: null
---

# Add L > D Pre-Spawn Checklist for Subagent Delegation

## Current State
Subagent delegation decisions are currently made ad-hoc based on agent judgment. The Perplexity system has subagent_usage guidance, S3 has wave-based subagent orchestration, but neither includes a formal pre-spawn validation gate. The GSD2 Iron Rule ("One Task, One Context Window") exists as a finding in the KB but isn't operationalized as a checklist at delegation points.

## Proposed Change
Add a three-question pre-spawn checklist to every subagent delegation point across all systems:

1. **Parallelizable?** Can this task be meaningfully split into independent units that don't need each other's intermediate results?
2. **Loss-tolerant?** If the subagent misses some context from the parent, will the output still be useful? (Research: yes. Sequential code implementation: no.)
3. **Context-exhausted?** Has the parent agent's context window actually been consumed to the point where delegation is necessary, or is this a convenience delegation?

If any answer is "no," the task stays single-agent.

Additionally, integrate this checklist into the research-proposer skill as a standard evaluation criterion when assessing proposals that add multi-agent complexity. Any proposal that increases agent-to-agent handoffs should be evaluated against L > D.

## Rationale
The L > D Hypothesis, backed by Google's 180-configuration empirical study, establishes that information loss across agent boundaries (L) typically exceeds context degradation (D). Multi-agent swarms degrade sequential tasks by 39-70%. This finding has Strong evidence strength and is flagged P1. The checklist operationalizes this finding into a lightweight gate that prevents the most common subagent misuse patterns.

## Door Type Assessment
Two-way door. The checklist is an additive validation step. If it proves too restrictive (blocking useful delegations), individual questions can be relaxed or the checklist can be removed entirely. No system behavior changes irreversibly.

## Implementation Assessment
Low complexity. Requires adding checklist text to: (1) Perplexity subagent_usage guidelines, (2) S3 CLAUDE.md subagent delegation section, (3) research-proposer skill's Phase 4 assessment criteria. All are text/config changes in existing files. No code changes, no schema migrations.

## Operational Impact
Reduces ops burden. Prevents unnecessary subagent spawning, which reduces token spend, debugging complexity, and "telephone game" information loss. No new monitoring or maintenance required.

## Implementation Steps
1. Add the 3-question checklist to the Perplexity system's subagent_usage section
2. Add the checklist to S3's CLAUDE.md under subagent delegation guidance
3. Add "L > D assessment" as a standard criterion in the research-proposer's Phase 4 (Cost & Complexity Assessment) -- any proposal adding multi-agent handoffs must pass the checklist
4. Update the delta report template to flag proposals that increase agent-to-agent boundaries
