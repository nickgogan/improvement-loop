---
title: "Cross-Repo Structural Comparison"
id: "cross-repo-comparison"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-08"
updated: "2026-04-19"
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
---

# Cross-Repo Structural Comparison

Fourteen agentic tooling repos compared across 6 analysis dimensions. Each repo was analyzed at a specific version using the `/repo-analyzer` skill. This document synthesizes patterns, divergences, and findings candidates across all fourteen.

**Repos analyzed:**

| Repo | Version | Spectrum | Type |
|------|---------|----------|------|
| GSD | v1.33.0 | wholesale | Workflow framework |
| Superpowers | v5.0.7 | thin-wrapper | Skill pack (plugin) |
| BMAD Method | v6.2.2 | cherry-pick | SDLC framework |
| OpenClaw | v2026.4.5 | cherry-pick | Agent platform (product) |
| Paperclip | v2026.403.0 | cherry-pick | Agent company (product) |
| gstack | v0.15.16.0 | cherry-pick | Skill pack (with tooling) |
| mem0 | v1.0.11 | evaluating | Memory service (library) |
| Archon | v0.3.2 | cherry-pick | Workflow platform (multi-adapter) |
| n8n | v2.16.0 | cherry-pick | Workflow automation platform |
| LangGraph | v1.1.6 | cherry-pick | Agent orchestration framework |
| Beads | v1.0.2 | cherry-pick | Multi-agent issue tracker (CLI) |
| OpenViking | latest | cherry-pick | Context database for agents |
| AIO Sandbox | v1.0.0.150 | evaluating | Agent execution sandbox |
| DeerFlow | v2.0 | cherry-pick | Super agent harness |

---

## 1. Comparison Matrix: Structural Scale

| Metric | GSD | SP | BMAD | OC | PC | gs | m0 | Ar | n8n | LG | Beads | OV | Sandbox | DF |
|--------|-----|-----|------|-----|-----|-----|-----|-----|------|-----|-------|-----|---------|-----|
| Total files | 600 | 142 | 559 | 13K | 1.5K | 413 | 1.9K | 745 | 17K | 531 | 1,545 | 1,941 | 1,036 | 891 |
| MD files | 341 | 75 | 418 | 636 | 184 | 90 | 441 | 271 | 220 | 16 | 250 | 176 | 51 | 117 |
| MD % | 56.8 | 52.8 | 74.8 | 4.8 | 12.6 | 21.8 | 22.9 | 36.4 | 1.3 | 3.0 | 16.2 | 9.1 | 4.9 | 13.1 |
| MD:code | 1.64 | 9.4 | 8.5 | 0.05 | 0.18 | 0.49 | 0.08 | 0.78 | 0.02 | 0.05 | 0.24 | 0.13 | 0.07 | 0.20 |
| Max depth | 5 | 4 | 7 | 12 | 7 | 4 | 8 | 8 | 14 | 9 | 5 | 7 | 9 | 10 |
| Primary lang | MD+CJS | MD+Shell | MD+JS | TS | TS | TS | Py | TS+MD | TS+Vue | Py | Go | Py+Rust+C++ | TS+Py | Py+TS |
| Stars | - | - | - | - | - | - | - | - | - | - | 20.9k | 22.6k | 4.3k | 62.7k |

### Four architectural classes (expanded from three)

**Markdown-dominant (MD IS the codebase):** GSD (1.64:1), Superpowers (9.4:1), BMAD (8.5:1). Prompt-native systems where markdown files define agent behavior.

**Markdown-parity (MD + code co-primary):** Archon (0.78:1), gstack (0.49:1). Markdown is a first-class runtime artifact alongside substantial code.

**Code-dominant with rich context files:** Beads (0.24:1), DeerFlow (0.20:1), Paperclip (0.18:1). Substantial code with significant markdown context investment (CLAUDE.md, AGENTS.md, skills, agent definitions).

**Code-dominant (MD supports the codebase):** OpenClaw (0.05:1), mem0 (0.08:1), OpenViking (0.13:1), Sandbox (0.07:1), n8n (0.02:1), LangGraph (0.05:1). Production software where markdown is documentation and configuration.

**New insight from batch 3:** Beads and DeerFlow occupy a middle ground — they're production Go/Python codebases but with deeply invested markdown context systems (Beads: 250 MD files including agent definitions, commands, skills, ADRs; DeerFlow: 117 MD files including 16 public skills with agent personas). This "code-dominant with rich context" class bridges the prompt-native and code-dominant worlds.

---

## 2. Comparison Matrix: Context Loading Strategies

| Repo | Mechanism | Model | What loads at startup | How additional context arrives |
|------|-----------|-------|----------------------|-------------------------------|
| **GSD** | Chain-loading via `@`-references | Push | Command → workflow → references (pre-assembled chain) | Agent prompts include `<files_to_read>` blocks |
| **Superpowers** | Hook-injected bootstrap | Pull | SessionStart hook injects ONE skill (`using-superpowers`) | Agent self-activates skills on demand |
| **BMAD** | Config-driven 3-level progressive disclosure | Hybrid | L1: skill metadata (~100 tokens each). L2: skill body on activation. L3: step files on demand | Step files loaded just-in-time |
| **OpenClaw** | Distributed boundary guides | Cascade | Root AGENTS.md + subsystem AGENTS.md pairs | Skills loaded on demand; workspace templates |
| **Paperclip** | Env-var injection + API | Pull | Onboarding assets (SOUL.md, AGENTS.md, HEARTBEAT.md) | PAPERCLIP_TASK_ID, PAPERCLIP_WAKE_REASON env vars |
| **gstack** | Shell preamble | Push | ~80-line bash preamble on every skill invocation | ETHOS.md injected; learnings searched at start |
| **mem0** | Library API | None | Root AGENTS.md for contributors only | Not applicable |
| **Archon** | Three-tier layered + path-scoped rules | Push | CLAUDE.md (780 lines) + 11 domain rules auto-loaded by path | Agents injected when spawned; skills on trigger |
| **n8n** | Chain-loading with package-scoped distribution | Hybrid | Root CLAUDE.md → `@AGENTS.md` + package-level CLAUDE.md → `@AGENTS.md` | Plugin namespace provides agents, skills, commands |
| **LangGraph** | Minimal dual-file | None | CLAUDE.md and AGENTS.md at root (~58 lines) | No additional context loading |
| **Beads** | Layered progressive-disclosure + live CLI injection | Hybrid | Root CLAUDE.md + AGENTS.md → AGENT_INSTRUCTIONS.md + SessionStart hook runs `bd prime` | SKILL.md → 14 resource files loaded on demand |
| **OpenViking** | Filesystem-as-context-database (L0/L1/L2) | Pull | Workspace files (SOUL/TOOLS/USER/MEMORY/HEARTBEAT) loaded by ContextBuilder | UserPromptSubmit hook auto-recalls memories; Stop hook auto-captures |
| **AIO Sandbox** | None (infrastructure) | N/A | No context files in repo | External skill mounting via `AIO_SKILLS_PATH` |
| **DeerFlow** | Demand-driven injection with XML tags | Hybrid | `apply_prompt_template()` injects SOUL.md, memory, skill catalogue (names only) | Agent calls `read_file` for full SKILL.md; `<memory>` tags |

### Context loading taxonomy (updated with 14 repos)

Seven strategies across 14 repos:

1. **File-chain assembly** (GSD, BMAD, n8n): Context pre-assembled from file references. GSD uses `@`-references; BMAD uses step-file sequential loading; n8n uses CLAUDE.md → `@AGENTS.md` chain-loaders per package.

2. **Hook/preamble injection** (Superpowers, gstack, Beads): Context injected via code execution at session/skill start. Superpowers runs a bash hook; gstack runs a bash preamble; Beads runs `bd prime` via SessionStart hook to generate CLI-aware context from the live binary.

3. **Layered auto-loading** (Archon): Three tiers — massive global CLAUDE.md, domain-scoped rules, and injected specialist agents/skills.

4. **Distributed boundary guides** (OpenClaw): Context scattered across the repo via AGENTS.md/CLAUDE.md symlink pairs at subsystem boundaries.

5. **Runtime context injection** (Paperclip): Context injected via environment variables and API calls at execution time.

6. **Progressive skill loading** (DeerFlow): Skill catalogue (names + descriptions) at boot, full SKILL.md on demand via `read_file`. SOUL.md and memory injected as XML-tagged sections.

7. **Tiered content loading** (OpenViking): Three representation tiers per file/directory (L0 abstract ~100 tokens, L1 overview ~2k, L2 full content). Retrieval traverses tiers progressively.

8. **Minimal/None** (mem0, LangGraph, AIO Sandbox): Little to no context engineering. These are libraries/frameworks/infrastructure.

**New insight:** Beads' `bd prime` is a novel variant — context generated dynamically from the installed CLI binary, not from static files. This ensures context always matches the current version. OpenViking's L0/L1/L2 is the most sophisticated retrieval-based approach. DeerFlow's XML-tagged injection (`<soul>`, `<memory>`, `<skill>`) provides clean semantic boundaries for different context types.

**Push vs. pull spectrum (updated for 14 repos):**

```
Push (harness)  ◄──────────────────────────────────────────────────────►  Pull (agent)
 GSD    Archon  gstack  BMAD   n8n    Beads    DeerFlow  OpenClaw  Paperclip  OpenViking  Superpowers
 (chain) (layered)(preamble)(config)(chain+  (CLI      (XML      (cascade)  (env-var)   (hook-recall) (self-
                                    plugin)  inject)    inject)                                        activate)
```

---

## 3. Comparison Matrix: Orchestration

| Repo | Pattern | Agent count | Coordination | Parallelism |
|------|---------|-------------|-------------|-------------|
| **mem0** | Service | 0 | N/A | Async variants |
| **LangGraph** | Framework (BSP) | 0 (primitives) | Typed channels | Superstep parallelism; Send fan-out |
| **gstack** | Single-agent, role-switching | 1 + specialists | Specialist dispatch | Review Army (7 parallel) |
| **Superpowers** | Orchestrator + disposable workers | 1 + 4 subagent types | Main holds state | Per-task subagents |
| **BMAD** | User-mediated hub | 4 personas + sub-agents | Skill invocation chains | Party Mode (2-4 parallel) |
| **n8n** | Sequential handoff | 2 agents + plan | File-based (plans, specs) + Linear MCP | Turbo build only |
| **GSD** | Hub-and-spoke | 24 named agents | Workflow orchestrators | 4x researchers; wave-based |
| **Archon** | Hub-and-spoke + DAG | 13 specialists + router | DAG `$nodeId.output` variables; worktrees | Topological layer parallelism |
| **OpenClaw** | Gateway-mediated | Multi-agent (isolated) | Gateway routes; ACP spawn | Multi-agent routing |
| **Paperclip** | Hierarchical org chart | CEO + reports | API-mediated (issues, comments) | Multi-agent heartbeats |
| **Beads** | Database-as-shared-memory | N agents (dynamic) | Dolt DB read/write; hash IDs | Fan-out via epic sub-issues; concurrent writers |
| **OpenViking** | Infrastructure (shared memory) | N agents (consumers) | Namespace isolation (`viking://`) | Parallel vector search |
| **AIO Sandbox** | Infrastructure (execution env) | N agents (consumers) | Session UUIDs | Concurrent sessions |
| **DeerFlow** | Orchestrator-worker (batched) | Lead + subagents + ACP | `task` tool calls; ThreadPoolExecutor | 2-4 concurrent subagents; middleware-capped |

### Orchestration spectrum (updated for 14 repos)

```
Manual                                                                                      Autonomous
  │                                                                                            │
  BMAD       gstack    n8n        Superpowers   GSD       Archon    OpenClaw  DeerFlow  Beads  Paperclip
  (user       (user     (human     (agent        (auto     (AI       (gateway  (lead     (db    (heartbeat
   picks)      picks)    gates)     self-acts)    pipeline)  routes)   routes)   dispatches) coords) CEO)
```

**New orchestration patterns from batch 3:**

**Beads introduces database-as-shared-memory coordination.** Unlike file-based (GSD/BMAD) or API-based (Paperclip) coordination, agents coordinate by reading and writing to a shared Dolt database. Hash-based IDs prevent collision without coordination overhead. This is the first database-centric coordination model in the registry.

**DeerFlow introduces middleware-capped batched parallel dispatch.** The lead agent dispatches 2-4 concurrent `task` calls per model response, hard-capped by `SubagentLimitMiddleware`. Subagents are non-recursive, non-interactive, non-presenting — the strictest containment in the registry.

**Three coordination paradigms now clearly emerge:**
- **File-based** (GSD, BMAD, Superpowers, gstack, n8n): Artifacts as handoff
- **Database/API-based** (Beads, Paperclip, OpenClaw, Archon): Structured state shared via DB/API
- **In-process** (DeerFlow, LangGraph): State passed through function calls / graph channels

---

## 4. Comparison Matrix: Governance

| Repo | Constitution? | Hard enforcement | Soft enforcement | Budget/resource | Audit |
|------|--------------|-----------------|-----------------|----------------|-------|
| **GSD** | `.clinerules` | Tool allowlists; 4-gate taxonomy; revision caps | Scope guardrails; anti-patterns | Model profiles | STATE.md + git |
| **Superpowers** | SKILL.md | `<HARD-GATE>` XML; Iron Laws | Rationalization prevention | None | Git |
| **BMAD** | AGENTS.md | 14 deterministic validators | 13 inference validators | None | Artifacts |
| **OpenClaw** | Root AGENTS.md | Plugin SDK boundary; drift detection (SHA-256) | Subsystem boundary guides | Configurable sandboxing | Activity logs |
| **Paperclip** | CEO AGENTS.md | Atomic checkout (409); budget hard-stop; approval gates | Chain of command; definition of done | Budget 80/100% | X-Paperclip-Run-Id |
| **gstack** | ETHOS.md | Freeze/guard; CI validation; E2E evals | ETHOS principles; specialist guides | None | Session markers |
| **mem0** | Root AGENTS.md | Provider pattern; pre-commit hooks | "Do NOT" list | None | Git |
| **Archon** | CLAUDE.md (780 lines) | Zod validation; per-node tool allow/deny; hooks | Engineering principles | None | Immutable sessions DB |
| **n8n** | Root AGENTS.md | ESLint, Biome, strict TS, janitor | Security fix hygiene | None | Git |
| **LangGraph** | CLAUDE.md | Serialization allowlist; typed channels; conformance tests | Formatting rules | None | Checkpoints |
| **Beads** | AGENTS.md + AGENT_INSTRUCTIONS.md | Pre-commit hooks; `bd` CLI constraints; gate system | Repetition-as-enforcement (3x) | None | Dolt version history |
| **OpenViking** | None (infra) | Path locks + RBAC + tenancy isolation; merge_op immutability | Anti-prompt-injection in extraction prompts | None | Transaction redo log |
| **AIO Sandbox** | None (infra) | Resource caps (Docker); JWT auth (optional) | None | mem: 8g, cpu: 4 | None |
| **DeerFlow** | None | Bash audit (regex block/warn); guardrails system; subagent containment; loop detection; skill security scanner | Middleware stack ordering | None | JSONL per skill |

### Five governance philosophies (expanded from four)

1. **Structural enforcement** (GSD, BMAD, OpenClaw, Archon, n8n, LangGraph): Architecture-encoded — tool allowlists, validators, CI checks, typed channels.

2. **Psychological enforcement** (Superpowers): Persuasion-encoded — rationalization prevention, Red Flags, Iron Laws.

3. **Economic enforcement** (Paperclip): Resource-encoded — budget hard-stops, atomic checkout, approval gates.

4. **Specification-as-governance** (LangGraph, n8n): Contract-encoded — conformance tests, spec-driven development.

5. **Middleware-as-enforcement** (DeerFlow): Pipeline-encoded — composable, ordered middleware layers intercept every tool call and model response. 12 layers from error handling through loop detection. Fail-closed defaults. Most sophisticated enforcement pipeline in the registry.

**New governance patterns from batch 3:**

- **Repetition-as-enforcement** (Beads): Critical constraints deliberately repeated across 3+ files. Not duplication debt — conscious design choice to ensure coverage regardless of which file an agent reads.
- **Merge-operation immutability** (OpenViking): Schema-level `merge_op: immutable` on identity fields prevents overwriting. Governance at the data schema level, not the prompt level.
- **Skill security scanner** (DeerFlow): LLM-based scanner classifies new/modified skills as allow/warn/block. Fail-closed on model failure. First automated skill vetting in the registry.
- **Two-tier command audit** (DeerFlow): Regex-pattern auditing with severity levels — high-risk (BLOCK) vs medium-risk (WARN + execute). More granular than binary allow/deny.

---

## 5. Comparison Matrix: Agent Design

| Repo | Identity pattern | Memory system | Execution model |
|------|-----------------|---------------|-----------------|
| **GSD** | YAML + XML sections | STATE.md + git | Spawned per-task |
| **Superpowers** | SKILL.md instructions | Context window only | Self-activated |
| **BMAD** | Persona block (named) | Config + artifacts | User-activated, persona persists |
| **OpenClaw** | 6-file workspace taxonomy | MEMORY.md + daily notes + Dreaming | Continuous agent loop |
| **Paperclip** | SOUL.md + AGENTS.md + HEARTBEAT.md | PARA + knowledge graph + tacit | Heartbeat cycle |
| **gstack** | Template-generated SKILL.md | Cross-session learnings (JSONL) | User-invoked |
| **mem0** | No agent identity | Triple storage (vector + graph + SQLite) | Library API |
| **Archon** | Frontmatter schema (name, model, tools, hooks) | Immutable sessions DB | Spawned by DAG nodes |
| **n8n** | Plugin-namespaced + package-scoped | Plans (gitignored) + specs (committed) | Command-triggered |
| **LangGraph** | Framework primitives | Checkpoints + BaseStore | Graph execution (BSP) |
| **Beads** | Agent bead (state machine) + role bead | Dolt DB (issue fields persist through compaction) | Autonomous task completion |
| **OpenViking** | SOUL/TOOLS/USER/MEMORY/HEARTBEAT workspace files | L0/L1/L2 tiered retrieval + session archives | Continuous (ContextBuilder) |
| **AIO Sandbox** | None (infrastructure) | None (consumer-managed) | Container lifecycle |
| **DeerFlow** | SOUL.md in `<soul>` tags + 12-middleware stack | MemoryMiddleware → async summarization | LangGraph agent loop |

### Identity spectrum (expanded for 14 repos)

```
No identity        Role-based           State machine          Full identity
   │                  │                     │                      │
  mem0, LG,        GSD, gstack,         Beads (formal         OpenClaw (SOUL.md,
  Sandbox           Archon, n8n          FSM + Witness)        Dreaming, daily notes)
  (service/         (functional                                Paperclip (SOUL.md,
   framework/       specialists)         DeerFlow (SOUL.md     PARA, voice/tone)
   infra)                                + middleware stack)    OpenViking (5-file
                                                               workspace taxonomy)
```

**Beads introduces the most formal agent lifecycle.** Agent beads are first-class issue types with a state machine (idle→spawning→running→done/stuck/dead/stopped) and an external Witness monitor. This is the only repo with a named, external liveness monitor that can declare agents dead.

**OpenViking has the richest workspace taxonomy.** Five canonical files (SOUL.md, TOOLS.md, USER.md, MEMORY.md, HEARTBEAT.md) define agent state across identity, capabilities, user context, persistent memory, and periodic tasks. This is the most structured "who is this agent?" specification in the registry.

### Memory architecture comparison (expanded for 14 repos)

| Repo | Persistence | Structure | Consolidation | Scope |
|------|-------------|-----------|---------------|-------|
| GSD | STATE.md (session) | Flat file | None | Per-project |
| Superpowers | None | Context window | None | Per-session |
| BMAD | Config + artifacts | Flat file | Distillator | Per-project |
| OpenClaw | MEMORY.md + daily notes | Flat files | Dreaming (Light→Deep→REM) | Per-agent |
| Paperclip | PARA + knowledge graph | Graph + daily notes + tacit | Weekly synthesis; decay | Per-agent, company |
| gstack | Learnings JSONL | Append-only log | `/learn` skill | Per-project |
| mem0 | Vector + Graph + SQLite | Triple storage | Auto LLM extraction | Scoped (user/agent/run) |
| Archon | SQLite/PostgreSQL | Relational tables | Immutable sessions | Per-conversation |
| n8n | Plans + specs | Flat files + Linear MCP | None | Per-ticket/feature |
| LangGraph | Checkpoints + BaseStore | Typed state + key-value | None built-in | Per-execution |
| Beads | Dolt (SQL + Git) | Relational + versioned | Semantic memory decay | Per-project, cross-repo |
| OpenViking | L0/L1/L2 abstracts + session archives | Tiered retrieval + typed memories | Two-threshold compaction + auto-extraction | Per-account × user × agent |
| AIO Sandbox | None | None | None | N/A |
| DeerFlow | Per-thread/agent store | Summarized conversations | MemoryMiddleware → async updater | Per-thread |

**Memory architecture now spans 5 paradigms:**
1. **File-based** (GSD, Superpowers, BMAD, gstack, n8n): Flat files or JSONL, git-backed
2. **Structured database** (Beads: Dolt, Archon: SQLite/PostgreSQL): SQL with version control
3. **Triple storage** (mem0): Vector + graph + relational, auto-extracted
4. **Tiered retrieval** (OpenViking): L0/L1/L2 progressive loading with session archiving
5. **Graph state** (LangGraph): Typed channels with checkpoint-based time-travel

Beads' Dolt memory is unique: SQL queryability + Git-like version control + cell-level merge = agents can use the database as both working memory and coordination substrate. OpenViking's tiered retrieval is the most bandwidth-efficient — only load detail when needed.

---

## 6. Comparison Matrix: Sandboxing

New dedicated section — with AIO Sandbox, DeerFlow's provisioner, and Archon's worktrees, sandboxing now has enough variation for meaningful comparison.

| Repo | Sandbox model | Isolation level | Container? | Key mechanism |
|------|-------------|----------------|-----------|---------------|
| **GSD** | Git worktrees | Process-level | No | Worktree per execution |
| **Archon** | IsolationResolver + worktrees | Process-level | No | 7-step worktree resolution; branded types |
| **OpenClaw** | Configurable sandboxing | Per-agent | Optional | Auth isolation |
| **Paperclip** | Budget-bounded execution | Economic | No | Budget hard-stop at 100% |
| **AIO Sandbox** | All-in-one container | Container-level | Yes | Single container; shared filesystem; MCP hub |
| **DeerFlow** | Three-tier provisioner | Graduated | Yes | Local → Docker pool (LRU) → Kubernetes |
| **OpenViking** | Shell blocklist + workspace restriction | Process-level | No | Regex command blocklist; `restrictToWorkspace` |
| **Others** | None or minimal | None | No | — |

**Three sandbox architectures:**
1. **Worktree isolation** (GSD, Archon): Git worktrees provide filesystem isolation without containers. Lightweight but limited to file-level isolation.
2. **Container isolation** (AIO Sandbox, DeerFlow): Docker containers provide OS-level isolation. AIO Sandbox is monolithic (all services in one container); DeerFlow is graduated (local → Docker → K8s).
3. **Economic isolation** (Paperclip): No technical sandbox — budget constraints prevent runaway execution.

---

## 7. Pattern Clusters

### Shared Patterns (3+ repos)

| Pattern | Repos | Count |
|---------|-------|-------|
| SKILL.md as standard skill format | GSD, SP, BMAD, OC, PC, gs, m0, Ar, n8n, Beads, OV, DF | 12/14 |
| AGENTS.md / CLAUDE.md as context entry | All 14 except Sandbox | 13/14 |
| Human gate at critical transitions | GSD, SP, BMAD, PC, gs, Ar, n8n, Beads, DF | 9/14 |
| Multi-AI-platform support | SP, BMAD, OC, gs, Ar, n8n, LG | 7/14 |
| Subagent dispatch for review | GSD, SP, BMAD, gs, Ar, n8n, DF | 7/14 |
| Pre-implementation design phase | GSD, SP, BMAD, gs, Ar, n8n | 6/14 |
| Artifact-based handoff | GSD, BMAD, SP, gs, n8n | 5/14 |
| Git as shared state | GSD, SP, BMAD, gs, Ar | 5/14 |
| Verification as independent pass | GSD, SP, BMAD, gs, Ar | 5/14 |
| Kebab-case directories | GSD, SP, BMAD, OC, PC, gs, Ar, n8n, Beads, Sandbox, DF | 11/14 |
| Progressive/tiered context loading | BMAD, OV, DF, Beads | 4/14 |
| Hook-based lifecycle management | SP, gs, Beads, OV | 4/14 |
| SOUL.md or equivalent identity file | OC, PC, OV, DF | 4/14 |
| Memory decay/compaction strategies | Beads, OV, PC, DF | 4/14 |
| Formal agent lifecycle states | Beads, PC, OC, DF | 4/14 |
| Monorepo with package-level context | Ar, n8n, LG | 3/14 |
| MCP server integration | Sandbox, DF, OV | 3/14 |
| Database-backed state management | Beads, Ar, LG | 3/14 |

### New Shared Patterns (emerged with batch 3)

**Progressive/tiered context loading (4/14):** BMAD (L1/L2/L3 step files), OpenViking (L0/L1/L2 abstracts), DeerFlow (skill catalogue → full SKILL.md), Beads (SKILL.md → 14 resource files). Four independent implementations of "load less first, more on demand." This is emerging as a convention.

**Memory decay/compaction strategies (4/14):** Beads (semantic decay — summarize closed tasks), OpenViking (two-threshold compaction — 50% archive, 70% force-clear), Paperclip (weekly synthesis + decay rules), DeerFlow (MemoryMiddleware → async summarization). Four approaches to the same problem: how to manage growing context without losing valuable information.

**MCP server integration (3/14):** AIO Sandbox (MCP Hub aggregating 4 sub-servers), DeerFlow (MCP server support in agent runtime), OpenViking (MCP tools in Claude Code plugin). MCP is becoming infrastructure.

### Unique Patterns (1 repo only — batch 3 additions)

| Pattern | Repo | Description | Innovation |
|---------|------|-------------|------------|
| Database-as-shared-memory | Beads | Dolt DB as coordination substrate; hash IDs; cell-level merge | High |
| ZFC (Zero Framework Cognition) | Beads | All cognitive logic in prompts, code is dumb plumbing | High |
| Agent state machine + Witness | Beads | Formal FSM with external liveness monitor | High |
| Cross-repo issue routing | Beads | `.beads/routes.jsonl` pattern-based routing across repos | High |
| Async gate taxonomy | Beads | Typed gates (timer, CI, PR, human) with polling evaluation | Medium |
| `bd prime` live CLI injection | Beads | Context generated from live binary, not static files | High |
| L0/L1/L2 tiered retrieval | OpenViking | Three-tier progressive content loading with semantic abstracts | High |
| Filesystem-as-context-database | OpenViking | `viking://` URI scheme; directories as namespaces | High |
| 5-file workspace taxonomy | OpenViking | SOUL/TOOLS/USER/MEMORY/HEARTBEAT canonical workspace | Medium |
| Hook-based transparent memory | OpenViking | Three-hook lifecycle for invisible memory inject/capture | High |
| Memory merge_op immutability | OpenViking | Schema-level field immutability prevents identity drift | High |
| Two-threshold compaction | OpenViking | 50% archive (async), 70% force-clear (sync) | High |
| All-in-one sandbox container | AIO Sandbox | Browser+shell+IDE+MCP in one container, shared filesystem | Medium |
| MCP Hub aggregation | AIO Sandbox | Single `/mcp` multiplexes named sub-servers | Medium |
| Auto-generated multi-SDK | AIO Sandbox | Fern generates Python+TS SDKs from OpenAPI spec | Low |
| 12-layer middleware enforcement | DeerFlow | Composable, ordered middleware for agent governance | High |
| Batched parallel subagent dispatch | DeerFlow | 2-4 concurrent `task` calls, hard-capped by middleware | High |
| Three-tier sandbox provisioner | DeerFlow | Local → Docker pool (LRU) → Kubernetes | High |
| Skill security scanner | DeerFlow | LLM-based skill vetting with fail-closed default | High |
| Loop detection hash window | DeerFlow | Sliding window of tool call hashes; warn at 3, stop at 5 | High |
| Progressive skill loading | DeerFlow | Descriptions at boot, full content on-demand via `read_file` | High |

### Contradictory Approaches (updated)

| Problem | Approach A | Approach B | Approach C |
|---------|-----------|-----------|-----------|
| **Coordination substrate** | Files (GSD, BMAD, SP, gs, n8n) | Database (Beads, Ar, LG) | API (PC, OC, DF) |
| **Context loading** | Push everything (GSD, Ar) | Progressive tiers (BMAD, OV, DF, Beads) | Pull on demand (SP, PC) |
| **Governance enforcement** | Structural (GSD, BMAD, OC, Ar, n8n) | Middleware pipeline (DF) | Psychological (SP) |
| **Agent identity** | Ephemeral (GSD, SP, Ar) | Formal FSM (Beads) | Persistent SOUL (OC, PC, OV, DF) |
| **Sandbox architecture** | Worktree (GSD, Ar) | All-in-one container (Sandbox) | Graduated provisioner (DF) |
| **Memory compaction** | Semantic decay (Beads) | Two-threshold (OV) | Async summarization (DF) |
| **Multi-agent coordination** | Shared DB (Beads) | Orchestrator dispatch (DF, GSD) | Infrastructure layer (OV, Sandbox) |

---

## 8. Research Dimension Heat Map

| Dimension | GSD | SP | BMAD | OC | PC | gs | m0 | Ar | n8n | LG | Beads | OV | Sand | DF |
|-----------|-----|-----|------|-----|-----|-----|-----|-----|------|-----|-------|-----|------|-----|
| Context Eng | H | H | H | H | H | H | H | H | H | L | H | **H** | L | **H** |
| Model | M | L | L | H | M | M | H | M | L | L | - | L | - | M |
| Prompt | H | H | H | M | M | H | L | M | H | L | M | M | - | M |
| Tools | M | M | M | H | H | H | H | H | M | H | **H** | M | **H** | **H** |
| Intent | H | H | H | M | H | H | L | H | M | H | **H** | L | - | M |
| Orchestration | H | H | H | H | H | M | L | H | M | H | **H** | L | L | **H** |
| Evaluation | H | H | H | M | M | H | M | H | H | M | M | M | M | **M** |
| Sandboxing | M | M | L | H | H | M | L | H | H | M | L | L | **H** | **H** |
| Governance | H | H | H | H | H | M | L | M | H | M | **H** | **M** | M | **H** |
| Agent Design | H | H | H | H | H | H | M | H | H | H | **H** | **H** | L | **H** |

**H** = High, **M** = Medium, **L** = Low, **-** = None. Bold = new batch.

### Cross-dimension observations (updated for 14 repos)

- **Context Engineering remains High for 12/14 repos.** Only LangGraph and AIO Sandbox are low. Batch 3 adds two of the most sophisticated approaches: OpenViking's L0/L1/L2 tiered retrieval and Beads' live CLI injection + semantic decay.
- **Sandboxing now has 5 High-relevance repos** (OC, PC, Ar, Sandbox, DF) — enough for meaningful comparison. Three distinct architectures (worktree, container, provisioner) are now observable.
- **Governance gains DeerFlow and Beads as strong sources.** DeerFlow's 12-layer middleware is the most sophisticated enforcement pipeline. Beads' ZFC principle and repetition-as-enforcement add conceptual patterns.
- **Progressive/tiered loading is converging.** Four repos (BMAD, OV, DF, Beads) independently implement "load less first, more on demand" — making this the strongest convergent signal in batch 3.

---

## 9. Findings Candidates (Cross-Repo)

### Previously Promoted (CR-1 through CR-14)

All 14 previous cross-repo findings (CR-1 through CR-14) were promoted in sessions 30-32. See individual finding files for current state. The updates below note how batch 3 affects existing findings.

**CR-1 (Context loading non-convergence):** Reinforced — batch 3 adds three more distinct strategies (live CLI injection, L0/L1/L2 tiered retrieval, XML-tagged demand injection). Now 10+ strategies across 14 repos.

**CR-2 (Push vs. pull tradeoff):** OpenViking's hook-based pull model is the most sophisticated pull variant. DeerFlow's XML-tagged hybrid is a clean middle ground. Beads' live CLI injection is a novel variant of push (dynamic, not static).

**CR-3 (Governance enforcement philosophies):** Now five philosophies with DeerFlow's middleware-as-enforcement as the fifth.

**CR-4 (Orchestration correlates with product type):** Beads (CLI tool using database coordination) and DeerFlow (agent harness using orchestrator-worker) confirm the pattern. AIO Sandbox (infrastructure with no orchestration) adds the "infrastructure" class.

**CR-8 (Memory architecture spectrum):** Now five paradigms (file, database, triple-storage, tiered-retrieval, graph-state). Beads' Dolt adds versioned-SQL. OpenViking adds tiered retrieval.

### New Cross-Repo Findings (CR-15 through CR-19)

### CR-15: Progressive/Tiered Context Loading Is Converging

**Dimension:** Context Engineering
**Pattern:** Four repos independently implement progressive loading — loading minimal context first, expanding on demand: BMAD (L1 metadata → L2 body → L3 step files), OpenViking (L0 abstract → L1 overview → L2 full content), DeerFlow (skill descriptions at boot → full SKILL.md via `read_file`), Beads (SKILL.md entry point → 14 resource files on demand). Despite different implementations, all converge on the same principle: don't load everything upfront, and provide multiple resolution levels. This is the strongest convergent signal in the batch 3 analysis.
**Why notable:** Four independent implementations from different orgs (GSD team, ByteDance, Volcengine, Gastown Hall) with no shared ancestry suggests this is a genuine best practice emerging from production experience, not trend-following. Combined with existing findings on tiered-context-injection and deferred-tool-loading, this pattern has 6+ independent implementations across the registry.
→ Promoted to [[progressive-tiered-context-loading-convergence]] on 2026-04-19

### CR-16: Memory Decay/Compaction Is Converging on Multi-Strategy Approaches

**Dimension:** Context Engineering, Agent Design
**Pattern:** Four repos now address context compaction with distinct strategies: Beads (semantic decay — summarize closed tasks, preserve high-impact items), OpenViking (two-threshold — async archive at 50%, forced clear at 70%), Paperclip (weekly synthesis + memory decay rules), DeerFlow (MemoryMiddleware → async summarization per thread). All four go beyond simple truncation — they use semantic understanding to decide what survives compaction. This convergence on "intelligent compaction" (as opposed to FIFO/sliding window) suggests the community has learned that naive compaction loses too much valuable context.
**Why notable:** Each implementation solves a different aspect: Beads focuses on what to keep (importance scoring), OpenViking on when to compact (dual thresholds), Paperclip on consolidation frequency (weekly), DeerFlow on where to persist (per-thread storage). A complete solution might combine all four approaches.
→ Promoted to [[memory-decay-compaction-convergence]] on 2026-04-19

### CR-17: Three Sandbox Architectures for Agent Execution

**Dimension:** Sandboxing
**Pattern:** The registry now has three distinct sandbox architectures: (1) **Worktree isolation** (GSD, Archon) — Git worktrees provide filesystem isolation without containers. Lightweight, no Docker dependency, but limited to file-level isolation. (2) **Monolithic container** (AIO Sandbox) — Single Docker container with all services (browser, shell, IDE, MCP). Shared filesystem enables cross-tool workflows. Trade-off: `seccomp:unconfined` required for browser. (3) **Graduated provisioner** (DeerFlow) — Three-tier provider (local → Docker pool → Kubernetes) behind a unified interface. Configuration-driven isolation level. Most flexible but most complex.
**Why notable:** As agent autonomy increases, sandboxing becomes critical. These three architectures represent different points on the complexity/isolation tradeoff. Worktrees are simplest; containers are most isolated; provisioners are most flexible.
→ Promoted to [[three-sandbox-architectures-comparison]] on 2026-04-19

### CR-18: Middleware vs. Hooks vs. Rules — Three Enforcement Pipelines

**Dimension:** Governance
**Pattern:** Three distinct architectures for enforcing governance at runtime: (1) **Middleware pipeline** (DeerFlow) — 12 composable, ordered layers intercept every tool call and model response. Each layer has specific hook points. Ordering matters. (2) **Event-driven hooks** (Archon, Beads, Superpowers) — PostToolUse/SessionStart/PreCompact hooks fire on specific events. No ordering guarantee between hooks. (3) **Rule-based allowlists** (GSD, BMAD, n8n) — Static rules (tool allowlists, validators, lint) evaluated at invocation time. No interception of ongoing execution.
**Why notable:** These represent increasing sophistication: rules are static, hooks are event-driven, middleware is pipeline-driven. DeerFlow's middleware stack is the most powerful (it can modify, block, or augment any interaction) but also the most complex to reason about (12 layers with ordering dependencies).
→ Promoted to [[three-enforcement-pipeline-architectures]] on 2026-04-19

### CR-19: Agent Lifecycle Formalization Spectrum

**Dimension:** Agent Design
**Pattern:** Four repos formalize agent lifecycle beyond simple "running/done": Beads (full state machine: idle→spawning→running→done/stuck/dead/stopped + external Witness monitor), Paperclip (heartbeat cycle: wake→check→work→exit with CEO delegation), OpenClaw (Dreaming phases: Light→Deep→REM for memory consolidation), DeerFlow (middleware lifecycle: SandboxMiddleware acquires/releases per turn + MemoryMiddleware queues/summarizes post-agent). These represent different facets of lifecycle formalization: Beads focuses on liveness monitoring, Paperclip on work cycles, OpenClaw on memory consolidation, DeerFlow on resource management.
**Why notable:** Most agent systems have binary lifecycle (running or not). These four repos show that production agent systems need richer lifecycle models. The Witness pattern (Beads) is particularly novel — external monitoring that can declare agents dead is a safety mechanism the other repos lack.
→ Promoted to [[agent-lifecycle-formalization-spectrum]] on 2026-04-19

---

## Version Log

| Date | Repos | Notes |
|------|-------|-------|
| 2026-04-08 | GSD, Superpowers, BMAD, OpenClaw, Paperclip, gstack, mem0 (7) | Initial comparison. 8 cross-repo findings candidates. |
| 2026-04-09 | + Archon, n8n, LangGraph (10) | Full regeneration. 6 new candidates (CR-9 through CR-14). |
| 2026-04-19 | + Beads, OpenViking, AIO Sandbox, DeerFlow (14) | Full regeneration. 5 new candidates (CR-15 through CR-19). New architectural class, sandbox comparison matrix, convergence signals on progressive loading and memory decay. |
