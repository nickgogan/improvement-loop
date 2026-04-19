---
notion_id: 32b1e08b-9b34-81bc-8751-ee55413be31a
name: Global vs. Project-Level Skill and Context Scoping
summary: Claude Code and most agent harnesses support both global (applies to all projects) and project-level (applies only to the current folder) scoping for skills, CLAUDE.md files, and MCP connectors.
  Strategic scoping prevents irrelevant skills from cluttering context across roles.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- building-ai-agents-that-actually-work-full-course.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-08'
related_findings:
- file: context-engineering-supersedes-prompt-engineering.md
  rel: extends
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: aios-architecture-folder-per-role-agent.md
  rel: same-problem
pipeline_status: "raw"
consumed_by: []
---
# Global vs. Project-Level Skill and Context Scoping

## What It Is
Users can place skills, MCPs, and CLAUDE.md files at a global level (applying to every project session) or at the project/folder level (applying only when that folder is the active workspace). For example, a 'truncate' skill (shorten text without compressing meaning) belongs at global level since it's universally useful. A 'Sebastian refer' skill (specific to a single contact) belongs at project level since it's relevant only to the executive assistant context. This mirrors the global vs. project distinction for CLAUDE.md files.

## Why It Matters
Without strategic scoping, all skills load into every session, recreating the same context bloat problem that a flat CLAUDE.md creates. Proper scoping ensures each agent role only loads the capabilities it actually needs, maintaining focused, efficient context windows.

## Why People Are Using It
Power users managing multiple AI roles (executive assistant, head of marketing, developer, content team) with different skill sets and tool access requirements benefit most from strict scoping discipline.

## Potential Alternatives
Carl's domain-based loading as an alternative approach to the same problem; dedicated CLAUDE.md per project that explicitly lists allowed skills; agent harnesses with built-in role isolation.

## Potential Improvements
An audit tool that shows which skills and MCPs are currently loaded in a session would make scope management more visible. Auto-suggestions for moving project-level skills to global (or vice versa) based on usage patterns would help maintenance.

## Potential Failure Modes
Skills mistakenly added to global scope bloat every session. Conversely, skills needed across multiple projects but scoped per-project create maintenance burden when the process changes and all copies must be updated.
