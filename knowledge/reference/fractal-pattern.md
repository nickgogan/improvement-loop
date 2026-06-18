---
title: "Fractal Unit Pattern"
id: "fractal-pattern"
type: "governance"
category: "project-lifecycle"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-05"
updated: "2026-04-05"
author: "nick"
source_dd: []
tags:
  - "fractal"
  - "structure"
  - "architecture"
  - "agentic-layer"
aliases:
  - "Unit Pattern"
  - "Standard Project Structure"
---

# Fractal Unit Pattern

Every system, incubator project, and graduated area follows the same 7-folder structure. This predictable shape means agents know where to find things, new projects bootstrap consistently, and the entire MetaSystem is navigable at any scale.

---

## The Canonical Structure

```
{unit}/
  CLAUDE.md               # REQUIRED — identity, scope, constraints

  app/                    # The product — source code, configs, deployments
  governance/             # Rules, constraints, applicable DDs
  knowledge/              # The knowledge vault
    patterns/             #   Reusable approaches
    guides/               #   How-to documentation, playbooks
    templates/            #   Scaffolding
    reference/            #   Active read-only context
  agents/                 # The agentic layer — team members
    {agent-name}/         #   Each agent is a directory
      skills/
      workflows/
      hooks/
  project-management/     # Requirements, milestones, progress
  operations/             # Errors, events, lessons, logs
  archive/                # Completed/retired work
```

---

## Folder Purposes

| Folder | Purpose | Build-time | Run-time |
|--------|---------|-----------|----------|
| **app/** | The actual product | Source code, build configs | Deployed artifacts |
| **governance/** | Rules and constraints | Applicable DDs, unit rules | Unchanged |
| **knowledge/** | Distilled knowledge | Patterns, guides, templates, reference | Growing library |
| **agents/** | The team | Agent defs, skills, workflows, hooks | Active agents |
| **project-management/** | Tracking | Plans, requirements, milestones | Progress tracking |
| **operations/** | Runtime concerns | Error tracking, build logs | Event tracking (message bus), lessons learned |
| **archive/** | History | — | Completed/retired work |

---

## Knowledge Vault Subdirectories

| Directory | Contains | Example |
|-----------|----------|---------|
| **patterns/** | Reusable approaches — what to do, not how | "Review Gate Pattern", "Agent Handoff Pattern" |
| **guides/** | How-to documentation and playbooks | "How to Write a Build Spec", "Notion MCP Error Recovery" |
| **templates/** | Scaffolding files for this unit's artifacts | Build spec template, agent definition template |
| **reference/** | Active read-only context material | System boundary docs, design context summaries |

---

## The Agentic Layer

The `agents/` directory is the primary interface for all work within a unit. Each agent is a "team member" with its own:

- **skills/** — capabilities the agent can execute
- **workflows/** — multi-step sequences
- **hooks/** — triggers and automations

**Principle:** Everything goes through agents whenever possible. Raw Claude Code should not directly modify system internals. Agents provide identity, scope boundaries, and auditable workflows.

**Relationship to `.claude/agents/`:** The `.claude/agents/` directory holds engine-facing definitions (subagent files consumed by Claude Code's harness). The fractal `agents/` directory holds richer team-member context. The engine definition is a subset of the full agent description.

---

## Operations as Communication Layer

The `operations/` directory serves dual purposes:

**During build:**
- Error tracking (structured error database)
- Build logs and session records

**During runtime:**
- Event tracking — can serve as a message bus between agents
- Lessons learned — post-mortems, retrospectives
- Runtime logs

---

## Relationship to Engine Directories

Some fractal folders coexist with Claude Code engine directories:

| Fractal folder | Engine directory | Relationship |
|---------------|-----------------|--------------|
| agents/ | .claude/agents/ | agents/ holds full context; .claude/agents/ holds engine-facing definitions |
| project-management/ | .planning/ | project-management/ is the fractal-standard view; .planning/ is the GSD engine directory |
| governance/ | .claude/rules/ | governance/ holds human-readable docs; .claude/rules/ holds engine-facing rules |

Both coexist. The fractal folder is the canonical, human-and-agent-readable location. The engine directory is consumed by specific tooling.

---

## Exemptions

- Units may have additional directories beyond the 7 standard folders for unit-specific operational needs

---

## All Content Files Use Vault Frontmatter

Every markdown content file (except CLAUDE.md and `_index.md` catalogs) carries YAML frontmatter defined in `_schema.yaml` at the workspace root. This enables:
- Obsidian Dataview queries across the vault
- Future MongoDB backing for programmatic queries
- Consistent metadata for agent consumption

---

*This pattern is a Design Decision candidate. See PROGRESS.md for tracking.*
