---
title: "Cross-Repo Structural Comparison"
id: "cross-repo-comparison"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-09"
updated: "2026-05-25"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "cross-repo"
  - "comparison"
repos_compared:
  - "gsd"
  - "superpowers"
  - "bmad-method"
  - "openclaw"
  - "paperclip"
  - "gstack"
  - "mem0"
  - "archon"
  - "n8n"
  - "langgraph"
  - "beads"
  - "openviking"
  - "sandbox"
  - "deer-flow"
  - "ob1"
  - "memongo"
  - "mempalace"
  - "supermemory"
  - "adk-python"
  - "autogpt"
  - "autogen"
  - "crewai"
  - "letta"
  - "langflow"
  - "deep-tutor"
  - "hermes-agent"
  - "pi-agent"
  - "taches-cc-resources"
  - "warp"
---

# Cross-Repo Structural Comparison

## Metadata
- Repos compared: 29
- Date: 2026-05-25
- Previous comparison: 2026-04-20 (15 repos)

---

## 1. Comparison Matrix

### Structural Scale

Repos grouped by scale to manage table width:

**Large-scale (3000+ files)**

| Metric | n8n | OpenClaw | Langflow | Warp | AutoGPT | CrewAI |
|--------|-----|----------|----------|------|---------|--------|
| Total files | 17,158 | 13,216 | 6,293 | 5,317 | 3,941 | 3,233 |
| MD files | 220 | 636 | ~50 | ~15 | 347 | 96 |
| Code files | 12,536 | 11,328 | 4,205 | 3,299 | 2,889 | 1,188 |
| MD:code ratio | 0.02 | 0.05 | 0.01 | <0.01 | 0.12 | 0.08 |
| Max depth | 14 | 12 | ~10 | ~8 | ~10 | ~8 |
| Primary lang | TS+Vue | TS | Py+TS | Rust | Py+TS | Py |

**Medium-scale (1000-3000 files)**

| Metric | ADK-Python | OpenViking | mem0 | AutoGen | Beads | Paperclip | Letta |
|--------|------------|------------|------|---------|-------|-----------|-------|
| Total files | 2,049 | 1,941 | 1,927 | 1,837 | 1,545 | 1,462 | ~1,185 |
| MD files | 205 | 176 | 441 | 162 | 250 | 184 | ~13 |
| Code files | 1,497 | 1,386 | 855 | 1,168 | 1,061 | 1,024 | ~878 |
| MD:code ratio | 0.14 | 0.13 | 0.52 | 0.14 | 0.24 | 0.18 | 0.01 |
| Max depth | ~6 | 7 | 8 | ~8 | 5 | 7 | ~6 |
| Primary lang | Py | Py+Rust+C++ | Py+TS | Py+C# | Go | TS | Py |

**Small-to-medium (100-1000 files)**

| Metric | AIO Sandbox | DeerFlow | Supermemory | Archon | GSD | BMAD | OB1 | gstack |
|--------|-------------|----------|-------------|--------|-----|------|-----|--------|
| Total files | 1,036 | 891 | 867 | 745 | 600 | 559 | 477 | 413 |
| MD files | 51 | 117 | 28 | 271 | 341 | 418 | 142 | 90 |
| Code files | 769 | 597 | 392 | 348 | 160 | 47 | 76 | 175 |
| MD:code ratio | 0.07 | 0.20 | 0.07 | 0.78 | 1.64 | 8.5 | 1.87 | 0.49 |
| Max depth | 9 | 10 | 17 | 8 | 5 | 7 | 8 | 4 |
| Primary lang | TS+Py | Py+TS | TS | TS+MD | MD+CJS | MD+JS | MD+TS | TS |

**Small / Compact (under 500 files or compact scope)**

| Metric | Memongo | MemPalace | Superpowers | TACHES | DeepTutor | Hermes | Pi Agent |
|--------|---------|-----------|-------------|--------|-----------|--------|----------|
| Total files | 363 | 260 | 142 | ~100 | ~100 | ~80 | ~150 |
| MD files | 60 | 66 | 75 | ~45 | ~8 | ~5 | ~5 |
| Code files | 237 | 116 | 37 | ~15 | ~80 | ~60 | ~130 |
| MD:code ratio | 0.25 | 0.57 | 9.4 | 3.0 | 0.10 | 0.08 | 0.04 |
| Max depth | ~5 | 4 | 4 | 4 | ~4 | ~3 | ~5 |
| Primary lang | TS | Py | MD+Shell | MD | Py | Py | TS |

### Five Architectural Classes (expanded from four)

1. **Markdown-dominant (MD IS the codebase):** GSD (1.64:1), Superpowers (9.4:1), BMAD (8.5:1), OB1 (1.87:1), TACHES (3.0:1). Prompt-native systems where markdown files define agent behavior.

2. **Markdown-parity (MD + code co-primary):** Archon (0.78:1), gstack (0.49:1), MemPalace (0.57:1), mem0 (0.52:1). Markdown is a first-class runtime artifact alongside substantial code.

3. **Code-dominant with rich context layer:** Beads (0.24:1), DeerFlow (0.20:1), Paperclip (0.18:1), Memongo (0.25:1), ADK-Python (0.14:1), AutoGen (0.14:1), OpenViking (0.13:1), AutoGPT (0.12:1). Substantial code with significant markdown context investment.

4. **Code-dominant (MD is documentation):** n8n (0.02:1), OpenClaw (0.05:1), LangGraph (0.05:1), CrewAI (0.08:1), Sandbox (0.07:1), Supermemory (0.07:1), Langflow (0.01:1), Letta (0.01:1), DeepTutor (0.10:1), Hermes (0.08:1), Pi Agent (0.04:1), Warp (<0.01:1). Production software where markdown supports the codebase.

5. **Compiled product (Rust/C++ dominant):** Warp (3,299 Rust files), OpenViking (250 C++ headers). Native performance-critical codebases with agent context as a thin layer on top.

---

### Context File Patterns

| Repo | Context file count | Primary mechanism | Layering strategy | Key pattern |
|------|-------------------|-------------------|-------------------|-------------|
| GSD | ~160 | Chain-loading (`@`-refs) | Command → workflow → agent | Push (pre-assembled chain) |
| Superpowers | ~37 | Hook-injected bootstrap | SessionStart → self-activate | Pull (agent decides) |
| BMAD | ~420 | Config-driven progressive | L1 metadata → L2 body → L3 step files | Hybrid (config-driven) |
| OpenClaw | ~24 pairs | Distributed boundary guides | Root → subsystem AGENTS.md | Cascade (symlink pairs) |
| Paperclip | ~14 | Env-var + API injection | SOUL.md + wake payload | Pull (API-driven) |
| gstack | ~41 | Shell preamble + templates | ETHOS.md → skill-specific | Push (shell execution) |
| mem0 | ~9 | Library API | Root AGENTS.md only | Minimal |
| Archon | ~67 | Three-tier layered | CLAUDE.md → rules → agents/skills | Push (auto-loaded) |
| n8n | ~33 | Chain-loading per package | CLAUDE.md → `@AGENTS.md` + plugins | Hybrid (chain + plugin) |
| LangGraph | 2 | Dual-file identical | CLAUDE.md = AGENTS.md (58 lines) | Minimal |
| Beads | ~30 | CLI injection + progressive | `bd prime` → SKILL.md → 14 resources | Hybrid (live CLI) |
| OpenViking | ~10 | Filesystem-as-context | L0/L1/L2 + workspace files | Pull (tiered retrieval) |
| AIO Sandbox | 0 | External skill mount | `AIO_SKILLS_PATH` env var | None (infrastructure) |
| DeerFlow | ~60 | Demand-driven XML injection | SOUL.md + skill catalogue → full on demand | Hybrid (XML-tagged) |
| OB1 | ~27 | Minimal root + on-demand | CLAUDE.md (50 lines) → skills | Pull (self-contained skills) |
| Memongo | ~5 | Capability x layer matrix | CLAUDE.md + AGENTS.md | Minimal + structured |
| MemPalace | ~10 | Multi-harness plugin | .claude-plugin/ + .codex-plugin/ | Push (hook-injected) |
| Supermemory | ~5 | SKILL-as-package-export | SKILL.md + references/ | Minimal |
| **ADK-Python** | ~140 | Skills + llms.txt | AGENTS.md → .agents/skills/ (7) | Push (skill-routed) |
| **AutoGPT** | ~21 | Hierarchical CLAUDE.md | Root → platform → backend → subsystem | Push (scope-graduated) |
| **AutoGen** | ~5 | .github/copilot-instructions | Design docs in docs/design/ | Minimal |
| **CrewAI** | ~2 | AGENTS.md template | Scaffolded by `crewai create` | Push (version-freshness protocol) |
| **Letta** | ~15 | System prompt templates | Prompt generator assembles sections | Push (template-composed) |
| **Langflow** | ~15 | AGENTS.md + docs/agents/ | Topic-specific sub-docs + skills | Push (layered sub-docs) |
| **DeepTutor** | ~3 | AGENTS.md briefing | Architecture + tool table + CLI | Minimal |
| **Hermes** | ~5 | Layered prompt assembler | Identity → rules → skills → memory | Push (cache-marker layered) |
| **Pi Agent** | ~2 | buildSystemPrompt() | Project context files → skills | Push (code-assembled) |
| **TACHES** | ~45 | Command-as-proxy | Commands → skills → references | Push (thin wrappers) |
| **Warp** | ~15 | WARP.md + skills | Common-skills lock + local overrides | Push (core/specialized) |

### Context Loading Taxonomy (11 strategies across 29 repos)

1. **File-chain assembly** (GSD, BMAD, n8n, TACHES): Context pre-assembled from file references.
2. **Hook/preamble injection** (Superpowers, gstack, Beads, MemPalace): Context injected via code execution at session start.
3. **Layered auto-loading** (Archon, AutoGPT, Langflow): Scope-graduated context per directory level.
4. **Distributed boundary guides** (OpenClaw): AGENTS.md/CLAUDE.md pairs at subsystem boundaries.
5. **Runtime context injection** (Paperclip): Env vars and API calls at execution time.
6. **Progressive skill loading** (DeerFlow, ADK-Python): Skill catalogue at boot, full content on demand.
7. **Tiered content loading** (OpenViking): L0/L1/L2 representation tiers per file.
8. **Minimal root + on-demand** (OB1, DeepTutor, AutoGen, LangGraph, Supermemory, Memongo): Ultra-compact root; skills self-contained.
9. **Template-composed prompt assembly** (Letta, Hermes, Pi Agent, CrewAI): System prompt built programmatically from template sections.
10. **Core/specialized skill inheritance** (Warp): Lock file + common skills + local overrides.
11. **Dual-audience `@`-pointer pattern** (AutoGPT, n8n, CrewAI): CLAUDE.md points to AGENTS.md for cross-tool compatibility.

---

### Workflow Comparison

| Repo | Phases/stages | Human gates | Parallelism | Workflow type |
|------|--------------|-------------|-------------|---------------|
| GSD | 7 (new→discuss→research→plan→execute→verify→complete) | Yes (every boundary) | 4x researchers; wave-based | Linear pipeline |
| Superpowers | 3 (brainstorm→implement→verify) | Yes (brainstorm gate) | Per-task subagents | Orchestrator+workers |
| BMAD | 4 SDLC phases (analysis→plan→solution→implement) | Yes (user-mediated) | Party Mode (2-4) | Linear pipeline |
| OpenClaw | Continuous (gateway-routed) | No formal gates | Multi-agent gateway | Event-driven |
| Paperclip | Heartbeat cycle (wake→check→work→exit) | Yes (board approval) | Multi-adapter parallel | Hierarchical org |
| gstack | 4 (/autoplan: CEO→design→eng→devex) | Yes (taste decisions) | Review Army (7 parallel) | Single-agent role-switch |
| mem0 | N/A (library) | N/A | Async variants | None |
| Archon | DAG workflow engine | Yes (approval gates) | Topological layers | DAG |
| n8n | Sequential handoff | Yes (plan review) | Turbo build | Linear |
| LangGraph | Superstep-based (BSP) | Yes (interrupt/Command) | Within-superstep | Graph (BSP) |
| Beads | Task lifecycle (claim→work→land) | Yes (hard landing gate) | Fan-out via epics | Database-coordinated |
| OpenViking | Continuous (context builder) | No | Parallel vector search | Event-driven |
| AIO Sandbox | Container lifecycle | No | Concurrent sessions | None |
| DeerFlow | Orchestrator-worker | Yes (clarification interrupt) | 2-4 concurrent subagents | Orchestrator+workers |
| OB1 | Skill invocation | Yes (background eval) | Up to 5 background | Single-agent + eval |
| Memongo | N/A (memory library) | N/A | N/A | None |
| MemPalace | N/A (memory library) | N/A | N/A | None |
| Supermemory | N/A (memory service) | N/A | N/A | None |
| **ADK-Python** | Graph-based (node lifecycle) | Yes (interrupt/resume) | Independent nodes parallel | Graph (DAG) |
| **AutoGPT** | Graph execution (block-based) | Yes (HumanInTheLoop block) | Topological sort | Graph (visual DAG) |
| **AutoGen** | Group chat orchestration | Yes (InterventionHandler) | Superstep-parallel | Graph + group chat |
| **CrewAI** | 2 layers (Crews + Flows) | Yes (human_input, guardrails) | @start parallel; wave-based | Linear + event-driven |
| **Letta** | Agent loop (receive→rebuild→call→tool→summarize) | Yes (RequiresApproval rule) | Sleeptime background | Agent loop |
| **Langflow** | DAG execution (vertex scheduling) | No built-in | Concurrent vertex layers | Graph (visual DAG) |
| **DeepTutor** | Capability stages (2-6 per capability) | No (ask_user tool) | StreamBus fan-out | Pipeline per capability |
| **Hermes** | Self-improvement loop (N-task cycle) | No | Single agent | Continuous loop |
| **Pi Agent** | Session tree (branch/compact/navigate) | No | Multi-session concurrent | Interactive loop |
| **TACHES** | Ralph loop (plan→build→observe) | Yes (observation phase) | Parallel subagent dispatch | Autonomous loop |
| **Warp** | Feature flag lifecycle (5 stages) | Yes (PR review) | Oz room agents | Multi-agent rooms |

---

### Governance Comparison

| Repo | Constitution/rules | Enforcement type | Permission model |
|------|-------------------|------------------|-----------------|
| GSD | `.clinerules` | Hard (tool allowlists, 4-gate taxonomy) | Per-agent tool lists |
| Superpowers | SKILL.md Iron Laws | Psychological (`<HARD-GATE>`, rationalization prevention) | Skill-scoped |
| BMAD | AGENTS.md rules | Hard (14 deterministic validators) + Soft (13 inference) | Persona-scoped |
| OpenClaw | Root AGENTS.md | Hard (drift detection SHA-256, plugin SDK boundary) | Plugin boundary |
| Paperclip | CEO AGENTS.md | Economic (budget hard-stop, atomic checkout) | Chain of command |
| gstack | ETHOS.md | Hybrid (freeze/guard + principles) | Per-skill allowed-tools |
| mem0 | Root AGENTS.md | Soft (provider pattern) | Library API |
| Archon | CLAUDE.md (780 lines) | Hard (Zod validation, per-node tool allow/deny) | Per-node tool lists |
| n8n | Root AGENTS.md | Hard (ESLint, Biome, strict TS, janitor) | Package-scoped |
| LangGraph | CLAUDE.md | Hard (serialization allowlist, typed channels) | Tool injection |
| Beads | AGENTS.md | Hard (pre-commit, CLI constraints, gate system) | Maintainer vs contributor |
| OpenViking | None (infra) | Hard (RBAC, path locks, merge_op immutability) | Tenancy isolation |
| AIO Sandbox | None (infra) | Hard (Docker resource caps) | Container-level |
| DeerFlow | None explicit | Hard (12-layer middleware, bash audit, guardrails) | Middleware-filtered |
| OB1 | CLAUDE.md | Two-layer (CI deterministic + LLM judgment) | Skill-scoped |
| Memongo | CLAUDE.md | Soft (guidelines) | None |
| MemPalace | CLAUDE.md + non-negotiables | Hard (performance budgets, retraction log) | Fork-boundary |
| Supermemory | CLAUDE.md | Soft (pre-submit gate) | Tenant isolation |
| **ADK-Python** | API principles doc | Hard (pre-commit hooks, private-by-default naming) | CLA + code review |
| **AutoGPT** | CODEOWNERS + settings.json | Hard (secret detection, CODEOWNERS, AutoMod) | Recursive permission narrowing |
| **AutoGen** | TRANSPARENCY_FAQS.md | Soft (InterventionHandler, trusted namespaces) | Message-level control |
| **CrewAI** | .pre-commit-config | Hard (ruff strict, mypy strict, pip-audit, commitizen) | Per-agent tool lists + delegation flag |
| **Letta** | AI_POLICY.md | Hard (tool rules engine: init/terminal/child/parent/conditional) | Block read-only + char limits |
| **Langflow** | 15 frozen contracts | Hard (frozen component surface, AST security scan, pre-commit) | Component-as-contract |
| **DeepTutor** | None | Soft (pre-commit secrets baseline) | User-toggleable tools |
| **Hermes** | System rules block | Soft (approval model slot) | Model-slot-based |
| **Pi Agent** | AGENTS.md | Hard (supply-chain hardening, auto-close new contributors) | Multi-session git rules |
| **TACHES** | NEVER-modify constraints | Hybrid (audit subagents + heal-skill loop) | Per-command allowed-tools |
| **Warp** | WARP.md + presubmit | Hard (presubmit pipeline, skills-lock) | Core/specialized inheritance |

### Seven Governance Philosophies

1. **Structural enforcement** (GSD, BMAD, OpenClaw, Archon, n8n, LangGraph, ADK-Python, CrewAI, Pi Agent): Tool allowlists, validators, CI checks, typed channels.
2. **Psychological enforcement** (Superpowers): Persuasion-encoded constraints, rationalization prevention.
3. **Economic enforcement** (Paperclip): Budget hard-stops, approval gates.
4. **Specification-as-governance** (LangGraph, n8n, Langflow): Conformance tests, frozen contracts, spec-driven development.
5. **Middleware-as-enforcement** (DeerFlow): Composable pipeline layers intercept every call.
6. **Two-layer split** (OB1, TACHES): Deterministic checks + LLM judgment.
7. **Tool-rule engine** (Letta): Declarative constraint system both rendered into prompt AND enforced programmatically. Dual enforcement (soft + hard) from a single rule set.

---

### Cross-Agent Comparison

| Repo | Agent count | Coordination pattern | Handoff mechanism | Shared state |
|------|-------------|---------------------|-------------------|--------------|
| GSD | 24 named | Hub-and-spoke | Artifact files + completion markers | .planning/ + git |
| Superpowers | 1 + 4 subagent types | Orchestrator+workers | Prompt templates | Context window |
| BMAD | 4 personas + sub | User-mediated hub | Skill invocation chains | Config + artifacts |
| OpenClaw | Multi (isolated) | Gateway routing | ACP spawn | Workspace files |
| Paperclip | CEO + reports | Hierarchical org | API (issues, comments) | Supabase + Git |
| gstack | 1 + specialists | Single + dispatch | Role-switching | Learnings JSONL |
| mem0 | 0 (service) | N/A | Library API | Triple storage |
| Archon | 13 specialists | Hub-and-spoke + DAG | `$nodeId.output` vars | Immutable sessions DB |
| n8n | 2 agents + plan | Sequential handoff | Plans + specs | Linear MCP + git |
| LangGraph | 0 (primitives) | Graph (BSP) | Typed channels | Checkpoints + store |
| Beads | N (dynamic) | Database-as-shared-memory | Dolt DB reads/writes | Dolt DB |
| OpenViking | N (consumers) | Infrastructure | URI scheme (`viking://`) | Tiered retrieval |
| AIO Sandbox | N (consumers) | Infrastructure | Session UUIDs | Container filesystem |
| DeerFlow | Lead + subagents | Orchestrator-worker | `task` tool calls | ThreadPoolExecutor |
| OB1 | 1 (user's client) | Hub-and-spoke (DB) | Supabase MCP | pgvector DB |
| Memongo | N/A | N/A | N/A | N/A |
| MemPalace | N (consumers) | Infrastructure | MCP tools / commands | ChromaDB |
| Supermemory | N (consumers) | Infrastructure | MCP tools | Memory graph |
| **ADK-Python** | 7 types (composable) | Graph + transfer | Transfer-to-agent, task delegation, A2A | InvocationContext + state |
| **AutoGPT** | N (fleet via tmux) | Fleet supervisor + graph | Checkpoint protocol + ORCHESTRATOR:DONE | JSON state file + RabbitMQ |
| **AutoGen** | N (group chat) | 5 patterns (RR, Selector, Swarm, Magentic, DiGraph) | Message routing + handoffs-as-tools | Agent runtime + gRPC |
| **CrewAI** | User-defined per crew | Sequential + hierarchical + flow | Delegation tool + context chaining + A2A | Memory + event bus |
| **Letta** | Multi-agent groups | Round-robin, supervisor, dynamic, sleeptime | `send_message_to_agent_and_wait` | Shared memory blocks |
| **Langflow** | Visual (user-wired) | DAG vertex execution | Graph links (output→input) | Flow state |
| **DeepTutor** | 1 (orchestrator) | Pipeline (orchestrator→capability) | Capability dispatch + StreamBus | UnifiedContext |
| **Hermes** | 1 (multi-channel) | Single agent, multi-entry | Channel-specific history | Tiered memory |
| **Pi Agent** | 1 + extensions | Single + extensions | EventBus + sendMessage() | Session tree |
| **TACHES** | 1 + 3 auditors | Main + audit subagents | Command→skill delegation | File state (whats-next.md) |
| **Warp** | N (Oz agents) | Room-based (@mentions) | Tasks + artifacts + notifications | Room state (SSE) |

---

## 2. Pattern Clusters

### Shared Patterns (3+ repos)

| Pattern | Repos | Count |
|---------|-------|-------|
| SKILL.md as standard skill format | GSD, SP, BMAD, OC, PC, gs, m0, Ar, n8n, Beads, OV, DF, OB1, ADK, CrewAI, TACHES, Warp, MemPalace, Memongo, Supermemory | 20/29 |
| AGENTS.md / CLAUDE.md as context entry | 27 of 29 (all except Sandbox, Hermes) | 27/29 |
| Human gate at critical transitions | GSD, SP, BMAD, PC, gs, Ar, n8n, Beads, DF, OB1, ADK, AutoGPT, AutoGen, CrewAI, Letta, TACHES, Warp | 17/29 |
| Multi-AI-platform support (CLAUDE.md + AGENTS.md + Copilot etc.) | SP, BMAD, OC, gs, Ar, n8n, LG, OB1, AutoGPT, ADK, MemPalace, Warp | 12/29 |
| Graph/DAG-based execution model | LG, ADK, AutoGPT, Langflow, AutoGen, Archon | 6/29 |
| A2A or remote agent protocol | ADK, CrewAI, Warp (Oz), AutoGen (gRPC) | 4/29 |
| Progressive/tiered context loading | BMAD, OV, DF, Beads, ADK, Hermes | 6/29 |
| MCP server integration | Sandbox, DF, OV, OB1, ADK, CrewAI, Letta, Langflow, Memongo, MemPalace, Supermemory, Warp | 12/29 |
| Centralized prompt registry/templates | CrewAI (en.json), Letta (system_prompts/), DeepTutor (prompts/), Hermes (layered assembler) | 4/29 |
| Memory decay/compaction strategies | Beads, OV, PC, DF, Letta, Hermes, CrewAI | 7/29 |
| Pre-commit hook enforcement | GSD, BMAD, n8n, ADK, CrewAI, Langflow, AutoGPT, Pi Agent | 8/29 |
| Subagent dispatch for work | GSD, SP, BMAD, gs, Ar, n8n, DF, AutoGPT, AutoGen, TACHES, Warp | 11/29 |
| Self-improving/self-modifying capabilities | OB1, gs, SP, Hermes, Pi Agent | 5/29 |
| Tool rules / tool allowlists per agent | GSD, Archon, DeerFlow, Letta, CrewAI, AutoGPT | 6/29 |
| Event bus / event-driven observability | CrewAI, Letta, Pi Agent, DeepTutor | 4/29 |
| Provider-agnostic multi-model support | ADK, CrewAI, Letta, AutoGen, mem0, Hermes | 6/29 |
| Docker/container sandboxing | Sandbox, DF, AutoGPT, Letta, n8n, CrewAI | 6/29 |
| Sleeptime / background memory processing | Letta (sleeptime agents), OpenClaw (Dreaming), Hermes (N-task reflection) | 3/29 |
| Three-tier memory hierarchy | Letta (core/recall/archival), Hermes (hot/warm/cold), mem0 (vector/graph/SQLite) | 3/29 |
| Version-freshness protocol for context files | CrewAI (AGENTS.md), ADK (llms.txt) | 2/29 |
| Artifact-based handoff between agents | GSD, BMAD, SP, gs, n8n, TACHES, Warp | 7/29 |

### Unique Patterns (1 repo only -- notable innovations since last comparison)

| Pattern | Repo | Why notable |
|---------|------|-------------|
| Fleet orchestration via tmux + checkpoint protocol | AutoGPT | Production multi-agent coding without custom infrastructure |
| Permission narrowing via recursive inheritance | AutoGPT | Sub-agents can only be MORE restrictive -- prevents privilege escalation |
| Convergence loop with dual clean-poll exit | AutoGPT | Accounts for delayed bot responses creating false "done" signals |
| Declarative tool-rule engine (dual enforcement) | Letta | Rules rendered into prompt AND enforced programmatically |
| Git-backed memory versioning | Letta | Full audit trail via git commits on memory blocks |
| Sleeptime background memory agent (v4) | Letta | Decouples response latency from memory quality |
| Provider-adaptive prompt rendering | Letta | Anthropic gets line numbers; others get standard rendering |
| Auxiliary model slot architecture (8 slots) | Hermes | Per-task-type model assignment (main, compression, vision, approval, router, etc.) |
| Inference-driven memory tier curation | Hermes | Agent itself decides promotion/demotion between memory tiers |
| Runtime self-modification via extension API | Pi Agent | Agent can register/unregister tools and providers at runtime |
| Session tree as first-class abstraction | Pi Agent | Sessions branch, compact, navigate like git |
| Core/specialized skill inheritance | Warp | `specializes` field links to core skill; only overridable categories can change |
| Skills-lock for portable agent skills | Warp | Lock file prevents silent overwrites; version-pinned common skills |
| Oz multi-agent room model | Warp | Agents in rooms, @mentions, kanban tasks, typed artifacts |
| Two-layer plugin model (Tools vs Capabilities) | DeepTutor | Level 1 (single-shot tools) vs Level 2 (multi-stage pipelines) |
| Context-gated vs user-toggleable tool visibility | DeepTutor | Reduces tool noise by auto-mounting only relevant tools |
| Intake-and-decision-gate recursive loop | TACHES | Analyze → ask → gate (Start/Ask more/Add context) -- loops until user chooses |
| Three dedicated audit subagents (skill/command/subagent) | TACHES | Typed specialist auditors for each artifact class |
| Ralph autonomous loop with backpressure | TACHES | Fresh context per iteration; tests as backpressure signal |
| Component-as-contract (frozen public surface) | Langflow | Class names and input names immutable once shipped |
| Policy-guarded tool execution (ToolGuard) | Langflow | Runtime policy enforcement on tool invocation |
| Ledger-based orchestration with stall detection | AutoGen (MagenticOne) | Fact + plan ledgers; detects stuck agents and replans |
| Handoffs-as-tools pattern | AutoGen | Agent delegation expressed as tool calls with descriptions |
| 5 orchestration patterns in one framework | AutoGen | RoundRobin, Selector, Swarm, MagenticOne, DiGraph |
| Event-driven flow orchestration with @listen/@router | CrewAI | Decorator-based DAG with or_()/and_() trigger composition |
| Unified Memory with LLM-analyzed encoding | CrewAI | LLM infers scope/categories/importance at write time |
| Version freshness protocol in AGENTS.md | CrewAI | Instructs AI to check PyPI version before writing code |
| Plugin system as cross-cutting concern manager | ADK-Python | BasePlugin with ordered execution and short-circuit capability |
| Private-by-default file naming (enforced) | ADK-Python | New files must start with `_`; public API via explicit `__init__.py` exports |
| Event-to-LLM context orchestration | ADK-Python | Events as ground truth; LLM context as orchestrated view |
| `llms.txt` + `llms-full.txt` convention | ADK-Python | Two-tier LLM-consumable project files (11KB / 1.2MB) |

### Contradictory Approaches

| Problem | Approach A | Approach B | Approach C |
|---------|-----------|-----------|-----------|
| **Agent coordination** | Files (GSD, BMAD, SP, gs, n8n, TACHES) | Database/API (Beads, PC, OC, Letta, OB1) | In-process/graph (LG, ADK, AutoGen, DF) |
| **Context loading** | Push all upfront (GSD, Ar, AutoGPT) | Progressive tiers (BMAD, OV, DF, Beads, ADK, Hermes) | Minimal + pull (OB1, SP, LG, DeepTutor) |
| **Governance enforcement** | Structural (GSD, BMAD, n8n, ADK, CrewAI) | Middleware pipeline (DF) | Dual enforcement prompt+code (Letta) |
| **Agent identity** | Ephemeral (GSD, SP, Ar) | Persistent SOUL (OC, PC, OV, DF) | Self-improving (OB1, Hermes, Pi) |
| **Multi-agent orchestration** | Explicit graph (LG, ADK, AutoGPT, Langflow, AutoGen) | Hierarchical org (PC, AutoGPT, CrewAI) | Room/chat-based (AutoGen, Warp, CrewAI) |
| **Memory persistence** | Context window only (SP, GSD) | Agent self-manages (Letta, Hermes, OC) | External service (mem0, Supermemory, Memongo) |
| **Tool constraint** | Static allowlists (GSD, Archon, n8n) | Declarative rule engine (Letta) | Middleware interception (DF, ADK) |
| **Workflow definition** | Visual/GUI (AutoGPT, Langflow, n8n) | Code/decorators (CrewAI, LG, ADK) | Markdown files (GSD, BMAD, TACHES) |
| **Sandbox model** | Worktree isolation (GSD, Ar) | Container (Sandbox, DF, Letta, n8n) | Economic constraint (PC) |
| **Prompt management** | Centralized registry (CrewAI, Letta, DeepTutor) | Distributed in agent files (GSD, BMAD, SP) | Code-assembled (ADK, Pi, Hermes) |

---

## 3. Research Dimension Heat Map

Rows = 11 dimensions. Columns grouped by type to manage width.

**Agent Frameworks (build agents with these)**

| Dimension | ADK | AutoGen | CrewAI | LangGraph | Letta | Langflow | DeerFlow |
|-----------|-----|---------|--------|-----------|-------|----------|----------|
| Context Eng | H | H | H | L | H | H | H |
| Model | H | M | H | L | M | M | M |
| Prompt | M | H | H | L | H | M | M |
| Tools | H | H | H | H | H | H | H |
| Intent | M | M | H | H | M | M | M |
| Orchestration | H | H | H | H | H | H | H |
| Evaluation | H | M | H | M | L | M | M |
| Sandboxing | H | H | M | M | H | H | H |
| Governance | M | L | M | M | M | H | H |
| Agent Design | H | H | H | H | H | H | H |
| Agentic Systems | H | H | H | - | H | H | - |

**Coding Agent Harnesses (build software with these)**

| Dimension | GSD | SP | BMAD | Archon | n8n | AutoGPT | TACHES | Warp | Pi |
|-----------|-----|----|------|--------|-----|---------|--------|------|----|
| Context Eng | H | H | H | H | H | H | H | M | M |
| Model | M | L | L | M | L | M | L | L | M |
| Prompt | H | H | H | M | H | H | H | M | L |
| Tools | M | M | M | H | M | H | H | M | M |
| Intent | H | H | H | H | M | M | M | M | L |
| Orchestration | H | H | H | H | M | H | H | M | L |
| Evaluation | H | H | H | H | H | M | H | M | L |
| Sandboxing | M | M | L | H | H | H | M | L | L |
| Governance | H | H | H | M | H | H | M | M | M |
| Agent Design | H | H | H | H | H | H | H | H | M |
| Agentic Systems | - | - | - | - | - | H | M | H | L |

**Agent Platforms and Personal OS**

| Dimension | OpenClaw | Paperclip | OB1 | gstack | Beads | Hermes | DeepTutor |
|-----------|----------|-----------|-----|--------|-------|--------|-----------|
| Context Eng | H | H | M | H | H | H | L |
| Model | H | M | L | M | - | H | L |
| Prompt | M | M | M | H | M | M | L |
| Tools | H | H | H | H | H | M | H |
| Intent | M | H | M | H | H | L | L |
| Orchestration | H | H | L | M | H | L | M |
| Evaluation | M | M | M | H | M | M | L |
| Sandboxing | H | H | L | M | L | L | L |
| Governance | H | H | H | M | H | L | L |
| Agent Design | H | H | H | H | H | H | M |
| Agentic Systems | - | - | H | - | - | M | - |

**Memory and Infrastructure**

| Dimension | mem0 | OpenViking | Memongo | MemPalace | Supermemory | AIO Sandbox |
|-----------|------|------------|---------|-----------|-------------|-------------|
| Context Eng | H | H | M | H | M | L |
| Model | H | L | - | - | L | - |
| Prompt | L | M | - | L | M | - |
| Tools | H | M | M | M | M | H |
| Intent | L | L | L | L | L | - |
| Orchestration | L | L | - | - | - | L |
| Evaluation | M | M | H | VH | H | M |
| Sandboxing | L | L | L | L | L | H |
| Governance | L | M | H | VH | L | M |
| Agent Design | M | H | L | M | H | L |
| Agentic Systems | - | - | - | - | - | - |

**H** = High, **M** = Medium, **L** = Low, **VH** = Very High, **-** = None/Not applicable.

---

## 4. Findings Candidates

Cross-repo patterns visible ONLY at the comparison level -- convergences, divergences, or meta-patterns not apparent from any single analysis.

### Previously Promoted (CR-1 through CR-23)

All 23 previous cross-repo findings remain valid. Updates from the 14 new repos:

- **CR-1 (Context loading non-convergence):** Reinforced further -- now 11 distinct strategies across 29 repos. Template-composed assembly (Letta, Hermes, Pi) and core/specialized inheritance (Warp) are new variants.
- **CR-3 (Governance enforcement philosophies):** Now seven philosophies with Letta's dual-enforcement tool-rule engine as the seventh.
- **CR-8 (Memory architecture spectrum):** Now seven paradigms with Letta's three-tier self-managed hierarchy and Hermes' inference-driven tiered curation as additions.
- **CR-15 (Progressive/tiered loading convergence):** Strengthened to 6 repos (ADK-Python and Hermes add independent implementations).
- **CR-16 (Memory decay/compaction convergence):** Strengthened to 7 repos (Letta, Hermes, CrewAI add implementations).
- **CR-17 (Three sandbox architectures):** Now four -- AutoGPT's fleet approach (tmux worktrees as lightweight containers) adds a distinct pattern.
- **CR-22 (MCP as primary vs supplementary):** MCP now reaches 12/29 repos. Clearly infrastructure-level adoption.

### New Cross-Repo Findings (CR-24 through CR-30)

### CR-24: Graph-Based Execution Engines Converge on Six Repos

**Dimension:** Orchestration
**Pattern:** Six repos independently implement graph/DAG execution engines: LangGraph (Pregel BSP with typed channels), ADK-Python (Workflow with BaseNode contract + NodeRunner), AutoGPT (visual block-based with topological sort), Langflow (vertex scheduling with cycle support), AutoGen (DiGraph team pattern with conditional edges), Archon (YAML DAG with topological layer execution). All share: nodes as computation units, edges as data/control flow, parallel execution of independent nodes, conditional routing. Yet implementation details diverge significantly -- BSP supersteps vs topological layers vs visual canvas vs YAML definition.
**Why notable:** Graph execution for agents is clearly converging as a pattern (6/29), but there is no convergence on execution semantics. The BSP model (LangGraph) is theoretically cleanest; the visual model (AutoGPT, Langflow) is most accessible; the YAML model (Archon) is most portable. A complete understanding requires studying all six.

### CR-25: Dual-Enforcement Governance (Prompt + Code) Emerges as Best Practice

**Dimension:** Governance, Tool Integration
**Pattern:** Three repos now enforce constraints both in the prompt (soft, LLM-cooperating) AND in code (hard, programmatic): Letta (tool rules rendered as XML in prompt AND enforced by ToolRulesSolver), DeerFlow (middleware both logs intent in prompt via `<tool_usage_rules>` AND intercepts at runtime), ADK-Python (agent validation at construction + runtime LLM call limits). Single-channel enforcement (prompt-only or code-only) is the majority pattern. Dual enforcement acknowledges that neither channel is sufficient alone -- prompts can be ignored, code can be circumvented by unexpected input.
**Why notable:** This represents a maturity signal. Early systems rely on prompt compliance (Superpowers, BMAD) or code enforcement (LangGraph, n8n). Production systems that have experienced failures converge on both channels simultaneously.

### CR-26: Provider-Agnostic Multi-Model Architecture Now Standard

**Dimension:** Model Selection
**Pattern:** Six repos implement full provider-agnostic multi-model abstractions with adapter/registry patterns: ADK-Python (BaseLlm + LLMRegistry, 5 adapters), CrewAI (crewai.LLM with 6 native providers + LiteLLM), Letta (27 LLM clients with auto-mode selection), AutoGen (ChatCompletionClient with 7 providers), mem0 (24 LLM + 15 embedding providers), Hermes (8 model slots, any provider). All use abstract base + factory pattern. Per-agent model assignment is common (ADK inheritance, CrewAI per-agent, Hermes per-task-type slots). This is no longer innovative -- it is table stakes for agent frameworks.
**Why notable:** The convergence signal is that this dimension is SOLVED at the framework level. Research value is low for basic multi-model support. The remaining frontier is model-specific optimization (Letta's provider-adaptive rendering, Hermes' task-type slots, CrewAI's separate function_calling_llm).

### CR-27: Background Memory Processing Is a Distinct Architectural Pattern

**Dimension:** Context Engineering, Agent Design
**Pattern:** Three repos implement background/async memory processing where conversation response is decoupled from memory work: Letta (sleeptime agents process memory asynchronously after foreground responds), OpenClaw (Dreaming: Light→Deep→REM runs as background session), Hermes (reflection after N tasks creates/edits skill files). All three solve the same problem: memory management adds latency to conversation. By making it asynchronous, the user gets fast responses while memory quality improves in the background. Letta has evolved this through 4 versions (v1→v4), indicating production refinement.
**Why notable:** This pattern was only visible as "memory decay/compaction" before (CR-16). Separating it as "background memory processing" distinguishes it from synchronous compaction strategies (OpenViking's two-threshold, DeerFlow's middleware). The key architectural decision is whether memory processing blocks the user turn or runs independently.

### CR-28: Event Bus / Observability Layer Is Emerging Infrastructure

**Dimension:** Evaluation, Orchestration
**Pattern:** Four repos implement typed event bus systems for agent observability: CrewAI (singleton `crewai_event_bus` with 17+ typed events, OpenTelemetry on top), Letta (events as ground truth, EventActions), Pi Agent (EventBus for inter-extension communication, 30+ event types), DeepTutor (StreamBus with fan-out to all consumers). ADK-Python achieves similar via Plugin system callbacks. All enable external monitoring without modifying core logic. Three approaches: dedicated bus (CrewAI, DeepTutor), event sourcing (Letta, ADK), extension hooks (Pi).
**Why notable:** Agent observability via events is converging but implementation approaches diverge. The key design tension: bus-based (simple pub/sub) vs event-sourcing (events ARE the state) vs hook-based (extension points). Event sourcing is most powerful (enables replay, time-travel debugging) but most complex.

### CR-29: Agent-to-Agent Protocol (A2A) Adoption Is Early but Multi-Vendor

**Dimension:** Agentic Systems
**Pattern:** Four repos implement cross-system agent communication protocols: ADK-Python (full Google A2A protocol: agent cards, HTTP-based delegation, converters), CrewAI (A2A implementation: polling/push/streaming updates, A2UI extension, auth), AutoGen (gRPC-based distributed runtime with protobuf schemas), Warp (Oz rooms with @mentions, SSE streaming, agent auth). The first two adopt Google's A2A standard; AutoGen uses its own protobuf-defined protocol; Warp uses a custom room-based model. Cross-framework agent interop is still early -- no two frameworks can talk to each other out of the box despite A2A being a "standard."
**Why notable:** A2A protocol adoption signals that the industry expects multi-framework agent ecosystems. But with 3 different protocols across 4 repos (A2A, gRPC/protobuf, custom), standardization is far from complete. The A2A standard has the most momentum (2 adopters from different orgs).

### CR-30: Skills System Design Has Converged on a Common Anatomy

**Dimension:** Agent Design, Context Engineering
**Pattern:** Across 20 repos using SKILL.md, a common anatomy has emerged: YAML frontmatter (name, description, triggers, allowed-tools) + structured body (instructions, process, output format) + optional references/ directory. Variations: ADK-Python adds full `references/` directories with 11+ docs per skill; Warp adds `specializes` field for inheritance; CrewAI adds progressive disclosure levels (METADATA/INSTRUCTIONS/RESOURCES); BMAD adds step-file decomposition for complex workflows; TACHES adds workflow sub-files. The SKILL.md pattern is now the most widely adopted convention in the agentic ecosystem -- more universal than AGENTS.md (which has more naming variations).
**Why notable:** With 20/29 repos using SKILL.md, this is effectively a de facto standard. The remaining innovation space is in: inheritance (Warp), progressive disclosure (CrewAI), workflow decomposition (BMAD, TACHES), and self-improvement (OB1, Hermes). The base pattern is settled.

---

## Version Log

| Date | Repos | Notes |
|------|-------|-------|
| 2026-04-08 | 7 (GSD, Superpowers, BMAD, OpenClaw, Paperclip, gstack, mem0) | Initial comparison. 8 cross-repo findings. |
| 2026-04-09 | 10 (+Archon, n8n, LangGraph) | Full regeneration. CR-9 through CR-14. |
| 2026-04-19 | 14 (+Beads, OpenViking, AIO Sandbox, DeerFlow) | Full regeneration. CR-15 through CR-19. |
| 2026-04-20 | 15 (+OB1) | Incremental. CR-20 through CR-23. |
| 2026-05-25 | 29 (+Memongo, MemPalace, Supermemory, ADK-Python, AutoGPT, AutoGen, CrewAI, Letta, Langflow, DeepTutor, Hermes, Pi Agent, TACHES, Warp) | Full regeneration. 7 new findings (CR-24 through CR-30). 7 governance philosophies. 11 context loading strategies. Graph execution convergence (6 repos). SKILL.md anatomy converges (20 repos). MCP adoption reaches 12/29. |
