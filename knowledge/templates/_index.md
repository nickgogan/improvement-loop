---
title: "Template Catalog"
id: "templates-index"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-05"
updated: "2026-04-05"
author: "claude"
source_dd:
  - "DD-109"
tags:
  - "catalog"
  - "template"
  - "moc"
aliases:
  - "Templates MOC"
---

# Templates

Scaffolding templates for projects, skills, agents, and prompts. Consumed by the `/bootstrap` skill and by agents during project creation.

## Template Categories

| Directory | Purpose | DD |
|-----------|---------|-----|
| `project-scaffold/` | Bootstrap manifest schema + project templates | DD-48, DD-109 |
| `agent-templates/` | Agent definition templates | DD-109 |
| `skill-templates/` | Skill definition templates | DD-109 |
| `prompt-templates/` | Prompt templates for different task types | DD-109 |

## Project Scaffold Contents

| File | Purpose |
|------|---------|
| `bootstrap-manifest.schema.json` | JSON Schema defining the manifest format |
| `bootstrap-manifest.example.json` | Example manifest for a mixed-type project |
| `CLAUDE.md.template` | Project CLAUDE.md with `{{VAR}}` placeholders |
| `PROGRESS.md.template` | Project PROGRESS.md with `{{VAR}}` placeholders |
