---
name: GitHub Labels as Distributed Workflow State
summary: Using GitHub issue and PR labels as a persistent, distributed state machine for autonomous agent workflows. Labels encode current processing state (in-progress, needs-fixed, needs-human, rate-limited)
  and act as coordination locks — preventing duplicate workflows from firing on the same issue.
implementation_notes: Create a label set covering all workflow states before deploying autonomous workflows. The orchestrator (cron job) reads labels before dispatching — only issues with no factory label
  are eligible for triage; only triage-accepted issues are eligible for implementation. Labels survive system restarts, require no separate state DB, and are visible in the GitHub UI for human monitoring.
  Label `needs-human` after N consecutive failures to create a human escalation path.
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- dark-factory-archon-autonomous-coding.md
related_findings:
- file: dark-factory-ai-only-codebase-management.md
  rel: enabled-by
- file: archon-yaml-defined-harness-workflows.md
  rel: enabled-by
- file: github-actions-cron-as-agent-scheduler.md
  rel: same-problem
- file: effort-scaling-rules-embedded-in-orchestrator.md
  rel: same-problem
- file: atomic-checkout-with-409-exclusion.md
  rel: same-problem
- file: work-ticket-contract-prompt-mode-vs-work-mode.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-07-12'
pipeline_status: classified
consumed_by: []
---

# GitHub Labels as Distributed Workflow State

## What It Is
In an autonomous coding pipeline (dark factory), GitHub issue and PR labels serve as the workflow's persistent state machine. Rather than maintaining a separate database of "what is this issue currently doing," each issue's label set encodes its current state — readable by any workflow, visible to humans in the GitHub UI, and durable across restarts.

Cole Medin's dark factory label design:

| Label | State Meaning |
|-------|--------------|
| `factory-accepted` | Triage workflow classified as in-scope |
| `factory-rejected` | Triage workflow classified as out-of-scope |
| `in-progress` | Implementation workflow is currently running |
| `needs-fixed` | Implementation failed; awaiting retry or human |
| `needs-human` | Failed 2+ times or classifier flagged as ambiguous; requires human review |
| `factory-rate-limit` | Daily token/API spend limit reached; pause until next day |

The orchestrator (a cron job) reads these labels before dispatching workflows:
- No factory label → eligible for triage
- `factory-accepted` + no `in-progress` → eligible for implementation  
- `in-progress` → skip (already being processed)
- `needs-human` → skip (human must clear the label)
- `factory-rate-limit` → skip all workflows until label is cleared

The triage workflow's agentic classification node (LLM) produces a verdict, but a separate deterministic node applies the label programmatically — separating the "decide" step from the "act" step for reliability.

## Why It Matters
Distributed autonomous systems need coordination primitives. Without a shared state store, two orchestrator cron cycles could simultaneously dispatch implementation workflows for the same issue, wasting tokens and creating merge conflicts. GitHub labels solve this without requiring a separate database: they are the canonical state, not a reflection of it.

The pattern also provides free observability: a human scanning the GitHub issues page can immediately see the full workflow state of every issue — what's in flight, what failed, what needs attention. No dashboard required.

## Why People Are Using It
GitHub is already the source of truth for issues and PRs in any code-based dark factory. Labels are a native GitHub primitive — no additional tooling, webhooks, or infrastructure needed. The state is co-located with the work items themselves.

StrongDM uses a similar label/status approach in their production dark factory. Cole Medin derived this label schema by studying StrongDM's architecture and adapting it for Archon-based workflows.

## Potential Improvements
- Add a `factory-approved` label for issues that a human has manually approved for implementation (bypassing triage) — supports hybrid human + factory workflows
- Use label creation timestamps to detect stale `in-progress` labels (workflow died without cleanup) and auto-clear them after a timeout
- Expose label state changes via GitHub webhook to a monitoring dashboard for real-time pipeline visibility

## Potential Failure Modes
- Orphaned `in-progress` labels if a workflow crashes without cleanup — orchestrator will skip those issues forever without a timeout/cleanup mechanism
- Label namespace collision if the repo is used for non-factory purposes (human engineers may misinterpret or accidentally apply factory labels)
- GitHub API rate limits under high-volume label operations (100+ issues per triage cycle)
- Race condition: two orchestrator cycles start simultaneously and both read `no label` before either applies `in-progress`
