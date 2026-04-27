---
name: 'Morning Routine Skill with Active Experiment Check-In'
summary: A Claude Code skill named "daily" that runs at morning start, surfaces all active experiments from Obsidian, asks targeted observation questions for each, logs responses, and generates next
  actions for the day — converting a daily habit into an automated experiment review and scheduling loop.
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
- file: obsidian-experiment-notes-personal-health-tracking.md
  rel: companion
pipeline_status: synthesized
consumed_by:
  - "building-agentic-systems.md"
---
# Morning Routine Skill with Active Experiment Check-In

## What It Is

A Claude Code skill (installed as `/daily`) that runs at the start of each morning session and implements a structured morning operating routine:

1. **Goal check:** Read the goals file from Obsidian and surface current goals
2. **Experiment discovery:** Scan the vault for all notes with `type: experiment` and `status: in_progress`; list them for the session
3. **Observation collection:** For each active experiment, ask a targeted question (e.g., "How is the morning sunlight experiment going? Any observations about caffeine delay? What was your wake-up time?")
4. **Data logging:** Write the responses to the experiment note's observation section and update the numeric tracking fields (mood, energy, sleep quality)
5. **Next-action scheduling:** Based on observations, schedule or suggest the day's experiment actions (gym session, morning walk, etc.) into the calendar

The skill is parameterized by the user's experiment portfolio — as experiments are added or completed, the morning routine automatically adapts because it reads live from the vault rather than from hardcoded questions.

## Why It Matters

The morning routine skill is the mechanism that prevents experiments from remaining intentions. Without a daily review forcing function, even well-designed experiments decay: the user forgets to log, misses a few days, loses track of trends, and eventually abandons the experiment.

The skill inverts the discipline requirement: instead of the user needing to remember to check their experiments, Claude Code asks the questions every morning. The user only needs to show up and answer — the logging, scheduling, and pattern surfacing are handled automatically.

The skill is also the bridge between the NotebookLM knowledge layer (where experiments were designed) and the Obsidian data layer (where results accumulate): it is the daily agent that keeps the review loop running.

## Why People Are Using It

- Replaces willpower with structure: the skill forces the review loop to run even when motivation is low
- Self-updating: adding a new experiment to Obsidian automatically adds it to the morning check-in
- Low friction: questions are targeted and specific; the user answers in natural language and Claude writes the structured data
- Observation data compounds: over weeks, the vault accumulates enough data to run meaningful analysis (the practitioner shows energy and mood trends from gym consistency data)

## Potential Improvements

A streak tracker and experiment completion detector would signal when a behavior has become a habit (and the experiment can be closed). A weekly summary skill that reviews all experiment data and surfaces insights would complement the daily check-in.

## Potential Failure Modes

- The skill must be invoked manually each morning; there is no push mechanism to start it automatically
- Experiment fatigue: too many active experiments make the morning check-in feel like work rather than a routine
- Observation quality varies with morning mood — rushed responses produce low-quality data
- The skill reads from the vault path hardcoded in its SKILL.md; vault reorganization breaks the skill
