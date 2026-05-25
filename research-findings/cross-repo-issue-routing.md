---
name: Cross-Repo Issue Routing
summary: Pattern-based routing of issues/tasks across repository boundaries via configuration files. External dependencies tracked as typed references. Hydration pulls related issues from other repos for
  context.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: Not Flagged
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
pipeline_status: "classified"
---

## What It Is

A routing mechanism that enables issues/tasks to flow across repository boundaries via pattern rules defined in a configuration file (`.beads/routes.jsonl`). Cross-repo dependencies are tracked as typed references (`external:<repo>/<id>`). A hydration command (`bd hydrate`) pulls related issues from other repos into the local context, enabling agents to reason about cross-repo dependencies without switching contexts.

## Why It Matters

Most agent task systems are repo-scoped — issues in repo A have no awareness of issues in repo B. For multi-repo projects (like MetaSystem with its incubator/ and systems/ separation), cross-repo routing enables coordinated work without manual context switching. This is especially relevant as agent teams scale to work across multiple codebases.

## Why People Are Using It

Observed in [Beads](https://github.com/gastownhall/beads) v1.0.2 — see [[beads-analysis]] for structural details. Beads implements routing via `.beads/routes.jsonl` pattern rules, `external:<repo>/<id>` dependency references, and `bd hydrate` for cross-repo context loading.

## Potential Alternatives

- Monorepo approach (avoid cross-repo by consolidating)
- Manual cross-referencing via issue comments
- External issue trackers (Linear, Jira) as the cross-repo layer

## Potential Improvements

Could be extended with routing rules based on dimension/category tags, enabling automatic routing of research findings to the most relevant system.

## Potential Failure Modes

- Stale cross-repo references when the target repo evolves
- Network dependency for hydration (requires access to remote repos)
- Routing rule complexity can grow with many repos
