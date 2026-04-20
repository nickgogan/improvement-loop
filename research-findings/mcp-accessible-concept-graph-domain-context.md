---
name: "MCP-Accessible Concept Graph for Domain Context"
summary: "Expose a curated, multi-source concept graph via an MCP server so agents can query domain expertise on demand. Differs from document retrieval (NotebookLM MCP) and API docs (Context7) — the graph encodes concept relationships, not just document content. Agents execute SQL-like queries against the graph and receive synthesized, attributed answers."
implementation_notes: null
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "tastematter-concept-graph-mcp-ai-signal.md"
related_findings:
  - file: notebooklm-mcp-claude-code-cited-knowledge-layer.md
    rel: same-problem
  - file: mcp-as-code-api-progressive-tool-discovery.md
    rel: enabled-by
  - file: programmatic-tool-calling-code-orchestrated-tool-use.md
    rel: enabled-by
  - file: concept-graph-support-contradiction-detection.md
    rel: companion
  - file: hybrid-retrieval-pattern-semantic-lexical-graph.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: raw
consumed_by: []
---

## What It Is

An architecture where a curated concept graph (encoding domain knowledge with relationship edges between concepts) is exposed as an MCP server. Agents access it via two tools:

1. **Search** — query the graph for relevant concepts, sources, and relationships
2. **Execute** — run code-mode queries (SQL-like syntax) against the full graph schema for precise retrieval

The critical implementation detail is **code mode**: rather than giving the LLM an arbitrary list of tool parameters, the agent writes code to query the graph. The LLM receives the graph schema and generates query code that returns only the needed subset — reducing token consumption by ~90% compared to listing all tools/results upfront. (Attribution: Cloudflare-originated pattern, implemented here for knowledge graph access.)

The graph stores:
- Concepts with topic-cluster assignment
- Source documents (tweets, papers, videos) linked to concepts
- Support/contradiction relationship edges between concepts and sources

Agents can then synthesize across the graph: "What patterns have practitioners tried for X?" returns attributed insights with chains tracing to specific authors and timestamps.

## Why It Matters

This is the deployment layer that makes a curated concept graph useful *to agents*, not just humans reading a daily brief. Once the graph is MCP-accessible:

- Agents can consult domain expertise mid-task without injecting the entire graph into context
- Code-mode queries keep token overhead minimal (schema injection once, then query output only)
- Attribution chains are preserved in responses, enabling grounded reasoning and tradeoff analysis
- The same graph can serve agents with different domain questions (context engineering, GTM engineering, etc.)

The distinction from `notebooklm-mcp-claude-code-cited-knowledge-layer` is structural: NotebookLM returns *document excerpts with citations*; a concept graph returns *synthesized concept relationships*. The former answers "what did this source say?" The latter answers "what do practitioners believe about X and where do they disagree?"

## Why People Are Using It

TasteMatter (practitioner-built). The builder demonstrates the full workflow: add MCP connector to Claude.ai → code mode introspects schema → agent queries graph → synthesized answer with attribution. Beta access free via Cloudflare access policy (50-slot cap at demo time). Also works with Claude Code via MCP connector.

## Potential Improvements

- **Subgraph scoping**: Allow domain-scoped queries (e.g., "only context engineering concepts") so agents in narrow domains don't retrieve noise from adjacent topics.
- **Contradiction surfacing API**: A dedicated tool that returns concept pairs where contradictions are encoded — useful for building balanced briefs.
- **Freshness metadata**: Expose concept and source timestamps so agents can weight recent evidence differently from older findings.
- **Write path**: Allow agents to contribute new findings back to the graph (with human review gate), creating a bidirectional knowledge loop.

## Potential Failure Modes

- **Self-organizing taxonomy drift**: Without periodic cleanup, the concept layer bloats (taxonomy explosion documented in live demo), degrading query relevance.
- **Code-mode query failures**: The agent must generate valid query syntax. If the schema changes or is ambiguous, queries fail silently (demonstrated in the TasteMatter demo where one query ran improperly).
- **Access cap constraints**: Beta implementations with slot limits (50 in this case) limit team-wide adoption.
- **Graph freshness vs. coverage tradeoff**: Timely graphs are noisier; curated graphs are stale. The TasteMatter approach (automated ingestion + daily brief) accepts noise as a cost of timeliness.
