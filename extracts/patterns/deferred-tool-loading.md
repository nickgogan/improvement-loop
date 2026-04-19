---
title: "Deferred Tool Loading"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "gpt-54-tool-search-deferred-tool-loading"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The agent has access to 10+ tools or tool definitions exceed 10K tokens. A lightweight tool registry (name + brief description per tool) exists or can be generated from the full definitions."
  invariants: "Every tool available in the full catalog remains discoverable through the lightweight registry. Tool definitions loaded on-demand are identical to their full catalog versions — no lossy summarization at retrieval time. The agent never silently fails to find a relevant tool due to registry mismatch."
  governance: "Nick owns the tool registry taxonomy and decides which MCP servers and tools are exposed. Changes to the lightweight registry (adding/removing tools, changing descriptions) require review. Agents must not autonomously modify the registry."
  recovery: "If the agent fails to find a relevant tool via search, fall back to loading the full tool catalog for that request. If retrieval latency exceeds acceptable thresholds, pre-load tool definitions for the most frequently used tools as a warm cache. If registry and full definitions drift out of sync, regenerate the registry from source definitions."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Deferred Tool Loading

**Source:** [[gpt-54-tool-search-deferred-tool-loading]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agents connected to many MCP servers or tool providers must inject all tool definitions into every request. As the tool surface grows (10+, 20+, 50+ tools), tool definition tokens consume a large and increasing fraction of the context budget — crowding out task-relevant content, inflating cost, and degrading model attention on the actual work. The problem scales linearly with tool count and is a hard ceiling on agent capability expansion.

## Forces

- **Discoverability vs. economy.** Loading all definitions guarantees the model knows every available tool, but most tools are irrelevant to any single request.
- **Accuracy vs. latency.** On-demand retrieval adds a lookup step. If the lightweight registry description is too terse, the model may fail to identify the right tool; if too verbose, the token savings shrink.
- **Consistency vs. flexibility.** The lightweight registry must stay in sync with the full tool catalog. Any drift means the agent either misses tools or retrieves stale definitions.
- **Vendor convergence vs. lock-in.** Both OpenAI and Anthropic now implement this pattern, making it a cross-vendor expectation — but each vendor's implementation details differ, creating integration overhead for multi-model systems.

## Solution

Replace the pattern of injecting all tool definitions into every request with a two-tier approach:

1. **Lightweight registry.** At inference time, the model receives only a compact list of available tools — name plus a short description per tool. This registry is small enough to fit comfortably in any context window.

2. **On-demand retrieval.** When the model determines it needs a specific tool, it issues a search query against the registry to pull the full definition (parameters, types, constraints) for just that tool. Only the selected tool's definition enters the context.

**Key mechanics:**

- Registry entries must be descriptive enough to support accurate tool selection. A one-line summary per tool is the minimum; keyword tags improve recall.
- Search should support both exact name lookup and semantic query (e.g., "create a pull request" matches `github.createPullRequest`).
- For high-frequency tools that appear in most sessions, consider pre-loading their definitions as a warm cache to avoid the retrieval round-trip.
- The registry is regenerated from the full tool catalog whenever tools are added, removed, or modified — it is a derived artifact, not a hand-maintained one.

OpenAI reports 47% token reduction at equivalent accuracy. Anthropic's Tool Search Tool confirms the pattern with guidance that it is most beneficial when tool definitions exceed 10K tokens or 10+ tools are available.

## Consequences

**Positive:**
- Significant context token savings (47% reported) that scale with tool count — the more tools, the greater the benefit.
- Reduced per-request cost proportional to token savings.
- Removes a hard ceiling on how many tools an agent can have access to without context degradation.
- Improved model attention — fewer irrelevant definitions competing for the model's focus on the actual task.

**Negative:**
- Adds retrieval latency — each on-demand tool load is an extra step before the tool can be called.
- Accuracy depends on registry quality. Poor descriptions lead to missed tools or wrong selections.
- Registry maintenance is a new operational concern, though automation (regeneration from source) mitigates this.
- Multi-vendor environments must maintain registry format compatibility across different implementations of the same pattern.

## Known Uses

- **OpenAI GPT-5.4 Tool Search** (April 2026): Production API feature. 47% token reduction benchmarked across 36 MCP server definitions.
- **Anthropic Tool Search Tool** (April 2026): Claude's implementation — agent searches for relevant tools by query, loads only matching definitions. Recommended for 10+ tools or 10K+ token definitions.
- **MetaSystem environment**: Currently exposes 50+ MCP tools across multiple servers. The lightweight `ToolSearch` tool in the current session is an active instance of this pattern.

## Contract

### Preconditions

- The agent has access to 10+ tools, or total tool definition tokens exceed 10K.
- A lightweight tool registry (name + brief description per tool) exists or can be generated from the full tool definitions.
- The retrieval mechanism (search by name, keyword, or semantic query) is functional and tested.

### Invariants

- Every tool available in the full catalog remains discoverable through the lightweight registry — no silent tool loss.
- Tool definitions loaded on-demand are identical to their full catalog versions — no lossy summarization at retrieval time.
- The registry is a derived artifact: it is regenerated from source definitions, never hand-edited independently.

### Governance

- Nick owns the tool registry taxonomy and decides which MCP servers and tools are exposed.
- Changes to the tool surface (adding/removing servers or tools) trigger registry regeneration.
- Agents must not autonomously modify the registry or add tools without approval.

### Recovery

- If the agent fails to find a relevant tool via search, fall back to loading the full tool catalog for that request and flag the registry gap.
- If retrieval latency exceeds acceptable thresholds, pre-load definitions for the top-N most frequently used tools as a warm cache.
- If registry and full definitions drift out of sync (detected by failed tool calls or missing parameters), regenerate the registry from source definitions immediately.
