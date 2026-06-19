---
title: "Skill Authoring Best Practices"
id: "skill-authoring-guide"
type: "guideline"
category: "agent-design"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-07"
updated: "2026-04-07"
author: "claude"
source_dd:
  - "DD-34"
  - "DD-49"
  - "DD-65"
tags:
  - "guide"
  - "skill-design"
  - "agent-design"
  - "claude-code"
aliases:
  - "How to write skills"
  - "SKILL.md format"
---

# Skill Authoring Best Practices

Reference for writing skills in MetaSystem. Synthesized from Anthropic's official guide (code.claude.com/docs/en/skills) and research findings (skill-as-new-employee, skills-as-SOPs, skills-2.0-lifecycle, skill-chaining, global-vs-project-scoping).

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

## Mental Model: New Employee Onboarding

Design a skill as if writing an onboarding doc for a new hire:
1. **Purpose** — what the process accomplishes
2. **Triggering conditions** — when to invoke it and what context is needed
3. **Step-by-step execution** — with branching logic
4. **Policies and constraints** — compliance rules, tone, escalation triggers
5. **Expected output** — precise format and content

## Key Principles

**Keep SKILL.md under 500 lines.** Move detailed reference to supporting files:
```
my-skill/
├── SKILL.md           # Main instructions (required)
├── reference.md       # Detailed docs (loaded on demand)
└── examples/          # Example outputs
```

**Description is the routing mechanism.** Claude uses it to decide when to auto-load. Front-load keywords users would naturally say. Don't waste characters on generic phrasing.

**Skills are SOPs, not suggestions.** Encode the complete workflow: steps, tools, format, preferences. A skill perfected once is available forever at near-zero prompting cost.

**Skills are loaded on demand, not every session.** Only the description loads into context. Full content loads when invoked. So skill files can be detailed — they don't cost tokens until used.

**Scope strategically.** Personal skills (`~/.claude/skills/`) apply to all projects. Project skills (`.claude/skills/`) apply to this project only. Don't put project-specific skills at global scope.

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
