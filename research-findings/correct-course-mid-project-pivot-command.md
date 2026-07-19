---
name: 'Correct Course: Structured Mid-Project Pivot Command'
summary: A dedicated Scrum Master command that analyzes project progress, identifies whether to revert, branch, or restart, and generates new/modified epics and stories to accommodate mid-project scope
  changes without losing completed work.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- bmad-method-masterclass.md
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
related_findings:
- file: bmad-method-v6-multi-agent-sdlc.md
  rel: enabled-by
pipeline_status: synthesized
consumed_by:
- skills/correct-course-mid-project-pivot.md
- production-agent-execution.md
---

## What It Is

A structured command (`correct course`) in the BMad Scrum Master agent for handling mid-project pivots. When a developer realizes they forgot something, want to make a significant change, or need to integrate a new API/library mid-build, they wrap up their current story and invoke this command. The Scrum Master then:

1. Analyzes how far the project has progressed (completed stories, in-progress work)
2. Determines whether it is better to revert to an earlier stage, generate new future stories from the current state, or recommend a full restart
3. Identifies which epics and stories need modification, addition, or removal
4. May update the architecture doc, PRD, or tech stack as side effects
5. Produces a revised story backlog that accounts for the pivot while preserving completed work

The PM agent also supports `correct course` for higher-level requirement changes.

## Why It Matters

Mid-project scope changes are inevitable. Without a structured correction mechanism, developers either hack changes into existing stories (accumulating tech debt) or restart from scratch (wasting completed work). This command provides a middle path: acknowledge the change, assess impact, and re-plan from the current state.

## Why People Are Using It

BMad community members reportedly requested this feature without realizing it already existed. Brian describes it as "a lifesaver depending on the situation" and positions it as the escape hatch when the planning-heavy approach encounters reality.

## Potential Improvements

Could be extended with impact analysis that estimates token/time cost of the pivot. Could integrate with version control to identify which committed code would need refactoring.

## Potential Failure Modes

The command may recommend overly conservative approaches (full restart) when incremental adjustment would suffice. Quality depends on how well the agent understands the current project state from reading existing artifacts.

## Extraction Note — 2026-04-19
Extracted as **skill**: [[correct-course-mid-project-pivot]] in `extracts/skills/`
