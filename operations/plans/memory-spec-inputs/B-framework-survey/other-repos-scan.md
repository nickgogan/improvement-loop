---
title: "Other watched-library repos — memory-mechanism catch-all scan"
purpose: "Feeds the B-framework-survey track of the E1 memory-architecture spec"
scope: "All watched-library analyses NOT already covered by dedicated memory dossiers (mem0, openclaw, hermes-agent, archon, letta, supermemory, memongo, mempalace, superpowers, bmad-method, gsd, Claude Code, Codex)"
method: "Grepped 21 analysis docs + read 4 registry-only entries (no analysis) for memory/persist/checkpoint/ledger/recall/reflect/consolidate/decay/session-state keywords. No web research; no repo re-cloning."
date: "2026-07-16"
---

# Other-Repos Memory Scan

## 1. Notable — real memory mechanism

### CrewAI
`analysis/crewai-analysis.md`
- **Surface**: Unified `Memory` class (crew-level, shared across agents) with short-term / long-term / entity memory; separate `Flow` state (Pydantic model or dict) persisted via a `@persist` decorator; separate checkpoint layer (event-driven state snapshots, JSON or SQLite).
- **Writer**: Memory is written with **LLM-analyzed encoding at write time** — an LLM infers scope, category, and importance when a memory is saved, rather than leaving all the work to retrieval-time ranking.
- **Recall**: Adaptive-depth retrieval; supports scope/slice views; pluggable storage (LanceDB default, Qdrant Edge). A 17+-category typed event bus (`crewai_event_bus`) fires on every memory/knowledge/checkpoint event, giving built-in observability into memory read/write.
- **Distinctive**: Write-time LLM classification is the opposite of most frameworks' read-time-only retrieval — it's a "smart writer" rather than "smart reader" design. Three separate persistence layers (memory / flow-state / checkpoint) are cleanly decomposed rather than conflated.

### AutoGen
`analysis/autogen-analysis.md`
- **Surface**: Abstract `Memory` interface (`update_context`, `query`, `add`, `clear`) with pluggable backends — ChromaDB, Redis, Mem0, a "Canvas" scratchpad, and a plain `ListMemory`. Separately, `MagenticOneOrchestratorState` holds a **task ledger + progress ledger**, JSON-serializable for persistence.
- **Writer**: Memory enriches model context by injection (added as messages) before inference. The ledger is written turn-by-turn by the orchestrator: facts extracted and classified (given/verified, to-look-up, to-derive, educated-guess), plan created, then a structured per-turn JSON progress assessment.
- **Recall**: Ledger state feeds a stall-detection + adaptive-replanning loop. Experimental `TaskCentricMemory` stores task-insight pairs specifically for cross-session learning (distinct from the in-conversation Memory interface).
- **Distinctive**: The MagenticOne ledger is a meta-cognitive state-tracking pattern (what's known, what's the plan, is the group stalling) — not memory-as-recall so much as memory-as-self-monitoring. Framework is in maintenance mode, so this pattern is frozen but usable as reference.

### ADK-Python (Google)
`analysis/adk-python-analysis.md`
- **Surface**: `sessions/` (session services: in-memory, SQLite, database, Vertex AI) and a separate `memory/` module (in-memory, Vertex AI RAG).
- **Writer**: **Event sourcing is the persistence model** — events are the ground truth; the LLM context is a derived view reconstructed from the event log. Every node's output/interrupt is persisted as an event.
- **Recall**: Session state reconstructed from event replay; memory services surface longer-horizon retrieval (RAG) separately from session events. Graph workflow has a checkpoint-resume lifecycle (`ResumabilityConfig`) built on the same event log.
- **Distinctive**: Clean separation of *session* (event-sourced, short-horizon, exact replay) from *memory* (RAG, long-horizon, lossy retrieval) as two different services with two different consistency models.

### LangGraph
`analysis/langgraph-analysis.md`
- **Surface**: `BaseCheckpointSaver` (Postgres / SQLite / in-memory) persists full graph state after every superstep. `BaseStore` is a separate persistent, cross-thread key-value + vector store. `interrupt()` pauses a node, persists state via checkpoint, and waits for human input; resumes via `Command`.
- **Writer**: Checkpoint written automatically after each superstep (no manual write call). Store is explicitly read/written by tools via `InjectedStore` type-annotation injection.
- **Recall**: Any checkpoint implementation must pass a **conformance test suite** (`libs/checkpoint-conformance/`) — a specification-as-tests guardrail so custom backends (Postgres/SQLite/Redis) are interchangeable. `EncryptedSerializer` provides AES-EAX at-rest encryption for checkpoint data; a 47-entry `SAFE_MSGPACK_TYPES` allowlist guards deserialization.
- **Distinctive**: The checkpoint/store split (execution-state persistence vs. cross-thread durable memory) plus the conformance-test-as-interface-spec pattern is the most infrastructure-mature checkpointing design in this batch. Already noted in the analysis as "skipped: framework-specific, single-source" for KB extraction — worth reconsidering given E1's checkpoint-spec needs.

### AutoGPT Platform
`analysis/autogpt-analysis.md`
- **Surface**: **Graphiti** — a FalkorDB-backed knowledge graph — for CoPilot's long-term memory (`copilot/graphiti/`). Separately, a fleet-orchestration **checkpoint protocol**: agents emit `CHECKPOINT:<step-name>` to signal progress, tracked per-agent alongside window/worktree/branch/objective/PR/session_id in a JSON state file.
- **Writer**: Graphiti ingests conversation/task content into graph form (not detailed further in the analysis — flagged as a "direct content" doc, not deep-read). Checkpoint protocol is agent-emitted text parsed by the orchestrator.
- **Recall**: `verify-complete.sh` validates checkpoints, unresolved threads, CI status, and staleness before considering an agent done — checkpoint state gates task completion, not just progress display.
- **Distinctive**: Two unrelated "memory" mechanisms coexist at different altitudes — Graphiti as agent long-term memory (knowledge-graph recall) vs. the checkpoint protocol as fleet-supervision progress ledger (operational, not semantic). Worth distinguishing these when citing AutoGPT in the spec.

### gstack
`analysis/gstack-analysis.md`
- **Surface**: Cross-session learnings in JSONL files at `~/.gstack/projects/{slug}/learnings.jsonl`, plus session markers (`~/.gstack/sessions/`) and analytics timeline events (`~/.gstack/analytics/`).
- **Writer**: `/learn` skill (review, search, prune, export) manages the learnings file explicitly — this is a user/agent-invoked write path, not automatic capture.
- **Recall**: Learnings are loaded via a shared bash "preamble" block (injected identically across all skills) at skill start, and searched on demand.
- **Distinctive**: Learnings persist and compound ("the agent gets smarter over time within a project") but the write path is deliberate/curated rather than an always-on capture hook — a middle ground between opencode's `/learn` (below) and OpenViking's fully automatic hooks.

### deer-flow
`analysis/deer-flow-analysis.md`
- **Surface**: `MemoryMiddleware` queues conversation content post-execution; a background updater summarizes and writes to per-thread/per-agent storage.
- **Writer**: Async, write-behind — happens after the turn completes, not inline.
- **Recall**: `_get_memory_context()` loads the stored summary and injects it into the next system prompt inside `<memory>` XML tags, alongside `<soul>` (persona) tags.
- **Distinctive**: Clean write-behind/read-on-boot split with explicit prompt-tag namespacing (`<memory>` vs `<soul>`) — a small, legible reference implementation of "summarize after, inject before."

### opencode
`analysis/opencode-analysis.md`
- **Surface**: `/learn` command as "the memory write-path" — session learnings distilled into the *deepest applicable* `AGENTS.md` file, 1–3 lines each, with explicit include/exclude criteria. Separately, `task_id` lets a child subagent session resume with context intact (persistent subagent identity across turns).
- **Writer**: Agent-invoked at end of session; writes plain markdown into the existing chain-loaded context-file hierarchy (no new infrastructure).
- **Recall**: Ordinary chain-loading — the distilled learning is picked up automatically next time that directory subtree is touched, via the same lazy AGENTS.md loading as everything else.
- **Distinctive**: A "complete file-based memory loop with zero new infrastructure" (analysis's own words) — memory *is* the existing context-file system, not a bolt-on store. Already flagged in-analysis as "partial existing coverage" via `gsd-global-learnings-store-cross-session-persistence`.

### beads
`analysis/beads-analysis.md`
- **Surface**: Shared Dolt database as the only coordination channel between agents ("database-as-shared-memory"). Closed tasks are summarized rather than deleted; "notes" fields survive context compaction.
- **Writer**: Agents write directly to issue state in Dolt (hash-based IDs prevent collision; cell-level merge handles concurrent writes).
- **Recall**: Any agent reads shared state directly from the DB — no message bus, no direct agent-to-agent channel.
- **Distinctive**: Two patterns here are **already promoted to the KB** as standalone findings — `database-as-shared-memory-coordination` and `semantic-memory-decay-compaction` (both 2026-04-19). Listed here for completeness; no new extraction needed, but beads is the clean shipped reference if the spec cites either pattern.

### OpenViking
`analysis/openviking-analysis.md` (richest hit-count of the batch — 45)
- **Surface**: Five-file workspace taxonomy (`SOUL.md`, `TOOLS.md`, `USER.md`, `MEMORY.md`, `HEARTBEAT.md`) loaded at session start; a three-tier (L0/L1/L2) progressive-detail filesystem-as-context store; typed memory items (profile/preferences/entities/events/cases/patterns/tools/skills) with per-field `merge_op` (immutable / upsert / append) governing update semantics.
- **Writer**: Fully hook-driven and automatic — `Stop` hook → `auto-capture.mjs` parses the transcript and runs an async LLM-based `memory_extraction` pass into typed items after every session; extraction prompts carry explicit anti-prompt-injection and "no relative time expressions" rules.
- **Recall**: `UserPromptSubmit` hook → `auto-recall.mjs` → memory search → results injected as a `<relevant-memories>` system-message prefix before every turn. Namespace isolation by `account_id` × `user_id` × `agent_id` keeps agents' learned patterns from bleeding into each other.
- **Distinctive**: The most complete "transparent memory" reference implementation in the batch — agent never explicitly calls memory tools; it's captured and recalled entirely via lifecycle hooks. Several sub-patterns (hook-based transparent injection, merge-op immutability) are already promoted to the KB individually, but the *pipeline as a whole* (SessionStart → bootstrap, UserPromptSubmit → recall, Stop → capture, async extraction into typed+schema'd memory) has not been captured as a single end-to-end architecture reference. See escalation flag below.

### Paperclip
`analysis/paperclip-analysis.md`
- **Surface**: PARA-based (Projects/Areas/Resources/Archives) three-layer file memory per agent workspace: (1) knowledge graph of atomic YAML facts with supersession, (2) daily notes as raw timeline, (3) `MEMORY.md` as curated tacit-knowledge.
- **Writer**: Agent skill (`para-memory-files`) governs writes; includes decay rules and a weekly synthesis pass that rolls daily notes up into durable knowledge.
- **Recall**: `qmd` provides semantic recall over the memory store.
- **Distinctive**: Already promoted to the KB as `para-based-file-memory` (2026-04-08) — described in-analysis as "more structured than OpenClaw's flat memory files." Note for completeness; no new extraction needed.

### Gbrain (registry-only, no analysis doc)
`gbrain.md`
- **Surface**: Markdown-in-git as system of record, synced into a derived Postgres layer; self-wiring typed knowledge graph built with **zero LLM calls**; hybrid search (vector + keyword + graph signal).
- **Writer**: Git commits to markdown are the source of truth; a sync process derives the DB from git, not the reverse ("write-back discipline — memory is not the brain").
- **Recall**: 30+ typed MCP tools; a synthesis layer returns cited prose plus explicit gap analysis rather than raw retrieved pages.
- **Distinctive**: This is a *world-KB*, not agent conversational memory (per the KB's own memory/wiki/world-KB trichotomy) — already the "cleanest shipped instance" of several existing findings (markdown-git-system-of-record, write-back-discipline, query-shape-first-storage-design). Directly comparable to MetaSystem's own markdown-git substrate — worth a one-line mention in the spec as a real-world analog, no new extraction needed.

### ob1
`analysis/ob1-analysis.md`
- **Surface**: One Supabase (pgvector) database as the sole "brain"; any AI client connects via MCP; extensions/recipes/skills all read/write the same `thoughts` table.
- **Writer/Recall**: No middleware, no sync protocol — direct reads/writes to the shared table.
- **Distinctive**: "Hub-and-spoke memory architecture" — contrasts with file-first approaches (MetaSystem, OpenClaw) and structured-ontology approaches (Paperclip). Already flagged in-analysis as "skipped: covered by multiple existing memory architecture findings" — listed for completeness only.

## 2. Minor — incidental state only

- **langflow** — `MemoryComponent` gives cross-turn context; `session_id`-scoped persistence across flow runs. Generic RAG-style memory node, no distinctive recall/write mechanics documented.
- **n8n** — one doc reference to "memory tiers" in an internal engineering-standards file; not elaborated in the analysis.
- **pi-agent** — `appendEntry()` for state persistence of custom entries not sent to the LLM; a log, not a recall mechanism.
- **deep-tutor** — `read_memory` / `write_memory` listed as always-on tools; no detail on storage shape or recall path.
- **pydantic-ai** — analysis explicitly states memory is treated as a harness capability the framework deliberately does not provide ("everything else — memory, guardrails, context management... is a shared store").
- **sandbox** — only Docker-level memory/CPU resource caps; unrelated to agent memory.
- **oz-workspace** — per-room kanban board (backlog → in progress → done) and inbox notifications are persisted task state, not agent memory/recall.
- **taches-cc-resources** — "memory" appears only metaphorically ("rules from memory" as a failure mode the audit skill guards against by mandating reading from disk); no memory mechanism.

## 3. Nothing relevant

- warp
- ponytail (registry-only)
- mattpocock-skills (registry-only)

## 4. Escalation flags

Repos whose memory mechanism looked substantial enough in this pass that a dedicated deep-dive dossier might be worth the orchestrator's consideration (none of these currently have one; all were assessed only via the existing structural-analysis doc):

1. **OpenViking** — strongest candidate. The full session-lifecycle hook pipeline (SessionStart/UserPromptSubmit/Stop → bootstrap/recall/capture) plus typed-schema memory with per-field `merge_op` governance is the most implementation-ready reference for E1's "auto-recall / auto-capture" mechanics. Individual sub-patterns are already promoted to the KB, but no document currently captures the pipeline end-to-end as a single architecture.
2. **CrewAI** — the write-time LLM-analyzed memory encoding (classify at save, not just at retrieval) plus the three-layer persistence split (memory / flow-state / checkpoint) is distinctive enough, and the framework mature enough, to warrant closer treatment than a cherry-pick line.
3. **LangGraph** — checkpoint/store architecture (conformance-tested, encryptable, cross-thread durable store separate from execution-state checkpoint) is the most infrastructure-mature "durable execution" pattern here; relevant if E1 needs a checkpoint/replay design reference, not just a recall-store reference.
4. **AutoGen** — the MagenticOne ledger (task ledger + progress ledger + stall detection + replanning) is a distinct pattern class — meta-cognitive self-monitoring state rather than recall memory — that none of the already-covered repos (mem0/letta/supermemory/etc.) represent. Worth a flag if the spec wants to cover "process/progress memory" as a category alongside semantic/episodic memory.
