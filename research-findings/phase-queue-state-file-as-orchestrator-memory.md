---
name: "Phase-Queue State File as Orchestrator Memory"
summary: "A flat file stores all phase prompts and their completion status, serving as the orchestrator's sole memory. The orchestrator reads the state file, finds the next incomplete phase, dispatches it to a headless session, marks it complete on return, and loops. This externalizes orchestrator state entirely to the filesystem, keeping the orchestrator session context-free."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "gstack-gsd-superpowers-orchestrator-headless.md"
related_findings:
  - file: "orchestrator-headless-dispatch-context-isolation.md"
    rel: "enables"
  - file: "artifact-as-contract-pattern.md"
    rel: "extends"
  - file: "ralph-wiggum-execution-pattern.md"
    rel: "same-problem"
  - file: "phase-task-hierarchical-plan-decomposition.md"
    rel: "enables"
  - file: "append-only-run-log-as-working-memory.md"
    rel: "same-problem"
  - file: "spec-frontmatter-state-machine-unattended-dev-loop.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-07-13"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
---

# Phase-Queue State File as Orchestrator Memory

## What It Is

A design pattern where all orchestrator state is externalized into a single flat file (a "build queue" or "state file"). The file contains one entry per phase, each with: a phase prompt (the self-contained instruction for what that phase must accomplish), a completion status flag, and optionally a summary of the phase's output. The orchestrator's entire control loop is: (1) read the state file, (2) find the first incomplete phase, (3) dispatch it as a `claude -p` headless subprocess with the phase prompt, (4) receive the summary on completion, (5) mark the phase complete in the state file, (6) loop.

The key design insight: the state file IS the orchestrator's memory. The orchestrator session itself carries zero accumulated work context -- it only reads and writes the state file. This is what enables <10% context utilization after 100+ dispatched sessions in the demonstrated 16-phase build.

The state file format doubles as a progress dashboard: scanning it shows which phases are done, which are pending, and (if summaries are stored) what each completed phase produced.

## Why It Matters

Traditional orchestrators accumulate state in their context window -- they remember what Phase 1 did, carry that into Phase 2 planning, and progressively degrade as context fills. The state-file pattern breaks this by making the orchestrator stateless between dispatches. The orchestrator re-reads the state file on every iteration, meaning it is crash-recoverable: if the orchestrator session dies, a fresh session can read the same state file and continue from the last completed phase.

This matters for MetaSystem because it provides a concrete design for the artifact that sits between GSD's phase decomposition output and the headless dispatch loop. The state file is the handoff artifact between the planning phase (which generates the phases and their prompts) and the execution phase (which dispatches them).

## Why People Are Using It

Demonstrated in a live 16-phase overnight autonomous build (Eric Tech). The orchestrator completed all 16 phases across 100+ headless sessions while staying at <10% context utilization. The state file allowed the build to run unattended overnight -- each phase was self-contained in the queue, requiring no human intervention to advance.

The pattern also appears in GSD's ROADMAP.md (which tracks phase completion status) and in Ralph loop's plan.md (which tracks task completion per iteration). This finding focuses on the specific orchestrator-level state file for multi-session dispatch.

## Potential Improvements

- Include dependency declarations between phases in the state file so the orchestrator can detect when a phase depends on a prior phase that failed
- Store phase summaries in the state file so the orchestrator can include relevant prior-phase context in the next dispatch prompt
- Version the state file so rollback to a prior state is possible when a phase produces bad output
- Add a retry counter per phase to detect infinite-retry loops on stuck phases

## Potential Failure Modes

- **Phase prompts must be fully self-contained.** If a phase prompt implicitly depends on context from a prior phase's execution (not just its output artifacts), the headless session will lack that context and may produce wrong results.
- **No inter-phase dependency resolution.** A flat queue processes phases sequentially; if Phase 5 depends on Phase 3's output but Phase 3 failed, Phase 5 will execute anyway with stale or missing inputs unless dependency checks are built in.
- **State file corruption.** If the orchestrator crashes mid-write to the state file, the file may be left in an inconsistent state. Atomic writes or journaling would mitigate this.
- **Summary lossy compression.** When the orchestrator stores only a summary of each phase's output, important details may be lost -- the summary is a compression boundary and lossy by nature.
