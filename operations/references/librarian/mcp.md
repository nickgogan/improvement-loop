---
term: mcp
type: concept
variants: []
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "claude"
stage: "draft"
tags:
  - "librarian-concept"
  - "mcp"
  - "tool-protocol"
aliases:
  - "MCP"
  - "Model Context Protocol"
  - "MCP server"
---

# MCP (Model Context Protocol)

## Short definition

**MCP** is a harness-level protocol for exposing external resources (tools, data, services) to an agent over a uniform `execute(name, input) → string` interface. An MCP *server* provisions a set of tools; an MCP *client* (the harness) loads their definitions and routes tool calls. Treated as baseline infrastructure in the KB rather than an adoption decision — the ecosystem-calibrated posture is stated at `designing-agent-tools.md` §Step 7 line 280 (ecosystem figures cited from source; the Librarian references the line rather than restating values that drift).

Single referent. No variants — "MCP" names one protocol surface. The adjacent disciplines (tool registry design, deferred loading, tool-definition token budgets) live under G5 and are surfaced through this concept file's composition table rather than duplicated here.

## Not to be confused with

| Not MCP | What it is instead |
|---|---|
| **Tool definition** | The metadata (name, description, schema) loaded into an agent's context. MCP is one *source* of tool definitions; SDK-native tools and skill wrappers are alternatives. See G5 §Contract line 32 ("difference between tool definitions (metadata) and tool implementations (code)"). |
| **Harness** | The runtime surface an agent runs inside. A harness *loads* MCP servers; MCP is not itself a harness. See `harness.md`. |
| **Skill** | Procedural packaging of a bounded operation authored as `SKILL.md`. A skill may wrap MCP tools, but MCP is the wire protocol and skills are the procedural layer. See `skill.md`. |
| **A2A (Agent-to-Agent)** | Cross-organization agent delegation protocol. G3 §Step 4 line 221 draws the boundary explicitly: *"MCP handles agent-to-resource; A2A handles agent-to-agent."* |
| **Tool Search / deferred loading** | A *discipline* for loading tool definitions on demand (G5 §Key Concepts Concept 4, line 60). MCP is orthogonal — MCP tools can be eager-loaded or deferred; the protocol does not mandate either. |

## Why this is a concept, not a dimension

The Researcher scans for aspects (Tools, Context, Prompt, Orchestration, …). MCP is a *consumer lens* that cross-cuts several at once: Tools (how tools reach the agent), Context (MCP tool definitions can consume a substantial fraction of the context budget at scale — G5 §Key Concepts line 60 carries the ecosystem-calibrated figure), Permissions (MCP tools enter the harness's allowlist — `agent-safety-and-permissions.md` §Tool Gateway line 388), and Architecture (Layer 4 of the infrastructure-longevity stack — G3 §Step 6 line 252). Scan-topic framing would force an "MCP" partition that overlaps every layer. Consumer-query framing is the right place: this concept file points into the aspects that already exist.

## Composition

Pointers into the substrate. **No observed use-case load at registry time** (session-49 use-case registry flagged 0 MCP-specific UCs); composition is provisional and query-driven — expand when the first MCP-nouned consumer query arrives.

| Aspect | Tier 1 (guides, default) | Tier 2 (patterns / findings, on escalation) | Tier 3 (watched-libraries / external, on explicit ask) |
|---|---|---|---|
| Protocol role, uniform execute interface | G3 §Step 3 line 193–202 (Brain / Hand split; MCP named as one "hand") | `mcp-as-code-api-progressive-tool-discovery`; `mcp-as-primary-architecture-vs-supplementary` | Anthropic MCP spec; Anthropic's internal MCP servers (Slack, Asana, Claude Code — G5 §Step 3 line 132) |
| Ecosystem baseline / adoption posture | G5 §Step 7 line 280 ("MCP is baseline infrastructure"); G3 §Step 6 line 252 (Layer 4 longevity) | `mcp-ecosystem-critical-mass-97m-installs` | Public MCP server registries |
| Token cost — MCP tool definitions in context | G5 §Key Concepts line 60 (tool-definition token cost at scale); G5 §Worked Example lines 419–421 (illustrative hybrid loading strategy) | `mcp-as-code-api-progressive-tool-discovery`; `mcp-server-cards-discovery` | — |
| Permissions and allowlisting | G6 §Tool Gateway line 388 ("Allowlisted tools: … MCP tools") | `mcp-session-scoped-authorization`; `mcp-enterprise-governance-gaps` | — |
| Boundary with A2A (agent-to-agent) | G3 §Step 4 line 221 ("MCP handles agent-to-resource; A2A handles agent-to-agent") | — | A2A spec (Google / Linux Foundation) |
| SDK-native vs MCP vs managed tradeoff | G5 §Step 7 lines 274–279 (comparison table) | `cli-first-tool-integration-less-overhead-than-mcp`; `mcp-n-plus-m-integration-economics` | — |
| Evaluation / observability over MCP | — | `mcp-evaluation-primitives-deepeval-metrics` | — |
| Memory-as-service via MCP | — | `mcp-integration-for-memory-as-service`; `mcp-accessible-concept-graph-domain-context` | Memongo, other memory-service MCP servers |
| Advanced protocol features (async, elicitation, N+M integration) | — | `mcp-async-task-model`; `mcp-elicitation-for-user-input`; `mcp-n-plus-m-integration-economics` | Anthropic MCP spec §capabilities |

No whole-artifact cross-guide thread today — the concept has not accumulated whole-MCP queries. If consumers begin submitting "design my MCP surface" / "audit my MCP tool loading" queries, the composition can promote to thread form (the way `harness.md` did) without restructuring this file.

## Librarian read rule

**Default (Tier 1).** For definitional / placement queries ("what is MCP?", "where does MCP fit in my stack?"), G3 §Step 3 line 193–202 (brain/hand split) + G5 §Step 7 line 280 (baseline posture) is sufficient — two short reads, no Tier-2.

**Escalate to Tier 2 when:**
- Consumer is sizing MCP token cost in a specific context — pull `mcp-as-code-api-progressive-tool-discovery` alongside G5's ecosystem-calibrated example at §Key Concepts line 60.
- Consumer is deciding MCP-vs-alternatives (CLI wrapper, SDK-native tool, script) — surface `cli-first-tool-integration-less-overhead-than-mcp` and `mcp-as-primary-architecture-vs-supplementary`; these form a `contradicts`-adjacent design debate and route the query through `decide.md`.
- Consumer is asking about MCP governance / authorization / enterprise risk — `mcp-session-scoped-authorization` + `mcp-enterprise-governance-gaps`.

**Escalate to Tier 3 when:**
- Consumer asks for the MCP spec itself (handshake shape, capability negotiation, message framing) — Anthropic MCP docs are authoritative; do not paraphrase from training.
- Consumer is comparing specific MCP server implementations (Slack vs Asana vs Context7 vs Notion MCP) — cite each server and its source.
- A Tier-1 or Tier-2 answer names a specific capability (resources, tools, prompts, elicitation) and the consumer needs the exact shape to implement or verify.

**Do not:**
- Treat MCP as a harness substitute. MCP is a protocol the harness speaks; the harness still owns prompt composition, caching, permissions, session mechanics. See `harness.md`.
- Recommend MCP adoption without checking token-cost posture. Eager-loading many MCP servers can consume a substantial fraction of the context budget before the consumer's message lands — G5 §Key Concepts line 60 carries the ecosystem-calibrated figure. The question is loading discipline, not adoption.
- Silently escalate to Tier 3. MCP-spec and server-implementation reads are high-value but external-substrate; ask before pulling per read-contract §Step 5.

## Provenance surfacing

Tier-1 citations: `<guide>.md#<anchor>` with line-range appendix until the section manifest lands. Tier-2 citations: finding slug (`mcp-*.md` under `research-findings/`). Tier-3 citations: Anthropic MCP docs URL or watched-lib path. Ecosystem metrics (install counts, server counts) always cite the G5 / finding source — figures move, and the Librarian is not the source of truth.

## Cross-references

- Related concepts: `harness.md` (MCP is a protocol the harness loads), `skill.md` (skills may wrap MCP tools), `agent.md` (agents consume MCP tool definitions — MCP-adjacent aspects surface through `agent.md`'s composition when a query names MCP).
- Related operations: `audit.md` (MCP allowlisting and token cost are two audit aspects); `decide.md` (MCP vs SDK-native vs CLI-wrapper is a canonical tradeoff); `explain.md` (mechanism questions about MCP).
- Use-case registry (no flagged UCs at registry time; author-promoted on first MCP-nouned query): `operations/references/librarian/use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role — G5 tool-integration Contract invariants fire as emergent audit criteria for any MCP-using agent), DD-82 (IL 4-agent architecture).
