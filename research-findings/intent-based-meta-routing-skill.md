---
name: Intent-Based Meta-Routing Skill
summary: 'Archon''s archon-dev skill acts as a meta-router: it inspects user input keywords and dispatches to one of 10 specialized cookbooks. This is intent classification implemented as a routing table
  in markdown, not code. Each cookbook is a self-contained workflow for a specific development task.'
implementation_notes: null
category: Intent Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
related_findings:
- file: context-aware-routing-skill-classifier-sub-skill.md
  rel: same-problem
- file: archon-yaml-defined-harness-workflows.md
  rel: extends
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
  - "writing-agent-specifications.md"
---

## What It Is

Archon's `archon-dev` skill is a SKILL.md file that acts as a **meta-router** — instead of containing a single workflow, it inspects user intent via keyword matching and dispatches to one of 10 specialized cookbook files:

- Research → research cookbook
- Plan → planning cookbook
- Implement → implementation cookbook
- Review → code review cookbook
- Debug → debugging cookbook
- Test → testing cookbook
- etc.

Each cookbook is a self-contained markdown file with a focused workflow for that specific development task. The meta-router skill is essentially an intent classifier built as a routing table in markdown — no code, no AI classification call, just keyword-to-file mapping.

This is context loading optimized by intent: instead of loading everything (or loading nothing and discovering later), the meta-router loads exactly the one relevant cookbook based on what the developer is trying to do.

## Why It Matters

As skill libraries grow, the "which skill should I use?" problem becomes a real UX issue. A developer shouldn't need to know that the debugging procedure lives in cookbook 7. The meta-routing pattern lets them express intent naturally ("I need to debug this") and the router selects the right context.

This pattern differs from AI-based intent classification (which is slower and less deterministic) and from manual skill selection (which requires the user to know the skill catalog). It's a lightweight middle ground: deterministic keyword matching in markdown.

## Why People Are Using It

Observed in [Archon](https://github.com/coleam00/archon) v0.3.2 — see [[archon-analysis]] for structural details. The `archon-dev` SKILL.md routes to 10 specialized cookbooks in `.claude/skills/archon-dev/cookbooks/`. Each cookbook averages several hundred lines of focused instructions for a specific development task.

## Potential Alternatives

AI-powered intent classification (more flexible but non-deterministic). Flat skill catalog with explicit user selection. Hierarchical skill menus (multi-step selection).

## Potential Improvements

Fuzzy matching beyond exact keywords. Fallback to AI classification when no keywords match. Cookbook discovery mechanism so new cookbooks register themselves in the routing table automatically.

## Potential Failure Modes

Keyword collisions where user input matches multiple cookbooks. Missing keywords for valid intents. Maintenance burden when adding new cookbooks requires updating the routing table.
