---
title: "ADK-Python -- Structural Analysis"
id: "adk-python-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "improvement-loop"
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
  - "adk-python"
analyzed_version: "v2.0.0"
analyzed_date: "2026-05-25"
repo_url: "https://github.com/google/adk-python"
spectrum_position: "cherry-pick"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# ADK-Python -- Structural Analysis

Google's Agent Development Kit (ADK) for Python -- an open-source, code-first framework for building, evaluating, and deploying AI agents. v2.0 introduces graph-based workflow orchestration and structured task delegation alongside the existing LLM agent abstractions.

---

## 1. Structural Inventory

### File Statistics

| Metric | Count |
|--------|-------|
| Total files (excl. `.git/`) | 2,049 |
| Python source files | 1,497 |
| Source library (`src/google/adk/`) | 594 files, ~128k lines |
| Test files | 519 |
| Markdown files | 205 |
| YAML/TOML/JSON config | 183 |

### Top-Level Tree

```
adk-python/
  .agents/              # AI coding assistant skills (7 skills)
  .gemini/              # Gemini CLI config (points to AGENTS.md)
  .github/              # Workflows, issue templates, release-please
  assets/               # Images/branding
  contributing/         # Contributing guide + 130+ sample agents
  scripts/              # Utility scripts (check_new_py_files.sh, etc.)
  src/google/adk/       # Core library
  tests/                # Unit, integration, remote tests
  AGENTS.md             # AI assistant context file (top-level)
  llms.txt              # LLM-consumable project overview (11KB)
  llms-full.txt         # Extended LLM context (1.2MB)
  pyproject.toml        # Build config (flit), dependencies, extras
  README.md             # User-facing readme
```

### Source Package Structure (`src/google/adk/`)

| Module | Files | Purpose |
|--------|-------|---------|
| `agents/` | 30 | Agent abstractions: BaseAgent, LlmAgent, Loop/Sequential/Parallel agents |
| `workflow/` | 26 | Graph-based orchestration: BaseNode, Workflow, NodeRunner, triggers |
| `tools/` | 120+ | Tool ecosystem: function tools, MCP, OpenAPI, BigQuery, Spanner, etc. |
| `flows/llm_flows/` | 22 | LLM execution flows: auto-flow, single-flow, content building |
| `evaluation/` | 55+ | Eval framework: metrics, LLM-as-judge, trajectory, simulation |
| `sessions/` | 16 | Session services: in-memory, SQLite, database, Vertex AI |
| `memory/` | 7 | Memory services: in-memory, Vertex AI RAG |
| `cli/` | 50+ | CLI tools: web server, API server, agent loader, conformance |
| `plugins/` | 11 | Plugin system: base plugin, logging, retry, analytics |
| `a2a/` | 29 | Agent-to-Agent protocol: converters, executor, agent card |
| `auth/` | 23 | Authentication: OAuth2, credential services, exchangers |
| `models/` | 15 | LLM adapters: Google, Anthropic, LiteLLM, Gemma, Apigee |
| `telemetry/` | 9 | OpenTelemetry tracing, metrics, Google Cloud export |
| `integrations/` | 35 | External integrations: Firestore, Slack, BigQuery, LangChain |
| `code_executors/` | 10 | Code execution: container, GKE, Vertex AI, local |
| `optimization/` | 7 | Prompt optimization: GEPA, simple optimizer |
| `planners/` | 4 | Planning: ReAct, built-in planner |
| `skills/` | 5 | Experimental skill system (runtime-loadable instructions) |
| `apps/` | 6 | App container: resumability config, event compaction |
| `events/` | 6 | Event model: Event, EventActions, RequestInput |
| `environment/` | 3 | Local environment abstraction |
| `labs/` | 3 | Experimental features (OpenAI LLM adapter) |
| `platform/` | 4 | Platform abstractions: thread, time, uuid |
| `features/` | 3 | Feature flag system (experimental decorator) |

### Naming Conventions

- **Private-by-default**: New Python files in `src/` must be prefixed with `_` (enforced by pre-commit hook `check_new_py_files.sh`)
- **Module exports**: Public API explicitly exported in `__init__.py`; internal cross-module imports use direct module paths (no `__init__.py` imports within framework)
- **Test files**: `test_*.py` in `tests/unittests/` and `tests/integration/`
- **Samples**: snake_case directories under `contributing/samples/` with `agent.py` + `README.md`

---

## 2. Context File Map

### AI Coding Assistant Context

| File | Audience | Scope | Mechanism | Content Type |
|------|----------|-------|-----------|--------------|
| `AGENTS.md` | AI assistants (Gemini, etc.) | Project-wide | Gemini CLI auto-loads via `.gemini/settings.json` | Architecture overview + skill routing |
| `llms.txt` | LLMs | Project-wide | Manual consumption / `llms.txt` convention | Concise project overview (~11KB) |
| `llms-full.txt` | LLMs | Project-wide | Manual consumption | Full docs index with links (~1.2MB) |
| `.gemini/settings.json` | Gemini CLI | Tool config | `contextFileName: "AGENTS.md"` | Points Gemini to AGENTS.md |

### Skills System (`.agents/skills/`)

7 structured skills providing domain-specific context for AI coding assistants:

| Skill | Description | Reference Files |
|-------|-------------|-----------------|
| `adk-architecture` | Core architecture, event flow, state management | 11 reference docs (interfaces, principles, architecture) |
| `adk-agent-builder` | Building agents and workflows | 17 reference docs (patterns, HITL, testing) |
| `adk-style` | Code style, typing, Pydantic, formatting | 9 reference docs |
| `adk-debug` | Debugging agents (CLI + web modes) | Inline (single SKILL.md) |
| `adk-git` | Conventional commits, branch naming | Inline (single SKILL.md) |
| `adk-sample-creator` | Creating sample agents | Inline (single SKILL.md) |
| `adk-setup` | Dev environment setup | Inline (single SKILL.md) |

Each skill follows the structure: `SKILL.md` (entry point with YAML frontmatter) + optional `references/` directory for deep documentation.

### Standard Documentation

| File | Audience | Purpose |
|------|----------|---------|
| `README.md` | Users | Installation, quick start, links |
| `CONTRIBUTING.md` | Contributors | CLA, workflow, testing requirements |
| `contributing/adk_project_overview_and_architecture.md` | Contributors / LLMs | Architecture deep-dive for vibe-coding |
| `contributing/README.md` | Contributors | Contributing resources index |
| `src/google/adk/skills/README.md` | Developers | Experimental skills warning |
| `src/google/adk/labs/README.md` | Developers | Experimental labs warning |

### Sample READMEs

130+ sample directories under `contributing/samples/`, each with its own `README.md` covering:
- Overview, sample inputs, graph visualization (Mermaid), how-to instructions

---

## 3. Workflow Topology

### Framework Execution Model

ADK implements a layered execution architecture:

```
User Message
  -> Runner.run_async()
    -> Runner._exec_with_plugin()        # event persistence, plugin chain
      -> agent.run_async()               # yields events
        -> LlmAgent._run_async_impl()
          -> BaseLlmFlow.run_async()     # flow selection
            -> _AutoFlow or _SingleFlow  # flow implementation
              -> call_llm                # LLM request/response
              -> execute_tools           # tool dispatch
```

### Workflow Runtime (v2.0 -- Graph-Based)

The v2.0 Workflow is a graph-based orchestration engine:

1. **Nodes** (`BaseNode`): Units of execution. Types: FunctionNode, LlmAgentWrapper, JoinNode, ParallelWorker, ToolNode, ScheduleDynamicNode
2. **Edges**: Define transitions with optional routing conditions
3. **Graph**: Compiled from `edges=[("START", node_a, node_b)]` syntax
4. **NodeRunner**: Per-node executor creating child Context, enriching events, managing state
5. **Workflow orchestration loop**: Dispatch ready nodes, collect outputs, handle routing

### Execution Phases

| Phase | Description | Gate |
|-------|-------------|------|
| Graph compilation | Edges parsed into Graph with triggers/routes | Validation (node names must be identifiers) |
| Node dispatch | Ready nodes (all predecessors completed) dispatched concurrently | Trigger evaluation |
| Node execution | NodeRunner creates Context, iterates `node.run()` | Retry config, error handling |
| Output collection | `ctx.output`, `ctx.route`, `ctx.interrupt_ids` read | One output per node |
| Routing | Dict-based conditional edges evaluated | Route value matching |
| Completion | All terminal nodes completed or interrupt propagated | Event persistence |

### Human-in-the-Loop (HITL) Lifecycle

```
1. Interrupt: Node yields RequestInput with long_running_tool_ids
2. Persist: Leaf node's interrupt event saved to session
3. Propagate: Ancestors accumulate interrupt_ids via ctx
4. Resume: User sends FunctionResponse; Runner reconstructs state
5. Continue: Interrupted node receives response, continues execution
```

Two modes:
- **Resumable** (recommended): `App(resumability_config=ResumabilityConfig(is_resumable=True))` -- checkpoints and resumes at interrupted node
- **Non-resumable**: Replays from START using session events

### Multi-Agent Patterns

| Pattern | Mechanism | Use Case |
|---------|-----------|----------|
| Chat Transfer | LLM-driven `transfer_to_agent` | Natural routing between specialized agents |
| Task Delegation | `mode='task'` with structured I/O | Structured sub-agent work with schemas |
| Single Turn | `mode='single_turn'` | Autonomous one-shot execution |
| Sequential | `SequentialAgent(sub_agents=[...])` | Ordered pipeline |
| Parallel | `ParallelAgent(sub_agents=[...])` | Concurrent execution |
| Loop | `LoopAgent(sub_agents=[...], max_iterations=N)` | Iterative refinement |
| Workflow Graph | `Workflow(edges=[...])` | Complex DAG orchestration |

---

## 4. Governance Model

### Constraint Files

| Constraint | Location | Enforcement |
|------------|----------|-------------|
| Private-by-default file naming | `scripts/check_new_py_files.sh` | pre-commit hook |
| Code formatting (pyink, isort) | `.pre-commit-config.yaml` | pre-commit hook |
| License headers | `.pre-commit-config.yaml` (addlicense) | pre-commit hook |
| Markdown formatting | `.pre-commit-config.yaml` (mdformat) | pre-commit hook |
| Type checking | `.github/workflows/mypy.yml` | CI workflow |
| Unit tests | `.github/workflows/python-unit-tests.yml` | CI workflow |
| PR template | `.github/pull_request_template.md` | GitHub enforcement |
| Stale issue/PR management | `.github/workflows/stale-bot.yml` | Automation |
| Release process | release-please configs + cherry-pick workflows | CI-driven |

### Permission Model

- **CLA required**: Google Contributor License Agreement mandatory for all contributions
- **Code review**: All submissions require review via GitHub PRs
- **Testing mandate**: Unit tests + manual E2E required for non-trivial PRs
- **Large changes**: Must open Issue first, gather feedback before implementation

### Guardrails

| Guard | Description | Mechanism |
|-------|-------------|-----------|
| Agent validation | LlmAgent validates configs at construction | `model_validator` in Pydantic |
| LLM call limit | `max_llm_calls` in RunConfig | `LlmCallsLimitExceededError` |
| Node name validation | Must be valid Python identifier | `field_validator` on BaseNode |
| App name validation | Regex + reserved words check | `validate_app_name()` |
| Output schema enforcement | JSON-only mode with response_schema | Controlled generation |
| Feature flags | `@experimental(FeatureName.X)` decorator | Runtime warning/gating |
| Interrupt ID uniqueness | HITL best practice -- unique per iteration | Developer responsibility (documented) |

### API Stability Principles (from `api-principles.md`)

1. Semantic Versioning 2.0.0
2. Breaking changes require MAJOR version bump
3. Self-containment: no cross-package `__init__.py` imports
4. Explicit exports only
5. Intuitive public naming; descriptive private naming

---

## 5. Cross-Agent Protocol

### Agent Roster

ADK defines these agent types in code:

| Agent Type | Class | Role |
|------------|-------|------|
| LLM Agent | `LlmAgent` (aliased as `Agent`) | Primary conversational agent with tools |
| Base Agent | `BaseAgent` | Abstract base for custom agents |
| Sequential Agent | `SequentialAgent` | Run sub-agents in sequence |
| Parallel Agent | `ParallelAgent` | Run sub-agents concurrently |
| Loop Agent | `LoopAgent` | Iterate sub-agents until exit |
| LangGraph Agent | `LanggraphAgent` | Adapter for LangGraph graphs |
| Remote A2A Agent | `RemoteA2AAgent` | Remote agent via A2A protocol |

### Handoff Mechanisms

1. **Transfer-to-Agent** (chat-style): LLM decides transfer via `transfer_to_agent` action in EventActions. Framework switches active agent context.
2. **Task Delegation** (structured): Parent calls `request_task_<name>(args)` tool. Sub-agent receives isolated context with task arguments. Returns via `finish_task` tool.
3. **Workflow Edges** (graph): Explicit edge definitions route between nodes. Node output becomes next node's input.
4. **A2A Protocol** (remote): HTTP-based agent-to-agent communication using `a2a-sdk`. Agent cards describe capabilities.

### Shared State Model

```
InvocationContext (singleton per invocation)
  ├── session          # Full conversation state
  ├── services         # artifact, memory, credential services
  ├── process_queue    # Shared event queue
  └── run_config       # Execution configuration

Context (per-node, tree structure)
  ├── state            # Mutable State (key-value, shared across nodes)
  ├── output           # Node result (set once)
  ├── route            # Routing value for conditional edges
  ├── interrupt_ids    # Accumulated HITL interrupts
  └── resume_inputs    # User responses on resume
```

### Coordination Patterns

| Pattern | Mechanism | Data Flow |
|---------|-----------|-----------|
| State sharing | `ctx.state` (mutable dict) or `Event(state={...})` | All nodes in same invocation share state |
| Output passing | Node output becomes next node's `node_input` | Sequential via graph edges |
| Branch isolation | Events filtered by `branch` field | Parallel nodes see only own history |
| Event stream | Yielded Events persisted and streamed to caller | Runner consumes process_queue |
| Plugin chain | BasePlugin callbacks intercept all agents globally | PluginManager executes in registration order |

### Built-in Agent-Based Tooling

The CLI includes a built-in "ADK Agent Builder Assistant" (`cli/built_in_agents/`) that uses sub-agents (Google Search, URL Context) and tools (explore project, read/write files, search ADK knowledge/source) to help developers build agents interactively.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns |
|-----------|-----------|--------------|
| **Context Engineering** | **High** | Event-to-LLM context orchestration (branch isolation, task delegation translation, history trimming/compaction); 1:1 node-Context mapping; InvocationContext singleton; session state management; `llms.txt` + `llms-full.txt` convention for project context |
| **Model Selection** | **High** | Model-agnostic via `BaseLlm` + LLMRegistry; adapters for Gemini, Anthropic, LiteLLM, Gemma, Apigee; model inheritance in multi-agent hierarchies |
| **Prompt Craft** | **Medium** | Instruction templates with `{state_var}` interpolation; system instruction isolation for task agents; `output_schema` for controlled generation; prompt optimization module (GEPA) |
| **Tool Integration** | **High** | Rich tool ecosystem: FunctionTool, MCP toolset, OpenAPI spec parser, BigQuery/Spanner/Bigtable toolsets, CrewAI/LangChain adapters, Google API toolsets, skill-based tools; tool confirmation HITL; authenticated tools with OAuth2 |
| **Intent Engineering** | **Medium** | Agent `description` drives LLM routing decisions; task mode with structured input/output schemas; output_schema for controlled generation; `output_key` for state-based data flow |
| **Orchestration** | **High** | Graph-based Workflow (v2.0): DAG execution, routing, fan-out/fan-in, loops, retry, dynamic nodes, nested workflows; NodeRunner with two communication channels (Context + Event); checkpoint-resume lifecycle |
| **Evaluation** | **High** | Full eval framework: trajectory evaluators, LLM-as-judge, final response match, hallucination detection, safety evaluation, rubric-based metrics, user simulation with personas, custom metric registry |
| **Sandboxing** | **High** | Multiple code executors: ContainerCodeExecutor (Docker), GKE sandbox, Vertex AI executor, Agent Engine sandbox; `UnsafeLocalCodeExecutor` explicitly named for non-production use; VMaaS sandbox integration |
| **Governance** | **Medium** | API stability principles (SemVer, explicit exports); private-by-default file naming; pre-commit enforcement; feature flag system (`@experimental`); CLA + code review requirements |
| **Agent Design** | **High** | BaseAgent/LlmAgent hierarchy; Pydantic-based configuration; callback chain (before/after model, before/after tool); plugin system for cross-cutting concerns; agent modes (chat, task, single_turn); YAML-based agent config alternative |
| **Agentic Systems** | **High** | Multi-agent coordination: chat transfer, task delegation, workflow graph; A2A protocol for remote agents; parallel execution with branch isolation; shared state via InvocationContext; event-sourced session persistence; resumable workflows |

### Findings Candidates

The following patterns are worth promoting to the Research KB as formal findings:

1. **Event-to-LLM Context Orchestration** (Context Engineering, High Priority)
   - The explicit distinction between "Events as ground truth" and "LLM context as orchestrated view" is a mature architectural pattern. Three strategies (task delegation translation, branch isolation, history compaction) address different context pollution vectors. Directly relevant to our managing-agent-context guide.

2. **Graph-Based Workflow with Checkpoint-Resume** (Orchestration, High Priority)
   - BaseNode contract with `rerun_on_resume`, `wait_for_output`, and `retry_config` provides a well-defined node lifecycle. The two communication channels (Context for parent-child, Event for persistence/streaming) cleanly separate concerns. The HITL interrupt propagation via `interrupt_ids` up the ancestor chain is a novel coordination mechanism.

3. **Skills System for AI Coding Assistants** (Context Engineering, Medium Priority)
   - The `.agents/skills/` directory pattern with YAML-frontmatter SKILL.md files and `references/` subdirectories provides structured, navigable context for AI assistants. The skill naming and trigger description pattern (`description: "Use when..."`) enables routing. Combined with `AGENTS.md` as the top-level router, this forms a layered context architecture for AI-assisted development.

4. **Private-by-Default File Naming with Pre-commit Enforcement** (Governance, Medium Priority)
   - The convention of `_` prefixed Python files for all new modules, enforced by a pre-commit hook script, is a novel approach to API surface control. Combined with explicit `__init__.py` exports, it creates a two-layer visibility system. Relevant to our designing-agent-tools guide (tool surface area control).

5. **Plugin System as Cross-Cutting Concern Manager** (Agent Design, Medium Priority)
   - BasePlugin with ordered execution, short-circuit capability, and change propagation through the callback chain provides a clean separation of cross-cutting behaviors (logging, monitoring, caching, retry) from agent logic. Plugin precedence over agent callbacks with explicit ordering semantics.

6. **Multi-Model Adapter Registry** (Model Selection, Medium Priority)
   - `BaseLlm` + `LLMRegistry` pattern with adapters for multiple providers (Gemini, Anthropic, LiteLLM, Gemma). Model inheritance in multi-agent hierarchies (sub-agents inherit parent model unless overridden). Relevant to model-resilient-prompt-engineering guide.

7. **Code Executor Sandboxing Hierarchy** (Sandboxing, Medium Priority)
   - Explicit hierarchy from `UnsafeLocalCodeExecutor` (named to signal risk) through container-based (Docker), to cloud-managed (GKE, Vertex AI, Agent Engine). The naming convention itself serves as a governance guardrail -- developers must consciously choose the unsafe option.

8. **LLM-Consumable Project Files (`llms.txt` convention)** (Context Engineering, Low-Medium Priority)
   - Two-tier approach: `llms.txt` (concise, 11KB) and `llms-full.txt` (comprehensive, 1.2MB) providing project context at different granularity levels for AI consumption. This is an emerging convention worth tracking.

---

## Summary

ADK-Python is a substantial framework (128k source lines, 594 files) with a mature architecture for multi-agent orchestration. The v2.0 release adds graph-based workflow execution alongside the existing LLM agent abstractions, creating a dual-mode system: conversational (chat transfer) and deterministic (workflow graph).

Key architectural decisions of note:
- **Event sourcing** as the persistence model (events are ground truth; LLM context is a derived view)
- **1:1 Context-Node mapping** with explicit parent-child tree mirroring execution
- **Two communication channels** (Context for orchestration, Events for persistence/streaming)
- **BaseNode contract** unifying agents and functions as graph nodes
- **Plugin system** for cross-cutting concerns with defined precedence rules

The AI coding assistant context layer (AGENTS.md, skills, llms.txt) represents a sophisticated approach to enabling AI-assisted development on a complex codebase -- routing assistants to domain-specific context rather than requiring full codebase comprehension.
