---
title: "Pydantic AI -- Structural Analysis"
id: "pydantic-ai-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-07-13"
updated: "2026-07-13"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "pydantic-ai"
analyzed_version: "v2.9.0"
analyzed_date: "2026-07-13"
repo_url: "https://github.com/pydantic/pydantic-ai"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# Pydantic AI -- Structural Analysis

## Metadata
- **Repo:** https://github.com/pydantic/pydantic-ai
- **Version analyzed:** v2.9.0 (released 2026-07-10; 1.107.x maintained in parallel)
- **Date:** 2026-07-13
- **Spectrum position:** study

Special attention in this pass (per watch rationale): the **capability primitive's
implementation** (composition mechanics, progressive disclosure, lifecycle hooks,
guardrails) and the **core-vs-harness package split**.

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total files | 2,079 |
| Total directories | 164 |
| Markdown files | 251 |
| Code files (by language) | Python 566; TS 1; JS 1; shell 6 |
| Config/YAML/JSON files | 1,204 yaml/yml (972 in `tests/models`, 187 in `tests/cassettes` — VCR recordings), 7 toml, 5 json |
| MD-to-code ratio | ~0.44 md per code file (251:574) |
| Max directory depth | 6 below repo root |

The yaml mass is almost entirely recorded model-API traffic (`pytest-recording`/`vcrpy`
cassettes) backing the "integration tests over mocks" testing policy — an artifact of
governance, not configuration.

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Agent definitions | 0 | — (no persona files; the "agent" is a code object) |
| Commands/skills | 5 SKILL.md + 11 skill reference docs | `.claude/skills/` (3), `.agents/skills/` (1), `pydantic_ai_slim/pydantic_ai/.agents/skills/building-pydantic-ai-agents/` (1 + 11 references) |
| Workflows/orchestration | ~33 | `.github/workflows/` — 10 agentic (gh-aw) workflow definitions + 10 prompt files + 11 shared fragments + AGENTS.md/CLAUDE.md |
| Reference docs (LLM-directed) | 18 | 13 `AGENTS.md` (root + 12 directory-scoped) + 5 `agent_docs/*.md` |
| Templates (artifact schemas) | 1 | `.github/pull_request_template.md` |
| Human documentation | 171 | `docs/` (mkdocs site; also chain-loaded by agents via CLAUDE.md) |
| Other | ~23 | README/CONTRIBUTING/issue templates/package READMEs |

Markdown here is not "the codebase" (contrast GSD/BMAD) — the product is Python — but
the LLM-directed markdown layer is unusually deep for a code-product repo: three distinct
audiences (contributing agents via AGENTS.md/agent_docs, consuming coding agents via the
packaged skill, CI maintenance agents via gh-aw workflow prompts).

### Directory Naming Conventions
snake_case throughout (Python convention), including package dirs (`pydantic_ai_slim`).
Private modules prefixed `_` (`_agent_graph.py`, `_tool_search.py`, `_spec.py`).
Dotted convention dirs for agent tooling: `.agents/`, `.claude/`, `.gemini/`, `.github/`.

### Top-Level Structure
```
pydantic-ai/
├── pydantic_ai_slim/pydantic_ai/   # core framework package (240 py) — agent/, capabilities/,
│                                   #   models/, providers/, profiles/, toolsets/, native_tools/,
│                                   #   durable_exec/, embeddings/, ui/, _cli/, .agents/skills/
├── pydantic_graph/                 # graph library powering the agent loop (14 py)
├── pydantic_evals/                 # evaluation framework (29 py)
├── clai/                           # CLI + web UI chat client (3 py)
├── examples/                       # runnable examples package (41 py)
├── docs/                           # mkdocs site (171 md) incl. docs/harness/
├── tests/                          # 207 py + 1,159 yaml cassettes
├── agent_docs/                     # coding guidelines for contributing agents (5 md)
├── .github/workflows/              # CI + 10 gh-aw agentic maintenance workflows
├── .claude/skills/ + .agents/skills/  # repo-workflow skills
└── AGENTS.md, CLAUDE.md -> AGENTS.md, pyproject.toml (uv workspace + pydantic-ai metapackage)
```

The repo is a `uv` workspace of 5 member packages; the root `pydantic-ai` metapackage
re-exports `pydantic-ai-slim` plus all provider extras. **The harness lane is not in this
repo at all** — `pydantic-ai-harness` is a separate repository/package (see Dimension 4).

### Code Surface Outline (optional — ast-grep)
Skipped — ast-grep unavailable (`command -v ast-grep` failed). Find-based inventory used
as baseline; targeted reads verified the capability subsystem.

### Notable Structural Patterns

- **The capability subsystem is a directory, not a class.**
  `pydantic_ai_slim/pydantic_ai/capabilities/` (31 files) holds the abstraction
  (`abstract.py`, 38k), the convenience class (`capability.py`), composition
  (`combined.py`, 31k), the hook engine (`hooks.py`, 57k), progressive disclosure
  (`_deferred_capability_loader.py`), and ~20 first-party capability implementations
  (Thinking, WebSearch, WebFetch, XSearch, ImageGeneration, MCP, ToolSearch,
  Instrumentation, ProcessHistory, ReinjectSystemPrompt, PrefixTools, ThreadExecutor...).
  Everything cross-cutting is a capability; the directory's own AGENTS.md instructs
  "prefer a capability over a new `Agent` constructor kwarg."
- **Composition mechanics (capability primitive).** `AbstractCapability` exposes seven
  getter seams — `get_instructions()`, `get_description()`, `get_model_settings()`,
  `get_toolset()`, `get_native_tools()`, `get_wrapper_toolset()`, `get_ordering()` —
  plus the hook methods. An agent is `Agent(model, capabilities=[...])`; each capability
  contributes prompt fragments, tools, settings, and interceptors through those seams.
  `Capability` (the convenience class) covers instructions+tools+toolsets without
  subclassing and mirrors the `Agent.tool`/`tool_plain`/`instructions` decorators at
  capability scope. `CombinedCapability` merges a list with **middleware semantics**:
  first-listed is outermost; `CapabilityOrdering(position, wraps, wrapped_by, requires)`
  lets a capability declare ordering constraints that are **topologically sorted**, with
  user order as tiebreaker (e.g. `DeferredCapabilityLoader` pins itself
  `position='outermost', wrapped_by=[Instrumentation]`).
- **Progressive disclosure is cache-aware by design.** `defer_loading=True` (+ required
  stable `id`) hides a capability's instructions/tools/settings behind a framework-owned
  `load_capability` tool. The catalog of deferred capabilities renders as a dynamic
  instruction — and deliberately lists **every** deferred capability every turn,
  including already-loaded ones, so the rendered prefix stays byte-identical and the
  provider's prompt cache stays warm; redundant loads are bounced with a cheap
  `ModelRetry` ("one occasional wasted retry is far cheaper than busting the prefix
  cache on every load" — in-code comment). Loaded state is resumable across runs via
  message history.
- **Declarative agent specs.** `_spec.py` + `agent/spec.py` let agents be constructed
  from YAML/JSON (`AgentSpec`), with a `CAPABILITY_TYPES` registry keyed by
  `get_serialization_name()`; capabilities holding functions/callables return `None` and
  explicitly opt out of spec-constructibility.
- **A skill ships inside the pip package.**
  `pydantic_ai_slim/pydantic_ai/.agents/skills/building-pydantic-ai-agents/` (SKILL.md +
  11 reference docs) is included in the wheel and installable into consumers' coding
  agents via library-skills.io, the Claude plugin marketplace, or agentskills.io
  (`docs/coding-agent-skills.md`). CLAUDE.md requires feature PRs to update this skill —
  the skill is release-gated documentation, versioned with the code.

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `AGENTS.md` (root; `CLAUDE.md` symlinks to it) | LLM | Global | Chain-loader | Identity/Persona + Constraints/Rules | "Channel your inner Samuel Colvin" — contributor-agent constitution; chain-loads agent_docs + 11 directory AGENTS.md |
| `agent_docs/index.md` | LLM | Global | Referenced | Constraints/Rules | Coding guidelines "extracted from PR review patterns", each rule tagged `<!-- rule:NNN -->`; links 4 topic guides |
| `agent_docs/{api-design,code-simplification,documentation,pydantic-ai-slim}.md` | LLM | Global | Referenced | Constraints/Rules | Topic guides loaded on demand from index |
| `pydantic_ai_slim/pydantic_ai/AGENTS.md` (+ `CLAUDE.md` symlink) | LLM | Project | Referenced | Constraints/Rules | Package-level API-design/type/style rules |
| `pydantic_ai_slim/pydantic_ai/{capabilities,models,providers,profiles,toolsets,native_tools,durable_exec,ui}/AGENTS.md` | LLM | Project | Referenced | Constraints/Rules | Directory-scoped rules (8 files; e.g. capabilities/: "prefer a capability over an Agent kwarg", preserve composition order) |
| `docs/AGENTS.md`, `tests/AGENTS.md`, `.github/workflows/AGENTS.md` | LLM | Project | Referenced | Constraints/Rules | Docs-voice rules, testing rules, workflow-editing rules |
| `.claude/skills/{address-feedback,pre-push-review,testing-skill}/SKILL.md` | LLM | Task | Injected | Workflow/Process | Repo-workflow skills for contributing agents (testing-skill bundles `parse_cassette.py`) |
| `.agents/skills/complete-partial-pr/SKILL.md` | LLM | Task | Injected | Workflow/Process | Cross-harness repo skill under the vendor-neutral `.agents/` convention |
| `pydantic_ai_slim/pydantic_ai/.agents/skills/building-pydantic-ai-agents/SKILL.md` + 11 `references/*.md` | LLM | Global (consumer-side) | Injected | Workflow/Process + Tool Usage | THE packaged consumer skill: quick-start patterns + progressive-disclosure references (ARCHITECTURE, CAPABILITIES-AND-HOOKS, ON-DEMAND-CAPABILITIES, TOOLS-CORE/ADVANCED, AGENTS-CORE, ORCHESTRATION-AND-INTEGRATIONS, TESTING-AND-DEBUGGING...) |
| `.github/workflows/*.md` (10 gh-aw definitions) | LLM | Task | Injected | Workflow/Process | Agentic maintenance workflows (frontmatter: schedule, tools, safe-outputs) compiled to `.lock.yml` |
| `.github/workflows/shared/*.md` + `shared/prompts/*.md` | LLM | Task | Referenced | Constraints/Rules + Workflow/Process | Shared fragments imported by workflows (adversarial-review, rigor, network-vendor-domains, otel-logfire) |
| `.claude/settings.json`, `.gemini/config.yaml` | LLM (harness) | Global | Auto-loaded | Tool Usage | Harness configs (Claude Code, Gemini CLI) |
| `docs/**/*.md` (171) | Both | Global | Referenced | Workflow/Process | mkdocs user docs; root AGENTS.md points agents at agent.md/tools.md/output.md etc. as task context |
| `README.md`, `CONTRIBUTING.md` | Human | Global | — | Workflow/Process | Standard OSS docs |

### Sampling Notes
Read in full: root AGENTS.md (auto-surfaced), `pydantic_ai_slim/pydantic_ai/AGENTS.md`,
`docs/AGENTS.md`, `capabilities/AGENTS.md`, `agent_docs/index.md` (first ~50 lines),
packaged SKILL.md (first 40 lines), ON-DEMAND-CAPABILITIES.md (first 30 lines),
bug-hunter workflow frontmatter. Classified by pattern: remaining 9 directory AGENTS.md,
remaining 10 skill references, remaining 9 gh-aw workflows + 20 shared/prompt fragments.

### Context Loading Strategy
Three-audience, layered:

1. **Contributor agents**: `CLAUDE.md -> AGENTS.md` symlink at root (AGENTS.md is
   canonical — 13 AGENTS.md files, 8 with CLAUDE.md symlinks) chain-loads
   `agent_docs/index.md` (always) → topic guides (on demand) → directory AGENTS.md
   (when working in that directory). The rules corpus is explicitly mined from PR review
   history (`<!-- braindump: rules extracted from PR review patterns -->`, per-rule
   `rule:NNN` IDs) — a machine-maintained, provenance-tagged guideline set.
2. **Consumer coding agents**: the packaged skill inside the wheel, itself structured
   for progressive disclosure (lean SKILL.md + 11 on-demand reference files), preaching
   what it practices ("treat `defer_loading=True` as a design question for every
   capability... keep the base agent prompt small: identity, task boundaries, global
   safety, routing").
3. **CI maintenance agents**: gh-aw workflow markdown with YAML frontmatter, importing
   shared fragments — prompt assembly via `imports:` lists.

---

## 3. Workflow Topology

Pydantic AI is a library, not a phased workflow system — no discernible
development-process workflow for users. Two real topologies exist:

### 3a. The agent run loop (code-level, `_agent_graph.py` on `pydantic_graph`)

| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| `UserPromptNode` | `agent.run()` | prompt + instructions assembled | No |
| `ModelRequestNode` | prompt ready / tool results appended | model response received | No |
| `CallToolsNode` | response has tool calls | tools executed or deferred | Optional — `requires_approval=True` tools and deferred-tool flow pause the run for external approval |
| `SetFinalResult` → End | output validated | final result | No |

```
run() --> UserPromptNode --> ModelRequestNode --> CallToolsNode --+--> SetFinalResult --> End
                                   ^                              |
                                   +--- tool results / retries ---+
                                   (deferred tools => run pauses; resumes
                                    later with approval results in history)
```

Every edge is hookable: capability lifecycle methods interleave as
before/after/wrap/on_error around run, node, model-request, tool-validate,
tool-execute, output-validate, and output-process (7 hook families × 4 phases —
see Dimension 4).

### 3b. Repo maintenance topology (gh-aw agentic workflows)
Scheduled, independent, parallel-by-isolation: bug-hunter (weekly), docs-drift,
regression-detector, provider-mapping/roundtrip/streaming-resilience sweeps,
ui-security-review, stale-issues-finder, pr-review — each an isolated agent run whose
only write path is typed `safe-outputs` (e.g. `create-issue: max 1, expires 7d`).
Human gate: everything lands as an issue/comment/PR for maintainer review; agents
never push directly.

### Transition Mechanisms
Agent loop: typed graph-node returns (pydantic_graph `BaseNode`), not file markers.
Deferred tools: run suspension + message-history resumption (approval results replayed).
Maintenance workflows: cron triggers + GitHub events.

### Parallelism
Tool calls execute concurrently by default (`sequential=False` per tool);
`ThreadExecutor` capability offloads sync work. Multi-agent parallelism is
user-composed (asyncio), not framework-orchestrated.

---

## 4. Governance Model

### Constraint Expression
| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| Constitution file | `AGENTS.md` (root) | Soft (agent-read) | "Your primary responsibility is to the project and its users"; agent as "first line of defense against low-quality contributions"; scope discipline ("a hunch is unacceptable") |
| Rules files | `agent_docs/*.md`, 12 scoped `AGENTS.md` | Soft | PR-review-mined rules with `rule:NNN` provenance IDs |
| Version policy | `docs/version-policy.md` | Hard (process) | No breaking changes in minors; deprecations removed only at next major, ≥3 months after 2.0; V1 security fixes ≥6 months; `beta` modules exempt |
| Inline constraints | code comments/docstrings | Soft→Hard | e.g. cache-preservation invariant documented at the deferred-catalog render site |
| CI gates | `.pre-commit-config.yaml`, `ci.yml`, `pr-guard.yml` | Hard | lint/format/typecheck on commit; full test suite + 100%-coverage policy in CI |
| Agentic guard | `pr-guard.yml`, `bots.yml`, gh-aw `safe-outputs` | Hard (structural) | Maintenance agents' writes capped by typed output contracts (max counts, title prefixes, expiry) |
| Runtime governance (user-facing) | capability/hook/guardrail APIs | Hard (code) | `requires_approval` tools, `UsageLimits`, hook `timeout` + `HookTimeoutError`, args validators |

### Guardrail Patterns
**Guardrails are not a separate primitive — they are capabilities implemented through
the hook lattice.** `AbstractCapability` exposes 7 hook families (run, node,
model-request, tool-validate, tool-execute, output-validate, output-process), each with
before/after/wrap/on-error variants (~28 interception points), typed per-hook `Protocol`
signatures in `hooks.py`, and a `Hooks` capability for function-based registration.
The documented guardrail exemplar (`PIIRedactionGuardrail`) wraps `after_model_request`;
approval workflows wrap `before_tool_execute`; the third-party ecosystem
(`pydantic-ai-shields`) ships CostTracking/ToolGuard/InputGuard/OutputGuard/
PromptInjection as capability packages. Determinism knobs: hook timeouts, tool
`requires_approval`, `args_validator`, `UsageLimits`, SSRF protection (`_ssrf.py`).

### Permission Model
No role system in-repo. Boundaries are structural:
- **Core vs harness (the package split).** In-repo core = agent loop + providers +
  capabilities/hooks abstraction + only two classes of first-party capability:
  (a) provider-native/model-coupled ones that must ship with model code, and
  (b) "fundamental to the agent experience" ones (thinking, web search, tool search).
  Everything else — memory, guardrails, context management, code execution
  (**code mode, executing in Monty, Pydantic's Rust-based sandboxed Python
  interpreter**), multi-agent orchestration — lives in the **separate**
  `pydantic-ai-harness` repo/package. The harness is explicitly the *incubation lane*:
  looser backward-compatibility requirements, faster iteration, and a graduation path
  into core once a capability "proves itself broadly essential" (code mode named as
  first candidate). A `harness-compat.yml` CI job enforces the cross-repo contract.
  The "fall up" pattern governs maturation: local model-agnostic implementation first,
  provider-native auto-switch later (already live for WebSearch/WebFetch/ImageGeneration
  via `NativeOrLocalTool`).
- **Contribution routing:** capability contributions are redirected to the harness repo
  ("the capabilities abstraction gives contributions clear boundaries").
- **Maintenance agents:** read-only GitHub permissions + typed safe-outputs (above).

---

## 5. Cross-Agent Protocol

### Agent Roster
No fixed roster — agents are user-defined code objects. Framework-relevant "agents":

| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|
| User agents (`Agent[Deps, Output]`) | user code / YAML `AgentSpec` | mounted capability list | models, tools, other agents |
| Delegate agents | user code | own capability sets | parent agent (agent-as-tool) |
| gh-aw maintenance agents (10) | `.github/workflows/*.md` | GitHub read + safe-outputs | maintainers (via issues/PRs) |
| Contributor coding agents | AGENTS.md ecosystem | repo skills | humans (PRs) |

### Handoff Mechanisms
Documented multi-agent patterns (`docs/multi-agent-applications.md`), cheapest-first:
1. **Agent delegation** — parent agent calls a delegate agent inside a tool
   (`await delegate.run(...)` in a tool function); usage rolls up via shared `RunUsage`;
   deps flow by passing `ctx.deps`.
2. **Programmatic hand-off** — sequential agent runs where application code (or a
   human-in-the-loop) picks the next agent; state via message history.
3. **Graph-based control flow** — `pydantic_graph` state machines for complex routing.
4. **Deep Agents** — documented pattern for planning/spawning subagent hierarchies.
Capability-level sharing is the quieter cross-agent story: the same capability instance
mounts on multiple agents, so improving one shared unit upgrades every agent using it.

### Shared State
`RunContext` (deps, usage, message history) within a run; message history objects
across runs/hand-offs (serialization via `ModelMessagesTypeAdapter`); no framework-level
shared store (memory is a harness capability). Durable execution adapters
(`durable_exec/`: Temporal, DBOS, Prefect, Restate) externalize run state for
crash-resumable agents.

### Coordination Patterns
`Hub-and-Spoke` (delegation) and `Sequential Pipeline` (hand-off) as first-class docs
patterns; `Peer-to-Peer`/`Event-Driven` absent from core (left to graphs/user code).
Maintenance fleet: independent scheduled singletons, no inter-agent communication.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | High | Cache-stable deferred-capability catalog (byte-identical prefix preservation); capability-level progressive disclosure (`defer_loading` + `load_capability`); packaged skill with lean-SKILL.md + on-demand references; opinionated eager-prompt minimalism ("identity, task boundaries, global safety, routing") |
| Model | Medium | Provider-agnostic model classes + profiles with capability flags; `NativeOrLocalTool` "fall up" (native-preferred, local fallback); provider-adaptive tools |
| Prompt | Medium | Instructions as first-class capability contribution (static + dynamic functions); `ReinjectSystemPrompt`; catalog-as-dynamic-instruction |
| Tools | High | Toolsets + `WrapperToolset` composition; tool search vs capability-on-demand as two disclosure granularities; `requires_approval`; deferred tools with run suspension/resumption; per-tool timeout/retries/validators |
| Intent | Medium | Declarative `AgentSpec` (YAML/JSON agents, serialization-name registry); typed output modes |
| Orchestration | High | Capability composition with middleware semantics + topologically-sorted `CapabilityOrdering`; agent delegation/hand-off/graph triad; durable execution adapters |
| Evaluation | Medium | `pydantic_evals` package (evaluators incl. span-based); cassette-based integration testing at scale (1,100+ recordings); `harness-compat` cross-repo CI |
| Sandboxing | Medium | Code mode executes in **Monty** (Pydantic's minimal Rust-based Python interpreter, ~7.9k stars) — in the harness repo, not here; SSRF protection in core |
| Governance | High | Core-vs-harness split as inter-repo graduation pipeline; version policy with beta-module escape hatch; agentic maintenance fleet with typed safe-outputs; PR-review-mined rules corpus; constitution-grade AGENTS.md |
| Agent Design | High | Capability as the single composition primitive (7 getter seams + 28 hook points); guardrails-as-hook-capabilities; agents as `model + [capabilities]`; skill-in-the-package distribution |

### Findings Candidates

Suggestions only — promotion requires a separate `/promote-findings` invocation.

1. **Cache-stable progressive-disclosure catalog** (Context Engineering) — the deferred
   catalog deliberately re-lists every deferred capability every turn so the rendered
   instruction prefix stays byte-identical and the provider prompt cache stays warm;
   redundant loads bounce via `ModelRetry`. A disclosure mechanism designed *around*
   cache economics — directly relevant to any engine skill-catalog design.
   (`capabilities/_deferred_capability_loader.py`)
2. **Middleware-semantics capability composition with declared ordering constraints**
   (Orchestration / Agent Design) — `CapabilityOrdering(position, wraps, wrapped_by,
   requires)` topologically sorted by `CombinedCapability`, user order as tiebreaker;
   composition order as a first-class, declarable property rather than list-position
   convention. (`capabilities/abstract.py`, `combined.py`)
3. **Guardrails as hook-lattice capabilities, not a separate primitive** (Agent Design /
   Tools) — 7 hook families × before/after/wrap/on-error with typed per-hook Protocols;
   PII redaction, approval, cost budgets all land as capabilities. Positive-space
   evidence that one interception lattice can carry the whole guardrail taxonomy.
   (`capabilities/hooks.py`, `docs/capabilities.md` §Guardrail)
4. **Core-vs-harness as an inter-repo graduation pipeline** (Governance) — extends
   existing finding `lean-core-vs-harness-two-lane-framework-layering` with the
   implementation detail the video didn't show: the harness is a *separate repo* with
   looser compat requirements, an explicit incubation→graduation path (code mode named),
   a membership test ("provider-coupled or fundamental" for core), contribution routing,
   and a `harness-compat` CI contract. (`docs/harness/overview.md`)
5. **Skill-in-the-package distribution** (Context Engineering / Tools) — the framework
   ships its consumer-facing coding-agent skill *inside the wheel*
   (`pydantic_ai_slim/pydantic_ai/.agents/skills/`), release-gated by CLAUDE.md ("update
   the relevant agent skills when introducing a new feature"), installable via
   library-skills.io / Claude plugin marketplace / agentskills.io. Docs-as-dependency:
   the skill version always matches the installed library version.
   (`docs/coding-agent-skills.md`)
6. **PR-review-mined rules corpus with per-rule provenance** (Context Engineering /
   Governance) — `agent_docs/` guidelines are "extracted from PR review patterns," each
   tagged `<!-- rule:NNN -->`; review history compiled into agent-loadable rules rather
   than hand-curated style docs. (`agent_docs/index.md`)
7. **Agentic repo-maintenance fleet with typed safe-outputs** (Governance /
   Orchestration) — 10 scheduled gh-aw agents (bug-hunter, docs-drift,
   regression-detector, 3 provider sweeps, ui-security-review, stale-issues-finder,
   pr-review) with read-only permissions and structurally-capped write paths
   (`create-issue: max 1, expires 7d`), sharing prompt fragments (adversarial-review,
   rigor) via `imports:`. (`.github/workflows/`)
8. **AGENTS.md-canonical with CLAUDE.md symlinks + directory-scoped rules** (Context
   Engineering) — 13 AGENTS.md, 8 CLAUDE.md symlinks, root chain-loader; corroborates
   the MemPalace `AGENTS.md↔CLAUDE.md` symlink observation at larger scale and adds
   the scoped-per-directory layer. (root + package AGENTS.md files)
9. **Declarative AgentSpec with serialization-name registry** (Intent / Agent Design) —
   agents constructible from YAML/JSON; capability types opt in via
   `get_serialization_name()`, and non-round-trippable capabilities explicitly return
   `None`. Agent-as-configuration with a typed escape hatch. (`_spec.py`,
   `agent/spec.py`, `docs/agent-spec.md`)
10. **Opinionated disclosure design rules** (Context Engineering) — the packaged skill
    instructs consumer agents to treat `defer_loading=True` as a design question for
    *every* capability, keep the eager prompt to identity/boundaries/safety/routing, and
    choose capability-on-demand (bundles with shared instructions) vs tool search (flat
    catalogs) by shape. A shipped decision rubric for the disclosure-granularity
    question. (`.agents/skills/building-pydantic-ai-agents/references/ON-DEMAND-CAPABILITIES.md`)

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-07-13 | v2.9.0 | all | Initial analysis at registry creation. Focus: capability primitive implementation + core-vs-harness split. Note: harness lane (`pydantic-ai-harness`) and Monty sandbox are separate repos — analyzed here only via in-repo docs/contracts. |
