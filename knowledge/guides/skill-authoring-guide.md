---
title: "SKILL.md Mechanics Reference"
id: "skill-authoring-guide"
type: "guideline"
category: "agent-design"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-07"
updated: "2026-06-20"
author: "claude"
source_dd:
  - "DD-109"
  - "DD-65"
tags:
  - "guide"
  - "skill-design"
  - "claude-code"
  - "reference"
aliases:
  - "SKILL.md format"
  - "SKILL.md frontmatter"
---

# SKILL.md Mechanics Reference

Factual reference for the Claude Code SKILL.md format — frontmatter fields, invocation
control, dynamic context, and variables.

> **Design guidance lives elsewhere.** *How* to scope, name, structure, and gate a skill
> (the Decision sequence, safety-critical classification, output shape) is owned by the
> Librarian skill concept doc and the design skill:
> - `operations/references/librarian/skill.md` §Construction — the authoring Decision sequence.
> - `/design-skill` — drafts a SKILL.md from intent, then delegates audit to `/assess-skill`.
>
> This file is the *syntax cheat-sheet* those consume; it deliberately no longer restates
> design philosophy (superseded session 124 to avoid duplicating the §Construction substrate).

## SKILL.md Structure

```yaml
---
name: kebab-case-name          # becomes /slash-command (max 64 chars)
description: >-                 # front-load the key use case
  What this does. When to use it.
  Truncated at 250 chars in the skill listing.
user-invocable: true            # false = only Claude can invoke (background knowledge)
disable-model-invocation: false # true = only user can invoke (side-effect workflows)
allowed-tools: Read Grep Glob   # tools granted without per-use approval
argument-hint: "[arg]"          # shown during autocomplete
context: fork                   # optional: run in isolated subagent
agent: Explore                  # optional: which subagent type (with context: fork)
---

Markdown instructions here.
```

All frontmatter fields are optional. Only `description` is recommended.

## Supporting files

SKILL.md is the entry point; detailed reference can live beside it and load on demand:

```
my-skill/
├── SKILL.md           # Main instructions (required)
├── reference.md       # Detailed docs (loaded on demand)
└── examples/          # Example outputs
```

Skills load **on demand, not every session** — only the `description` sits in context; full
content loads when invoked. So supporting files cost no tokens until used.

## Invocation Control

| Setting | Who can invoke | Loaded into context? |
|---------|----------------|---------------------|
| Default | User + Claude | Description only |
| `disable-model-invocation: true` | User only | No — fully hidden from Claude |
| `user-invocable: false` | Claude only | Description always loaded |

Use `disable-model-invocation: true` for workflows with side effects (deploy, commit, send messages).

## Dynamic Context

Shell commands run before Claude sees the content:
- Inline: `` !`git status --short` ``
- Block: ` ```! ` fenced code block

## Variables

| Variable | Description |
|----------|-------------|
| `$ARGUMENTS` / `$0`, `$1` | Arguments passed at invocation |
| `${CLAUDE_SKILL_DIR}` | Directory containing the SKILL.md |
| `${CLAUDE_SESSION_ID}` | Current session ID |

## Scope (where a SKILL.md lives)

| Scope | Path | Applies to |
|-------|------|-----------|
| Personal | `~/.claude/skills/` | All projects |
| Cross-system | workspace-root `.claude/skills/` | The whole vault |
| System-specific | `{system}/.claude/skills/` | That system only (DD-109) |
| Project-scoped | `incubator/{project}/.claude/skills/` | That project only |
