---
name: "Plugin Namespacing for Organizational Context"
summary: "n8n uses .claude/plugins/n8n/ with an n8n: prefix for all skills, commands, and agents — preventing collisions in large teams where multiple developers might have personal Claude Code plugins. The plugin system auto-discovers and namespace-prefixes all items."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: null
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources: []
related_findings:
  - {file: "monorepo-context-distribution-three-strategies.md", rel: "same-problem"}
  - {file: "skills-inside-workspace-contextual-skill.md", rel: "extends"}
proposals: null
date_discovered: "2026-04-09"
last_updated: "2026-04-09"
pipeline_status: "raw"
consumed_by: []
---

## What It Is

n8n places all Claude Code customizations in `.claude/plugins/n8n/` rather than directly in `.claude/`. This creates a colon-namespaced prefix — skills become `/n8n:create-pr`, agents become `n8n:developer`, commands become `/n8n:plan`. The plugin directory contains 2 agents, 2 commands, and 11 skills, all auto-discovered and prefixed by the Claude Code plugin system.

The namespace prevents collisions: a developer with a personal `/create-pr` skill won't conflict with the project's `/n8n:create-pr`. In large teams where developers bring their own Claude Code configurations, this organizational convention keeps project-level and personal customizations cleanly separated.

## Why It Matters

As Claude Code adoption grows in large organizations, the "whose skill is this?" problem becomes real. Without namespacing, a team member's personal skill named `/plan` would shadow the project's `/plan`. The plugin pattern solves this by scoping project customizations under a project-specific prefix, leaving the root namespace for personal tools.

This is also a documentation signal — seeing `/n8n:create-pr` immediately communicates that this is a project-specific skill, not a personal one or a Claude Code built-in.

## Why People Are Using It

Observed in [n8n](https://github.com/n8n-io/n8n) v2.16.0 — see [[n8n-analysis]] for structural details. n8n's plugin contains 2 specialist agents (developer, linear-issue-triager), 2 commands (plan, triage), and 11 skills covering development workflows from bug reproduction to PR creation.

Known limitation: requires omitting the `name` field from SKILL.md frontmatter due to a Claude Code bug where the name field overrides the namespace prefix.

## Potential Alternatives

Flat `.claude/` directory with naming conventions (e.g., `n8n-create-pr` prefix). Separate `.claude/` directories per team member. No namespacing — rely on convention to avoid collisions.

## Potential Improvements

Multi-level namespacing for organizations with multiple projects (e.g., `org:project:skill`). Plugin versioning for tracking which version of project skills a developer is using.

## Potential Failure Modes

Namespace prefix adds typing friction (users must type `n8n:` prefix). Plugin discovery issues if the directory structure doesn't match Claude Code expectations. The known bug requiring `name` field omission.
