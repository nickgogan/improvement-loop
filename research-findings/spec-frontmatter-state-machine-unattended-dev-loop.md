---
name: "Spec-Frontmatter State Machine for Unattended Dev Loops"
summary: |-
  Plain English: run an unattended dev loop by putting the state machine in the work
  artifact itself — the story spec's frontmatter `status:` field is the transition
  variable any orchestrator can poll, and when the worker gets stuck it HALTs by
  writing a terminal status plus the blocking condition into the artifact instead of
  asking a question no one will answer. BMAD v6.10.0's bmad-dev-auto runs one iteration
  entirely off spec frontmatter; the bmad-loop orchestrator (a separately-installed
  module) polls `status:` and dispatches iterations — a file-mediated protocol across
  separately-installed components. Supporting mechanics: an append-only review-triage
  log with loopback tracking; an end-of-run commit so the next iteration starts with a
  clean worktree; `final_revision` recorded at exit as "the only link back from an
  out-of-tree spec to its in-tree commits"; and a synchronous-subagent mandate —
  review layers are "several blocking calls awaited together in one turn — never
  backgrounded," because an unattended run has no event loop to resume a yielded turn.
implementation_notes: null
category: "Agentic Systems"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "loop-node-anatomy-schema-enforced-ralph-primitive.md"
    rel: "same-problem"
  - file: "phase-queue-state-file-as-orchestrator-memory.md"
    rel: "same-problem"
  - file: "workflow-state-vs-conversation-state.md"
    rel: "extends"
  - file: "incremental-one-feature-per-session-pattern.md"
    rel: "same-problem"
  - file: "heartbeat-execution-model.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "agentic-systems"
  - "loop-engineering"
  - "unattended-autonomy"
---

# Spec-Frontmatter State Machine for Unattended Dev Loops

## What It Is

An unattended-autonomy design where the coordination protocol lives entirely in files:

1. **State in the artifact.** The story spec's frontmatter `status:` is the state
   machine; the worker (bmad-dev-auto) runs one iteration and writes the resulting
   status; the orchestrator (bmad-loop, installed from a separate module repo) polls it
   and dispatches the next iteration. Neither component imports the other — the spec
   file IS the interface, including `## Auto Run Result` and `## Review Triage Log`
   sections.
2. **HALT instead of questions.** When blocked, the worker writes a terminal status
   plus the blocking condition into the artifact — the unattended substitute for
   asking the user.
3. **Loop hygiene.** Append-only review-triage log with loopback tracking; end-of-run
   commit so each iteration starts on a clean worktree; `final_revision` written at
   exit as the only link from the out-of-tree spec to its in-tree commits.
4. **Synchronous subagents only.** Parallel review layers are dispatched as blocking
   calls awaited together in one turn, never backgrounded — an unattended run has no
   event loop to resume a yielded turn.

## Why It Matters

Unattended loops need three things attended sessions get for free: a resumable
authority on "where are we" (the frontmatter status — pollable by *any* orchestrator,
which is what lets the loop and worker ship as separate modules), a protocol for being
stuck that doesn't deadlock (HALT-with-reason), and provenance from plan to code
(`final_revision`). This is the file-based counterpart to schema-enforced loop nodes
(Archon): Archon puts the loop contract in the workflow engine's schema; BMAD puts it
in the work artifact, trading enforcement strength for zero shared infrastructure.

## Why People Are Using It

The dev-auto/bmad-loop pair is BMAD's shipped answer to full-autonomy implementation;
its constraints (synchronous mandate, HALT protocol) are corrections from real
unattended runs. Source: Observed in
[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.10.0 — see
[[bmad-method-analysis]] for structural details.

## Potential Alternatives

- **Engine-enforced loop schemas** (Archon `loop:` nodes) — stronger guarantees
  (max_iterations required, deterministic exit checks) but both sides must live inside
  one engine.
- **Queue/state-file orchestration** (phase queues) — state lives beside the work, not
  in it; loses the any-orchestrator-can-poll property.
- **Long-running single session** — no protocol needed until compaction or a crash
  erases the state that lived in conversation.

## Potential Improvements

- A hard iteration budget in the artifact itself (Archon requires `max_iterations`;
  the spec-frontmatter design leaves runaway bounds to the orchestrator).
- Status-vocabulary convention across frameworks so tooling can read any project's
  loop state.

## Potential Failure Modes

- **Frontmatter races** — two writers (worker finishing, orchestrator retrying) on one
  file with no locking; the end-of-run commit discipline narrows but doesn't close it.
- **HALT dead-ends** — terminal statuses accumulate unnoticed without a sweep that
  routes blocked specs back to a human.
- **Status/content drift** — the status field and the artifact body can disagree
  (contrast the memlog design, which rejects status fields for exactly this reason).
