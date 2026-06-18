---
name: "Multi-Adapter Workflow Invocation (CLI, Web UI, Chat, GitHub)"
summary: "Archon provides multiple invocation surfaces for the same workflow: CLI (from within a coding agent session), web UI (browser dashboard), GitHub (comment @archon on an issue), Slack, and Telegram. All adapters trigger the same underlying workflow DAG. The pattern decouples workflow definition from invocation surface, enabling both developer-initiated and event-triggered execution."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "archon-open-source-harness-builder.md"
related_findings:
  - file: "archon-yaml-defined-harness-workflows.md"
    rel: "extends"
  - file: "claude-routines-webhook-triggered-pipeline-chaining.md"
    rel: "same-problem"
  - file: "scheduled-skill-chaining-with-file-based-activation.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
---

## What It Is

Archon decouples workflow definition from invocation surface. The same workflow YAML can be triggered through:

1. **CLI** — invoked from within a Claude Code session (e.g., "use Archon to fix issue #5"), runs as a background process the agent can monitor
2. **Web UI** — a browser-based dashboard where users select projects and workflows, chat with the Archon agent, and monitor execution with live log streaming and DAG visualization
3. **GitHub** — comment `@archon` on a GitHub issue to trigger a workflow
4. **Slack** — message a Slack bot to dispatch workflows
5. **Telegram** — message a Telegram bot for workflow dispatch

All adapters feed into the same execution engine and produce the same outputs (e.g., PRs, comments). The web UI adds observability features: live DAG progress visualization, per-node log streaming, and a conversation interface where the Archon agent has project/workflow context pre-injected.

The architecture means a workflow can be triggered by a human (CLI, web UI), by an event (GitHub comment), or by a scheduled job (cron on a VPS dispatching CLI commands). The same workflow definition serves all three trigger patterns.

## Why It Matters

Different stakeholders prefer different invocation surfaces. A developer in their IDE wants CLI invocation. A project manager wants a web dashboard. An automated pipeline wants event-triggered dispatch. By decoupling definition from invocation, the workflow investment is amortized across all surfaces — you define the workflow once and get access from everywhere.

The event-triggered patterns (GitHub comment, Slack message) are particularly significant because they enable **non-developer stakeholders** to trigger AI workflows. A QA engineer can comment `@archon` on a bug report; a project manager can message Slack to generate a PRD. The workflow handles the technical complexity.

## Why People Are Using It

Cole Medin demonstrates both CLI and web UI invocation of the same fix-GitHub-issue workflow, showing identical results from different surfaces. The GitHub adapter specifically enables "dark factory" patterns where issues are auto-triaged and fixed without developer intervention.

## Potential Improvements

- Adapter-specific input validation (GitHub comments may contain different metadata than CLI invocations)
- Unified notification: regardless of invocation surface, send completion notifications to a configured channel
- Adapter priority for conflicting invocations (if both a CLI user and a GitHub comment trigger the same workflow for the same issue)

## Potential Failure Modes

- Adapter-specific bugs that only manifest on one surface (e.g., GitHub comment parsing fails on edge-case issue bodies)
- Security surface expansion — each adapter is a new entry point that must be secured
- Context quality varies by adapter — CLI invocations from a coding agent session have richer project context than a Telegram message
