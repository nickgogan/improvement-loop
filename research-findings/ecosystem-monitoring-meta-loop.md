---
name: "Ecosystem Monitoring Meta-Loop (the Loop That Manages Loops)"
summary: |-
  A meta-loop that manages a growing loop portfolio with three features: a composability
  scan that finds logic repeated across loops and proposes extracting it into a shared
  skill; a health check built on a shared write-run-log utility skill so every loop logs
  results to one folder (making failing or useless loops visible and killable — token
  savings); and convention-based discovery — every loop follows a `*-loop` naming
  convention, and each run globs for that pattern, so new loops are picked up
  automatically with zero registry maintenance.
implementation_notes: |-
  The engine runs a growing loop portfolio (research-loop, watch-blogs, watch-upstream,
  audits, scheduled routines) with no surface that monitors the portfolio's run health —
  this is a concrete recipe for that gap. The two adoptable mechanics: a shared run-log
  skill all loops call (one place to update, one place to read health), and
  convention-based discovery (compatible with the no-hardcoded-counts rule — the loop
  inventory is computed per run, never maintained). Design required: what counts as a
  "loop" in the engine, log schema, and where run logs live in operations/.
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "IL (loop portfolio operations)"
  - "General"
adopted_in: []
sources:
  - "8-claude-loops-to-build-10x-faster.md"
related_findings:
  - file: "monitoring-agent-failure-detection-autonomous-repair.md"
    rel: "same-problem"
  - file: "shared-context-folder-as-cross-skill-update-multiplier.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

A "loop that manages your other loops." Every loop added to a system adds operational
debt; this meta-loop pays it down with three mechanisms:

1. **Composability scan.** As loops accumulate, the same logic gets written twice (two
   loops both fetching Slack data). The meta-loop scans the loop library for repeated
   logic and proposes pulling it into a single composable skill every loop calls —
   avoiding the whack-a-mole trap where a bug fixed in one loop reappears in another.
2. **Health check via a shared run-log skill.** A `write-run-log` utility skill writes
   every loop's results to one folder. Updating that one skill updates logging across
   every loop. Cross-referencing the logs shows what is and isn't running successfully —
   the practitioner's claim is that most loop operators are silently burning tokens on
   broken or useless loops, and this makes them visible enough to turn off.
3. **Convention-based discovery.** Every loop is named `<name>-loop`. On each run the
   meta-loop scans skills for that convention, so any new loop is automatically included.
   There is no registry file to maintain — the monitoring layer self-corrects.

## Why It Matters for Us

The engine's loop portfolio is growing (research-loop, watch-blogs, watch-upstream,
periodic audits, scheduled routines) and nothing monitors its run health — a failure in a
scheduled scan is only noticed when someone happens to look. The zero-maintenance registry
mechanic is directly compatible with the engine's no-hardcoded-counts rule: the inventory
is derived by scan, never written down. The shared run-log skill is the same
update-multiplier argument the KB already holds for shared context folders, applied to
observability.

## Why People Are Using It

Practitioner-demonstrated (Marchese, 2026-07) as the maintenance answer to loop sprawl;
he frames it as net token-saving because it surfaces loops worth killing. Single-source
so far.

## Potential Improvements

- Log-schema standardization so health checks are queryable rather than prose-read.
- Alerting: pipe run-log anomalies to a notification channel instead of waiting for the
  next meta-loop run.
- Extending the composability scan with recurrence thresholds (only propose extraction on
  2-3+ repetitions — aligns with the engine's abstractions-earn-their-keep rule).

## Potential Failure Modes

- The meta-loop is itself a loop: it can fail silently, and nothing monitors the monitor.
- Naming-convention discovery misses loops that don't follow the convention (silent
  coverage gaps) and false-positives on non-loop skills that happen to match.
- Composability suggestions can drive premature abstraction if applied on first
  duplication rather than clear recurrence.
