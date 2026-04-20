---
name: Brownfield-Aware Agent Variants for Legacy Codebases
summary: Dedicated brownfield variants of PM and Architect agents that include additional steps for understanding existing code, identifying constraints, and planning changes that respect the current system
  state -- distinct from greenfield workflows.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- bmad-method-masterclass.md
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
pipeline_status: raw
consumed_by: []
---

## What It Is

The BMad Method provides distinct agent workflow variants for brownfield (existing codebase) vs. greenfield (new project) development:

- **Brownfield PRD**: Additional steps where the PM agent absorbs context about the existing application -- its current architecture, known issues, existing user base, and technical debt -- before generating requirements
- **Brownfield Architecture**: The Architect agent performs research on the existing project structure, dependencies, and constraints before proposing changes. This feeds into architecture decisions that must be compatible with (not replace) the existing system
- **Analyst-driven context gathering**: The Business Analyst performs competitive analysis and existing-system assessment to build understanding before any planning begins

Brian's analogy: "Greenfield means you're looking out on a clean green pasture... A brownfield is where all the [waste] has flowed. It's a cesspool. Maybe it's an existing application that's existed for months or years."

The practical difference: brownfield variants add a context-gathering phase before the standard workflow, ensuring agents understand what exists before proposing what to build.

## Why It Matters

Most real-world development is brownfield -- modifying, extending, or fixing existing systems. Agents that assume a clean slate produce architectures and stories that conflict with existing code. The brownfield variants force the agent to read and understand before proposing.

## Why People Are Using It

BMad Method includes brownfield as a first-class workflow, not an afterthought. This addresses a common complaint that agentic coding tools assume new projects.

## Potential Improvements

Automated codebase analysis (dependency graphs, test coverage maps) could feed brownfield context automatically. Integration with git history analysis for understanding project evolution.

## Potential Failure Modes

Brownfield context can be massive -- risk of context window exhaustion before any actual planning begins. Agent may over-respect existing patterns that should actually be refactored.
