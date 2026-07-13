---
title: "War-Game Plan Scaffold"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "war-game-plan-format-for-executor-handoff"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "writing-agent-specifications.harvest-queue"
identification_report: "writing-agent-specifications.harvest-queue.md::war-game-plan-format-for-executor-handoff::template::war-game-plan-scaffold"
deployed: false
deployed_to: null
context:
  applies_to:
    - "plan handoffs where a stronger (or more expensive) planning model authors a brief that a cheaper executor model will run unsupervised"
    - "missions likely to deviate from the happy path, where improvisation by the executor is the expensive failure mode"
    - "capturing a frontier model's judgment as a durable, reusable execution artifact before access to that model becomes scarce or costly"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — a plan-document format; reverting to linear plans requires no migration"
  auditability: "high on structure (required per-move fields, ledger, and abort section are mechanically checkable); medium on substance (branch quality is only validated by execution traces)"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Demonstrated end-to-end by one practitioner with a 10-project batch fanned out to parallel agents (tasks/ + wargames/ folders, success-criteria file, ledger file; bulk-draft all war-games before polishing any). No quantified experiment."
contract:
  preconditions: "A mission brief exists. The authoring model is instructed to war-game, not execute. The executor model/agent is named so the war-game can be tailored to its documented behavior. The human has set a war-game depth cap (how many orders of consequences to simulate)."
  invariants: "Every move states its expected observation on success AND on failure, its most-likely failure with observable signals, and the countermove. Every fork carries an explicit trigger condition ('if you observe X, take route A'). Assumptions the war-gamer could not resolve are entered in the blocked-variables ledger, never silently assumed. The document terminates with explicit abort conditions. The war-gamer never executes the mission."
  governance: "The human decides war-game depth and fills the blocked-variables ledger before handoff; execution must not start with unfilled ledger entries. The plan author (strong model) owns the decision tree; the executor follows triggers and countermoves, escalating on abort conditions rather than improvising. Stale war-games are re-drafted when the underlying system changes."
  recovery: "Executor observes something no branch anticipated: stop at the nearest abort condition or escalate to the human/advisor rather than improvising. Ledger variable turns out wrong mid-run: halt, correct the ledger, resume from the last valid move. Branch explosion during authoring: cut depth to the human-set cap and record un-simulated junctures as abort conditions. War-game drifted from the current codebase: re-run the war-gaming prompt against current state before executing."
tags:
  - "extracted-artifact"
  - "template"
  - "plan-contracts"
  - "intent-engineering"
  - "planner-executor"
---

# War-Game Plan Scaffold

**Source:** [[war-game-plan-format-for-executor-handoff]]
**Form:** template
**Extraction date:** 2026-07-13

A plan-artifact format that replaces linear plans with simulated execution. A strong model fights the mission on paper move by move — expected observations, most-likely failures with their signals, countermoves, trigger-conditioned forks — so a cheaper executor runs a pre-simulated decision tree instead of improvising when reality deviates. Unresolvable assumptions go to a blocked-variables ledger the human fills; the document ends with abort conditions. The structure mirrors the agentic loop itself: action, reaction, counteraction.

## Variables

| Variable | Type | Description |
|----------|------|-------------|
| `{{MISSION}}` | string | What the executor is to accomplish, with success criteria. |
| `{{EXECUTOR_MODEL}}` | string | The named model/agent that will run the brief. The war-game is tailored to its documented behavior. |
| `{{DEPTH}}` | integer/policy | Human-set cap on how deep to simulate (second/third/fourth-order consequences). |
| `{{MOVE_N}}` | block | One move of the mission (see per-move fields in the body). |
| `{{FORK_TRIGGER}}` | condition | Observable condition that selects a route ("if you observe X, take route A"). |
| `{{LEDGER_ENTRY}}` | (variable, why blocked, value) | An assumption recon could not resolve; the human supplies the value before execution. |
| `{{ABORT_CONDITION}}` | condition | An error or missing access that must stop execution entirely. |

## Body

### Authoring prompt (given to the strong model)

```text
War-game order. You are not executing this mission, you are purely war-gaming it.
A cheaper executor model will run the brief below: {{EXECUTOR_MODEL}}. Consult that
model's documented behavior and tailor the brief to it.

Fight the mission on paper, move by move, to depth {{DEPTH}}. For every move state:
what you expect to observe if it worked; what you expect to observe if it didn't;
the most likely failure and its signals; the countermove. Give every fork an explicit
trigger condition. Any assumption you cannot resolve goes to a blocked-variables
ledger as a placeholder the human must fill. End the document with abort conditions —
errors or missing access that should stop execution entirely.

Mission: {{MISSION}}
```

### Plan document (the war-game the executor receives)

```markdown
# War-Game: {{MISSION}}

**Executor:** {{EXECUTOR_MODEL}}
**Success criteria:** <verifiable end-state>

## Moves

### Move 1: <action>
- **If it worked, you will observe:** <expected observation>
- **If it didn't, you will observe:** <expected observation>
- **Most likely failure:** <failure> — **signals:** <observable signals>
- **Countermove:** <what to do instead>

### Fork after Move 1
- **Trigger:** {{FORK_TRIGGER}} → take Route A (Moves 2a…)
- **Otherwise** → take Route B (Moves 2b…)

<!-- Repeat per move/fork to depth {{DEPTH}}. -->

## Blocked-Variables Ledger  <!-- human fills before execution -->
| Variable | Why blocked | Value (human) |
|---|---|---|
| {{LEDGER_ENTRY}} | | |

## Abort Conditions
- {{ABORT_CONDITION}}
- <…>  <!-- stop entirely; do not improvise past these -->
```

## Usage

Use when handing a mission from a strong planning model to a cheaper executor. Author with the prompt above; the human then (1) decides how deep the war-game goes and (2) fills every ledger entry — execution must not start with blanks. For batches, draft all war-games first, then loop-polish ("draft all 10 before polishing any"); a working folder layout is `tasks/` + `wargames/` plus a success-criteria file and the ledger file. Re-draft when the underlying system changes; optionally feed observed execution traces back to prune branches that never fire.

## Variation Axis

- **Depth** — deeper simulation covers more deviations but risks branch explosion and boilerplate burying the decision-relevant forks; the human's depth cap is the dial.
- **Executor tailoring** — how much the brief adapts to the named executor's documented strengths/failure modes; only as good as that documentation.
- **Fallback pairing** — standalone war-game (cheapest) vs. war-game plus a live advisor fallback for deviations the tree didn't anticipate (dearer, more resilient).

## Contract

### Preconditions
A mission brief exists. The authoring model is instructed to war-game, not execute. The executor model/agent is named so the war-game can be tailored to its documented behavior. The human has set a war-game depth cap (how many orders of consequences to simulate).

### Invariants
Every move states its expected observation on success AND on failure, its most-likely failure with observable signals, and the countermove. Every fork carries an explicit trigger condition ("if you observe X, take route A"). Assumptions the war-gamer could not resolve are entered in the blocked-variables ledger, never silently assumed. The document terminates with explicit abort conditions. The war-gamer never executes the mission.

### Governance
The human decides war-game depth and fills the blocked-variables ledger before handoff; execution must not start with unfilled ledger entries. The plan author (strong model) owns the decision tree; the executor follows triggers and countermoves, escalating on abort conditions rather than improvising. Stale war-games are re-drafted when the underlying system changes.

### Recovery
Executor observes something no branch anticipated: stop at the nearest abort condition or escalate to the human/advisor rather than improvising. Ledger variable turns out wrong mid-run: halt, correct the ledger, resume from the last valid move. Branch explosion during authoring: cut depth to the human-set cap and record un-simulated junctures as abort conditions. War-game drifted from the current codebase: re-run the war-gaming prompt against current state before executing.
