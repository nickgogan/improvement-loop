---
title: "B — Cross-Framework Memory Survey: Synthesis"
author: Synthesizer (E1 memory-architecture spec, Track B judgment layer)
date: 2026-07-16
consumes: >
  B-framework-survey/ (11 dossiers: mem0, openclaw, hermes, claude-code, codex,
  archon, letta-supermemory, memongo-mempalace, process-repos, escalated-repos,
  other-repos-scan); A1-kb-design-brief.md; governance/prd.md §E1
status: design-input (comparison + judgment; recommendations, not rulings — Nick rules)
recency_rule: 2026/late-2025 weighted over older; older wins only on demonstrated de facto consensus
---

# B — Cross-Framework Memory Survey: Synthesis

The judgment layer over eleven collector dossiers. Where dossiers disagree, this
document says which is better evidenced and why — it does not average. Every
consensus and failure claim is dated to the underlying dossier evidence. The target
is the engine's profile: markdown+git substrate, single-operator (Nick), human-gated
writes to durable knowledge, four actors (Owner/Researcher/Codifier/Librarian), runs
on Claude Code, harness-first, minimum-viable-abstraction.

---

## 1. Comparison matrix

Two tables: memory-type coverage (which types each framework treats as first-class),
then the mechanics (write path, recall, consolidation, decay). Nuance follows in prose —
cells are deliberately terse.

### 1a. Memory-type coverage

`Y` first-class · `~` present but thin/adjacent · `—` absent by design or omission.
"Process" = the AutoGen-ledger candidate fifth type (is the *task* progressing), distinct
from what the agent *knows*.

| Framework | Working | Episodic | Semantic | Procedural | Process |
|---|---|---|---|---|---|
| mem0 | ~ | Y | Y | ~ (logged, not learned) | — |
| OpenClaw | Y | Y | Y | ~ (ad-hoc `learnings.md`) | — |
| Hermes | ~ | Y | Y | Y | — |
| Claude Code | Y | Y | Y | Y | — |
| Codex | Y | Y | Y | Y | — |
| Archon | Y | Y | Y | Y | ~ (run state) |
| Letta | Y | Y | Y | Y | — |
| Supermemory | ~ | Y | Y | — | — |
| Memongo | ~ | Y | Y | Y | ~ (`trace`/provenance) |
| MemPalace | — | ~ | Y | — (explicit) | — |
| Superpowers | Y | — | — (explicit) | ~ (static) | ~ (ledger) |
| BMAD | Y | Y | ~ (human-set) | — | ~ |
| GSD | Y | Y | Y (CRUD store) | ~ (static) | ~ |
| OpenViking | Y | Y | Y | Y | — |
| CrewAI | Y | Y (unified) | Y (unified) | ~ (Flow) | ~ (checkpoint) |
| LangGraph | Y | Y (store) | Y (store) | — (graph *is* procedure) | ~ (checkpoint) |
| AutoGen/MagenticOne | ~ | ~ | — | ~ (`TaskCentricMemory`, exp.) | **Y** |
| Beads (`bd`) | ~ | Y | Y | Y (chemistry formulas) | **Y** |

### 1b. Mechanics

| Framework | Substrate | Write path (gate) | Recall | Consolidation | Decay |
|---|---|---|---|---|---|
| mem0 | vector+graph+SQLite triple | autonomous LLM extract (**ungated**) | vector sim → rerank → temporal | none in-core | soft rank-bias only; ADD-only → monotonic growth |
| OpenClaw | markdown canonical + SQLite index | user cmd / agent distill / Dreaming (**autonomous**) | hybrid semantic+BM25; MEMORY.md bootstrap-inject | Dreaming 3-phase; `DREAMS.md` diary | promotion-gate as write filter; no post-promotion decay |
| Hermes | SQLite (FTS5) + markdown caps | inference-driven agent; skills `write_approval` **off by default** | FTS5 keyword-only (weak); frozen snapshot | reflect-after-task; weekly Curator (unconf.) | **none — manual only** |
| Claude Code | markdown files, machine-local | CLAUDE.md human; auto-memory agent-judged (**autonomous**) | agentic file-read (no index); 200-line/25KB inject | "Auto Dream" (**unconfirmed first-party**) | none native; survives-compaction re-inject |
| Codex | JSONL rollouts + markdown + AGENTS.md | AGENTS.md human; Memories autonomous (idle-6hr, two-model); **generate/use two-switch** | grep + wholesale-summary inject | inline extract→consolidate at write | ~30-day prune (3rd-party) |
| Archon | SQLite/Postgres event-source + files | human semantic; run-state automatic | resume by cursor / provider-keyed persisted session | none (raw event log) | none; **liveness-inference bugs** — no RAG (deliberately cut) |
| Letta | DB + **git-backed** markdown+YAML blocks | agent self-edit (LLM, **ungated**) | hybrid `conversation_search`; core always-in-context | sleeptime→reflection background | char-cap hard trim; **no archival dedup** (#3116) |
| Supermemory | cloud (CF) / immature self-host | extraction pipeline (**ungated**, LLM) | hybrid RAG+memory; `profile()` API | synchronous at write (contradiction resolve) | **content-derived temporal expiry** + supersede (retained) |
| Memongo | single MongoDB polymorphic collection | LLM extract + **surprisal novelty gate** | rankfusion hybrid + weighted rerank | "Dreamer" | **importance-based + permanent-exemption + explicit `Forget`** |
| MemPalace | verbatim files + vector + SQLite KG | verbatim hooks; **no-LLM** structural extract | semantic over raw; zero-LLM raw mode | **none (verbatim-always)** | none — append-only + **atomic supersede** + surgical purge |
| Superpowers | git-ignored scratch md + git log | controller append (convention) | `cat progress.md` tail | none | deleted with worktree |
| BMAD | append-only memlog + derived artifacts | **append-only tool (no edit/delete)**, blind-write | resume-by-tail; derive artifacts | derive-don't-edit render | none (run-scoped) |
| GSD | **mutable** STATE.md + structured stores | mutated in place; learnings **auto-copied** to CRUD store | read STATE.md; auto-inject learnings | reconcile / self-heal | `state sync` rebuild-from-filesystem |
| OpenViking | viking:// FS-paradigm, vector+RAGFS | hook-driven auto extract (**Layer-2 only, no agent-init**) | transparent auto-recall (RRF hybrid) | commit-driven extraction | hotness-tiering + temporal decay; **`merge_op` field immutability** |
| CrewAI | vector + Flow-state + checkpoint (3-layer) | **write-time LLM classification** (smart-writer) | adaptive-depth composite score | at write (contradiction detect) | `forget` op (hardening) |
| LangGraph | checkpoint DB + separate durable **store** | checkpoint auto/superstep; store explicit app-code (**no LLM**) | thread_id checkpoint / namespace store | none (mechanical) | **none — unbounded, no retention policy** |
| AutoGen/MagenticOne | Pydantic-serializable ledger | orchestrator self-writes turn-by-turn | consulted at every decision point | **re-derive on measured stall** | task-scoped, no carryover |
| Beads (`bd`) | **embedded Dolt (versioned SQL) canonical**; JSONL opt-in export only (v1.0.5+, 2026-05-28) | human/agent CLI (gated); every write auto-commits to Dolt | `bd prime` wholesale inject (now `--max-memories`/`--max-memory-chars` capped) + `bd ready` computed frontier | none at knowledge layer | `bd admin compact` — **permanent lossy** summarize of closed issues (human-in-loop `--analyze`/`--apply` default; Tier-1 30d shipped, Tier-2 90d planned) |

**Prose nuance.** (1) The "Semantic" column hides a fork: for mem0/Supermemory/Memongo/
CrewAI/OpenViking the semantic tier is *LLM-extracted*; for Claude Code/Codex/Archon/BMAD
it is *human-authored* (CLAUDE.md/AGENTS.md/project-context). The engine sits with the
second group. (2) "Decay: none" is not neutral — for Hermes and MemPalace it is a *named,
shipped consequence* (stale-memory complaint / accepted monotonic growth), not an
oversight. (3) The Process column is nearly empty on purpose: only MagenticOne and **Beads** treat
it as first-class — Beads is the survey's strongest *infrastructure* case for the type (a
shipped issue-graph with status/dependency-edges/typed close-reasons, orthogonal to and
separately stored from its own `bd remember` semantic store); the rest (Archon/GSD/BMAD/
Superpowers/CrewAI/LangGraph) carry run/checkpoint state that is process-shaped but framed
as orchestration, not memory. (4) Catch-all repos not
in the table but load-bearing below: **Gbrain** (markdown-git system-of-record → derived
Postgres, zero-LLM typed graph, write-back discipline — the closest external analog to the
engine's own substrate), **opencode** (`/learn` distills into the deepest applicable
AGENTS.md — file-based memory with zero new infrastructure), **Paperclip** (PARA files +
weekly synthesis pass + decay rules),
**ADK** (event-sourced session vs RAG memory as two consistency models), **deer-flow**
(write-behind summarize-after / inject-before with `<memory>`/`<soul>` prompt-tag
namespacing).

### 1c. Build-class classification (coding vs non-coding — the emerging axis)

A separate compact table (cheaper to maintain than a matrix column). Class is inferred
from each dossier's stated target and, tellingly, from the *shape its memory design took* —
memory visibly inherits the class it was built for. Full analysis in §9.

| Class | Frameworks | How the memory design inherited its class |
|---|---|---|
| **Coding-lifecycle** (repos / tests / reviews / tickets) | Claude Code, Codex, Beads, Superpowers, BMAD, GSD, Archon, Letta (→ Letta Code), opencode, gstack | Beads = ticket/issue-graph + `bd ready` frontier + typed close-reasons *because engineering*; Superpowers/BMAD/GSD = progress/run ledgers + resume-by-tail; Claude Code/Codex auto-memory = build-command/debug/convention notes ("use pnpm not npm," "tests need Redis"); Archon = event-sourced run history keyed by provider |
| **Personal / non-coding companion** (day-to-day life) | OpenClaw, Hermes, Paperclip | OpenClaw = daily-note journal (`memory/YYYY-MM-DD.md`) + `DREAMS.md` diary + `SOUL.md`/`USER.md` persona/profile on a *life cadence*, DM-vs-group visibility scoping; Hermes = `USER.md` "deepening model of who you are"; Paperclip = PARA + weekly life-synthesis |
| **Dual-use memory infrastructure** (framework-agnostic backend) | mem0, Supermemory, Memongo, MemPalace, OpenViking, Gbrain | Reveal their intended market through their *trace examples*: mem0 "lives in Berlin," Supermemory "moved to SF," Memongo "Company Brain" (non-coding business), MemPalace wings=people/rooms=topics — a conversational/personal skew even where the substrate is neutral |
| **Orchestration framework** (memory as a subordinate capability) | CrewAI, LangGraph, AutoGen/MagenticOne, ADK | Memory serves execution: checkpoint/store split (LangGraph), process ledger (MagenticOne), 3-layer persist (CrewAI), event-sourced session vs RAG (ADK) |

**Classification caveats (judgment calls, stated for honesty):** *Hermes* and *Letta* are
genuinely dual — Hermes carries a personal-companion framing (USER.md, "junior colleague
who never forgets") *and* coding skills; Letta's center of gravity shifted from
conversational agents to Letta Code (coding) mid-2026. Both are placed by their memory
design's *dominant* inheritance, not cleanly. The dual-use-infra row is classified by
example-traces (inferential), not by a hard product boundary.

---

## 2. De facto consensus (independently converged, 3+ frameworks, dated)

Ranked by strength of convergence.

1. **File-first canonical + index-as-accelerator (never index-as-store).**
   Converged: OpenClaw (markdown canonical, SQLite+embeddings explicitly downstream,
   2026-07 docs), Claude Code (five native markdown surfaces, 2026), MemPalace (verbatim
   files, ChromaDB/pgvector as index, v3.6.0 2026-07-14), Gbrain (git-markdown SoR, DB
   *derived* from git), Codex (AGENTS.md + markdown memories), opencode (learnings into
   AGENTS.md). **Six independent, VC-adjacent-to-solo scale range. Confidence: high.**
   Direct validation of the engine's markdown+git posture — the index, if ever built, is
   subordinate to the files.
   **Counter-example weighed (Beads):** Beads went the *opposite* way — since v1.0.5
   (2026-05-28) it demoted git-visible JSONL to an opt-in export and made embedded Dolt
   (versioned SQL) the sole canonical store. On its face this subtracts from the consensus.
   But its own dated evidence *strengthens* it: the entire severe-failure cluster (§4 #9 —
   daemon/database mismatch, `DATABASE MISMATCH DETECTED`, unmergeable primary-key forks
   across clones #4259, silent local-vs-git divergence) originates precisely in the opaque
   DB-vs-git sync layer that a directly-diffable plain-file store does not have, because
   there is no separate database to fall out of sync *with* git. Yegge's own 2026-07-06
   concession (the architecture is "sound," the implementation "plagued by critical bugs
   requiring constant fixes") corroborates. Recency-weighted read: Beads is a
   well-evidenced case that leaving the canonical store *behind* an opaque sync layer buys
   concurrency guarantees at the cost of a whole failure class — so for a single-operator
   engine it counts *for* file-first-canonical, not against it. **Net confidence: high,
   unchanged.**

2. **Append-write / resolve-at-read (append capture; correctness by ranking or
   supersession, never destructive overwrite).** Converged: mem0 (April-2026 pivot
   *removed* write-time UPDATE/DELETE → append + retrieval-time temporal resolution),
   BMAD memlog (no edit/delete subcommand exists), Superpowers progress ledger, MemPalace
   (append-only + atomic supersede, never delete), Supermemory (`updates` edge, old
   retained `isLatest:false`), Letta git-memory (append commits), ADK/LangGraph (event
   sourcing). **Seven+ independent, arrived from opposite motivations (audit vs compaction
   vs latency). Confidence: high.** *Load-bearing caveat carried forward:* pure append
   without an explicit supersession mechanism returns stale, confidently-cited facts
   (mem0 monotonic growth, Supermemory/MemPalace flagged bloat) — append is consensus,
   *append-plus-supersession* is the survivable form.

3. **Bounded, size-capped always-injected memory.** Converged: Hermes (2,200/1,375-char
   hard caps, 2026-07 re-confirmed), Claude Code (200-line/25KB MEMORY.md window), Codex
   (32KiB AGENTS.md, 8,000-char skill-metadata budget), OpenViking (two-threshold
   50%/70% compaction). **Four independent. Confidence: high.** Injection is a scarce
   budget mediated by a cap + curation step, not free.

4. **Progressive disclosure for procedural/skills (name+description at launch, body on
   invocation).** Converged: Claude Code, Codex (2%/8,000-char metadata), Hermes (~3K tok
   for ~100 skills), OpenClaw (53 SKILL.md). **Four independent, all 2026, cross-vendor
   open standard (agentskills.io). Confidence: high.**

5. **Externalize a durable surface as the resume mechanism; trust it over recollection.**
   Converged: Superpowers ("trust the ledger and git log over recollection"), BMAD
   (resume-by-reading-the-tail), GSD (STATE.md read at every workflow start), reinforced
   by Claude Code's survives-compaction re-injection guarantee. **Three-to-four
   independent. Confidence: high, scoped to working memory.** The convergence is on the
   *necessity* of an out-of-context durable surface, independent of its file shape.
   **Class note (refines confidence): this is a coding-class discipline.** All four sources
   are coding-lifecycle; "trust the log over recollection / resume-by-tail" is a
   compaction-and-crash-recovery habit inside a *work run*, not demonstrated in the personal
   corpus (OpenClaw externalizes daily notes but has no resume-by-tail contract). Read as
   **high within the coding class, unproven cross-class** — which is consistent with A1's
   Unknown-2 verdict being a coding-class phenomenon (§9).

6. **Async/background consolidation decoupled from foreground work.** Converged: Letta
   (sleeptime/reflection), OpenClaw (Dreaming), Hermes (reflect-after-N), Codex (idle-6hr
   batch), deer-flow (write-behind), Memongo (Dreamer). **Six independent. Confidence:
   high on the *decoupling*, low on the *cadence fit* for the engine** — every source is a
   high-frequency conversational/production agent (see §6, and A1 gap G2). The engine's
   session-close batch (`/self-improve`, `/session-handoff`) is the low-frequency analog,
   not a background daemon.
   **Class note: leans personal/companion.** Background consolidation is a long-lived-
   companion need (life journals must be periodically distilled — OpenClaw/Hermes/Letta/
   mem0); coding-class run-scoped memory needs it less (Superpowers deletes its ledger with
   the worktree — nothing to consolidate). Codex is the coding-class exception, and it is a
   *harness*, not a task-runner. See §9.

7. **Instruction/memory files degrade to soft hints without enforcement.** Converged:
   Codex (AGENTS.md "behaves more like a soft hint than a durable operating constraint,"
   #25884 2026-06-02; also #4466 2025-09-29, #6502 2025-11-11), Claude Code (context rot
   "single most common cause of perceived quality drops"; catastrophic CLAUDE.md-collapse
   risk), Hermes (stale memory outranks current reality, 2026-05-23), Archon (CLAUDE.md/
   AGENTS.md drift #2103 2026-07-14). **Four independent. Confidence: high.** A rule read
   once is not a rule applied for the session — enforcement must be code (hooks), not prose.

---

## 3. Contested / divergent (credible frameworks, opposite directions)

For each: which side is better evidenced under the recency rule, and the trade-off each buys.

1. **Write-time classification vs read-time resolution.**
   - Write-time: CrewAI (smart-writer LLM classifies scope/importance at save), Memongo/
     Supermemory (extract-at-write), mem0-*pre*-April.
   - Read-time: mem0-*post*-April (ADD-only, resolve at retrieval), Codex (grep at read),
     MemPalace (verbatim, all work at read).
   - **Better evidenced: read-time, on recency.** mem0's April-2026 pivot is the most
     recent, best-motivated datapoint — it *removed* write-time UPDATE/DELETE, citing
     halved extraction latency/cost, and CrewAI's own write-time design carries the
     matching failure (#2242: "saved fine, retrieved wrong" — encode errors invisible
     until a later failed recall). **Trade-off:** write-time buys richer recall metadata
     and cheap reads but makes bad classifications permanent-until-reprocess and silent;
     read-time buys robust cheap writes and no canonical-truth-maintenance burden but pays
     per-query cost and grows monotonically. *For the engine specifically:* write volume
     is low (governance entries, findings, handoffs — not chat-turn frequency), so a
     write-time LLM-classify step for e.g. auto-tagging findings is *affordable* where it
     is not for high-volume agents — this is the one place the engine can rationally take
     the minority side.

2. **Mutable state file vs append-only ledger.**
   - Mutable: GSD STATE.md (rewritten in place, recover by rebuilding from filesystem).
   - Append-only: BMAD memlog + Superpowers ledger (recover by trusting the log).
   - **Better evidenced against mutable: the append-only side, on cost of ownership.** GSD
     paid a recurring correctness tax — ~15 STATE.md parse/frontmatter bug-fixes across
     v1.28–v1.42 in two months — that the append-only repos structurally do not incur (no
     edit/delete subcommand ⇒ that bug class cannot exist). **Trade-off:** mutable buys a
     single compact router artifact and an in-place current-state view but needs
     `state validate`/`sync` self-healing tooling and drifts from disk; append-only buys
     crash-safety and drift-immunity but accretes (ledger bloat) and offers no in-place
     "where am I now" without reading the tail. *Note:* these recovery philosophies are
     incompatible — a spec must pick a side, not blend.

3. **Autonomous promotion vs gated promotion.**
   - Autonomous: Hermes (self-improve loop), OpenClaw (Dreaming, GA default-on),
     OpenViking (auto-capture), Codex (Memories generation).
   - Gated: the engine (human-gate, DD-29), Hermes `write_approval` (opt-in), Letta
     read-only blocks.
   - **Better evidenced: gated, decisively.** Hermes' self-rewrite-clobbers-good-work is
     *the single most corroborated failure in the entire survey* (independent practitioner
     blogs + the rebuild-video source + the shape of Hermes' own reactive mitigations,
     all triangulating). Its remediations (`write_approval`, `guard_agent_created`,
     `reset`) are all opt-in add-ons bolted on after the field noticed. **Trade-off:**
     autonomous buys zero operator friction and continuous accretion but incurs junk
     accumulation, self-rewrite clobbering, and persistence-attack surface; gated buys
     quality/auditability but costs operator throughput and risks cold-start under-
     promotion (OpenClaw's three threshold-gates can starve a true-but-rare fact). The
     engine's already-ruled `/self-improve` gate is validated, not challenged — Hermes'
     reports don't discriminate by stakes, so "trusted autonomous promotion for
     low-stakes writes" is not a safe relaxation.

4. **Verbatim storage vs extraction/curation.**
   - Verbatim: MemPalace (no LLM at write, ever), the verbatim-storage thesis.
   - Extraction: mem0, Supermemory, Memongo, CrewAI, OpenViking.
   - **Split by layer, not a winner.** Verbatim buys zero-LLM cost, citation-grade
     fidelity, and immunity to KB-poisoning, but cannot do relational reasoning
     ("similar text, not related facts" — OpenClaw's most consistent complaint) and grows
     forever. Extraction buys structure/relationships and compactness but adds LLM cost,
     opacity, and circular-reinforcement poisoning risk. **The KB's own resolution holds:
     keep the raw corpus (cold, citation) *and* a curated capped distillate (hot,
     injection)** — these are different layers, not competing architectures. mem0's
     verbatim baseline (96.6% R@5, zero LLM) plus the workload-alignment finding both say:
     keep raw, search it well, add extraction only where a named bottleneck justifies it.

5. **Single converged substrate vs typed/tiered separate stores.**
   - Converged (physical): mem0 scoped filter, Memongo single polymorphic collection, ob1
     single table, Beads single Dolt DB.
   - Split: LangGraph (checkpoint vs durable store), CrewAI (Memory/Flow-state/checkpoint
     3-layer), ADK (session vs RAG memory), Letta (core/recall/archival tiers).
   - **Both defensible; the engine's answer is "physically converged, logically split."**
     Converged buys operational simplicity (one backup, one query plane) but risks
     conflation — LangGraph explicitly warns durable knowledge stored in thread-scoped
     checkpoints gets pruned with the thread. Split buys clean consistency models but adds
     cognitive load (CrewAI forum threads). **Beads is the sharpest datapoint that the two
     axes are independent:** it unifies the *physical* substrate (one Dolt DB) yet still
     ships two *logically* distinct subsystems — the issue graph (process/work state) and
     `bd remember` (semantic facts) — with different write and decay rules. Even a tool
     marketed monolithically as "memory for coding agents" did not fold process and
     knowledge into one model. *For the engine:* one filesystem substrate (converged), but
     do not let session-scratch and durable findings share a lifecycle/retention policy
     just because both are markdown in the same repo (LangGraph's checkpoint-vs-store
     lesson, plus Beads' issue-graph-vs-`bd remember` split, applied to files).

6. **Semantic/embedding recall vs keyword/grep recall.**
   - Embedding: mem0, Supermemory, Letta, OpenViking, Memongo.
   - Keyword/grep: Hermes FTS5, Codex grep, MemPalace raw mode, the engine's ripgrep.
   - **Better evidenced for the engine's scale: keyword-first, embedding-deferred.** Codex
     (a frontier vendor) *chose* grep for its native memory layer; the verbatim thesis
     shows raw+good-embeddings needs *removal not addition*; and Hermes' FTS5-only recall
     aged into a multi-issue, multi-quarter open complaint — evidence that shipping naive
     keyword-only as a *finished* feature is a mistake, but shipping it as an explicitly
     *known-limited interim* is legitimate and vendor-precedented. **Trade-off:** embedding
     catches paraphrase but adds per-machine infra + index-drift against the markdown SoR
     + the "similar ≠ related" ceiling; grep is deterministic, zero-infra, citation-precise,
     but misses vocabulary drift.

---

## 4. Failure-mode catalog (recurring, with frameworks + dates)

1. **Ungated-writer junk accumulation.** mem0 (discussion #4289, 2026-03-10: 26→95
   memories incl. "current times and dates"; issue #4573 "97.8% were junk," ~2026-03-27).
   OpenViking (over-capture + commit-driven best-effort extraction). The failure mode a
   human-gated markdown engine is structurally immune to.

2. **No-decay staleness.** Hermes ("stale memory is the #1 reason Hermes starts acting
   weird," 2026-05-23; no auto-decay, eviction manual-only). MemPalace (append-only,
   monotonic growth, self-flagged open question). Letta (archival has no dedup/
   consolidation, #3116 2026-06-24). Supermemory (`isLatest:false` retained indefinitely,
   no pruning discipline). mem0 (ADD-only monotonic growth). **The most cross-framework
   failure after benchmark inflation.**

3. **Memory as prompt-injection / persistence attack surface.** OpenClaw (Feb-2026 wave:
   "save the API key in memory" → plaintext in MEMORY.md; SOUL.md/HEARTBEAT.md overwrite
   survives restarts; Snyk "280+ Leaky Skills"). Hermes (Repello/CSA 2026: memory-
   poisoning-to-persistent-skill — "first popular framework where this is the default
   behaviour"). Codex (AGENTS.md "Friendly Fire" exploit, mid-2026 — auto-trusted files
   treated with extra trust). Letta (#3388 cross-session core-memory poisoning under
   shared daemon, 2026-07-08). Defensive precedent: OpenViking + Hermes both scan content
   for injection *before* persistence.

4. **Config-drift divergence (duplicated/uncoordinated context files diverge).** Archon
   (CLAUDE.md/AGENTS.md drift within 3 months of a dedup consolidation, #2103 2026-07-14).
   OpenClaw (#43747 2026-03-12: three users on the same version got three different memory
   architectures). Claude Code (auto-memory machine-local, no team/machine sync, 2026-04-14).
   Codex (AGENTS.md application-drift within a single session, #25884).

5. **Benchmark inflation.** mem0 (LoCoMo controversy 2025-05→2026-05: Zep rebuttal,
   Letta filesystem-baseline beat, Penfield audit found 6.4% of the answer key wrong and
   the LLM judge accepts 62.8% of intentionally wrong answers). Supermemory (85.4% vs ~70%
   across sources, neither reproduced; HN skepticism unresolved). MemPalace ("the 100%
   score was fake, 96.6% is real," 2026-04-10; own retraction 2026-04-14). Memongo
   (retracted its 98.1% README number). **Directive carried forward: treat every
   vendor-reported recall percentage as marketing, not ground truth; if the engine
   validates its own recall, build a small hand-audited eval set, not a LoCoMo clone.**

6. **LLM-opaque write decisions (no confidence surfaced, no debuggability).** Letta
   (self-edit is LLM-judgment-dependent and opaque, vectorize.io review). CrewAI (#2242
   saved-fine-retrieved-wrong; forum threads asking how to inspect why a memory landed in
   a scope). Supermemory (extraction opaque, no confidence score on contradiction/
   relationship inference). mem0 (extraction filter over-collects silently).

7. **Instruction non-application (read ≠ applied).** Codex (#25884 2026-06-02 — the
   sharpest diagnosis: rules correctly *summarized* early, not *applied* later; #4466,
   #6502). Claude Code (context rot; catastrophic CLAUDE.md-collapse drops accuracy below
   the no-CLAUDE.md baseline). Hermes (stale entries outrank current reality).

8. **Liveness-inference false-forgetting / substrate corruption (bonus, engine-relevant).**
   Archon (#1216 2026-04-14: startup flips *all* running rows to failed, aborting live
   work — the cited precedent behind the no-autonomous-lifecycle-mutation principle; #1516
   2026-05-01 silent local-state destruction). Codex (#24089 2026-05-22 impossible token
   counts corrupt the compaction that depends on them; #29426). Letta (#3397 duplicate-
   label block silently rendered but unreachable). **Lesson: never auto-expire/auto-fail
   on a staleness guess — surface ambiguity to a human.**

9. **Multi-writer / multi-machine sync fragility (opaque-store-vs-git divergence).** Beads
   is the dossier'd case, and the pattern is dated across five independent accounts,
   2026-02→05: Reddit r/ClaudeCode (2026-02-17, worktree/merge-sync failures), Reddit
   r/codex (2026-03-05, embedded-Dolt build failure → forced self-hosted Dolt → port
   conflicts → "I stopped using beads"), dev.to (2026-04-30, `DATABASE MISMATCH DETECTED`
   + silent SQLite-vs-git divergence, "issues both exist and don't exist"), GitHub #4259
   (2026-05-29, `bd dolt pull` unmergeable after a per-clone `DEFAULT(UUID())` forked the
   dependencies-table primary key across clones), and the v1.0.4/1.0.5 bug window (JSONL
   auto-import overwriting live Dolt data). Yegge's own 2026-07-06 concession corroborates.
   **Every severe complaint traces to a multi-writer or multi-machine context** — no
   single-writer/embedded-mode account fails this way. **Lesson for the engine: this is a
   failure class a single-operator, directly-git-diffable markdown store does not have —
   there is no separate DB to diverge from git. Do not adopt DB-behind-sync plumbing to buy
   concurrency guarantees a single-operator engine does not need (see §6 D10).**

---

## 5. A1 verdicts revisited

### Verdict 1 — "per-actor AND shared over one scoped substrate" → **CONFIRMED, refined toward physical/directory isolation.**

The external survey independently reproduces the per-actor-and-shared model from four
directions: mem0's composable scope filter (`user_id`/`agent_id`/`run_id` on one store),
OpenViking's `account_id × user_id × agent_id` namespace isolation (a *second independent
instance* of scoped-single-store), Claude Code's native subagent `memory: user|project|
local` scoping, and LangGraph's namespace-scoped durable store separate from thread-scoped
checkpoints.

**The refinement:** filter-based isolation is *forget-prone*. mem0's #3998 (2026-02-08) is
a concrete production failure — agents defaulted to a shared `userId`, so a personal-
assistant's data bled into a healthcare-assistant's context, because the isolation was an
optional filter an implementer forgot to apply. Letta's #3388 (cross-session poisoning
under a shared daemon) is the same class. The engine's per-actor *directory* scoping
(Claude Code subagent memory dirs) sidesteps this by construction — physically separate
paths cannot be "forgotten." So the verdict stands, but the *mechanism* firms up: prefer
directory/physical per-actor isolation over an in-store scope filter; keep the shared
durable KB (research-findings) as one governed, write-gated substrate. This is a
scoping-and-write-permission decision, not a storage-topology one (A1's own framing,
now externally corroborated).

### Verdict 2 — "append-only run log as first accumulation surface" → **CONFIRMED for the working/run-log surface; REFINED to not extend append-only to the durable semantic layer.**

The process-repos dossier tested A1's two-repo convergence claim in depth and it survives
*narrower than "consensus" implied*: it is **2-of-3, not 3-of-3**. BMAD memlog and
Superpowers progress ledger genuinely converged on append-only / resume-by-tail / trust-
the-log, from opposite motivations, both actively maintained (BMAD v6.10.0 2026-07-03,
Superpowers v6.1.1 2026-07-02). mem0's April pivot independently corroborates append-write/
resolve-at-read at the mechanism level. **That part is solid — the run log is the right
first surface.**

**The refinement has two parts.** (a) GSD is not a near-miss — it is a *considered
opposite*: its Global Learnings Store (the only automatic cross-run semantic layer among
the three process repos) is explicitly structured CRUD, *not* append-only. There is no
cross-repo convergence on *any* mechanism for promoting working memory into durable
semantic knowledge — so do not extend the append-only default to a future learnings/
semantic layer without new evidence; the only concrete precedent (GSD) points the other
way. (b) Multiple frameworks (MemPalace, Supermemory, Letta, mem0) show append-only
*without* a supersession mechanism accretes stale, confidently-cited facts — matching
A1's own gap G4. Append-only is confirmed *paired with* an explicit supersession
mechanism (DD-44-style status field / MemPalace atomic supersede / Supermemory `updates`
edge), not as a bare growth-only log. **Caveat on GSD as a reference:** its upstream is
archived (governance collapse April–May 2026); the design lives on only in a community
fork under unproven stewardship — cite the *pattern*, flag the provenance.

---

## 6. Implications for the memory-spec ruling agenda

Recommendations with evidence chains. Nick rules.

**D1 — Per-actor vs shared scoping.** *Recommend:* one governed markdown+git substrate;
per-actor accretion via **directory isolation** (lean on Claude Code's native subagent
`memory:` scopes — zero new infra, each of Owner/Researcher/Codifier/Librarian gets a
`project`-scope dir today); shared durable knowledge (research KB) stays one write-gated
substrate; cross-actor sharing is opt-in, not default. *Evidence:* §5 Verdict-1 chain
(mem0 #3998 filter-leak, Letta #3388, OpenViking namespace, Claude Code native scoping).

**D2 — Accumulation surfaces.** *Recommend:* append-only run/progress log first (confirmed
§5-V2); the shipped `/self-improve` lesson store second (already live, `operations/self/`);
the frozen System Log as one-time bootstrap feedstock only; **do not** build standalone
tool-call telemetry (fold tool-call detail into run-log `event` entries — no survey
evidence supports it as an early standalone surface). *Evidence:* BMAD/Superpowers
convergence, `/self-improve` already shipped, A1 gap G1.

**D3 — Reflection mechanism shape (gated, auditable diary?).** *Recommend:* yes to a
**human-reviewable consolidation diary** — OpenClaw's `DREAMS.md` ("why this got promoted")
is a genuinely good idea *independent of* Dreaming's reliability problems: cheap to
produce, gives a lightweight audit trail without approving every write. But keep promotion
**gated per-batch**, not autonomous. Adopt Codex's **generate/use two-switch** as the
primitive — run "read-only" (validate what reflection would surface, without trusting it)
or "write-only" (deliberate capture that doesn't pollute live recall) independently; this
maps onto the engine's generator/assessor separation. *Evidence:* OpenClaw DREAMS.md +
Codex two-switch (positives), Hermes self-rewrite (the decisive negative), engine
human-gate / IB-176 promotion pipeline.

**D4 — Reflection cadence.** *Recommend:* **session-close / idle-triggered batch scan,
NOT a background sleeptime daemon.** Every cadence source (Letta, OpenClaw, Hermes, Codex,
Memongo, deer-flow) is a high-frequency conversational/production agent; none matches the
engine's episodic, human-gated, session-bounded profile (A1 gap G2). Codex's idle-6hr
*batch* is the compatible shape (reviewable before commit); Letta's sleeptime→reflection
churn + #3388 poisoning warn against background daemons sharing context across tasks. The
engine's `/self-improve` scan + `/session-handoff` reconcile-in-place already *are* this
pattern — extend them, don't add a daemon. *Evidence:* A1 G2, Codex idle-gate, Letta
sleeptime instability.

**D5 — Decay / demotion policy (Hermes's missing-policy lesson).** *Recommend:* decide
demotion/decay **explicitly and early** — Hermes shipped without it, the field noticed
within months, and retrofitting eviction onto a populated store is harder than designing
it in. Prefer **importance-based decay with a permanent/foundational exemption** (Memongo)
over wall-clock TTL, paired with **explicit supersession** (MemPalace atomic supersede /
Supermemory `updates` edge / the engine's DD-44 status field). Add **surprisal/novelty as
an upstream write-gate** (Memongo `mongodb-novelty.ts`) — "is this materially new vs
existing frontmatter" catches near-duplicate bloat before decay has to. *Evidence:* Hermes
"stale memory #1 complaint," Memongo importance-decay + surprisal, MemPalace supersede,
§4 failure-mode #2.
**Class analysis firms this recommendation up (the D-item that moves — §9).** Decay is a
*personal-class necessity* and a *coding-class nicety*: coding memory has an executable
oracle (tests/builds/`state sync` re-derive truth and catch staleness — GSD literally
rebuilds STATE.md from the filesystem), so a pure coding agent can lean on re-derivation.
The engine cannot: it runs a coding-*lifecycle* but its work product is governance/research
*knowledge*, which has **no oracle** — a stale DD or finding is unfalsifiable-by-machine,
exactly like a stale personal fact. So the engine inherits the personal class's staleness
problem *without* the coding class's self-correction, making explicit decay/supersession
**more** necessary here, not less. Weight D5 up.

**D6 — Write-permission constraints on auto-injected surfaces (security).** *Recommend:*
treat any file that is both (a) auto-loaded into every session and (b) agent-writable as a
**privileged-write / durable-persistence channel, gated like code** — not passive
documentation. The engine's git-versioning + human-gate already blocks the "agent silently
persists poisoned content, trusted on reload" pattern by a different mechanism, but the
survey surfaces one explicit gap to name in the spec: **scan content before persistence**
(Hermes and OpenViking both do this; the KB's current memory findings don't mention it).
*Evidence:* OpenClaw SOUL.md/HEARTBEAT.md persistence attacks, Hermes memory-poisoning-to-
skill, Codex AGENTS.md Friendly Fire, §4 failure-mode #3.

**D7 — Does "process memory" enter the taxonomy?** *Recommend:* **name it as a distinct
type, scope it minimally, and route it to E2 (task layer), not E1 — a recommendation Beads
now firms from "likely" to "confirmed."** Two independent lines converge. MagenticOne's
task/progress ledger supplies the *concept* — a serializable, inspectable "is the *task*
progressing" object distinct from what the agent knows, converged across the 2026 literature
and Microsoft's Azure guidance. **Beads supplies the shipped *infrastructure* proof:** a
25.4k-star tool whose whole differentiated contribution is a process-memory substrate —
issue status (`open/in_progress/blocked/…`), typed dependency edges, atomic lease-backed
claims, `bd ready` computed frontier, typed close-reasons — and which, despite being
marketed monolithically as "memory for coding agents," still ended up with *two structurally
different subsystems*: the issue graph (process/work state) and `bd remember` (semantic
facts), separately stored with different write and decay rules. That a builder motivated to
unify "agent memory" could not is strong evidence the type is real and structurally distinct
from knowledge memory — the thesis holds cleanly. **The E1-vs-E2 routing implication is now
concrete:** Beads' own internal split maps directly onto the engine's *existing* separation
of `project-management/implementation-backlog/` + `design-decisions/` (E2 — status-bearing
markdown, already carrying DD-44 supersession) from `knowledge/` + `research-findings/` (E1
— the knowledge layer). Beads does not argue for unifying these into one store; it argues
they should be **conceptually distinct with different write/decay rules**, which the engine
already has. So process memory belongs to **E2's work-item contract**, not E1's knowledge
memory. Keep it *light and human-reviewed* (MagenticOne's documented failure modes — false
stalls, ledger bloat, replan thrash — plus minimum-viable-abstraction discipline forbid an
autonomous per-turn version). *Evidence:* escalated §4 (AutoGen ledger + Azure guidance),
beads §5 (two-subsystem split, E1/E2 mapping), engine Occam's-razor rule.
**Class analysis reinforces (§9): process memory is a coding-class-only type.** It does not
appear anywhere in the personal/companion corpus (OpenClaw/Hermes/Paperclip have no issue-
graph/task-ledger/blocker-frontier equivalent) — it emerges only where work has tickets,
blockers, and reviews. The engine has that side (its coding-like lifecycle), and it lives on
E2's work layer — corroborating the E2, not E1, routing.

**D8 — Lean on Claude Code natively vs build.** *Recommend, lean on (free, compaction-
resilient, governance-compatible):* CLAUDE.md hierarchy, auto-memory, subagent `memory:`
scopes, and **hooks** (compaction-immune by construction — the right home for capture/
injection logic and content-scanning). Inherit the **proactive-compaction discipline**
(compact at a stable checkpoint with a hint, never at the hard cutoff — now first-party).
*Recommend, build (three native gaps):* (i) cross-machine/durable sharing — native
auto-memory is machine-local/unsynced, so the *repo-governed* files (PROGRESS/HISTORY/DDs)
remain the source of truth, exactly as Process Rule 2 already assumes; (ii) semantic
retrieval over episodic depth — Claude Code supplies none, and this is the biggest open
decision (see D9); (iii) cross-subagent knowledge pooling — file-mediated handoff, since
subagents don't share memory. **Do not** design any load-bearing mechanism around "Auto
Dream" (unconfirmed first-party). *Evidence:* claude-code dossier §5 bottom line.

**D9 — Recall mechanism (A1 gap G3, the single biggest deferred decision).** *Recommend:*
**deterministic ripgrep/grep over markdown as the interim; treat any embeddings layer as
explicitly known-limited and deferred.** Ship keyword recall as a *known-limited interim
state, not a finished feature* (Hermes' FTS5-only ages into a recurring complaint if
mislabeled "done"). If/when recall is built, follow the recall-ladder (hybrid keyword +
neighbor expansion + **citation** + **abstention**) rather than naive keyword-only, and
gate a depth policy so cheap queries stop early. *Evidence:* Codex chose grep (vendor
precedent), verbatim-thesis 96.6% R@5 zero-LLM, OpenClaw "similar ≠ related" ceiling,
Hermes FTS5 multi-quarter open gap, A1 gap G3 (embedding stack = per-machine maintenance +
index-drift against the markdown SoR).

**D10 — Portable ideas from Beads for the E2 task layer (adopt the query pattern, not the
plumbing).** *Recommend, adopt (low-cost, no new infra):* (i) a **computed-frontier query**
in the spirit of `bd ready` — the engine's IB items currently have no scripted "what's
unblocked right now" read distinct from a human scanning frontmatter status by hand; a
ripgrep/frontmatter-filter script that does the blocked/unblocked dependency reasoning is a
legitimately portable, database-free upgrade. (ii) **typed close-reasons and typed edges**
(`supersedes`/`duplicates`/`discovered-from`) — a real vocabulary for *how* work concluded,
directly analogous to and validating the engine's existing DD-44 supersession semantics;
cheap to add as IB/DD frontmatter fields. *Recommend, do NOT adopt:* Beads' **Dolt /
embedded-database / sync-daemon plumbing.** Its entire severe-failure class (§4 #9) lives in
the opaque DB-behind-git sync layer, which exists to solve *concurrent multi-agent-write
contention* — a problem a **single-operator** engine does not have. Adopting the substrate
would import the dominant failure mode to buy concurrency guarantees the engine doesn't need;
its own `bd admin compact` lossy decay likewise answers a Beads-specific constraint (bounded
local-DB size + wholesale `bd prime` injection budget) that a read-on-demand markdown store
with free lossless git/`archive/` scrollback does not share. *Evidence:* beads §5
transferability, §4 #9 failure cluster, DD-44/DD-55/DD-56 markdown-in-git commitment.

---

## 7. KB corrections ledger (collector-flagged staleness/errors)

One line each; source dossier in parentheses.

- **`dreaming-memory-consolidation.md` mis-attribution:** its Light/REM/Deep three-phase
  structure describes **OpenClaw** v2026.4.5, not Memongo — the finding lists a Memongo
  source in frontmatter but its body describes OpenClaw's Dreaming; only Memongo's
  `POST /v1/consolidate` entry point is independently confirmed. (memongo-mempalace §2)
- **mem0 watched-library docs stale on the April rewrite:** `watched-libraries/mem0.md`
  (v1.0.11, 2026-04-07) + analysis predate the April-2026 single-pass ADD-only extraction;
  their write/conflict-resolution description is superseded (structural/provider facts
  remain accurate). (mem0 §1)
- **Letta sleeptime finding stale after the reflection migration:** the internal analysis
  (2026-05-25) describes `SleeptimeMultiAgentV4` as current, but Letta had already migrated
  to client-side "reflection" subagents by #3294 (2026-04-08, v0.19.0) — "sleeptime" and
  "reflection" are the same lineage mid-rename; the code-level default is no longer sleeptime.
  (letta-supermemory, Letta §1)
- **GSD upstream archived → community fork:** `gsd-build/get-shit-done` is archived
  (`archived: true`, last push 2026-05-31, governance collapse + rug-pull); the design
  lives on only in `open-gsd/get-shit-done-redux` under new stewardship. Any spec citing
  GSD's STATE.md/Global-Learnings-Store must flag this provenance. (process-repos §GSD)
- **Memongo license stale:** `memongo.md` records "MIT licensed"; Memongo relicensed
  MIT→Apache-2.0 at v1.1.0 (2026-06-25). (memongo-mempalace §1)
- **OpenClaw watched-library entry misses three events:** the analysis (2026-04-08) does
  not reflect the OpenAI/Foundation transition (Feb 2026), Dreaming's GA promotion to
  default-on, or the February security-incident wave. (openclaw §1)
- **Supermemory internal analysis stale on self-hosted maturity:** the 2026-04-23 analysis
  predates the self-hosted server line (v0.0.3→v0.0.5) and its July-2026 data-loss-adjacent
  bug cluster (80 open issues). (letta-supermemory, Supermemory §1)
- **CrewAI internal analysis missed the "Cognitive Memory" rebuild:** the 2026-05-25
  analysis (v1.14.6) captured the resulting API but not the 2025 five-operation
  (encode/consolidate/recall/extract/forget) framing by name. (escalated §2.1)
- **`ledger-based-orchestration-stall-detection.md` still `raw`:** not yet synthesized/
  promoted; it is the KB's only process-memory finding. (escalated §4.1)
- **LangGraph checkpoint architecture "skipped: single-source":** the analysis deferred KB
  extraction; the escalation recommends reconsidering given E1's checkpoint-spec needs, and
  no external end-to-end capture of the checkpoint/store split exists. (escalated §3.1)
- **OpenViking pipeline not captured end-to-end:** sub-patterns are promoted individually
  (`hook-based-transparent-memory-injection`, `merge_op`, `two-threshold-compaction`,
  `three-tier-progressive-context-loading`) but no finding traces the SessionStart→
  UserPromptSubmit→Stop pipeline as one architecture. (escalated §1.1, other-repos-scan §4)
- **`production-memory-architecture-spectrum` undersells Superpowers:** it places
  Superpowers at level 1 ("no memory — context window only"); the v6 progress ledger is a
  partial revision — level 1 undersells the ledger's within-run durability. (process-repos
  §Superpowers)
- **openwiki absent from the 12-framework survey:** langchain-ai/openwiki (12.3k stars,
  CI-driven self-updating agent wikis + OKF concept format — direct E1 reflection-loop
  prior art) was not surveyed; registered as a watched library at the 2026-07-18 link
  intake. The survey's framework set should note the gap; a /repo-analyzer pass is the
  remedy. (2026-07-18 link-intake triage, batch D)
- **Pre-collapse applicability values on live findings:** `ai-delegated-knowledge-organization.md`
  and `para-based-file-memory.md` still carry `applicability: "S3 (Claude Code Build)"` —
  Claude Build is archived; current convention is `"IL (...)"` / `"General"`. Symptomatic
  of a wider pre-collapse-value sweep candidate. (2026-07-18 link-intake Pass 2, batch D)

---

## 8. Evidence-quality appendix (where the survey itself is weak)

Calibrate trust accordingly.

- **AutoGen/MagenticOne section is thin.** Its external grounding is a single
  `perplexity_ask` pass after two Deep Research timeouts — the process-memory taxonomic
  claim (the survey's one novel input) rests on lighter sourcing than the other escalated
  frameworks; treat "process memory as a fifth type" as a well-reasoned proposal, not a
  heavily-evidenced consensus. (escalated §4.1)
- **LangGraph sentiment is inferred, not observed.** No direct practitioner/issue-tracker
  sentiment was found; "sentiment" was inferred from documentation-warning emphasis and a
  conformance-suite CI run. Lower-confidence than the other three escalated frameworks
  (which had real GitHub-issue and forum voice). (escalated §3.4)
- **Perplexity timeouts forced gh/WebSearch fallbacks.** Letta+Supermemory ran entirely on
  WebSearch/WebFetch/HN-Algolia/`gh` CLI after repeated 5-minute timeouts on both providers;
  AutoGen fell back to a single ask pass. Where these dossiers cite live GitHub state
  (issue numbers, dates, repo stats) that is high-confidence primary data; where they infer
  sentiment it is thinner. (letta-supermemory intro, escalated §4.1)
- **"Auto Dream" (Claude Code) is unconfirmed first-party.** Documented across ~8 third-
  party blogs with consistent mechanics but *absent* from the first-party memory docs as
  fetched 2026-07-16; one source explicitly bills it as replicating an "unreleased" feature.
  Do not treat any Auto-Dream claim as load-bearing. (claude-code §1)
- **BMAD memlog is externally under-evidenced.** No dated 2026 practitioner commentary
  specific to memlog reliability/drift/bloat was found; the available HN praise predates the
  mechanism by ~9 months and is about BMAD generally. The append-only convergence rests on
  design-doc analysis + Superpowers' own incident report, not independent third-party
  confirmation at scale. (process-repos §BMAD, §convergence)
- **Hermes internal grounding was thin** (one 2026-05-24 analysis); several sentiment
  claims are aggregate-sourced without individually-confirmed publish dates (though the
  most load-bearing ones — the memory-attributed switching wave 2026-07-10, stale-memory
  2026-05-23, self-rewrite — are dated and multiply-corroborated). (hermes intro, §4)
- **All benchmark numbers are vendor-reported or disputed.** mem0, Supermemory, MemPalace,
  Memongo, and Letta figures are self-reported and/or contested across sources with no
  primary reproduction; §4 failure-mode #5 documents the pattern. Use none of them to set
  the engine's own evaluation approach.
- **Memongo is pre-audience** (29 stars, solo-maintained, quiet 19+ days at survey time) —
  a citable *design pole* (lifecycle-verb vocabulary, surprisal gate, importance-decay),
  not a dependency candidate; no external sentiment exists at all. (memongo-mempalace §4)
- **Codex Memories specifics are underspecified first-party** — the ~30-day pruning figure
  and Cloud retention are third-party (Mem0's competitive post); the feature is the "newest
  and least-settled surface" with active weekly "World State" churn. (codex §1, §2)
- **Beads is the best-sourced negative-evidence dossier in the survey** — its failure claims
  rest on dated first-party GitHub issues (#4259 2026-05-29), a live `gh api`/CHANGELOG read
  (2026-07-16), dated HN threads (2025-11-28, 2026-01-02, 2026-01-23), Reddit (2026-02-17,
  2026-03-05), dev.to (2026-04-30), longitudinal blogs (llbbl 2026-06-27), and the creator's
  *own* 2026-07-06 concession — a rare case of vendor-corroborated practitioner complaints.
  **One calibration caveat:** two of the abandonment accounts (dev.to daemon/SQLite framing;
  the 2025-11 trial) describe pre- or early-Dolt-migration builds, not the current v1.1.0
  architecture — the sync-fragility *class* is real and multi-sourced, but not every specific
  bug maps to the shipped-today store. Also note the task brief's premise ("JSONL-in-git
  canonical") described Beads' pre-v0.55 design; current Beads is Dolt-canonical, JSONL an
  opt-in export — the internal `beads-analysis.md` already had this right (no internal drift),
  and the KB's earlier misattribution of "semantic decay" to Beads was already corrected.
  (beads §intro, §4, §5)
- **The §9 coding-vs-non-coding analysis is a re-analysis of existing dossiers, not new
  collection** — no dossier ran a controlled head-to-head coding-vs-personal comparison, so
  every class contrast is cross-dossier inference. Specific soft spots: the coding/personal
  line is fuzzy for the dual-use-infra row (classified by example-traces, inferential);
  Hermes and Letta are genuinely dual (judgment-call placement); the "process memory absent
  from the personal corpus" finding is an *absence of evidence* (strong because the personal
  dossiers are detailed, but still an absence, not a proof of impossibility). The
  oracle-availability contrast (§9-b) is the best-grounded claim; the cadence and
  security contrasts are real but partially shared across classes (stated as such, not
  overstated).

---

## 9. Coding-agent vs non-coding-agent memory (the emerging class axis)

Nick's hypothesis: memory solutions built for coding agents (repos/tests/reviews/tickets)
are diverging from those built for personal/non-coding companion agents (running someone's
day-to-day life), and the distinction will matter. Tested against the corpus below.

**Verdict: CONFIRMED, with two pushbacks.** The axis is real and the divergence is
sharpest exactly where Nick predicted — verification and process state. But the classes
*converge* on substrate mechanics (file-first, append-write, bounded injection, instruction-
drift), and one shared primitive (preference memory) shows up identically in both, so the
distinction is second-order structure over a shared base, not two disjoint worlds. Classes
in §1c.

### The class differences (from dossier evidence)

**(a) What gets remembered.** *Coding:* decisions ("Stripe over PayPal"), conventions
("use pnpm"), build/test commands, repo state, work-item status, dependency edges, typed
close-reasons (Beads, Superpowers/BMAD/GSD ledgers, Claude Code/Codex auto-memory examples
are all literally build/test/convention facts). *Personal:* identity, preferences,
relationships ("Alice manages the auth team"), dated life events ("moved to Berlin/SF,"
"exam tomorrow"), profile (name/pronouns/timezone) — OpenClaw `USER.md`, Hermes `USER.md`,
mem0/Supermemory life-fact traces.

**(b) Ground-truth / verification — the deepest and best-evidenced difference.** *Coding
has an oracle.* Tests/builds/CI can validate whether a remembered fact is still true:
Superpowers' and GSD's verifiers are explicitly told *not* to trust the summary and to
check the actual codebase (goal-backward); GSD's `state sync` *rebuilds* STATE.md from the
filesystem; MemPalace's no-LLM extractor records verifiable code symbols/paths; Beads'
`bd ready` computes deterministically from the dependency graph. *Personal has no oracle.*
"User lives in NYC" vs "moved to SF" can only be falsified by the user — which is *why* the
personal/infra class invested in temporal reasoning (mem0), content-derived expiry
(Supermemory "exam tomorrow"→expires), and contradiction detection: machinery built to
compensate for the missing executable check. Hermes ("stale memory outranks current
reality") is the personal class failing precisely at the point where coding would have
self-corrected. **This is the class distinction that matters most for design.**

**(c) Session cadence / lifetime.** *Coding:* task/run-scoped — Superpowers = one SDD run
per worktree (ledger deleted with it), BMAD = one run-folder, GSD = project roadmap,
Archon = per-run; memory lifetime is bound to a work unit, with "landing the plane" gates.
*Personal:* long-lived companion, continuous — OpenClaw daily notes accrete indefinitely;
Letta "one agent per project, infinitely lived, no more compactions"; the Hermes switching
thesis is explicitly "competing against the session model itself." *Pushback:* not binary —
coding *harnesses* (Claude Code/Codex) carry durable cross-session convention memory too;
the real coding trait is a **sharp ephemeral/durable split** (run log vs CLAUDE.md), where
personal memory is one accreting journal.

**(d) Decay / staleness — what "stale" even means differs by class.** *Coding:* stale =
contradicted by current code; detectable and correctable by re-derivation; discarded with
the work unit — so decay pressure is *lower*. *Personal:* stale = the world changed and
nobody told the agent; undetectable without user input — so decay is a *necessity*, and the
class that skipped it (Hermes) got "stale memory is the #1 reason it acts weird." Decay is a
personal-class necessity, a coding-class nicety (see D5).

**(e) Security exposure.** *Personal:* holds secrets/PII, always-on, multi-channel — broad
blast radius (OpenClaw API-keys-in-MEMORY.md, SOUL.md/HEARTBEAT.md persistence attacks;
Hermes memory-poisoning-to-persistent-skill "first framework where this is the default").
*Coding:* narrower blast radius (a repo) but a supply-chain surface (Codex AGENTS.md
"Friendly Fire," write-to-repo). *Pushback:* the underlying failure mode — auto-loaded +
agent-writable = persistence channel — is **shared, not class-specific**; only the exposure
profile (PII/always-on vs repo/supply-chain) differs. D6 holds for both classes.

**(f) Which types dominate — and does process memory exist for personal agents?** *Coding
class:* process memory (Beads, MagenticOne, the three process-repo ledgers), procedural
(skills/formulas), semantic-as-conventions (CLAUDE.md/AGENTS.md). **Process memory does not
appear anywhere in the personal corpus** — OpenClaw/Hermes/Paperclip have no issue-graph,
task-ledger, or blocker-frontier equivalent. It is a coding-class-only type (see D7).
*Personal class:* semantic (identity/preferences), episodic (life events), working, with
rich relationship/entity modeling (Supermemory graph). *Telling signal:* the dual-use infra
(mem0/Supermemory/Memongo) skews personal in its *trace examples* — direct corroboration of
G5 below.

**(g) Where the classes converge anyway (this refines the §2 confidence labels).** Checking
each consensus item across both classes: **#1 file-first, #2 append-write/resolve-at-read,
#3 bounded injection, #7 instruction-drift all hold CROSS-class** (each has coding *and*
personal exemplars) — genuinely class-independent, confidence stays high. **#5 externalize-
durable-surface/trust-the-log is coding-class-specific** (all four sources are coding-
lifecycle; the resume-by-tail contract has no personal exemplar) — high within the coding
class, unproven cross-class. **#6 async consolidation leans personal/companion** (life
journals need periodic distillation; coding run-scoped memory needs it less). So: the two
classes *diverge on what/why/how-long* but *converge on the storage substrate mechanics* —
which is why this axis reshapes the type taxonomy and decay policy far more than it reshapes
the substrate decision.

### Where the hypothesis is weaker (don't overstate)

- **Preference memory is a shared primitive.** "User prefers TypeScript" is the canonical
  lifecycle-trace example in *both* classes (OpenClaw, mem0, Memongo, Letta, Codex all use
  a TS/JS preference) — the primitive is identical; only the second-order structure around
  it diverges.
- **The security failure mode is shared** (see (e)) — class changes the exposure, not the
  mechanism.
- **The substrate consensuses hold cross-class** (see (g)) — the classes are not disjoint
  worlds; they share the file-first/append/bounded-injection base.

### Placing our engine on the axis, and the D-item impact

The engine is a **hybrid**: it runs a rigorous engineering-*lifecycle* (specs, human gates,
git, DDs, verify-before-build) but its *work product* is governance/research/knowledge — not
code — and it is single-operator and long-lived (Nick is the perpetual operator). The
precise diagnosis: **a coding-lifecycle wrapper around oracle-free (personal-class) content.**

*Coding-class lessons that transfer:* process/ticket state → E2 (IB items + DD-44); the
append-only run log → the first accumulation surface (D2); the sharp ephemeral/durable split
(session-scratch vs durable findings, D8/LangGraph). *Personal-class lessons that transfer:*
long-lived operator-preference memory (Nick's standing preferences — literally the auto-
memory items already in the system prompt); always-on cross-session accumulation; injection-
surface security (auto-loaded CLAUDE.md/rules = the persistence channel, D6). *Single-
operator:* no multi-writer contention, so the personal class's always-on continuity fits and
the coding class's team/sync problems (Beads §4 #9, Claude Code no-team-sync) do not apply.

| D-item | Class-sensitive? | Effect on the recommendation for us |
|---|---|---|
| **D5 (decay/demotion)** | **Yes — moves.** | Because our knowledge is oracle-free (personal-class trait), we cannot rely on coding-style re-derivation to catch staleness. Explicit decay/supersession is **more** necessary, not less. **Weight D5 up.** |
| **D7 (process memory → E2)** | Yes — confirms. | Process memory is coding-class-only; it lives on our coding-lifecycle side, i.e. E2. Reinforces E2-not-E1 routing. No direction change, added evidence. |
| **D2 (run log first surface)** | Yes — confirms. | The append-only run log is a coding-class artifact; appropriate because we run a coding-like lifecycle. No change. |
| **D9 (grep vs embedding recall)** | Mild. | Coding-class grep precedent (Codex) is the closer analog for our process/governance recall; personal-class embedding recall serves relationship/paraphrase queries we have *less* of — but *more* of on the research-KB side. Firms grep-first for process/governance; leaves embedding as a research-recall maybe. No move. |
| **D6 (injection-surface security)** | No. | Failure mode is shared across classes; our exposure is coding-class (repo/supply-chain), covered by git-gate + single-operator. No change. |
| D1, D3, D4, D8, D10 | No. | Not class-sensitive in a way that changes the recommendation. |

**Net: exactly one D-item moves — D5 firms up** (decay is more necessary for us, not less,
because we combine a coding lifecycle with oracle-free content). D7/D2/D9 gain confirming
class evidence without changing direction. A1 verdicts and all other recommendations are
untouched — the class analysis sharpens *why* the existing calls are right for a hybrid
engine; it does not overturn any.

### Tie to A1 gap G5 (workload-alignment)

A1's gap G5 warned that the memory benchmarks (LoCoMo/LongMemEval) are conversational/
personal-agent-centric, so coding-agent memory "may have bottlenecks the suite doesn't
measure." **This class dimension is G5's qualitative answer.** It identifies *what* those
unmeasured bottlenecks are: process/work-state memory, verification-backed convention memory,
and run-log recovery — none of which a personal-fact-recall benchmark measures. So the
dimension **resolves the direction of G5**: coding-agent memory is dominated by types
(process, procedural, verifiable-semantic) that the conversational benchmarks structurally
ignore, which is why their scores can't be used to pick the engine's structure. **What it
does *not* resolve — still needs measurement:** the engine's *specific* hybrid bottleneck
(oracle-free governance knowledge under a coding lifecycle) is measured by *no* existing
benchmark of either class. The engine still needs its own small, hand-audited eval set
(echoing §4 failure-mode #5's directive) — the class analysis tells us which *kind* of
memory to evaluate, not how well ours performs.
