---
name: Visual Skills Management and Meta-Skill Creator
summary: A dashboard that renders all agent skills as browsable, searchable, editable cards with live markdown preview. Includes a meta-skill creator that generates new skills from descriptions, GitHub
  references, or uploaded files, adapting them to the local agent OS.
implementation_notes: null
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- stop-using-claude-code-in-terminal.md
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
related_findings:
- file: agent-management-tool-landscape-2026.md
  rel: same-problem
- file: meta-skill-for-skill-authorship.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---

## What It Is

A web dashboard layer for managing agent skills that provides: (1) browsable, searchable skill cards organized by category, (2) rendered markdown preview of skill files and their reference documents, (3) inline editing that writes directly to the underlying SKILL.md files, and (4) a meta-skill creator that generates new skills from a description, a GitHub reference URL, or an uploaded skill file -- adapting them to fit the local agent OS conventions.

Documented by Simon Scrapes. The system shows 21+ installed skills, allows category filtering, and provides real-time markdown preview that is significantly more readable than raw .md files in VS Code. Changes made in the dashboard are immediately reflected in the underlying file system.

## Why It Matters

Skills in Claude Code are stored as markdown files buried in nested directories (.claude/skills/skill-name/SKILL.md). Discovering, comparing, and editing them requires navigating file trees. For non-technical users or business owners, this is a barrier. The dashboard makes the skill library a first-class visible asset rather than hidden infrastructure. The meta-skill creator lowers the barrier to skill creation by leveraging Anthropic's skill creator pattern with local OS adaptations.

## Why People Are Using It

Practitioners with 20+ skills installed lose track of what exists. The visual interface serves as both a discovery mechanism (what skills do I have?) and a maintenance tool (is this skill still current?). The meta-skill creator enables skill adoption from community sources without manual file creation.

## Potential Improvements

Could integrate with MetaSystem's existing skill architecture. Skill health metrics (last used, success rate, token cost) would add an evaluation dimension. Version history for skill edits would enable rollback. Skill dependency mapping would show which skills reference or chain to others.

## Potential Failure Modes

Dashboard editing bypasses version control -- changes are immediate without git commit history. The meta-skill creator may produce skills that look valid but have subtle issues (wrong file paths, incorrect tool references) that only surface at runtime. Over-reliance on visual management could lead to skill sprawl -- easy creation without corresponding pruning discipline.
