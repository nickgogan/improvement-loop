---
name: MCP Async Task Model (Call-Now-Fetch-Later)
summary: MCP supports returning task handles immediately while work continues asynchronously. Tasks move through states (working, input_required, completed, failed, cancelled). Combined with server-side
  agent loops, servers can spawn internal agents and coordinate complex background workflows using standard MCP primitives.
implementation_notes: Enables long-running research or build tasks to execute asynchronously. When MetaSystem moves to autonomous background agents (e.g., Kairos daemon pattern), MCP async tasks provide
  the protocol-level support for non-blocking execution.
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- mcp-everything-your-team-needs-to-know-workos.md
related_findings:
- file: mcp-session-scoped-authorization.md
  rel: same-problem
- file: kairos-autonomous-background-daemon.md
  rel: same-problem
- file: session-persistence-crash-resilient.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: raw
consumed_by: []
---
# MCP Async Task Model (Call-Now-Fetch-Later)

## What It Is
Requests can return task handles immediately while real work continues asynchronously. Tasks move through defined states: working, input_required, completed, failed, cancelled. Clients poll or subscribe for updates. Combined with server-side agent loops, servers can spawn internal agents, coordinate their work, and deliver results using standard MCP primitives -- enabling complex background workflows without custom orchestration.

## Why It Matters
Unblocks operations exceeding millisecond timeframes: ETL jobs, file conversions, multi-step provisioning, research workflows. Centralizes business logic on the backend while exposing it through a simple protocol interface. This is the infrastructure required for non-blocking agent workflows.

## Why People Are Using It
Part of the MCP 2026 spec. Addresses the fundamental limitation of synchronous tool calls in long-running agent workflows.

## Potential Improvements
Standardized timeout guarantees. Progress reporting (percentage complete) beyond binary state transitions. Priority queuing for task handles.

## Potential Failure Modes
Clients must implement polling/subscription logic. No built-in timeout guarantees -- runaway tasks can consume resources indefinitely. Server-side agent loops require servers to implement sampling and tool definitions internally, adding complexity.
