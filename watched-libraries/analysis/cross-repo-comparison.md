---
title: "Cross-Repo Structural Comparison"
id: "cross-repo-comparison"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-08"
updated: "2026-04-09"
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
---

# Cross-Repo Structural Comparison

Ten agentic tooling repos compared across 6 analysis dimensions. Each repo was analyzed at a specific version using the `/repo-analyzer` skill. This document synthesizes patterns, divergences, and findings candidates across all ten.

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

---

## 1. Comparison Matrix: Structural Scale

| Metric | GSD | Superpowers | BMAD | OpenClaw | Paperclip | gstack | mem0 | Archon | n8n | LangGraph |
|--------|-----|-------------|------|----------|-----------|--------|------|--------|-----|-----------|
| Total files | 600 | 142 | 559 | 13,216 | 1,462 | 413 | 1,927 | 745 | 17,158 | 531 |
| Markdown files | 341 | 75 | 418 | 636 | 184 | 90 | 441 | 271 | 220 | 16 |
| MD % of total | 56.8% | 52.8% | 74.8% | 4.8% | 12.6% | 21.8% | 22.9% | 36.4% | 1.3% | 3.0% |
| MD:code ratio | 1.64:1 | 9.4:1 | 8.5:1 | 0.054:1 | 0.18:1 | 0.49:1 | 0.08:1 | 0.78:1 | 0.017:1 | 0.049:1 |
| Max depth | 5 | 4 | 7 | 12 | 7 | 4 | 8 | 8 | 14 | 9 |
| Primary language | MD+CJS | MD+Shell | MD+JS | TypeScript | TypeScript | TypeScript | Python | TS+MD | TypeScript+Vue | Python |
| Skills/agents | 24 agents, 70 cmds | 14 skills, 1 agent | 41 skills | 53+8 skills | 10 skills | 41 skills | 9 skills | 13 agents, 7 skills, 21 workflows | 2 agents, 11 skills | 0 (framework primitives) |

### Three architectural classes

The repos now split into three groups by MD:code ratio:

**Markdown-dominant (MD IS the codebase):** GSD (1.64:1), Superpowers (9.4:1), BMAD (8.5:1). Code is glue — the framework is its prompts. These are "prompt-native" systems where the markdown files define agent behavior, not documentation.

**Markdown-parity (MD + code co-primary):** Archon (0.78:1), gstack (0.49:1). Markdown is a first-class runtime artifact (agent definitions, workflow commands) but substantial TypeScript code provides the execution engine. These are hybrid systems where both markdown and code carry behavioral weight.

**Code-dominant (MD supports the codebase):** OpenClaw (0.054:1), Paperclip (0.18:1), mem0 (0.08:1), n8n (0.017:1), LangGraph (0.049:1). These are production software products where markdown provides context files, skills, and documentation — but TypeScript/Python is the runtime.

**Implication:** The prompt-native systems (GSD, Superpowers, BMAD) are the richest sources for context engineering, prompt design, and agent design patterns. The code-dominant platforms (OpenClaw, Paperclip, n8n, LangGraph) are richer for orchestration infrastructure, sandboxing, and governance enforcement. The hybrid systems (Archon, gstack) bridge both — Archon's YAML workflow engine with markdown commands is a notable middle ground.

**Scale spectrum:** n8n (17,158 files) and OpenClaw (13,216 files) are production platforms orders of magnitude larger than the others. LangGraph (531 files) and Superpowers (142 files) are the most focused. Repo size does not correlate with pattern richness — Superpowers has more novel governance patterns than n8n despite being 120x smaller.

---

## 2. Comparison Matrix: Context Loading Strategies

| Repo | Mechanism | Model | What loads at startup | How additional context arrives |
|------|-----------|-------|----------------------|-------------------------------|
| **GSD** | Chain-loading via `@`-references | Push | Command → workflow → references (pre-assembled chain) | Agent prompts include `<files_to_read>` blocks |
| **Superpowers** | Hook-injected bootstrap | Pull | SessionStart hook injects ONE skill (`using-superpowers`) | Agent self-activates skills on demand ("1% chance → invoke") |
| **BMAD** | Config-driven 3-level progressive disclosure | Hybrid | L1: skill metadata (~100 tokens each). L2: skill body on activation (<5K). L3: step files on demand | Step files loaded just-in-time; config.yaml resolves user preferences |
| **OpenClaw** | Distributed boundary guides | Cascade | Root AGENTS.md (~300 lines) + subsystem AGENTS.md pairs | Skills loaded on demand; workspace templates for deployed agents |
| **Paperclip** | Env-var injection + API | Pull | Onboarding assets (SOUL.md, AGENTS.md, HEARTBEAT.md) on agent creation | PAPERCLIP_TASK_ID, PAPERCLIP_WAKE_REASON env vars + heartbeat-context API |
| **gstack** | Shell preamble | Push | ~80-line bash preamble runs on every skill invocation (config, learnings, session, repo mode) | ETHOS.md injected into all skills; learnings searched at skill start |
| **mem0** | Library API | None | Root AGENTS.md for contributors only | Not applicable — service consumed by other agents |
| **Archon** | Three-tier layered + path-scoped rules | Push | CLAUDE.md (780 lines) + 11 domain rules auto-loaded by path | Agents injected when spawned; skills injected on trigger; `archon-dev` meta-routes to cookbooks |
| **n8n** | Chain-loading with package-scoped distribution | Hybrid | Root CLAUDE.md → `@AGENTS.md` + package-level CLAUDE.md → `@AGENTS.md` | Plugin namespace (`.claude/plugins/n8n/`) provides agents, skills, commands; templates for scaffolding |
| **LangGraph** | Minimal dual-file | None | CLAUDE.md and AGENTS.md at root (identical content, ~58 lines) | No additional context loading |

### Context loading taxonomy (updated)

These ten mechanisms cluster into five strategies:

1. **File-chain assembly** (GSD, BMAD, n8n): Context pre-assembled from file references at invocation time. GSD uses `@`-references; BMAD uses step-file sequential loading; n8n uses CLAUDE.md → `@AGENTS.md` chain-loaders distributed per monorepo package. n8n's chain-loading is the most sophisticated — it solves the naming constraint (Claude Code auto-loads CLAUDE.md) while keeping content in a cross-tool-compatible filename (AGENTS.md).

2. **Hook/preamble injection** (Superpowers, gstack): Context injected via code execution at session/skill start. Superpowers runs a bash hook that injects one skill; gstack runs a bash preamble that assembles config, learnings, and session state.

3. **Layered auto-loading** (Archon): Three tiers — massive global CLAUDE.md (780 lines), domain-scoped rules (auto-loaded by path), and injected specialist agents/skills. The `archon-dev` skill adds a fourth layer: intent-based routing to 10 cookbooks. Most layers within a single repo.

4. **Distributed boundary guides** (OpenClaw): Context scattered across the repo via AGENTS.md/CLAUDE.md symlink pairs at subsystem boundaries. Progressive disclosure — you see rules for where you are, not rules for everywhere.

5. **Runtime context injection** (Paperclip): Context injected via environment variables and API calls at execution time. No file loading — the server provides compact state on demand.

6. **Minimal** (mem0, LangGraph): Little to no context engineering. These are libraries/frameworks — their value is in runtime architecture, not development tooling.

**Push vs. pull spectrum (updated):**

```
Push (harness assembles)  ◄──────────────────────────────────────────►  Pull (agent decides)
 GSD       Archon    gstack     BMAD      n8n       OpenClaw    Paperclip   Superpowers
 (chain)   (layered) (preamble) (config)  (chain+   (cascade)   (env-var)   (self-activate)
                                          plugin)
```

**New insight from Archon and n8n:** Both are push-leaning but with distinct strategies. Archon loads aggressively (780-line CLAUDE.md + 11 domain rules), trusting Claude Code's path-scoped rule loading to keep domain rules relevant. n8n distributes context per package, trusting that Claude Code loads the right CLAUDE.md for where you're working. Archon's approach risks token waste on irrelevant rules; n8n's approach risks missing cross-cutting concerns. These represent two different solutions to monorepo context engineering.

**Cross-platform context mirroring:** Both Archon and n8n maintain parallel context for multiple AI tools — Archon mirrors `.claude/agents/` to `.github/agents/` and `.github/prompts/`; n8n uses plugin namespacing plus the CLAUDE.md→AGENTS.md pattern for cross-tool compatibility. LangGraph takes the simplest approach: identical CLAUDE.md and AGENTS.md files. This cross-platform concern didn't exist in the original 7-repo comparison.

---

## 3. Comparison Matrix: Orchestration

| Repo | Pattern | Agent count | Human role | Agent coordination | Parallelism |
|------|---------|-------------|------------|-------------------|-------------|
| **mem0** | Service | 0 (consumed by others) | N/A | N/A | Async variants |
| **LangGraph** | Framework (BSP) | 0 (primitives for building) | `interrupt()` → `Command` | Typed channels between nodes | Superstep parallelism; Send fan-out |
| **gstack** | Single-agent, role-switching | 1 primary + specialists | User invokes skills; decides on taste | Specialist dispatch during review | Review Army (7 parallel) |
| **Superpowers** | Orchestrator + disposable workers | 1 main + 4 subagent types | User approves designs; reviews diffs | Main agent manages all state | Per-task subagents (sequential default) |
| **BMAD** | User-mediated hub | 4 named personas + sub-agents | User IS the orchestrator — activates personas, selects capabilities | Skill invocation chains | Party Mode (2-4 parallel); Distillator fan-out |
| **n8n** | Sequential handoff with human gates | 2 agents + plan agent | Reviews plans, approves PRs, guides triage | File-based (plans, specs) + Linear MCP | Turbo build parallelism only |
| **GSD** | Hub-and-spoke | 24 named agents | Human gates at phase boundaries | Workflow orchestrators spawn agents | 4x researchers; wave-based execution |
| **Archon** | Hub-and-spoke with DAG execution | 13 specialists + AI router | Approval nodes in workflows; CLI user | DAG `$nodeId.output` variable passing; worktree isolation | Topological layer parallelism; multi-workflow via worktrees |
| **OpenClaw** | Gateway-mediated | Multi-agent (isolated) | Per-skill; can review DREAMS.md | Gateway routes; agents isolated | Multi-agent routing; ACP spawn |
| **Paperclip** | Hierarchical org chart | CEO + reports (CTO, CMO, UX) | Board approves; CEO delegates | API-mediated (issues, comments, checkout) | Multi-agent concurrent heartbeats |

### Orchestration spectrum (ordered by automation)

```
Manual                                                                           Autonomous
  │                                                                                │
  BMAD       gstack      n8n          Superpowers    GSD        Archon    OpenClaw  Paperclip
  (user picks (user picks (human gates  (agent self-  (automated (AI routes (gateway  (heartbeat-
   personas)   skills)    each stage)   activates)    pipeline)   to DAGs)   routes)   driven, CEO
                                                                                       delegates)
```

**New orchestration patterns from the three additions:**

**Archon introduces DAG-based workflow orchestration.** Unlike GSD's predefined phase sequences or Paperclip's heartbeat cycles, Archon defines workflows as YAML DAGs with typed nodes (AI prompts, bash scripts, TypeScript, approval gates). Independent nodes execute in parallel within topological layers. This is the first concrete implementation of composable AI+deterministic workflow authoring in the registry.

**LangGraph introduces BSP (Bulk Synchronous Parallel) orchestration.** Borrowed from distributed computing (Google's Pregel paper), this is fundamentally different from every other pattern here. Nodes execute in parallel supersteps, communicate via typed channels, and synchronize at barriers. It's the only framework-level orchestration model — the others all define specific agent behaviors.

**n8n introduces spec-driven development as an orchestration pattern.** While n8n's agent count is low (2 agents + plan), the spec-driven development skill creates a bidirectional sync loop between `.claude/specs/` and implementation code. Specs serve as living architectural decisions that persist across sessions. This is intent-as-orchestration.

**Coordination mechanism correlates with product type (updated):**
- Frameworks (GSD, BMAD) use file-based coordination (artifacts as handoff)
- Platforms with workflow engines (Archon, n8n) use structured workflows (DAGs, specs)
- Products (OpenClaw, Paperclip) use API-based coordination (database, REST endpoints)
- Skill packs (Superpowers, gstack) use context-window coordination (main agent holds state)
- Libraries/frameworks (LangGraph, mem0) use programmatic coordination (typed channels, library API)

---

## 4. Comparison Matrix: Governance

| Repo | Constitution? | Hard enforcement | Soft enforcement | Budget/resource governance | Audit trail |
|------|--------------|-----------------|-----------------|---------------------------|-------------|
| **GSD** | `.clinerules` | Tool allowlists per agent; 4-gate taxonomy; revision caps | Scope guardrails; anti-patterns; context budget | Model profiles (quality/balanced/budget) | STATE.md + git commits |
| **Superpowers** | `using-superpowers` SKILL.md | `<HARD-GATE>` XML tags; Iron Laws | Rationalization prevention tables; Red Flags | None | Git only |
| **BMAD** | `AGENTS.md` + skill validator | 14 deterministic validator rules; sequential enforcement | 13 inference validator rules; persona persistence | None | Produced artifacts |
| **OpenClaw** | Root `AGENTS.md` (~300 lines) | Plugin SDK boundary; CI architecture checks; drift detection (SHA-256) | Subsystem boundary guides | Configurable sandboxing; auth isolation | Activity logs; PR maintainer evidence bar |
| **Paperclip** | CEO `AGENTS.md` | Atomic checkout (409); budget hard-stop; approval gates; run ID audit | Chain of command; definition of done | Budget hard-stop at 100%; critical-only above 80% | X-Paperclip-Run-Id on every mutation |
| **gstack** | `ETHOS.md` | Freeze/guard (directory lock); CI skill validation; E2E evals | Careful (destructive warnings); ETHOS principles; specialist guides | None | Session markers; analytics |
| **mem0** | Root `AGENTS.md` | Provider pattern (abstract classes); pre-commit hooks | "Do NOT" list; PR template | None | Git only |
| **Archon** | `CLAUDE.md` (780 lines) | Zod schema validation; CI gate (`bun run validate`); per-node tool allow/deny; hook-based validation | Engineering principles (KISS, YAGNI, DRY); domain rules | None | Immutable sessions; workflow events DB |
| **n8n** | Root `AGENTS.md` + package AGENTS.md | ESLint, Biome, TypeScript strict, lefthook, janitor static analysis | Security fix hygiene rules; design system token enforcement; Linear priority caps | None | Git only |
| **LangGraph** | `CLAUDE.md` / `AGENTS.md` | Serialization allowlist (SAFE_MSGPACK_TYPES); typed channels; conformance tests; Zod/Pydantic validation | Formatting rules only | None | Checkpoint state |

### Four governance philosophies (expanded from three)

1. **Structural enforcement** (GSD, BMAD, OpenClaw, Archon, n8n, LangGraph): Governance encoded in architecture — tool allowlists, validator rules, CI boundary checks, SDK contracts, Zod schemas, typed channels. Hard to bypass because it's not just instructions.

2. **Psychological enforcement** (Superpowers): Governance encoded in persuasion — rationalization prevention, Red Flags, Iron Laws, `<HARD-GATE>` tags. Based on Meincke et al. (2025) research showing 33%→72% compliance improvement. Novel approach: acknowledges that LLMs rationalize rule-breaking and proactively blocks common evasion patterns.

3. **Economic enforcement** (Paperclip): Governance encoded in resource constraints — budget hard-stops, atomic checkout exclusion, approval gates with board oversight. The agent can't overspend because the server stops it.

4. **Specification-as-governance** (LangGraph, n8n): Governance encoded in specs and conformance tests. LangGraph's `checkpoint-conformance` test suite defines what implementations must do. n8n's spec-driven development skill enforces bidirectional sync between specs and code. This is governance by contract — compliance is verified, not just instructed.

**New governance patterns from the additions:**

- **Per-node tool restrictions** (Archon): Workflow YAML nodes specify `allowed_tools`/`denied_tools`. The orchestrator routing call uses `tools: []` to prevent tool use during classification. This is the most granular tool-level governance in the registry.
- **Hook-based enforcement** (Archon): The triage agent's `PostToolUse` hook validates label application after every Bash call. Enforcement happens after execution, not before.
- **Security fix hygiene** (n8n): Explicit rules for public repos: neutral branch names, commit messages, test descriptions to prevent attackers from monitoring for vulnerability signals. A governance pattern specific to open-source.
- **Auto-generated threat model** (LangGraph): `.github/THREAT_MODEL.md` with trust boundaries, component inventory, data classification, and specific threats. No other repo has a formal threat model.

---

## 5. Comparison Matrix: Agent Design

| Repo | Agent identity pattern | Persona depth | Memory system | Execution model |
|------|----------------------|---------------|---------------|-----------------|
| **GSD** | YAML frontmatter + XML sections | Role-based (Executor, Planner, Verifier) | `.planning/STATE.md` + git | Spawned per-task, fresh context |
| **Superpowers** | SKILL.md instructions | Capability-based (brainstorming, TDD, verification) | Git only; context window | Self-activated on demand |
| **BMAD** | SKILL.md with persona block | Named personas (Mary, John, Winston, Amelia) with communication styles | `_bmad/` config + produced artifacts | User-activated, persona persists |
| **OpenClaw** | 6-file workspace taxonomy | SOUL.md for personality; "guest" metaphor | MEMORY.md + daily notes + Dreaming (Light→Deep→REM) | Continuous agent loop; heartbeats |
| **Paperclip** | Onboarding assets (SOUL.md, AGENTS.md, HEARTBEAT.md) | CEO with strategic posture, voice/tone, P&L ownership | PARA-based (knowledge graph + daily notes + tacit) | Heartbeat cycle (wake, check, work, exit) |
| **gstack** | Template-generated SKILL.md | Role-switching (CEO, designer, engineer, QA, CSO) | Cross-session learnings (JSONL) | User-invoked skills |
| **mem0** | No agent identity (service) | N/A | Triple storage (vector + graph + SQLite); scoped by user/agent/run | Library API calls |
| **Archon** | Frontmatter schema (name, description, model, tools, hooks) | Role-based specialists (reviewer, triager, analyst, etc.) with model selection | Immutable sessions DB; workflow events DB | Spawned by workflow nodes; fresh context per node (`fresh_context`) |
| **n8n** | Plugin-namespaced agents + package-scoped AGENTS.md | Light personas (developer, triager) with full-stack capability | Plans (gitignored) + specs (persistent) + Linear MCP | Command-triggered; plan→spec→implement→validate loop |
| **LangGraph** | Framework primitives (no agent identity) | N/A (user defines) | Checkpoints (Postgres/SQLite/Memory); BaseStore (key-value + vector) | Graph execution (BSP supersteps) |

### Identity spectrum (expanded)

```
No identity          Role-based              Persona-based           Full identity
   │                    │                        │                       │
  mem0, LangGraph    GSD, gstack,            BMAD (names,          OpenClaw (SOUL.md,
  (service/          Archon, n8n             styles, session       MEMORY.md, Dreaming)
   framework)        (functional             lock)                 Paperclip (SOUL.md,
                      specialists)                                 PARA memory, voice/tone)
```

**Archon's agent design innovation:** Agents defined with structured frontmatter (`name`, `description`, `model`, `tools`, `hooks`) that the harness interprets. The `hooks` field (e.g., `PostToolUse` for validation) adds behavioral enforcement at the agent definition level — governance embedded in agent identity. This is the richest agent metadata schema in the registry.

**n8n's spec-driven identity:** Agents are lightweight, but the spec-driven development skill gives them persistent intent context. `.claude/specs/` files act as living architectural decisions that persist across sessions and agent invocations. The agent's "identity" comes from the spec it's implementing, not from a persona definition.

### Memory architecture comparison (expanded)

| Repo | Persistence | Structure | Consolidation | Scope |
|------|-------------|-----------|---------------|-------|
| GSD | STATE.md (session) | Flat file | None | Per-project |
| Superpowers | None | Context window | None | Per-session |
| BMAD | Config + artifacts | Flat file | Distillator (lossless compression) | Per-project |
| OpenClaw | MEMORY.md + daily notes | Flat files | Dreaming (Light→Deep→REM with scoring) | Per-agent |
| Paperclip | PARA folders + MEMORY.md | Knowledge graph + daily notes + tacit | Weekly synthesis; memory decay rules | Per-agent, company-scoped |
| gstack | Learnings JSONL | Append-only log | `/learn` skill (review, prune, export) | Per-project |
| mem0 | Vector + Graph + SQLite | Triple storage | Automatic fact extraction via LLM | Scoped (user/agent/run) |
| Archon | SQLite/PostgreSQL | Relational tables (sessions, events, messages) | Immutable sessions (linked by parent_session_id) | Per-conversation; cross-workflow via DB |
| n8n | Plans (gitignored) + specs (committed) | Flat files + Linear MCP | None (plans are ephemeral; specs are living docs) | Per-ticket (plans), per-feature (specs) |
| LangGraph | Checkpoints + BaseStore | Typed state (channels) + key-value + vector search | None built-in; user-configurable | Per-execution (checkpoints), cross-thread (store) |

**New memory insight:** LangGraph's checkpoint system is the only one designed for time-travel debugging and replay. Any checkpoint can be loaded to resume execution from that point. Combined with the `interrupt()` primitive, this enables resumable human-in-the-loop workflows — a pattern none of the other repos implement at the infrastructure level.

---

## 6. Special Focus: Brainstorming / Critical Thinking Skills

Nick flagged this comparison across Superpowers, BMAD, and GSD. Extended to all 10 repos.

### Comparison

| Aspect | GSD | Superpowers | BMAD | gstack | Archon | n8n | LangGraph |
|--------|-----|-------------|------|--------|--------|-----|-----------|
| **Name** | Discuss phase | Brainstorming skill | Brainstorming + Advanced Elicitation + Adversarial Review | Office Hours | PRPs (issue plans) + `archon-dev` meta-router | `/n8n:plan` command + spec-driven development | N/A (framework) |
| **Scope** | Per-phase implementation | Per-project design-first gate | Cross-phase creative/analytical tool | Pre-implementation design session | Per-issue implementation planning | Per-ticket planning + per-feature specs | — |
| **Mandatory?** | Optional (recommended) | **HARD-GATE**: every project, no exceptions | User-activated (optional) | User-invoked (optional) | Workflow-dependent | Skill-invoked (optional) | — |
| **Focus** | HOW to implement | WHAT to build | Expansive ideation (100+ ideas) | 6 forcing questions; design thinking | Research → classify → plan → implement | Structured plan with risks + living spec | — |
| **Anti-bias** | Scope containment | "YAGNI ruthlessly"; rationalization prevention | Anti-bias protocol ("shift domain every 10 ideas") | 6 decision principles | Multi-agent parallel review (5+ agents) | Spec as truth anchor against drift | — |

**New patterns from additions:**

- **Archon's PRP pattern**: Issue implementation plans saved to `.claude/PRPs/issues/` — structured research and planning documents per GitHub issue. The `archon-dev` meta-skill routes to the right cookbook based on intent (research, plan, implement, review, debug). This is intent classification as a development workflow.
- **n8n's spec-driven development**: Specs are not one-time planning artifacts — they're living documents that persist and evolve. The bidirectional sync between spec and code creates a continuous alignment loop, not just a pre-implementation gate.

---

## 7. Pattern Clusters

### Shared Patterns (3+ repos)

| Pattern | Repos | Description |
|---------|-------|-------------|
| **SKILL.md as standard skill format** | GSD, Superpowers, BMAD, OpenClaw, Paperclip, gstack, mem0, Archon, n8n (9/10) | Near-universal. YAML frontmatter + markdown body. Only LangGraph (a Python framework) doesn't use it. |
| **Multi-AI-platform support** | Superpowers (5), BMAD (7+), OpenClaw (3), gstack (8), Archon (3), n8n (2+), LangGraph (2) (7/10) | Skills or context designed for portability across Claude Code, Cursor, Copilot, Codex, etc. |
| **AGENTS.md / CLAUDE.md as context entry point** | All 10 (10/10) | Every repo has at least one auto-loaded context file. Universal convention. |
| **Git as shared state** | GSD, Superpowers, BMAD, gstack, Archon (5/10) | Frameworks without a database use git (commits, branches, worktrees) as the coordination substrate. |
| **Artifact-based handoff** | GSD, BMAD, Superpowers, gstack, n8n (5/10) | Agents produce files that downstream agents consume. The file IS the communication channel. |
| **Subagent dispatch for review** | GSD, Superpowers, BMAD, gstack, Archon, n8n (6/10) | Review is the most common use case for multi-agent coordination. Fresh subagents provide independent judgment. |
| **Human gate at critical transitions** | GSD, Superpowers, BMAD, Paperclip, gstack, Archon, n8n (7/10) | Human approval required before consequential actions. Universal in frameworks/platforms. |
| **Kebab-case directory naming** | GSD, Superpowers, BMAD, OpenClaw, Paperclip, gstack, Archon, n8n (8/10) | Near-universal. mem0 (snake_case for Python) and LangGraph (snake_case) diverge for language conventions. |
| **Pre-implementation design phase** | GSD, Superpowers, BMAD, gstack, Archon, n8n (6/10) | Thinking before building is an emerging convention. |
| **Verification as independent pass** | GSD, Superpowers, BMAD, gstack, Archon (5/10) | Verification treated as a distinct phase with fresh context. |
| **Monorepo with package-level context** | Archon (10 packages), n8n (44+ packages), LangGraph (8 libs) (3/10) | Large repos distribute context per package/library. Each with a different strategy (Archon: rules, n8n: chain-loaders, LangGraph: none). |
| **DAG/graph-based workflow execution** | Archon (YAML DAGs), LangGraph (StateGraph/Pregel) (2/10) | Graph-based workflow execution is emerging but not yet widespread. Different implementations: Archon's is YAML-declarative, LangGraph's is programmatic. |
| **Worktree isolation for concurrent work** | GSD, Archon (2/10) | Git worktrees as an isolation mechanism for parallel workflow execution. Archon adds IsolationResolver with 7-step resolution and branded types. |
| **Cross-platform context file mirroring** | Archon (.claude/ + .github/), n8n (CLAUDE.md→AGENTS.md), LangGraph (dual identical files) (3/10) | Maintaining context files that work across multiple AI coding tools. Three different strategies for the same problem. |

### Unique Patterns (1 repo only)

| Pattern | Repo | Description | Innovation potential |
|---------|------|-------------|---------------------|
| **Dreaming memory consolidation** | OpenClaw | Light→Deep→REM phases for promoting short-term to long-term memory | High |
| **Persuasion-engineered constraints** | Superpowers | 7 persuasion principles from Meincke et al. (2025). 33%→72% compliance | High |
| **Budget hard-stop governance** | Paperclip | Auto-pause at 100% budget; critical-only above 80% | High |
| **Atomic checkout exclusion (409)** | Paperclip | Single-assignee task model enforced by HTTP status codes | Medium |
| **Step-file micro-architecture** | BMAD | Complex workflows decompose into numbered step files loaded one at a time | High |
| **Deterministic skill validator** | BMAD | 27 rules (14 deterministic + 13 inference). CI for prompts | High |
| **Shell preamble as boot sequence** | gstack | Identical ~80-line bash block on every skill invocation | Medium |
| **Three-tier eval system with costed tiers** | gstack | Tier 1 (free), Tier 2 ($3.85/run), Tier 3 ($0.15/run). Explicit cost awareness | High |
| **Provider pattern at 78-provider scale** | mem0 | Abstract base + factory across 5 categories | Medium |
| **Triple storage architecture** | mem0 | Vector + graph + SQLite layers with optional graph on top of vector | High |
| **PARA-based file memory with decay** | Paperclip | Knowledge graph + daily notes + tacit with memory decay rules | High |
| **Agent-as-guest metaphor** | OpenClaw | "You have access to someone's life..." Shapes concrete privacy rules | Medium |
| **Meta-skill for skill authorship** | Superpowers | `writing-skills/` teaches agents how to write skills | Medium |
| **Anti-bias protocol for ideation** | BMAD | "Shift creative domain every 10 ideas" to combat LLM semantic clustering | High |
| **Distillator with round-trip validation** | BMAD | Lossless compression verified by spawning a reconstruction subagent | High |
| **DAG workflow engine with mixed node types** | Archon | AI prompts, bash, TypeScript, Python, approval gates as first-class DAG nodes. Variable substitution (`$nodeId.output`) between nodes | High |
| **IsolationResolver 7-step worktree resolution** | Archon | Existing env → no codebase skip → workflow reuse → linked issue → PR branch → limit+cleanup → create new. Branded types. | High |
| **Intent-based meta-routing skill** | Archon | `archon-dev` inspects user keywords and dispatches to 10 cookbooks. Intent classification as markdown routing table | High |
| **Hook-based enforcement for agent outputs** | Archon | `PostToolUse` hook validates label categories after every Bash call. Enforcement-after-execution | Medium |
| **Triple context namespace** | Archon | `.claude/` + `.archon/` + `.github/` — same agent concepts adapted for 3 platforms | Medium |
| **Per-node tool restrictions in YAML** | Archon | `allowed_tools`/`denied_tools` per workflow node; `tools: []` for routing calls | High |
| **CLAUDE.md → AGENTS.md chain-loading** | n8n | Root CLAUDE.md is a single line: `@AGENTS.md`. Solves naming constraint for cross-tool compat | High |
| **Plugin namespacing** | n8n | `.claude/plugins/n8n/` with `n8n:` prefix for all skills/commands/agents | Medium |
| **Spec-driven development as a skill** | n8n | Bidirectional sync between `.claude/specs/` and implementation. Specs as living architectural decisions | High |
| **Security fix hygiene governance** | n8n | Neutral branch names, commit messages, test descriptions to prevent attacker monitoring | Medium |
| **Janitor static analysis with TCR** | n8n | AST-based test architecture enforcement. Test-commit-revert: changes commit only if tests pass | High |
| **PromptBuilder utility with Mermaid** | n8n | Programmatic prompt composition + Mermaid flowcharts for LLM consumption | Medium |
| **Template-shipped context files** | n8n | Community node scaffolding includes CLAUDE.md + AGENTS.md + `.agents/` for downstream developers | Medium |
| **Pregel BSP execution model** | LangGraph | Bulk Synchronous Parallel from distributed computing applied to agent orchestration | High |
| **Typed channels as state primitives** | LangGraph | LastValue, BinaryOperator, EphemeralValue, Topic, NamedBarrier — richer than any other state model | High |
| **Interrupt/Command primitives** | LangGraph | `interrupt()` pauses + checkpoints; `Command` combines state mutation + routing in one atomic op | High |
| **Tool injection via type annotations** | LangGraph | `InjectedState`, `InjectedStore`, `ToolRuntime` — declarative tool permissions | High |
| **Auto-generated threat model** | LangGraph | `.github/THREAT_MODEL.md` with trust boundaries, components, data classification | Medium |
| **Specification-as-tests** | LangGraph | `checkpoint-conformance` test suite — interface defines tests, implementations prove compliance | High |
| **Dual authoring APIs** | LangGraph | Declarative (StateGraph) + functional (@entrypoint/@task), both compile to Pregel | Medium |
| **Send for fan-out patterns** | LangGraph | `Send(node, state)` dispatches multiple node instances with different state in parallel | Medium |

### Contradictory Approaches

| Problem | Approach A | Approach B | Repos |
|---------|-----------|-----------|-------|
| **How to load agent context** | Push: harness pre-assembles everything (GSD chain-loading, gstack preamble, Archon layered) | Pull: agent decides what to load (Superpowers self-activation, Paperclip env-var) | GSD+gstack+Archon vs Superpowers+Paperclip |
| **How to enforce rules** | Structural: tool allowlists, validators, SDK boundaries, CI (GSD, BMAD, OpenClaw, Archon, n8n) | Psychological: persuasion, rationalization prevention (Superpowers) | 5 repos vs Superpowers |
| **Who orchestrates?** | Human picks what happens next (BMAD, gstack, n8n) | System automates the pipeline (GSD, Archon, Paperclip) | BMAD+gstack+n8n vs GSD+Archon+Paperclip |
| **Agent identity** | Ephemeral: fresh context per task (GSD, Superpowers, Archon) | Persistent: SOUL.md, memory, dreaming (OpenClaw, Paperclip) | GSD+Superpowers+Archon vs OpenClaw+Paperclip |
| **Workflow definition** | YAML/declarative (Archon DAGs, LangGraph StateGraph) | Code/imperative (Paperclip heartbeats, GSD CJS workflows) | Archon+LangGraph vs Paperclip+GSD |
| **Monorepo context distribution** | Per-package context files (n8n: 44+ AGENTS.md, Archon: path-scoped rules) | Single global context (LangGraph: one CLAUDE.md for all libs) | n8n+Archon vs LangGraph |
| **Agent persona depth** | Role-based: functional labels (GSD, Archon: "reviewer", "analyst") | Named personalities: communication styles, session lock (BMAD: Mary, Winston) | GSD+Archon vs BMAD |
| **Workflow decomposition** | Large orchestration files (GSD, Superpowers) | Micro-files loaded just-in-time (BMAD step files, Archon cookbooks) | GSD+Superpowers vs BMAD+Archon |
| **Multi-agent review** | Parallel specialist dispatch (gstack: 7, Archon: 5+) | Sequential review stages (Superpowers: spec → quality) | gstack+Archon vs Superpowers |
| **Memory consolidation** | Background autonomous (OpenClaw Dreaming) | User-triggered (gstack `/learn`) | OpenClaw vs gstack |
| **Governance data store** | Flat files in repo (GSD, BMAD, Superpowers, n8n) | Relational database (Paperclip: PostgreSQL, Archon: SQLite/PostgreSQL) | 4 repos vs 2 repos |
| **Cross-platform strategy** | Platform-specific mirrors (Archon: `.claude/` + `.github/`) | Naming indirection (n8n: CLAUDE.md→AGENTS.md, LangGraph: identical files) | Archon vs n8n+LangGraph |

---

## 8. Research Dimension Heat Map

| Dimension | GSD | SP | BMAD | OC | PC | gs | m0 | Ar | n8n | LG | Strongest sources |
|-----------|-----|-----|------|-----|-----|-----|-----|-----|------|-----|-----------------|
| Context Engineering | H | H | H | H | H | H | H | H | H | L | All except LangGraph |
| Model | M | L | L | H | M | M | H | M | L | L | OpenClaw, mem0 |
| Prompt | H | H | H | M | M | H | L | M | H | L | GSD, SP, BMAD, gstack, n8n |
| Tools | M | M | M | H | H | H | H | H | M | H | OpenClaw, Paperclip, gstack, mem0, Archon, LangGraph |
| Intent | H | H | H | M | H | H | L | H | M | H | GSD, SP, BMAD, Paperclip, gstack, Archon, LangGraph |
| Orchestration | H | H | H | H | H | M | L | H | M | H | GSD, BMAD, OpenClaw, Paperclip, Archon, LangGraph |
| Evaluation | H | H | H | M | M | H | M | H | H | M | GSD, SP, BMAD, gstack, Archon, n8n |
| Sandboxing | M | M | L | H | H | M | L | H | H | M | OpenClaw, Paperclip, Archon, n8n |
| Governance | H | H | H | H | H | M | L | M | H | M | GSD, SP, BMAD, OpenClaw, Paperclip, n8n |
| Agent Design | H | H | H | H | H | H | M | H | H | H | All except mem0 |

**H** = High relevance, **M** = Medium, **L** = Low

### Cross-dimension observations (updated)

- **Context Engineering is High for 9/10 repos.** LangGraph is the sole exception — as a framework, it doesn't invest in context engineering for development. The other 9 repos each have a distinct strategy, giving this dimension the most pattern diversity.
- **Agent Design is High for 9/10 repos (all except mem0).** Even the newer additions (Archon with frontmatter-driven agents, n8n with spec-driven identity, LangGraph with dual authoring APIs) contribute novel patterns.
- **Orchestration now has two poles.** The original 7 repos were all ad-hoc orchestration patterns. Archon and LangGraph add production-grade workflow engines (DAG and BSP respectively), raising the bar for what "orchestration" means.
- **Sandboxing strengthens with the new repos.** Archon's IsolationResolver (7-step worktree resolution with branded types) and n8n's task-runner sandboxing add concrete patterns. The dimension is no longer dominated by just OpenClaw and Paperclip.
- **Tools dimension benefits from LangGraph and Archon.** LangGraph's type-annotation-based tool permissions and Archon's per-node tool restrictions add granular patterns that didn't exist in the original comparison.
- **Evaluation gains n8n's janitor + TCR pattern.** The janitor's AST-based architecture enforcement with test-commit-revert is a novel evaluation mechanism distinct from the subagent review patterns seen elsewhere.

---

## 9. Findings Candidates (Cross-Repo)

These findings emerge from comparing repos, not from individual analyses. The first 8 (CR-1 through CR-8) were identified in the original 7-repo comparison. CR-9 through CR-14 are new from incorporating Archon, n8n, and LangGraph.

### CR-1: Context Loading Mechanisms — No Convergence

**Dimension:** Context Engineering
**Pattern:** Ten repos exhibit at least seven distinct context loading strategies. No two repos use the same mechanism. The ecosystem has not converged.
**Status:** → Promoted to [[seven-context-loading-mechanisms-no-convergence]] on 2026-04-08
**Update:** The three new repos add cross-platform mirroring as a cross-cutting concern (3 different strategies) and reinforce the non-convergence finding.

### CR-2: Push vs. Pull Context Loading Tradeoff

**Dimension:** Context Engineering, Agent Design
**Pattern:** Push models guarantee completeness but risk bloat. Pull models scale but risk incompleteness. Progressive disclosure (BMAD) and chain-loading (n8n) attempt middle ground.
**Status:** → Promoted to [[push-vs-pull-context-loading]] on 2026-04-08
**Update:** Archon's 780-line CLAUDE.md is the most aggressive push model. n8n's chain-loading is the most elegant middle ground.

### CR-3: Structural vs. Psychological vs. Economic Governance Enforcement

**Dimension:** Governance
**Pattern:** Three (now four) enforcement philosophies: structural, psychological, economic, specification-based. No repo uses all four.
**Status:** → Promoted to [[structural-vs-psychological-vs-economic-governance]] on 2026-04-08
**Update:** LangGraph and n8n add specification-as-governance (conformance tests, spec-driven development).

### CR-4: Orchestration Correlates with Product Type

**Dimension:** Orchestration
**Pattern:** The coordination mechanism follows from the product architecture: file-based for frameworks, API-based for products, context-window for skill packs, workflow-engine for platforms, programmatic for libraries.
**Status:** → Promoted to [[orchestration-correlates-with-product-type]] on 2026-04-08
**Update:** Archon (DAG platform) and LangGraph (BSP framework) confirm the pattern — platforms use structured workflows, frameworks use programmatic coordination.

### CR-5: Identity Depth Correlates with Deployment Persistence

**Dimension:** Agent Design
**Pattern:** Persistent agents have deep identity. Ephemeral agents have shallow identity. Archon's agents add a new data point: rich metadata (model, tools, hooks) but no personality.
**Status:** → Promoted to [[identity-depth-correlates-with-persistence]] on 2026-04-08

### CR-6: Anti-Bias Protocol for LLM Ideation

**Dimension:** Prompt, Evaluation
**Pattern:** BMAD explicitly mitigates LLM semantic clustering. No other repo addresses this failure mode directly.
**Status:** → Promoted to [[anti-bias-protocol-for-llm-ideation]] on 2026-04-08

### CR-7: Rationalization Prevention as Governance Layer

**Dimension:** Governance, Prompt
**Pattern:** Superpowers includes explicit tables of common LLM rationalizations with rebuttals. Research-backed (Meincke et al. 2025, N=28,000).
**Status:** → Promoted to [[rationalization-prevention-pattern]] on 2026-04-08

### CR-8: Production Memory Architecture Spectrum

**Dimension:** Context Engineering, Agent Design
**Pattern:** Five distinct memory architectures across the original 7 repos. Archon adds relational DB state, n8n adds spec-as-memory, LangGraph adds checkpoint-based time-travel.
**Status:** → Promoted to [[production-memory-architecture-spectrum]] on 2026-04-08
**Update:** LangGraph's checkpoint system enables time-travel debugging and resumable workflows — a fundamentally different use of persistence.

### CR-9: DAG vs. BSP — Two Graph-Based Orchestration Models

**Dimension:** Orchestration
**Pattern:** Two repos introduce graph-based workflow execution, but with fundamentally different models. Archon's YAML DAGs are declarative, multi-node-type (AI + bash + TypeScript + approval gates), and execute via topological layer parallelism. LangGraph's Pregel BSP is programmatic, channel-mediated, and executes via superstep synchronization. Both enable parallelism but Archon targets workflow authoring (non-code users can write YAML) while LangGraph targets developers (Python code defines graphs). Neither of the original 7 repos had a formal graph execution model — they all used ad-hoc orchestration.
**Why notable:** Graph-based orchestration may represent the next maturity level for agentic systems. The split between declarative (YAML) and programmatic (Python) mirrors the broader no-code vs. code-first divide. MetaSystem's GSD uses ad-hoc phase sequencing — if it ever needs more complex orchestration, these two models represent the design space.
→ Promoted to [[dag-vs-bsp-two-graph-based-orchestration-models]] on 2026-04-09

### CR-10: Cross-Platform Context File Strategy

**Dimension:** Context Engineering, Agent Design
**Pattern:** Three repos address the problem of maintaining context files that work across multiple AI coding tools, with three different strategies: (1) Archon mirrors agent definitions across `.claude/agents/` and `.github/agents/` — platform-specific copies. (2) n8n uses `CLAUDE.md` → `@AGENTS.md` indirection — CLAUDE.md (auto-loaded by Claude Code) is a pointer to AGENTS.md (readable by any tool). (3) LangGraph duplicates content into both CLAUDE.md and AGENTS.md — simplest approach, but content can drift. This problem didn't appear in the original 7-repo comparison because those repos targeted a single platform.
**Why notable:** As the ecosystem matures and projects support multiple AI tools (Claude Code, Cursor, Codex, Copilot), cross-platform context becomes a real concern. n8n's chain-loading indirection is the most elegant solution — minimal duplication, works across tools, and the naming constraint is solved at the pointer level.
→ Promoted to [[cross-platform-context-file-strategy]] on 2026-04-09

### CR-11: Specification-as-Governance (Conformance Tests + Spec-Driven Development)

**Dimension:** Governance, Evaluation
**Pattern:** Two repos encode governance as specifications rather than instructions or structural constraints. LangGraph's `checkpoint-conformance` test suite defines what implementations must do — the interface owns the tests, not the implementation. n8n's spec-driven development skill enforces bidirectional sync between `.claude/specs/` and code — specs are living governance artifacts, not one-time documents. Both invert the typical relationship: instead of code being validated against external rules, the spec/test IS the governance mechanism.
**Why notable:** This is a fourth governance enforcement philosophy not present in the original comparison (structural, psychological, economic, specification-based). Particularly relevant for MetaSystem where Design Decisions and Build Specs already serve a similar purpose — but without automated bidirectional enforcement.
→ Promoted to [[specification-as-governance-fourth-enforcement-philosophy]] on 2026-04-09

### CR-12: Per-Node Tool Restrictions as Workflow-Level Governance

**Dimension:** Tools, Governance
**Pattern:** Archon's workflow YAML nodes can specify `allowed_tools` or `denied_tools` arrays, giving fine-grained tool access control per workflow step. The orchestrator's routing calls use `tools: []` to prevent any tool use during classification. GSD has per-agent tool allowlists but not per-step within a workflow. Superpowers has skill-level tool guidance but not enforceable restrictions. Archon's per-node granularity is the finest in the registry.
**Why notable:** As workflow complexity grows, per-step tool restrictions become important. A research step shouldn't be able to write files. A classification step shouldn't be able to execute code. Archon demonstrates this at the YAML configuration level, making it accessible to non-code workflow authors.
→ Promoted to [[per-node-tool-restrictions-workflow-governance]] on 2026-04-09

### CR-13: Immutable Sessions as Audit Architecture

**Dimension:** Governance, Agent Design
**Pattern:** Archon's sessions are never mutated — only deactivated and replaced, linked by `parent_session_id`. Combined with the `workflow_events` table and `immutable session` transitions, this creates a complete audit trail of every state change. Paperclip's `X-Paperclip-Run-Id` header on every mutation is similar in spirit but less comprehensive. The other repos rely on git history (GSD, Superpowers, n8n) or in-memory state (Superpowers, gstack).
**Why notable:** For compliance-sensitive environments or debugging complex multi-step failures, immutable session audit trails are valuable. This pattern is relevant as MetaSystem considers more automated workflows.
→ Promoted to [[immutable-sessions-as-audit-architecture]] on 2026-04-09

### CR-14: Monorepo Context Distribution — Three Strategies

**Dimension:** Context Engineering
**Pattern:** Three repos with monorepo architectures each solve package-level context differently: (1) **n8n** distributes CLAUDE.md→AGENTS.md chain-loaders per package (44+ packages). Each package gets domain-specific conventions. (2) **Archon** uses path-scoped `.claude/rules/*.md` files that auto-load based on which package you're editing (11 domain rules). No per-package CLAUDE.md needed. (3) **LangGraph** uses a single global CLAUDE.md for all 8 libraries — no distribution at all. These represent a tradeoff between context precision (n8n), authoring effort (Archon as middle ground), and simplicity (LangGraph).
**Why notable:** As projects grow into monorepos, context distribution becomes a real architectural decision. n8n's approach is the most thorough but requires maintaining CLAUDE.md+AGENTS.md pairs per package. Archon's path-scoped rules are more maintainable. LangGraph's minimalism works for a framework but wouldn't scale for a platform like n8n.
→ Promoted to [[monorepo-context-distribution-three-strategies]] on 2026-04-09

---

## Version Log

| Date | Repos | Notes |
|------|-------|-------|
| 2026-04-08 | GSD v1.33.0, Superpowers v5.0.7, BMAD v6.2.2, OpenClaw v2026.4.5, Paperclip v2026.403.0, gstack v0.15.16.0, mem0 v1.0.11 | Initial cross-repo comparison. 8 cross-repo findings candidates. |
| 2026-04-09 | + Archon v0.3.2, n8n v2.16.0, LangGraph v1.1.6 | Full regeneration with 10 repos. 6 new cross-repo findings candidates (CR-9 through CR-14). Added markdown-parity class, DAG/BSP orchestration, cross-platform context, spec-as-governance. |
