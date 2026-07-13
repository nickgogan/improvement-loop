---
name: "No Autonomous Lifecycle Mutation Across Process Boundaries"
summary: |-
  Plain English: a process that cannot tell "this work is running somewhere else" from
  "this work is orphaned" must not mark that work failed or cancelled on a staleness
  guess — it should surface the ambiguity to a human with a one-click resolution
  action. Archon v0.5.0 codifies this as a named engineering principle in its master
  context (with cited precedent: issue #1216, where a staleness heuristic wrongly
  killed live runs), paired with UI affordances that show orphan-*looking* runs with
  explicit user actions instead of auto-cancelling them. Generalizes to any
  multi-entry-point agent system with shared run state: epistemic uncertainty about
  another process's liveness is a hard stop for destructive state transitions, and
  the correct fallback is ambiguity-surfacing, not conservative auto-mutation.
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "advisory-only-for-persistent-mutations.md"
    rel: "same-problem"
  - file: "agent-clarification-over-assumption-pattern.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "governance"
  - "run-lifecycle"
  - "autonomy-boundaries"
  - "archon"
---

# No Autonomous Lifecycle Mutation Across Process Boundaries

## What It Is

A codified engineering principle in Archon v0.5.0's master context (CLAUDE.md): **a process that cannot distinguish "actively running elsewhere" from "orphaned" must not mark that work failed or cancelled based on a staleness heuristic.** When liveness is ambiguous — a run last heartbeated N minutes ago, a session whose owning process may or may not exist — the system surfaces the ambiguity to the user with a one-click resolution action (cancel / keep waiting) instead of auto-mutating the lifecycle state.

The principle is written with cited precedent (issue #1216) where a staleness-based cleanup wrongly transitioned live work to failed. It belongs to the same family as Archon's broader "ambiguity-surfacing over auto-mutation" guardrail posture.

## Why It Matters

Multi-entry-point agent systems (CLI + web + chat adapters + detached background runs, all sharing run state in a database) constantly face the orphan-detection problem, and the reflexive fix — a staleness timeout that marks stale-looking runs failed — is a destructive write made under epistemic uncertainty. The principle names the exact boundary: *heuristics may inform display, never destructive lifecycle transitions across a process boundary you cannot observe.* The failure mode it prevents is nasty precisely because it is silent: a healthy long-running loop gets cancelled by a janitor process, and the user sees a failure that never happened. The generalization for agent-system design: liveness uncertainty is an intent/preference question (does the user want this run kept?), not a resolvable gap, so it routes to the human — the run-lifecycle instance of clarification-over-assumption.

## Why People Are Using It

Observed in [Archon](https://github.com/coleam00/archon) v0.5.0 — see [[archon-analysis]] for structural details. Codified in CLAUDE.md as a named principle with issue precedent after a real incident (#1216), and reflected in the run console UI, which flags orphan-looking runs with explicit user actions rather than auto-cancelling them.

## Potential Alternatives

Lease/heartbeat protocols with authoritative ownership (a process that holds the lease *can* safely mutate — turns the guess into knowledge, at the cost of protocol machinery). TTL-based auto-cleanup with generous margins (still guesses, just less often). Durable-execution engines where liveness is the platform's problem.

## Potential Improvements

Pairing the principle with a positive mechanism (heartbeat/lease) so the "cannot distinguish" precondition arises rarely. Auto-expiring the surfaced ambiguity into a *non-destructive* parked state after prolonged user silence.

## Potential Failure Modes

Ambiguity-surfacing at scale becomes alert fatigue — hundreds of orphan-looking runs each demanding a click. Truly orphaned resource-holding runs (worktrees, ports, provider sessions) leak until a human acts. The principle protects lifecycle *state*; it does not by itself protect the *resources* the zombie state pins.
