---
name: 'BMAD Help: Context-Aware Adaptive Module Routing'
summary: BMAD V6's help system inspects installed modules, checks project state, and adapts recommendations dynamically. Can recommend skipping phases based on context (e.g., skip brainstorming if idea
  is solid). Routes users to the right workflow/skill across all installed modules.
implementation_notes: Parallels MetaSystem's skill discovery problem. A similar routing layer could inspect installed skills and recommend the right one based on user intent and project state.
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- bmad-v6-is-finally-here.md
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
related_findings:
- file: bmad-dependency-graph-module-ordering.md
  rel: enabled-by
- file: bmad-module-marketplace-with-vetting.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- production-agent-execution.md
---

## What It Is

BMAD Help is a context-aware routing system within BMAD V6. When a user asks "what should I do?", it: (1) inspects all installed modules and skills, (2) checks whether the user has already completed any project steps, (3) interprets the user's intent from their question, and (4) recommends the appropriate workflow, agent, or skill. Crucially, it adapts its recommendations based on context -- telling a user with a solid idea to skip brainstorming and jump to PRD creation, while recommending the creative innovation suite to someone still exploring.

The system issues exact commands to run (e.g., "start with BMAD BMM create PRD"). It scales with the module ecosystem -- as more modules are installed, more options become available and the routing adapts.

## Why It Matters

As agent ecosystems grow, users face a discovery problem: which skill or workflow should I use for my current situation? A routing layer that understands both the available tools and the user's current state solves this without requiring users to memorize all options. This is particularly relevant for MetaSystem, which has 30+ skills and growing.

## Why People Are Using It

BMAD V6 demonstrates this in production. The demo shows two different contexts producing two different recommendations from the same help command. Users report the help system as one of the key V6 improvements over V4, where "there was a lot and it was hard to know what to do."

## Potential Improvements

Implement a similar routing layer for MetaSystem skills. Could be a lightweight skill that reads .claude/skills/ directory, inspects PROGRESS.md for current state, and recommends the appropriate next action.

## Potential Failure Modes

Routing logic can become stale if it does not update when new skills are added. Over-eager routing (recommending specific actions when the user just wants information) can feel presumptuous. The routing layer itself consumes tokens to inspect state.
