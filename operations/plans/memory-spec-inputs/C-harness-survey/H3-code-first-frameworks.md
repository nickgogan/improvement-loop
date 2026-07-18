---
title: "H3 — Code-First Agent Frameworks — Pydantic AI, LangGraph, Google ADK, CrewAI, AutoGen — Harness-Landscape Dossier"
author: Researcher (external survey, subagent pass)
date: 2026-07-16
part_of: "Harness-landscape survey — C-harness-survey — feeding E1 memory-spec + E4 harness epic"
status: research-input (not a decision)
---

# H3 — Code-First Agent Frameworks

Pydantic AI, LangGraph, Google ADK, CrewAI, AutoGen — the "your code owns the control
flow, the model fills slots inside a program/graph you wrote" class. This dossier tests
that framing against each framework's actual loop-ownership mechanics, then asks what
the class offers or costs a single-operator markdown+git engine that currently lives
**inside** an LLM-first harness (Claude Code) rather than embedding a framework as a
library.

**Headline answer to the framing challenge:** the hypothesis holds at the *shape* level
and bends at the *steering* level, uniformly across all five. Every framework compiles
or constructs a bounded, inspectable, code-owned loop/graph/event-chain (the shape) with
a hard ceiling (max iterations, token/call limits, termination conditions). Inside that
shape, the turn-by-turn decision of whether to call another tool, which tool, and
whether to stop is the model's, every time, in every framework surveyed — including the
ones that look most "graph-first" on the surface (LangGraph, Pydantic AI). Where the
frameworks genuinely diverge is one level up, at *multi-agent routing*: some keep that
code-owned by default (LangGraph conditional edges, ADK Workflow Graph, CrewAI
Sequential), others hand it to the model as a named, first-class mode (CrewAI
Hierarchical, AutoGen SelectorGroupChat/MagenticOne, ADK Chat Transfer). See
§Class-Level Synthesis for the full argument.

**Currency snapshot** (internal repo-analysis dates vs. this pass's external research,
2026-07-16; Perplexity MCP timed out on all 5 attempts today — WebSearch/WebFetch +
first-party docs substituted throughout):

| Framework | Internal analysis | External currency reached this pass | Spectrum position |
|---|---|---|---|
| Pydantic AI | v2.9.0, 2026-07-13 (fresh) | Confirms + extends (durable-exec adapters, MCP maturity, A2A) | study |
| LangGraph | v1.1.6, 2026-04-09 (3 months stale) | v1.2 (2026-05-11) confirmed; no v1.3 found | cherry-pick |
| Google ADK | v2.0.0, 2026-05-25 (~2 months stale) | Bi-weekly cadence into a 2.x series (2.4.0 referenced); v2.0 GA date confirmed 2026-05-19 | cherry-pick |
| CrewAI | v1.14.6, 2026-05-25; escalated-repos.md already updated memory to v1.15.x (2026-07-16) | Control-flow layer (Crews/Flows) unchanged in shape since v1.14.6; AMP/adoption figures updated | cherry-pick |
| AutoGen | v0.7.5, 2026-05-25, frozen (maintenance mode) | Successor **Microsoft Agent Framework** v1.0 shipped 2026-04-03, now the load-bearing package — covered separately below | monitor |

Where this dossier's ground overlaps `B-framework-survey/escalated-repos.md` (memory
architecture for CrewAI, LangGraph, AutoGen), it is skimmed and cross-referenced, not
duplicated — this dossier's lens is the harness/control-flow layer, that one's is memory.

---

## 1. Pydantic AI

Given proportionally the most depth here: freshest internal grounding (2026-07-13,
v2.9.0) and Nick's explicit interest.

### 1.1 Loop ownership

`Agent.run()` compiles to a `pydantic_graph` state machine: `UserPromptNode` →
`ModelRequestNode` → `CallToolsNode` → (loop back to `ModelRequestNode` if tool results
or a validation retry are pending) → `SetFinalResult` → `End`. The graph is the
code-owned *shape*; whether `CallToolsNode` loops back or proceeds to `SetFinalResult`
is entirely the model's decision (did it call a tool, did it produce a final answer).
Every edge in that graph is hookable — 7 hook families × before/after/wrap/on-error
(~28 interception points) — so the shape is not just a diagram, it's an enforcement
surface (§1.3).

One genuine exception to "model steers within the shape": tools marked
`requires_approval=True` **suspend the run entirely** — control passes to neither code
nor model but to an external approver; the run resumes only when approval results are
replayed back into message history. This is Pydantic AI's cleanest true human-in-the-loop
gate, structurally distinct from an advisory checkpoint.

### 1.2 Control-flow substrate

`pydantic_graph` (14 files) is a small, general-purpose typed graph library that both
powers the built-in agent loop internally *and* is exposed publicly for hand-rolled
multi-agent state machines (`docs/multi-agent-applications.md` names "graph-based
control flow" as one of four multi-agent patterns). Durable execution is **not**
reinvented in core — it is delegated whole-cloth to four external adapters living in
`durable_exec/`: Temporal, DBOS, Prefect, Restate, each co-maintained with the vendor
(confirmed this pass via Temporal's own 2026 blog post, DBOS's integration docs, and a
live GitHub issue, `pydantic/pydantic-ai#4446`, proposing a fifth adapter for ZenML —
the adapter family is still actively growing as of mid-2026, not a one-off integration).
Each vendor brings a different durability mechanism: Temporal replays an event history;
DBOS is a lightweight database-backed library with no external workflow engine; Prefect
wraps each LLM/tool call as an individually cached task; Restate journals completed
operations and replays-and-skips on recovery.

For the simpler HITL/deferred-tool case, resumption uses **message-history replay**
(rebuild state by replaying the conversation) rather than a dedicated checkpoint table —
architecturally simpler but coarser-grained than LangGraph's per-superstep checkpoint
rows (§2.2). Pydantic AI is arguably the most architecturally honest of the five about
the checkpoint-vs-durable-execution distinction industry commentary raised in 2026
(§Class-Level Synthesis): it doesn't claim its own native mechanism *is* durable
execution — durable execution is treated as a distinct, fully delegated concern from
day one.

### 1.3 Enforcement points

Guardrails are not a separate primitive — they ride the same 7-hook-family lattice as
everything else (`capabilities/hooks.py`). The documented exemplar
(`PIIRedactionGuardrail`) wraps `after_model_request`; approval workflows wrap
`before_tool_execute`. Hard/deterministic knobs: `requires_approval` per tool,
`UsageLimits`, hook timeouts (`HookTimeoutError`), typed output validation (a malformed
response triggers automatic `ModelRetry`, not silent pass-through). Advisory/soft logic
(cost tracking, prompt-injection detection) rides the same hard mechanism via the
third-party `pydantic-ai-shields` capability package — one interception lattice carries
the whole guardrail taxonomy, hard and soft alike.

### 1.4 Multi-agent coordination model

Four named patterns, ascending autonomy: (a) **agent delegation** — a tool function
calls another agent; code-owned call site, model-owned decision to invoke it; (b)
**programmatic hand-off** — sequential runs where application code or a human picks the
next agent; (c) **graph-based control flow** — `pydantic_graph` state machines, fully
code-owned topology; (d) **Deep Agents** — a documented pattern for planning/spawning
subagent hierarchies, the closest thing to autonomous-crew territory this framework
names explicitly.

Confirmed this pass: **native A2A support** via `agent.to_a2a()` / the `FastA2A` module,
exposing any Pydantic AI agent as an A2A-compliant server in one method call — but as of
Pydantic AI 1.x, `to_a2a()` emits a deprecation warning pointing at the standalone
`FastA2A` library, and will be removed from core in v2. That's a third instance of the
core-vs-harness graduation logic already documented internally (§ Governance Model in
the repo analysis) — except this time graduating **out** to a fully independent package
rather than into the `pydantic-ai-harness` repo. A live issue on
`pydantic/pydantic-ai-harness` (#128) asks whether A2A support belongs in the harness
lane, confirming that repo is an active target for exactly this kind of surface.

### 1.5 Memory attach points

Deliberately not a core-package concern. The hook lattice provides the *mechanical*
attach point (a memory capability could hook `after_run`/`before_model_request`), but
the store and retrieval logic are explicitly named as living in the separate
`pydantic-ai-harness` repo, not core. `RunContext` (deps, usage, message history) is the
only memory-shaped primitive in core, scoped to a single run — cross-run memory is
entirely a harness/user concern. This is the most extreme "keep core lean" position of
the five frameworks on this specific dimension; contrast CrewAI, which ships a
full write-time-classified memory system in its main package (§4.5).

### 1.6 Ops surface

OpenTelemetry-native observability (Logfire is Pydantic's own product, but the
framework emits standard OTel so any collector works); `pydantic_evals` for span-based
evaluation; cassette-based integration testing at industrial scale (1,159 VCR
recordings in the repo's own suite) as a governance-grade example of testing an
LLM-calling codebase deterministically. Deployment itself is **not opinionated** — no
Pydantic-AI-specific hosted platform exists (contrast LangGraph Platform, CrewAI AMP,
ADK's Agent Engine, Microsoft's Foundry Hosted Agents). The closest thing to an ops
story is the durable-execution adapter family, and each adapter inherits *its* vendor's
hosting options (Temporal Cloud, DBOS Cloud, etc.) rather than Pydantic AI shipping its
own.

### 1.7 Practitioner sentiment (dated)

2026 comparison content converges on a **complementary, not competitive**, framing
relative to LangGraph specifically: "Pydantic AI is the right starting point for most
new agent projects in 2026 ... its v1 release in April 2026 made it safe to build
commercial products on" (aggregator-level 2026 comparison blogs — treat as directional,
sourcing beyond the aggregator layer wasn't independently verified this pass). The
pattern several 2026 sources describe as gaining traction: **"PydanticAI for agent
logic and LangGraph for orchestration"** — the two composed rather than chosen
exclusively, evidence against a strict one-framework-per-project mental model for this
whole class (see §Class-Level Synthesis). No sharp negative-sentiment thread specific to
Pydantic AI surfaced this pass, unlike LangGraph's boilerplate complaints (§2.7) or
CrewAI's "over-engineered" critique (§4.7) — plausibly because it's the newest major
entrant and hasn't accumulated multi-year production scar tissue yet. Read the absence
of criticism as **thin sentiment history**, not validated robustness.

### 1.8 What makes it distinctive in this class

- **Type-safety-first as the load-bearing default**, not a bolt-on: Pydantic models are
  simultaneously the tool-argument schema and the output schema, validated
  automatically, with retry-on-failure (`ModelRetry`) as a first-class flow rather than
  an afterthought.
- **The capability primitive is architecturally unique among the five.** No other
  framework surveyed has a *single* primitive unifying prompt-contribution +
  tool-provision + lifecycle-interception + model-settings; the other four keep these as
  separate constructor concerns (a tools list, a `system_message` string, a callbacks/
  hooks argument, model config, as distinct parameters). Pydantic AI collapses all four
  into one shareable, composable unit — "the layer above MCP," per its own framing.
- **Core-vs-harness as a two-*repo* split**, not just a two-namespace one — every other
  framework here keeps its experimental/optional surface in the *same* repository (ADK's
  `labs/`/`skills/` experimental dirs; AutoGen's `autogen-ext`). Pydantic AI's harness
  lane is an independently versioned package family with its own `harness-compat.yml`
  CI contract and an explicit incubation→graduation criterion ("proves itself broadly
  essential"). Durable execution, MCP-adjacent tooling questions, A2A, memory, and code
  mode (Monty-sandboxed) all route through this lane by design.
- **Graph support is optional infrastructure, not the product's identity** — unlike
  LangGraph or ADK's Workflow engine, where the graph *is* the framework's public face,
  `pydantic_graph` mostly stays invisible (it's what `Agent.run()` compiles to) unless a
  developer opts into hand-rolling one for complex multi-agent routing.
- **Durable execution treated as always-external** — confirmed current this pass — is
  the most defensible position among the five on the checkpoint-vs-durable-execution
  distinction industry commentary raised in 2026 (§Class-Level Synthesis, §2.3).

---

## 2. LangGraph

### 2.1 Loop ownership

The Pregel/BSP engine executes nodes within supersteps, synchronizing channels between
them. The prebuilt `create_react_agent`/`create_agent` entry points compile a 2-node
cycle (agent ↔ tools) where the agent node's LLM call decides — via a conditional edge —
whether the cycle continues to `tools` or exits to `END`: the identical
code-owns-shape/model-owns-steering split found in Pydantic AI, implemented via explicit
graph compilation rather than an internal fixed state machine. Hand-built `StateGraph`
pushes further toward code ownership than any other framework surveyed: every edge,
including "does this cycle again," can be an ordinary deterministic Python function with
*zero* model involvement if the developer chooses. LangGraph is the only framework in
this survey where the fully code-owned extreme — no model-decided routing anywhere in
the graph — is a realistic, idiomatic configuration, not just a theoretical possibility.

### 2.2 Control-flow substrate

Pregel (Bulk Synchronous Parallel, from Google's distributed-computing paper) is the
most structurally distinctive execution model in this survey. Typed channels
(`LastValue`, `BinaryOperator`, `EphemeralValue`, `Topic`, `NamedBarrierValue`) are a
richer state primitive than any competitor's plain dict or Pydantic model. **v1.2**
shipped 2026-05-11 (confirmed this pass) adding **graceful shutdown** (stop an in-flight
run cooperatively after the current superstep completes, saving a resumable checkpoint)
and **per-node timeouts** directly in `add_node()` — both squarely production-reliability
features, confirming continued substrate investment through at least May 2026; no v1.3
was found this pass, so treat mid-2026-forward claims as unconfirmed rather than absent.
Checkpointing is automatic — a new row is written after *every* superstep, no manual
call — contrasting with Pydantic AI's default reliance on message-history replay.

### 2.3 Enforcement points

`interrupt()` + `Command` is the cleanest HITL primitive surveyed: a true
execution-pausing gate (state persisted, run halted, resumes only on receiving a
`Command`), not an advisory checkpoint. `InjectedState`/`InjectedStore`/`ToolRuntime`
type annotations form a declarative, opt-in tool-permission model — a tool receives
exactly what its signature declares, nothing ambient. Serialization security
(`SAFE_MSGPACK_TYPES` allowlist, `EncryptedSerializer` AES) is the most
defense-in-depth-postured of the five, matching its Klarna/Replit/Uber/LinkedIn-scale
production base (companies named across multiple 2026 sources this pass).

A 2026 critique worth carrying forward carefully: a vendor blog (Diagrid, which sells
Dapr-based commercial services — read the framing with that interest in mind) argues
LangGraph's checkpointing is "a save point... you are responsible for detecting the
need to use," not true durable execution: no built-in failure-detection watchdog, no
automatic restart, no duplicate-resume protection, no distributed task queue. The
technical distinction is real regardless of the source's commercial angle — it's
exactly why "durable execution [is] becoming a first-class feature across frameworks
like LangGraph, Pydantic AI" (Temporal's own 2026 framing, cited earlier) increasingly
means bolting on an *external* durable-execution engine (Temporal, in LangGraph's case)
rather than trusting native checkpointing alone for crash-safety guarantees beyond
resumability and time-travel debugging.

### 2.4 Multi-agent coordination model

Subgraph composition (nested graphs, state mapped between parent/child schemas) and
`Send`-based fan-out are LangGraph's most distinctive multi-agent primitives — native to
the same BSP execution model as everything else (a sub-agent is just a subgraph node,
not a separate runtime concept), unlike delegation/handoff-style patterns bolted on top
of a single-agent core. `RemoteGraph` extends this to distributed/cross-process graphs
via the LangGraph Server API + SSE — LangChain's own proprietary remote-execution
protocol, notably **not** A2A (no A2A support found for LangGraph in this survey or the
internal analysis; see §Class-Level Synthesis for the cross-framework A2A tally).

### 2.5 Memory attach points

Covered in depth in `escalated-repos.md` §3 (checkpoint/store split, conformance-test-
as-spec, encryption layering) — not duplicated here. For this dossier's harness lens,
the load-bearing fact is mechanical: `InjectedStore` is the attach point (a node opts
into store access via type annotation, exactly like `InjectedState`/`ToolRuntime` for
control-flow concerns), and the conformance suite means any custom backend's
correctness is machine-verified before deployment, not just documentation-asserted —
per this pass, official backends now span Postgres, SQLite, DuckDB, Redis (with vector
search), and MongoDB/Azure DocumentDB, broader than the April 2026 analysis captured.

### 2.6 Ops surface

LangGraph Platform/Server for hosted deployment (Docker-based CLI, SSE streaming).
Production users named across 2026 sources: Klarna, Replit, Elastic, Uber, LinkedIn.
`.github/THREAT_MODEL.md` — an auto-generated, dated security/trust-boundary document —
remains unique among the five surveyed; no comparable artifact exists in Pydantic AI,
ADK, CrewAI, or AutoGen's repos per the internal analyses.

### 2.7 Practitioner sentiment (dated, 2026)

The sharpest boilerplate criticism in this survey. Recurring complaint themes from 2026
review/comparison content (aggregator-sourced — treat as directional, not primary):
"LangChain feels like just a wrapper of wrappers" as "a recurring [HN] comment" carrying
from mid-2025 into 2026 discourse; "a working agent took 4 lines with `create_agent`
versus 17 with a hand-built `StateGraph`"; "a common and expensive mistake is reaching
for a hand-built StateGraph on day one 'for flexibility' before the use case demands it,
then drowning in boilerplate." Countervailing signal from the *same* 2026 commentary
stream: "eight of twelve agentic projects starting in LangChain and four getting
rewritten to LangGraph when state management became the bottleneck" — teams that
outgrow lighter frameworks migrate *to* LangGraph specifically for the state-management
substrate the boilerplate complaints are about. Both signals should be read together:
sentiment is bimodal by workload complexity, not uniformly negative. LangGraph's own API
evolution is a visible response to the complaint — `create_agent`/`create_react_agent`
exist specifically to make the common case low-boilerplate while keeping full
`StateGraph` available for the complex case, the same "hide the graph by default, expose
it on demand" move Pydantic AI makes via progressive disclosure and ADK makes via its
dual Chat-Transfer/Workflow-Graph modes (§Class-Level Synthesis).

---

## 3. Google ADK

### 3.1 Loop ownership

`BaseLlmFlow` (`_AutoFlow`/`_SingleFlow`) implements the internal `call_llm` →
`execute_tools` cycle for a single `LlmAgent` — the same code-shape/model-steering split
as the others. The v2.0 **Workflow** graph engine (`BaseNode`/`Edge`/`Graph`,
`NodeRunner`) is a separate, additive orchestration layer for deterministic DAG
composition of nodes (which can themselves be `LlmAgentWrapper` nodes wrapping an
`LlmAgent`). ADK is the most terminologically explicit of the five about the
code-owned/model-owned distinction this dossier centers on: it names **"Chat Transfer"**
(LLM-decided `transfer_to_agent` mid-conversation) and **"Workflow Graph"** (code-owned
edges) as two distinct, coexisting, individually documented patterns — where the other
four leave this as an implicit consequence of how a developer wires things, ADK gives it
two names and lets the developer pick per use case.

### 3.2 Control-flow substrate

Event sourcing is the persistence model: Events are ground truth, LLM context is an
explicitly named "orchestrated view" derived from them via three distinct
context-pollution countermeasures (task-delegation translation, branch isolation,
history compaction) — the most mature context-vs-persistence separation of the five per
the internal analysis's own "High Priority" findings flag. A 1:1 Context-Node mapping in
the Workflow engine mirrors the parent-child execution tree structurally. HITL interrupt
propagation climbs the ancestor chain via accumulated `interrupt_ids` — a distinct
mechanism from LangGraph's single-point `interrupt()`/`Command` pair, closer to a
bubbling-exception model than a pause-the-whole-graph model.

### 3.3 Enforcement points

`max_llm_calls`/`LlmCallsLimitExceededError` as a hard ceiling; Pydantic
`model_validator`-based agent-config validation at *construction* time (fail before run,
not during); the `@experimental(FeatureName.X)` decorator is a structural, not just
documentational, governance mechanism — it fires a runtime warning on use, gating
adoption of unstable surface mechanically. Naming-as-governance: `UnsafeLocalCodeExecutor`
is explicitly named to signal risk, forcing a conscious opt-in versus the
Docker/GKE/Vertex-AI-managed executors — the internal analysis flags this naming
convention itself as a governance pattern worth carrying forward.

### 3.4 Multi-agent coordination model

The widest named-pattern roster of the five: Chat Transfer, Task Delegation (structured
I/O via `request_task_<name>`/`finish_task`), Sequential/Parallel/Loop agents, Workflow
Graph, **plus A2A protocol support** (`RemoteA2AAgent`, agent cards) for cross-system
interop — confirmed current this pass ("agent-to-agent interoperability" named as an ADK
strength in 2026 review content, and Google's own partner-training material pairs
"ADK, MCP, and A2A" as the three pillars of its 2026 agent-deployment story). ADK is the
only framework surveyed with four distinct multi-agent mechanisms operating
simultaneously at different granularities: conversational routing, structured
delegation, deterministic graph, and a cross-vendor remote protocol.

### 3.5 Memory attach points

`sessions/` (in-memory/SQLite/database/Vertex AI backends) for conversational state,
`memory/` (in-memory, Vertex AI RAG) as a separate cross-session knowledge service — a
two-service split conceptually similar to LangGraph's checkpoint/store divide, but
implemented as named **services** injected into `InvocationContext.services` rather than
a typed-annotation injection pattern. Confirmed this pass: Agent Engine's "sessions and
memory bank" reached **General Availability** in 2026 — the managed-cloud version of
this split is now a supported product, not just a library abstraction.

### 3.6 Ops surface

The deepest deployment optionality of the five: **Vertex AI Agent Engine** (serverless,
"Python-first, no Docker management" per Google's own framing — now folded into the
2026 Google Cloud Next rebrand of Vertex AI + Agentspace into the "Gemini Enterprise
Agent Platform," a name change without a migration requirement for existing customers),
**Cloud Run**, and **GKE Autopilot**, each with dedicated 2026 deployment guides found
this pass. The `evaluation/` module (55+ files: trajectory evaluators, LLM-as-judge,
hallucination/safety evaluation, rubric-based metrics, user-simulation personas) is the
most built-out native eval framework of the five, matching the internal analysis's own
"High" priority flag for Evaluation.

### 3.7 Practitioner sentiment (dated, 2026)

Praised for "the right balance between structure and flexibility" and for being "the
only major framework with a mobile-agent story." Criticized for "beta status across key
SDKs," "Google Cloud deployment lock-in," and "an ecosystem still catching up to
LangGraph" — one 2026 review scored it 3/5 on this basis. A specific, sharp-edged
complaint surfaced this pass that the other frameworks' sentiment coverage didn't match
in concreteness: **"only one built-in tool can be attached per agent, and built-in tools
can't be combined with custom function tools in the same agent."** Versioning moved fast
through 2026: v1.0 GA, then v2.0.0 GA confirmed 2026-05-19 with "breaking changes to the
agent API, event model, and session schema," continuing on a roughly bi-weekly release
cadence into a 2.x series by mid-2026 per PyPI/GitHub release data (one source referenced
version 2.4.0 as "more recent" without a precise date). This dossier's internally-grounded
v2.0.0 snapshot (2026-05-25) is therefore already at least one and plausibly several
minor versions behind current as of 2026-07-16 — treat ADK version-specific claims here
as directionally current, not exact.

---

## 4. CrewAI

### 4.1 Loop ownership

The Agent Execution Loop (per the internal analysis) is the most literally textbook
ReAct implementation of the five: parse the model's response into `AgentAction` or
`AgentFinish`; on Action, execute the tool and loop back; on Finish, validate against
guardrails. This is a Python-level `while`-style loop, not a compiled graph cycle, but
functionally identical to the others in its code-shape/model-steering division.
**Sequential** process is fully code-owned (task order fixed at Crew-definition time;
each task's output mechanically becomes the next task's context). **Hierarchical**
process inverts this: a manager agent (auto-generated or custom) dynamically decides,
at run time, which coworker handles each task. CrewAI's own documentation is explicit
that this is the point where "the LLM is doing the delegation" — making Hierarchical
the most model-owned multi-agent mode among all five frameworks' *named, first-class*
options (not merely a possible custom edge function a developer could theoretically
write, as in LangGraph, but a documented, dedicated mode).

### 4.2 Control-flow substrate

Two structurally separate engines under one package: **Crews** (task-agent
orchestration, Sequential/Hierarchical) and **Flows** (event-driven:
`@start`/`@listen`/`@router` decorators compiling to an implicit DAG, `or_()`/`and_()`
for parallel-trigger composition). A Flow can wrap Crews as steps, so the two compose
rather than compete — "a Flow is a Python class that wraps your Crews and direct LLM
calls inside an event-driven execution engine," per 2026 docs confirmed this pass. A
DocuSign production case study (cited via a 2026 CrewAI production guide) reports
CrewAI Flows generating **"14x less code"** than an equivalent LangGraph implementation
for a comparable stateful workflow — a specific, attributed claim from one customer's
case study, not an independently audited benchmark; treat the multiplier as directional.

### 4.3 Enforcement points

Guardrails as composable output-validation loops — function-based or LLM-prompt-based,
returning `(bool, feedback_or_result)`, with failed validation re-injecting the error and
retrying up to `guardrail_max_retries` — the same "retry-with-error-context" idiom
Pydantic AI implements via `ModelRetry`, arrived at independently. `human_input=True`
(task-level) and `@human_feedback` (flow-level, with approved/rejected/custom-label
routing and non-blocking async providers, e.g. Slack) are CrewAI's two HITL gates — the
flow-level one is notably more flexible (async, non-blocking) than a synchronous
pause-the-process interrupt.

The Diagrid/Dapr critique from §2.3 singles out CrewAI by name for a specific structural
gap: **"CrewAI cannot durably checkpoint ReAct agents mid-iteration through tool
selection; developers must model each action as explicit persisted steps."** In other
words, the Agent Execution Loop's individual tool-selection steps are not themselves
checkpoint boundaries — only Flow `@persist` state and event-driven checkpoints are
(§4.5) — a real granularity gap relative to LangGraph's automatic per-superstep
checkpointing.

### 4.4 Multi-agent coordination model

The Delegation Tool (`delegate_work`) and Ask-Question Tool (`ask_question`) let agents
route to coworkers as ordinary tool calls — model-decided, code-executed, the same shape
as Pydantic AI's agent-delegation-as-tool pattern (§1.4). Hierarchical process is the
framework-automated version of the same idea. Full A2A protocol implementation (agent
cards, three update mechanisms — polling/push/streaming — an A2UI rendering extension)
is, per the internal analysis, notably early ("one of the first frameworks to implement"
A2A); this pass found continued ecosystem discussion of CrewAI's enterprise
interoperability story in 2026 but no A2A-specific update beyond what the internal
analysis already captured.

### 4.5 Memory attach points

Not duplicating `escalated-repos.md` §2's deep coverage (write-time LLM-classified
"Cognitive Memory" — encode/consolidate/recall/extract/forget — plus the three-layer
Memory/Flow-state/Checkpoint split). For this harness-focused dossier, the load-bearing
fact is mechanical: Memory writes, Flow `@persist` state writes, and event-driven
checkpoint writes are **three independent persistence events** that can all fire off the
same task completion, each solving a genuinely different consistency need. CrewAI's
"memory attach point" is plural, not a single seam — more so than any other framework
surveyed here.

### 4.6 Ops surface

**CrewAI AMP** (formerly "Enterprise") — real-time observability tracing "every agent
thought, every tool call, every LLM completion" (2026 vendor material; the specificity
is notable even discounting vendor framing, since it names the tracing *granularity*
explicitly rather than just asserting "observability"). **AMP Factory** for on-premise/
VPC deployment (AWS/Azure/GCP, SSO via Entra/Okta, SOC 2 Type II) is the most
enterprise-compliance-postured ops surface of the five. Adoption-scale claims vary by
source and month within 2026 — "450 million agent-runs/month" (one source, "early
2026") vs. "1.4 billion agentic automations/month" (CrewAI's own blog, "as of April
2026"), with "60% of Fortune 500" repeated across both. Cite as a vendor-reported growth
signal, not an audited figure — the metric definitions (agent-runs vs. automations)
aren't obviously the same unit, so the two numbers shouldn't be read as a single trend
line.

### 4.7 Practitioner sentiment (dated, 2026)

Positive: the DocuSign case study, and CrewAI's own framing that the system "gets better
at retrieving relevant context over time without any manual tuning." Negative/mixed: a
2026 Hacker News thread ("Sick of AI Agent Frameworks," already logged in the
escalated-repos.md memory dossier) names CrewAI alongside LangGraph and AutoGen as
over-engineered relative to a direct LLM-call loop for many use cases — this is a
control-flow-layer complaint as much as a memory one, so it belongs here too. The same
bimodal pattern seen in LangGraph's sentiment (§2.7) recurs: teams that need the
Sequential/Hierarchical/Flows structure report it paying for itself (DocuSign), while
teams below that complexity threshold experience it as overhead. Sentiment tracks
workload scale, not framework quality in the abstract.

---

## 5. AutoGen (frozen) + Microsoft Agent Framework (successor, now live)

AutoGen's own package is frozen (maintenance mode, no new features, per the internal
analysis dated 2026-05-25). Its successor, **Microsoft Agent Framework** (MAF), shipped
v1.0 on 2026-04-03 and is now the load-bearing package for anything forward-looking —
this section covers both, clearly separated, because the harness-epic-relevant material
(the "Agent Harness" vocabulary, CodeAct, Hosted Agents) lives entirely in the successor.

### 5.1 Loop ownership

**AutoGen core** is uniquely, among all five frameworks surveyed, genuinely event-driven
pub/sub with **no fixed loop at all** at the runtime layer — agents subscribe/publish to
CloudEvents-based topics; there is no compiled graph or bounded cycle at the core-runtime
level, the closest thing in this survey to "no predetermined shape." The **AgentChat**
layer built on top reintroduces a loop as a convention (`Team.run()` → `GroupChatManager`
selects speaker → `agent.on_messages()` → check termination → loop) — the shape
reappears one layer up, imposed by the high-level API, not guaranteed by the
core runtime. Within a single `AssistantAgent.on_messages()` call, the model still runs
its own ReAct-style tool loop — the same universal pattern found in all five frameworks.

**Microsoft Agent Framework**, per its v1.0 stabilized surface (confirmed this pass via
Visual Studio Magazine and Microsoft's own devblog, both dated around 2026-04-03), adds
**graph-based workflows** as a first-class capability layered on top of the inherited
event substrate — a genuine architectural shift toward the LangGraph/ADK-Workflow style
of code-owned topology, while retaining AutoGen's orchestration-pattern menu
underneath.

### 5.2 Control-flow substrate

AutoGen core: pub/sub CloudEvents, `SingleThreadedAgentRuntime` for local execution, a
gRPC-based distributed runtime for multi-process deployment. Five named AgentChat
orchestration patterns ride on top — RoundRobin, Selector, Swarm, MagenticOne, DiGraph —
the broadest named-pattern menu of the five frameworks for the *same* layer (multi-agent
team orchestration), because AutoGen treats "which pattern" as a first-class, explicit
choice rather than an emergent property of how edges happen to be wired.

MAF's stabilized 1.0 surface (per the sources above) spans: core single-agent
abstraction + service connectors unified across **.NET and Python**; middleware hooks;
agent memory/context providers; graph-based workflows; and multi-agent orchestration
patterns explicitly named as **sequential, concurrent, handoff, group chat, and
Magentic-One**. This is a direct update to `escalated-repos.md` §4.4, which — via a
thinner, single-`perplexity_ask`-pass research check after two Deep Research timeouts —
could not confirm whether MAF exposed a `MagenticOneGroupChat`-equivalent API and
flagged the pattern as "documented architecture, not confirmed as a shipped primitive."
This dossier's independent search of Microsoft's own devblog and third-party coverage
**confirms Magentic-One survived the succession as a shipped, first-class pattern**,
named explicitly among MAF's stable 1.0 orchestration menu.

### 5.3 Enforcement points

AutoGen core: `InterventionHandler` (`on_send`/`on_publish`/`on_response`, can return
`DropMessage`) is a runtime-level message-interception mechanism registered at
construction time — structurally close to Pydantic AI's hook lattice, but scoped to the
pub/sub layer rather than the single-agent loop. Composable termination conditions
(AND/OR algebra over ~11 named predicate types — token budget, timeout, keyword,
handoff, functional, etc.) is the most systematically enumerated termination-condition
taxonomy of the five.

MAF, per BUILD-2026 devblog material fetched this pass, names **"Agent Harness"** as an
explicit architectural layer — see §5.7 below; the term itself, and its definition, are
significant enough to this survey to warrant a dedicated subsection rather than folding
into enforcement points alone.

### 5.4 Multi-agent coordination model

Covered in depth in `escalated-repos.md` §4 (ledger-based MagenticOne orchestration —
task ledger, plan, progress ledger, stall detection and replanning) — not duplicating
the lifecycle trace here. For this dossier's harness angle, the load-bearing fact:
MagenticOne's ledger is explicitly a **control-flow/orchestration artifact** (it drives
`next_speaker` routing and stall-triggered replanning), not a knowledge-memory artifact —
it belongs as much to "loop ownership" (§5.1) as to memory. The escalated-repos.md
dossier already recommends the E1 spec decide whether it's in scope as a fifth memory
type; this dossier flags the same object from the harness side: MagenticOne is the
single clearest example across all five frameworks of an orchestrator whose control-flow
decisions are not just steered by the model turn-by-turn (true of all five) but
**planned and re-planned by the model at a higher level** — the model owns not only
"what happens next" but "what the plan even is."

MAF's stable multi-agent menu — sequential, concurrent, handoff, group chat,
Magentic-One — spans the same code-owned-to-model-owned spectrum as AutoGen's five
patterns did, now unified across .NET and Python.

**A2A tally note:** this pass's fetch of Microsoft's BUILD-2026 Agent Framework
announcement post found **no mention of A2A protocol support**. Combined with LangGraph
(RemoteGraph, LangChain-proprietary, not A2A) and MAF both sitting outside the A2A
cluster, A2A adoption within this five-framework class is **3 of 5** (CrewAI, ADK,
Pydantic AI) as of this pass — not universal, contrary to what its "150+ supporting
organizations" framing (§1.4) might suggest about industry-wide convergence.

### 5.5 Memory attach points

AutoGen core: abstract `Memory` interface (`update_context`/`query`/`add`/`clear`),
pluggable backends (ChromaDB, Redis, Mem0, Canvas scratchpad, `ListMemory`),
application-code-driven writes (not automatic/LLM-classified — closer to LangGraph's
explicit-write model than OpenViking's or CrewAI's automatic extraction). Not
duplicating further — see `escalated-repos.md` §4 for the full memory-type breakdown.
MAF's stabilized surface names "agent memory and context providers" as part of its 1.0
scope; this pass did not find MAF-specific memory-architecture detail beyond that naming.

### 5.6 Ops surface

AutoGen core: `agbench` (benchmarking), GAIA benchmark integration, a `Replay` model
client for deterministic testing — solid, but frozen; no further 2026 ops investment is
expected in this package.

MAF: **Hosted Agents** via Foundry Agent Service — scale-to-zero (pay nothing while
idle, scales back up on next request), "resume with filesystem intact" (files, disk
state, and session identity persist across scale-to-zero), per-session VM-isolated
sandboxes. Note: the fetched source explicitly frames this as filesystem/session
persistence, **not** as durable-execution/checkpointing semantics in the Temporal/DBOS
sense (§1.2, §2.3) — it's a deployment-continuity feature, not a crash-recovery
guarantee for mid-execution failures.

### 5.7 "Agent Harness" — a terminology convergence worth flagging prominently

Per Microsoft's own BUILD-2026 devblog post (fetched this pass), **Agent Harness** is
defined in-source as *"the layer where model reasoning meets real execution: shell and
filesystem access, human-in-the-loop approval flows, and context management across
long-running sessions."* Concretely: automatic token monitoring and chat-history
compaction (context-overflow prevention), persistent session state via file-based memory
and skill discovery, plan/execute modes, and background-agent delegation. **CodeAct** —
the model writes one short Python program calling tools via `call_tool(...)`, executed
once in a sandbox, instead of a multi-step choose-tool/wait/choose-next-tool loop — is
named as reducing latency by roughly 50% and token usage by over 60% "in representative
workloads" (a vendor claim, dated to the BUILD-2026 post; not independently benchmarked
this pass). CodeAct and Handoff orchestration are explicitly distinguished in the source
material: CodeAct compresses *sequential tool calls within a single agent*; Handoff
coordinates *between* specialist agents.

This is a striking convergence: a major vendor is now using **"harness"** for
essentially the execution-layer concept this survey — and the engine's own North Star
vocabulary (`PROGRESS.md`: "a harnessed, self-describing, single-operator system...
harness materializations compiled per target") — uses the term for. Read the scope
carefully, though: Microsoft's usage (shell/filesystem access + HITL + context
management *within one agent's long-running session*) is narrower than the engine's
usage (the whole enclosing environment an agent runs inside, the thing you invoke *vs.*
the thing you embed). Microsoft's "Agent Harness" sits closer to what this dossier calls
**enforcement points + control-flow substrate** (§5.3, §5.2) than to the full
LLM-first-harness meaning this survey's other legs (Claude Code, GSD, etc.) use the word
for. It is the code-first class's closest linguistic approach to the harness concept,
not an instance of it — MAF is still a library you import and whose graph you compile,
not a process you invoke that reads your markdown.

### 5.8 Practitioner sentiment (dated)

AutoGen core: the internal analysis's own governance-gaps list ("no built-in content
filtering... no RBAC... no audit trail beyond telemetry") is itself a form of documented
critique, dated 2026-05-25.

MAF: too new for accumulated practitioner sentiment distinct from launch-announcement
coverage. Treat "production-ready convergence of AutoGen and Semantic Kernel" as vendor
self-assessment at v1.0 (2026-04-03), not yet field-tested commentary the way
LangGraph's or CrewAI's multi-year sentiment corpus is. Worth revisiting this framework
specifically at the next harness-survey refresh — it's the fastest-moving package in
this class as of mid-2026.

---

## 6. Class-Level Synthesis

### 6.1 What defines code-first as a class

- **Your program is the entry point.** You `import` a library, instantiate typed
  objects (`Agent`, `Graph`, `Crew`, `Team`), and call `.run()`/`.kickoff()`/
  `.invoke()`. This is the structural inverse of an LLM-first harness (Claude Code,
  GSD, and this engine's own current substrate): there, you invoke a CLI/process that
  owns the outer loop, and your artifacts (CLAUDE.md, skills, subagent definitions) are
  *data it reads*, not code that imports it. In this class, the framework is a
  *library you embed*; in an LLM-first harness, the harness is an *environment you
  enter*. The five frameworks surveyed here never invert that relationship — even
  AutoGen's genuinely-no-fixed-loop core (§5.1) is still something your Python process
  imports and drives, not something that invokes *you*.
- **The unit of composition is a typed object or class**, constructed via imperative
  code or declarative config (YAML/JSON — Pydantic AI's `AgentSpec`, CrewAI's
  `agents.yaml`, ADK's YAML agent config), version-controlled and testable with ordinary
  software-engineering tooling — type-checkers, unit tests mocking model responses,
  cassette-recorded integration tests (Pydantic AI's 1,159 VCR recordings is the
  extreme end), CI gates. This is a different verification epistemology than an
  LLM-first harness's eval-transcript-graded-by-another-LLM approach, and it's real,
  not merely aesthetic (§6.4).
- **The "harness," where the term appears at all, is a downstream deployment
  concern** — how you host/scale/observe an already-written program (LangGraph
  Platform, Vertex AI Agent Engine, CrewAI AMP, Foundry Hosted Agents) — not the
  enclosing process that owns the run from the start. Microsoft's "Agent Harness"
  (§5.7) is the one partial exception worth watching: it names an execution-layer
  concept close to but narrower than the LLM-first meaning, folded into a library
  developers still import rather than a process that invokes them.

### 6.2 Where the code-first claim bends — loop ownership, argued across all five

The single-agent tool loop is **uniformly hybrid** across every framework surveyed,
regardless of surface syntax:

```
CODE OWNS (the shape + the ceiling)          MODEL OWNS (the steering)
┌────────────────────────────────┐
│ compiled graph cycle            │
│  (LangGraph create_react_agent, │ ◄── every iteration: continue-or-stop
│   Pydantic AI's node graph,     │     decided by the model's own output
│   ADK's BaseLlmFlow)            │
│  — or a Python while-loop       │
│   (CrewAI's Agent Execution     │ ◄── tool selection + arguments
│   Loop)                          │     decided by the model's own output
│  — or an event chain             │
│   (CrewAI Flows, AutoGen's      │
│   pub/sub-then-AgentChat-loop)  │
│                                   │
│ + a hard ceiling: max_iterations,│
│   max_llm_calls, termination-    │
│   condition trees, UsageLimits   │
└────────────────────────────────┘
              ▲
              │ HITL gate (interrupt()/Command, requires_approval,
              │ @human_feedback, task-level human_input=True):
              │ neither code nor model proceeds — an external actor decides
```

Pydantic AI's `CallToolsNode`↔`ModelRequestNode` cycle, LangGraph's `create_react_agent`
two-node graph, ADK's `BaseLlmFlow`, and CrewAI's textually-literal
`AgentAction`/`AgentFinish` parse-and-loop are the same pattern in four different
syntaxes. **The frameworks that look most "graph-first" on the surface (LangGraph,
Pydantic AI) are exactly as model-steered at this level as the ones that look most
"agentic" (CrewAI).** The code-first hypothesis, read as "the model never decides
control flow," is false for all five; read as "code defines the bounded shape and hard
ceiling the model's decisions execute inside," it holds for all five, uniformly. The
genuine, structurally-guaranteed exception in every framework is the HITL gate — the one
place where the pattern breaks because *no* automated actor (code or model) proceeds
without an external one.

**Multi-agent routing is where the frameworks actually diverge**, and where each one
treats the choice as a configurable knob rather than a fixed philosophy:

| Framework | Code-owned routing mode | Model-owned routing mode |
|---|---|---|
| LangGraph | Conditional edges (plain Python functions) — the idiomatic default | Possible via an LLM-calling edge function, but not a named first-class mode |
| Pydantic AI | Graph-based control flow (`pydantic_graph`) | Agent delegation (a tool call decides), Deep Agents |
| ADK | Workflow Graph (explicit edges) | Chat Transfer (`transfer_to_agent`), Task Delegation |
| CrewAI | Sequential process | Hierarchical process (LLM manager delegates) — named, first-class |
| AutoGen/MAF | RoundRobinGroupChat, DiGraph | SelectorGroupChat, Swarm handoff, MagenticOne (plans *and* re-plans) |

Every framework offers **both** columns; none forces either extreme. That itself is a
class-level convergence: "configurable autonomy" is table stakes across this whole
class in 2026, not a differentiator *between* frameworks — only a differentiator
between *modes within* one framework. MagenticOne (§5.4) is the one mechanism in this
survey that goes further still: the model doesn't just steer within a fixed plan, it
authors and revises the plan itself.

### 6.3 The intra-class spectrum: strictly-typed pipeline ↔ autonomous crew

Position ≈ how much of the control-flow **topology** (not content — topology) is fixed
at compile/definition time versus decided at run time by a model.

```
STRICTLY-TYPED PIPELINE                                        AUTONOMOUS CREW
│                                                                          │
├─ LangGraph hand-built StateGraph (explicit nodes/edges/typed channels)  │
├─ ADK Workflow Graph mode                                                │
├─ Pydantic AI pydantic_graph explicit state machines                    │
├─ CrewAI Sequential process                                              │
│                                                                          │
│         ├─ LangGraph create_react_agent/create_agent (shape fixed,      │
│         │   hidden; still a compiler-owned graph)                       │
│         ├─ ADK LlmAgent w/ tool-based routing                           │
│         ├─ Pydantic AI Agent w/ delegation-via-tool-call                │
│         ├─ CrewAI Flows (developer-defined DAG shape; crew-calls        │
│         │   inside a step can be as autonomous as the Crew allows)      │
│                                                                          │
│                          ├─ CrewAI Hierarchical (LLM manager assigns    │
│                          │   tasks at run time — routing is genuinely   │
│                          │   emergent, not enumerable at definition)    │
│                          ├─ AutoGen/MAF SelectorGroupChat               │
│                          ├─ AutoGen/MAF MagenticOne (plan itself is     │
│                          │   model-authored and revisable on stall)     │
│                          ├─ AutoGen core raw pub/sub runtime (no        │
│                              predetermined topology — the graph is      │
│                              emergent from runtime subscriptions)       │
```

All five frameworks span most or all of this spectrum internally — the spectrum is a
property of the *class*, expressed as a menu of modes each framework offers, not a
property that sorts the five frameworks into fixed positions relative to each other.
The nearest thing to a framework-level (not mode-level) position: LangGraph's idiomatic
default sits furthest toward strictly-typed (§2.1's "fully code-owned extreme... a
realistic, idiomatic configuration"); AutoGen core's raw runtime sits furthest toward
autonomous/emergent (§5.1's "no predetermined shape"); the other three sit in the
middle by default, offering an explicit named escape hatch in both directions (ADK's
two-name policy, §3.1, is the clearest example of a framework being self-aware about
this).

### 6.4 Convergent trends across the class, 2026

- **Durable execution as an externalized, industry-wide concern**, not a framework's own
  checkpointing. Temporal, DBOS, Prefect, and Restate all now integrate with multiple
  frameworks in this class (Pydantic AI natively across all four; LangGraph via Temporal
  per this pass's research). Temporal's own 2026 framing — "durable execution becoming
  a first-class feature across frameworks like LangGraph, Pydantic AI, and the OpenAI
  Agents SDK... no longer optional infrastructure" — and the Dapr/Diagrid critique
  naming LangGraph, CrewAI, *and* ADK together for the same checkpoint-is-not-durable-
  execution gap (§2.3, §4.3), both point at the same underlying convergence: native
  checkpointing solves resumability and inspectability; it does not solve automatic
  failure detection, automatic restart, or exactly-once semantics, and the class is
  converging on solving those by delegating to a dedicated durable-execution substrate
  rather than each framework reinventing one.
- **"Harness" as an emerging, still-inconsistent term of art.** Pydantic AI's separate
  `pydantic-ai-harness` repo, Microsoft's "Agent Harness" concept (§5.7), and the
  Dapr/Diagrid competitor's own framing all use "harness"/"durable execution layer"
  language, but mean three different scopes: an incubation-lane package family
  (Pydantic AI), an execution-layer-within-one-agent's-session concept (Microsoft), and
  a full alternative runtime (Dapr). None of the three matches this survey's own
  LLM-first-harness usage (the enclosing environment/process). Worth tracking as a term
  in flux, not yet a stable cross-vendor concept.
- **Code mode / CodeAct convergent evolution.** Pydantic AI's Monty-sandboxed code-mode
  capability (named "first candidate" for core graduation, per the internal analysis)
  and Microsoft Agent Framework's CodeAct (§5.7) independently arrive at the same
  optimization: let the model write one short program calling tools programmatically
  instead of chaining individual tool-call/wait/tool-call turns. Two unrelated vendors
  converging on the same pattern in the same year is reasonably strong evidence this is
  becoming a class-wide idiom, not a single vendor's bet.
- **A2A adoption is real but partial** — 3 of 5 frameworks (CrewAI, ADK, Pydantic AI),
  not universal; LangGraph and AutoGen/MAF sit outside the cluster as of this pass
  (§5.4). Don't over-read A2A's "150+ supporting organizations" framing as meaning every
  framework in this class has converged on it.
- **"Hide the graph by default, expose it on demand" as a shared response to boilerplate
  criticism.** LangGraph's `create_agent` (§2.7), Pydantic AI's progressive disclosure
  (internal analysis), and ADK's Chat-Transfer/Workflow-Graph naming (§3.1) are three
  independent instances of the same move: keep the low-boilerplate path as the default
  entry point, keep the fully-typed/fully-explicit path available for when the use case
  actually needs it. This is the class's visible, dated (2026) reaction to its own most
  common practitioner complaint.
- **Frameworks increasingly compose rather than compete.** The "PydanticAI for agent
  logic, LangGraph for orchestration" pattern (§1.7), CrewAI's own LangGraph/OpenAI-
  Agents adapters (internal analysis), and ADK's CrewAI/LangChain adapters (internal
  analysis) all point the same direction: by mid-2026, practitioners increasingly pick
  a framework *per concern* (single-agent logic vs. multi-agent orchestration vs.
  deployment) rather than adopting one framework end-to-end. This has a direct
  implication for how to read "market share" or "production adoption" claims in this
  survey — they're not mutually exclusive counts.

### 6.5 What this class offers a single-operator markdown+git engine living inside an LLM-first harness

The engine's current substrate (Claude Code, skills as markdown, control flow largely
the model's own judgment about which skill/tool to invoke next, gated by CLAUDE.md
prose and human review points) sits at the structural opposite end from this entire
class: no compiled graph, no typed channels, no conformance-tested checkpoint backend —
state is markdown files in git, and control-flow *enforcement* is prose the model is
expected to read and follow, not code the runtime mechanically enforces. What this class
concretely demonstrates, worth carrying into E4:

- **A typed, code-enforced ceiling where the engine currently has a prose one.**
  Hard Constraint 2 ("the human review gate is mandatory") is today enforced by the
  model choosing to honor CLAUDE.md and by Nick's out-of-band review — not by anything
  that would mechanically halt execution the way `interrupt()`/`Command`,
  `requires_approval`, or `@human_feedback` do. This is a genuine, not merely
  theoretical, capability gap: an LLM-first harness *can* still implement a real gate
  (a hook that blocks a tool call pending explicit confirmation is structurally the
  same idea as `requires_approval`), it just isn't code-owned in the same
  compile-time-checked sense this class demonstrates.
- **Conformance-testing-as-spec, generalized beyond memory.** Already flagged as "the
  single most transferable idea" in the memory-survey's LangGraph verdict
  (`escalated-repos.md` §3.5) for backend correctness; this dossier's independent read
  reaches the same idea from the control-flow side — any new skill/agent contract
  (`/assess-skill`, `/assess-agent`) could in principle have a machine-checkable
  conformance suite rather than a prose rubric an LLM applies at review time. Not a new
  recommendation, convergent validation from a second angle.
- **Durable execution's replay-from-journal model as an alternative resumability
  epistemology** to the engine's PROGRESS.md/`/session-handoff` pattern. The engine's
  mechanism is prose-mediated (the next session reads PROGRESS.md and infers what to
  do); this class's mature alternative is journal-replay-with-automatic-retry
  (Temporal/DBOS/Restate). The engine's low write-volume, single-operator profile
  doesn't justify importing the infrastructure — but the *epistemology* (a durable,
  replayable record of exactly what completed vs. what's pending, distinct from a
  human-readable summary) is worth holding up against whatever E1's memory-spec lands
  on for the append-only run/progress log.
- **Typed multi-agent handoff primitives as a sharper version of an already-present
  engine idiom.** `Command`, `transfer_to_agent`, `HandoffMessage` are typed,
  runtime-enforced handoff contracts; the engine's Researcher→Codifier handoff via
  `pipeline_status` frontmatter is *already* a lightweight version of the same pattern
  (a typed field the next actor reads to know it's their turn) — convergent validation
  the engine independently arrived at a recognizable instance of this class's idiom,
  not a gap to fill.
- **The core-vs-harness graduation pipeline as convergent validation, not a new
  import.** Pydantic AI's incubation→graduation model (internal analysis) structurally
  matches the engine's own `knowledge/patterns/` → `knowledge/guides/` → `.claude/skills/`
  pipeline — untested ideas incubate, proven ones graduate. Worth naming explicitly in
  any E4 harness-layer design note as prior art the engine already practices, just
  without this class's cross-repo compatibility tooling (`harness-compat.yml`).

### 6.6 What this class costs / doesn't fit

- **Multi-tenant, multi-invocation infrastructure the engine doesn't need.** All five
  frameworks assume threads, sessions, and often concurrent users as baseline
  requirements — vector DBs, Postgres/Redis checkpoint backends, Docker/GKE sandboxes.
  Adopting any of them wholesale would import infrastructure disproportionate to a
  single-operator engine's actual write volume, the same Occam's-razor conclusion the
  memory-survey side already reached for OpenViking's infrastructure
  (`escalated-repos.md` §1.5) and CrewAI's three-layer split (§2.5).
- **The class's central premise is close to incompatible with the engine's foundational
  choice, taken literally.** "Your code owns the control flow" means agents are typed
  Python (or Go/Java/TS/.NET) objects, compiled/typechecked ahead of time. The engine's
  agents (Owner/Researcher/Codifier/Librarian) are markdown personas an LLM roleplays
  into, read by an LLM-first harness — not classes. Importing this class's core idea
  *literally* would mean rewriting the engine's agent layer in a general-purpose
  language, a categorically different system, not an incremental adoption. The
  transferable material is at the **metaphor level** (typed ceilings, conformance
  tests, durable-replay semantics, typed handoff contracts) — not the **literal level**
  (embed Pydantic AI or LangGraph as a dependency).
- **A different, harder-to-port verification epistemology.** Type-checkers, unit tests
  mocking model responses, and cassette-recorded integration tests (Pydantic AI's 1,159
  recordings) don't transfer cleanly to a markdown-native engine where the "unit under
  test" is a prompt or skill's effect on model behavior, not a deterministic function.
  The engine's actual analogues — `/assess-skill` rubrics, DD-92 ContextSpec
  conformance — are already the LLM-first-appropriate translation of the same instinct;
  this class mostly *confirms* the instinct rather than offering a directly portable
  tool.
- **Bottom line.** This class is optimized for teams shipping a product whose users are
  external and whose scale/reliability requirements justify real infrastructure
  investment (CrewAI's Fortune-500 customer roster, LangGraph's Klarna/Uber/LinkedIn
  scale). The engine is a single-operator research/governance tool whose "user" is Nick
  and whose dominant risk is drift and inconsistency, not concurrent load or
  crash-recovery-at-scale. The governance *ideas* this class demonstrates transfer;
  the infrastructure does not — a conclusion that lines up exactly with what the
  memory-survey side already found for OpenViking, CrewAI, and LangGraph's persistence
  layers, so this dossier's engine-relevance verdict is convergent with, not novel
  relative to, the B-framework-survey track.

---

## Sources

**Internal:**
- `systems/improvement-loop/watched-libraries/analysis/{pydantic-ai,langgraph,adk-python,crewai,autogen}-analysis.md`
- `systems/improvement-loop/watched-libraries/{pydantic-ai,langgraph,adk-python,crewai,autogen}.md`
- `systems/improvement-loop/operations/plans/memory-spec-inputs/B-framework-survey/escalated-repos.md` (2026-07-16) — memory architecture for CrewAI, LangGraph, AutoGen; skimmed and cross-referenced, not duplicated
- `systems/improvement-loop/PROGRESS.md` — North Star harness vocabulary

**External (WebSearch/WebFetch, 2026-07-16 — Perplexity MCP timed out on all 5 attempted calls today):**
- Pydantic AI: pydantic.dev docs (durable-execution overview, Temporal/DBOS/MCP pages), DBOS integration docs, Temporal blog "Build durable AI agents with Pydantic and Temporal," GitHub `pydantic/pydantic-ai#4446` (ZenML integration proposal), `pydantic/pydantic-ai-harness#128` (A2A support issue), StackA2A "Build an A2A Agent with PydanticAI and FastA2A," multiple 2026 comparison blogs (xpay.sh, ertas.ai, zenml.io, speakeasy.com) for sentiment/positioning
- LangGraph: docs.langchain.com (durable execution), diagrid.io "Checkpoints Are Not Durable Execution" (vendor-interested, Dapr-affiliated — read accordingly), AWS blog (DynamoDB checkpoint saver), multiple 2026 review/comparison sites (aireviewzones.com, kalviumlabs.ai, upgrad.com, enterprisedna.co) for release/sentiment data
- Google ADK: google.github.io/adk-docs, developers.googleblog.com ("why we built ADK 2.0," agents/A2A enhancements), Google Cloud docs (GKE/Agent Engine deployment guides), benpoole.me "A Year with Google's ADK," futurumgroup.com, chatforest.com ADK 2.0 review
- CrewAI: docs.crewai.com (AMP/enterprise introduction, Flows concepts), crewai.com blog "Lessons From 2 Billion Agentic Workflows," jahanzaib.ai / dev.to CrewAI Flows production guides (DocuSign case study), techjacksolutions.com production guide
- AutoGen / Microsoft Agent Framework: devblogs.microsoft.com/agent-framework (BUILD-2026 announcement — Agent Harness/CodeAct/Hosted Agents definitions fetched directly; "Build your own claw and agent harness" post), learn.microsoft.com/en-us/agent-framework/overview, Visual Studio Magazine "Microsoft Ships Production-Ready Agent Framework 1.0" (2026-04-06), alexbevi.com "Two Lineages, One Framework," langchain.com "LangChain vs. AutoGen in 2026"

**Not reached this pass:** Perplexity MCP (`perplexity_research` ×2, `perplexity_ask` ×3) — all 5 calls timed out (300s) before any WebSearch fallback began; no Perplexity-sourced material appears in this dossier. A future refresh pass should retry Perplexity for deeper multi-source synthesis, particularly on AutoGen/MAF sentiment (too new for this pass to assess) and on independent (non-vendor-blog) verification of the CrewAI adoption-scale figures.
