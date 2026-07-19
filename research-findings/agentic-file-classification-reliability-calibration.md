---
name: "Agentic File-Classification Reliability Calibration — 78% Accuracy, Context-Blind Failure Mode"
summary: |-
  Plain English: Tiago Forte (creator of the PARA method) gave Claude Code his real,
  messy 32-file desktop backlog and one instruction — sort it into PARA — then checked
  every placement by hand. Result: 78% correct (7 of 32 misfiled), with the model's
  understanding of the taxonomy itself independently verified as flawless beforehand.
  The misses cluster in one specific place: the agent cannot tell a time-bound project
  apart from the ongoing area it lives inside, or spot that something looking disposable
  actually has planned future value — both are gaps in context the agent structurally
  doesn't have, not gaps in understanding the categories. Useful calibration data for
  any design that routes agent output into a small taxonomy (decision/pattern/work-item
  routing, memory-tier classification) — a real, checked-every-decision error rate and
  its specific failure shape, not a benchmark number.
implementation_notes: null
category: "Agentic Systems"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "IL (self-improve lesson-routing and Form Router classification-gate design reference)"
  - "General"
adopted_in: []
sources:
  - "ai-organized-my-files-para-claude-code.md"
related_findings:
  - file: "ai-delegated-knowledge-organization.md"
    rel: "extends"
  - file: "para-based-file-memory.md"
    rel: "same-problem"
  - file: "flat-root-vault-with-property-based-organization.md"
    rel: "same-problem"
  - file: "production-memory-architecture-spectrum.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-18"
last_updated: "2026-07-18"
pipeline_status: "raw"
consumed_by: []
---

# Agentic File-Classification Reliability Calibration — 78% Accuracy, Context-Blind Failure Mode

## What It Is

A quantified reliability calibration for agentic taxonomy classification, from a
controlled real-world trial rather than a benchmark. Tiago Forte — creator of the PARA
method (Projects/Areas/Resources/Archives) and author of the bestselling *Building a
Second Brain* — gave Claude Code (Opus 4.6, a fresh $20/mo Pro account with memory and
connectors off) his own two-weeks-neglected desktop: 32 real files spanning screenshots,
PDFs, markdown, spreadsheets, financial statements, and a zip archive. Before running the
experiment, he adversarially confirmed the model's understanding of PARA itself was
100% correct — ruling out "doesn't understand the taxonomy" as an explanation for
whatever followed.

Setup and procedure:

- **Working-directory isolation.** A fresh folder ("PARA Reorg") became the agent's
  sandboxed root; every file was dropped in first, and the session's working directory
  was scoped to just that folder — "basically how I start every significant session."
- **Single instruction, explicit escape hatch.** "Organize all the files, folders, and
  documents into the PARA system. If there's anything you're unsure about, ask me."
- **Exploration before action.** The agent read file contents (not just filenames) and
  screenshots (via image reading), taking 2-3 minutes, then surfaced clarifying
  questions *before moving anything*: an unreadable PDF (offered multiple-choice
  guesses), three ambiguous self-referential screenshots ("what are these for?"), and
  permission to archive likely-ephemeral items (a meme, a calendar-deletion screenshot).
- **Plan, then permission, then execution.** It proposed a structure (4 projects, 3
  areas, 1 archive), asked for blanket permission before moving files, then worked a
  self-tracked todo list to execute (~3-4 minutes).

**Result: 7 of 32 documents misfiled — 78% accuracy.** Two named failure instances share
one root cause:

1. Several finance documents were actually a bounded, time-sensitive **project** (this
   year's tax filing) nested inside a general ongoing **area** (finances); the agent
   filed them at the area level. Forte: "There's really no way for Claude to know that."
2. Two screenshots capturing surprising agent behavior were archived as unimportant
   ephemera; Forte knew they had specific planned future value (footage for a course)
   invisible in the artifacts themselves.

**The generalized failure mode:** the agent cannot distinguish a general/ongoing
category from a specific/bounded instance nested within it, and cannot detect hidden
future value in content that looks disposable — both are failures of missing
lived/future context, not comprehension failures of the taxonomy.

## Why It Matters

This is a rare real-world (not synthetic) calibration point for a task shape that
recurs constantly in agent system design: an agent classifies content into a small
fixed taxonomy on a human's behalf — project/area/resource/archive here,
decision/pattern/work-item elsewhere, or memory-tier routing, or accept/reject/monitor
triage. 78%-with-verified-taxonomy-comprehension is a useful prior: even when the agent
unambiguously understands the categories, instance-level judgment calls introduce a
roughly 1-in-4 error rate in this trial, and the errors are not random — they cluster
where a bounded instance sits inside a general category, and where classification
requires knowing something about future intent that isn't present in the artifact
itself.

For the engine specifically, this is relevant prior art anywhere output gets
auto-routed into a small taxonomy — the self-improve lesson-store's routing into
DD-shaped / pattern-shaped / IB-shaped promotion candidates, and the Form Router's
pattern/skill/rule/template/agent classification are both structurally the same task
shape. Not a mandate to add gates (this finding is evidence, not a directive on
implementation), but a concrete data point for calibrating how much a small-taxonomy
classifier should be trusted unreviewed, and where specifically ("is this a bounded
sub-instance of a broader category?", "does this look disposable but have unstated
future value?") the ambiguity will bite hardest.

## Why People Are Using It

Forte ran this as a public, unedited, checked-every-decision experiment specifically to
pressure-test his own PARA method against Claude Code, on a stock account with no
special configuration ("everything you see here is going to be exactly what you would
see if you sign up for a pro account tomorrow"). This is honest-disclosure practitioner
reporting — the creator of the taxonomy testing whether an agent can apply it, and
publishing the failures alongside the successes rather than only the wins.

His response to the 78% was calibration, not rejection: (1) he recommends learning and
applying PARA manually first, since manual application "reveals the structure of your
life" in a way delegation skips; and (2) his team shipped an official "PARA skill" that
adds "a bunch of little subtle instructions and guidelines to try to get that accuracy
rate a little bit higher" — i.e., prompt/skill-layer refinement as the response to a
measured error rate, not abandonment of delegation.

## Potential Improvements

- Both named failure instances resolve with one targeted clarifying question ("is this
  a sub-project of X, or does it belong at the X level?" / "is this archival, or does it
  have planned future use?") — a cheap, narrowly-scoped question pattern aimed at
  exactly the ambiguity class identified, rather than broader interrogation of every
  classification.
- A consequence-weighted human-review gate: Forte's own point is that stakes vary
  (buried tax documents risk a missed deadline; a misfiled meme doesn't) — routing
  designs could flag only classifications whose downstream cost of error is high for
  review, rather than reviewing uniformly or not at all.
- Track corrections over time as calibration data rather than treating each trial as a
  one-off. The "PARA skill" response is exactly this at the prompt-engineering layer; a
  routing system could go further and log correction patterns to detect recurring
  boundary-ambiguity types.

## Potential Failure Modes

- n=32, single trial, single practitioner, single model (Opus 4.6) — 78% is one data
  point, not a validated rate; don't treat it as a general agent-classification-accuracy
  constant.
- The failure mode is specifically about context the agent structurally cannot have (the
  human's future plans, the human's current tax-year cycle) — mitigations that add more
  taxonomy instructions (like the "PARA skill") address comprehension gaps, not this
  context gap; only a clarifying question or human review closes it.
- Post-hoc "checked every decision" review detects the error after the fact, it doesn't
  prevent it. File moves are cheaply reversible, so post-hoc review was sufficient here;
  for irreversible or time-sensitive routing decisions, an equivalent design would need
  a pre-hoc gate instead.
