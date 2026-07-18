---
title: "H5 — Harness survey: Meta-harness / agent-platform / agent-OS class"
type: "resource"
target_system:
  - "improvement-loop"
created: "2026-07-16"
---

# H5 — Meta-Harness / Agent-Platform / Agent-OS Class — Dossier

Harness-landscape survey input for the engine's E1 memory-spec and E4 harness epic. Written
2026-07-16. Perplexity MCP (`perplexity_research`) timed out on all three deep-research
calls attempted for this dossier (300s each, Databricks/Letta/AIOS) — this dossier is built
entirely from WebSearch + WebFetch against vendor docs, launch blogs, GitHub repos/issues,
arXiv papers, and independent review/comparison sites, per the task's fallback instruction.
Internal grounding for §5 (OpenClaw, Hermes) is the existing memory-focused dossiers at
`../B-framework-survey/openclaw.md` and `hermes.md` (2026-07-16) — this dossier does **not**
redo that memory analysis; §5 extracts only the daemon/scheduling/OS-layer facts those
dossiers didn't need.

**Class hypothesis under test** (from the task brief): *these systems wrap and RUN agents
from the outside — evaluation, optimization, scheduling, ops loops around whole agents —
rather than being the loop the model runs in.*

**Early correction, stated up front because it reshapes every section below:** the evidence
does not support one uniform posture. Three mechanically distinct postures are in play, and
conflating them is the single biggest risk in treating "meta-harness"/"agent-OS" as one
class:

1. **Wraps someone else's harness with an ops shell** (evaluation, deployment, security,
   monitoring) — the harness's control loop stays owned by whatever code the customer
   brought. Fits the hypothesis cleanly. Examples: Databricks Agent Bricks in Custom-Code
   mode, AWS Bedrock AgentCore Runtime, Azure AI Foundry Hosted Agents.
2. **Owns the whole harness and brands it "OS"** — there is no external harness being
   wrapped; the platform *is* the loop the model runs in, plus a persistence/memory layer on
   top. Does **not** fit the hypothesis — this is a competing harness, not a wrapper.
   Examples: Letta's base runtime, OpenClaw, Hermes Agent, AIOS's Cerebrum-on-kernel model.
3. **Generates the harness from a declarative spec, so no harness is ever visible to the
   customer** — the platform owns the loop end-to-end but the customer never writes or sees
   scaffolding code. A third thing, not quite either of the above. Examples: Databricks
   Agent Bricks in Declarative mode, Azure AI Foundry Prompt Agents.

Every subject below is characterized against: layer added over a harness (or claim to
replace one); who owns the control loop; enforcement/eval surfaces; scheduling/wake model;
memory as managed service vs. pluggable; multi-agent story; and dated practitioner
sentiment, with vendor-only claims flagged explicitly.

---

## 1. Databricks Agent Bricks

### Snapshot
Databricks' agent-building platform on the Data Intelligence Platform / Mosaic AI stack.
Launched at Data + AI Summit 2025 (InfoQ, 2025-07-28: "Databricks Agent Bricks Automates
Enterprise AI Development with TAO and ALHF Methods"); substantially expanded at DAIS 2026
(Databricks blog, "Agent Bricks: Data + AI Summit 2026," published 2026-06-16). Positioned
as the most significant addition to the Mosaic AI stack in the year between the two summits,
per third-party framing (talentoparati.com, 2026-05-31/06-17).

### Mechanics
A four-step declarative workflow, per the DAIS 2026 blog and the 2025 InfoQ piece:

1. **Task Declaration** — select a task type (Knowledge Assistant/RAG, Information
   Extraction, Custom LLM, Multi-Agent Supervisor, structured document processing), describe
   the goal in natural language, connect data sources (Unity Catalog-governed).
2. **Automatic Evaluation** — the platform auto-generates task-specific eval benchmarks,
   synthetically generating data and/or building custom LLM judges where none exist.
3. **Automatic Optimization** — combines prompt engineering, model fine-tuning, reward
   models, and **TAO** (Test-time Adaptive Optimization) in a search.
4. **Cost/Quality balance** — produces an "Optimal Curve" (a Pareto frontier over
   Latency/Cost vs. Quality) so a team can pick a configuration against a target rather than
   accept a single fixed output.

**TAO** requires only unlabeled usage data — it uses test-time compute plus RL to improve
model quality from historical input examples, scaling with an adjustable tuning-compute
budget rather than human-labeling effort. Databricks' own claim (InfoQ, 2025-07-28, quoting
CTO Matei Zaharia): TAO "can bring inexpensive open source models like Llama to within the
quality of costly proprietary models like GPT-4o and o3-mini" — vendor-sourced, no
independent benchmark reproduction found in this pass.

**ALHF** (Agent Learning from Human Feedback) is the human-in-the-loop correction mechanism:
domain experts give natural-language corrections post-deployment, and an algorithm translates
that guidance into technical adjustments — retrieval-algorithm tuning, prompt refinement,
vector-DB filtering, agentic-pattern changes — without the expert touching code. This is a
**lagging**, post-hoc correction, not a pre-write gate (see Verdict).

**MLflow integration** is the tracing/eval backbone: Mosaic AI Agent Evaluation logs all
eval metrics/data to MLflow Runs; token usage and cost are auto-tracked via MLflow traces.
A 2026 pricing change moved MLflow LLM-judge billing from a fixed price-per-judge-request to
token-based pricing ($0.15/M input, $0.60/M output), which Databricks states "reduces daily
evaluation costs by 95%" (Databricks community blog, "Demystifying Databricks Pricing for AI
Agents," 2026) — vendor-sourced cost-reduction figure. Bring-your-own-LLM-judge (OpenAI,
Anthropic, custom) is supported at no extra evaluation charge.

As of the 2026 update, Agent Bricks spans **three build modes**, which is the single most
important mechanical fact for the class question: **Custom-Code Agents** (any
framework/model — explicitly named compatibility with LangGraph, Agno, CrewAI, the Claude
Code SDK, and OpenAI Agent SDKs), **Declarative Agents** (the original natural-language-spec
mode), and **Agentic AI Functions** (at-scale document/batch processing). MCP integration
(Google Drive, Jira, Slack, GitHub) handles data connectivity; "Databricks Sandbox" provides
secure, downscoped-to-Unity-Catalog VM execution.

### Layer added / control-loop ownership
Genuinely bifurcated by build mode — this is posture 1 and posture 3 from the framing above,
both inside one product:
- **Custom-Code mode = posture 1.** The customer's harness (LangGraph, CrewAI, Claude Code
  SDK, etc.) owns the loop; Agent Bricks wraps it with evaluation, deployment, monitoring,
  security (Sandbox), and MCP-mediated data access. This is the part of Agent Bricks that
  cleanly matches the task's "wraps and runs from the outside" hypothesis.
- **Declarative mode = posture 3.** The customer never writes or sees harness code — they
  write a task description; Databricks generates, evaluates, and optimizes the scaffolding
  end-to-end. There is no "harness" in the traditional sense to point at; Databricks owns
  100% of the loop, but not by wrapping anything.

The DAIS 2026 blog's own framing makes the wrapping posture explicit: *"the core agent loop
is just 1% of the work. The other 99% is the hidden technical debt of agentic systems: token
capacity, deployment, security, evaluation, monitoring, context, sharing."* This is the
single clearest vendor-sourced statement in this entire survey of the "meta-harness wraps
the loop, isn't the loop" hypothesis — but it describes only the Custom-Code half of the
product.

### Enforcement/eval surfaces
MLflow traces + auto-generated LLM judges + synthetic benchmark generation constitute the
quality-eval surface; Databricks Sandbox (VM isolation, downscoped Unity Catalog access) is
the execution/enforcement surface; ALHF is the human-feedback-to-technical-adjustment
translation layer. Notably, this is Databricks' most fully-built-out surface among any
subject in this survey — no other subject researched here ships an equivalent auto-benchmark
+ auto-judge + optimization-sweep pipeline as a first-class product feature (AWS AgentCore
is converging toward this — see §4 — but reached GA on its Evaluations sub-product roughly
eight months after Agent Bricks' 2025 launch).

### Scheduling/wake model
**Absent, and this is itself a finding.** Nothing in the sources describes a cron/heartbeat/
autonomous-wake mechanism for Agent Bricks agents. They are invoked on request (Knowledge
Assistant "Answers," billed per-answer) or deployed as always-on serving endpoints
(Serverless Real-time Inference), not autonomous daemons with their own wake cadence. Agent
Bricks is a request/response service model, full stop — the opposite pole from the
personal-daemon class in §5.

### Memory: managed vs. pluggable
Databricks' "memory" in the sources found is RAG/retrieval over governed data (AI Search,
Unity Catalog) — a knowledge-grounding substrate, not a cross-session
personalization/preference memory in the Letta/OpenClaw/Hermes sense. No `MEMORY.md`-style
durable-fact store or archival-memory tier for an individual agent's accreted state was found
for Agent Bricks specifically. Worth flagging as a real scope gap relative to what "agent
memory" means elsewhere in this survey.

### Multi-agent story
Real and heavily used, not a niche feature: the **Supervisor Agent** mode — "systems of
multiple agents ... auto-optimized using an organization's own data — that work together to
complete tasks across specialized domains" — accounted for **37% of Agent Bricks usage**,
the single largest use-case category, per the DAIS 2026 blog (vendor-sourced usage-share
figure, no independent corroboration found).

### Pricing/positioning
Consumption-based, stacked across many meters rather than one flat platform fee: Knowledge
Assistant Answers priced at $0.075/Answer (promotional rate, billed under the Serverless
Real-time Inference SKU); ingestion/parsing/embedding/AI-Search compute billed under their
own native SKUs; MLflow judge tokens billed separately (see above). Relative to the rest of
the Mosaic AI stack: **Mosaic AI Agent Framework** is the code-first, full-control substrate
for expert practitioners; **Agent Bricks sits on top of it**, trading flexibility for
automation — "task-first" vs. "code-first," per third-party framing (krunalkanojiya.com,
lucentinnovation.com, both 2026). This positioning is corroborated by SunnyData's practitioner
review (below): Agent Bricks in Declarative mode cannot choose models, run A/B experiments,
or tune embeddings/chunking directly — those live one layer down, in the Framework.

### Practitioner sentiment (dated)
- **SunnyData practitioner review** (2026, tutorial-style, reads as independent rather than
  vendor-published): "Agent Bricks represents a powerful step forward in enabling AI
  workflows... lowering the barrier of entry and accelerating prototyping in a way that few
  platforms can match" — but "users cannot choose their own models, run A/B experiments, or
  fine-tune core components like embeddings and chunking strategies, nor is there support for
  advanced orchestration features such as MCP agents or workspace-level action tools. These
  limitations won't matter to casual users, but they can be frustrating for more advanced
  practitioners." This is the clearest independent signal found for Agent Bricks
  specifically.
- **Adoption scale claims are vendor-only.** "100k+ agents built," "1+ quadrillion
  tokens/year," and the named-customer list (AstraZeneca, 7-Eleven, Fox Corp, Block, Merck,
  First American, Edmunds, Workday, Virgin Atlantic, Zapier, EchoStar) all trace to
  Databricks' own DAIS 2026 blog post. **No independent corroboration of these figures was
  found in this research pass** — treat as directional marketing, not verified market signal.
- **Focused independent HN/Reddit discussion of Agent Bricks specifically was sparse.** The
  clearest Hacker News hit found in this pass ("It's worse than I expected," referencing a
  "better models leading to worse tools" post) was about a different topic — benchmarking
  coding agents on Databricks' own large codebase — not Agent Bricks the product. This is a
  genuine evidence gap worth naming rather than papering over: this dossier could not find a
  dated, critical, independent practitioner thread aimed squarely at Agent Bricks' TAO/ALHF
  mechanics or its production reliability, in contrast to the dense practitioner-critique
  trails available for OpenClaw and Hermes (§5).

### Adjacent finding: Omnigent — Databricks' own literal "meta-harness"
Databricks separately open-sourced **Omnigent** under Apache 2.0 on **2026-06-13** (three
days before the Agent Bricks DAIS 2026 blog), explicitly branded a **"meta-harness"** —
Databricks' own words, not this survey's coinage (MarkTechPost, 2026-06-13; Databricks blog,
"Introducing Omnigent: A Meta-Harness to Combine, Control and Share Your Agents").
Mechanically, Omnigent has almost nothing to do with Agent Bricks/TAO: it is a composition
layer that sits **above already-running harnesses you already use** (Claude Code, Codex, Pi,
custom agents via OpenAI Agents SDK/Claude Agents SDK), offering:
- **Composition** — switch between harnesses with one-line changes, combine multiple
  models/harnesses/techniques without rewriting code.
- **Control** — "stateful, contextual policies that track agent actions and enforce
  guardrails like cost budgets and permissions at the meta-harness layer, not via prompts."
- **Collaboration** — share live agent sessions via URL; teammates review/comment/steer in
  real time; launch agents locally or on hosted sandbox providers (Modal, Daytona), access
  from web/mobile/macOS native app or API.

This is a much more literal fit for "wraps and runs agents from the outside" than Agent
Bricks is — Omnigent doesn't optimize a harness's internals (that's TAO's job), it manages
*already-running instances* of other harnesses from outside them.

**Reception is essentially unmeasured as of this dossier's writing.** The only non-vendor
commentary found was a Substack newsletter roundup (Orchestra, week-ending 2026-06-12) that
frames the launch neutrally and *anticipates* skepticism ("expected to be met with some
skepticism," citing Databricks' history and general vendor-lock-in concern) — this is the
newsletter author's own expectation, not a documented reaction, and it is the only
independent source found. No HN/Reddit thread specific to Omnigent surfaced in this pass;
most plausibly the product is simply too new (about five weeks old relative to
2026-07-16) for a sentiment record to exist yet. **Flag clearly: adoption/reception evidence
for Omnigent is effectively absent, not just thin.**

### Verdict
Agent Bricks is the strongest, most concretely evidenced example in this survey of a real
outer-loop evaluation/optimization mechanism (TAO + ALHF + MLflow judges + synthetic
benchmarks) bolted onto — not replacing — a harness the customer can still choose (in
Custom-Code mode). The multi-agent story (37% Supervisor Agent usage) and the "1%/99%"
framing are the most quotable, on-point evidence for the task's whole premise anywhere in
this dossier. Its biggest evidentiary weakness is that essentially every quantitative claim
about adoption, cost savings, and quality improvement is vendor-sourced and uncorroborated;
the one independent review found (SunnyData) is positive-with-caveats but is a single data
point. ALHF's post-hoc-correction shape (fix quality after deployment via natural-language
feedback, not gate writes before they land) is worth naming as a contrast with this engine's
pre-commit human gate — same "human corrects the machine" spirit, opposite timing.

---

## 2. Letta platform + ADE

### Snapshot / lineage
Letta is the commercial/platform continuation of **MemGPT** (arXiv:2310.08560, "MemGPT:
Towards LLMs as Operating Systems," Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang,
Shishir G. Patil, Joseph E. Gonzalez — UC Berkeley, October 2023). MemGPT's core move was to
treat an LLM's context window like OS virtual memory: a small, fast, always-resident tier
(context window ≈ RAM) backed by a larger, paged-out tier the model must explicitly retrieve
from (external storage ≈ disk). The open-source repo **went viral on Hacker News within
hours of being discovered — 11,000 GitHub stars in the first few days — before the team had
formally announced a release** (per Ry Walker's research writeup and corroborated by
multiple sources); the MemGPT open-source project is now folded into Letta.

### Mechanics — the OS claim, mechanically
Letta ships as a **server process** (Letta Server) that persists agent state — memory
blocks, conversation history, tool configurations, model settings — in a **PostgreSQL
database**, addressable via REST API/SDKs. "An agent created once retains its full state...
indefinitely regardless of how many requests are made or how long passes between them" (per
docs/ZenML LLMOps synthesis). This is the most literal "OS" mechanic found anywhere in this
survey: the claim isn't just about memory management (MemGPT's original, narrower framing),
it's that **the agent itself is a persistent server-side process**, analogous to how an OS
process keeps running independent of any particular terminal session attached to it.

### The ADE
The **Agent Development Environment** (announced 2025-01-15) is a visual
inspection/debugging client, not the runtime — it is a window *into* the Letta Server, not
the server itself. What it exposes: the full context-window composition (system prompt,
available tools with I/O, editable core-memory "Blocks," token/character budgets per
component); agent reasoning and tool calls, which are otherwise invisible to end users since
agents must explicitly call a `send_message()` tool to speak to a human (everything else is
internal reasoning, visible only in the ADE); and memory state across all three tiers
(below). Three visualization modes: Debug, Interactive, Simple. Sources did not explicitly
confirm agents keep running with the ADE closed, but this follows directly from the
server-process architecture documented separately — the ADE is a client, and closing a
client does not stop a server.

### Memory architecture (brief — full framework detail belongs to the memory-spec track, not
this harness dossier; noted here only as it bears on the OS/layer claim)
Three tiers explicitly analogized to computer architecture — Core Memory (RAM: small,
in-context, editable blocks), Recall Memory (disk cache: searchable conversation history
outside context), Archival Memory (cold storage: long-term vector-DB, agent-queried via tool
calls). A 2026 addition, **Context Repositories** (2026-02), rebuilt memory for Letta Code
around a **git-backed memory filesystem (MemFS)** — agent memory blocks project onto local
markdown files with git version history, conflict resolution, and direct inspection/editing.
**Sleep-time compute** is a background "sleep" process that reviews recent conversation
history and commits distilled memory into the repository "with informative commit
messages" — mechanically parallel to OpenClaw's Dreaming and Hermes' rumored curator-cron,
but git-commit-native rather than markdown-file-append-native. Multiple subagents get
**isolated git worktrees**, write concurrently, and merge via git conflict resolution — this
is the same coordination primitive (git worktree per concurrent writer) this survey's other
sources reach for independently.

### Multi-agent story
Native and well-documented: a **shared memory block** pattern lets multiple agents read/write
a common "collaborative workspace" block; a **supervisor-worker pattern**
(docs.letta.com/tutorials/multi-agent/supervisor-worker) has a supervisor route tasks to
tagged workers by expertise (`match_all`/`match_some` tag filters); built-in cross-agent
communication tools; a **Conversations API** (2026-04) for shared memory across parallel
user sessions/multi-tenancy; `memory_insert` is additive and conflict-safe for concurrent
multi-agent writes to a shared block.

### Deployment model and pricing
Self-hosted OSS: free, all features included. Letta Cloud: free tier (bring-your-own-key),
Pro at $20/month, an API plan at $20/month base plus $0.10 per active agent per month plus a
small tool-execution fee (aimed at fleets of many long-lived agents). ADE is included in
managed cloud.

### 2026 convergence with the personal-daemon class
Two 2026 launches matter for this dossier's cross-subject comparison: **Letta Code**
(2026-04) — a locally-running, personalized agent that "learns over time" — and
**Channels** (2026-05) — connecting agents to Telegram/Discord/Slack/WhatsApp/Signal,
explicitly **replacing** the standalone "LettaBot" project. This moves Letta's newest
product surface toward the exact same "always-on process + multi-channel gateway +
persistent memory" shape OpenClaw and Hermes were built around from day one (§5) — a third,
independently-arrived-at instance of the same shape, worth flagging as convergent evidence
in the class section.

### Enforcement/eval surfaces
Comparatively thin next to Databricks/AWS. No built-in auto-benchmark generation, LLM-judge
pipeline, or optimization sweep was found in any source. Letta's surface is
**state/memory-inspection** (the ADE), not **quality-evaluation/optimization** — a real,
useful contrast worth carrying into the class section: Letta ships an *observability* layer,
not an *evaluation/optimization* layer, even though both get loosely called "the ops layer
around an agent."

### Scheduling/wake model
The base Letta Server is a request/response persistent-state service — invoked via REST API,
no autonomous wake loop of its own. Sleep-time compute runs during agent idle periods (not
on an explicit cron/heartbeat schedule per the sources found) — closer to "whenever nothing
else is happening" than to a scheduled trigger. The 2026 Letta Code/Channels pivot is where
an autonomous-daemon-with-channels model starts to appear, but this is new territory for
Letta relative to base-platform maturity.

### Practitioner sentiment (dated)
- **"Pragmatic production review"** (aireviewzones.com, 2026) — flagged here as
  **vendor-adjacent, not independent**: despite detailed critical sections, the piece
  cross-promotes other reviews on the same site and concludes with praise for Letta's
  "brilliant operating-system metaphors," reading as marketing-influenced rather than
  disinterested technical scrutiny. What it reports as working: dynamic context compaction,
  git-backed memory concurrency (parallel subagent writes via isolated worktrees without
  corruption), Conversations-API multi-tenancy (hundreds of concurrent user threads per
  agent instance). What it reports as broken: smaller open models (Qwen-2.5-7B,
  Llama-3.1-8B, Mistral-7B) frequently fail at JSON parsing and tool invocation; multi-agent
  ReAct loops can burn **"up to 15× more tokens than standard single-agent chats"**; local
  inference needs 600-second timeouts during context-compaction; accuracy "drops of up to
  50%" past 30K-token tasks (no methodology or date given for this last figure — treat as
  unverified).
- **Framework lock-in is the most consistent independent criticism** (aggregate 2026
  sourcing): "Letta is not just a memory layer, it is a full agent runtime... to use Letta's
  memory, agents must run inside the Letta environment." Contrasted explicitly against
  pluggable-memory competitors (Mem0) that "operate entirely out-of-band." Migration cost
  framed sharply: "you're not just swapping out a memory layer — you're rebuilding your
  agents from scratch." Teams moving prototypes to production specifically cite this
  lock-in, plus "the unpredictability of self-editing memory," as reasons to evaluate
  alternatives.
- **A genuine evidence gap, stated plainly:** unlike OpenClaw (a dense HN pile-on trail) and
  Hermes (a dense GitHub-issue trail), this research pass did not surface a sharp, dated,
  independent HN/Reddit thread specifically about Letta-the-platform in 2026. Available
  sentiment leans on SEO-oriented "X vs. Y" comparison-blog content, which is a structurally
  weaker signal (these sites often cross-sell competing products and have their own
  monetization incentive) than direct forum/issue-tracker discussion. This dossier is
  explicitly less confident about Letta's true field reputation than about OpenClaw's or
  Hermes' as a result.

### Verdict
Letta is the cleanest instance in this survey of posture 2 — **owns the whole harness, brands
it OS** — not a wrapper around anything. Its OS claim is mechanically the most literal (agent
= persistent server process with a DB-backed identity that outlives any client), and its 2026
git-backed-memory pivot is independently convergent with this engine's own markdown+git
architecture (see class section — this is now a second, unrelated lineage reaching the same
conclusion). Its evaluation/optimization surface is essentially absent, which is a genuine
gap relative to the Databricks/AWS class, not a stylistic choice this dossier can spin
positively. Framework lock-in is real and well-attested independently, and should weigh
against treating "adopt Letta" as a live option for anything that isn't already all-in on its
runtime.

---

## 3. AIOS (academic agent-OS project)

### Snapshot
AIOS ("AI Agent Operating System," `github.com/agiresearch/AIOS`, associated with the AGI
Research group / Rutgers, key paper "AIOS: LLM Agent Operating System," Kai Mei, Xi Zhu,
Yongfeng Zhang et al., arXiv:2403.16971, first posted March 2024, currently at revision v5).
The paper was accepted at **COLM 2025** (Conference on Language Modeling), with related work
at NAACL 2025 and ICLR 2025. AIOS was also a **finalist in the AgentX – LLM Agents MOOC
Competition** (Berkeley RDI). This is an academic project with a genuine open-source
release, not a research-paper-only artifact.

### Architecture — the most literal "kernel" in this survey
A three-layer design: **Application Layer** (agents interact only through the AIOS SDK,
**Cerebrum** — no direct resource access) → **Kernel Layer** (LLM-specific services plus
traditional OS operations) → **Hardware Layer**. Kernel components, per the paper:

- **LLM Core** — wraps LLM instances as "cores" (CPU-core analogy), a unified API across
  cloud providers (OpenAI, Anthropic, Google) and local backends (vLLM, Ollama, Hugging
  Face).
- **Scheduler** — centralizes *all* system-call queues (rather than distributing them per
  module). Two strategies: **FIFO** and **Round Robin** with context-interruption for
  genuine time-slicing across concurrent agent calls.
- **Context Manager** — preemptive multitasking via snapshot/restore: "logits-based"
  snapshots for open-source models, "text-based" snapshots for closed APIs — lets the kernel
  interrupt LLM generation **mid-token** without recomputing from scratch.
- **Memory Manager** — RAM-resident interaction histories with **LRU-K eviction** once
  memory exceeds 80% of allocation, spilling infrequently-accessed items to the Storage
  Manager.
- **Storage Manager** — persistent files plus vector-DB capability: versioned file
  management, thread-safe per-file locks, semantic search.
- **Tool Manager** — dynamic tool loading, hashmap-based concurrent-access conflict
  resolution, pre-execution parameter validation.
- **Access Manager** — privilege-based cross-agent access control, plus human-in-the-loop
  prompts for irreversible operations (deletion, privilege changes).

**This is the only subject in this survey with a literal, CPU-scheduler-style mechanism** —
FIFO/Round-Robin queues, mid-token preemption via snapshot/restore, thread-bound system
calls preventing one agent from monopolizing shared LLM resources. The paper reports solving
a concrete, named failure mode of naive concurrent-agent frameworks: prompts converted to
tensors loaded into GPU memory until CUDA OOM. Benchmarks (GPT-4o-mini, Llama-3.1-8B,
Mistral-7B): HumanEval via ReAct improved 48.8%→50.6% with AIOS; GAIA via AutoGen improved
7.3%→9.7%; SWE-Bench-Lite via MetaGPT held at 5.9%. Framed primarily as an **efficiency**
contribution: **2.1× throughput improvement**, with scalability tested across 250–2000
concurrent agents showing linear execution-time/wait-time scaling and a *growing* efficiency
gap favoring AIOS as concurrency increases — the quality deltas are modest; the efficiency
claim is the paper's real payload.

The **Agent SDK (Cerebrum)** is a separate repository from the kernel (AIOS), with framework
adapters supporting ReAct, Reflexion, AutoGen, Open-Interpreter, and MetaGPT "without agent
code modification," communicating to the kernel over HTTP via a unified `send_request()`
call.

### Is it live or stalled in 2026?
**Live but modest**, and the two facts sit in tension. GitHub: latest release **v0.3.0
(2026-01-22)**; commit activity through **2026-06-22** (Cerebrum SDK last touched
2026-04-23); **6.1k stars, 860 forks**. That star count is three orders of magnitude below
OpenClaw's (~346k) and roughly thirty-fold below Hermes Agent's (~211k) — both personal-
daemon projects with a fraction of AIOS's academic rigor. No named production
deployments/customers surfaced in this research pass. Academic credentials (COLM 2025,
AgentX finalist) continue accruing through 2025–2026, but that is conference/competition
recognition, not market adoption.

**Aggregate synthesis on real-world influence** (WebSearch-synthesized characterization,
not a single directly-quoted primary source — flagged accordingly): *"Most production teams
treat AIOS as a research grammar — they adopt the module decomposition and the interface
discipline, while implementing each module in whatever language and runtime fits their
existing stack."* This is consistent with everything else observed: modest stars, academic
venue, no customer logos, but the six-module decomposition (scheduler / context manager /
memory manager / storage manager / tool manager / access manager) shows up as *vocabulary* in
multiple third-party "agent OS" explainers found during this research pass (e.g.,
Knowlee.ai's "AIOS Explained (2026)," OrchestrAI's "Agent Operating System: Architecture, 5
Layers & Examples (2026)") even where the underlying implementation is not AIOS itself.

### Positioning vs. MemGPT/Letta
The two "LLM OS" lineages target different scopes and, per sources found, do not integrate
with each other. **AIOS** emphasizes offloading to and scheduling the underlying
OS/hardware resources — concurrent LLM calls, GPU memory, multi-agent throughput; a
systems/infrastructure-resource-management framing. **MemGPT/Letta** emphasizes virtual
memory for a *single* agent's own context window — a memory-hierarchy framing, largely
orthogonal to concurrent-multi-agent scheduling. Both independently claim "OS" branding;
neither depends on or cites deep integration with the other in the sources reviewed. They
read as complementary in principle (AIOS could in theory schedule Letta-style agents) but
nothing found suggests anyone has actually combined them.

### Layer added / control loop / enforcement / scheduling / memory / multi-agent (compact)
- **Layer/control loop:** posture 2 (owns the loop) for anything running through Cerebrum on
  the AIOS kernel — but crucially, AIOS also supports adapting *existing* multi-agent
  frameworks (AutoGen, MetaGPT) to run *under* its scheduler "without agent code
  modification," which is closer to posture 1 (wraps someone else's framework) at the
  scheduling layer specifically. AIOS is the one subject in this survey that plausibly
  straddles both postures simultaneously by design.
- **Enforcement/eval:** Access Manager (privilege control + human-in-the-loop for
  irreversible ops) is the enforcement surface; no evaluation/optimization-sweep surface
  (no TAO/ALHF/MLflow-judge equivalent) was found.
- **Scheduling/wake:** the most literal scheduler in this survey (FIFO/Round-Robin,
  preemptive snapshot/restore) — but this schedules *concurrent inference calls*, not
  autonomous wake-ups of an idle agent; it has no cron/heartbeat concept because it assumes
  agents are already being invoked and need fair, efficient resource-sharing, not a reason
  to wake up in the first place.
- **Memory:** managed by the kernel's Memory Manager (RAM + LRU-K eviction to Storage
  Manager, which adds vector search) — a genuinely OS-style memory hierarchy, pluggable in
  the sense that it's open-source and self-hosted, not a billed managed service.
  Not compared favorably or unfavorably against Letta's three-tier model in any source
  found; the two systems solve adjacent but distinct problems (concurrent-agent memory
  isolation vs. single-agent context virtualization).
- **Multi-agent:** handled via framework adapters (AutoGen, MetaGPT, etc.) rather than
  native orchestration primitives of its own — AIOS provides the scheduling substrate
  multiple agents run *on*, not a supervisor/worker pattern of its own the way Letta does.

### Verdict
AIOS is the strongest evidence in this survey that a literal, CPU-scheduler-shaped "agent
OS" is buildable and even measurably effective at its stated efficiency goal — and also the
strongest evidence that literal OS-ness is not what's driving adoption or mindshare in this
space. The correlation across this whole dossier is genuinely inverse: the more an artifact
resembles a textbook operating system (AIOS), the smaller its footprint; the more commercial
traction an artifact has (Agent Bricks, Bedrock, Vertex), the less anything resembles a CPU
scheduler and the more it resembles a managed cloud request/response service. Worth carrying
into the class section as a named, quotable pattern.

---

## 4. Cloud agent platforms in brief

### AWS Bedrock AgentCore
Reached **general availability at the end of April 2026**. Architecturally decomposed into
roughly a dozen independently-billable sub-services across five billing patterns
(per-session active consumption, per-request, per-record, pass-through, free/preview):
**Runtime** ($0.0895/vCPU-hour + $0.00945/GB-hour, per-second billing with a 128MB
minimum), **Gateway** (tool/integration routing), **Memory** ("Knowledge & Memory
Store" — RAG knowledge base plus agent memory), **Identity**, **Observability**, and
**Evaluations** (reached GA **2026-03**, roughly eight months after Agent Bricks' 2025
launch) — plus a **2026-06** release of "new optimization capabilities" explicitly framed
as turning "production traces into continuous improvement." AWS is visibly building the
same eval-loop-around-agent posture Databricks shipped first, just decomposed into more,
smaller, separately-metered named products. Runtime itself is framework/model-agnostic — a
hosting layer for whatever agent code you bring, not a competing harness — putting AgentCore
squarely in posture 1. **Practitioner sentiment (2026, "months of production" retrospective
accounts):** default service quotas "shockingly low" for real-time production apps; a
multi-tenant "noisy neighbor" effect producing observed latency variance (2s at 8am vs. 6s
at 2pm during peak US business hours); no built-in semantic caching or automatic model
fallback in the Gateway (a Claude 500 error crashes the app absent custom retry logic);
managed Knowledge Bases feel "rigid" once scaled past proof-of-concept. Both runtime **and**
ops layers are present, but per these accounts the ops/evaluation maturity visibly lags the
runtime's GA date.

### Azure AI Foundry Agent Service
Cleanly illustrates the control-loop-ownership spectrum **within a single product**, which
makes it a useful boundary reference regardless of adoption scale: **Prompt Agents** are
fully platform-owned (author via portal or SDK/REST; "no application code to maintain, no
compute to pay for, no containers to optimize, scale, or patch" — posture 3, generated
loop, nothing to wrap) versus **Hosted Agents**, which run externally-authored frameworks
(Microsoft Agent Framework, LangGraph) inside Azure-managed, **per-session VM-isolated
sandboxes** — dedicated compute/memory/filesystem per session, state persisting across
`$HOME` and `/files` through scale-to-zero idle periods and resuming exactly where a session
left off on the next request (posture 1, classic wrap-and-host). No extra charge for
Foundry-native Prompt/workflow agents beyond model-token consumption; Hosted Agents and
Tools/IQ connections bill separately; realistic deployment costs run $500–1,500/month for
small pilots and $2,000–8,000/month for medium enterprise deployments per 2026 cost-guide
estimates. **Practitioner criticism (2026 comparison pieces):** "surface sprawl" at the
high end and "cost structure opaque until production traffic" at the low end; hard
Azure-lock (Entra ID/Azure-networking dependency, no multi-cloud path); a conversation-
oriented design not well suited to long-running stateful tasks needing checkpoint/resume; no
native versioning, rollback, or CI/CD (teams must bolt on Azure DevOps or GitHub Actions
manually) — i.e., relative to AWS's more explicit, separately-named Evaluations/Optimization
products, Azure's ops/governance layer reads as comparatively thin in these accounts.

### Google Vertex AI Agent Engine
Rebranded the **Gemini Enterprise Agent Platform** at Cloud Next 2026, folding in
Agentspace (existing customers unaffected; same service under a new name). Bundles a
code-first dev kit (**ADK** — customer owns the agent-loop code, posture 1/2 hybrid
depending on how it's used), a low-code visual builder (**Agent Studio**), 200+ foundation
models (Gemini, Claude, others), a managed **Runtime** (deployment/scaling/session
management: $0.0864/vCPU-hour + $0.0090/GB-hour, with a free tier of 50 vCPU-hours + 100
GB-hours/month), a persistent **Memory Bank** (a managed, billed memory service — $0.25 per
1,000 events or memories, billing effective **2026-02-11**), and enterprise governance.
Realistic production support-agent costs run $500–2,000+/month per 2026 estimates. **A
practitioner complaint specific to the scheduling/wake dimension this dossier is tracking
across every subject:** "scheduling is difficult... practitioners would prefer the ability
to set repetitive jobs easily rather than scheduling individual instances repeatedly" — a
concrete, named gap versus the cron-native personal-daemon class in §5, and even versus
Agent Bricks' simpler request-driven model.

**Cross-cutting note for all three cloud platforms:** memory is uniformly a **managed,
billed, API-mediated service** — sharp contrast with the personal-daemon class (OpenClaw,
Hermes: local markdown files) and with Letta's git-backed MemFS. None of the three cloud
platforms expose memory as an inspectable file a human can open and edit directly; all three
meter it per-event/record. This is a clean, durable axis for the class-level section.

---

## 5. Personal-daemon agent-OS claimants: OpenClaw and Hermes — the daemon/OS layer

This section extracts only the **always-on-process / channel / scheduling / OS-layer**
facts not covered by the existing memory-focused dossiers at `../B-framework-survey/
openclaw.md` and `hermes.md` (2026-07-16) — see those files for memory architecture,
lifecycle traces, and the full security-incident record. Do not re-derive that material
here.

### OpenClaw
The **Gateway** is a **WebSocket Server process** containing a Session Registry, Command
Queue, **Heartbeat Runner**, **Cron Scheduler**, and Event Broadcaster
(docs.openclaw.ai/gateway/heartbeat). Confirmed explicitly in the docs: **"Cron runs inside
the Gateway process, not inside the model, and the Gateway must be running for schedules to
fire"** — an unambiguous always-on-daemon requirement for any scheduled behavior.

Two distinct scheduling primitives, deliberately separated:
- **Heartbeat** — a periodic turn in the agent's **main session** (shares conversation
  history by default), default interval **30 minutes** (60 minutes under Anthropic
  OAuth/token auth), configurable or disableable, manually triggerable
  (`openclaw system event --mode now`). Reads an optional `HEARTBEAT.md` checklist; default
  prompt explicitly guards against hallucinated self-tasking: *"Do not infer or repeat old
  tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK."* Purpose is
  **awareness/surfacing**, not background task execution — it does not create persistent
  task records.
- **Cron** — detached, isolated background sessions with persistent task records; supports
  one-shot timers, fixed intervals, and full cron expressions with timezone handling. Cron
  lanes always take priority over/defer heartbeat runs to avoid collision.

The docs frame the always-on requirement as central to the product's identity, not
incidental: *"On a laptop heartbeat is annoying because your machine sleeps and the app
closes, but on a VPS heartbeat and cron stay alive, which is the whole point of hosting
OpenClaw somewhere that does not go to sleep."*

**Multi-agent:** subagents spawn via a `sessions_spawn` tool or `/subagents spawn` command —
non-blocking (returns a run ID immediately), fully isolated sessions (own context, memory,
execution environment), configurable per-subagent model/reasoning-level choice. **The
hierarchy is explicitly flat: subagents cannot spawn further subagents** — the main agent
must fully decompose a task upfront, a concrete, named architectural limit.

**Security cross-reference (already documented in the memory dossier, restated here only
because it's a daemon-layer fact, not a memory-layer one):** `HEARTBEAT.md` is itself a
documented indirect-prompt-injection target — an attacker-controlled instruction written
into the heartbeat checklist can make the agent "silently await commands from an attacker C2
server," surviving restarts because the Gateway re-reads the file on every heartbeat tick.
The always-on daemon model and the security surface are directly coupled: a periodic,
autonomous, unsupervised wake-up that reads a workspace file is exactly the mechanism an
injected instruction needs to persist and re-trigger.

### Hermes Agent
The **gateway** is a **single long-running daemon process** (`gateway/run.py`,
`GatewayRunner`) — "long-running process with 20 platform adapters, unified session
routing, user authorization, slash command dispatch, hook system, cron ticking, background
maintenance" (hermes-agent.nousresearch.com/docs/developer-guide/architecture). The
scheduler **ticks every 60 seconds**, running due jobs in isolated agent sessions. Each CLI
profile runs its **own isolated gateway daemon** (own `HERMES_HOME`, config, memory,
sessions, gateway PID) — multiple profiles run concurrently without resource contention.

A meaningful architectural difference from OpenClaw: **the CLI is daemon-independent** —
`cli.py` invokes `AIAgent.run_conversation()` directly, with no dependency on the gateway
process. You can use Hermes entirely ad hoc, without ever running the daemon — unlike
OpenClaw, where cron/heartbeat (and by extension the docs' own framing of the product's
purpose) require the Gateway to be running. Hermes cleanly separates "occasional CLI use"
from "always-on daemon use"; OpenClaw's docs frame always-on VPS hosting as close to the
point of the product.

**Cron** is first-class, built, and documented: jobs stored in `jobs.json`, multiple
schedule formats supported, can attach skills/scripts, deliver to any of the 20 platform
adapters (Telegram, Discord, Slack, WhatsApp, Signal, Matrix, etc.). Mechanically distinct
from OpenClaw's heartbeat in one specific, verifiable way: **each cron tick creates a fresh
`AIAgent` instance with no history**, injects the job's attached skills as context, runs the
job prompt, and delivers the response — a **stateless-per-run** design, in contrast to
OpenClaw's heartbeat running inside the shared main session with history by default.

**A documented marketing/reality gap, worth flagging explicitly per the task's skepticism
instruction:** several aggregate secondary sources describe Hermes as shipping "a
first-class agent heartbeat primitive: a recurring scheduled wake-up that starts a fresh
agent run with configured context, skills, toolsets, state checks, and guardrails" — language
that reads as describing a heartbeat mechanism distinct from cron, OpenClaw-style. But
**GitHub issue #NousResearch/hermes-agent#15400**, "Feature: First-class agent heartbeat
jobs for supervised long-running projects," opened **2026-04-24**, was **closed as "not
planned"** with no maintainer explanation recorded in the thread. The issue's own text
frames heartbeat as a *desired-but-unbuilt* capability: *"They want an agent to periodically
re-evaluate the world and make conservative decisions"* — i.e., exactly the OpenClaw-style
main-session periodic check-in, requested and explicitly declined. **The verifiable, shipped
reality is: Hermes' wake model is cron-only.** A distinct heartbeat primitive was requested
and rejected. Treat any secondary-source description of Hermes "heartbeat" as either
describing cron loosely, or as inaccurate — this is a concrete case of aggregate blog
content overstating a shipped capability relative to the project's own issue tracker, not a
vendor-marketing-vs-independent-blog gap but an aggregate-blog-vs-primary-source one.

**Multi-agent:** subagent delegation via `delegate_tool.py`; a single `AIAgent` class serves
CLI, gateway, ACP, batch, and API-server entry points — one core loop, many surfaces, which
reads as an architecturally cleaner design than OpenClaw's larger, more fragmented codebase
(the existing memory dossier's §4 already documents HN sentiment describing OpenClaw as
"vibe coded" with "hundreds of thousands of lines" and a backlog of stale PRs — not
re-litigated here, but the daemon-layer design comparison is consistent with that broader
engineering-discipline gap).

### Cross-subject comparison
Both OpenClaw and Hermes are posture 2 (own the whole loop, brand it around always-on
presence) — not wrappers over anything. Both require an always-on host (a VPS, in practice)
for their scheduling primitives to mean anything; both explicitly say so in their own docs.
Where they differ concretely: OpenClaw ships *two* primitives (heartbeat + cron) with
different session/history semantics; Hermes ships *one* (cron only, stateless-per-run,
explicitly declining to add a second). OpenClaw's heartbeat lives inside the trust boundary
of the main session (and is consequently a documented injection-persistence vector); Hermes'
cron jobs are stateless and isolated by construction, which is a smaller attack surface for
this specific mechanism even though Hermes has its own, differently-shaped memory/skill-
persistence security concerns (documented in the existing memory dossier).

---

## 6. Class-level synthesis

### Is "meta-harness" a real distinct layer, or marketing on top of harness+evals?

**Split verdict — say so plainly rather than forcing a clean answer.**

Evidence the mechanism is real: three independent groups converged on a genuinely novel
outer-loop pattern — search/optimize over a harness (or harness-generating spec) using
**raw execution traces**, not compressed scores, as feedback — within roughly a twelve-month
window. Databricks' TAO+ALHF+MLflow-judge pipeline (2025→2026); AWS AgentCore's
Evaluations (GA 2026-03) and Optimization capabilities (2026-06), explicitly framed as
turning "production traces into continuous improvement"; and the academic **"Meta-Harness:
End-to-End Optimization of Model Harnesses"** paper (arXiv:2603.28052, Stanford/MIT/KRAFTON,
2026-03) — an agentic proposer (Claude Code) that inspects raw prior-candidate source code,
traces, and scores via terminal tools (grep, cat) rather than ingesting summaries, running
~60 harness candidates over 20 iterations and up to 10 million diagnostic tokens per
evaluation. That paper is the most rigorous, narrowly-scoped, non-marketing definition of
"meta-harness" found in this entire research pass, and it explicitly does **not** schedule
or host agents — it optimizes harness *code*, a genuinely different mechanism from anything
else in this dossier.

Evidence the label is doing more marketing work than technical work: **Databricks itself
uses "meta-harness" for two mechanically unrelated products released the same month** —
Agent Bricks/TAO (search over prompts/models/chunking/fine-tuning to hit a quality target)
and Omnigent (composition/policy/collaboration across already-running instances of other
harnesses). When one vendor applies the same term to two different mechanisms within weeks
of each other, the term is not tracking a stable architectural boundary. Compounding this:
every vendor surveyed converges on nearly identical "the loop is 1% of the work, the other
99% is deployment/eval/security/monitoring" positioning language, but each implements that
"99%" as a differently-shaped, non-interoperable bundle (Databricks: TAO/ALHF under one
brand plus a separate Omnigent; AWS: ~12 separately-metered micro-products; Azure: a
two-tier Prompt/Hosted split with comparatively thin ops; Vertex: an ADK+Studio+
Runtime+Memory-Bank bundle). Agreement that *some* such layer should exist is not evidence of
a settled *shape* for that layer. And independent, non-vendor corroboration of adoption is
thin across the board: Agent Bricks' headline numbers (100k+ agents, 1+ quadrillion
tokens/year) are entirely self-reported; Omnigent has essentially no sentiment record yet
(about five weeks old at this writing).

**Conclusion for the engine:** trust the *mechanism* — an outer loop that evaluates/optimizes
a harness (or harness-spec) using raw traces rather than compressed summaries is real,
convergently evidenced, and worth learning from. Do **not** trust "meta-harness" or
"agent-OS" as a stable *label* that implies a fixed feature set — this survey found the term
applied to at least three mechanically different things (TAO-style search-and-optimize;
Omnigent-style multi-harness composition/policy/collaboration; AIOS-style kernel scheduling)
inside a single research pass, including two of them from the same vendor in the same month.

### Three postures, not one — the corrective finding on the class hypothesis

Restating the finding from the top of this dossier because it is the central empirical
correction to the task's framing: the hypothesis ("these systems wrap and RUN agents from
the outside") holds for **posture 1** subjects (Agent Bricks Custom-Code mode, AWS AgentCore
Runtime, Azure Hosted Agents) but is **actively wrong** for **posture 2** subjects (Letta's
base runtime, OpenClaw, Hermes, AIOS's Cerebrum-on-kernel) — these are not wrappers, they
*are* the loop the model runs in, competing with rather than sitting outside other harnesses.
**Posture 3** (Agent Bricks Declarative mode, Azure Prompt Agents) is a third thing again —
the platform owns the loop end-to-end, but there is no harness object being wrapped because
none is ever exposed to the customer. Any future reference to "the meta-harness class" in
this engine's work should specify which posture is meant; treating all of §1–5 as one
uniform "wraps agents from outside" pattern would be a factual error this research
specifically surfaced and corrected.

### What the agent-OS claim consistently includes, vs. what nobody ships

**Consistently included — the actual invariant core, present in some form across nearly
every subject:**
1. **Persistence** — state that outlives a single request/session, addressable by ID,
   stored server-side or on-disk. Universal across this survey.
2. **Memory tiering** — a small, fast, always-loaded tier plus a larger searchable/archival
   tier. Convergent across Letta (core/recall/archival), OpenClaw (`MEMORY.md` + SQLite
   index), Hermes (`MEMORY.md`/`USER.md` + `state.db` FTS5), AIOS (RAM + LRU-K eviction to
   storage), and the cloud platforms (session state vs. Memory Bank/Knowledge & Memory
   Store).
3. **Some access/tool gating** — every subject has *some* control over what an agent can
   call or touch (AIOS's Access Manager, AWS Identity, Azure governance, OpenClaw's Sandbox
   permissions, Hermes' skill-write guards).

**Inconsistently included — where "OS" claims most often overreach the evidence:**
1. **A real, OS-style scheduler.** Only **AIOS** ships anything resembling actual CPU
   scheduling (FIFO/Round-Robin, preemptive mid-token snapshot/restore across concurrent
   agent calls). Everyone else's "scheduling" is either a simple cron/interval trigger
   (Hermes, OpenClaw's cron primitive) or genuinely absent (Letta's base platform,
   Databricks, all three cloud platforms — these are request/response services with
   autoscaling, not autonomously-scheduled processes). **The correlation across this entire
   dossier runs backward from what "OS" branding would suggest: the artifact with the most
   literal OS-style scheduler (AIOS, 6.1k stars, no named customers) has the smallest
   footprint of anything surveyed, and the artifacts with the largest footprints (Agent
   Bricks: 100k+ agents; the three hyperscaler platforms) have no scheduler in the
   CPU-scheduling sense at all.** This is worth stating as a named pattern, not just an
   observation: OS-ness and adoption are inversely correlated in this survey.
2. **Native multi-agent orchestration primitives** (not just "call another agent as a
   tool"). Genuinely shipped, with real primitives (tagged workers, supervisor routing,
   shared memory blocks), by Letta and — per usage share — heavily used in Agent Bricks
   (37% Supervisor Agent). OpenClaw has it but strictly flat (no recursive delegation).
   Hermes has basic delegation. AIOS provides the scheduling substrate other frameworks'
   multi-agent logic runs *on*, rather than orchestration primitives of its own.
3. **The auto-eval/auto-optimize outer loop** (the "meta-harness" mechanism proper, in the
   narrow academic-paper sense). Shipped only by the enterprise-cloud class (Databricks
   TAO/ALHF, AWS Evaluations/Optimization). Letta's "sleep-time compute" and OpenClaw's
   "Dreaming" and Hermes' rumored curator-cron are memory-*consolidation* processes, not
   task-performance optimization — they share only the "runs while idle" shape with the
   enterprise mechanism, not its function.

**What nobody ships, full stop:** no subject in this survey unifies (a) OS-grade concurrent
scheduling, (b) auto-eval/auto-optimization, (c) native multi-agent orchestration, and
(d) an always-on autonomous wake/daemon model, in one product with broad independent
adoption evidence. Every subject trades off at least one axis, and the closest attempts at
combining more of them (Omnigent — five weeks old, no sentiment record; AIOS — the most
architecturally complete, the least adopted) are precisely the two least production-proven
entries in this entire dossier. That is the honest empirical shape of "is agent-OS real":
the individual pieces are real, convergently evidenced, and separately shippable; nobody has
assembled all of them with the market to prove it out yet.

### Implications for an engine whose north star is "agentic OS on a markdown+git kernel"

**Worth copying:**

- **Git-backed, markdown-projected memory with per-agent-worktree concurrency is now
  validated by two independent, unrelated lineages, not one.** The existing B-survey
  dossier already established this for OpenClaw (file-first canonical memory, SQLite as
  accelerator not store-of-record). This dossier adds a second, mechanically similar but
  organizationally unrelated convergence: Letta's 2026 Context Repositories (MemFS) —
  git-backed markdown files, isolated worktrees per concurrent subagent, merge-via-git-
  conflict-resolution. A VC-funded enterprise memory-platform company and a solo-founder
  personal-assistant fork reached the same architectural conclusion independently. Per this
  engine's own bar for treating a pattern as evidence-backed (recurrence, not
  elegance-alone), two independent arrivals at "git worktree per concurrent writer, markdown
  as the projection" is real, usable corroboration for the engine's existing markdown+git
  kernel bet — worth citing explicitly in the E1 spec as external validation, not just an
  analogy.
- **Prefer raw traces over compressed summaries when reasoning about what changed.** The
  Meta-Harness paper's core methodological finding — that compressed scalar
  feedback/summaries are insufficient to diagnose long-horizon failures where early choices
  affect behavior many steps later, and that raw log inspection (grep/cat over actual
  execution traces) works where summarization doesn't — is a direct, evidence-backed
  argument for a practice this engine already follows: reading `PROGRESS.md`/`HISTORY.md`/
  git diffs directly rather than working from compressed status reports. Worth citing as
  external validation, not adopted as new practice.
- **Azure's explicit Prompt-Agent-vs-Hosted-Agent boundary is a useful vocabulary to borrow
  for E4's harness epic**, independent of whether Azure's product itself is worth using: for
  every engine skill/agent, name explicitly which posture it is — does the engine own this
  loop end-to-end (à la Prompt Agents), or does it wrap/host something whose loop logic
  lives elsewhere (à la Hosted Agents)? This engine is currently uniformly "owns the loop"
  (skills run inside Claude Code; the harness *is* Claude Code) — worth stating that as a
  deliberate, examined choice in the E4 epic rather than an unexamined default, especially
  since it's consistent with the already-ruled harness-native/no-second-runtime finding from
  the Hermes memory dossier.
- **Hermes' "fail loud, not silent" overflow handling** (a write exceeding the memory cap
  returns an error requiring explicit consolidation, not a silent truncation) is reconfirmed
  here as consistent with the better-designed half of this whole survey — already flagged in
  the B-survey Hermes dossier; this pass found nothing to weaken it and one more data point
  (Databricks' bootstrap-file-budget "soft degrade" in OpenClaw, the opposite pattern) to
  contrast it against.

**Worth avoiding — claims not to repeat:**

- **Do not adopt "OS" as a literal architecture target** (CPU-style scheduling, preemption,
  resource isolation across concurrent agent calls). This survey's own evidence argues
  against it directly: the one subject that built a literal OS-style scheduler (AIOS) has
  the thinnest footprint of anything surveyed, and this engine's actual operating mode
  (human-gated, single-operator, request-driven — Nick opens a session, work happens, session
  closes) has no concrete, recurring need for concurrent-call scheduling. Building one now
  would be exactly the abstraction-without-recurring-concrete-problem this engine's own
  governance rule against speculative infrastructure already warns off.
- **Do not let "meta-harness"/"agent-OS" branding imply a fixed, load-bearing feature
  checklist.** This dossier found the term applied to at least three mechanically different
  things — including two from the same vendor in the same month. If this engine ever
  describes a component using "meta-harness" or "agent-OS" positioning language, it should
  immediately specify which mechanism is meant (outer-loop optimizer? multi-harness
  composition layer? kernel scheduler? persistence service?) — the label alone would
  communicate almost nothing verifiable to a future reader, exactly as it currently doesn't
  across the vendor landscape.
- **Do not copy the enterprise class's per-component metered-billing decomposition** (AWS's
  ~12 billing components; Databricks' per-Answer/per-judge-token stacking) as an
  architectural template for how to split responsibilities. That fragmentation is a vendor
  monetization artifact, and the practitioner complaints found in this research (opaque cost
  structure, "surface sprawl") are a direct, named consequence of it. This engine has no
  billing surface, so the risk is indirect — but if the E4 harness epic ever specs out
  sub-agent-as-a-service boundaries, "many small separately-metered services" should not be
  mistaken for "well-factored separation of concerns."
- **Do not adopt "auto-generate a benchmark and grade yourself against it" as a
  self-improvement mechanism without a pre-write human gate.** TAO/ALHF explicitly optimize
  against LLM-judge-graded synthetic benchmarks with only a *lagging* human-correction path
  (ALHF is post-hoc natural-language feedback, applied after deployment, not a pre-commit
  gate). This is the same shape of risk the existing Hermes memory dossier already flagged
  for autonomous self-rewriting (self-graded self-improvement drifts without a pre-commit
  human gate — the most consistently corroborated failure mode in that entire dossier). This
  engine's per-proposal Nick gate (IB-176) is strictly ahead of anything shipped anywhere in
  this survey on this specific axis, including the best-funded enterprise products — that is
  evidence the current discipline is correctly calibrated, not overcautious, and a reason to
  resist ever loosening it toward "trusted autonomous optimization" even for a narrowly-scoped
  component.
- **Be skeptical of vendor-only adoption numbers by default.** Nearly every headline
  adoption figure in this dossier (Agent Bricks' 100k+ agents and 1+ quadrillion
  tokens/year; most of the named-customer lists; Omnigent's entire positioning) is
  vendor-self-reported with no independent corroboration found in this research pass. Where
  this dossier could find independent practitioner sentiment (OpenClaw's HN trail, Hermes'
  GitHub issues, Databricks' one SunnyData review), it was noticeably more mixed and more
  specific than the vendor framing — treat that pattern as the expected baseline, not the
  exception, when this class of claim shows up again in future research.
