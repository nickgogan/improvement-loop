---
title: "C — Harness-Landscape Survey: Synthesis + Harness×Memory Harmonization"
author: Synthesizer (E1 memory-spec + E4 harness epic, Track C judgment layer)
date: 2026-07-18
consumes: >
  C-harness-survey/ (5 dossiers: H1-terminology-taxonomy, H2-llm-first-harnesses,
  H3-code-first-frameworks, H4-workflow-orchestrators, H5-meta-harness-agent-os);
  B-synthesis-memory-survey.md (memory matrix, 7 consensus items, failure catalog,
  D1–D10, coding/personal/dual-use class axis); governance/prd.md §Epics (E1, E4, E7);
  governance/actors.md §Orchestration
status: design-input (taxonomy ruling + comparison + judgment; recommendations, not rulings — Nick rules)
recency_rule: 2026/late-2025 weighted over older; when dossiers disagree, name the better-evidenced side — do not average
engine_profile: markdown+git kernel · single-operator (Nick) · human-gated · four actors · runs INSIDE Claude Code (LLM-first) · north star "agentic OS — portable kernel, materializations compiled per target"
---

# C — Harness-Landscape Survey: Synthesis + Harness×Memory Harmonization

The judgment layer over five harness dossiers, joined to the completed memory survey so
both taxonomies meet in one place. Section 3 (harness × memory harmonization) is the core
deliverable. Every collector fell back off Perplexity (down/flaky for all five) onto
first-party docs / WebSearch / `gh` — evidence quality is calibrated per-dossier in §6.
Recency rule applied throughout; where dossiers disagree the better-evidenced side is named,
not averaged. Claims are flagged **[strong]** (converged across multiple dossiers or dated
first-party) vs **[inferred]** (cross-dossier or architectural inference).

---

## 1. Ruled taxonomy & glossary

### 1.1 Adjudicating H1's six dimensions against H2–H5

H1 proposed six axes to cut real systems better than the marketing labels do. Tested against
the mechanics in H2–H5, all six survive, with three amendments. The amendments are the
load-bearing part — they are where the harness evidence actually reshapes H1's proposal.

| H1 dimension | Verdict | What H2–H5 did to it |
|---|---|---|
| **D1 — control-loop ownership** (code-driven ↔ model-driven) | **SPLIT into D1-shape + D1-steering** | H3's headline refinement: the hypothesis "holds at the *shape* level, bends at the *steering* level, uniformly across all five." Amendment below. |
| **D2 — persistence** (ephemeral ↔ durable external) | **CONFIRMED — promoted to the spine of §3** | Every class persists somewhere specific (files / checkpoint-store / workflow-state / managed-DB / daemon-file). This axis *is* the "where memory lives" question. |
| **D3 — enforcement locus** (advisory ↔ structural) | **CONFIRMED — elevated to most load-bearing for the engine** | H1 called it "the axis the field names least." H2's class-level finding makes it the survey's single strongest cross-vendor consensus (§4b). |
| **D4 — coordination topology** (single ↔ fixed-graph ↔ dynamic) | **CONFIRMED — settled for the engine** | H3 §6.2: "configurable autonomy is table stakes" — every framework offers both code- and model-owned routing. Places the engine trivially at *fixed multi-agent, file-mediated* (actors.md). |
| **D5 — lifecycle layer** (dev ↔ run ↔ ops) | **CONFIRMED** | H5 is organized around it: ADE = dev-time, Agent Bricks/AWS Evaluations = ops-time, harness = run-time. Resolves the ADE/harness/meta-harness apparent overlap exactly as H1 predicted. |
| **D6 — packaging** (library ↔ product ↔ substrate ↔ managed service) | **CONFIRMED — substrate/service end refined by H5's three postures** | H3 §6.1 nails the library↔product split ("embed a library" vs "enter an environment"). H5 shows the substrate/service cell is not one thing — amendment below. |

**Amendment 1 — D1 splits into shape-ownership and steering-ownership (H3's refinement).**
H3 proves, across all five code-first frameworks *and* (via H2) all three LLM-first
harnesses, that turn-by-turn **steering** — which tool to call, whether to stop — is the
model's decision, every time, in every system surveyed. Steering-ownership is therefore a
near-constant, not a discriminating axis. What varies is **shape-ownership** — who owns the
bounded loop structure and its hard ceiling:
- **Code-compiled shape:** the shape is a graph/state-machine your program compiles ahead of
  time (LangGraph `create_react_agent`, Pydantic AI's node graph, ADK `BaseLlmFlow`, a
  workflow DAG). [strong — H3 §6.2, four syntaxes of one pattern]
- **Model-reached-through-tools shape:** even the harness's own meta-controls are things the
  model requests *through* ordinary tool-calling, not a script outside its reach — Claude
  Code's Plan Mode is a permission gate its tool calls trip against; opencode's
  `plan_enter`/`plan_exit` are literally callable tools. [strong — H2 class-level]

A third sub-axis, **multi-agent routing**, is where frameworks genuinely diverge — but H3
shows every framework offers *both* code-owned and model-owned routing as a configurable
mode, so this is a knob within a system, not a fixed position between systems. **Ruling:**
report D1 as `{D1-shape: code-compiled | model-reached}` (the real discriminator) +
`{D1-steering: ~always model}` (near-constant, drop as a discriminator) + `{D1-routing:
configurable}`. The old single "code vs model" axis conflated three things.

**Amendment 2 — D6's substrate/service cell fractures into H5's three postures.** The
"meta-harness"/"agent-OS" region of D6 is not one architectural cell; H5 shows the label is
applied to at least three mechanically distinct things:
1. **Wrap** someone else's harness with an ops shell — the customer's loop stays owned by
   their code (Agent Bricks Custom-Code mode, AWS AgentCore Runtime, Azure Hosted Agents,
   Databricks' *Omnigent*). Fits "wraps and runs from outside."
2. **Own** the whole loop and brand it OS — no external harness is wrapped; the platform *is*
   the loop, plus persistence (Letta base, OpenClaw, Hermes, AIOS's Cerebrum-on-kernel).
   Actively *wrong* to call these wrappers — they are competing harnesses.
3. **Generate** the harness from a declarative spec — the platform owns the loop end-to-end
   but the customer never sees scaffolding code (Agent Bricks Declarative mode, Azure Prompt
   Agents). A third thing again.

**Ruling:** "meta-harness"/"agent-OS" is a *marketing umbrella*, not a taxonomic cell. Any
reference to it must specify posture (wrap / own / generate) + D5 lifecycle-layer (dev / run
/ ops). H5's own inverse-correlation finding sharpens this: the more literally OS-shaped a
system is (AIOS's FIFO/round-robin scheduler, mid-token preemption), the *smaller* its
adoption — OS-ness and market footprint run backward in this survey. [strong — H5 verdict]

**Amendment 3 — D3 is elevated, not just confirmed.** H1 filed D3 as real-but-least-named.
H2's class-level synthesis makes it the survey's strongest converged finding (§4b): all three
LLM-first vendors independently designed every safety-critical guardrail to live *outside*
the model's reach, and H3/H4/H5 show code-first, orchestrator, and platform classes enforce
structurally too. For a governance-first engine, D3 is the dimension that matters most.

### 1.2 Final glossary (each ≤3 lines, via the dimensions; ⚠ = the field disputes this)

- **Harness.** The code/infra layer around a model that supplies state, tool dispatch,
  context management, and stop conditions — "everything that isn't the model" (Trivedy, viral
  2026-03-10). Dimensionally: D6-B (opinionated product) at D5-B (run-time). ⚠ *Disputed
  (H1 §4.1):* whether "harness" names the whole runtime layer (Anthropic / Claude Code /
  Codex usage) or narrowly the control-loop-execution mechanism (HuggingFace glossary,
  2026-05-25).
- **Scaffold(ing).** The behavior-defining configuration around the model — system prompt,
  tool descriptions, response parsing, context management. ⚠ *Disputed (H1 §4.1):* Anthropic
  treats scaffold = harness (synonyms); HuggingFace treats scaffold ⊆ harness (the config
  content *inside* the loop mechanism). METR still says "scaffolding"/"elicitation," never
  "harness."
- **Agent framework.** A library/SDK of programmable agent abstractions (model clients,
  tools, memory, loops) that your program imports — D6-A, D1-shape = code-compiled. You own
  operations. (LangChain, Pydantic AI, ADK, CrewAI, AutoGen/MAF.)
- **Workflow orchestrator.** A system where an explicit, externally-inspectable DAG/graph/
  pipeline owns macro control flow, with an LLM call or a whole agent embedded as a *node* —
  D1-shape = graph-owned, D4 = fixed graph. (n8n, Langflow, Archon.) ⚠ *H4 caution:* DeerFlow
  2.0 migrated *out* of this class (fixed pipeline → one skill under a lead agent) — the class
  is a posture a project can leave.
- **Meta-harness.** Marketing umbrella, not a cell. ⚠ *Disputed (H1 §4.3, H5 §6):* applied to
  ≥3 mechanisms — an ops-time outer loop that optimizes a harness/spec from *raw traces*
  (Agent Bricks TAO; the Stanford/MIT "Meta-Harness" paper, arXiv:2603.28052, 2026-03); a
  composition/policy layer over already-running harnesses (Databricks Omnigent; the `omnigent`
  wrapper in H2); Anthropic's hosting substrate agnostic to which harness runs on it (Managed
  Agents). Specify which; the bare label communicates almost nothing.
- **Agent OS / LLM OS / AIOS.** Umbrella for a substrate virtualizing memory/scheduling/tools
  under agents — D6-C. ⚠ *Disputed (H1 §4.5, H5):* the academic sense (AIOS kernel, MemGPT
  virtual memory) is genuinely kernel-shaped; 2025-26 enterprise usage (Fiserv, PwC) is
  governance/orchestration with no scheduler. H5: OS-shape and adoption are inversely
  correlated.
- **ADE (Agent Development Environment).** Letta's single-vendor product name for a dev-time
  visual inspector (context-window viewer, editable memory blocks, tool tester) — D5-A
  (dev-time). Not a generic category; exactly one referent in the evidence.
- **Code-first vs LLM-first.** The D1-shape poles. *Code-first:* your program imports the
  framework and compiles the loop shape — "a library you embed." *LLM-first:* you invoke a
  process that owns the loop and reads your artifacts as data — "an environment you enter"
  (H3 §6.1). ⚠ *Two "code-first" senses (H1 §1.8):* loop-ownership (this one) vs.
  action-space form ("LLM-as-Code"/CodeAct — model emits code instead of JSON tool-calls) —
  different axis, same word.

*Adjacent, for completeness:* **agent runtime** = the execution half (D5-B + D2-durable);
**agent platform** = D6-D managed service, ⚠ H1 §4.6 unresolved whether "platform" is a real
architectural distinction or a pricing tier.

---

## 2. Classification table — both surveys on the ruled dimensions

One row per system. `D1-shape`: model-reached (MR) / code-compiled (CC) / DAG / n-a.
`D3`: advisory / **structural** / mixed. `Memory home` = D2 expressed as where memory lives
(the §3 spine). `Mem-class` = the B-survey coding/personal/dual-use/orchestration axis
(B §1c) — so both taxonomies meet here. Systems marked *(mem-only)* were in the memory
survey but are memory backends or process tools, not harnesses.

| System | Harness class (posture) | D1-shape | D3 enforcement | Memory home (D2) | Mem-class (B §1c) |
|---|---|---|---|---|---|
| **Claude Code** | LLM-first harness | MR | structural (hooks, deny-by-default, sandbox opt-in) | operator/harness markdown (CLAUDE.md, JSONL) + hooks attach | coding-lifecycle |
| **Codex** | LLM-first harness | MR | structural (kernel sandbox, approval axes) | AGENTS.md + JSONL rollouts; coarse memory toggles | coding-lifecycle |
| **opencode** | LLM-first harness | MR | mixed (permission engine hard; **no sandbox**) | nested AGENTS.md via `/learn` | coding-lifecycle *(new — not in B matrix)* |
| **omnigent** | meta-harness (posture 1 wrap) + hybrid | MR (own agents) | structural (6-phase policy, OS sandbox) | n-a (composes others') | orchestration |
| **Pydantic AI** | code-first framework | CC | structural (`requires_approval`, `UsageLimits`, typed retry) | out of core → `pydantic-ai-harness`; RunContext single-run | orchestration |
| **LangGraph** | code-first framework | CC | structural (`interrupt()`/`Command`, injected-store) | checkpoint DB (thread) + durable store (namespace) | orchestration |
| **Google ADK** | code-first framework | CC | structural (`max_llm_calls`, construction-time validation) | `sessions/` + `memory/` services; event-sourced | orchestration |
| **CrewAI** | code-first framework | CC | structural (guardrail loops, `@human_feedback`) | 3-layer: Memory + Flow `@persist` + checkpoint | orchestration |
| **AutoGen / MAF** | code-first framework | CC (MAF adds graphs) | structural (`InterventionHandler`, MagenticOne ledger) | pluggable `Memory` iface (Chroma/Redis/Mem0) | orchestration (MagenticOne = **process** memory) |
| **n8n** | workflow orchestrator | DAG | mixed (Wait/HITL node; agent-box leaky) | workflow static data + execution DB | orchestration |
| **Langflow** | workflow orchestrator | DAG (cycle-tolerant) | mixed (ToolGuard per-call; **no HITL node**) | request/session vars; thin cross-run | orchestration |
| **Archon** | workflow orchestrator | DAG (YAML) | structural (`approval:` node, `until_bash`, fail-closed schema) | event-sourced session + typed `.md` sidecars | coding-lifecycle |
| **DeerFlow 1.x → 2.0** | orchestrator → **LLM-first** (migrated out) | DAG → MR | structural (loop-detect, allowlist, HITL middleware) | ThreadState + async `MemoryMiddleware` | orchestration → coding-adjacent |
| **Databricks Agent Bricks** | platform (posture 1 wrap / posture 3 generate) | n-a (wraps/generates) | structural (Sandbox, MLflow judges) | managed RAG over Unity Catalog | dual-use (managed) |
| **AWS Bedrock AgentCore** | platform (posture 1 wrap) | n-a | structural (Identity, sandbox) | managed "Knowledge & Memory Store" (metered) | dual-use (managed) |
| **Azure AI Foundry** | platform (posture 1 wrap + posture 3 generate) | n-a | structural (VM-isolated sandbox) | managed session state (metered) | dual-use (managed) |
| **Google Vertex Agent Engine** | platform (posture 1/2 hybrid via ADK) | CC (ADK) | structural (governance layer) | managed "Memory Bank" ($0.25/1k events) | dual-use (managed) |
| **Letta (+ ADE)** | platform (posture 2 own) | MR | mixed (read-only blocks; self-edit ungated) | Postgres agent-as-process; 2026 **MemFS** (git-backed .md) | coding-lifecycle (→ Letta Code); genuinely dual |
| **AIOS** | agent-OS (posture 2 own, literal kernel) | MR (Cerebrum) | structural (Access Manager, HITL for irreversibles) | kernel Memory Manager (RAM + LRU-K → storage) | orchestration/infra |
| **OpenClaw** | personal daemon (posture 2 own) | MR | mixed (Sandbox perms; **injection-prone** HEARTBEAT.md) | markdown (MEMORY.md, daily notes) + SQLite index | **personal-companion** |
| **Hermes** | personal daemon (posture 2 own) | MR | mixed (skill-write guards; stale-memory risk) | markdown (MEMORY.md/USER.md) + `state.db` FTS5 | **personal-companion**; genuinely dual |
| mem0 *(mem-only)* | memory backend (dual-use infra) | n-a | n-a (ungated writer) | vector+graph+SQLite triple | dual-use-infra |
| Supermemory *(mem-only)* | memory backend | n-a | n-a (ungated) | cloud CF store | dual-use-infra |
| Memongo *(mem-only)* | memory backend | n-a | n-a (surprisal gate) | single MongoDB polymorphic | dual-use-infra |
| MemPalace *(mem-only)* | memory backend | n-a | n-a (no-LLM extract) | verbatim files + vector + KG | dual-use-infra |
| OpenViking *(mem-only)* | memory backend | n-a | hook-driven (Layer-2 only) | `viking://` FS + vector/RAGFS | dual-use-infra |
| Gbrain *(mem-only)* | memory backend | n-a | write-back discipline | git-markdown SoR → derived Postgres | dual-use-infra (closest to engine) |
| Beads (`bd`) *(mem-only)* | **process-memory** tool | n-a | gated CLI, auto-commit | embedded Dolt (versioned SQL) | coding-lifecycle |
| Superpowers *(mem-only)* | process tool | n-a | convention | git-ignored scratch .md + git log | coding-lifecycle |
| BMAD *(mem-only)* | process tool | n-a | append-only (no edit/delete) | append-only memlog + derived artifacts | coding-lifecycle |
| GSD *(mem-only)* | process tool | n-a | mutable + self-heal | mutable STATE.md + CRUD store | coding-lifecycle |
| Paperclip *(mem-only)* | personal tool | n-a | weekly pass | PARA files + weekly synthesis | **personal-companion** |

**The engine's own row (for reference):** LLM-first harness (posture 2 own, →3 generate) ·
D1-shape MR · D3 structural (pre-commit hook, human gate) · Memory home = markdown+git
operator files · Mem-class = **coding-lifecycle wrapper around oracle-free content** (B §9).
That row is identical in kind to Claude Code's — which is the whole point of §3.

---

## 3. Harness × memory harmonization (the core)

The join: **D2 (where memory lives) is a near-deterministic function of harness class.** Pick
a harness class and you have largely picked your memory home, which patterns come free, and
which you must fight for. Worked per class, then the recurring pairings.

### 3.1 LLM-first harnesses (Claude Code, Codex, opencode)

**Native attach points [strong — H2 §5].** The attach points *are the harness's own file-
injection lifecycle*, exposed with sharply different granularity across the three:
- **Claude Code** — richest: hooks. `SessionStart` injects CLAUDE.md/rules/auto-memory + a
  builder's `additionalContext`; `PreCompact`/`PostCompact` is the one *literal lifecycle
  intercept* a custom memory layer can observe or veto; per-subagent `memory: user|project|
  local` scoping. Hooks are compaction-immune by construction.
- **Codex** — coarse: config toggles only (`generate_memories`/`use_memories`/
  `disable_on_external_context`) over a background-batch pipeline the harness runs; no
  lifecycle event *into* that pipeline. But it ships native **Automations** scheduling.
- **opencode** — most manual: neither hook nor toggle; memory writes only via explicit
  `/learn` distilling into the deepest applicable nested AGENTS.md, re-injected by the
  harness's own file-read logic (`Instruction.resolve`).

**Where memory lives:** operator-owned / harness-native **markdown files** (CLAUDE.md,
AGENTS.md, session JSONL) — the substrate itself.

**B-patterns — supports / fights / impossible:**
- *Supports natively [strong]:* #1 file-first-canonical (the class **is** file-first — B's
  six-independent consensus and this class are the same evidence), #3 bounded size-capped
  injection (CC 200-line/25KB, Codex 32KiB), #4 progressive-disclosure skills (all three ship
  the Agent Skills standard), #5 externalize-durable-surface/resume-by-log (CC's
  survives-compaction re-injection — and this is a *coding-class* discipline whose home is
  exactly LLM-first coding harnesses). #7's disease *and its cure* both live here: instruction
  files degrade to soft hints (the disease), and hooks/deny-rules (the cure) are the native
  attach point.
- *Fights / non-native [strong]:* semantic/embedding recall. None of the three ships it —
  CC does agentic file-read (no index), Codex *chose* grep, opencode does file-read. You'd
  bolt on an MCP vector server. This *aligns* with B-D9 (grep-first, embeddings-deferred):
  grep-nativeness is the path of least resistance, not a limitation to route around.
- *Makes hard [strong]:* two capabilities are simply absent from the class and must be
  built — **cross-machine/durable sync** (auto-memory is machine-local; B §4 config-drift)
  and a **scheduler** (Claude Code has *no native cron*, H2 §4). Codex is the exception on
  scheduling (Automations: cron/webhook/app-event, survives machine-off) — a genuine
  product-level, not maturity, gap between the two vendors.

**Coding-vs-personal:** the entire class is **coding-lifecycle** (B §1c). Its memory is
build/test/convention notes with a *sharp ephemeral/durable split* (run-log vs CLAUDE.md). It
does **not** natively do always-on accumulation — that is the personal-daemon pairing (§3.5).

### 3.2 Code-first frameworks (Pydantic AI, LangGraph, ADK, CrewAI, AutoGen/MAF)

**Native attach points [strong — H3 §*.5].** A typed, code-declared persistence layer:
LangGraph's `InjectedStore` annotation (a node opts into store access, checkpoint vs durable
store split), ADK's `sessions/` + `memory/` services, CrewAI's three independent persistence
events off one task completion, AutoGen's pluggable `Memory` interface. Pydantic AI is the
outlier — memory is *deliberately out of core* (only single-run `RunContext`; store logic
lives in the separate `pydantic-ai-harness` repo).

**Where memory lives:** the **framework store/checkpointer** — typically Postgres/Redis/
vector-DB behind a typed API. *Not* files by default.

**B-patterns — supports / fights / impossible:**
- *Supports [strong]:* #2 append-write/resolve-at-read via event-sourcing (ADK events as
  ground truth; LangGraph per-superstep checkpoint append). The typed/tiered **split-store**
  side of B's contested #5 is this class's home turf — LangGraph checkpoint-vs-store, CrewAI
  3-layer, ADK session-vs-memory — and it makes the split *explicit and typed*, which is the
  good version of it. Conformance-testing-as-spec (LangGraph) is the class's signature
  contribution and B's flagged "single most transferable idea."
- *Fights [inferred, but well-grounded]:* #1 file-first-canonical. The class stores in
  DBs/checkpointers, not a markdown SoR. A markdown+git engine embedding LangGraph would run
  **two sources of truth** (git files + checkpoint DB) — precisely the Beads failure class
  (B §4 #9, opaque-store-vs-git divergence). Human-inspectable memory (git-diffable, gateable)
  also fights an opaque checkpoint row.
- *Effectively impossible without becoming a different system [strong — H3 §6.6]:* adopting
  this class's core idea *literally* means agents are typed Python/Go/.NET objects, not
  markdown personas — "a categorically different system, not an incremental adoption." The
  transferable material is at the metaphor level (typed ceilings, conformance tests, durable-
  replay semantics, typed handoff contracts), not the dependency level.

**Coding-vs-personal:** **orchestration-framework** memory class (memory serves execution).
Its natural pairing is **task-scoped process/checkpoint memory** (the checkpointer *is* the
run state; the store is durable knowledge). The one genuine *process-memory* exemplar in the
whole survey — MagenticOne's task/progress ledger — lives here, and both H3 and B route it to
the task layer (E2), not the knowledge layer (E1).

### 3.3 Workflow orchestrators (n8n, Langflow, Archon, DeerFlow)

**Native attach points [strong — H4].** Workflow-engine state: n8n's static data + execution
DB, Langflow's session vars, and Archon's richest-in-class event-sourced session store + typed
**markdown output sidecars** (`$ARTIFACTS_DIR/nodes/<id>.md`) with cross-run
`persist_session`. The "agent-in-a-box" seam means memory *inside* an agent turn is invisible
to the workflow — capture happens at node boundaries only (all four systems).

**Where memory lives:** the workflow-engine state store; Archon's typed `.md` sidecars are the
closest to file-first in this class.

**B-patterns:**
- *Supports [strong]:* #2 append-write/supersede — Archon's event-sourced immutable
  deactivate-and-replace (never mutate in place) is textbook append+supersede; its
  `output_format` fail-closed schema validation is B's typed-handoff pattern. Archon also
  supplies the survey's sharpest *cautionary* evidence for B §4 #8 (never auto-expire on a
  staleness guess — the false-orphan #1216 incident and its ruled "no autonomous lifecycle
  mutation across process boundaries").
- *Makes hard:* fine-grained mid-turn memory capture is impossible by the agent-in-a-box seam
  — fine for the engine (it captures at session/handoff boundaries, not mid-turn).

**Coding-vs-personal / the real role for the engine [strong — H4 §5.4]:** this class's value
to the engine is **not** as a memory home but as a **wake/dispatch layer over an LLM-first
harness**. Its transferable primitives are exactly the ones Claude Code lacks: native
scheduling (n8n Schedule Trigger, DeerFlow's 2026-07-01 scheduler), HITL-as-a-node (n8n Wait,
Archon `approval:`), cheap-gate-before-spend (Archon `requires:`), typed fail-closed handoff
(Archon `output_format`). Its hard boundary is the mirror of §3.1's: it gives you *when to
invoke / what to hand off / whether to accept-retry*, never supervision inside the turn.

### 3.4 Platform / meta-harness / agent-OS (three postures)

**Where memory lives — the cleanest axis in H5:**
- **Posture 1 (wrap) — cloud platforms:** memory is a **managed, billed, API-mediated
  service** (AWS "Knowledge & Memory Store," Vertex "Memory Bank" $0.25/1k events, Azure
  session state). H5 cross-cutting finding [strong]: **none of the three hyperscalers exposes
  memory as a file a human can open and edit** — all meter it per-event/record.
- **Posture 2 (own):** Letta (Postgres agent-as-process; 2026 **Context Repositories/MemFS** =
  git-backed markdown projection + worktree-per-writer), AIOS (kernel Memory Manager, RAM +
  LRU-K eviction → storage), plus the personal daemons (§3.5).
- **Posture 3 (generate):** memory is whatever the platform generates — opaque.

**B-patterns:**
- *Fights [strong]:* managed-DB memory vs #1 file-first-canonical — memory as a metered
  service is the opposite of a git-diffable file. This is a durable class axis, not a maturity
  gap.
- *Supports + external validation [strong — H5's flagged contribution]:* Letta's MemFS is a
  **second independent lineage** (a VC-funded enterprise memory company) reaching the same
  git-backed-markdown + worktree-per-concurrent-writer conclusion OpenClaw reached — two
  unrelated arrivals validate the engine's markdown+git bet by the engine's own recurrence
  bar. The Meta-Harness paper's "raw traces beat compressed summaries" methodology validates
  the engine reading PROGRESS/HISTORY/git-diffs directly.
- *Do-not-adopt [strong]:* TAO/ALHF auto-optimize-against-self-generated-benchmark with only a
  *lagging* human correction (ALHF is post-hoc). B's gated-promotion consensus (contested #3)
  and Hermes' self-rewrite failure both say don't. H5: the engine's IB-176 per-proposal
  pre-write gate is *ahead of every shipped platform* on this axis.

### 3.5 Personal daemons (OpenClaw, Hermes) — the coding/personal axis made concrete

Broken out from posture-2 because the coding-vs-personal axis is sharpest here.
**Native attach points [strong — H5 §5]:** an always-on daemon process (OpenClaw Gateway with
Heartbeat Runner + Cron Scheduler; Hermes `GatewayRunner` ticking every 60s) writing to
markdown + a search index. **Where memory lives:** local markdown (MEMORY.md, daily notes,
USER.md) + SQLite/FTS5 index. **Pairing:** personal daemons pair with **always-on
accumulation** — a life-cadence journal that grows continuously, distilled by a background
consolidation pass (OpenClaw Dreaming, Hermes curator) — the exact contrast to the coding
class's ephemeral/durable split. Security coupling [strong]: the always-on wake-that-reads-a-
file is *itself* the injection-persistence vector (OpenClaw HEARTBEAT.md → C2 persistence).

### 3.6 The recurring pairings — evidence-backed vs rare/forced

| Pairing | Evidence | Strength |
|---|---|---|
| **LLM-first harness + file-first markdown memory (hooks/file-cmd attach)** | Claude Code (CLAUDE.md+hooks), Codex (AGENTS.md), opencode (nested AGENTS.md); B §1 six-independent file-first | **strong** (H2 + B, same evidence) — *the engine's own pairing* |
| **Code-first framework + checkpointer/store split (task-scoped process + durable store)** | LangGraph checkpoint+store, CrewAI 3-layer, ADK session+memory, Letta tiers | **strong** (H3 + B §3.5) |
| **Cloud platform + managed metered DB memory (API-mediated, non-file)** | AWS Memory Store, Vertex Memory Bank, Azure session state, Agent Bricks RAG | **strong** (H5 cross-cutting, all 3 hyperscalers) |
| **Personal daemon + always-on accumulation to markdown+index** | OpenClaw (heartbeat/cron→daily notes+MEMORY.md), Hermes (60s→USER.md+state.db), Letta Code/Channels 2026 | **strong** (H5 §5 + B personal class) |
| **Git-backed markdown memory + worktree-per-concurrent-writer** | OpenClaw *and* Letta MemFS (2026) — two independent lineages | **strong** for the convergence (H5 flags explicitly) |
| LLM-first harness + native embedding/semantic recall | none of the three ships it; Codex (frontier vendor) chose grep | **rare/forced** [strong] — a bolt-on, never native |
| Code-first framework + file-first-canonical markdown SoR | only Letta MemFS bridges it, and Letta is posture-2-own, not a library-you-embed | **forced** [inferred] — reintroduces two-sources-of-truth (Beads failure) |
| Cloud platform + human-inspectable file memory | does not exist across all three hyperscalers | **impossible** [strong — H5] |
| Workflow orchestrator + fine-grained mid-turn memory capture | agent-in-a-box seam, all four systems | **impossible** [strong — H4] |
| Literal agent-OS (CPU scheduler) + broad adoption | AIOS most OS-shaped, smallest footprint | **inversely correlated** [strong — H5] |

**Where the engine sits — the synthesis payoff.** The engine is pairing #1 (LLM-first harness
+ file-first markdown+git memory) — the strongest, best-evidenced pairing in the survey. That
choice is now **validated twice, independently**: once by the harness-class evidence
(file-first is what LLM-first harnesses natively do — H2) and once by the memory-survey
evidence (file-first-canonical, six independent frameworks — B §1 #1). The two taxonomies
*converge on the architecture the engine already has*. Every "fights/forced/impossible" row
above is a pairing the engine correctly does **not** occupy.

---

## 4. Engine implications

### 4a. E1 memory-spec — does harness evidence change any D-item?

Walked D1–D10 (B §6) against the harness evidence. **Result: zero reversals; one amendment
(D8); D3/D4/D6 gain concrete Claude-Code-native mechanisms; D4's implementation-locus moves to
E4.**

| D-item | Verdict vs harness evidence |
|---|---|
| **D1** per-actor/shared scoping | **CONFIRMED + mechanism.** Claude Code's native subagent `memory: user\|project\|local` scopes (H2 §5) *are* B-D1's directory-isolation, zero new infra — one scope dir per actor. opencode's asymmetric subagent permission inheritance (deny flows parent→child, allow does not) is a portable per-actor write-scoping idea. |
| **D2** append-only run log first | **CONFIRMED.** Codex JSONL rollouts, CC session JSONL, Archon event-sourced history all validate. Fold tool-call detail into run-log events (tool-calls are harness-native events, not a standalone surface). |
| **D3** reflection = gated auditable diary + generate/use two-switch | **CONFIRMED + attach point.** Codex's `generate_memories`/`use_memories` two-switch ships natively (H2 §5) — B-D3 already adopts it as the primitive. New: CC `PreCompact`/`PostCompact` hooks are the *literal lifecycle intercept* the reflection trigger can hang on — reflection need not be session-close-only. |
| **D4** cadence = session-close/idle batch, NOT background daemon | **CONFIRMED, locus moved to E4.** Recommendation unchanged (batch, not sleeptime daemon). But the *scheduling gap* bites: Claude Code has **no native cron** (H2 §4); Codex does (Automations). On the engine's actual harness a scheduled reflection cannot be designed standalone — it must ride E4's wake/dispatch scheduler. Reflection cadence and queue-wake share one missing primitive. |
| **D5** decay/demotion (the item that *moved up* in B) | **CONFIRMED.** No harness ships oracle-based auto-correction for oracle-free knowledge; §3's coding-vs-personal re-confirms the engine = coding-lifecycle wrapper around oracle-free content. Weighting holds. |
| **D6** write-perm on auto-injected surfaces (security) | **CONFIRMED + mechanism.** Codex "Friendly Fire" (auto-trusted AGENTS.md), the deny-makes-invisible pattern, B §4 #3 all converge. The control is a `PreToolUse` hook + deny-by-default rule (native in CC), not prose. Add scan-before-persist. |
| **D7** process memory → E2 not E1 | **CONFIRMED.** MagenticOne ledger (H3 §5.4, a control-flow artifact) + Archon typed sidecars (H4) reinforce: process memory lives in the task/orchestration layer. |
| **D8** lean-on-CC-natively vs build | **AMENDED.** All three build-gaps (cross-machine sync / semantic retrieval / cross-subagent pooling) confirmed by H2 §5–6. **New native gap #iv: scheduling/wake** — no native cron in Claude Code, so any *timed* memory operation (background consolidation) has no native home. Keep "do not build around 'Auto Dream'" (unconfirmed first-party, H2 §1). |
| **D9** recall = ripgrep interim, embeddings deferred | **CONFIRMED decisively.** All three LLM-first harnesses use keyword/grep/file-read; Codex (frontier vendor) *chose* grep — direct vendor precedent. Embedding is non-native (MCP bolt-on), so "deferred" is also the path of least resistance. |
| **D10** Beads query pattern not plumbing | No new harness evidence; unchanged. |

**Single biggest E1 implication:** the memory attach points E1 needs are *already native* in
Claude Code — as **hooks** (`SessionStart` inject, `PreCompact`/`PostCompact` intercept) and
**subagent `memory:` scopes** — so E1 attaches the memory layer to the harness rather than
building storage machinery. **But** the one thing Claude Code does not provide is a scheduler,
so **reflection cadence is not an E1-standalone decision — it rides E4's wake/dispatch
layer.** E1 and E4 are coupled at exactly this seam; the spec should design the reflection
trigger as *a queued job on the E4 scheduler*, not a self-contained E1 daemon.

### 4b. E4 harness epic

**The enforcement-locus consensus — the survey's strongest finding, and E4's reason to exist
[strong].** All three LLM-first vendors converged *independently* on a two-tier split:
LLM-first describes *control flow*, never *enforcement*; every safety-critical guardrail lives
outside the model's reach. Triangulated three ways in H2's class-level synthesis — Claude
Code's own docs ("hooks are code, not judgment"; rules "do not block tool calls"), Codex's
`#25884` (a rule the model correctly *summarized* then stopped *applying* a few turns later),
and opencode's own governance table labeling AGENTS.md "Soft." H3/H4/H5 show code-first,
orchestrator, and platform classes enforce structurally too — so it is really *four* classes
converging, with the three-LLM-first-vendors slice being the engine's own harness. **For E4:**
anything the kernel declares mandatory belongs in a `PreToolUse`-equivalent hook or a
deny-by-default permission rule (which makes the disallowed action *invisible*, never entering
the model's option set), **never in CLAUDE.md prose**. This is exactly PRD E4's acceptance
criterion ("a deliberately induced gate violation is blocked with the harness on and passes
with it off; no mandatory skill depends on unprompted agent memory to fire") and PRD Goal 2's
"removing it observably breaks enforcement." The survey supplies strong, independent,
cross-vendor confirmation the engine's existing posture (DDs immutable, human gate, hooks over
prose) is *correct*, not merely cautious.

**opencode's Plan-mode leak — why the seeded-violation tests are mandatory, not optional
[strong].** opencode's Plan Mode is an architecturally *hard* permission ruleset in source,
yet dated 2026 GitHub issues report it *leaking* in practice — subagents bypass the read-only
restriction (`#26514`), Bash executes during Plan Mode (`#20938`), files edited despite plan
mode (`#32793`) — because enforcement is delivered through two mechanisms (permission deny +
prose reminder) that don't always agree, and subagent delegation slips through. **Lesson: a
source-verified "hard" rule is necessary but not sufficient evidence of *delivered*
enforcement.** Reading Claude Code's hook/permission architecture establishes what is
*designed*; it does not establish what is *delivered*. The engine must empirically test the
exact leak-prone paths practitioners keep finding — **subagent delegation, background/resumed
sessions, mode transitions**. The PRD *already mandates* this discipline system-wide (E4's
negative test; E1's "a seeded violation fails" the store check; E3's seeded schema violation;
E5's `--check` flagging a hand-edit) — the opencode leak is the external evidence that
*validates why* seeded-violation tests are load-bearing across the whole kernel program. Cite
it in the E4 spec as the empirical precedent.

**METR's coin-flip + Archon's rules-layer collapse — twin counter-signals against
over-investing in harness machinery.** H1 §4.4: against a genre of 2026 "harness is the moat"
posts (30+ point swings, harness > model), METR's own Time Horizon research found Claude
Code's specialized scaffold beat a generic ReAct baseline in only **50.7% of bootstrap
samples** (a statistical coin flip), and a Codex scaffold *underperformed* METR's generic
Triframe. This is a live, unresolved empirical disagreement between the term's popularizers and
its original evals-lineage home. It is a **second, independent** counter-signal reinforcing the
engine's *already-held* one — PRD E4/E5 inputs name "Archon's rules-layer collapse (don't
over-layer)" and the PRD Over-layering risk cites Archon deleting its own rules layer.
**Critical reconciliation (do not misread these as contradicting the enforcement consensus):**
METR measured harness effect on *task-success capability* (does the scaffold solve more
tasks); the enforcement consensus is about *governance guarantees* (does the rule hold
regardless of the model). E4 is squarely the *latter*. So: **build the enforcement parts
(hooks/deny-rules) — they are load-bearing and consensus-backed; do not gold-plate the
capability-boosting parts (elaborate skill routing, dynamic sub-harnesses) — METR says the
leverage there is a coin flip.** The discipline that resolves "how much is enough" is the
PRD's own seeded-violation test: build only what observably breaks when removed.

**The three-postures finding — the engine's posture, and what it clarifies for E4/E5.** Today
the engine is **posture 2** (owns the loop — skills run inside Claude Code; the harness *is*
Claude Code; H5 §6 states this outright). Its north star ("portable kernel — materializations
compiled per target," PRD Vision) is **posture 3** (generate materializations from a
declarative kernel spec — PRD E5 is literally posture-3 machinery: "materializations derived
from kernel sources by a compile step"). It is explicitly **not posture 1** — the PRD non-goal
rules out competing with / wrapping orchestration platforms ("the engine compiles *onto* such
substrates; it does not compete with them"). So the engine is **migrating posture 2 → posture
3 via E4 → E5**, and this clarifies the ruled harness-first ordering:
- **E4** formalizes the posture-2 *reference materialization* — make the current owned-loop
  harness's enforcement surfaces named and testable (hooks/checks/config). It builds the first
  compiled target.
- **E5** is the posture-3 move — generalize that reference into a spec that *generates*
  materializations for other targets.
- **The clarity:** E4 must produce a materialization clean enough that E5 can generalize it —
  its hooks/checks should be authored as *instances of a general pattern*, not Claude-Code
  one-offs, so E5 has something to abstract. That is *why* harness-first is correct (you cannot
  generalize a materialization that does not exist yet — the PRD's own rationale). H5's
  Azure "Prompt-Agent vs Hosted-Agent" vocabulary is worth borrowing for the E4 spec: state
  for each engine skill/agent that the engine **owns the loop end-to-end** (posture 2, today)
  as a *deliberate, examined* choice, with E5 turning that owned loop into a compilable spec.

**Single biggest E4 implication:** the enforcement-locus consensus. It is the survey's most
corroborated finding (four classes; three LLM-first vendors independently), it validates E4's
existence and its seeded-violation acceptance criteria directly, and the other three E4
findings are refinements on it (opencode: *verify* the enforcement empirically; METR+Archon:
build only the *minimum* enforcement that breaks-when-removed; three-postures: the enforcement
lives in a posture-2 reference materialization on its way to posture-3).

---

## 5. Contradictions & open questions

1. **METR's coin-flip vs the engine's seven-epic harness-first bet.** The engine ruled
   harness-first and is investing heavily; METR's data says harness *machinery* ≈ coin-flip vs
   generic ReAct for task success. Partly resolved (§4b: E4 is governance-enforcement, a
   different axis than METR measured), but the tension is real for E4's *capability-boosting*
   surface (skill routing, dynamic sub-harnesses). **Open, and the survey cannot settle it:**
   how much harness machinery is load-bearing vs gold-plating? The PRD's seeded-violation test
   ("build only what breaks when removed") is the right *discipline*, but no evidence here
   gives the right *amount* a priori.

2. **The scheduling gap vs the ruled orchestration end-state.** actors.md rules "wake-up is
   periodic and signal-driven" (Owner wakes actors on a schedule); Claude Code has no native
   cron (H2 §4). The end-state needs a scheduler the chosen harness does not provide. Options
   the survey surfaces but cannot rule between: (a) external cron around `claude -p` (H2's
   documented pattern), (b) migrate scheduled parts to a Codex-Automations-style native
   scheduler, (c) adopt a workflow-orchestrator as the wake/dispatch layer over Claude Code
   (H4 §5.4 frames n8n/DeerFlow scheduler *exactly* for this), or (d) build the "meta-harness
   or the Owner itself wakes on a schedule" custom (actors.md). **Tension:** option (c) is the
   cleanest fit for actors.md's orchestration but introduces a second system atop Claude Code
   — brushing the "don't over-layer" risk and the non-goal against orchestration platforms.
   An E4 decision, unsettleable here.

3. **Posture 2 → 3 needs a second compile target the survey can nominate but not choose.**
   PRD E5's acceptance criterion requires "a second target's adaptation commentary" to prove
   the generalized form is not Claude-Code-shaped. **The survey offers a concrete cheapest
   target:** Codex/opencode via the **AGENTS.md open standard** (Agentic AI / Linux
   Foundation, per H2) and the cross-vendor **Agent Skills standard** (agentskills.io, per B
   #4) — both already shared across Claude Code, Codex, opencode, Cursor. A Codex or opencode
   AGENTS.md materialization is the lowest-friction second target because the skill/instruction
   substrate is already portable. *Which* target to commit to is a Nick/E5 decision.

4. **"Physically converged, logically split" (B §3.5) vs code-first's opposite topology.** No
   real contradiction — B already ruled physically-converged for the engine, and H3 confirms
   the code-first split (separate checkpoint DB + store) is exactly what the engine must *not*
   import (two-sources-of-truth = Beads failure). Worth stating as a *convergence*: the
   engine's file-first choice means "embed LangGraph for its store" is a forced pairing to
   avoid — H3 and B agree.

5. **Gated promotion (B contested #3, decisively better-evidenced) vs the "human out of the
   loop by default" end-state (actors.md).** As gates migrate Nick → Owner via delegated-
   judgment grants, is the engine drifting toward the Hermes self-rewrite failure? Structurally
   no — actors.md keeps every delegated ruling *listed for after-the-fact review* and *reversible
   by construction* (two-way-door), which Hermes lacked (no audit trail). **But** the survey
   cannot settle *how far* delegation can safely go before delegated-but-audited becomes
   autonomous-ungated in practice — an autonomy-tier question for future rulings (DD-108
   supervised-autonomy trajectory), not this survey.

6. **Self-modifying memory as a live counter-example the engine rejects.** DeerFlow 2.0 ships
   "custom agents that update themselves — persist edits to their own SOUL.md/config.yaml from
   chat" (H4 §4.7); Letta's self-edit blocks are ungated (B §4 #6). Both are the autonomous
   self-modification B contested #3 and Hermes' failure warn against. Not a contradiction — a
   pattern the engine's human-gate correctly does not adopt — but worth naming since two 2026
   systems shipped it, so it will recur in future intake as a tempting capability.

---

## 6. Evidence-quality appendix

**Perplexity was down or flaky for all five collectors** — every dossier fell back to
first-party docs / WebSearch / WebFetch / `gh`. Calibrate accordingly:

- **H1 (terminology) — strongest in the survey.** Dated primary sources (vendor blogs, arXiv,
  authors' own posts), confidence-keyed (✓/~/?). Terminology and coinage claims are the
  best-grounded material. *Soft spots:* some academic-paper claims ("Self-Harness,"
  "Harness-1") flagged ~/unverified; the **METR coin-flip datapoint is secondary** (adambaitch
  .substack citing METR's published results, not primary-traced) — load-bearing for the §4b
  over-investment caution, so a refresh should pull METR's Time Horizon numbers first-party.
- **H2 (LLM-first) — strong on mechanics.** Mostly first-party docs + dated GitHub issues +
  internal opencode source read; opencode leak reports are dated issues [strong]. *Soft
  spots:* Codex hook blocking-status inconsistent across sources (system still stabilizing);
  headless-billing "paused May–June 2026" is an actively-renegotiated fact, not stable; opencode
  was **not in the prior B memory matrix** — its memory mechanics (nested AGENTS.md via
  `/learn`) are first-characterized here and should be back-filled into the memory taxonomy.
- **H3 (code-first) — strong on mechanics, thin on sentiment.** First-party docs + internal
  repo-analyses solid; sentiment is aggregator-sourced ("directional, not primary"). MAF is too
  new for field sentiment (vendor self-assessment at v1.0); its "Agent Harness"/CodeAct
  numbers are BUILD-2026 vendor claims, un-benchmarked. CrewAI adoption figures vendor-only and
  unit-inconsistent (450M vs 1.4B). A2A tally (3/5) is this-pass fetch.
- **H4 (workflow orchestrators) — mixed; one named inference gap.** n8n/Langflow/Archon
  mechanics well-sourced (first-party + dated issues + practitioner write-ups). **DeerFlow
  sentiment is architectural-inference** — H4 explicitly found no dated 2026 forum/HN threads on
  DeerFlow 2.0 production reliability; the sole signal is *revealed preference* (the 1.x→2.0
  rewrite moving out of the class). Archon's scheduling mechanism is hedged (couldn't confirm
  native cron); the DeerFlow SQLite-multi-worker caveat is only partially legible from a grep
  snippet.
- **H5 (meta-harness/platform/OS) — adoption numbers largely vendor-only.** Agent Bricks (100k+
  agents, 1+ quadrillion tokens/yr) entirely self-reported, no independent corroboration;
  Omnigent has *no* sentiment record (≈5 weeks old at research time); Letta's field reputation
  is *less* confident than OpenClaw's/Hermes' (SEO comparison-blog sourcing, not forum/issue
  voice); AIOS efficiency (2.1×) is paper/vendor with no named production deployments. The
  Meta-Harness paper (arXiv:2603.28052) is the most rigorous non-marketing definition. The
  three-postures correction is H5's own *analytical* contribution (strong reasoning, a
  re-framing rather than a measured finding) — durable, but flag it as judgment, not data.

**Where a future refresh pays off (ranked):**
1. **METR Time Horizon numbers, first-party** — the coin-flip datapoint is load-bearing for
   the E4 over-investment caution and is currently secondary-sourced.
2. **AutoGen/MAF** — H3's fastest-moving package, too new for sentiment; re-verify the
   "Agent Harness"/CodeAct claims independently.
3. **DeerFlow 2.0 production sentiment** — the one architectural-inference gap; a forum/
   Perplexity pass could confirm or refute the revealed-preference read.
4. **Independent corroboration of platform adoption** (Agent Bricks, Omnigent) — all
   vendor-self-reported today.
5. **Codex Memories + hooks** — "newest, least-settled surface," blocking-status inconsistent,
   ~30-day prune third-party; re-verify first-party once stabilized (bears on the D4/D8
   scheduling comparison).
6. **opencode leak-path status** — the Plan-mode-leak issues are the empirical backbone of the
   §4b "verify delivered enforcement" caution; check whether they're fixed (strengthens or
   weakens the caution) before E4 relies on it.

---

*End C-synthesis. Pairs with B-synthesis-memory-survey.md: B ruled the memory architecture, C
rules the harness taxonomy and shows the two meet at the engine's already-chosen pairing
(LLM-first harness + file-first markdown+git memory). Both feed the E1 memory-spec and E4
harness epic; Nick rules.*
