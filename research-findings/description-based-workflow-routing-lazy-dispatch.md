---
name: Description-Based Workflow Routing with Lazy YAML Loading
summary: Archon workflow YAML files include a brief description field that the coding agent reads first to determine which workflow matches the user's intent. The full YAML is only loaded after the routing
  decision. The agent never sees every workflow definition — it matches intent against short descriptions, then loads the selected workflow. Paired with a skill file copied into target repos so the coding
  agent knows how to invoke the Archon CLI.
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
- file: tiered-context-injection-over-monolithic-files.md
  rel: same-problem
- file: context-aware-routing-skill-classifier-sub-skill.md
  rel: same-problem
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- production-agent-execution.md
tags:
- session-95-reextract
---

## What It Is

Archon workflows are YAML files, each with a `description` field at the top — a brief natural-language summary of what the workflow does and when to use it (e.g., "use this workflow when the user asks to fix a GitHub issue"). When a user says "use Archon to fix issue #5," the coding agent loads the Archon skill, reads only the descriptions of available workflows, selects the best match, and then loads and executes that specific workflow's full YAML. The full node-by-node definition is never loaded into context until routing is complete.

This is paired with a **skill integration pattern**: Archon ships a skill file (`.claude/skills/archon/`) that gets copied into any target repository. This skill teaches the coding agent how to discover available workflows, invoke the Archon CLI, and monitor background processes. The skill acts as the glue between the coding agent's native skill system and the external workflow orchestrator.

## Why It Matters

Context budget is finite. Loading all workflow definitions into context at once wastes tokens on irrelevant workflows. The description-first routing pattern applies the same lazy-loading principle that tiered context injection uses for instructions — only load what you need, when you need it. The skill integration pattern solves the adoption barrier: the coding agent doesn't need to understand Archon's internals; it only needs to know the CLI invocation patterns, which the skill file provides.

This is a reusable architectural pattern for any system that offers multiple workflows or processes: provide a lightweight routing layer (descriptions) that fits in context cheaply, and defer the full specification loading until after selection.

## Why People Are Using It

Cole Medin demonstrates this in Archon's default setup: after installing Archon and copying the skill into a target repo, the user simply says "use Archon to fix issue #1" — the agent routes to the correct workflow without any manual workflow selection. The web UI also leverages this: the Archon agent has project and workflow context injected at conversation start, enabling natural-language workflow invocation.

## Potential Improvements

- Confidence scoring on the routing decision, with fallback to human selection when ambiguous
- Description versioning as workflows evolve
- Multi-workflow suggestion when a task could plausibly match several workflows

## Potential Failure Modes

- Ambiguous descriptions cause misrouting to the wrong workflow
- Description drift — the description no longer accurately reflects what the workflow does after edits to the YAML body
- The skill file in target repos requires manual updates when Archon's CLI interface changes
