---
title: "The Deletion Test for No-Op Instructions"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "skill-pruning-failure-modes-noop-deletion-test"
identification_report: "defending-agent-context.harvest-queue.md::skill-pruning-failure-modes-noop-deletion-test::rule::deletion-test-for-no-op-instructions"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "defending-agent-context.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "anyone auditing or pruning a context artifact (a skill file, an always-loaded instruction file, an agent system prompt) that has grown oversized"
    - "reviewers of agent-written instructions, which systematically accrete passages that restate behavior the model already does by default"
    - "authors deciding, per paragraph, whether an instruction earns the tokens it costs"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — a paragraph removed by a wrong deletion-test call is restorable from version control; the rule itself is a review discipline with no migration cost"
  auditability: "high — the deletion test is a binary per-paragraph check any reviewer can re-run; it can be confirmed empirically with with/without-section eval runs (the cheap thought-experiment is an approximation of the A/B)"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "The originating practitioner applies these pruning techniques across one of the most-downloaded skill repositories in circulation; the sediment failure mode is independently familiar to anyone maintaining shared instruction files."
contract:
  preconditions: "A context artifact (a skill file, an always-loaded instruction file, an agent system prompt, or equivalent) is being authored or audited — especially one written by an agent, which systematically produces no-ops. The reviewer can reason about the model's default behavior (its priors)."
  invariants: "Every retained paragraph passes the deletion test: deleting it would change agent behavior. Instructions that merely restate model-default behavior are removed. Hard constraints (security boundaries, gates) are exempt — they may look like no-ops precisely because they rarely bind, and are retained regardless of the deletion-test result."
  governance: "Owner: the maintainer of the context artifact. The deletion test is applied per paragraph at authoring review and at audit. On shared artifacts, ownership and pruning rules must exist so that 'kill it dead' does not degenerate into a pruning war (sediment courage without governance)."
  recovery: "A removed paragraph that turns out to matter (behavior regresses under a different model or an edge branch) → restore it from version control; the deletion test samples, it does not prove. A hard constraint wrongly pruned as a no-op → restore immediately and mark it exempt. Pruning wars on a shared artifact → establish ownership rules before continuing to prune."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
  - "skill-pruning"
  - "no-ops"
  - "audit"
---

# The Deletion Test for No-Op Instructions

**Source:** [[skill-pruning-failure-modes-noop-deletion-test]]
**Form:** rule
**Extraction date:** 2026-07-13

A bloated skill or instruction file is usually a symptom, and one of the named causes is the **no-op**: a passage that appears to do something but does not change agent behavior. This rule is the cheap, named procedure for detecting and removing them — the deletion test — and it is especially load-bearing for agent-written artifacts, which produce no-ops systematically.

## Condition

Fires when auditing or authoring any context artifact — a skill file, an always-loaded instruction/memory file, an agent system prompt, or a shared reference doc — particularly when it has grown oversized or was written by an agent. Applies per paragraph / per instruction, not to the artifact as a whole.

## Action

**Required:** For each paragraph or instruction, run the deletion test — delete it (mentally, or actually) and ask whether agent behavior would change. If behavior would be unchanged because the model already does it from priors, the paragraph is a no-op; remove it.

**Forbidden:** Retaining prior-restating filler that the model already honors by default — e.g., "write a long detailed commit message," "write clear code," "be thorough." These read as instructions but change nothing.

**Exempt:** Hard constraints (security boundaries, gates, destructive-action guards) are *not* removed even if they appear to be no-ops. They often look inert precisely because they rarely bind — deleting them fails silently until the edge case arrives.

## Boundary

Enforced at two points: authoring review (before a passage is added or accepted) and audit (when an artifact is flagged oversized, this is the diagnosis step for the no-op share of the bloat). It sits alongside the two other pruning modes the source names — duplication (single source of truth for every part) and sediment (re-sort accreted contributions by branch; kill stale/irrelevant material) — but the deletion test is the specific procedure for the no-op mode.

## Enforcement

- **Cheap check (thought experiment):** delete the paragraph mentally and predict whether behavior changes. `(behavior_changes_if_deleted == false) AND (not a hard constraint)` → no-op → remove.
- **Empirical check (when the cheap check is uncertain):** run the artifact with and without the section as an A/B eval; if outputs are behaviorally equivalent, the section is a no-op. The thought experiment is the cheap approximation of this A/B.
- **Lint aid:** flag prior-restating phrases ("write clear code," "be thorough," "write a detailed commit message") as no-op candidates for human confirmation.
- **Agent-authored artifacts get a harder pass:** because agent-written skills systematically produce no-ops, apply the deletion test more aggressively to them.

## Rationale

The evidence that context bloat degrades behavior, and the budget reasons to stay small, are established elsewhere. What this rule supplies is the *audit taxonomy's* cheapest, only-named procedure for distinguishing instructions that earn their tokens from prior-restating filler. Crucially, the no-op test is orthogonal to "does this apply broadly?": a passage can be universally applicable yet still be a no-op (the model does it anyway), so the deletion test catches waste that a scope/global-truth check on additions does not. It is the removal-side complement to authorship-side minimality rules.

## Failure Modes

- **False no-ops.** Behavior that survives deletion under today's model may regress under a different model or in an edge branch; the deletion test samples, it does not prove. Restore from version control if a regression appears.
- **Over-pruning safety text.** Hard constraints can look like no-ops because they rarely bind — deleting them fails silently until the edge case arrives. The exemption above exists for exactly this.
- **Sediment courage without governance.** "Kill it dead" needs ownership rules on shared artifacts, or pruning wars replace sediment.

## Contract

### Preconditions
A context artifact (a skill file, an always-loaded instruction file, an agent system prompt, or equivalent) is being authored or audited — especially one written by an agent, which systematically produces no-ops. The reviewer can reason about the model's default behavior.

### Invariants
Every retained paragraph passes the deletion test: deleting it would change agent behavior. Instructions that merely restate model-default behavior are removed. Hard constraints are exempt — they may look like no-ops precisely because they rarely bind, and are retained regardless of the deletion-test result.

### Governance
Owner: the maintainer of the context artifact. The deletion test is applied per paragraph at authoring review and at audit. On shared artifacts, ownership and pruning rules must exist so "kill it dead" does not degenerate into a pruning war.

### Recovery
A removed paragraph that turns out to matter → restore it from version control; the test samples, it does not prove. A hard constraint wrongly pruned → restore immediately and mark it exempt. Pruning wars on a shared artifact → establish ownership rules before continuing.
