---
title: "mem0 -- Structural Analysis"
id: "mem0-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-08"
updated: "2026-04-08"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "mem0"
analyzed_version: "v1.0.11"
analyzed_date: "2026-04-08"
repo_url: "https://github.com/mem0ai/mem0"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
  - "research-dimension-mapping"
---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total files | 1,927 |
| Total directories | 345 |
| Python files | 601 (31.2%) |
| MDX files (docs) | 360 (18.7%) |
| TypeScript files | 254 (13.2%) |
| TSX files (React) | 151 (7.8%) |
| Markdown files | 81 (4.2%) |
| PNG files | 67 |
| JSON files | 62 |
| SVG files | 46 |
| YAML/YML files | 69 |
| Jupyter notebooks | 27 |
| MD-to-code ratio | **0.08:1** (code dominant — library + platform) |
| Max directory depth | 8 |

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Skills (SKILL.md) | 9 | `skills/`, `mem0-plugin/skills/`, `openclaw/skills/` |
| Documentation (MDX) | 360 | `docs/` (Mintlify) |
| Markdown docs | ~30 | `docs/` (plain .md files) |
| Jupyter notebooks | 27 | `cookbooks/`, `embedchain/notebooks/`, `examples/` |
| Package READMEs | ~15 | Various `*/README.md` |
| Project files | ~5 | Root (README, AGENTS.md, CLAUDE.md, CONTRIBUTING.md) |
| Other | ~21 | Various |
| **Total (MD+MDX)** | **~441** |

Key insight: mem0 is a polyglot monorepo (Python + TypeScript) providing a memory layer as both a library and a hosted platform. The 360 MDX documentation files reflect the product's focus on developer adoption. The core library (601 Python files) implements the provider pattern with 78 total providers across 5 categories.

### Directory Naming Conventions
Snake_case for Python packages (`mem0/`, `vector_stores/`, `graph_memory/`). Kebab-case for TypeScript and docs packages (`mem0-ts/`, `mem0-plugin/`, `vercel-ai-sdk/`).

### Top-Level Structure
```
.
├── .agents/              # Agent plugins (minimal)
├── .claude-plugin/       # Claude marketplace manifest
├── .cursor-plugin/       # Cursor marketplace manifest
├── cli/                  # CLIs
│   ├── python/           # Python CLI (Typer + Rich)
│   └── node/             # Node CLI (Commander + Chalk)
├── cookbooks/            # Jupyter notebook examples
├── docs/                 # Mintlify documentation site (360 MDX files)
├── embedchain/           # Legacy RAG framework (Poetry-based)
├── evaluation/           # LOCOMO benchmarking framework
├── examples/             # Sample apps (demos, Chrome extension, multi-agent)
├── mem0/                 # Core Python SDK
│   ├── memory/           # Main memory logic (main.py = 113K)
│   ├── llms/             # 24 LLM providers
│   ├── embeddings/       # 15 embedding providers
│   ├── vector_stores/    # 30 vector store providers
│   ├── graphs/           # 4 graph store providers (Neo4j, Memgraph, Kuzu, Apache AGE)
│   ├── reranker/         # 5 reranker providers
│   ├── client/           # Platform client
│   ├── configs/          # Configuration (Pydantic v2)
│   ├── proxy/            # Proxy utilities
│   └── utils/            # Factory pattern, helpers
├── mem0-plugin/          # AI editor plugins (Claude, Cursor, Codex)
│   ├── hooks/            # Lifecycle hooks for auto-memory capture
│   └── skills/           # Plugin skills (mem0, mem0-codex)
├── mem0-ts/              # TypeScript SDK
├── openclaw/             # OpenClaw plugin (@mem0/openclaw-mem0)
│   └── skills/           # OpenClaw skills (memory-dream, memory-triage)
├── openmemory/           # Self-hosted memory platform
│   ├── api/              # FastAPI + Alembic + MCP server
│   └── ui/               # Next.js 15 + React 19
├── server/               # FastAPI REST server (Docker: FastAPI + PostgreSQL/pgvector + Neo4j)
├── skills/               # Claude Code skills (mem0, mem0-cli, mem0-vercel-ai-sdk)
├── tests/                # Python SDK tests (pytest)
└── vercel-ai-sdk/        # Vercel AI SDK memory provider
```

### Notable Structural Patterns
1. **Provider pattern at massive scale**: 78 providers across 5 categories (24 LLMs, 30 vector stores, 15 embeddings, 4 graph stores, 5 rerankers). Each inherits from a base class with consistent interface.
2. **Polyglot monorepo**: Python SDK + TypeScript SDK + Node CLI + Python CLI + FastAPI server + Next.js UI + OpenClaw plugin + Vercel AI SDK provider. Different linters/formatters per package.
3. **Triple storage architecture**: Vector stores (semantic similarity) + Graph stores (relationships) + SQLite (metadata/history). Optional graph layer on top of vector memory.
4. **Multi-platform marketplace**: `.claude-plugin/`, `.cursor-plugin/`, `mem0-plugin/` — plugins for Claude, Cursor, and Codex with MCP server integration.
5. **Legacy RAG framework**: `embedchain/` is maintained separately with its own Poetry build system.

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `CLAUDE.md` / `AGENTS.md` (root) | LLM | Global | Auto-loaded | Constraints/Rules | Comprehensive repo guide: structure, dev setup, build/test commands, coding standards, architecture, CI/CD, contributing (~580 lines) |
| `.claude-plugin/` | Build | Global | Auto-loaded | Tool Usage | Claude marketplace manifest |
| `.cursor-plugin/` | Build | Global | Auto-loaded | Tool Usage | Cursor marketplace manifest |
| `skills/mem0/SKILL.md` | LLM | Tool | Auto-loaded | Tool Usage | Platform SDK skill — Python + TypeScript client usage |
| `skills/mem0-cli/SKILL.md` | LLM | Tool | Auto-loaded | Tool Usage | CLI skill — terminal workflows |
| `skills/mem0-vercel-ai-sdk/SKILL.md` | LLM | Tool | Auto-loaded | Tool Usage | Vercel AI SDK provider skill |
| `mem0-plugin/skills/mem0/SKILL.md` | LLM | Tool | Auto-loaded | Tool Usage | Plugin version of mem0 skill (for Claude/Cursor/Codex) |
| `mem0-plugin/skills/mem0-codex/SKILL.md` | LLM | Tool | Auto-loaded | Tool Usage | Codex-specific variant |
| `openclaw/skills/memory-dream/SKILL.md` | LLM | Tool | Auto-loaded | Workflow/Process | OpenClaw dreaming integration |
| `openclaw/skills/memory-triage/SKILL.md` | LLM | Tool | Auto-loaded | Workflow/Process | OpenClaw memory triage |
| `docs/**/*.mdx` (360 files) | Human | Global | Referenced | Workflow/Process + Tool Usage | Mintlify documentation site |

Sampling notes: Read root CLAUDE.md/AGENTS.md in full (~580 lines). Read 2 skill exemplars (skills/mem0, mem0-plugin/skills/mem0). Read core memory/main.py (80 lines). Classified remaining by pattern.

### Context Loading Strategy
**Minimal context loading — library, not framework:**

mem0 is a library/SDK, not an agent framework. Its context loading is minimal:
1. **Root AGENTS.md**: Comprehensive repo guide for contributors (dev setup, build commands, architecture, coding standards). Not agent behavioral instructions — this is developer documentation for AI coding assistants.
2. **Skills**: 9 skills across 3 deployment targets (Claude Code, OpenClaw, mem0-plugin). Skills teach AI agents how to *use* mem0, not how to *be* an agent. Compare to BMAD/GSD where skills *are* the agent behavior.
3. **Plugin hooks**: `mem0-plugin/hooks/` provides lifecycle hooks for automatic memory capture. These inject into AI editor sessions, not into mem0 itself.

**Key difference from other analyzed repos**: mem0 doesn't have agent identity files (SOUL.md, HEARTBEAT.md, persona definitions). It's a service that other agents consume, not an agent framework itself.

## 3. Workflow Topology

### No SDLC Workflow

mem0 is a library/SDK with no internal workflow topology (no phases, stages, or gates). Instead, it provides a memory lifecycle that consuming agents use:

| Operation | API | What It Does |
|-----------|-----|--------------|
| `add()` | `POST /v1/memories/` | Extract facts from conversation, store in vector + optional graph |
| `search()` | `POST /v1/memories/search/` | Semantic search with optional reranking |
| `get()` | `GET /v1/memories/{id}` | Retrieve single memory by ID |
| `get_all()` | `GET /v1/memories/` | List all memories (filtered by user/agent/run) |
| `update()` | `PUT /v1/memories/{id}` | Update a memory |
| `delete()` | `DELETE /v1/memories/{id}/` | Soft-delete a memory |
| `history()` | `GET /v1/memories/{id}/history/` | Change history for a memory |

### Memory Processing Pipeline (Internal)

```
Input (messages)
      │
      ▼
┌─────────────────┐
│  FACT EXTRACTION │──── LLM extracts facts from messages
│  (LLM call)      │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌──────────┐
│ VECTOR │ │  GRAPH   │ (optional)
│ STORE  │ │  STORE   │
│ (embed │ │ (Neo4j/  │
│  +store)│ │  etc.)   │
└────────┘ └──────────┘
    │         │
    ▼         ▼
┌─────────────────┐
│  SQLITE METADATA│──── History, timestamps, dedup
│  (local storage) │
└─────────────────┘
```

### Scoped Memory Model

| Scope | Purpose | Example |
|-------|---------|---------|
| `user_id` | Per-user memories | "User prefers TypeScript" |
| `agent_id` | Per-agent memories | "Agent learned coding patterns" |
| `run_id` | Per-session memories | "Current conversation context" |
| Combined | Intersection scoping | user_id + agent_id for personalized agent memory |

### Parallelism
- **Async variants**: `AsyncMemory` and `AsyncMemoryClient` for concurrent operations.
- **Batch ingestion**: Bulk memory operations.
- **No workflow parallelism**: mem0 is a single-operation library, not a workflow system.

## 4. Governance Model

### Constraint Expression
| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| Root AGENTS.md | `AGENTS.md` | Soft (LLM-read) | 580 lines of repo standards, coding conventions, per-package configs |
| Provider pattern | `mem0/*/base.py` | Hard (abstract class) | All providers inherit from base with consistent interface |
| Pydantic v2 configs | `mem0/configs/` | Hard (validation) | MemoryConfig with typed fields and validation |
| Pre-commit hooks | `.pre-commit-config.yaml` | Hard | Ruff lint + isort on every commit |
| CI per-package | `.github/workflows/` | Hard | 6 CI workflows + 6 CD workflows |
| OIDC publishing | CD workflows | Hard | No tokens/secrets — trusted publishing |
| PR template | `.github/PULL_REQUEST_TEMPLATE.md` | Soft | Linked issue, type, test coverage, checklist |
| "Do NOT" list | `AGENTS.md` | Soft | 10 explicit prohibitions (no npm, no CI mods, no .env commits, etc.) |

### Guardrail Patterns
1. **Provider pattern as hard boundary**: All providers inherit from abstract base classes. Adding a new provider requires following the exact pattern (inherit, configure, register, test). This is architectural enforcement via code structure.
2. **Per-package linting diversity**: Different linters per package (Ruff for Python, Biome for Node CLI, ESLint for Vercel AI SDK, Prettier for TS SDK). Each package enforces its own standards.
3. **Sensitive field redaction**: `_SENSITIVE_FIELDS_EXACT` and `_RUNTIME_FIELDS` frozensets in memory/main.py for automatic secret redaction.
4. **Optional dependency groups**: New providers go to optional dependency groups in pyproject.toml, never to core dependencies. Prevents bloating the core install.
5. **Separate build systems**: Python SDK (Hatch), Embedchain (Poetry), TypeScript packages (pnpm + tsup). Each ecosystem gets its native tooling.

### Permission Model
- **Scoped memory access**: Memories are scoped by user_id, agent_id, run_id. No cross-scope access without explicit filtering.
- **API key authentication**: Platform API uses `MEM0_API_KEY` bearer tokens.
- **Plugin MCP tools**: 9 tools with defined operations (add, search, get, update, delete, list entities).
- **No agent-level permissions**: mem0 doesn't define what agents can do — it's a service, not a governance layer.

## 5. Cross-Agent Protocol

### No Multi-Agent Coordination

mem0 is a memory service, not a multi-agent framework. It doesn't coordinate agents — it provides memory that agents consume. The "cross-agent" pattern here is:

| Consumer | Integration | How It Uses mem0 |
|----------|-------------|-------------------|
| Claude Code | `mem0-plugin/` | MCP server + lifecycle hooks for automatic memory capture |
| OpenClaw | `openclaw/` | Plugin with dreaming (memory consolidation) and triage skills |
| Cursor | `mem0-plugin/` | MCP server connection |
| Codex | `mem0-plugin/` | MCP server + Codex-specific skill variant |
| LangChain | Example code | Agent memory backend |
| CrewAI | Example code | Multi-agent shared memory |
| AutoGen | Example/cookbook | Agent memory layer |
| OpenAI Agents SDK | Example code | Agent memory backend |
| Vercel AI SDK | `vercel-ai-sdk/` | Memory provider for Vercel AI applications |

### Shared State
- **Vector store**: Semantic memory storage (30 provider options)
- **Graph store**: Relationship-aware memory (4 provider options)
- **SQLite**: Local metadata, history, dedup
- **Memory scopes**: user_id, agent_id, run_id for isolation

### Coordination Pattern
**Service-as-shared-memory.** mem0 provides the memory layer that multiple agents can share. Agents don't coordinate through mem0 — they each independently add and search memories. Cross-agent knowledge sharing happens implicitly: Agent A stores "user prefers TypeScript," Agent B searches and finds it.

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | **High** | Triple storage architecture (vector + graph + SQLite). Scoped memory (user/agent/run). Automatic fact extraction from conversations via LLM. Reranking for search quality. Memory history tracking. MCP integration for tool-based memory access. |
| Model | **High** | 24 LLM provider integrations. 15 embedding providers. 5 reranker providers. Provider pattern with abstract base classes. Factory pattern for provider instantiation. Model-agnostic architecture — swap providers without changing code. |
| Prompt | Low | Fact extraction prompts in `mem0/configs/prompts.py`. Procedural memory system prompt. No complex prompt engineering — mem0 generates the prompts for memory operations internally. |
| Tools | **High** | 9 MCP tools for memory operations. Python + TypeScript SDKs. Two CLIs (Python + Node). Vercel AI SDK provider. Plugin system for AI editors (Claude, Cursor, Codex). |
| Intent | Low | No intent engineering — mem0 is a service that agents call, not a system that interprets intent. |
| Orchestration | Low | No orchestration patterns. Single-operation library. CrewAI/AutoGen examples show mem0 as memory backend, not orchestrator. |
| Evaluation | Medium | LOCOMO benchmarking framework in `evaluation/`. Experiment runner. Score generation. Comparison baselines (RAG, full context, LangMem, OpenAI). |
| Sandboxing | Low | Memory scoping (user/agent/run) provides logical isolation. No process-level sandboxing. |
| Governance | Low | Provider pattern enforcement. Sensitive field redaction. Scoped access. No agent governance patterns — this is library-level code governance, not agent governance. |
| Agent Design | Medium | Memory architecture patterns: fact extraction, scoped memory, graph relationships, history tracking. These inform how agents should structure memory, even though mem0 itself isn't an agent. OpenClaw dreaming integration shows memory consolidation. |

### Findings Candidates

1. **Triple storage architecture** (Context Engineering) — Vector stores for semantic similarity, graph stores for relationship-aware retrieval, SQLite for metadata/history. The graph layer is optional on top of vector — not a replacement. 30 vector store providers + 4 graph store providers give massive deployment flexibility. Compare to OpenClaw's flat markdown memory and Paperclip's PARA-based file memory.
→ Promoted to [[triple-storage-memory-architecture]] on 2026-04-08

2. **Provider pattern at scale** (Tools, Model) — 78 providers across 5 categories, all inheriting from abstract base classes with consistent interfaces. Factory pattern for instantiation. This is the most systematic provider integration approach across all analyzed repos.
→ Promoted to [[provider-pattern-at-scale]] on 2026-04-08

3. **Scoped memory model** (Context Engineering, Agent Design) — Memories scoped by user_id, agent_id, run_id (or combinations). This maps cleanly to MetaSystem's memory model: user_id = user memories, agent_id = project memories, run_id = session context. The scoping model is simpler than OpenClaw's session-based isolation or Paperclip's company-scoped hierarchy.
→ Promoted to [[scoped-memory-model]] on 2026-04-08

4. **Automatic fact extraction** (Context Engineering) — LLM-based extraction of facts from conversations without explicit user action. Messages go in, structured memories come out. This is the "intelligence" layer that MetaSystem's auto-memory system approximates with its frontmatter-tagged memory files.
→ Promoted to [[automatic-fact-extraction]] on 2026-04-08

5. **MCP integration for memory-as-service** (Tools) — 9 MCP tools (add_memory, search_memories, get_memories, get_memory, update_memory, delete_memory, delete_all_memories, delete_entities, list_entities) that any MCP-capable agent can use. This turns memory into a protocol-standard service rather than a library dependency.
→ Promoted to [[mcp-integration-for-memory-as-service]] on 2026-04-08

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-08 | v1.0.11 | all | Initial analysis. 1,927 files, 441 MD+MDX, 78 providers (24 LLM + 30 vector + 15 embedding + 4 graph + 5 reranker). Polyglot monorepo (Python + TypeScript). |
