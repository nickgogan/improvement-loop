---
title: "Template Catalog"
id: "templates-index"
type: "governance"
category: "governance"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-05"
updated: "2026-04-05"
author: "claude"
source_dd:
  - "DD-49"
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
| `project-scaffold/` | Bootstrap manifest schema + project templates | DD-48, DD-49 |
| `agent-templates/` | Agent definition templates | DD-49 |
| `skill-templates/` | Skill definition templates | DD-49 |
| `prompt-templates/` | Prompt templates for different task types | DD-49 |

## Project Scaffold Contents

| File | Purpose |
|------|---------|
| `bootstrap-manifest.schema.json` | JSON Schema defining the manifest format |
| `bootstrap-manifest.example.json` | Example manifest for a mixed-type project |
| `CLAUDE.md.template` | Project CLAUDE.md with `{{VAR}}` placeholders |
| `PROGRESS.md.template` | Project PROGRESS.md with `{{VAR}}` placeholders |
