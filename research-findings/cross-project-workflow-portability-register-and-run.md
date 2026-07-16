---
name: 'Cross-Project Workflow Portability: Register and Run'
summary: Archon workflows are project-agnostic by design. Define a workflow once, register any number of repositories, and run the same workflow across all of them. Workflows ship bundled with the CLI (not
  per-project), and new repos are auto-registered on first workflow run. The workflow definition is decoupled from the target codebase.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- archon-open-source-harness-builder.md
related_findings:
- file: archon-yaml-defined-harness-workflows.md
  rel: extends
- file: skills-portability-across-sdk-and-framework-boundaries.md
  rel: same-problem
- file: multi-ide-portability-via-installer-templates.md
  rel: same-problem
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
tags:
- session-95-reextract
---

## What It Is

Archon's workflows live in the `.archon/` folder within the Archon repo itself — not in any target project. When the CLI runs, all default workflows plus custom workflows are available regardless of which project is targeted. Projects are registered as "Archon projects" either during setup, through the web UI's "add project" button, or automatically on first CLI invocation from a new repo.

The architecture separates three concerns:
1. **Workflow definitions** — live in Archon's repo, shared across all projects
2. **Project registration** — a lightweight record (local path or GitHub URL) stored in Archon's database (SQLite/Postgres)
3. **Workflow execution** — the CLI targets a registered project and runs a workflow against it

This means a "fix GitHub issue" workflow written once works identically across a React app, a Python service, and a Go CLI — because the workflow nodes contain generic prompts (investigate, implement, validate) that the coding agent interprets in context of the target codebase.

## Why It Matters

Without portability, workflow definitions become repo-coupled: you write a workflow for Project A, then copy and modify it for Project B. This is the same problem that afflicts project-specific CI/CD configurations. Archon's design avoids this by making workflows inherently portable — the target codebase is a runtime parameter, not a build-time dependency.

For organizations managing multiple codebases, this creates a "define standards once" capability: the team's approved development workflow (plan, implement, test, review, PR) is encoded as an Archon workflow and applied uniformly across all projects.

## Why People Are Using It

Cole Medin demonstrates running the same fix-GitHub-issue workflow across multiple repos without modification. The web UI shows a project dropdown for selecting which registered project to target, while the workflow dropdown shows all available workflows regardless of project selection.

## Potential Improvements

- Project-specific workflow overrides (e.g., a Python project might add a mypy node to the validation step)
- Workflow-project compatibility metadata (e.g., this workflow requires a package.json)
- Workflow versioning so project-specific overrides don't block upstream workflow updates

## Potential Failure Modes

- Generic workflows may miss project-specific validation requirements (e.g., no type checking in a TypeScript project if the workflow only runs generic tests)
- Workflow prompts that assume specific project structures (e.g., referencing `src/`) fail on non-conforming repos
- Project registration state drift — registered paths become stale if repos move
