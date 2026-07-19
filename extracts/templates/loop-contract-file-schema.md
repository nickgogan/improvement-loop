---
title: "Loop Contract File Schema"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "loop-contract-anatomy-and-evolve-session-cadence"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "autonomous-scheduled-agent-operation.harvest-queue"
identification_report: "autonomous-scheduled-agent-operation.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams operating an autonomous loop or recurring automation that needs a single living file holding what it is for, what it may do alone, what it currently believes, and what it has already tried"
    - "anyone running a portfolio of long-lived automations (engineering scans, CRM lifecycle jobs, doc-drift checks, inbox triage) who wants each one legible to a human skim and durable across runs without a database"
    - "loop owners maintaining an automation over its operating lifetime, including the periodic 'evolve session' where the automation proposes revisions to its own contract"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "low — the filled file IS the automation's constitution and memory; individual edits are trivially reversible via git, but losing or corrupting the file loses the loop's goal/boundary rationale and its accumulated state + run log, which cannot be reconstructed from the automation's code alone."
  auditability: "high — every section is plain-text markdown, so the loop's goal, its unsupervised-vs-escalate boundaries, its current state, and its per-run history are all directly readable from the file with no execution required; git carries the diff trail of contract edits."
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Production-run at the source practitioner's company (Super Divine) for months across four live loops — a react-doctor CLI-scan loop, a CRM lifecycle loop, a documentation-drift loop, and a support-inbox triage loop — explicitly framed as 'none of this is a demo.' Not yet adopted by the extracting system; adoption requires first deciding which engine units count as a 'loop' needing its own contract file."
contract:
  preconditions: "An autonomous loop or recurring automation exists (or is being set up) that runs repeatedly toward some purpose, and there is a place to keep one markdown file per automation. For the evolve-session cadence, the automation's past config, state/log history, and recent run transcripts are retrievable."
  invariants: "A filled file always carries all three sections: a Contract (goal + boundaries + SOP), a State snapshot, and an append-only Log. The Contract's boundaries always distinguish what the automation may do unsupervised from what must escalate to a human. The State section is kept deliberately small — current hypothesis, open backlog, shipped-but-follow-up only — it is working memory, not history. The Log is append-only: entries are added, never rewritten or deleted. One file per automation; unrelated loops are never merged into one file."
  governance: "Owner: whoever owns the automation over its operating lifetime keeps the file in sync with the running loop. The Contract section changes rarely and its edits should go through the same review the loop's behavior would; State is overwritten freely each run; Log only grows. A dedicated evolve session (every 5–10 runs) is the sanctioned channel for revising the Contract, pruning stale State, or promoting a repetitive SOP step into a script — coordinate it with any system-wide self-improvement cadence rather than running a second, uncoordinated self-modification path."
  recovery: "If the State section grows into a history log, prune it back to working-memory size — hypothesis, open backlog, pending follow-ups only. If the file has no boundaries, the automation has no escalation policy: do not run it unsupervised until they are written. If an evolve session proposes pruning a State item, confirm it is actually stale (not merely untouched recently) before removing it — evolve sessions seeing only the loop's own history can overfit to recent noise. If a large transcript feed makes an evolve session one of the most expensive runs in the loop's lifecycle, budget it separately from regular runs."
tags:
  - "extracted-artifact"
  - "template"
  - "loop-engineering"
  - "loop-contract"
  - "self-improvement"
  - "agentic-systems"
---

# Loop Contract File Schema

**Source:** [[loop-contract-anatomy-and-evolve-session-cadence]]
**Form:** template
**Extraction date:** 2026-07-19

A fill-in scaffold for the **one living markdown file per automation** that is simultaneously a loop's constitution and its memory. Answering every variable below produces a complete Loop Contract File: what the loop is *for*, what it may do alone versus what it must escalate, what it currently believes, and a durable run-by-run record of what it has already tried. Fill it once when the loop is created; then maintain it across the loop's operating lifetime — State is overwritten each run, the Log grows each run, and the Contract is revised on the evolve-session cadence.

## Variables

| Variable | Type | Description |
|---|---|---|
| `{{AUTOMATION_NAME}}` | string | Short name/purpose of this loop — the one automation this file governs. |
| `{{GOAL}}` | string | What winning looks like for this loop, and whether there is even a finish line (many loops are ongoing, not terminating). |
| `{{BOUNDARIES}}` | list | What the agent may do **unsupervised** vs. what must **escalate to a human**. Include explicit "never" rules where a default failure mode is known (e.g. a doc-maintainer loop's "never rewrite accurate docs to look busy" — added because the default agent failure is bias toward action). |
| `{{SOP}}` | list or "none" | Any specific workflow or principle the agent must follow **every run** (e.g. "verify each apparent drift before touching anything"). Set to "none" if the goal + boundaries fully specify the run. |
| `{{STATE_HYPOTHESIS}}` | string or "none" | The loop's current working hypothesis — what it currently believes about its problem. Kept small. |
| `{{STATE_BACKLOG}}` | list | Open items the loop knows about but has not yet handled. Working memory, not a full history. |
| `{{STATE_FOLLOWUP}}` | list | Things already shipped this cycle that are awaiting follow-up (verification, downstream effect, human sign-off). |
| `{{LOG}}` | append-only list | Run-by-run record: one entry per run (date/run-id + what happened + outcome). Append only — never rewrite or delete prior entries. Without it, "every morning the loop just rediscovers the same noise." |
| `{{EVOLVE_CADENCE}}` | integer (runs) | Every N runs (typically 5–10), hand the agent its own past config, state/log history, and recent run transcripts, and have it propose revisions to this file: sharpen the Contract, prune stale State, or promote a repetitive SOP step into a script. |

## Body

```
# Loop Contract File: {{AUTOMATION_NAME}}

## Contract
Goal:        {{GOAL}}
Boundaries:
  unsupervised-OK:   {{BOUNDARIES}}   # what the agent may do alone
  must-escalate:     {{BOUNDARIES}}   # what requires a human
SOP:         {{SOP}}                  # principles/steps followed every run
Evolve cadence: every {{EVOLVE_CADENCE}} runs

## State   (small on purpose — working memory, not history; overwritten each update)
Hypothesis:  {{STATE_HYPOTHESIS}}
Backlog:     {{STATE_BACKLOG}}
Follow-up:   {{STATE_FOLLOWUP}}

## Log   (append-only — one entry per run; never rewrite prior entries)
{{LOG}}
```

## Usage

Create one filled copy per automation and store it where the loop (and a human skimming the portfolio) can find it. Use it as:

- **The loop's constitution + memory in one place.** Ad-hoc "just prompt it in a loop" setups have no single home for what the loop is for, what it may do alone, what it believes, and what it tried — so each run re-litigates settled questions or silently drifts. This file is that home.
- **A durable working memory without a database.** The State + Log sections give the loop continuity across runs while staying git-diffable and human-skimmable — the property the source treats as central. For small loops, Contract + State + Log live in this one file; larger loops may reference additional artifacts from it.
- **The input to evolve sessions.** Every `{{EVOLVE_CADENCE}}` runs, feed the file (plus recent transcripts) back to the agent and ask it to revise itself — the sanctioned self-tuning channel. Scope each evolve session to this one automation, not a system-wide research cadence.

Render one filled file per distinct automation. A portfolio of loops (engineering scan, CRM lifecycle, doc-drift, inbox triage) gets one Loop Contract File each — never merge unrelated loops into a single file.

## Variation Axis

What changes between renderings:

- **Finish line.** A terminating loop (a goal it can complete) vs. an ongoing loop (maintenance with no end state) — shapes how `{{GOAL}}` and the completion expectation in `{{STATE_*}}` are written.
- **Boundary tightness.** Fully-unsupervised (nothing escalates) vs. draft-for-approval by risk (e.g. a CRM loop that auto-outreaches low-risk segments but drafts-for-approval high-risk ones) vs. verify-before-acting on everything (a doc-drift loop). The unsupervised-vs-escalate split in `{{BOUNDARIES}}` is where this lives.
- **State richness.** Minimal (hypothesis only) vs. full (hypothesis + backlog + follow-up) — richer State carries more continuity but must still be pruned to stay working-memory-sized.
- **Evolve cadence.** Frequent (every ~5 runs, faster adaptation, more evolve-session cost) vs. sparse (every ~10+ runs, cheaper, slower to shed staleness).

## Composition Note

This template is a **sibling, not a replacement**, of the [[loop-anatomy-spec-template]], and the two compose — a single automation may carry **both**:

- The **[[loop-anatomy-spec-template]]** fixes one loop's *mechanical iteration anatomy* at **build time** — completion signal, iteration budget, context policy, human-gate message, observability, resume state. It is a specify-stage checklist, filled once before the harness is built and largely static thereafter.
- **This Loop Contract File** tracks the *whole automation's living governance* across its **operating lifetime** — goal, boundaries, SOP, current state, and run log — edited continuously (State overwritten each run, Log grown each run, Contract revised each evolve session).

They answer different questions ("how does one iteration mechanically run and stop" vs. "what is this automation for, what may it do alone, what does it currently believe, what has it tried") at different altitudes, so a loop can hold an anatomy spec at build time and a contract file across its lifetime without either subsuming the other.

## Contract

### Preconditions
An autonomous loop or recurring automation exists (or is being set up) that runs repeatedly toward some purpose, and there is a place to keep one markdown file per automation. For the evolve-session cadence, the automation's past config, state/log history, and recent run transcripts are retrievable.

### Invariants
A filled file always carries all three sections: a Contract (goal + boundaries + SOP), a State snapshot, and an append-only Log. The Contract's boundaries always distinguish what the automation may do unsupervised from what must escalate to a human. The State section is kept deliberately small — current hypothesis, open backlog, shipped-but-follow-up only — it is working memory, not history. The Log is append-only: entries are added, never rewritten or deleted. One file per automation; unrelated loops are never merged into one file.

### Governance
Owner: whoever owns the automation over its operating lifetime keeps the file in sync with the running loop. The Contract section changes rarely and its edits should go through the same review the loop's behavior would; State is overwritten freely each run; Log only grows. A dedicated evolve session (every 5–10 runs) is the sanctioned channel for revising the Contract, pruning stale State, or promoting a repetitive SOP step into a script — coordinate it with any system-wide self-improvement cadence rather than running a second, uncoordinated self-modification path.

### Recovery
If the State section grows into a history log, prune it back to working-memory size — hypothesis, open backlog, pending follow-ups only. If the file has no boundaries, the automation has no escalation policy: do not run it unsupervised until they are written. If an evolve session proposes pruning a State item, confirm it is actually stale (not merely untouched recently) before removing it — evolve sessions seeing only the loop's own history can overfit to recent noise. If a large transcript feed makes an evolve session one of the most expensive runs in the loop's lifecycle, budget it separately from regular runs.
