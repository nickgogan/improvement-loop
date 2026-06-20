---
title: "Scheduled Operations Assistant"
id: "scheduled-operations-assistant"
type: "schematic"
category: "system-design"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-06-18"
updated: "2026-06-18"
author: "claude"
altitude: "middle"
maturity: "seed"
grounded_in:
  - "scheduled-tasks-for-real-time-context-maintenance"
  - "claude-code-daily-brief-multi-source-inbox-obsidian"
  - "ai-managed-vault-separate-from-human-vault"
  - "advisory-only-for-persistent-mutations"
  - "autonomy-gradient-not-binary-delegation"
  - "build-operate-separation-principle"
  - "five-pillar-agentic-os-framework"
composed_of:
  - "systems/improvement-loop/.claude/skills/design-agent"
  - "systems/improvement-loop/archive/household-os/architecture"
  - "systems/improvement-loop/archive/household-os/schemas"
source_dd:
  - "DD-107"
tags:
  - "schematic"
  - "operations"
  - "assistant"
aliases:
  - "Operations Assistant"
  - "Personal Ops Assistant"
  - "Household Assistant"
---

# Scheduled Operations Assistant

> A single persistent assistant that runs on a cadence — pulling live data from many sources into
> one curated store and surfacing a daily brief — acting on its own only where a mistake is cheap
> and reversible, and recommending (never applying) anything that touches durable state.

This schematic captures the **scheduled personal/operations assistant** pattern (daily-brief
agents, vault-as-OS, second-brain maintenance). It is the configuration the engine is steering
**Household OS toward as a consumer** (now on Notion, DD-106) — the engine *designs* it, it does
not run it. Like [[project-coding-workcell]] and unlike the engine's own research-scanner and
audit-workcell seeds, this is a consumer-facing blueprint.

## Demand

| Axis | Value |
|------|-------|
| **Function** | operations / assistant |
| **Scope / lifespan** | personal-persistent (a standing assistant over a person's or household's operational life) |
| **Non-functionals** | data boundary: private personal data — strict ownership, no vendor lock-in of memory; reliability: medium — a missed brief is recoverable next cadence, but a wrong mutation of durable state is not; autonomy need: bounded — runs unattended but gates persistent changes; cost: bounded by cadence |

Reach for this when one owner wants an agent to keep their operational reality (calendar, inbox,
tasks, notes, household data) current and digestible without manual upkeep — and wants the agent to
*act* on the cheap, reversible stuff but *ask* before changing anything durable.

## Configuration

### Capability + memory core

Run **scheduled ingestion tasks** that pull live operational data (calendar, email, messages,
tasks, transcripts, metrics) into a **curated store on a cadence**, then synthesize a **daily
brief** from the store's current state. **Memory is an agent-owned store, separate from the human's**
([[ai-managed-vault-separate-from-human-vault]]): the assistant writes only its own store; the human
reads it. Keeping the store in an owner-portable form (markdown vault, or a Notion workspace the
owner controls) is the anti-lock-in core that survives a model swap. This ingest→curate→brief core
is the reusable part; swap the sources and the surface and it holds.

### Coordination / architecture

**Single persistent agent** with a set of recurring scheduled jobs; it may fan out **stateless**
helpers for per-source ingestion (one fetch/triage per source), but synthesis into the brief is
single-threaded so the daily read is coherent. There is no long-lived multi-agent topology — the
schedule, not an orchestrator, is what drives the work.

### Autonomy

**consultant** — its dominant posture is *advise*: it produces briefs and surfaces
recommendations, and the human acts on anything durable. This is a deliberate **gradient**, not a
flat level ([[autonomy-gradient-not-binary-delegation]]): the assistant is *fully autonomous on
low-blast reversible actions* (archive cold email, draft/overwrite today's brief, file a summary)
and **advisory-only on persistent or broad-blast mutations** — settings, schema, anything that
outlives the run is recommended with a rollback note and applied by the human
([[advisory-only-for-persistent-mutations]]). It operates; it does not reconfigure itself or its
world.

### Deployment surface

Two grounded options; the schematic is surface-parameterized:
- **Notion-embedded** (the DD-106 Household OS direction): a Notion custom agent over the owner's
  workspace, provider model, scheduled runs.
- **Claude Code over a local markdown vault** (what the source findings actually document): scheduled
  Claude Code tasks writing an AI-owned Obsidian vault.
The *grounding evidence sits on the vault variant*; the Notion variant is the engine's intended
target and is the thinner-grounded of the two (see maturity).

## Evaluation & feedback

- **How it's evaluated:** **outcome + human.** The brief is judged by whether the owner can run
  their day from it without opening the underlying apps — an outcome the owner observes directly, not
  a metric the agent self-reports. Triage rules (what to archive vs. surface) are owner-taught and
  owner-corrected.
- **Feedback mechanism:** **human + external.** Human: the owner corrects triage rules, reprioritizes,
  and applies/declines the advisory recommendations — that adjudication steers the next cadence.
  External: the live sources themselves are the feedback signal that keeps the store from decaying
  into a six-month-old snapshot ([[scheduled-tasks-for-real-time-context-maintenance]]). The
  **build/operate split** keeps it honest — operating the assistant (running briefs) is separate from
  rebuilding it (changing its config), and only the former is unattended
  ([[build-operate-separation-principle]]).

## Grounding & composition

- **`grounded_in`** — the evidence:
  - [[scheduled-tasks-for-real-time-context-maintenance]] — recurring jobs keep a second brain
    current; grounds the scheduled-ingestion core and the staleness motivation.
  - [[claude-code-daily-brief-multi-source-inbox-obsidian]] — multi-source brief + rule-trained
    triage; grounds the synthesis surface and the reversible-autonomous triage actions.
  - [[ai-managed-vault-separate-from-human-vault]] — agent-owned store the human reads; grounds the
    memory core and the portability / no-lock-in non-functional.
  - [[advisory-only-for-persistent-mutations]] — recommend-don't-apply for durable, broad-blast state
    (D9 Governance); grounds the consultant autonomy on the mutation side.
  - [[autonomy-gradient-not-binary-delegation]] — autonomy by blast radius / reversibility; grounds
    the gradient (autonomous on reversible, advisory on persistent).
  - [[build-operate-separation-principle]] — operating ≠ rebuilding; grounds "runs unattended, but
    reconfiguration is gated."
  - [[five-pillar-agentic-os-framework]] — the personal-OS backdrop this assistant is one pillar of.
- **`composed_of`** — how the engine builds it (designs, does not operate):
  - `/design-agent` — author the assistant (identity, scheduled-job set, triage rules, autonomy
    envelope).
  - `archive/household-os/architecture` — the lifted Household OS architecture docs
    (the operational model the assistant serves).
  - `archive/household-os/schemas` — the 7 Notion schemas; the data contract for the
    Notion-embedded variant.

## Risk & maturity

- **Known risks / failure modes:** (1) silent staleness — a scheduled job fails and the brief looks
  current but isn't; failures must surface, not no-op; (2) over-aggressive triage deletes signal —
  the archive heuristic needs careful early oversight; (3) store rot — an agent-owned store that
  only grows, never curates, degrades over time (the same decay risk the research-scanner carries).
- **Maturity:** seed — the **vault variant is well-grounded** in practitioner-documented patterns,
  but the **Notion-embedded target (DD-106) is thinly grounded** — the source findings document
  Obsidian/Claude-Code instances, not Notion custom agents. Not instantiated via `/design-agent`.
  This is a captured blueprint with a known grounding gap on its intended surface.
- **Revisit when:** the Household OS Notion build begins (instantiate + harvest Notion-native
  findings to thicken the Notion variant's grounding), or any `grounded_in` finding moves (re-check
  the eval/feedback and autonomy layers).
