---
name: Per-Node Context Scoping (Skills, MCPs, and Commands)
summary: Archon allows specifying which skills, MCP servers, and commands are available at each workflow node. A validation node might load a linting skill, a planning node might connect an MCP server for
  documentation, while an implementation node loads a different skill set. Context is scoped to the step, not the workflow — preventing irrelevant tool/skill context from bloating nodes that do not need
  it.
implementation_notes: null
category: Context Engineering
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
- file: per-node-tool-restrictions-workflow-governance.md
  rel: extends
- file: tiered-context-injection-over-monolithic-files.md
  rel: same-problem
- file: new-chat-per-agent-step-context-hygiene.md
  rel: same-problem
- file: on-demand-vs-always-on-skill-activation.md
  rel: same-problem
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
tags:
- session-95-reextract
---

## What It Is

Beyond per-node model selection and per-node tool restrictions (both already documented), Archon supports specifying which **skills**, **MCP servers**, and **commands** (longer prompt files referenced by path) are loaded at each node. Cole Medin explicitly states: "you get to pick where you're injecting context — maybe you have a skill that you only need during the validation step, or you have an MCP server that you only want during planning."

This creates three dimensions of per-node scoping:
1. **Model** — which LLM processes this node (Haiku, Sonnet, Opus)
2. **Tools** — which tools are allowed/denied at this node (already documented in per-node-tool-restrictions)
3. **Context** — which skills, commands, and MCP servers are loaded into this node's session

The command system uses markdown files stored alongside the workflow YAML. A node references a command file by path (e.g., `command: archon-web-research`), and that file's content becomes the prompt for the node. This separates long prompts from the workflow definition, keeping the YAML readable while allowing rich per-node prompt engineering.

## Why It Matters

This extends the tiered context injection pattern from static instruction files to dynamic workflow execution. In a 10-node workflow, loading all skills and MCP servers into every node wastes context budget and introduces irrelevant instructions that can confuse the agent. Per-node scoping ensures each node gets exactly the context it needs — the "nothing more" principle applied at workflow granularity.

The command file pattern also solves a skill organization problem: complex node prompts can be version-controlled, shared across workflows, and updated independently of the workflow YAML structure.

## Why People Are Using It

Cole Medin shows the fix-GitHub-issue workflow where research nodes use an `archon-web-research` command file, classification nodes use no tools at all, and implementation nodes get full tool access. Each node's context is tailored to its purpose.

## Potential Improvements

- Dependency declarations between command files and the workflows that reference them
- Command file inheritance — a base prompt that all nodes share, with per-node overrides
- Automatic context budget estimation per node based on loaded skills + commands + prompt

## Potential Failure Modes

- Missing command files at runtime cause silent failures
- Over-scoping (loading too many skills into a node) negates the context savings
- Under-scoping (forgetting a needed skill) causes the node to fail in non-obvious ways
