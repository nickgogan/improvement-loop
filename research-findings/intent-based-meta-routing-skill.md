---
name: Intent-Based Meta-Routing Skill
summary: 'Archon''s archon-dev skill acts as a meta-router: it inspects user input keywords and dispatches to one of 10 specialized cookbooks. This is intent classification implemented as a routing table
  in markdown, not code. Each cookbook is a self-contained workflow for a specific development task.'
implementation_notes: '2026-07-12 annotation: the thin-router pattern this finding describes at skill level

  is now corroborated at the root-context-file level across multiple independent

  channels (Archon/Cole Medin cookbook routing; Jake Van Clief task-to-file tables;

  AI Code That Works "routes, does not contain" root router; Nate Herk CLAUDE.md

  routing rules). Flagged as a /reassess-priorities candidate on evidence-accumulation

  grounds (priority unchanged here — reassessment is the Curator''s call).'
category: Intent Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- every-level-of-a-claude-second-brain-explained.md
- the-folder-structure-that-makes-ai-build-better-software.md
related_findings:
- file: context-aware-routing-skill-classifier-sub-skill.md
  rel: same-problem
- file: archon-yaml-defined-harness-workflows.md
  rel: extends
- file: task-to-file-routing-table-in-context-files.md
  rel: same-problem
- file: claudemd-as-knowledge-base-traversal-guide.md
  rel: same-problem
- file: escalating-search-order-routing.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- writing-agent-specifications.md
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

**2026-07 corroboration (independent channels, root-file altitude):** the identical
mechanism — a deterministic markdown routing table dispatching intent to focused
context files — recurs as the load-bearing pattern in two more independent sources.
AI Code That Works ("The Folder Structure That Makes AI Build Better Software"): the
root CLAUDE.md "routes, it does not contain... a little table: kind of work on the
left, the file to read first on the right" — the front desk that knows which floor to
send you to, capped at ~200 lines. Nate Herk ("Every Level of a Claude Second Brain
Explained"): CLAUDE.md as router with where-things-live rules ("if you need
information about our quarter one priorities, look in this folder"), naming missing
routing — not model quality — as the reason agents ask for context they already have
on disk. Together with Jake Van Clief's task-to-file routing tables, the thin-router
pattern now spans skill-level and root-context-file-level implementations across
multiple independent channels.

## Potential Alternatives

AI-powered intent classification (more flexible but non-deterministic). Flat skill catalog with explicit user selection. Hierarchical skill menus (multi-step selection).

## Potential Improvements

Fuzzy matching beyond exact keywords. Fallback to AI classification when no keywords match. Cookbook discovery mechanism so new cookbooks register themselves in the routing table automatically.

## Potential Failure Modes

Keyword collisions where user input matches multiple cookbooks. Missing keywords for valid intents. Maintenance burden when adding new cookbooks requires updating the routing table.
