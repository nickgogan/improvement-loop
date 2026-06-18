---
title: "Build Loop Skill — Autonomous Phase Driver"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "build-loop-skill-autonomous-phase-driver"
extraction_date: "2026-05-25"
last_change_session: 103
last_change_sl: "session-103-codifier-complete-extract-artifacts-write-phase"
identification_report: "2026-05-25-identification-report-session-95.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "multi-phase projects where each phase has a self-contained prompt and can be executed independently"
    - "overnight or unattended build workflows where a human wants to fire-and-forget a complete project execution"
    - "orchestration layers that need to dispatch sequential phases without accumulating context from prior phases"
  platform_coupling: "specific:claude-code"
  autonomy: "autonomous-only"
  stage: "build"
  reversibility: "low — each completed phase modifies the working directory; reversing requires git checkout to pre-loop state"
  auditability: "high when the state file records per-phase timestamps, exit statuses, and summary outputs; medium when only completion flags are retained"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "A phase-queue state file exists listing all phases with their prompts and completion status. Each phase's prompt is self-contained (readable cold by a fresh agent). The execution environment supports spawning headless claude -p invocations. The OS has a native scheduler (launchd, cron) or the skill is invoked interactively."
  invariants: "Each phase dispatches as a fresh headless session — no context inherited from prior phases or from the orchestrator. State is externalized to the phase-queue file. The loop terminates: either all phases complete or a fatal error halts execution. The orchestrator session accumulates only dispatch metadata (phase name, start/end time, exit status), not execution content."
  governance: "Owner: the caller who defines the phase-queue and per-phase prompts. The phase prompts are caller-owned — the loop skill dispatches but does not rewrite them. The state file is the primary audit artifact. No mid-loop human gate exists by default — add explicit checkpoint phases if human review is required between stages."
  recovery: "If a phase fails: log the failure, record partial state, surface the error in the state file, halt the loop (do not proceed to subsequent phases that may depend on the failed phase's output). If the loop is interrupted (machine reboot, session timeout): the state file shows which phases completed; re-invocation resumes from the first incomplete phase. If a phase produces bad output that poisons subsequent phases: the damage is bounded by phase-level isolation (each starts fresh); fix the bad phase's prompt and re-run from that point."
tags:
  - "extracted-artifact"
  - "skill"
  - "orchestration"
  - "automation"
---

# Build Loop Skill — Autonomous Phase Driver

**Source:** [[build-loop-skill-autonomous-phase-driver]]
**Source (additional):** [[orchestrator-headless-dispatch-context-isolation]]
**Form:** skill
**Extraction date:** 2026-05-25

A breadth-first orchestration skill that drives a multi-phase project to completion by dispatching each phase as an independent headless session. The skill reads a state file, identifies the next incomplete phase, dispatches it via `claude -p`, records the result, and loops until all phases are done.

## Inputs

- **Phase-queue state file:** A structured file (JSON, YAML, or markdown checklist) listing all phases with: phase name, prompt (or prompt-file path), completion status, and optional metadata (timestamps, summaries).
- **Per-phase prompts:** Self-contained prompts for each phase. Each prompt must be readable cold by an agent with no prior context — the fresh session will have only the prompt and the project's persistent context (CLAUDE.md, rules, MCP servers).
- **Execution environment:** Must support `claude -p` headless invocations (Claude Code CLI).

## Outputs

- **Updated state file:** Each completed phase is marked done with timestamp and summary.
- **Per-phase artifacts:** Whatever each phase produces in the working directory.
- **Orchestrator log:** Dispatch metadata (which phases ran, when, exit status) retained in the orchestrator session or written to a log file.

## Steps

1. **Read state file.** Load the phase-queue. Identify the first incomplete phase.
2. **Validate preconditions.** Verify the phase's prompt file exists and is non-empty. Verify the execution environment supports headless dispatch.
3. **Dispatch phase.** Spawn a headless `claude -p` process with the phase's prompt. The orchestrator waits for the subprocess to exit.
4. **Collect results.** Read the headless session's stdout/exit code. Extract a summary if the output format supports it.
5. **Update state file.** Mark the phase complete. Record timestamp, exit status, and summary.
6. **Check termination.** If all phases are complete, exit the loop successfully. If the phase failed, halt and surface the error (do not proceed to dependent phases).
7. **Loop.** Return to step 1 for the next incomplete phase.

## Context Isolation Mode

An optional hardened variant for workflows where context bleed between phases is a material risk — e.g., phases that modify shared configuration, multi-agent orchestrations where subagents have access to MCP servers, or overnight runs where no human is watching for unexpected cross-phase state propagation ([[orchestrator-headless-dispatch-context-isolation]]).

**Isolation techniques:**

1. **Per-subagent MCP scoping.** Each headless session is dispatched with only the MCP servers it specifically needs — not all servers available to the orchestrator. If phase 3 requires database read access, only that MCP server is passed to phase 3's invocation. The orchestrator retains access to the full server set for dispatch purposes; each headless session's scope is narrowed at dispatch time.

2. **Explicit context boundary enforcement.** Each phase prompt declares its own preconditions and the specific context it needs. No implicit inheritance from the orchestrator conversation. The state file is the only cross-phase communication channel; no environment variables, no shared in-memory state.

3. **Orchestrator window utilization ceiling.** The orchestrator session accumulates only dispatch metadata (phase name, start/end time, exit status, summary) — never execution content. After 100+ headless dispatches, the orchestrator should remain at or below 10% context utilization. If the orchestrator's utilization is growing toward 40%, the dispatch summaries are too verbose; trim them or write them to the state file instead of keeping them in the orchestrator session.

**When to use this mode:** Multi-phase runs with more than ~8 phases; workflows involving write-capable MCP servers; any unattended overnight execution where context bleed would not be caught until the next human review.

**When the default mode is sufficient:** Short phase queues (3-5 phases); read-only or idempotent phases; supervised runs where a human is monitoring output between phases.

## Failure Modes

- **Sequential bottleneck.** Independent phases wait for each other unnecessarily. Mitigation: add parallel dispatch for phases with no dependencies (requires dependency metadata in the state file).
- **No mid-run human gate.** Errors in early phases compound into later phases with no opportunity for correction. Mitigation: insert explicit checkpoint phases (e.g., "pause: await human review") in the phase queue.
- **Silent headless failures.** A headless session may exit with code 0 but produce garbage output. Mitigation: add pass/fail criteria per phase (output schema validation, test execution) beyond exit code.
- **Cost accumulation.** Each headless session is a fresh API call. A 16-phase project with retries can consume significant resources without intermediate human review. Mitigation: budget caps or phase-count limits with human approval for continuation.
