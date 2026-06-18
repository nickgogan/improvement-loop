---
name: Convergence Loop with Dual Clean-Poll Exit
summary: "Multi-agent convergence requires two consecutive clean polls 60 seconds apart before accepting that all agents are done — accounts for delayed bot responses and asynchronous CI checks. A reliability pattern for determining when parallel automated work has genuinely completed."
implementation_notes: null
category: Governance
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - "S3 (Claude Code Build)"
  - General
adopted_in: []
sources: []
proposals: []
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
related_findings:
  - file: iterative-refinement-loop-with-quality-gate.md
    rel: same-problem
pipeline_status: raw
consumed_by: []
---

# Convergence Loop with Dual Clean-Poll Exit

## What It Is

A termination condition for multi-agent coordination loops: rather than accepting a single "all clear" signal, the system requires two consecutive clean polls separated by a 60-second interval before declaring convergence. The `/pr-polish` skill alternates review/address rounds and includes a MAX_ROUNDS safety valve (10 rounds). This pattern accounts for delayed bot responses, asynchronous CI pipeline results, and race conditions where one agent's output triggers another agent's action after the initial poll returns clean.

## Why It Matters

In systems with multiple automated agents (CI bots, review bots, linters, formatters), a single poll showing "no issues" is unreliable because asynchronous processes may still be running. Declaring convergence too early leads to merging PRs with pending review comments, failing CI that has not yet reported, or unaddressed formatting issues from a bot that triggers after the merge check. The dual-poll pattern provides a cheap, stateless reliability improvement.

## Why People Are Using It

Observed in [AutoGPT](https://github.com/significant-gravitas/autogpt) v0.5.0 — see [[autogpt-analysis]] for structural details. The `/pr-polish` skill uses this pattern with its review/address alternation loop, and the orchestrator's verify-complete script applies similar logic when checking agent fleet status — requiring agents to remain in a "done" state across multiple polls before accepting completion.

## Potential Alternatives

Event-driven completion via webhooks from all subsystems (eliminates polling but requires all systems to emit completion events). A dependency graph that tracks expected outputs and blocks until all are received. Exponential backoff polling that increases interval until a timeout, then accepts the last state.

## Potential Improvements

Make the poll interval and required consecutive count configurable per workflow (some CI pipelines are faster than others). Add a "last activity" timestamp check — if no new activity has occurred in the system for the interval period, one clean poll should suffice. Track which specific subsystems are known to be slow and weight the interval accordingly rather than using a fixed 60 seconds for all cases.

## Potential Failure Modes

The fixed 60-second interval is a magic number — too short for slow CI pipelines (30+ minute builds), too long for fast-feedback loops where it adds unnecessary latency. The MAX_ROUNDS safety valve can terminate prematurely if agents are making genuine progress but oscillating between review findings. A consistently flaky check (e.g., an intermittent CI failure) will prevent convergence entirely, requiring manual intervention to break the loop.
