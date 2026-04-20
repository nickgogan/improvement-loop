---
notion_id: 32b1e08b-9b34-811d-8fc9-f1fa3d1071aa
name: Phase-Task Hierarchical Plan Decomposition
summary: GSD2 structures all plans as a two-level hierarchy — high-level phases containing individual tasks — with each task assigned to a fresh-context sub-agent, and a project.md/requirements.md as the
  canonical dual sources of truth.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- gsd-2-vs-claude-code-a-new-ai-king.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: archon-yaml-defined-harness-workflows.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Phase-Task Hierarchical Plan Decomposition

## What It Is
GSD2 decomposes user prompts into: (1) phases — high-level implementation stages (research, architecture, implementation, testing, deployment); and (2) tasks within each phase — individual scoped work items, each executable by a single sub-agent in one context window. The project.md file serves as the high-level architectural source of truth; requirements.md documents functional requirements. This two-level hierarchy maps naturally to the MACHINE framework's master plan/sub-plan decomposition and Roman's 30k-token plan sizing guideline. GSD2 makes this decomposition explicit and user-visible during the planning phase, allowing human review and modification before execution begins.

## Why It Matters
Two-level decomposition (phase/task) gives practitioners a clear navigation structure over complex projects and allows targeted re-running of failed phases rather than restarting entirely.

## Why People Are Using It
The structured plan output (12 tasks for a simple expense tracker) provides transparency about what the agent is about to do — matching Claude Code's plan mode output.

## Potential Alternatives
Flat task lists (Ralph loops, MACHINE framework sub-plans). Three-level hierarchy for very large projects (epic/story/task). Linear sequential phases without explicit task decomposition.

## Potential Improvements
Dependency graph visualization between tasks and phases. Auto-detection of tasks that can be parallelized vs. tasks that must be sequential.

## Potential Failure Modes
Over-scoped phases produce tasks that exceed the one-context-window iron rule. Under-scoped tasks cause excessive inter-task integration overhead. Task decomposition quality depends entirely on the quality of the initial prompt — vague prompts produce vague tasks.
