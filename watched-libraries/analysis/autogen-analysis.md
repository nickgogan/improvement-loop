---
title: "AutoGen -- Structural Analysis"
id: "autogen-analysis"
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
  - "autogen"
analyzed_version: "v0.7.5"
analyzed_date: "2026-05-25"
repo_url: "https://github.com/microsoft/autogen"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# AutoGen -- Structural Analysis

> **Status:** Maintenance mode. Succeeded by [Microsoft Agent Framework](https://github.com/microsoft/agent-framework). No new features; community-managed going forward.

## 1. Structural Inventory

### Repository Stats

| Metric | Value |
|--------|-------|
| Total files (excl. .git) | 1,837 |
| Python files (.py) | 546 |
| C# files (.cs) | 497 |
| Markdown files (.md) | 162 |
| TypeScript/TSX files | 125 |
| Protobuf files (.proto) | 11 |
| Jupyter notebooks (.ipynb) | 49 |
| JSON config files | 42 |
| YAML/YML files | 41 |
| Total size (with .git) | ~73 MB |

### Top-Level Directory Tree

```
autogen/
├── .azure/pipelines/         # Azure DevOps CI
├── .devcontainer/            # Dev container configs
├── .github/                  # GitHub workflows, templates, copilot-instructions
├── docs/                     # Design docs (programming model, topics, protocol)
│   ├── design/               # 5 architectural design documents
│   └── dotnet/               # .NET-specific documentation
├── dotnet/                   # .NET implementation (full SDK)
│   ├── src/                  # Source projects
│   ├── test/                 # Test projects
│   └── samples/              # .NET samples
├── protos/                   # Shared protobuf definitions (agent_worker.proto, cloudevent.proto)
├── python/                   # Python implementation (primary)
│   ├── packages/             # Monorepo packages (uv workspace)
│   ├── docs/                 # Python docs (Sphinx)
│   ├── samples/              # 18 sample applications
│   └── templates/            # Cookiecutter templates for new packages
├── README.md                 # Main readme (maintenance mode notice)
├── CONTRIBUTING.md           # Contribution guide
├── SECURITY.md               # Microsoft security policy
├── CODE_OF_CONDUCT.md        # Microsoft OSS CoC
├── TRANSPARENCY_FAQS.md      # Responsible AI FAQs
├── FAQ.md                    # User FAQ
└── LICENSE                   # MIT
```

### Python Packages (monorepo via uv workspace)

| Package | Purpose |
|---------|---------|
| `autogen-core` | Core runtime: AgentId, AgentRuntime, message routing, subscriptions, telemetry, Component system, tools, memory, model context |
| `autogen-agentchat` | High-level multi-agent conversation API: agents, teams, conditions, state, UI |
| `autogen-ext` | Extensions: model providers, code executors, MCP tools, memory backends, specialized agents |
| `autogen-studio` | Web-based no-code IDE for building agent workflows |
| `autogen-magentic-one` | MagenticOne multi-agent team (excluded from workspace) |
| `magentic-one-cli` | CLI for running MagenticOne teams |
| `agbench` | Benchmarking suite for agent performance evaluation |
| `pyautogen` | Legacy v0.2 compatibility shim |
| `autogen-test-utils` | Shared test utilities |
| `component-schema-gen` | JSON schema generation for the Component system |

### Naming Conventions

- Python packages: `autogen-{name}` (hyphenated in pyproject.toml)
- Python modules: `autogen_{name}` (underscored in imports)
- Private modules: `_{name}.py` prefix convention
- Config classes: `{ClassName}Config(BaseModel)`
- State classes: `{ClassName}State(BaseState)`
- Component config: `component_config_schema` class variable

---

## 2. Context File Map

### AI/LLM Context Files

| File | Audience | Scope | Mechanism | Content Type |
|------|----------|-------|-----------|--------------|
| `.github/copilot-instructions.md` | GitHub Copilot / AI coding assistants | Repository-wide | Copilot instructions format | Development workflow, timing expectations, validation steps, directory reference |
| `docs/design/01 - Programming Model.md` | Developers/agents | Architectural | Design doc | Pub/sub model, CloudEvents, orchestration concepts |
| `docs/design/02 - Topics.md` | Developers/agents | Architectural | Design doc | Topic/subscription semantics, TopicId, AgentId |
| `docs/design/03 - Agent Worker Protocol.md` | Developers/agents | Architectural | Design doc | Worker/service protocol, agent lifecycle, RPC model |
| `docs/design/04 - Agent and Topic ID Specs.md` | Developers/agents | Architectural | Design doc | ID specifications |
| `docs/design/05 - Services.md` | Developers/agents | Architectural | Design doc | Service layer architecture |

### Human Onboarding / Governance

| File | Audience | Content Type |
|------|----------|--------------|
| `README.md` | Users/contributors | Getting started, quickstart examples, maintenance notice |
| `CONTRIBUTING.md` | Contributors | CLA, CI workflow, versioning, release process |
| `SECURITY.md` | Security researchers | Microsoft MSRC reporting process |
| `CODE_OF_CONDUCT.md` | Community | Microsoft OSS Code of Conduct |
| `TRANSPARENCY_FAQS.md` | Users/regulators | Responsible AI disclosures, limitations, intended uses |
| `FAQ.md` | Users | Common questions |
| `.github/PULL_REQUEST_TEMPLATE.md` | Contributors | PR checklist (docs, tests, checks) |

### Embedded System Prompts / Persona Files

| Location | Purpose |
|----------|---------|
| `autogen_agentchat/teams/_group_chat/_magentic_one/_prompts.py` | MagenticOne orchestrator prompts: task ledger, progress ledger, fact extraction, plan creation |
| `autogen_ext/agents/web_surfer/_prompts.py` | Web surfer agent prompts for multimodal and text-only browsing |
| Default `selector_prompt` in `SelectorGroupChat` | LLM-based speaker selection prompt template |
| `system_message` parameter on `AssistantAgent` | Per-agent system prompt (user-configurable) |

### Key Observation

AutoGen has a single `.github/copilot-instructions.md` file serving as the primary AI-facing context document. It focuses heavily on operational concerns (timing expectations, build commands, directory layout) rather than architectural intent or contribution patterns. There is no CLAUDE.md, AGENTS.md, or dedicated agent-facing architectural guide.

---

## 3. Workflow Topology

### Core Execution Model

AutoGen uses a **publish-subscribe event-driven architecture** with two layers:

1. **Core Layer** (`autogen-core`): Low-level event-driven runtime
   - Agents subscribe to topics (CloudEvents-based)
   - `SingleThreadedAgentRuntime` for local execution
   - gRPC-based distributed runtime for multi-process deployment
   - `InterventionHandler` protocol for message interception/modification/dropping

2. **AgentChat Layer** (`autogen-agentchat`): High-level conversation abstraction
   - `ChatAgent` protocol (stateful agent with `on_messages` / `on_messages_stream`)
   - `Team` abstraction (orchestrates multiple ChatAgents)
   - Pluggable termination conditions
   - State save/restore for pause/resume

### Team Orchestration Patterns

| Pattern | Class | Speaker Selection | Use Case |
|---------|-------|-------------------|----------|
| **Round Robin** | `RoundRobinGroupChat` | Fixed cyclic order | Structured sequential workflows |
| **LLM Selector** | `SelectorGroupChat` | Model-based (with configurable prompt) | Dynamic routing based on conversation |
| **Swarm** | `SwarmGroupChat` | Handoff messages (agent-initiated transfer) | Agent-to-agent delegation |
| **MagenticOne** | `MagenticOneGroupChat` | Orchestrator with ledger (facts + plan + progress) | Complex multi-step problem solving |
| **DiGraph** | `DiGraphGroupChat` (experimental) | Graph-based with conditional edges | DAG and cyclic workflows |

### Phase Model

```
Task Input
  → Team.run() / Team.run_stream()
    → GroupChatManager selects speaker
      → Agent.on_messages() produces Response
        → Response published to all participants
          → Check TerminationCondition
            → If not terminated: loop to speaker selection
            → If terminated: return TaskResult
```

### Termination Conditions (composable via AND/OR)

- `StopMessageTermination` -- agent sends explicit stop
- `MaxMessageTermination` -- turn count limit
- `TextMentionTermination` -- keyword detection
- `HandoffTermination` -- specific handoff target detected
- `TokenUsageTermination` -- token budget exhausted
- `TimeoutTermination` -- wall-clock timeout
- `ExternalTermination` -- external signal (API-driven)
- `SourceMatchTermination` -- specific agent spoke
- `TextMessageTermination` -- any text message produced
- `FunctionCallTermination` -- specific function was called
- `FunctionalTermination` -- arbitrary callable predicate

### Human-in-the-Loop Patterns

1. **UserProxyAgent**: Blocks execution waiting for human input; integrates with FastAPI/ChainLit/Streamlit
2. **HandoffTermination**: Team yields control on handoff, application collects input, team resumes
3. **CodeExecutorAgent.approval_func**: Gate for code execution approval (human or policy)
4. **Pause/Resume**: `Team.pause()` / `Team.resume()` with full state serialization

### State Management

All agents and teams implement state save/restore via Pydantic models:
- `AssistantAgentState` -- model context + tool state
- `TeamState` -- group chat manager state + participant states
- `MagenticOneOrchestratorState` -- facts, plan, progress ledger
- States are JSON-serializable for persistence

---

## 4. Governance Model

### Constraint Files

| File/Mechanism | Type | Scope |
|----------------|------|-------|
| `SECURITY.md` | Security disclosure policy | Microsoft-wide |
| `TRANSPARENCY_FAQS.md` | Responsible AI constraints | Framework-wide |
| `CODE_OF_CONDUCT.md` | Behavioral norms | Community-wide |
| `CONTRIBUTING.md` | Process constraints | Code contribution |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR quality gate | Per-PR |
| Trusted provider namespaces | Code-level security | Component deserialization |

### Permission / Trust Model

**Component System Trust Boundaries:**
- `_TRUSTED_PROVIDER_NAMESPACES` restricts which packages can be deserialized
- Default: `autogen_core.`, `autogen_agentchat.`, `autogen_ext.`, `autogen_studio.`
- Extensible via `AUTOGEN_ALLOWED_PROVIDER_NAMESPACES` env var
- All component providers must be importable Python paths

**Code Execution Sandboxing:**
- `DockerCommandLineCodeExecutor` -- Docker container isolation (recommended)
- `DockerJupyterExecutor` -- Jupyter in Docker
- `LocalCommandLineCodeExecutor` -- Local execution (unsafe, for dev only)
- `AzureContainerCodeExecutor` -- Azure-managed containers
- `CodeExecutorAgent.approval_func` -- Human/policy approval gate before execution

**InterventionHandler (runtime-level guardrails):**
- `on_send` -- intercept direct messages
- `on_publish` -- intercept broadcast messages
- `on_response` -- intercept responses
- Can return `DropMessage` to suppress messages entirely
- Registered at runtime construction time

### Governance Gaps

- No built-in content filtering or safety guardrails (relies on downstream LLM safety)
- No role-based access control for agent capabilities
- No audit trail mechanism beyond telemetry
- Transparency FAQ acknowledges LLM limitations but provides no enforcement mechanism
- Security posture defers to Docker for code execution; no sandboxing for non-code tool calls

---

## 5. Cross-Agent Protocol

### Agent Roster (built-in)

**Core Agents (autogen-agentchat):**
| Agent | Capability |
|-------|-----------|
| `AssistantAgent` | LLM-powered agent with tools, handoffs, memory, structured output |
| `CodeExecutorAgent` | Code generation + sandboxed execution with retry |
| `UserProxyAgent` | Human input bridge |
| `SocietyOfMindAgent` | Wraps an inner team as a single agent (hierarchical composition) |
| `MessageFilterAgent` | Per-source message filtering wrapper (experimental) |

**Extension Agents (autogen-ext):**
| Agent | Capability |
|-------|-----------|
| `MultimodalWebSurfer` | Playwright-based web browsing with visual grounding |
| `FileSurfer` | File system navigation and reading |
| `VideoSurfer` | Video content analysis |
| `MagenticOneCoderAgent` | Code-specialized agent for MagenticOne teams |
| `OpenAIAgent` | OpenAI Assistants API wrapper |
| `OpenAIAssistantAgent` | Legacy OpenAI Assistants wrapper |
| `AzureAIAgent` | Azure AI Agent Service wrapper |

### Handoff Mechanism

AutoGen implements two handoff patterns:

1. **Tool-based Handoff (Swarm pattern):**
   - `Handoff` config creates a `FunctionTool` with name `transfer_to_{target}`
   - Agent calls the handoff tool; produces `HandoffMessage`
   - `SwarmGroupChatManager` routes to the target agent
   - Message to target: "Transferred to {target}, adopting the role of {target} immediately."

2. **LLM-based Selection (Selector pattern):**
   - `SelectorGroupChat` uses an LLM to pick next speaker
   - Default prompt: "You are in a role play game. The following roles are available: {roles}. Read the following conversation. Then select the next role from {participants} to play."
   - Falls back to mention detection (regex matching agent names in output)
   - Configurable with `selector_func` or `candidate_func` for custom logic

### Shared State / Context

**Model Context Strategies:**
| Strategy | Class | Behavior |
|----------|-------|----------|
| Unbounded | `UnboundedChatCompletionContext` | Keep all messages (default) |
| Buffered | `BufferedChatCompletionContext` | Keep last N messages |
| Head+Tail | `HeadAndTailChatCompletionContext` | Keep first N + last M, skip middle |
| Token-limited | `TokenLimitedChatCompletionContext` | Keep messages within token budget |

**Memory System:**
- Abstract `Memory` interface: `update_context()`, `query()`, `add()`, `clear()`
- Implementations: ChromaDB (vector), Redis, Mem0, Canvas (scratchpad), ListMemory
- Memory enriches model context before inference (injected as messages)
- Experimental `TaskCentricMemory`: task-insight pairs for cross-session learning

**Group Chat Shared Context:**
- All participants share messages via pub/sub within the group
- Each agent maintains private model context (their view of conversation)
- `MessageFilterAgent` can restrict which messages an agent sees

### Coordination Patterns

**MagenticOne Orchestrator (most sophisticated):**
1. **Task Ledger** -- Extract facts, classify into: given/verified, to look up, to derive, educated guesses
2. **Plan Creation** -- Bullet-point plan considering team capabilities
3. **Progress Ledger** -- Per-turn structured assessment (JSON):
   - `is_request_satisfied` (bool + reason)
   - `is_in_loop` (bool + reason)
   - `is_progress_being_made` (bool + reason)
   - `next_speaker` (name + reason)
   - `instruction_or_question` (directed instruction)
4. **Stall Detection** -- If stuck, update facts and replan (adaptive replanning)
5. **Final Answer** -- Synthesize result when task is satisfied

**DiGraph (experimental):**
- Directed graph with conditional edges
- Supports: sequential, parallel fan-out, conditional branching, cyclic loops
- Edge conditions: string matching in messages, or arbitrary callables
- Activation groups for complex dependency patterns (all/any semantics)

### Hierarchical Composition

- `SocietyOfMindAgent` wraps an entire team as a single agent
- Inner team runs to completion; outer model summarizes results
- Teams can be participants in other teams (recursive nesting)
- Enables fractal multi-agent architectures

### Serialization / Declarative Config

- All components implement `Component[ConfigT]` pattern
- `ComponentModel` stores: provider (importable path), config (dict), version, label
- Full teams serializable to JSON via `dump_component()` / `load_component()`
- AutoGen Studio uses this for visual team building

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Notable Patterns |
|-----------|-----------|-----------------|
| **Context Engineering** | **High** | 4 model context strategies (unbounded, buffered, head+tail, token-limited); Memory interface with pluggable backends; MessageFilterAgent for per-agent context control; MagenticOne fact/plan ledger |
| **Model Selection** | **Medium** | Provider-agnostic `ChatCompletionClient` interface; 7 model providers (OpenAI, Azure, Anthropic, Ollama, LlamaCpp, SemanticKernel, Replay); `ModelFamily` enum for capability detection |
| **Prompt Craft** | **High** | MagenticOne's structured prompts (task ledger, progress ledger, replan); SelectorGroupChat prompt template with role/history injection; Configurable system messages per agent |
| **Tool Integration** | **High** | `Workbench` abstraction for tool collections; First-class MCP support (stdio, SSE, streamable HTTP); `FunctionTool` from Python callables; Tool overrides; Parallel tool execution; Handoffs-as-tools pattern |
| **Intent Engineering** | **Medium** | Handoff descriptions encode delegation intent; Agent descriptions drive speaker selection; Structured output mode via `output_content_type`; Termination conditions encode completion criteria |
| **Orchestration** | **High** | 5 orchestration patterns (RoundRobin, Selector, Swarm, MagenticOne, DiGraph); Composable termination; Pause/resume with state; SocietyOfMind hierarchical nesting; Graph-based workflow with conditional edges |
| **Evaluation** | **Medium** | `agbench` benchmarking suite; GAIA benchmark integration; Replay model client for deterministic testing; Test utils package |
| **Sandboxing** | **High** | Docker code execution (recommended); Azure Container execution; Jupyter isolation; Approval function gate; InterventionHandler for message-level control |
| **Governance** | **Low** | Trusted provider namespaces for deserialization; TRANSPARENCY_FAQS.md; No built-in content filtering or RBAC |
| **Agent Design** | **High** | Clean `ChatAgent` protocol; Component system for declarative config; State save/restore; Handoff mechanism for delegation; Agent descriptions as capability declarations |
| **Agentic Systems** | **High** | Multi-agent group chat as primary abstraction; MagenticOne ledger-based orchestration with stall detection; Distributed runtime via gRPC; Cross-language (Python/.NET) agent interop via protobuf |

### Findings Candidates

The following patterns are worth considering for promotion to the Research KB:

1. **Ledger-Based Orchestration with Stall Detection (MagenticOne)**
   - Task/fact ledger + progress ledger + adaptive replanning
   - Structured JSON output for orchestration decisions (is_satisfied, is_in_loop, is_progressing, next_speaker, instruction)
   - Replanning triggered by lack of forward progress
   - *Dimensions:* Orchestration, Prompt Craft, Context Engineering

2. **Composable Termination Conditions**
   - Boolean algebra over termination predicates (AND/OR composition)
   - Diverse condition types: token budget, timeout, keyword, handoff, functional
   - Clean protocol: callable that returns Optional[StopMessage]
   - *Dimensions:* Orchestration, Intent Engineering

3. **Model Context Windowing Strategies**
   - Four built-in strategies for conversation truncation
   - HeadAndTailChatCompletionContext preserves both initial instructions and recent messages
   - Handles edge cases (function call results at boundaries)
   - *Dimensions:* Context Engineering

4. **Handoffs-as-Tools Pattern**
   - Agent delegation expressed as tool calls (`transfer_to_{target}`)
   - Enables LLM to reason about when to delegate
   - Produces typed `HandoffMessage` for routing
   - *Dimensions:* Agent Design, Orchestration, Tool Integration

5. **InterventionHandler Protocol**
   - Message-level middleware for the agent runtime
   - Three hooks: on_send, on_publish, on_response
   - Can modify, log, or drop messages (via `DropMessage` sentinel)
   - *Dimensions:* Governance, Sandboxing

6. **Component System for Declarative Agent Configuration**
   - All agents, tools, models, teams serializable to JSON
   - Provider-based instantiation with trusted namespace validation
   - Enables visual builders (AutoGen Studio) and config-as-code
   - Version-aware deserialization
   - *Dimensions:* Agent Design, Agentic Systems

7. **DiGraph-Based Workflow with Activation Groups**
   - Directed graph orchestration with conditional edges (string or callable)
   - Activation groups for complex dependency patterns
   - `all`/`any` semantics for multi-path convergence
   - Supports cycles with safe exit conditions
   - *Dimensions:* Orchestration, Agentic Systems

8. **SocietyOfMind Hierarchical Composition**
   - Entire team wrapped as a single ChatAgent
   - Inner team runs to completion; outer model summarizes
   - Enables recursive multi-agent architectures
   - *Dimensions:* Agent Design, Orchestration

---

## Summary

AutoGen (v0.7.5) represents a mature multi-agent framework now in maintenance mode, succeeded by Microsoft Agent Framework. Its architecture is notable for:

**Strengths:**
- Clean separation between core runtime (pub/sub events) and high-level chat abstraction
- Rich orchestration pattern library (5 team types from simple to sophisticated)
- First-class MCP tool integration and multiple code execution sandboxing options
- MagenticOne's ledger-based orchestration with stall detection is a sophisticated meta-cognitive pattern
- Strong serialization story via the Component system
- Multiple model context windowing strategies

**Limitations:**
- Maintenance mode means no new features or active development
- No built-in content safety/guardrails beyond Docker sandboxing for code
- No A2A protocol support (this lives in the successor, Microsoft Agent Framework)
- Governance is minimal -- relies on downstream LLM safety
- AI context documentation is limited to a single copilot-instructions.md focused on operations rather than architecture

**Research Value:**
The orchestration patterns (especially MagenticOne's ledger and DiGraph), the composable termination system, and the handoffs-as-tools mechanism are the highest-value patterns for the IL knowledge base. The maintenance mode status means these patterns are frozen -- useful as reference implementations but unlikely to evolve further.
