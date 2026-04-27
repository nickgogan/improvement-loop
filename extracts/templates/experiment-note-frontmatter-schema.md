---
title: "Experiment Note Frontmatter Schema"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "obsidian-experiment-notes-personal-health-tracking"
identification_report: "building-agentic-systems.harvest-queue.md::obsidian-experiment-notes-personal-health-tracking::template::experiment-note-frontmatter-schema"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
version: 1
deployed: false
deployed_to: null
context:
  applies_to:
    - "longitudinal-tracking notes capturing hypothesis-driven personal experiments over weeks or months"
    - "personal health, productivity, and behavior-change tracking systems where each experiment has explicit success criteria"
    - "structured experiment journaling in any markdown-frontmatter knowledge vault"
    - "human-readable personal data layers consumed by AI agents that read and write observations"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "trivial — the template is a markdown file with frontmatter; removal or replacement does not invalidate prior experiment entries since each note is self-contained"
  auditability: "high — every experiment is a single file with explicit hypothesis, protocol, success criteria, and dated observations; full lineage is filesystem-grep-able"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-documented pattern from Obsidian + Claude Code workflow. No adoption within this system at time of extraction; could apply to MetaSystem reflection rounds, dimension experiments, or personal-OS use cases."
contract:
  preconditions: "Vault root is a markdown collection with frontmatter parsing (Obsidian, Logseq, raw filesystem grep, or equivalent). A dashboard note exists or will be created at {{DASHBOARD_LINK}} before the first experiment closes. Numeric tracked fields share a unit and scale across all observations within one experiment."
  invariants: "type field is always literal `experiment`. status is always one of {proposed, in_progress, complete}. Hypothesis section is non-empty before status advances past `proposed`. Success Criteria is measurable (contains a threshold, percentage, count, or boolean condition). Observations entries are dated and append-only — past entries are never edited. Numeric fields keep consistent units and scales across the lifetime of one experiment."
  governance: "Owner: Improvement Loop (extraction origin). Domain owner: whoever maintains the vault where the template is deployed. Schema changes (adding/removing frontmatter fields, renaming sections) require explicit authorization since they break agent reads on existing experiments."
  recovery: "If status transitions backward (in_progress → proposed): treat as a new experiment, archive the prior file. If numeric scale changes mid-experiment: close the experiment, start a fresh one with the new scale; do not mix scales in averages. If observations file grows beyond agent read budget: split into per-month observation logs linked from the master experiment note. If `experiment closed` convention is missing: add a `completed_date` frontmatter field and a closing observation entry before archiving."
tags:
  - "extracted-artifact"
  - "template"
  - "longitudinal-tracking"
  - "personal-data-layer"
---

# Experiment Note Frontmatter Schema

**Source:** [[obsidian-experiment-notes-personal-health-tracking]]
**Form:** template
**Extraction date:** 2026-04-27

## Frontmatter Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | literal `experiment` | yes | Marks the note as an experiment file. Agent reads filter on this. |
| `status` | enum `{proposed, in_progress, complete}` | yes | Closed enum. Drives dashboard aggregation and "active experiments" filters. |
| `dashboard` | wikilink | yes | Link to the domain dashboard note that aggregates related experiments (e.g., `[[Health Dashboard]]`). |
| `started_date` | ISO date | when status ≥ in_progress | When the protocol began. |
| `completed_date` | ISO date | when status = complete | When the experiment closed. Required for "experiment closed" convention. |
| `hypothesis_summary` | string | yes | One-sentence restatement of the body's Hypothesis section, for dashboard table rendering. |
| `tracked_fields` | list of strings | yes | Names of the numeric fields tracked in observations (e.g., `[gym_volume, sessions_per_week, mood, energy, sleep_quality]`). Lets agents discover which fields to write. |
| `tracked_units` | map field→unit | yes | Unit/scale per tracked field (e.g., `mood: "1-10"`, `gym_volume: "lbs"`). Enforces unit consistency. |

## Body Sections

| Section | Purpose |
|---------|---------|
| `## Hypothesis` | Explicit predicted outcome stated before the protocol begins. Falsifiable. |
| `## Protocol` | Step-by-step intervention. Concrete actions, not goals (e.g., "wake at 06:30, open window, walk 10 min, then coffee"). |
| `## Success Criteria` | Measurable threshold (e.g., "80% of days within 30 minutes of target wake-up time"). Must contain a numeric or boolean condition. |
| `## Observations` | Dated, append-only log. Each entry: ISO date + numeric tracked fields + freeform note. Filled daily (or per protocol cadence). |

## Variables / Placeholders

| Placeholder | Description |
|-------------|-------------|
| `{{EXPERIMENT_TITLE}}` | Short title of the experiment, used as the file name and H1. |
| `{{DASHBOARD_LINK}}` | Wikilink target for the domain dashboard. |
| `{{HYPOTHESIS}}` | One paragraph predicting the outcome and the mechanism. |
| `{{PROTOCOL}}` | Numbered list of steps that constitute the intervention. |
| `{{SUCCESS_CRITERION}}` | Measurable threshold; numeric or boolean. |
| `{{NUMERIC_TRACKED_FIELDS}}` | List of named fields with units, e.g., `mood (1-10), energy (1-10), gym_volume (lbs)`. |
| `{{OBSERVATIONS}}` | Daily entries; each line carries a date and the tracked-field values. |
| `{{STARTED_DATE}}` | ISO date when status flips to `in_progress`. |
| `{{COMPLETED_DATE}}` | ISO date when status flips to `complete`. |

## Body

```markdown
---
type: experiment
status: proposed
dashboard: {{DASHBOARD_LINK}}
started_date: null
completed_date: null
hypothesis_summary: "<one-sentence summary of {{HYPOTHESIS}}>"
tracked_fields:
  - <field_1>
  - <field_2>
tracked_units:
  <field_1>: "<unit or scale>"
  <field_2>: "<unit or scale>"
---

# {{EXPERIMENT_TITLE}}

## Hypothesis
{{HYPOTHESIS}}

## Protocol
{{PROTOCOL}}

## Success Criteria
{{SUCCESS_CRITERION}}

## Observations
<!-- Append-only. Each entry: ISO date, numeric values for tracked_fields, freeform note. -->

- YYYY-MM-DD — <field_1>: <value>, <field_2>: <value>. <freeform note>
- YYYY-MM-DD — <field_1>: <value>, <field_2>: <value>. <freeform note>

{{OBSERVATIONS}}
```

## Usage Notes

Use this template when:
- The work is a hypothesis-driven personal experiment with measurable success criteria
- Observations are recurring (daily, per-session, per-meal) and benefit from longitudinal aggregation
- An AI agent will read prior entries and append new observations during a check-in (morning briefing, end-of-day review)
- The vault doubles as the database — no separate time-series store yet

Do not use when:
- The need is general note-taking, not a tracked experiment
- There is no measurable success criterion (then it's a project log, not an experiment)
- Observations would mix incompatible units or scales (then split into multiple experiments)

Integration points:
- **Daily journaling:** the agent's morning routine reads `status: in_progress` experiments, appends an observation entry per active experiment, and surfaces any nearing the success-criteria threshold.
- **Dashboard rendering:** an Obsidian Dataview (or equivalent) query selects all experiments by `dashboard:` link and renders status, hypothesis_summary, and current vs. target metric.
- **Completion:** when success criteria are met (or refuted), the operator transitions status to `complete`, sets `completed_date`, and writes a closing Observations entry summarizing the result. The agent then drops the experiment from the active list.

## Variation Axis

1. **Domain** — health, productivity, sleep, behavior, finance, learning. The schema is domain-agnostic; only `tracked_fields` and `dashboard:` change per domain.
2. **Observation cadence** — daily (most common), per-session, per-meal, weekly. Cadence shapes how the agent batches reads and writes.
3. **Single-file vs. split observations** — for short experiments, all observations live in the experiment note. For long-running experiments (>3 months), split observations into a per-month linked log to keep agent reads cheap.

## Contract

### Preconditions
Vault root is a markdown collection with frontmatter parsing (Obsidian, Logseq, raw filesystem grep, or equivalent). A dashboard note exists or will be created at `{{DASHBOARD_LINK}}` before the first experiment closes. Numeric tracked fields share a unit and scale across all observations within one experiment.

### Invariants
`type` field is always literal `experiment`. `status` is always one of `{proposed, in_progress, complete}`. Hypothesis section is non-empty before status advances past `proposed`. Success Criteria is measurable (contains a threshold, percentage, count, or boolean condition). Observations entries are dated and append-only — past entries are never edited. Numeric fields keep consistent units and scales across the lifetime of one experiment.

### Governance
Owner: Improvement Loop (extraction origin). Domain owner: whoever maintains the vault where the template is deployed. Schema changes (adding/removing frontmatter fields, renaming sections) require explicit authorization since they break agent reads on existing experiments.

### Recovery
If status transitions backward (in_progress → proposed): treat as a new experiment, archive the prior file. If numeric scale changes mid-experiment: close the experiment, start a fresh one with the new scale; do not mix scales in averages. If observations file grows beyond agent read budget: split into per-month observation logs linked from the master experiment note. If `experiment closed` convention is missing: add a `completed_date` frontmatter field and a closing observation entry before archiving.
