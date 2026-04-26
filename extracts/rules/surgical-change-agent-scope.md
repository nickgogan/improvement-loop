---
title: "Surgical Change Constraint — Agent Scope Boundary"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "surgical-change-constraint-agent-scope"
extraction_date: "2026-04-20"
last_change_session: 44
last_change_sl: "session-44-codifier-extraction-run"
identification_report: "2026-04-20-identification-report.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic coding systems executing bounded tasks on existing codebases"
    - "agent harness and system prompt configurations governing edit behavior"
    - "pre-commit or diff-verification hooks that validate task scope compliance"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — out-of-scope edits that have been committed require explicit revert and diff review; pre-commit enforcement makes this trivial if caught early"
  auditability: "high — diff-scope check is fully deterministic; every changed hunk is verifiable against declared task scope"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Karpathy Skills CLAUDE.md encodes this as Principle 3; not yet adopted in this workspace's CLAUDE.md or hook configuration."
contract:
  preconditions: "Task scope is declared before execution (target files, line ranges, or semantic scope). Diff tooling is available to compare pre-task and post-task state. Agent has a means to surface the intended diff before commit."
  invariants: "Agent changes are confined to the declared task scope. Edits outside declared scope are either reverted or flagged as scope violations. The declared scope is immutable for the duration of the task unless a new scope is negotiated."
  governance: "Owner: Agent harness / prompt layer. Rule is encoded in CLAUDE.md or system prompt. Scope-expansion requires explicit user authorization during the task. Rule does not override explicit user instructions to refactor adjacent code."
  recovery: "If the agent touches out-of-scope code: revert those edits before commit and surface them as a scope-violation note. If scope is ambiguous: pause and negotiate scope with the user before making any changes."
tags:
  - "extracted-artifact"
  - "rule"
---

# Surgical Change Constraint — Agent Scope Boundary

**Source:** [[surgical-change-constraint-agent-scope]]
**Form:** rule
**Extraction date:** 2026-04-20

## Condition

An agent is executing a task with a declared scope (specific files, line ranges, or a bounded semantic change). The agent has the ability to modify code outside that declared scope.

## Action

**Forbidden:** Modifying any code outside the declared task scope — including comments, whitespace, import ordering, formatting, unrelated function bodies, or structural reorganization — regardless of whether the agent considers the change an improvement.

**Required:** Confine all edits to the declared scope. If the agent concludes that adjacent code must change for the task to succeed, pause and negotiate a scope expansion with the user before editing.

## Boundary

Enforced at the task execution boundary — specifically, at the diff-produced-by-the-task. Applies from the moment a scope is declared (explicit instruction, task file, or plan) until the task is marked complete.

## Enforcement

- **Mechanism:** Diff-scope check. Compute the diff the agent produced for the task. For each changed hunk, verify the file path and line range fall within the declared scope.
- **Check (deterministic):** `every changed_hunk ∈ declared_scope`. Any hunk outside scope is a violation.
- **Violation response:** Revert out-of-scope hunks before committing the task. Surface the attempted changes as a scope-violation note for the user. Do not silently discard them — they may indicate a genuinely missed dependency.
- **Cannot be checked by the agent alone:** The check must be performed by a layer the agent cannot bypass (pre-commit hook, harness-level diff verifier, or human review at commit time).

## Rationale

Unrequested changes create a "productivity theater" failure mode: the agent looks helpful by producing more lines than asked, but each extra edit introduces unreviewed drift. Karpathy documents this as one of the most common agent failure categories — agents "change or remove comments in code that they don't like or don't sufficiently understand, even if it is orthogonal to the task at hand."

Token cost is the smaller problem. The larger problem is trust erosion: when an agent changes 10 things while asked to change 1, the user must diff all 10 to verify correctness. This compounds across sessions into diff sprawl — a codebase that silently diverges from its intended architecture because no single review caught all the uninvited changes.

The surgical constraint is the complement to the simplicity constraint: simplicity governs how much *new* code is written; surgical governs how much *existing* code is touched.

## Failure Modes

- **Ambiguous scope.** If the task description does not fix the scope, the rule cannot be mechanically checked. Mitigation: require an explicit scope declaration step before execution.
- **Genuine refactor need.** Some tasks legitimately require adjacent refactor. The rule does not forbid this — it forbids doing it silently. The agent must surface the need and get authorization.
- **Invisible changes.** Whitespace normalization, dict key reordering, or import reshuffling can pass surgical inspection while polluting diffs. Mitigation: run the diff check against a whitespace-insensitive, structure-aware differ where possible.
- **Scope too narrow.** Over-strict scope prevents necessary fix-up and forces repeated scope negotiations. Mitigation: calibrate scope granularity to task complexity — file-level for typical tasks, line-level only when the concern is surgical minimality.

## Contract

### Preconditions
Task scope is declared before execution (target files, line ranges, or semantic scope). Diff tooling is available to compare pre-task and post-task state. Agent has a means to surface the intended diff before commit.

### Invariants
Agent changes are confined to the declared task scope. Edits outside declared scope are either reverted or flagged as scope violations. The declared scope is immutable for the duration of the task unless a new scope is negotiated.

### Governance
Owner: Agent harness / prompt layer. Rule is encoded in CLAUDE.md or system prompt. Scope-expansion requires explicit user authorization during the task. Rule does not override explicit user instructions to refactor adjacent code.

### Recovery
If the agent touches out-of-scope code: revert those edits before commit and surface them as a scope-violation note. If scope is ambiguous: pause and negotiate scope with the user before making any changes.
