---
name: Markdown-in-Git System of Record + Derived Disposable Database
summary: 'Keep knowledge as plain markdown files in a git repo — that is the system of record —

  and sync it into a derived local database (Gbrain: in-process PG lite, no server, no

  Docker) that powers hybrid search (vector + keyword + self-wiring knowledge graph).

  The database is a disposable local file, rebuildable from the markdown at any time;

  the serving layer is a subprocess that dies with the session. "Every layer is

  inspectable: the markdown is yours, the database is a local file, the MCP server is

  just a subprocess."'
implementation_notes: null
category: Agentic Systems
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P3 (Monitor)
applicability:
- General
- IL (knowledge architecture)
adopted_in:
- Improvement Loop
sources:
- give-your-ai-agent-a-second-brain-gbrain-hermes.md
related_findings:
- file: converged-memory-substrate-vs-patchwork.md
  rel: same-problem
- file: hybrid-retrieval-pattern-semantic-lexical-graph.md
  rel: enables
- file: karpathy-llm-knowledge-base-obsidian-rag.md
  rel: extends
- file: stateful-mcp-subprocess-vs-cli-shell-out.md
  rel: enables
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: raw
---

## What It Is

A two-tier storage architecture that separates ownership from retrieval performance:

- **System of record:** plain markdown in a git repo. Human-readable, diffable,
  versioned, portable across agents and tools. This is the layer you own and edit.
- **Derived layer:** the markdown is synced into a local embedded database (PG lite
  running in-process — no server, no Docker, no tunnel, no auth token). The DB carries
  the expensive retrieval machinery: vector embeddings, keyword index, and a knowledge
  graph that wires itself by extracting entity references from prose into typed edges
  (works-at, attended, mentions) with zero LLM calls — Gbrain's own benchmark claims
  +31 points precision over vector-only RAG from the graph layer.
- **Serving layer:** a local MCP stdio subprocess spawned per session, holding the DB
  open, dying with the session.

The derived layers are disposable by construction — corrupt or stale, you rebuild from
markdown. Nothing about your knowledge is trapped in the database.

## Why It Matters

Resolves the standing tension between "markdown is inspectable but retrieval-poor" and
"vector/graph stores retrieve well but are opaque black boxes you don't own." You get
level-3/4 retrieval (semantic + graph) without surrendering the system of record — the
inverse failure of RAG-first stacks where the vector store silently becomes the only
copy of the knowledge.

## Why People Are Using It

Gbrain (Garry Tan, 25k+ stars, MIT, actively developed) is the reference
implementation, commonly attached to OpenClaw/Hermes agents. The pattern matches the
engine's local-first commitments exactly on the record layer (the KB is already
markdown-in-git); the derived-DB layer is the not-yet-needed upgrade path if per-folder
retrieval pain ever appears.

## Potential Alternatives

Markdown-only with index-file navigation (no derived DB — sufficient below the scale
threshold). Database-primary stores with markdown export (ownership inverted; the
export is the disposable layer). Hosted memory services (Supermemory et al.) — retrieval
without local ownership.

## Potential Improvements

Sync-integrity checks (does the DB actually reflect HEAD?). Incremental re-derivation
on commit hooks rather than full rebuilds.

## Potential Failure Modes

Sync drift: edits to markdown that never reach the derived DB produce confidently
stale retrieval — the two-tier design needs a visible sync status. Embeddings require
a separate API key (agent-subscription OAuth does not carry over to the subprocess), a
recurring setup trap. The derived graph is only as good as naming consistency in the
prose — entity extraction by pattern matching misses aliased or misspelled names.
