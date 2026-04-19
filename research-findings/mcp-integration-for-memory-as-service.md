---
name: MCP Integration for Memory as Service
summary: mem0 exposes 9 MCP tools (add, search, get, update, delete memories plus entity management) that any MCP-capable agent can use. Turns memory from a library dependency into a protocol-standard service accessible from Claude Code, Cursor, and Codex.
implementation_notes: null
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- mem0-analysis.md
related_findings: []
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-08'
pipeline_status: "raw"
consumed_by: []
---
## What It Is

mem0 exposes 9 MCP (Model Context Protocol) tools:

1. **add_memory** — store a new memory
2. **search_memories** — semantic search across stored memories
3. **get_memories** — retrieve memories by scope filters
4. **get_memory** — retrieve a specific memory by ID
5. **update_memory** — modify an existing memory
6. **delete_memory** — remove a specific memory
7. **delete_all_memories** — clear all memories matching a scope
8. **delete_entities** — remove entity nodes from the graph layer
9. **list_entities** — enumerate known entities

Any MCP-capable agent can use these tools without importing mem0 as a library. The integration is available via the `mem0-plugin` package and supported in Claude Code, Cursor, and Codex.

## Why It Matters

Library dependencies create tight coupling — the consuming agent must be written in the same language, manage the dependency, and handle version compatibility. MCP transforms memory from a code dependency into a protocol-standard service. Any agent that speaks MCP can read and write memories, regardless of implementation language or framework.

This enables memory sharing across different AI tools. A Claude Code agent and a Cursor agent working on the same project can share the same memory store through the same protocol.

## Why People Are Using It

Observed in [mem0](https://github.com/mem0ai/mem0) v1.0.11 — see [[mem0-analysis]] for structural details.

The MCP integration is notable because it positions memory as infrastructure rather than application logic. This aligns with the broader trend of MCP becoming a standard integration layer for AI tools, and demonstrates that memory services are a natural fit for the protocol's tool-based architecture.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Library import (direct API) | Import mem0 as a Python dependency | When all agents are Python and tight integration is acceptable |
| REST API service | Expose memory operations via HTTP endpoints | When MCP is not available or when non-AI clients need access |
| File-based shared memory | Agents read/write shared markdown/JSON files | When no server infrastructure is acceptable |
| Database direct access | Agents connect directly to the backing store | When the abstraction layer adds unnecessary overhead |

## Potential Improvements

- Evaluate whether the 9-tool surface area is too granular or too coarse for typical agent workflows
- Assess whether batch operations (add multiple memories, search across scopes) would reduce round-trips
- Investigate how the MCP integration handles authentication and multi-tenant isolation

## Potential Failure Modes

- **MCP server availability**: Memory becomes a network dependency — server downtime blocks all memory operations
- **Protocol overhead**: MCP adds serialization/deserialization overhead compared to direct library calls
- **Tool discovery complexity**: 9 tools may overwhelm agents with limited tool-selection capacity
- **Shared memory conflicts**: Multiple agents writing to the same memory store without coordination may create conflicting entries
- **MCP ecosystem fragmentation**: If MCP adoption stalls, the integration becomes a maintenance burden on a niche protocol
