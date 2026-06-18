---
title: "Letta -- Structural Analysis"
id: "letta-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-05-25"
updated: "2026-05-25"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "letta"
analyzed_version: "v0.16.8"
analyzed_date: "2026-05-25"
repo_url: "https://github.com/letta-ai/letta"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
spectrum_position: "cherry-pick"
---

# Letta (formerly MemGPT) -- Structural Analysis

## Executive Summary

Letta is an open-source framework for building stateful AI agents with persistent memory and tiered context management. The system's core innovation is a structured memory hierarchy (core memory blocks, archival memory, recall memory) that agents self-manage via dedicated tools. Version 0.16.8 introduces git-backed memory versioning, a "sleeptime" background memory agent pattern, and a sophisticated tool-rule engine for constraining agent behavior.

---

## 1. Structural Inventory

### File Statistics

| Metric | Count |
|--------|-------|
| Total files | ~1,185 |
| Python (.py) | ~878 |
| Markdown (.md) | ~13 |
| YAML/YML | ~48 |
| JSON | ~116 |
| TXT | ~20 |
| SQL | 1 |

### Top-Level Directory Tree

```
letta/
├── .github/           # CI workflows, issue templates, model-sweep scripts
├── alembic/           # Database migrations
├── assets/            # Static assets
├── certs/             # TLS certificates
├── db/                # DB init scripts
├── examples/          # Notebooks and example data
├── fern/              # API documentation generator (Fern)
├── letta/             # Main Python package (878 .py files)
├── otel/              # OpenTelemetry config
├── sandbox/           # Sandbox execution runtime (Modal, Node.js)
├── scripts/           # Utility scripts
└── tests/             # Test suite
```

### Main Package (`letta/`) Subdirectories

| Directory | Purpose |
|-----------|---------|
| `adapters/` | LLM request/response adapters (SGLang, simple) |
| `agents/` | Agent implementations (14 files) |
| `cli/` | Command-line interface |
| `client/` | Python client SDK |
| `data_sources/` | Redis, external data connectors |
| `exceptions/` | Custom exception types |
| `functions/` | Tool/function definitions and sets |
| `groups/` | Multi-agent orchestration patterns |
| `helpers/` | Utility modules (datetime, JSON, tool rules) |
| `humans/` | Human persona text templates |
| `interfaces/` | Streaming interfaces (OpenAI, Anthropic) |
| `jobs/` | Background job management |
| `llm_api/` | Provider-specific LLM clients (27 files) |
| `local_llm/` | Local LLM support |
| `model_specs/` | Model pricing/context window data |
| `monitoring/` | Health monitoring |
| `openai_backcompat/` | OpenAI API backward compatibility |
| `orm/` | SQLAlchemy ORM models |
| `otel/` | OpenTelemetry instrumentation |
| `personas/` | Persona text templates |
| `plugins/` | Plugin system |
| `prompts/` | System prompt templates |
| `schemas/` | Pydantic data models |
| `serialize_schemas/` | Agent serialization |
| `server/` | REST API server (FastAPI) |
| `services/` | Business logic managers |
| `templates/` | Jinja2 templates |
| `types/` | Type aliases |

### Naming Conventions

- **Files:** `snake_case.py` throughout
- **Classes:** `PascalCase` (e.g., `LettaAgentV3`, `BlockManager`, `ToolRulesSolver`)
- **Agent versions:** Numeric suffixes indicating evolution (`base_agent.py` -> `base_agent_v2.py`, `letta_agent.py` -> `letta_agent_v2.py` -> `letta_agent_v3.py`)
- **Multi-agent patterns:** versioned (`sleeptime_multi_agent.py` through `sleeptime_multi_agent_v4.py`)
- **Schemas vs ORM:** Separate directories (`schemas/` for Pydantic, `orm/` for SQLAlchemy)

---

## 2. Context File Map

### System Prompts (Core Context Files)

| File | Audience | Mechanism | Content Type |
|------|----------|-----------|--------------|
| `prompts/system_prompts/letta_v1.py` | Agent (self-improving) | Injected as system message | Memory + filesystem instructions |
| `prompts/system_prompts/memgpt_v2_chat.py` | Agent (chat companion) | Injected as system message | Full memory hierarchy explainer |
| `prompts/system_prompts/sleeptime_v2.py` | Background memory agent | Injected as system message | Memory editing instructions |
| `prompts/system_prompts/sleeptime_doc_ingest.py` | Doc ingest agent | Injected as system message | Document summarization instructions |
| `prompts/system_prompts/react.py` | ReAct agent | Injected as system message | Minimal tool-use loop |
| `prompts/system_prompts/workflow.py` | Workflow agent | Injected as system message | Tool chaining via heartbeats |
| `prompts/system_prompts/voice_chat.py` | Voice agent | Injected as system message | Conversational voice agent |
| `prompts/system_prompts/voice_sleeptime.py` | Voice memory agent | Injected as system message | Voice-specific memory management |

### Memory-Related Files

| File | Purpose |
|------|---------|
| `schemas/memory.py` | Memory class with compile() rendering, ContextWindowOverview |
| `schemas/block.py` | Block/FileBlock data model (labeled memory sections) |
| `schemas/memory_repo.py` | Git-backed memory repo schemas |
| `services/block_manager.py` | Block CRUD operations |
| `services/block_manager_git.py` | Git-enabled block manager (version history) |
| `services/memory_repo/` | Git operations, markdown serialization, storage backends |
| `services/memory_repo/block_markdown.py` | Markdown+YAML frontmatter serialization for blocks |

### Persona and Human Templates

| File | Purpose |
|------|---------|
| `personas/examples/sam.txt` | Default persona |
| `personas/examples/sleeptime_memory_persona.txt` | Sleeptime memory agent persona |
| `personas/examples/voice_memory_persona.txt` | Voice memory agent persona |
| `humans/examples/basic.txt` | Default human description |

### Prompt Generation

| File | Purpose |
|------|---------|
| `prompts/prompt_generator.py` | Assembles system prompt from parts: base instructions + memory metadata + compiled memory blocks |
| `prompts/summarizer_prompt.py` | Summarization/compaction prompts (ALL, SLIDING, SELF variants) |
| `prompts/gpt_summarize.py` | Legacy summarization prompts |

### Configuration Files

| File | Scope | Purpose |
|------|-------|---------|
| `conf.yaml` | Server-wide | Full server configuration (DB, Redis, multi-agent, OTEL) |
| `.env.example` | Deployment | Environment variable template |
| `pyproject.toml` | Build | Package metadata and dependencies |

---

## 3. Workflow Topology

### Agent Lifecycle

```
Create Agent -> Configure (type, persona, human, tools, tool_rules, memory blocks)
             -> Agent Loop: receive message -> rebuild memory -> LLM call -> tool execution -> persist state
             -> Summarize/Compact when context overflows
```

### Agent Type Hierarchy

```
BaseAgentV2 (abstract)
├── LettaAgentV2
│   └── LettaAgentV3 (primary agent loop)
│       └── SleeptimeMultiAgentV3/V4 (foreground + background memory)
│
BaseAgent (legacy abstract)
├── LettaAgent (v1 agent loop with heartbeats)
│   └── VoiceSleeptimeAgent
├── EphemeralAgent
├── EphemeralSummaryAgent
├── VoiceAgent
├── LettaAgentBatch
├── RoundRobinMultiAgent
├── DynamicMultiAgent
├── SleeptimeMultiAgent/V2
└── SupervisorMultiAgent
```

### Agent Loop Factory (`AgentLoop.load()`)

The factory selects the execution loop based on `AgentType` and `enable_sleeptime`:

1. **letta_v1_agent / sleeptime_agent** with sleeptime enabled -> `SleeptimeMultiAgentV4`
2. **letta_v1_agent** without sleeptime -> `LettaAgentV3`
3. **Other types** with sleeptime -> `SleeptimeMultiAgentV3`
4. **memgpt_agent / memgpt_v2_agent** (legacy) -> `LettaAgent`

### Memory Management Flow

```
User Message
    |
    v
_rebuild_memory_async()
    |-- refresh blocks from DB
    |-- compile memory (Memory.compile())
    |       |-- render memory_blocks (XML tags with label/description/metadata/value)
    |       |-- render tool_usage_rules
    |       |-- render directories (file blocks)
    |       |-- [git-enabled]: render memory_filesystem tree
    |-- compile memory_metadata block (agent_id, timestamps, counts, archive tags)
    |-- inject into system message[0]
    |
    v
LLM Call (with compiled system prompt + in-context messages)
    |
    v
Tool Execution (may modify blocks -> triggers rebuild next step)
    |
    v
Summarization Check (if context exceeds threshold)
    |-- STATIC_MESSAGE_BUFFER: trim to fixed window
    |-- PARTIAL_EVICT_MESSAGE_BUFFER: summarize + evict portion
    |-- Compaction: sliding_window or all summarization
```

### Memory Hierarchy (Three Tiers)

1. **Core Memory** (in-context, always visible): Named blocks with labels, descriptions, character limits. Rendered into system prompt as XML. Self-editable via `core_memory_append`, `core_memory_replace`, `memory()` tool.

2. **Recall Memory** (conversation history): Searchable message database via `conversation_search` tool. Hybrid search (text + semantic similarity).

3. **Archival Memory** (long-term storage): Embedding-indexed passages. Accessed via `archival_memory_insert`, `archival_memory_search` with tags, date filters, semantic search.

### Git-Backed Memory (New in v0.16.x)

Agents tagged with `git-memory-enabled` get:
- Memory blocks stored as Markdown files with YAML frontmatter in a git repo
- Full version history via git commits
- Object storage (GCS/S3) as source of truth, PostgreSQL as cache
- Structured filesystem rendering (`<memory_filesystem>` tree in prompt)
- Memory file paths used as block identifiers (e.g., `system/persona`, `system/human`)

### Summarization Strategies

| Mode | Mechanism |
|------|-----------|
| `all` | Summarize entire evicted window into single summary |
| `sliding_window` | Summarize evicted prefix, keep recent messages |
| `self_compact_all` | Agent self-summarizes |
| `self_compact_sliding_window` | Agent self-summarizes sliding window |
| Default summarizer models: Haiku 4.5 (Anthropic), GPT-5-mini (OpenAI), Gemini 2.5 Flash (Google) |

### Sleeptime Pattern (Background Memory Management)

The "sleeptime" architecture splits memory management from conversation:
1. **Foreground agent** handles user interaction (LettaAgentV3)
2. **Background sleeptime agents** process conversation asynchronously
3. `SleeptimeMultiAgentV4` orchestrates: runs foreground step, then dispatches background tasks
4. Sleeptime agents run at configurable frequency (`sleeptime_agent_frequency`)
5. Background agents have their own persona (memory expert) and dedicated memory editing tools

### Human Gates

- **Tool Approval**: `RequiresApprovalToolRule` pauses execution and creates an `ApprovalRequestMessage`
- **No autonomous deployment**: Tool execution is sandboxed; no direct system modification

---

## 4. Governance Model

### Constraint Mechanisms

| Mechanism | Location | Purpose |
|-----------|----------|---------|
| **Tool Rules** | `schemas/tool_rule.py`, `helpers/tool_rule_solver.py` | Constrain agent tool call sequences |
| **AI Policy** | `AI_POLICY.md` | Human-in-the-loop requirement for contributions |
| **Privacy Policy** | `PRIVACY.md` | Data handling constraints |
| **Security Policy** | `SECURITY.md` | Vulnerability reporting |
| **Block Limits** | `schemas/block.py` | Character limits on memory blocks |
| **Read-Only Blocks** | `schemas/block.py` | Prevent agent modification of certain memory |
| **Context Window Limits** | `services/context_window_calculator/` | Token budget management |

### Tool Rule System (Sophisticated Constraint Engine)

The `ToolRulesSolver` enforces a rich set of constraints on tool invocation:

| Rule Type | Behavior |
|-----------|----------|
| `InitToolRule` | First tool that MUST be called |
| `TerminalToolRule` | Calling this tool ends the agent loop |
| `ChildToolRule` | After tool X, must use one of [Y, Z] |
| `ParentToolRule` | Tool Y can only be called after tool X |
| `ConditionalToolRule` | Route to child based on tool output |
| `ContinueToolRule` | Tool that continues execution |
| `MaxCountPerStepToolRule` | Limit invocations per step |
| `RequiredBeforeExitToolRule` | Must call before agent can exit |
| `RequiresApprovalToolRule` | Human approval required |

Tool rules are rendered into the prompt as `<tool_usage_rules>` XML block and enforced programmatically by the solver.

### Sandbox Execution

Tools execute in sandboxed environments:
- **E2B Sandbox** (`e2b_sandbox.py`): Cloud sandbox
- **Modal Sandbox** (`modal_sandbox.py`, `modal_sandbox_v2.py`): Serverless compute
- **Local Sandbox** (`local_sandbox.py`): Local subprocess isolation
- Environment variables injected per-agent (`LETTA_AGENT_ID`, `LETTA_SERVER_URL`)

### Memory Block Permissions

- `read_only: bool` — prevents agent write operations
- `hidden: bool` — blocks visibility from context
- Character limits per block — hard boundary enforcement
- Agent-scoped block ownership via `BlocksAgents` ORM

---

## 5. Cross-Agent Protocol

### Multi-Agent Orchestration Patterns

| Pattern | File | Mechanism |
|---------|------|-----------|
| **Round Robin** | `groups/round_robin_multi_agent.py` | Sequential turn-taking |
| **Supervisor** | `groups/supervisor_multi_agent.py` | Central coordinator dispatches to workers |
| **Dynamic** | `groups/dynamic_multi_agent.py` | Runtime agent selection |
| **Sleeptime** (v1-v4) | `groups/sleeptime_multi_agent_v4.py` | Foreground+background asynchronous |
| **Voice Sleeptime** | `agents/voice_sleeptime_agent.py` | Voice-specific async memory |
| **Swarm** | Referenced in `ManagerType` enum | Peer-to-peer (schema exists, impl TBD) |

### Inter-Agent Communication

Agents communicate via `send_message_to_agent_and_wait_for_reply()`:
- Uses the Letta client SDK internally
- Messages include sender agent ID automatically
- Augmented with sender identification prefix
- Executed in sandbox environment (not direct function call)
- Timeout: 1200s, retries: 3, concurrent sends: 50

### Group Configuration

Groups are configured via `Group` schema:
- `manager_type`: Orchestration pattern selection
- `agent_ids`: Member agents list
- `manager_agent_id`: Coordinator agent (for supervisor pattern)
- `shared_block_ids`: Shared memory blocks across group (deprecated)
- `sleeptime_agent_frequency`: How often background agents run
- `max_message_buffer_length` / `min_message_buffer_length`: Context window bounds
- `termination_token`: Signal for conversation end
- `max_turns`: Turn limit

### Shared State Mechanisms

1. **Shared Memory Blocks**: Blocks can be attached to multiple agents (via `BlocksAgents` ORM). Changes by one agent are visible to others on next memory rebuild.
2. **Conversations**: `ConversationManager` maintains shared conversation state with block associations.
3. **Message passing**: Agents receive messages tagged with `group_id` for multi-agent context.
4. **Last processed message tracking**: `last_processed_message_id` prevents duplicate processing by background agents.

### Tool Executor Routing

```
ToolExecutorFactory routes by ToolType:
├── LETTA_CORE / LETTA_MEMORY_CORE / LETTA_SLEEPTIME_CORE -> LettaCoreToolExecutor (direct)
├── LETTA_BUILTIN -> LettaBuiltinToolExecutor (web_search, run_code, etc.)
├── LETTA_FILES_CORE -> LettaFileToolExecutor
├── LETTA_MULTI_AGENT_CORE -> SandboxToolExecutor (isolated)
├── EXTERNAL_MCP -> ExternalMCPToolExecutor
└── Default -> SandboxToolExecutor
```

### MCP Integration

Full MCP (Model Context Protocol) support:
- `services/mcp/` — SSE client, stdio client, streamable HTTP client, FastMCP client
- `services/mcp_manager.py` — MCP server lifecycle management
- `services/mcp_server_manager.py` — Server registry
- OAuth support for MCP servers

---

## 6. Research Dimension Mapping

### Relevance Ratings

| Dimension | Relevance | Notes |
|-----------|-----------|-------|
| **Context Engineering** | **High** | Core innovation: three-tier memory hierarchy with self-managed blocks, git-backed versioning, structured XML rendering with metadata |
| **Model Selection** | Medium | Multi-provider routing (27 LLM clients), auto-mode model selection, provider-specific summarizer defaults |
| **Prompt Craft** | **High** | Sophisticated system prompt assembly: XML-structured sections, line-numbered memory blocks (Anthropic-specific), memory metadata injection, available_skills rendering |
| **Tool Integration** | **High** | Rich tool system: typed tool rules engine, multi-backend sandbox execution, MCP support, composio integration, tool schema generation |
| **Intent Engineering** | Medium | Tool rules as behavioral constraints (init/terminal/child/parent/conditional), heartbeat control flow, approval gates |
| **Orchestration** | **High** | Multiple multi-agent patterns (round-robin, supervisor, dynamic, sleeptime, swarm), group management, async background processing |
| **Evaluation** | Low | Model sweep scripts in `.github/scripts/model-sweep/`, basic test suite |
| **Sandboxing** | **High** | Three sandbox backends (E2B, Modal, Local), TypeScript generator, environment isolation, safe pickle |
| **Governance** | Medium | AI policy, tool approval rules, read-only blocks, character limits, but no formal governance framework |
| **Agent Design** | **High** | Clear agent hierarchy (BaseAgent -> versioned impls), factory pattern, agent state persistence, agent type enum, skills system |
| **Agentic Systems** | **High** | Full agentic platform: persistent state, self-modifying memory, background processing, multi-agent coordination, conversation management |

### High-Relevance Pattern Details

**Context Engineering:**
- Memory compiled as XML blocks with `<label>`, `<description>`, `<metadata>`, `<value>` sub-tags
- `ContextWindowOverview` tracks token budget across all sections
- Three rendering modes: standard, line-numbered (Anthropic-only), git-backed
- Memory filesystem tree rendering for git-enabled agents
- Archival memory tags exposed in metadata block for retrieval hints
- Available skills rendered as file tree with descriptions

**Prompt Craft:**
- System prompt assembled from: base_instructions + memory_metadata + memory_blocks + tool_usage_rules + directories + available_skills
- Provider-specific formatting (line numbers only for Anthropic models)
- Memory blocks show char_current/char_limit metadata
- Warning text injected about line number usage rules
- Summarization prompts are highly structured (7 sections with specific instructions)

**Tool Integration:**
- `ToolRulesSolver` compiles rules into `<tool_usage_rules>` block AND enforces programmatically
- Prefilled arguments from rules (conditional routing with pre-set params)
- Tool schema generation from Python function signatures
- Runtime tool JSON schema overrides
- TypeScript tool generation for Node.js sandbox

**Orchestration:**
- Sleeptime pattern: foreground agent responds immediately, background agents process memory asynchronously
- Configurable frequency for background processing
- Turn counting and message buffer length management
- Multi-agent message routing with sender identification
- Shared memory blocks for cross-agent state

**Agent Design:**
- Two-generation architecture (BaseAgent legacy + BaseAgentV2 current)
- Factory pattern (`AgentLoop.load()`) selects implementation by type
- Agent state fully serialized and persisted
- Ephemeral agents for one-off tasks (summarization)
- Version evolution visible in class hierarchy (v1 -> v2 -> v3)

---

## Findings Candidates

### FC-1: Three-Tier Memory Architecture with Self-Management

**Pattern:** Letta implements a three-tier memory hierarchy where the agent self-manages all tiers via dedicated tools:
1. Core Memory (always in context, XML-rendered, character-limited)
2. Recall Memory (conversation history, hybrid search)
3. Archival Memory (long-term, embedding-indexed, tagged)

Each tier has distinct access patterns, persistence characteristics, and tool interfaces. The agent decides what to promote/demote between tiers.

**Relevance:** Context Engineering, Agent Design
**Evidence strength:** Production system, v0.16.8

### FC-2: Git-Backed Memory Versioning

**Pattern:** Memory blocks stored as Markdown files with YAML frontmatter in git repositories, with full version history. Object storage (GCS) is source of truth, PostgreSQL is read cache. This gives agents a complete audit trail of memory evolution.

**Relevance:** Context Engineering, Governance
**Evidence strength:** Production system, dedicated service layer (`memory_repo/`)

### FC-3: Sleeptime Background Memory Agent Pattern

**Pattern:** Splitting memory management from conversation into foreground (interactive) and background (memory processing) agents. Background agents run asynchronously at configurable frequency, processing recent conversation into structured memory. This decouples response latency from memory quality.

**Relevance:** Orchestration, Agent Design, Context Engineering
**Evidence strength:** Production system, evolved through 4 versions (v1-v4)

### FC-4: Declarative Tool Rule Engine

**Pattern:** A constraint system for agent tool usage that is both rendered into prompts (as XML) AND enforced programmatically. Supports init/terminal/child/parent/conditional/approval rules with prefilled arguments. This dual enforcement (soft via prompt + hard via code) increases reliability.

**Relevance:** Tool Integration, Intent Engineering, Governance
**Evidence strength:** Production system, comprehensive rule types

### FC-5: Provider-Adaptive Prompt Rendering

**Pattern:** Memory block rendering adapts to the model provider. Anthropic models get line-numbered memory blocks; others get standard rendering. Summarizer model selection varies by provider (Haiku for Anthropic, GPT-5-mini for OpenAI, Gemini Flash for Google). This acknowledges that optimal context formatting is model-specific.

**Relevance:** Prompt Craft, Model Selection
**Evidence strength:** Production system, explicit provider branching

### FC-6: Structured Context Window Budget Tracking

**Pattern:** `ContextWindowOverview` provides complete token accounting across all prompt sections (system, core memory, memory filesystem, tool rules, directories, summary, function definitions, messages). Each section tracked independently, enabling fine-grained budget management.

**Relevance:** Context Engineering
**Evidence strength:** Production system, dedicated calculator service

### FC-7: Memory Block as Labeled Semantic Container

**Pattern:** Memory organized as labeled blocks with: label (path-like identifier), description (behavioral instructions for the agent), value (content), metadata (read_only, char limits), and limit enforcement. The description field explicitly tells the agent how a block should influence behavior -- making memory self-documenting.

**Relevance:** Context Engineering, Agent Design
**Evidence strength:** Core abstraction, used across all agent types

### FC-8: Multi-Modal Summarization Strategies

**Pattern:** Four distinct summarization modes with structured prompts (7-section template): all-at-once, sliding window, self-compact-all, self-compact-sliding-window. Self-compact modes let the agent summarize its own context. Prompts explicitly instruct preservation of identifiers, lookup hints, and error/fix history.

**Relevance:** Context Engineering, Prompt Craft
**Evidence strength:** Production system, detailed prompt engineering visible
