---
name: Loop Contract — Goal/Boundary/SOP + State + Log as One File Per Automation, Plus Evolve Sessions
summary: |-
  Plain English: every autonomous loop/automation gets ONE living markdown file that
  is simultaneously its constitution and its memory — a "contract" section (goal,
  boundaries on what it can do unsupervised vs. what needs human escalation, and an
  SOP), a deliberately small "state" section (current hypothesis, open backlog, items
  shipped but needing follow-up), and an append-only "log" of what happened each run.
  Production-run at AI Jason's company (Super Divine) across an engineering loop
  (react-doctor CLI scans), a CRM lifecycle loop, a documentation-drift loop, and a
  support-inbox triage loop, all for months. A second cadence rides on top: every 5-10
  runs, a dedicated "evolve session" hands the agent its own past config, state/log
  history, and raw conversation transcripts, and asks it to propose changes to its own
  contract, prune stale state, or convert a repetitive SOP step into a script.
implementation_notes: |-
  This is loop-level (per-automation) self-tuning, distinct in altitude from both the
  engine's system-wide self-evolving-loop-pattern (periodic KB research scan) and the
  self-improve skill (IB-176's engine-wide lesson store + scan/promote pipeline over
  operations/self/). Before adopting: decide what unit in the engine counts as a "loop"
  needing its own contract file (candidates: research-loop, watch-blogs,
  watch-upstream — the same gap ecosystem-monitoring-meta-loop.md already flags), where
  the file lives, and whether "evolve session" duplicates or complements
  self-improve's existing scan mode rather than adding a second, uncoordinated
  self-modification path.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (loop/automation portfolio governance)
- General
adopted_in: []
sources:
- i-was-building-loops-wrong.md
related_findings:
- file: append-only-run-log-as-working-memory.md
  rel: extends
- file: self-improving-skill-lessons-log.md
  rel: same-problem
- file: self-evolving-loop-pattern.md
  rel: same-problem
- file: loop-node-anatomy-schema-enforced-ralph-primitive.md
  rel: extends
- file: ecosystem-monitoring-meta-loop.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-18'
last_updated: '2026-07-18'
pipeline_status: synthesized
consumed_by:
- autonomous-scheduled-agent-operation.md
tags:
- orchestration
- loop-engineering
- loop-contract
- self-improvement
- agentic-systems
---

# Loop Contract — Goal/Boundary/SOP + State + Log as One File Per Automation, Plus Evolve Sessions

## What It Is

Three governing pieces, packaged as one markdown file per loop/automation:

1. **Contract** — the loop's constitution. Three sub-parts: **goal** (what does winning look like, is there even a finish line), **boundaries** (what the agent may do unsupervised vs. what must escalate to a human), and **SOP** (any specific workflow or principle the agent must follow every run). A concrete boundary example from the doc-maintainer loop: an explicit rule reading "never rewrite accurate docs to look busy" — added because the default agent failure mode is bias toward action, editing something even when nothing needs to change.
2. **State** — a durable but deliberately *small* snapshot: current hypothesis, open backlog items, things shipped but awaiting follow-up. Kept small on purpose — this is working memory, not history.
3. **Log** — an append-only, run-by-run record of what happened. Without it, "every morning the loop just rediscovers the same noise, wastes tokens chasing things already tried."

For small loops, contract + state + log live in one file; larger ones may reference additional artifacts from that file. Four production examples at the source's company (Super Divine): a react-doctor CLI-scan loop (daily scan, auto-fix, sub-agent-per-fix in isolated worktrees, verification before merge), a CRM lifecycle loop (daily user segmentation → auto-outreach or draft-for-approval by segment risk), a documentation-drift loop (diff the last 24h of shipped work against README/setup guide/runbooks, verify each apparent drift before touching anything), and a support-inbox triage loop.

**Evolve sessions.** Every 5-10 runs, a dedicated session hands the agent the loop's own existing configuration, past state/log history, and the raw conversation transcripts from recent runs, and has it propose improvements: sharpen the contract's specs/SOP, prune outdated state, or promote a repetitive manual SOP step into a script (their support-inbox loop got its programmatic pre-check trigger — see the companion trigger-taxonomy finding — from exactly this kind of evolve session). This is scoped to ONE automation revising itself, not a system-wide research cadence.

The source's own internal tool (referred to as "Loopery" in the video, later open-sourced) operationalizes this: a dashboard per loop tracking shipped PRs/score trends, a blue-dot indicator marking when an evolve session is available, one-click copyable prompt templates (doc-maintainer, react-doctor-style scans, tech-debt cleanup) that scaffold a new loop's contract file directly in the target repo, and centralized tracking of contracts/state/logs/triggers across the whole loop portfolio.

## Why It Matters

Ad-hoc "just prompt it in a loop" setups have no single place holding what the loop is *for*, what it's allowed to do alone, what it currently believes, and what it has already tried — so each run either re-relitigates settled questions or silently drifts from its original purpose. Packaging contract + state + log as one file makes the loop legible to a human skimming it and durable across runs without a database. The evolve-session cadence answers the standing objection to any fixed automation ("it'll go stale") by scheduling deliberate self-revision instead of leaving improvement to chance or to a human noticing decay.

## Why People Are Using It

Production-run at Super Divine (the source's company) for "the past months" across engineering, CRM/lifecycle, documentation, and support-triage loops — explicitly framed as "none of this is a demo." The pattern generalizes past engineering tasks (documentation maintenance, customer messaging) because the three-part anatomy doesn't assume code.

## Potential Alternatives

- **Single unstructured scratch file** — lower setup cost, but conflates constitution (rarely changes) with state (changes often) with log (never changes, only grows), making all three harder to reason about independently.
- **Append-only-log-only** (no contract, no state) — see `append-only-run-log-as-working-memory.md`; sufficient for pure working-memory/resume use cases but has no mechanism for the loop's own goal/boundary to survive if a human forgets why it was built that way.
- **Database-backed loop registry** — stronger querying, loses the git-diffable, human-skimmable property the source treats as central.

## Potential Improvements

- A machine-checkable schema for the contract/state/log split (the KB's Archon loop-node schema shows what schema-enforcement of the adjacent *mechanical* iteration anatomy looks like — see `loop-node-anatomy-schema-enforced-ralph-primitive.md`) would catch malformed contracts before a run starts.
- Convention-based portfolio discovery (glob for a naming pattern) rather than a maintained registry — the same zero-maintenance move `ecosystem-monitoring-meta-loop.md` proposes.
- Explicit versioning on the contract section specifically, since state and log already version themselves by construction (state is overwritten, log is append-only) but contract edits during an evolve session have no diff trail beyond git.

## Potential Failure Modes

- Evolve sessions that see only the loop's own history can overfit to recent noise (e.g., prune a state item that's actually still relevant, just not recently touched).
- Boundary rules are only as good as what's been thought to write down — the "don't rewrite accurate docs" rule was a reactive fix to an observed failure, not a design that anticipated it; new automations should expect a similar first-failure-then-patch cycle.
- No described mechanism for cross-loop conflicts (two loops editing overlapping surfaces) — each loop's contract is self-contained, so nothing catches interference between loops at the contract level.
- If the raw conversation history fed to an evolve session is large, that session itself can be one of the more expensive runs in the loop's lifecycle — worth budgeting separately from regular runs.
