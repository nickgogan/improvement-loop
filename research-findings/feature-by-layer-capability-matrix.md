---
name: "Feature-by-Layer Capability Matrix in Agent-Addressed Context Files"
summary: "A documentation pattern for compressing a large tool/capability surface into a navigable grid inside an agent-addressed context file (CLAUDE.md, AGENTS.md, or equivalent). Rows are features; columns are consumer layers (core library, facade, HTTP API, MCP tool, client SDK, SDK tool helper, etc.). Each cell names the specific file, method, or tool-name at that layer. One table replaces many lines of scattered documentation and lets agents navigate 'feature X, layer Y' lookups in one hop."
implementation_notes: "Directly adoptable for any MetaSystem surface with a large feature × layer matrix — e.g., the IL skill set × user-invocation/subagent-invocation/chained-invocation, or the Librarian reference layer × Tier-1/Tier-2/Tier-3 access mode. Especially valuable when an agent-addressed file needs to expose the full shape of a complex capability surface in scannable form."
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: null
applicability:
  - "General"
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-23"
pipeline_status: raw
consumed_by: []
tags:
  - "context-engineering"
  - "claude-md"
  - "capability-documentation"
  - "memongo"
---

# Feature-by-Layer Capability Matrix in Agent-Addressed Context Files

## What It Is

A table inside an agent-addressed context file (CLAUDE.md / AGENTS.md / equivalent) where rows are features and columns are consumer layers. Each cell names the concrete file, function, HTTP route, or tool-name exposing that feature at that layer.

Memongo's instance:

| Feature | Key file | Layers |
|---|---|---|
| Reasoning chain traversal | `packages/memory-engine/src/mongodb-reasoning-chain.ts` | Engine, Bridge (`memongoBridgeTraceChain`), API (`POST /v1/chain-trace`), MCP (`memongo_chain_trace`), Client (`.traceChain()`), AI SDK (`memongo_chain_trace`) |
| Surprisal novelty detection | `packages/memory-engine/src/mongodb-novelty.ts` | Engine, Bridge (`memongoBridgeScanNovelty`), API, MCP, Client, AI SDK |
| ... | ... | ... |

Six features by six layers in a single navigable grid.

## Why It Matters

For MetaSystem specifically: as the IL system accumulates skills, references, and agent-addressed conventions, the CLAUDE.md / agent.md / SKILL.md surface gets harder to scan. A feature-by-layer matrix is a cheap compression trick — one table replaces a scattered list of "here's the skill, here's the subagent invocation, here's the chain-invoke pattern" duplications. An agent reading the context file in one pass sees the full shape instead of reconstructing it from prose.

Two concrete places this might fit:
- **IL skill set × invocation mode** — user-invocable slash command, subagent spawn, chained-skill flow. One table in IL's CLAUDE.md would replace the current prose listing of skills per agent.
- **Librarian reference layer × access tier** — Tier-1 auto-loaded, Tier-2 subagent-injected, Tier-3 on-demand. The registry could expose this as a capability matrix.

The pattern is small and self-contained; no new shape, no new file, just a table. Low adoption cost.

## Why People Are Using It

Observed in [Memongo](https://github.com/romiluz13/Memongo) — see `[[memongo-analysis]]` for structural details. Specifically in the root `CLAUDE.md` under "Memory Intelligence", covering six capabilities × six consumer layers (Engine, Bridge, API, MCP, Client, AI SDK). The matrix is explicitly part of the agent-addressed context, not buried in per-package README files — so an agent operating in the Memongo repo reads the full capability surface on session start.

Memongo also follows the matrix with an aggregate line (*"Current totals: 25 collections, 67 standard indexes, 3 new API routes, 3 new MCP tools, 3 new client methods, 3 new AI SDK tools"*) that doubles as a freshness signal — when the totals drift from the matrix, the drift is visible.

## Potential Alternatives

- **Separate per-layer docs.** The default pattern: one doc per layer (API reference, MCP README, SDK README), each listing its own subset of features. Readable per-layer but forces agents to cross-reference to answer "what's the MCP tool for feature X?" or "which features does the client SDK expose?"
- **Prose listing inside each feature's section.** Readable for one feature at a time; unscannable across features; rots independently per section.

## Potential Improvements

- **Cell-level freshness markers.** If a cell references a function that gets renamed, the matrix silently rots. A convention for flagging "this cell verified against commit X" would help.
- **Generated from source.** Ideal state: matrix generated from a registry, not hand-maintained. Memongo's matrix is hand-maintained; any drift between implementation and matrix becomes a manual fix.

## Potential Failure Modes

- **Matrix staleness.** Low adoption cost ↔ low maintenance priority. If features are added in one layer and forgotten in the matrix, the matrix starts lying.
- **Scales only to moderate matrices.** Six-by-six is scannable. Sixty-by-sixty would not be; the pattern doesn't gracefully degrade.
