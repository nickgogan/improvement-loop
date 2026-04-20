---
name: Cloud-Local Plan Handoff (Teleport Pattern)
summary: Bidirectional handoff between cloud and local environments for planning. Plans originate locally and get 'refined' by uploading to cloud for validation, or originate on cloud and get 'teleported
  back' to local terminal for execution. Supports starting a fresh local session with an approved cloud plan.
implementation_notes: Relevant to any architecture where planning and execution happen in different environments.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- anthropic-just-dropped-ultra-plan.md
related_findings:
- file: claude-code-ultra-plan-three-mode-planning.md
  rel: extends
- file: cloud-plan-parallel-multitasking-pattern.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---
# Cloud-Local Plan Handoff (Teleport Pattern)

## What It Is
A bidirectional handoff mechanism between cloud-based planning and local terminal execution in Claude Code. Two directions: local-to-cloud ("Refine with Ultra plan" transports a locally drafted plan to the cloud for validation and critique) and cloud-to-local ("teleport back" brings an approved cloud plan into the local terminal for execution). The cloud-to-local path supports two modes: injecting the plan into the current local session or starting a fresh session with only the approved plan as context.

## Why It Matters
Planning and execution have different optimal environments. Cloud offers faster processing, multi-agent critique, and a web UI for review. Local offers filesystem access, tool execution, and project context. The teleport pattern lets practitioners use the best environment for each phase without manual copy-paste or context reconstruction. Starting a fresh session with an approved plan prevents stale conversation history from contaminating execution.

## Why People Are Using It
Ray Amjad shows the full round-trip: drafting a plan locally, refining it on cloud with inline commenting, then teleporting back for execution. The "start new session" option is highlighted as particularly valuable for keeping execution context clean and focused on the approved plan.

## Potential Improvements
The handoff currently carries the plan text but may lose local context that informed the original plan (e.g., which files were read, what errors were encountered). A richer handoff payload that includes relevant context alongside the plan would reduce re-discovery during execution. Automated validation that the local environment matches plan assumptions (correct branch, required files present) would catch mismatches early.

## Potential Failure Modes
Plans refined on cloud may reference files or patterns the cloud agent inferred but that do not match the actual local project state. The "fresh session" path discards local conversation history, which may contain important context that the plan text alone does not capture. If practitioners rely heavily on cloud refinement, they may develop plans that look good in isolation but fail against real project constraints.
