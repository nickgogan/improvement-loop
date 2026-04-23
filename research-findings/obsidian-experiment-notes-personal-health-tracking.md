---
name: 'Obsidian Experiment Notes as Personal Data Layer for Behavior Change Tracking'
summary: Structure personal experiments as Obsidian markdown files with typed frontmatter (hypothesis, protocol, observations, numeric data fields) so Claude Code can read existing experiment data, log new
  observations, and surface experiment status — turning a personal vault into a queryable behavioral data layer.
implementation_notes: null
category: Agentic Systems
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- notebooklm-claude-code-expert-experiments.md
proposals: []
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
related_findings:
- file: learn-plan-act-review-loop-closing-the-knowledge-gap.md
  rel: companion
- file: scale-threshold-heuristic-obsidian-vs-rag.md
  rel: companion
pipeline_status: raw
consumed_by: []
---
# Obsidian Experiment Notes as Personal Data Layer for Behavior Change Tracking

## What It Is

A pattern where personal behavioral experiments are stored as structured Obsidian markdown files with:

- **Frontmatter fields:** `type: experiment`, `status: in_progress/proposed/complete`, links to a health dashboard note
- **Body sections:** Hypothesis (explicitly stated), Protocol (step-by-step, e.g., "wake up, open window, go outside 10 min, get coffee"), Success Criteria (measurable, e.g., "80% of days within 30 minutes of target wake-up time"), Observations (filled daily)
- **Data fields:** Numeric tracking (gym volume, sessions per week, mood 1-10, energy 1-10, sleep quality) that Claude Code writes to each morning
- **Dashboard link:** A separate Obsidian note aggregates all active experiments, shows current vs. target state, and plots tracked data

Claude Code can read existing experiment files without explanation ("go look up my fitness experiments and get the data from there") and write new observation entries during the morning check-in. The vault becomes a queryable personal data store that agents can read and write to without custom infrastructure.

## Why It Matters

Two properties make this pattern effective:

1. **Machine-readable personal data:** Structured frontmatter and consistent field names mean Claude Code can locate, read, and write experiment data with a simple file read — no database, no API, no schema migration. The vault IS the database.

2. **Continuity across sessions:** Experiment data persists between Claude Code sessions without any special memory mechanism. A new session can pick up exactly where the last one ended by reading the experiment files. This eliminates the "context reset" problem for longitudinal personal tracking.

The practitioner demonstrates Claude reading pre-existing fitness experiment data mid-session without any explanation or upload — the vault's structure was sufficient for the agent to find and use the data.

## Why People Are Using It

- Zero infrastructure: Obsidian markdown is the database
- Human-readable and editable: the user can view, edit, and understand every data point without a dashboard tool
- Agent-writable: Claude Code can log observations, update status, and write analysis in the same format the user reads
- Dashboard composable: Obsidian Dataview queries aggregate all experiments into a single view without any code

## Potential Improvements

A formal experiment frontmatter schema (documented in CLAUDE.md or a template file) would make it reliable across sessions and agents. Export to a time-series store (CSV, SQLite) would enable richer statistical analysis than markdown can support.

## Potential Failure Modes

- Inconsistent field naming across experiments breaks agent reads — requires a template or schema enforcement
- Large observation histories in a single file slow down Obsidian and increase read cost for agents
- Without a defined "experiment closed" convention, old experiments accumulate and pollute the active experiment list
- Numeric tracking requires consistent units and scales; mixing scales (e.g., mood 1-5 vs. 1-10) produces meaningless averages
