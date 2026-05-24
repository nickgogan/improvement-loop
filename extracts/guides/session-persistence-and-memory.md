---
title: "Session Persistence and Memory"
type: "guideline"
category: "Context Engineering"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-19"
updated: "2026-04-26"
author: "claude"
source_findings:
  - "session-persistence-crash-resilient"
  - "workflow-state-vs-conversation-state"
  - "incremental-one-feature-per-session-pattern"
  - "ground-truth-environmental-feedback-loops"
  - "effort-scaling-rules-embedded-in-orchestrator"
  - "file-based-task-locking-parallel-agents"
  - "scalpel-local-parse-then-llm-cost-optimization"
  - "biomimetic-memory-auto-recall-over-tool-based"
  - "claude-code-long-term-memory-via-pre-prompt-recall"
  - "four-tier-agent-memory-model-with-write-policy"
  - "dual-ingestion-funnel-human-clip-plus-llm-research"
  - "four-layer-enterprise-memory-stack"
  - "structured-fact-extraction-from-conversations"
  - "memory-cross-layer-promotion-governance"
  - "ace-agentic-context-engineering-rag-based"
  - "memorymd-cross-session-preference-persistence"
  - "concept-graph-support-contradiction-detection"
  - "memory-bank-isolation-per-agent-per-project"
  - "mongodb-single-store-polymorphic-evidence-memory"
  - "open-brain-personal-knowledge-store-pattern"
  - "org-world-model-three-architecture-patterns"
  - "post-retrieval-reranking-weighted-signal-composition"
  - "query-decomposition-sub-query-rrf-merge"
  - "rank-fusion-hybrid-retrieval-mongodb-atlas"
  - "signal-capture-as-byproduct-of-work"
  - "subagent-persistent-memory-directory"
  - "surprisal-novelty-as-memory-write-gate"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "memory"
  - "session-persistence"
  - "retrieval"
contract:
  preconditions: "You have an agent system that persists beyond a single prompt-response cycle. You can write to a filesystem or database. You understand the difference between what was said (conversation) and what was done (workflow state)."
  invariants: "Memory is layered with explicit tiers, not a flat persistence target. Workflow state is tracked separately from conversation state. Sessions leave the system in a clean, resumable state. Memory writes are policy-governed and novelty-gated -- agents do not freely append to long-term stores. Memory banks are scoped (per-agent, per-project, per-session) with cross-bank queries opt-in. Environmental feedback, not self-assessment, drives decisions. Retrieval pipelines are debuggable -- ranked outputs decompose into inspectable signals."
  governance: "Memory tier boundaries, promotion policies, retention rules, and isolation scopes are documented per system. Session boundary conventions are enforced by handoff prompts. Retrieval recipe (decomposition, fusion, reranking) is versioned as a contract. This guide is owned by Meta-System knowledge layer."
  recovery: "If an agent crashes mid-task: load the last persisted workflow checkpoint and resume from the last completed step. If session handoff loses context: read the progress file and last handoff prompt. If memory is corrupted: fall back to the last known-good tier and reconstruct. If parallel agents conflict: check the lock directory for abandoned locks. If retrieval quality degrades: decompose the rerank score into per-signal contributions to identify the failing stage. If memory is poisoned by bad writes: roll back to a known-good corpus snapshot, re-run the novelty + contradiction filters, audit promotion logs."
---

# Session Persistence and Memory

How to build agent memory that survives crashes, scales across sessions, and does not pollute itself. This guide covers six concerns that look separate but are deeply coupled: what to remember, how to retrieve it, where to store it, how to recover from failure, how to govern writes, and how to ingest new signal at scale.

## When to Use This Guide

- Your agent sessions run long enough that a crash would lose non-trivial work (>10 minutes)
- You need cross-session continuity where agents build on prior sessions' knowledge
- You are designing a memory architecture with multiple storage layers
- You are evaluating retrieval architectures (vector / hybrid / RAG-based playbook) and need a decision framework
- You need to coordinate parallel agents on shared state
- You want to control what agents write to persistent memory and at what quality bar
- You are choosing between single-store and multi-store memory backends
- You need to scope and isolate memory across agents, projects, or sessions

## Key Concepts

**1. Memory is a four-tier system, not a flat store.** Working memory (current context window), episodic memory (task history with provenance), semantic memory (knowledge graph of entities and policies), and governance memory (append-only audit log). Each tier has distinct read/write policies, retention targets, and ownership. Long context is not memory. A vector store is not automatically memory either. Memory is a deliberate read/write policy system.

**2. Conversation state is not workflow state.** "What was said" (chat transcript) is fundamentally different from "what step am I on and what side effects have occurred" (workflow state machine). Without separation, retrying after a crash re-executes side effects. Workflow state makes operations idempotent and retry-safe. Conversation state is supplementary context, never the source of truth for progress.

**3. Persist after events, not on shutdown.** Crashes happen during execution, not during graceful shutdown. Persist full session state after every significant event -- step completion, tool execution, permission grant, commit. The load/reconstruct/restore pattern enables deterministic recovery from any checkpoint.

**4. Auto-recall beats tool-based memory.** Giving an agent a "search memory" tool fails because the agent must realize it needs information it does not have. Injecting relevant memories into context automatically before every prompt removes this meta-cognitive requirement. The tradeoff is token cost, bounded by a recall budget (default ~1024 tokens).

**5. Memory writes require policy gates AND novelty gates.** Unrestricted agent writes to long-term memory produce compounding pollution -- future retrievals return noisy data, which produces worse outputs, which get persisted again. Every write must follow: extract candidate, classify type, check policy, check novelty, check for contradictions, attach provenance, write with TTL and confidence score.

**6. One feature per session, clean state at exit.** Each session implements exactly one focused objective and leaves the system in a production-mergeable state. Context resets fully between sessions. The progress file carries forward what matters; conversation history does not.

**7. Ground truth beats self-assessment.** Agents should obtain concrete environmental feedback (test results, tool outputs, API responses) at each decision point. Self-assessment is unreliable because the same model that made the mistake evaluates whether a mistake was made.

**8. Memory architectures are not interchangeable.** Vector DB, structured ontology, signal-fidelity, and single-store-polymorphic each have a characteristic failure mode rooted in how they mishandle the information/judgment boundary. Choose by org scale, signal type, and judgment density -- not by deployment speed.

---

## Part 1: Design Your Memory Architecture

Before implementing persistence, retrieval, or write governance, decide what your agent needs to remember, where each type of memory lives, how the storage substrates compose, and how memory is scoped across agents and projects.

### Step 1.1: Map the Four Tiers

Every agent memory system has four tiers, whether you design them explicitly or let them emerge accidentally. Design them explicitly.

| Tier | What It Stores | Lifespan | Read Policy | Write Policy |
|------|---------------|----------|-------------|-------------|
| **Working** | Current context, active plan, last 6-10 exchanges | Minutes/hours | Always loaded | Compacted aggressively |
| **Episodic** | Task history with provenance (who, what, when, why) | Months (with pruning) | Retrieved by semantic similarity | Append with evidence pointers |
| **Semantic** | Entities, relationships, constraints, policies | Years (curated) | Retrieved by structured query | Policy-gated, schema-owned |
| **Governance** | Audit log of every prompt, retrieval, action, output | Retention by policy | Not in hot path | Append-only, immutable |

The critical insight: most agent memory failures happen at **tier boundaries**, not within a single tier. Over-promotion of noisy events pollutes durable memory. Under-promotion causes repeated misses and wasted context.

### Step 1.2: Choose Your Storage Topology — Single-Store vs. Multi-Store

The four tiers are a logical model. The physical substrate is a separate decision with two dominant patterns:

| Pattern | Description | Strengths | Weaknesses |
|---------|------------|-----------|------------|
| **Multi-store split** | Vector store for similarity, graph store for relationships, relational store for metadata, append-only log for governance. Each tier on its specialized substrate (mem0, Letta, Zep, layered enterprise stacks). | Per-tier optimization; per-substrate ops expertise; graceful degradation (one outage doesn't take down all tiers). | Cross-store consistency is hard. Provider lock-in per substrate. Higher ops cost. |
| **Single-store polymorphic** | One database with `oneOf` schema validation holding all evidence types -- conversation turns, session evidence, user facts, QA pairs (Memongo on MongoDB Atlas). | One backup, one query plane, one consistency boundary. Hybrid retrieval primitives (`$rankFusion`, `$scoreFusion`) inside the database. Lower ops cost. | Per-type index contention. Schema migrations affect all types. Single point of failure. |

**Decision criteria:**

- **Choose multi-store when:** relationship traversal is a dominant query mode; you have per-store ops expertise; regulatory boundaries require physical separation between memory types; or the cost of one tier's outage cascading is unacceptable.
- **Choose single-store when:** operational simplicity matters more than per-type optimization; your retrieval workload is well-served by hybrid primitives in a single substrate; you want one consistency boundary across evidence types.
- **Choose flat-file markdown (no DB) when:** deployment simplicity and transparency outweigh scale needs (CLAUDE.md, MEMORY.md, PARA-style vaults). Best for solo developers and early-stage systems where the corpus stays small enough to read.

The flat-file path is not a strawman. For systems where the working corpus stays under a few thousand entries and human inspection is part of the workflow, a markdown vault outperforms a database on debuggability and portability. Migrate to a DB when scale forces it, not before.

### Step 1.3: Define Promotion and Demotion Policies

Every movement of data between tiers must be governed:

**Promotion (upward movement):**
- Working to Episodic: Append events from the current session with evidence pointers and temporal context
- Episodic to Semantic: Distill episodes into durable facts -- this is the highest-risk transition. Gate by explicit policy: only promote when knowledge "truly changed"
- Semantic updates: Schema ownership validation. Not every agent can write to shared semantic memory

**Demotion (pruning/compaction):**
- Working memory: strict token budget + compaction after each session
- Episodic memory: importance/recency scoring for garbage collection
- Semantic memory: small by design, curated, rarely pruned
- Governance memory: never pruned without policy authorization

**Governance questions to answer before building:**
1. Who owns the promotion policy for each tier boundary?
2. Who can override memory pruning?
3. What constitutes a rollback trigger?
4. How quickly can the team reconstruct a corrupted memory state?

### Step 1.4: Scope and Isolate Memory Banks

A memory system that works for one agent becomes a liability when shared across agents, projects, or users. A Telegram bot agent and a coding agent sharing a memory bank pollute each other's recall. Isolation must be a first-class primitive.

**Isolation primitives:**

| Primitive | Granularity | Use Case |
|-----------|-------------|----------|
| `bankId` | Per-agent / per-project | Separate memories for Project A vs. Project B; for Researcher agent vs. Codifier agent |
| `bankMission` | Per-bank | Tells the memory engine who this agent is, improving fact-extraction relevance |
| `retainMission` | Per-bank | Guides what the engine should remember from conversations |
| Channel/User ID scoping | Per-conversation | Isolates memories per messaging channel or per user in multi-user scenarios |

**Subagent-scoped memory directories** (Claude Code pattern): each subagent gets a filesystem directory (`~/.claude/agent-memory/{name}/` for `user` scope; `.claude/agent-memory/{name}/` for `project` scope; `.claude/agent-memory-local/{name}/` for `local` scope). The first 200 lines or 25KB of `MEMORY.md` is auto-loaded into the subagent's system prompt on each invocation. The subagent is instructed to curate the file when it exceeds the budget, forcing compression rather than unbounded append.

| Scope | Directory | Use |
|---|---|---|
| `user` | `~/.claude/agent-memory/{name}/` | Learnings across all projects |
| `project` | `.claude/agent-memory/{name}/` | Project-specific; shareable via VCS |
| `local` | `.claude/agent-memory-local/{name}/` | Project-specific; not checked in |

**Cross-bank queries should be opt-in, not default.** Allow explicit cross-bank search when an agent detects a cross-project dependency, but isolate by default. Over-isolation creates knowledge silos -- the boundaries should match the actual knowledge boundaries, not just the organizational ones.

### Step 1.5: Match Architecture to Org Scale

For team or organizational memory (not just per-agent), three architectural patterns dominate, each with a characteristic failure mode:

| Architecture | How It Works | Characteristic Failure |
|-------------|-------------|----------------------|
| **Vector DB (semantic retrieval)** | Embed everything, retrieve by similarity. Fast deploy; adequate for status synthesis, dependency detection, report generation. | Never draws the information/judgment boundary. Semantic ranking is itself an interpretation but nothing in the architecture flags it as such. Breaks at ~10K documents or when users can no longer apply independent judgment to system output. |
| **Structured ontology (schema-bounded)** | Explicitly defined domain objects, relationships, actions. AI reasons within a bounded schema; cannot hallucinate structure. | Draws the boundary too conservatively. Handles known relationships precisely; blind to emergent ones. Breaks on novel business conditions outside the schema. |
| **Signal fidelity (high-quality data exhaust)** | Build the model around the highest-fidelity signal the business generates (e.g., transactions). Model improves as a byproduct of doing business. | Assumes the signal interprets itself. High input fidelity creates an illusion of high judgment quality at the output. Breaks on causal inference requiring context the signal doesn't carry. |

**Sizing guidance:**

| Org type | Recommended start |
|---|---|
| <100 people, strong senior team | Vector DB — senior judgment compensates for ranking failures |
| Enterprise / regulated | Structured ontology — high upfront cost, captures surprises |
| Platform business with clean signal (transactions) | Signal fidelity — but invest heavily in interpretive boundary labeling |
| Knowledge-work company (docs + conversations) | Vector DB first, but plan migration to structured before 10K documents |

**These architectures are not interchangeable.** Teams that treat them as such copy the architecture without understanding which failure mode they import. Architectural choice determines which risks become systemic and invisible vs. loud and diagnosable.

---

## Part 2: Build the Retrieval Pipeline

If memory is more than a flat file, retrieval is the hot path. A good retrieval pipeline turns a single user query into the right memories in context. A bad one returns plausible-but-wrong matches that the agent then trusts.

### Step 2.1: Choose Auto-Recall over Tool-Based

Two architectures for memory retrieval, with different failure modes:

| Strategy | How It Works | Failure Mode |
|----------|-------------|-------------|
| **Tool-based** | Agent has a `search_memory` tool it must choose to call | Agent does not realize it needs information it lacks -- silent miss |
| **Auto-recall** | System injects relevant memories into context before every prompt | Token cost on every turn, even when memories are irrelevant |

**Prefer auto-recall.** Tool-based memory fails at exactly the moment it is most needed: when the agent does not know what it does not know. Auto-recall makes memory a system-level concern, not an agent-level decision.

Tuning knobs for auto-recall:
- `recallMaxTokens`: bounds the token cost per turn (default ~1024)
- `recallBudget`: low/mid/high controls retrieval breadth
- Adaptive recall: start low, increase if the agent re-asks previously answered questions or contradicts past decisions

### Step 2.2: Hybrid Retrieval — Semantic + Lexical Fusion

Pure semantic retrieval misses exact-match queries. Pure lexical retrieval misses paraphrased ones. Production retrieval combines both, ideally inside the database to avoid cross-system consistency problems.

**Pattern: Native rank fusion in the database.** MongoDB Atlas's `$rankFusion` and `$scoreFusion` aggregation stages combine `$vectorSearch` (embedding-based) with Atlas `$search` (BM25-style full-text) into a single ranked result set. Both indexes sit on the same documents; the query planner co-optimizes.

| Source | Implementation |
|--------|---------------|
| Semantic | `$vectorSearch` with auto-embed (e.g., Voyage 4 Large) |
| Lexical | Atlas `$search` (BM25-style full-text) |
| Fusion | `$rankFusion` (RRF over both) or `$scoreFusion` (weighted score combination) |

**Benchmark discipline.** When evaluating retrieval recipe quality, run vector search with `exact:true` to disable ANN approximation. This isolates the recipe from index-tuning artifacts and produces a ceiling measurement. Production deploys can switch back to approximate search for latency.

**When to choose alternatives:**
- **Dual-index + application-side RRF:** if you're not on a database with native fusion, or you need custom fusion formulas.
- **Dedicated search service** (Vespa, Weaviate): when document-DB features aren't useful elsewhere in the stack.
- **Single-source vector retrieval:** only when queries are always conceptual and exact-match failures are acceptable.

### Step 2.3: Query Decomposition + RRF Merge

A single user query often compresses several distinct retrieval needs. *"What was the thing Nick mentioned about Atlas Search during the last Memongo session, and did we ever ship that fix?"* contains a temporal constraint, an entity constraint, a topic constraint, and a status constraint. A single embedding of the full sentence blurs all four.

**Pattern:**
1. **Decompose.** A small/cheap LLM (e.g., GPT-4-mini) rewrites the user query into multiple sub-queries, each targeting one concern.
2. **Parallel retrieve.** Each sub-query runs against the retrieval index independently (vector + lexical, fanned out).
3. **RRF merge.** Reciprocal rank fusion combines the ranked lists. RRF is robust to cross-sub-query score incomparability because it merges ranks, not scores.
4. **Downstream rerank.** Apply post-retrieval reranking (Step 2.4) on the merged set.

**Economics:** Decomposition with a small model is cheap relative to the retrieval it steers. The retrieval-quality gain typically outweighs the extra LLM latency.

**Tradeoffs:**
- Over-decomposition dilutes precision (too many marginal matches; RRF cannot compensate for noise at the input).
- Decomposer-model drift on upgrade silently shifts retrieval behavior. Treat the decomposition prompt as a versioned contract.
- Latency floor is set by the decomposition call.

### Step 2.4: Post-Retrieval Reranking with Inspectable Weights

After fusion, apply a final rerank to push the most-relevant results to the top. Two camps:

| Camp | Example | Strength | Weakness |
|------|---------|----------|----------|
| **Learned reranker** | ColBERT, Cohere Rerank, Anthropic contextual retrieval | Strong scores | Opaque — "the reranker thought this was more relevant" is not actionable debugging |
| **Weighted signal composition** | Sum of human-tuned weights over orthogonal signals | Inspectable, tuneable, no training loop | Requires manual tuning; misses signals not in the basis |

**Pattern: Weighted signal composition.** Memongo's reranker uses four signals with constant coefficients:

| Signal | Weight | What it measures |
|--------|--------|------------------|
| Quoted phrase match | 0.60 | Exact-phrase presence from the query |
| Temporal proximity | 0.40 | Recency relative to query-time |
| Entity name match | 0.40 | Named-entity agreement with query |
| Keyword overlap | 0.30 | Lexical token overlap |

The weights communicate design intent: literal matches dominate, temporal and entity tied, lexical lowest (because semantic search already handles loose token overlap).

**Properties learned rerankers don't give you:**
1. **Inspectability** — for any result, decompose its score into contributing signals.
2. **Tuneability** — weights are ops-editable; no retraining when the embedding model changes.
3. **No training loop** — no labeled data, no model artifact.

**When to choose a learned reranker instead:** when labeled preference data exists and absolute top-1 precision matters more than debuggability. Otherwise, weighted signals are the better default.

### Step 2.5: RAG-Based Behavioral Playbook (ACE Pattern)

For domains where the agent's *behavioral rules* (not just its facts) need to evolve over time, the ACE (Agentic Context Engineering) pattern replaces a monolithic CLAUDE.md with a vector database of if/then behavioral "bullets," retrieved per task and curated by a generator/reflector/curator agent loop.

**Three components:**
1. **Generator** — semantically retrieves the top-k most relevant behavioral bullets and executes the task with those bullets in context.
2. **Reflector** — analyzes the execution trace and extracts new if/then lesson candidates, optionally self-refining over multiple passes.
3. **Curator** — embeds new bullets, deduplicates against existing ones, updates helpful/harmful vote counts per bullet, removes bullets that accumulate enough negative votes.

**Why it matters:** ACE solves the two failure modes of naive monolithic context files. (1) Context rot: only relevant rules are retrieved per task, not all rules always. (2) Catastrophic collapse: granular vote-weighted upserts replace whole-file rewrites.

**Best suited to domains with binary success signals** (tests pass/fail, API calls succeed/error). Harder to use in subjective domains without an external judge. Combine with TDD where test pass/fail provides the binary success signal for the reflector to make this fully automated.

**Failure modes:**
- **Bullet poisoning:** if the Reflector misdiagnoses a failure cause, bad advice enters the DB and future tasks retrieve it. Requires periodic curation passes.
- **Conflict with hand-maintained CLAUDE.md:** a hard-coded rule conflicting with a retrieved bullet causes context clash. Pick one source of behavioral truth or design explicit precedence.

### Step 2.6: Mid-Tier Personal Knowledge Stores

Between flat-file `MEMORY.md` and full RAG infrastructure sits a third option: a lightweight, MCP-accessible personal knowledge store (~10 cents/month) that any MCP-speaking agent can query. The "Open Brain" pattern.

**Characteristics:**
- **Cost:** ~10 cents/month (lightweight database)
- **Interface:** MCP-accessible — bridges across agent systems
- **Content:** structured output from expertise-elicitation interviews + accumulating insights over time
- **Durability:** persistent, searchable, multi-dimensional

**Use case:** A multi-agent setup where context accumulated in one agent (e.g., a personal assistant) must be retrievable by another (e.g., a coding agent). The MCP bridge makes the store a shared context layer rather than an agent-specific one — and at a price point that doesn't require committing to RAG-grade infrastructure.

**Failure modes:** Without active maintenance, the store becomes a static snapshot rather than living memory. If the seed corpus is low-quality, the foundation compounds badly.

---

## Part 3: Implement Session State and Persistence

### Step 3.1: Separate Workflow State from Conversation State

Define explicit workflow states for your agent's task lifecycle:

```
planned --> awaiting_approval --> executing --> waiting_on_external --> completed
    ^                                                    |
    +-- failed (with retry count and last error) <-------+
```

Persist workflow state as structured data (JSON/YAML), not conversation history. Include:

| Field | Purpose |
|-------|---------|
| `current_step` | Which step in the workflow the agent is on |
| `completed_steps` | What has been done, with outcomes and side effects recorded |
| `pending_side_effects` | Side effects queued but not yet executed |
| `retry_count` | How many times the current step has been attempted |
| `last_error` | What went wrong on the last attempt |

This makes operations retry-safe -- on crash recovery, the agent skips completed steps and resumes from the last incomplete one without re-executing side effects.

### Step 3.2: Implement Crash-Resilient Persistence

Persist full session state after every significant event using a two-layer approach:

**Layer 1 -- Structured state (JSON/YAML):** Machine-readable, enables automated recovery.

**Layer 2 -- Narrative state (progress file, changelog):** Human-readable, enables cross-session context.

Git commits after every meaningful work unit serve as both a persistence mechanism and a recoverable history (demonstrated in multi-day autonomous scientific computing sessions).

**Recovery pattern:** load() -> reconstruct() -> restore(). Load the checkpoint file, reconstruct the workflow state from persisted data, restore the agent to the last known good state. If the external world has changed since the checkpoint, detect the drift and surface it to the user before resuming.

### Step 3.3: Extract Structured Facts, Not Raw Transcripts

Instead of storing conversation history as memory, extract discrete structured facts in the background after each agent turn:

| Fact Type | Example | Recall Trigger |
|-----------|---------|---------------|
| Decision | "Adopted fractal pattern for system organization" | Any discussion of system structure |
| Preference | "User prefers JSON responses" | Any formatted output request |
| Constraint | "DD-44 governs supersession lifecycle" | Any proposal to modify a DD |
| Technical context | "kb_parser.py has write_frontmatter()" | Any finding file write operation |

Facts should include: type, text content, timestamp, entities involved, and confidence score. Semantic ranking at recall time (not keyword matching) enables retrieval by relevance rather than recency.

**The compaction problem:** Claude Code's built-in compaction summarizes away critical decisions. Structured facts survive compaction because they live outside the conversation window. This is not a nice-to-have -- it is essential for any system running long enough to trigger compaction.

### Step 3.4: Cross-Session Preference Persistence with `memory.md`

The simplest viable cross-session memory: a plain `memory.md` file the agent reads at session start and writes to whenever the user makes a correction or states a preference. Costs nothing, requires no harness support, and gives users full visibility into what the agent remembers.

**Setup:**
1. Create `memory.md` alongside `CLAUDE.md`.
2. Add a directive to `CLAUDE.md` (or the agent's system prompt): *"Read memory.md on startup. When you learn something new or are corrected, update the relevant section in memory.md immediately. Keep memory.md current."*
3. Optionally pre-section it (`## Preferences`, `## Corrections`, `## Learned Facts`) to improve retrieval accuracy.

**Why it matters:** All major agent harnesses default to no cross-session memory — a fresh session has no knowledge of previous corrections or preferences. Without `memory.md`, users repeat the same corrections endlessly. With it, the agent gets progressively better at the role over time.

**Best practices:**
- Keep `CLAUDE.md` under 200 lines; `memory.md` is the place for accumulated nuance.
- Periodically prune entries older than 90 days that haven't been referenced.
- Verify memory.md contents periodically — false memories (hallucinated entries written without user verification) compound over time.

**Tradeoffs vs. opaque cloud memory:** `memory.md` is fully user-visible and portable; opaque memory systems (OpenClaw auto-memory, Manis built-in, Claude project memory) are easier to set up but the user can't see or audit what's stored.

---

## Part 4: Manage Session Lifecycle

### Step 4.1: Define Session Boundaries

Each session follows a strict lifecycle:

1. **Read** the progress file and git history to understand current state
2. **Select** exactly one focused objective from the task list
3. **Execute** with environmental verification at each decision point
4. **Leave clean state** -- production-mergeable, no major bugs, documentation updated
5. **Update** the progress file for the next session

**Context resets fully between sessions.** The progress file and git history are the sole bridge. Conversation history does not carry forward.

**Ground truth at every decision point:** The agent obtains concrete environmental feedback (test output, lint results, tool responses) rather than self-assessing "I think this is correct." This prevents dead-end strategies and grounds decisions in observable reality.

### Step 4.2: Scale Effort to Task Complexity

Embed explicit resource allocation rules in orchestrator prompts so agents do not overinvest in simple tasks or underinvest in complex ones:

| Tier | Query Type | Subagents | Tool Calls | Example |
|------|-----------|-----------|------------|---------|
| 1 | Simple factual | 1 | 3-10 | "What is the current config value?" |
| 2 | Comparison / synthesis | 2-4 | 10-15 | "Compare these 3 approaches" |
| 3 | Complex multi-source research | 10+ | Divided roles | "Survey the landscape and produce a report" |

Token usage explains 80% of performance variance in multi-agent systems. Without scaling rules, orchestrators default to spawning as many subagents as possible regardless of task complexity.

### Step 4.3: Coordinate Parallel Agents

For parallel execution, use filesystem locks -- the simplest viable coordination:

```
shared/
+-- upstream/           # Bare git repo (shared state)
+-- locks/              # Task claim directory
|   +-- parse_if.txt    # Agent A claimed this task
|   +-- parse_for.txt   # Agent B claimed this task
+-- agents/
    +-- agent_a/        # Agent A's workspace (cloned from upstream)
    +-- agent_b/        # Agent B's workspace (cloned from upstream)
```

**Per-agent workflow:**
1. Acquire lock: atomic file creation in `locks/` named after the task
2. Pull and merge from upstream
3. Work on the claimed task
4. Push changes to upstream
5. Remove the lock file

No orchestrator, no inter-agent messaging, no central coordinator. Git history shows lock-taking as a natural audit trail. Scales linearly.

---

## Part 5: Govern Memory Writes

Without governance, memory becomes a compounding liability. Every write must pass through a series of gates: policy authorization, novelty filtering, contradiction detection, and provenance attachment.

### Step 5.1: Policy-Gated Promotion

Every cross-tier movement is governed by an explicit policy:

| Pipeline Step | Question Answered |
|--------------|-------------------|
| 1. Extract | What is the candidate memory? Where did it come from? |
| 2. Classify | Working / episodic / semantic / governance? Or user-scoped vs. agent-scoped? |
| 3. Policy check | Is this agent role authorized to write to this tier? Escalate if not. |
| 4. Provenance | Source, confidence (HIGH/MED/LOW), timestamp, related entities. |
| 5. Write | TTL, confidence score, indexable fields. |

**Policy authorities:**
- *Working tier:* Agent writes freely (it's just context).
- *Episodic tier:* Agent appends with provenance; periodic human/automated audit.
- *Semantic tier:* Human-gated by default; only specific agent roles authorized.
- *Governance tier:* Append-only by system, immutable by agents.

The highest-risk operation is **episodic-to-semantic promotion**. A noisy episode getting promoted to durable knowledge pollutes every future session that retrieves from semantic memory. Define explicit ownership and approval for this boundary.

### Step 5.2: Novelty Filtering at Write Time

Most memory systems treat every turn as writeable, relying on downstream retrieval to surface the relevant subset. That works until the corpus accumulates many near-duplicate entries ("User prefers JSON" written 40 times across sessions), at which point retrieval precision drops and decay can't help — none of the duplicates is old enough to prune.

**Pattern: Surprisal-based novelty gate.** Compute a novelty score for each candidate against the existing corpus (typically embedding similarity + lexical overlap against nearest neighbors). High-novelty: write as a new memory. Low-novelty: merge with the existing match, or drop entirely.

**Why surprisal?** It is the information-theoretic complement to importance. *Importance* asks "does this matter?"; *surprisal* asks "is this new?" A mature memory system needs both. High-importance-but-redundant signals should merge rather than duplicate. High-novelty-but-low-importance signals shouldn't clutter the index.

**Tuning knobs:**
- **Dynamic threshold:** Early in a session or corpus, threshold should be low (everything is novel); late, threshold should rise.
- **Per-evidence-type thresholds:** Facts, QA pairs, and session evidence have different novelty baselines.
- **Audit trail:** Log novelty decisions so humans can audit why a candidate was accepted or rejected.

**Failure modes:**
- Embedding-driven novelty misses fine-grained facts (two memories may be embedding-nearby but semantically distinct: "deploys at 3pm Tuesday" vs. "deploys at 3am Tuesday").
- Cold start: with an empty corpus, everything is novel; the gate provides no filtering early.
- Merge-instead-of-write can hide corrections: if a corrected fact is merged into a stale fact, the correction is lost.

### Step 5.3: Contradiction Detection

Novelty catches redundant agreements. Contradictions are different: "User says A" followed by "User says not-A" is a high-novelty event the gate will admit, but it requires an explicit contradiction-resolution path, not just a write.

**Pattern: Concept graph with support/contradiction edges.** Each new piece of content is processed by the LLM not just to summarize, but to check it against existing concepts and classify whether it **supports** or **contradicts** them. The graph stores:

- **Concepts** (organized by topic clusters)
- **Sources** (with attribution to author, platform, timestamp)
- **Relationships:** support edges and contradiction edges between concepts and sources

Synthesis output gives every signal:
1. A specific **action item** (not just a summary)
2. A **supporting context chain** tracing back to the originating source
3. **Contradiction flags** when conflicting evidence exists

**Why it matters:** Most knowledge systems encode *what happened* but not *how ideas relate*. Encoding the epistemic state — where sources agree, where they conflict — is what lets the system serve as a decision-support layer rather than a reference layer. Particularly valuable in fast-moving fields where contradictory findings emerge weekly.

**Failure modes:**
- **Taxonomy bloat.** Self-organizing taxonomy with no pruning produces hundreds of near-duplicate concepts. Periodic merge/prune is mandatory.
- **Support/contradict false positives.** The LLM may classify a nuanced finding as contradicting a concept when it actually qualifies it. Poisons the reliability of synthesized output.
- **Attribution staleness.** Sources from months ago remain in the graph but their context (what was being debated at the time) may no longer be relevant.

**Pair novelty + contradiction detection.** Surprisal alone admits contradictions as "new" without flagging them. Contradiction detection alone admits redundant agreements as "consistent" without filtering them. Both gates are needed.

---

## Part 6: Design Ingestion Pipelines

### Step 6.1: Establish Dual Ingestion Funnels

Two parallel paths feed the memory system:

| Path | Source | Staging | Quality Gate |
|------|--------|---------|-------------|
| **Human-driven** | Web clipper, manual notes, observations | `raw/` folder for curation | Human review before promotion |
| **LLM-driven** | Autonomous research, structured extraction | Direct to structured format | Automated quality filter + periodic human audit |

The human path captures serendipitous discovery. The LLM path captures structured extraction at volume. Neither should bottleneck the other, but both need deduplication and cross-referencing to avoid contradictory entries on the same topic.

### Step 6.2: Use Local Parsing Before LLM Processing

For document-heavy ingestion, apply the scalpel pattern: local models handle structural decomposition (layout detection, OCR, text extraction) for free, and expensive LLM API calls are reserved for semantic understanding (entity extraction, relationship mapping, summarization). This reduces API costs by an order of magnitude and improves quality because the LLM receives clean, structured input rather than raw pixels.

### Step 6.3: Capture Signal as a Byproduct of Work

Organizational knowledge systems only compound if signal capture is a byproduct of doing the work — not a separate documentation act. When feeding the system requires extra effort, the people with the most valuable context will strategically withhold it, and the system stagnates.

**Two failure modes for active-documentation systems:**
1. **Strategic withholding.** Team members who benefit from information asymmetry will not voluntarily feed a system that erodes that advantage.
2. **Benign forgetfulness.** Even well-intentioned contributors skip documentation under time pressure.

**Design implication:** Tool selection and workflow design must prioritize passive capture — where using the tool to do the work also produces the signal.

| Active capture (avoid as primary) | Passive capture (prefer) |
|----------------------------------|--------------------------|
| Documentation files | Commit messages |
| Status emails | Ticket updates |
| External design docs | Decisions made in the system |
| Post-hoc summaries | Tool invocations + outcomes logged automatically |

**Caveats:**
- Passive capture can produce low-signal noise at high volume if not filtered. Quantity ≠ quality.
- Tool lock-in: optimizing for passive capture in one tool stack makes migration painful.
- Privacy: automatic capture may create compliance issues in regulated industries.
- The model accumulates a skewed picture if only certain types of work are naturally logged (code commits but not architecture discussions). Layer in explicit capture for under-represented signal types.

---

## Templates

### Memory Architecture Specification

```yaml
# Memory Architecture — {{SYSTEM_NAME}}
system: "{{SYSTEM_NAME}}"
created: "{{ISO_8601}}"
owner: "{{OWNER}}"

storage_topology: "{{single-store / multi-store / flat-file}}"
isolation_scope: "{{per-agent / per-project / per-user / shared}}"
org_scale_pattern: "{{vector-db / structured-ontology / signal-fidelity / hybrid}}"

tiers:
  working:
    store: "{{CONTEXT_WINDOW / IN_MEMORY}}"
    retention: "{{SESSION_DURATION}}"
    compaction: "{{AFTER_EACH_SESSION / EVERY_N_TURNS}}"
    max_tokens: {{TOKEN_BUDGET}}

  episodic:
    store: "{{DAILY_LOGS_DIR / DATABASE}}"
    retention: "{{MONTHS_WITH_PRUNING}}"
    write_policy: "append with evidence pointers"
    gc_scoring: "{{IMPORTANCE_WEIGHT}}% importance + {{RECENCY_WEIGHT}}% recency"

  semantic:
    store: "{{WIKI_DIR / KNOWLEDGE_GRAPH}}"
    retention: "years (curated)"
    write_policy: "policy-gated, schema-owned"
    promotion_gate: "{{WHO_APPROVES_EPISODIC_TO_SEMANTIC}}"

  governance:
    store: "{{AUDIT_LOG_DIR}}"
    retention: "append-only, {{RETENTION_POLICY}}"
    write_policy: "immutable append"

recall_strategy: "{{AUTO_RECALL / TOOL_BASED}}"
recall_budget: "{{recallMaxTokens}}"
retain_cadence: "every {{N}} turns with {{OVERLAP}} turn overlap"

bank_isolation:
  bankId: "{{NAMESPACE_KEY}}"
  bankMission: "{{ROLE_DESCRIPTION}}"
  cross_bank_queries: "{{opt-in / disabled}}"

promotion_policies:
  working_to_episodic: "{{CRITERIA}}"
  episodic_to_semantic: "{{CRITERIA — HIGHEST RISK TRANSITION}}"

rollback_triggers:
  - "{{CONDITION_1}}"
  - "{{CONDITION_2}}"
```

#### Worked Example: MetaSystem Memory Architecture

```yaml
# Memory Architecture — MetaSystem
system: "MetaSystem"
created: "2026-04-19"
owner: "Nick"

storage_topology: "flat-file"
isolation_scope: "per-system (Improvement Loop / Meta-System / Household OS / Claude Build)"
org_scale_pattern: "structured-ontology (governance: DDs, IBs, SL); knowledge-work vector-DB candidate at >10K findings"

tiers:
  working:
    store: "context window (CLAUDE.md + PROGRESS.md injection)"
    retention: "session duration"
    compaction: "harness-managed compaction"
    max_tokens: 200000

  episodic:
    store: "MEMORY.md (auto-memory) + PROGRESS.md (session bridge)"
    retention: "indefinite (manual pruning)"
    write_policy: "append with session context"
    gc_scoring: "manual review — no automated scoring yet"

  semantic:
    store: "CLAUDE.md files (project + system), skills, rules, governance docs"
    retention: "years (curated by Nick)"
    write_policy: "human-gated — Nick deploys all changes"
    promotion_gate: "Nick reviews and approves"

  governance:
    store: "git history + system-log entries per system (DD-59)"
    retention: "append-only, git-permanent"
    write_policy: "immutable (git commits)"

recall_strategy: "static file injection (CLAUDE.md at session start)"
recall_budget: "~15000 tokens across CLAUDE.md files"
retain_cadence: "session end (PROGRESS.md update)"

bank_isolation:
  bankId: "system-scoped (DD-55, DD-56, DD-59 boundaries)"
  bankMission: "Improvement Loop = research-intelligence; Meta-System = governance; Household OS = ops; Claude Build = schema"
  cross_bank_queries: "opt-in via explicit cross-system reference (e.g., agents/codifier/agent.md may read ../meta-system/governance/)"

promotion_policies:
  working_to_episodic: "session-handoff skill writes to PROGRESS.md"
  episodic_to_semantic: "Nick manually updates CLAUDE.md or deploys rules/skills"

rollback_triggers:
  - "MEMORY.md entry contradicts a Design Decision"
  - "CLAUDE.md instruction produces repeated agent errors"
  - "Cross-system reference creates a boundary violation"
```

### Session Checkpoint Schema

```yaml
# Checkpoint — {{AGENT_NAME}} — {{SESSION_ID}}
session_id: "{{UUID}}"
agent: "{{AGENT_NAME}}"
started: "{{ISO_8601}}"
last_checkpoint: "{{ISO_8601}}"
objective: "{{WHAT_THIS_SESSION_IS_DOING}}"
workflow_state: "{{planned/awaiting_approval/executing/waiting_on_external/completed/failed}}"
completed_steps:
  - step: "{{STEP_NAME}}"
    outcome: "{{success/failure}}"
    side_effects: ["{{FILE_WRITTEN}}", "{{API_CALLED}}"]
    artifacts: ["{{FILE_PATHS}}"]
    tokens: {input: {{N}}, output: {{N}}}
pending:
  - "{{NEXT_STEP}}"
retry_count: {{N}}
last_error: "{{ERROR_MESSAGE_OR_NULL}}"
constraints_active:
  - "{{CONSTRAINT}}"
progress_summary: "{{ONE_LINE_FOR_NEXT_SESSION}}"
```

#### Worked Example: Research Loop Session Checkpoint

```yaml
# Checkpoint — research-loop — sess-2026-04-19-001
session_id: "sess-2026-04-19-001"
agent: "research-loop"
started: "2026-04-19T09:00:00Z"
last_checkpoint: "2026-04-19T09:45:00Z"
objective: "Scan 5 new sources from watch list, extract findings"
workflow_state: "executing"
completed_steps:
  - step: "fetch_source_1"
    outcome: "success"
    side_effects: ["wrote research-sources/new-source-1.md"]
    artifacts: ["research-sources/new-source-1.md"]
    tokens: {input: 12000, output: 3500}
  - step: "extract_findings_source_1"
    outcome: "success"
    side_effects: ["wrote research-findings/new-finding-1.md", "wrote research-findings/new-finding-2.md"]
    artifacts: ["research-findings/new-finding-1.md", "research-findings/new-finding-2.md"]
    tokens: {input: 8000, output: 6000}
pending:
  - "fetch_source_2"
  - "fetch_source_3"
  - "extract_findings_source_2"
  - "extract_findings_source_3"
retry_count: 0
last_error: null
constraints_active:
  - "max 10 findings per session"
  - "P1 priority sources first"
progress_summary: "2/5 sources processed, 2 findings extracted. Next: source 2 (Anthropic blog post on agent memory)."
```

### Memory Write Policy

```yaml
# Write Policy — {{SYSTEM_NAME}}
system: "{{SYSTEM_NAME}}"

write_pipeline:
  1_extract: "Identify candidate memory from {{SOURCE — conversation / tool output / session summary}}"
  2_classify: "Assign type: {{working / episodic / semantic / user}}"
  3_policy_check: "Is {{AGENT_ROLE}} authorized to write to {{TARGET_TIER}}? {{YES_POLICY / ESCALATE_TO}}"
  4_novelty_check: "Compute surprisal vs. existing corpus. Threshold: {{THRESHOLD}}. Below: {{merge / drop}}. Above: continue."
  5_contradiction_check: "Compare candidate against existing concepts. On contradiction, surface for resolution rather than overwrite."
  6_provenance: "Attach: source={{SOURCE}}, confidence={{HIGH/MED/LOW}}, timestamp={{ISO_8601}}"
  7_write: "Write with TTL={{DURATION}} and confidence={{SCORE}}"

novelty_gate:
  signal: "embedding similarity + lexical overlap vs. nearest neighbors"
  threshold: "{{NUMERIC OR DYNAMIC}}"
  cold_start_policy: "{{accept-all-until-N-entries / fixed-threshold-from-day-one}}"
  per_type_thresholds: "{{enabled / disabled}}"

contradiction_gate:
  detector: "{{LLM-judgment / rule-based / hybrid}}"
  on_contradiction: "{{flag-for-human / auto-resolve-by-recency / auto-resolve-by-confidence}}"

read_ranking:
  weights:
    recency: {{RECENCY_WEIGHT}}
    source_reliability: {{RELIABILITY_WEIGHT}}
    user_relevance: {{RELEVANCE_WEIGHT}}

prohibited_writes:
  - "{{CATEGORY_1 — e.g., raw conversation transcripts to semantic tier}}"
  - "{{CATEGORY_2 — e.g., unvalidated facts to governance tier}}"
```

#### Worked Example: MetaSystem Write Policy

```yaml
# Write Policy — MetaSystem
system: "MetaSystem"

write_pipeline:
  1_extract: "Identify candidate memory from session work (decisions, preferences, constraints discovered)"
  2_classify: "Assign type: working (PROGRESS.md) / episodic (MEMORY.md) / semantic (CLAUDE.md, rules)"
  3_policy_check: "Agent can write to working and episodic. Semantic requires Nick's approval."
  4_novelty_check: "Manual review at session-end (no automated novelty gate yet — gap)"
  5_contradiction_check: "Manual: Owner agent cross-checks new DDs against existing constitution"
  6_provenance: "Attach: source=session-N, confidence=HIGH/MED, timestamp=2026-04-19"
  7_write: "Working: immediate. Episodic: session end. Semantic: after human review."

novelty_gate:
  signal: "manual / human review only"
  threshold: "n/a"
  cold_start_policy: "n/a"
  per_type_thresholds: "n/a"

contradiction_gate:
  detector: "Owner agent + human review"
  on_contradiction: "DD supersession via DD-44 lifecycle"

read_ranking:
  weights:
    recency: 20
    source_reliability: 50
    user_relevance: 30

prohibited_writes:
  - "Raw conversation transcripts to MEMORY.md (extract structured facts instead)"
  - "Unreviewed agent opinions to CLAUDE.md (human gate required)"
  - "Hardcoded counts or volatile data to any persistent tier"
```

### Hybrid Retrieval Recipe

```yaml
# Retrieval Recipe — {{SYSTEM_NAME}}
system: "{{SYSTEM_NAME}}"
backend: "{{MongoDB Atlas / Postgres+pgvector / dedicated search service / dual-store}}"

decomposition:
  enabled: "{{true / false}}"
  model: "{{small_model_name — e.g., gpt-4-mini}}"
  prompt_version: "{{semver}}"
  fan_out: "{{vector + lexical / vector only / vector + lexical + graph}}"

fusion:
  type: "{{rank_fusion / score_fusion}}"
  vector_index: "{{index_name, embedding_model, dimensions}}"
  lexical_index: "{{index_name, tokenizer}}"
  benchmark_mode: "{{exact:true / ann}}"

reranker:
  type: "{{weighted_signals / learned (model_name) / none}}"
  signals:
    quoted_phrase: {{WEIGHT}}
    temporal_proximity: {{WEIGHT}}
    entity_match: {{WEIGHT}}
    keyword_overlap: {{WEIGHT}}
  query_conditioned: "{{true / false}}"

caching:
  decomposition_cache: "{{enabled / disabled}}"
  rerank_cache_key: "{{(query, candidate_set) hash}}"

evaluation:
  benchmark: "{{LongMemEval-S / domain-specific / none}}"
  ann_disabled_for_recipe_eval: "{{true / false}}"
  per_query_class_breakout: "{{true / false}}"
```

#### Worked Example: Memongo Retrieval Recipe

```yaml
# Retrieval Recipe — Memongo (reference implementation)
system: "Memongo"
backend: "MongoDB Atlas"

decomposition:
  enabled: true
  model: "gpt-4-mini"
  prompt_version: "v1 (treat as ContractSpec)"
  fan_out: "vector + lexical"

fusion:
  type: "rank_fusion ($rankFusion)"
  vector_index: "Voyage 4 Large auto-embed, Atlas vectorSearch"
  lexical_index: "Atlas $search, default tokenizer"
  benchmark_mode: "exact:true (for benchmark); ann (for production)"

reranker:
  type: "weighted_signals"
  signals:
    quoted_phrase: 0.60
    temporal_proximity: 0.40
    entity_match: 0.40
    keyword_overlap: 0.30
  query_conditioned: false  # static weights; improvement candidate

caching:
  decomposition_cache: "disabled (improvement candidate)"
  rerank_cache_key: "n/a"

evaluation:
  benchmark: "LongMemEval-S"
  ann_disabled_for_recipe_eval: true
  per_query_class_breakout: true  # weakest at multi-hop temporal (84.0%)
```

### Parallel Coordination Setup

```markdown
## Parallel Agent Setup — {{PROJECT_NAME}}

### Shared Infrastructure
- Upstream repo: {{PATH}}
- Lock directory: {{PATH}}/locks/
- Agent count: {{N}}

### Lock Protocol
- Lock acquisition: atomic file creation in locks/
- Lock timeout: {{MINUTES}} minutes (detect abandoned locks)
- Lock metadata: agent ID, timestamp, task description
- Conflict resolution: {{GIT_MERGE / HUMAN_REVIEW}}

### Per-Agent Configuration
| Agent | Workspace | Task Scope |
|-------|-----------|-----------|
| {{AGENT_1}} | {{PATH}} | {{SCOPE}} |
| {{AGENT_2}} | {{PATH}} | {{SCOPE}} |
```

### Subagent Memory Directory Setup

```yaml
# Subagent Memory — {{SUBAGENT_NAME}}
name: "{{SUBAGENT_NAME}}"
description: "{{ROLE_DESCRIPTION}}"
memory: "{{user / project / local}}"

# Effective directory:
#   user    → ~/.claude/agent-memory/{{SUBAGENT_NAME}}/
#   project → .claude/agent-memory/{{SUBAGENT_NAME}}/
#   local   → .claude/agent-memory-local/{{SUBAGENT_NAME}}/

# MEMORY.md structure (auto-loaded: first 200 lines or 25KB)
sections:
  - "## Patterns I've seen"        # accumulating learnings
  - "## Conventions to follow"     # codified preferences
  - "## Recurring issues"          # known failure modes
  - "## Index of supplementary files"  # pointers to detail files in the directory

# Curation directive (added to system prompt automatically when over budget):
#   "Compress, prune, restructure MEMORY.md to fit budget; preserve high-signal sections."

# Orchestration prompts:
on_invocation: "Review the task, then check your memory for relevant patterns."
on_completion: "Save what you learned to your memory directory."
```

---

## Worked Example: MetaSystem Current State and Gaps

```
Session Management — MetaSystem (April 2026)

MEMORY TIERS (implicit, not designed):
  Working:  CLAUDE.md files + PROGRESS.md injection at session start  [exists]
  Episodic: MEMORY.md (auto-memory, append-only, unstructured)       [exists, no provenance]
  Semantic: CLAUDE.md, skills, rules                                 [exists, human-gated]
  Governance: git history + system-log entries (DD-59 distributed)   [exists, append-only]

STORAGE TOPOLOGY:
  Flat-file markdown                                                 [intentional — small corpus, debuggability]
  Migration trigger: >10K findings or human cannot scan corpus       [not yet hit]

ISOLATION SCOPE:
  Per-system boundary (DD-55, DD-56, DD-59)                          [enforced via folder structure]
  Cross-system reads: opt-in only                                    [enforced via constitution]

RECALL STRATEGY:
  Static file injection (CLAUDE.md loaded at session start)          [exists]
  Auto-recall from semantic store                                    [gap — no semantic query]
  Tool-based memory search                                           [gap — no search tool]
  Hybrid retrieval pipeline                                          [gap — flat-file scale; not yet justified]

SESSION BOUNDARY PROTOCOL:
  1. Read PROGRESS.md -> understand current state                    [enforced]
  2. Single focused objective per session                            [enforced via handoff prompts]
  3. Environmental feedback: file reads, grep, frontmatter checks    [enforced]
  4. Clean state: all files written, indexes updated                 [enforced]
  5. Update PROGRESS.md + write handoff prompt                       [enforced]

WRITE POLICY:
  Working: agent writes freely                                       [exists]
  Episodic: agent appends to MEMORY.md                               [exists, no quality filter]
  Semantic: human gate (Nick deploys)                                 [exists, enforced]
  Governance: git commits (automatic)                                [exists]
  Novelty filter at write time                                       [gap — manual review only]
  Contradiction detection                                            [gap — manual; Owner agent ad-hoc]

GAPS IDENTIFIED:
  1. No structured checkpoint (JSON workflow state)
     -> crash recovery requires full session replay
     -> APPLY: Step 3.1 (workflow state separation) + Step 3.2 (persistence)

  2. MEMORY.md lacks provenance, TTL, or confidence scoring
     -> no way to distinguish high-confidence decisions from speculative observations
     -> APPLY: Memory Write Policy template + Step 1.3 (promotion policies)

  3. No auto-recall from episodic or semantic memory
     -> agent relies on static CLAUDE.md injection only
     -> APPLY: Step 2.1 (auto-recall vs tool-based)

  4. No structured fact extraction
     -> decisions embedded in conversation are lost to compaction
     -> APPLY: Step 3.3 (structured fact extraction)

  5. No effort scaling rules in orchestrator prompts
     -> subagent count is ad hoc per skill
     -> APPLY: Step 4.2 (effort scaling)

  6. No parallel coordination (lock-based or otherwise)
     -> single-session only (extract-artifacts uses disjoint dispatch, not locks)
     -> APPLY: Step 4.3 (parallel coordination) when parallel work begins

  7. No novelty filtering at write time
     -> MEMORY.md may accumulate near-duplicate entries silently
     -> APPLY: Step 5.2 (novelty filtering); start with manual periodic dedup

  8. No contradiction detection between MEMORY.md entries and DDs
     -> entries that contradict governance can sit unflagged
     -> APPLY: Step 5.3 (contradiction detection); periodic Owner agent audit is current substitute

  9. Subagent memory directories not yet adopted
     -> Librarian/Codifier/Owner each could maintain their own learnings; currently hand-maintained reflections in agents/{role}/reflections/
     -> APPLY: Subagent Memory Directory Setup template; trial in Librarian first

 10. memory.md cross-session pattern not adopted
     -> Nick's preferences/corrections currently propagate via auto-MEMORY.md only
     -> APPLY: Step 3.4; consider adding session-scoped memory.md alongside MEMORY.md

 11. Active-documentation requirement for DDs/IBs/SL
     -> Acceptable for governance (deliberate friction), but capture-as-byproduct should expand for non-governance signal
     -> APPLY: Step 6.3; consider hooks for automatic session-event capture
```

---

## Decision Tree: What Kind of Memory Problem Do You Have?

```
START: What is failing?
  |
  +-- "Agent forgets decisions from prior sessions"
  |     -> Step 3.3: Extract structured facts from conversations
  |     -> Step 3.4: Add memory.md cross-session pattern
  |     -> Step 2.1: Implement auto-recall for fact injection
  |
  +-- "Agent crashes and loses all progress"
  |     -> Step 3.1: Separate workflow state from conversation state
  |     -> Step 3.2: Implement crash-resilient persistence
  |
  +-- "Agent's memory is full of noise / contradictions"
  |     -> Step 1.3: Define promotion and demotion policies
  |     -> Step 5.2: Add novelty filtering at write time
  |     -> Step 5.3: Add contradiction detection
  |     -> Memory Write Policy template: add provenance and TTL
  |
  +-- "Sessions overrun context and quality degrades"
  |     -> Step 4.1: One feature per session with clean-state exit
  |     -> Step 4.2: Effort scaling rules in orchestrator
  |
  +-- "Parallel agents step on each other's work"
  |     -> Step 4.3: Filesystem locks for coordination
  |
  +-- "Memory retrieval misses relevant information"
  |     -> Step 2.1: Switch from tool-based to auto-recall
  |     -> Step 2.2: Add hybrid retrieval (semantic + lexical fusion)
  |     -> Step 2.3: Add query decomposition for multi-intent queries
  |     -> Step 3.3: Ensure facts are typed and semantically embeddable
  |
  +-- "Reranker output is wrong but I can't tell why"
  |     -> Step 2.4: Switch to weighted-signal rerank with inspectable signals
  |
  +-- "CLAUDE.md is bloated and rules contradict each other"
  |     -> Step 2.5: Adopt ACE pattern for behavioral rules
  |     -> Or: shrink CLAUDE.md to permanent truths only; add memory.md for accumulating preferences
  |
  +-- "Memory from one project leaks into another"
  |     -> Step 1.4: Scope and isolate memory banks (bankId per project)
  |     -> Subagent Memory Directory Setup template (project / local scope)
  |
  +-- "Each subagent re-derives the same context every invocation"
  |     -> Step 1.4: Subagent persistent memory directories
  |     -> Subagent Memory Directory Setup template
  |
  +-- "Multi-store ops cost is killing us"
  |     -> Step 1.2: Evaluate single-store polymorphic (e.g., MongoDB Atlas with $rankFusion)
  |
  +-- "Document ingestion is too expensive"
  |     -> Step 6.2: Local parsing before LLM processing
  |
  +-- "Knowledge system isn't accumulating valuable signal"
  |     -> Step 6.3: Make capture a byproduct of work, not a separate doc act
```

---

## Pitfalls

### 1. Conversation history as the only state
Conversation transcripts are not retry-safe, not queryable, and grow unbounded. Separate workflow state (structured, persistent, retry-safe) from conversation state (append-only, ephemeral). Never derive workflow state from conversation replay.

### 2. Persist only on shutdown
Crashes happen during execution. Persist after every significant event -- step completion, tool execution, permission grant, commit. The load/reconstruct/restore pattern must work from any checkpoint, not just the final one.

### 3. Unrestricted agent writes to long-term memory
Without a write policy, agents pollute durable memory with unvalidated, low-confidence, or hallucinated information. This creates a compounding reliability problem: future retrievals return polluted data, which produces worse outputs, which get persisted again. Memory pollution is distinct from context rot -- it affects future sessions, not just the current one.

### 4. Tool-based memory as the only recall mechanism
Requiring the agent to decide when to search memory fails at exactly the moment it matters most: when the agent does not know what it does not know. Auto-recall removes this meta-cognitive requirement. The token cost is real but bounded and worth it.

### 5. Multi-feature sessions
Sessions that tackle multiple features exhaust context, leave unclean state, and make handoffs fragile. One feature, clean state, update progress. The constraint feels slow but yields higher throughput across a sequence of sessions.

### 6. Self-assessed progress
"I think this is correct" is not verification. Environmental feedback (test results, tool output, API responses) is the only reliable verification signal. Agents that self-assess pursue dead-end strategies without detection.

### 7. Promotion without governance
The highest-risk operation in any memory system is cross-layer promotion -- especially episodic to semantic. Uncontrolled promotion pollutes the knowledge layer that every future session relies on. Define explicit ownership, approval levels, and rollback paths for every tier boundary.

### 8. Raw transcript storage as memory
Storing entire conversation transcripts is expensive, noisy, and makes recall brittle (keyword search) or costly (full embedding). Extract discrete typed facts instead. Facts are compact, individually embeddable, and survive compaction.

### 9. Monolithic context-rewrite collapse
Whole-file rewrites of behavioral context (e.g., one big CLAUDE.md or one prompt file) carry catastrophic-edit risk: a single bad edit corrupts every future task that loads that file. Granular vote-weighted upserts (the ACE pattern in Step 2.5) eliminate the rewrite class of failure. If you must keep a monolithic file, version-control it aggressively and apply the smallest possible diffs.

### 10. Opaque rerankers as black-box debugging dead-ends
A learned reranker that ranks the wrong memory first leaves "the reranker thought this was more relevant" as the only explanation — which is not actionable. Prefer weighted-signal rerankers (Step 2.4) when debuggability matters more than absolute top-1 precision. If you adopt a learned reranker, also instrument per-signal probes so you can detect which retrieval-pipeline stage degraded when quality drops.

### 11. Cross-bank memory contamination
Memory banks shared across agents, projects, or users pollute each other's recall. A coding agent learning your prose style from a writing agent's bank will misapply it; a Project A bank polluting Project B's retrieval surfaces wrong context. Isolate banks by default (Step 1.4); make cross-bank queries opt-in. Over-isolation creates knowledge silos — the boundaries should match the actual knowledge boundaries, not just the organizational ones.

### 12. Active-documentation requirement
Knowledge systems that require a separate documentation step accumulate the *easy-to-document* signal and miss the *judgment-rich* signal that would make them valuable. The people with the most valuable context are the most strategic about withholding it. Capture must be a byproduct of doing the work (Step 6.3): commit messages over doc files, ticket updates over status emails, decisions made *in* the system rather than *about* the system.

---

## Related Guides

- **Memory tiers map to agent infrastructure:** The four-tier model in Step 1.1 is the memory dimension of the infrastructure tiers described in *Agent Architecture Decisions* (G3), Step 6.
- **Session resets defend against context rot:** The clean-state session boundaries in Step 4.1 are context rot mitigations described in *Managing Agent Context* (G2), Step 4.
- **Effort scaling requires baseline measurement:** The effort scaling rules in Step 4.2 presuppose the single-agent baseline measurement in *Agent Architecture Decisions* (G3), Step 1.
- **Structured facts are context engineering:** The fact extraction in Step 3.3 connects to the context curation patterns in *Managing Agent Context* (G2).
- **Retrieval pipeline overlaps with context retrieval:** The hybrid retrieval recipe in Part 2 also serves context-injection use cases in *Managing Agent Context* (G2). Memory and context are different concerns over the same retrieval substrate.
- **Write policies connect to governance:** The memory write policy in Step 5.1 is the memory-specific instantiation of the governance patterns in *Agent Governance and Trust* (G9).
- **Subagent memory connects to spec design:** Subagent memory directories (Step 1.4) are a specification-level decision — see *Writing Agent Specifications* (G1) for how to declare them in a subagent's contract.
- **Vault-as-OS memory substrate:** *[[building-agentic-systems]]* (G11) covers system-shape questions (open-brain, ai-managed-vault, compounding-knowledge-loop) that share findings with G7. G7 covers the substrate-level memory mechanics; G11 covers how those mechanics compose into an agentic OS.

---

## Contract

### Preconditions
- You have an agent system that persists beyond a single prompt-response cycle.
- You can write to a filesystem or database for state persistence.
- You understand the difference between conversation state (what was said) and workflow state (what was done).

### Invariants
- Memory is organized into explicit tiers with defined read/write policies per tier.
- Storage topology (single-store / multi-store / flat-file) is chosen against documented criteria, not by deployment speed.
- Workflow state is tracked separately from conversation state and is the authoritative record of progress.
- Sessions leave the system in a clean, resumable state verified by automated checks.
- Memory writes are policy-governed AND novelty-gated AND contradiction-checked — agents do not freely append to long-term stores without provenance, classification, and authorization.
- Memory banks are scoped (per-agent, per-project, per-user, or per-session); cross-bank queries are opt-in.
- Environmental feedback, not self-assessment, drives agent decisions at every state-modifying step.
- Promotion across tier boundaries is the highest-risk operation and is explicitly governed.
- Retrieval pipelines are debuggable: ranked outputs decompose into inspectable signal contributions.

### Governance
- Memory tier boundaries, promotion policies, retention rules, and isolation scopes are documented per system.
- Storage topology rationale is documented (why single-store vs. multi-store; what would trigger migration).
- Session boundary conventions (one-feature, clean-state, progress-update) are enforced by handoff prompts.
- Write policies specify which agent roles can write to which tiers, and what novelty / contradiction gates apply.
- Retrieval recipes (decomposition prompt, fusion configuration, rerank weights) are versioned as ContractSpecs; changes go through review.
- This guide is owned by Meta-System knowledge layer.

### Recovery
- If an agent crashes mid-task: load the last persisted workflow checkpoint, identify completed side effects, resume from the next incomplete step. Do not replay the conversation.
- If session handoff loses context: read PROGRESS.md and the handoff prompt from the prior session.
- If memory is corrupted at a tier: fall back to the last known-good state at that tier and reconstruct. Governance tier (git history) is the ultimate fallback.
- If parallel agents conflict: check the lock directory for abandoned locks; resolve via git merge or human review.
- If promotion pollutes the semantic tier: quarantine the affected entries, review the promotion filter, reconstruct from episodic tier if needed.
- If retrieval quality degrades: decompose the rerank score into per-signal contributions; identify the failing stage (decomposition / fusion / rerank); roll back to a prior version of the recipe; re-evaluate against benchmark with `exact:true` to isolate recipe quality from index tuning.
- If novelty gate admits noise: tighten threshold; add per-evidence-type thresholds; audit accepted-but-low-value writes to refine the signal.
- If a contradiction goes undetected: surface via periodic audit; route through the contradiction-resolution workflow rather than silent overwrite.
- If a subagent's memory drifts: diff the curation changes against prior MEMORY.md versions; revert if needed; tighten curation directive in the subagent's system prompt.
