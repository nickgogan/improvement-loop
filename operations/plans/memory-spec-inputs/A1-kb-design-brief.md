---
title: "A1 — KB Design-Input Brief for the E1 Memory-Architecture Spec"
author: Librarian (Builder mode)
date: 2026-07-16
consumes: PRD §E1 (governance/prd.md); IL research-findings memory cluster
status: design-input (read-only synthesis; not a decision)
---

# A1 — KB Design-Input Brief: E1 Memory & Knowledge Layer

**Scope.** Citation-grounded design input for the `memory-spec`, targeting the two
open unknowns named in PRD §E1: (1) per-actor vs shared store shape, and (2) which
accumulation surfaces to start with. Every claim below cites a research-findings
filename. Where the KB does not answer a spec question, section 5 says so — that list
drives a conditional external gap-check.

**Note on inputs.** Of the five files PRD §E1 names as the memory cluster,
`rebuilt-hermes-memory-in-claude-code` is a **research-source**, not a finding
(`research-sources/rebuilt-hermes-memory-in-claude-code.md`); its evidence reaches this
brief through the findings that cite it (`bounded-tiered-memory-inference-driven-curation.md`,
`memory-cross-layer-promotion-governance.md`, `session-history-import-as-memory-bootstrap.md`).
The other four resolve as findings and are cited directly.

---

## 1. What the research says about the two open unknowns

### Unknown 1 — per-actor vs shared store shape

The KB does not treat this as a binary. It converges on **one governed substrate,
scoped by actor, with per-actor isolation as the default access pattern and
cross-actor sharing opt-in** — i.e. per-actor *and* shared, not per-actor *or* shared.

**Evidence pushing toward a single shared substrate (not N separate stores):**
- `converged-memory-substrate-vs-patchwork.md` — all memory types (working, semantic,
  episodic, procedural) should be *access patterns over one governed store*, not a
  patchwork of point solutions; the patchwork creates infrastructure sprawl, sync
  complexity, and governance fragmentation. It explicitly names the engine's own
  filesystem (grep/glob/read over markdown) as a legitimate *lightweight convergence* —
  one substrate, multiple access patterns.
- `scoped-memory-model.md` (mem0) — the crispest statement of the reconciliation:
  memories carry composable scope dimensions (`user_id` / `agent_id` / `run_id`); a
  *single store with filterable dimensions* handles per-agent, per-session, and shared
  cases without separate storage per combination. "Composability is the key design
  insight."
- `database-as-shared-memory-coordination.md` — shared versioned store as a
  coordination substrate for concurrent agents (queryable state, conflict resolution),
  but this is filed under Orchestration and speaks to *task* coordination more than
  durable knowledge memory.

**Evidence pushing toward per-actor isolation (as scoping, not separate infra):**
- `subagent-persistent-memory-directory.md` — **Strong evidence (first-party Anthropic
  canonical spec)** and the most decisive finding for this unknown, because it is native
  to the exact runtime the engine uses: a Claude Code subagent declares
  `memory: user|project|local` and gets its own persistent directory
  (`~/.claude/agent-memory/{name}/` etc.), auto-preloaded (first 200 lines / 25 KB of
  `MEMORY.md`) with an auto-curation instruction. This gives each actor
  (Owner/Researcher/Codifier/Librarian) a private, git-trackable accretion surface with
  scope-appropriate sharing — for free, no database.
- `memory-bank-isolation-per-agent-per-project.md` — isolation must be first-class:
  agents sharing one bank pollute each other's recall; cross-scope recall should be
  *opt-in, not default*. Maps directly onto the engine's existing system-scope
  boundaries.
- `scoped-memory-model.md` again — enforces isolation by scope filter; the silent
  failure mode is *omitting* a scope filter and leaking cross-scope results.

**The governance constraint that decides the seam:**
- `agent-memory-architecture-multi-agent-layered.md` — shared layered memory
  (working/episodic/semantic/procedural) decouples agents and makes state auditable, but
  its named failure mode is decisive: *shared memory without access control lets one
  agent's noise pollute another's context.*
- `memory-cross-layer-promotion-governance.md` — "not every agent can write to shared
  semantic memory"; writes to durable shared tiers must be policy-gated with ownership.

**Verdict on Unknown 1.** Route by the trichotomy (`memory-wiki-world-kb-trichotomy.md`):
the **durable shared knowledge** (the research KB / domain wiki, and a world-KB layer if
one is ever built) is *shared* substrate under unified governance and write-gating; each
**actor's private working/episodic accretion** (encounter logs, classification
heuristics, source-triage patterns) is a *per-actor scoped directory* — Claude Code's
native subagent memory is the ready mechanism. Promotion from per-actor private memory to
shared durable knowledge is policy-gated (section 3). The filesystem is already a
converged substrate, so "per-actor vs shared" is a *scoping and write-permission*
decision, not a storage-topology one.

### Unknown 2 — which accumulation surfaces to start with

PRD §E1 lists candidate surfaces: session runs, tool calls, session logs. The KB ranks
them clearly by evidence.

- **Start with the append-only run/progress log** (session runs + decisions +
  completions). `append-only-run-log-as-working-memory.md` is **P1** and the *only*
  memory-accumulation surface with **independent cross-repo convergence** (BMAD `memlog`
  + Superpowers progress ledger), arrived at from opposite motivations (decision
  auditability vs compaction recovery). Its payoff is concrete and immediate:
  resume-by-reading-the-tail and recovery of "the single most expensive failure
  observed" — controllers re-dispatching completed work after compaction. This is the
  session-runs surface, and it subsumes tool-call/decision granularity as log `event`
  entries.
- **The lesson store is already shipped and extends naturally.**
  `append-only-lesson-store-owning-surface-identity.md` (**P1**, production evidence from
  CareerBuddy) is the failure-observation surface; the engine already runs it as
  `operations/self/` via `/self-improve` (IB-176). E1 "extends the shipped loop from one
  system-level store to a designed layer" — so this surface is live, not greenfield.
- **Bootstrap the reflection layer once from session logs.**
  `session-history-import-as-memory-bootstrap.md` — don't start the store empty; distill
  existing history at setup. This validates the ruled plan-of-record: mine the frozen
  System Log corpus once (cheap-model bulk pass), route the residue, then close it as a
  read-only archive. Transferable mechanics: cheap-model (Haiku-tier) summarization for
  the bulk pass, and **keep the raw corpus for citation** rather than discarding after
  distillation.
- **Tool-call telemetry as a *standalone* first surface is NOT evidenced.** No finding
  argues that separately capturing tool-call streams pays off before the run log / lesson
  store. Tool-call-level detail is best carried as `event` entries inside the run log
  (`append-only-run-log-as-working-memory.md`), not as its own early surface. (Gap — §5.)

**Verdict on Unknown 2.** First surface = the **append-only run/progress log**
(P1, cross-repo convergence, compaction-recovery payoff). The **lesson store** is already
live and is the second surface by default. **Session logs** are the one-time bootstrap
feedstock for reflection, not an ongoing capture surface. **Standalone tool-call
telemetry: defer** — fold tool-call granularity into the run log.

---

## 2. Store shape & write/read mechanics

**Append-only vs mutable — use both, at different layers.**
- Append-only for the ledger, lesson, and raw layers:
  `append-only-run-log-as-working-memory.md` (no edit/delete subcommand exists; blind
  write-only during a session with a JSON echo so the agent never re-reads its own
  history mid-run; no lifecycle status field — state is learned by reading the tail;
  atomic temp+fsync+rename writes). `append-only-lesson-store-owning-surface-identity.md`
  (recurrence appends a date to the *existing* entry keyed by (owning surface, failure
  pattern) — never a duplicate; status lifecycle open→promoted/declined/pruned; pruning
  is a status change, never a deletion; git is the archive).
- Mutable curated distillate for the always-injected hot layer:
  `bounded-tiered-memory-inference-driven-curation.md` (**Strong, production-tested**) —
  hard character ceilings on always-loaded memory, inference-driven writes, and a
  Curator that dedup-then-replaces on overflow favoring most-recent high-confidence
  facts. This is the hot/warm/cold split: **hot** = size-capped curated snapshot loaded
  verbatim each session; **warm** = retrieved prior-session snippets; **cold** = raw
  archival transcripts.

**Write-time vs query-time synthesis — prefer query-time / structure-over-prose to avoid
KB poisoning.** `write-time-vs-query-time-synthesis-kb-poisoning.md` — LLM-authored
summaries re-indexed alongside originals create circular reinforcement disconnected from
ground truth; its three principles are *immutable originals*, *structure over prose*
(extract verifiable relationships/citations, not narrative), and *query-time synthesis*
(synthesize fresh from originals). The engine's findings already approximate this
(evidence_strength + source backlinks = chain of custody), and `memory-recall-ladder`'s
citation stage depends on the raw corpus surviving. Note the tension with write-time
distillation (section 5).

**Injection — size-cap is load-bearing, not optional.**
`memory-system-evaluation-triad-storage-injection-recall.md` — injection is "what loads
automatically at session start"; its caution is that the axes are *not orthogonal* — an
aggressive storage policy degrades injection (snapshot bloat) unless a cap + curation
step mediates. The bounded-tiered ceilings (`bounded-tiered-memory-...md`) are exactly
that cap.

**Recall — staged ladder, and it is the parked axis.**
`memory-recall-ladder-staged-deepening-with-citation-and-abstention.md` — recall as a
five-stage ladder: hybrid (semantic + keyword) search → rerank → neighbor/context
expansion → **cite** (exact words, who decided, date) → **abstain** when nothing clears
the bar. `memory-system-evaluation-triad-storage-injection-recall.md` scores recall as
the *weak axis* of the current generation (keyword-only search silently fails on synonym
queries) and names it the engine's one open component. The citation + abstention stages
are what make recall trustworthy enough to inform governed decisions — "memory is a
hint, not an authority" requires knowing where the hint came from. A depth policy
(cheap queries stop at stage 1–2) is recommended to avoid a fixed five-stage tax.

**Verbatim vs extraction for the read path — workload-dependent, favors keeping raw.**
`verbatim-storage-thesis-for-memory.md` (raw words + good embeddings reach 96.6% R@5 with
zero LLM, matching/beating extraction systems on retrieval recall — "the key insight is
removal, not addition") vs `no-single-memory-architecture-workload-alignment.md`
(no architecture dominates; pick by workload bottleneck; retaining original content beats
added abstraction, and heavy structure costs orders of magnitude more without
proportional accuracy gains). Both point the same way for a citation-grounded engine:
**keep the raw corpus, search it well**; add extraction/structure only where a specific
bottleneck justifies it. `four-tier-agent-memory-model-with-write-policy.md` supplies the
governing rule: "Long context is not memory. A vector store is not automatically memory
either" — memory is a deliberate read/write *policy* (extract candidate → classify →
policy-check → attach provenance → write with TTL/confidence; re-rank on read by recency
+ source reliability + relevance).

**Framing to adopt in the spec vocabulary.**
`memory-vs-rag-product-distinction.md` — RAG retrieves stateless document chunks; memory
tracks stateful facts derived from interaction. The engine implicitly splits these
(`research-findings/` = RAG-style corpus vs per-actor private state) but does not name
it; naming it is a near-free vocabulary upgrade. `llm-statelessness-as-a-superpower-agent-memory-fi.md`
reframes the design goal: because responses are generated purely from the loaded context,
memory is not about *fighting* forgetfulness but about *curating the input state* — which
is exactly what a size-capped injected snapshot + on-demand recall is for.

---

## 3. Reflection — turning accumulated data into knowledge

**Mechanism: write-back at decision time, promotion policy-gated between tiers.**
- `write-back-discipline-memory-is-not-the-brain.md` — the habit that makes a store
  accumulate value: durable calls made in-session are *written back* as pages at decision
  time (Gbrain's five rules: search first, answer from pages, write decisions back, cite
  everything, "memory is not the brain"). Skip write-back and every decision rots in
  session history findable only by conversation search. The engine already practices the
  general form (session decisions → DDs and findings, not chat residue).
- `memory-cross-layer-promotion-governance.md` — promotion between tiers
  (working→episodic→semantic) is *the highest-risk operation*; each must be policy-gated
  with explicit ownership, approval level, and rollback path; episodic→semantic happens
  only when knowledge "truly changed." This is the exact shape of the engine's shipped
  `/self-improve` promote mode (draft → shadow-sandbox → fresh-context grade → per-proposal
  Nick gate) and independently corroborates generator-assessor separation.

**Routing by shape** is the engine's own ruled behavior and the PRD acceptance
criterion: reflection outputs route decision→DD, pattern→`knowledge/`, work→task layer
(`append-only-lesson-store-owning-surface-identity.md` implementation notes; PRD §E1).

**Cadence: async/background consolidation, converged across three repos.**
`sleeptime-background-memory-agent.md` — decouple reflection latency from foreground
work: a background "sleeptime" agent consolidates asynchronously at configurable
frequency (3-repo convergence: Letta sleeptime, OpenClaw dreaming, Hermes
reflect-after-N-tasks). `memory-decay-compaction-convergence.md` decomposes cadence into
three facets solved by different repos — *when* (dual thresholds), *how often* (weekly
synthesis cycles), *where* (per-thread scoped persistence) — and notes naive
FIFO/truncation loses too much, so consolidation must be semantically aware.

**Bulk bootstrap pass:** `session-history-import-as-memory-bootstrap.md` — cheap-model
(Haiku-tier) summarization for the one-time distill over the frozen SL corpus, preserving
raw transcripts for later citation-grade recall.

**Reflection failure modes to design against:** write-back without supersession
accumulates contradictory decision pages that get confidently cited
(`write-back-discipline-memory-is-not-the-brain.md`); over-promotion of noisy events
pollutes durable memory, under-promotion causes repeated misses
(`memory-cross-layer-promotion-governance.md`); cheap-model distillation is lossy over
exactly the corpus you'll never re-read, so the raw archive must stay reachable
(`session-history-import-as-memory-bootstrap.md`); background consolidation can race
foreground writes and reorganize memory in ways that confuse the next foreground turn
(`sleeptime-background-memory-agent.md`).

---

## 4. Decay / compaction / health — keeping the store from rotting

**Write-time gate (upstream) + decay (downstream) are complementary.**
- `surprisal-novelty-as-memory-write-gate.md` — an information-theoretic *write-path*
  filter: score each candidate's novelty against the existing corpus; high-novelty →
  write, low-novelty → merge or drop. Catches near-duplicate bloat ("User prefers JSON"
  written 40 times) *before* it enters the store, where decay can't help because none of
  the duplicates is old. Importance answers "does this matter?"; surprisal answers "is
  this new?" — a mature store needs both.
- `importance-based-decay-permanent-exemption.md` — decay relevance by *importance
  score*, not wall-clock TTL; `permanent`/`ongoing` tags are a first-class escape hatch
  for identity-level memory that must never decay; low-signal content is crowded out by
  retrieval competition rather than deletion. Its caveats: importance-score provenance
  and staleness, permanent-tag abuse, and unbounded growth with no hard TTL.

**Compaction is semantically aware, multi-strategy.**
`memory-decay-compaction-convergence.md` — combine threshold-triggered timing (when),
periodic consolidation (how often), and scoped persistence (where); the missing piece
across the observed repos is the "what to keep" importance-scoring dimension.
`memory-cross-layer-promotion-governance.md` gives per-tier demotion policy: working =
strict token budget + compact each session; episodic = months retention with
importance/recency GC; semantic = small, curated, years; governance = append-only by
policy.

**Growth-bounding and ceilings (from the shipped/production patterns).**
`append-only-lesson-store-owning-surface-identity.md` — pruning is a *status change,
never a deletion*; ~50-open-lessons pruning trigger; git is the archive.
`bounded-tiered-memory-inference-driven-curation.md` — hard character ceilings
(e.g. 2,200 / 1,375 chars) with a Curator that evicts on overflow. **Caveat:** these
thresholds are borrowed from other systems and are not yet validated for the engine (§5).

**Health / the deterministic store check (PRD acceptance criterion).**
`append-only-lesson-store-owning-surface-identity.md` supplies the model: the shipped
`/self-improve` store has a deterministic `store_check.py` that flags PROMOTE and
enforces schema (an untraceable lesson "is invention and gets no entry"). The PRD's
"deterministic store check exists and a seeded violation fails it" maps onto extending
this checker to the new layer. The missing-fourth-axis observation in
`memory-system-evaluation-triad-storage-injection-recall.md` (the triad omits
*curation/forgetting*; storage is treated as write-only) is the right frame for what
store-health must cover: supersession and forgetting, not just growth.

**The append-only-plus-supersession requirement.**
`no-single-memory-architecture-workload-alignment.md` warns that pure append-only stores
"return stale facts, leading to hallucinations of the past" on knowledge-update
workloads, and that graph/temporal organization handles revisions best. Since the engine's
own profile is closest to *cross-session aggregation + knowledge-update* (per that
finding), append-only capture must be paired with an explicit supersession mechanism —
not just a growth bound.

---

## 5. Tensions and gaps

### Contradictions the spec must resolve (surfaced, with both sides)

1. **Verbatim vs extraction/curation.** `verbatim-storage-thesis-for-memory.md` (keep
   exact words, no LLM extraction) is filed as a direct *contradicts* of
   `bounded-tiered-memory-inference-driven-curation.md` (LLM curator, hard ceilings,
   evict) and of `triple-storage`/`agentic-search` extraction poles.
   `no-single-memory-architecture-workload-alignment.md` and
   `four-module-agent-memory-decomposition.md` reconcile it as workload-dependent and
   module-separable. **Resolution the KB points to:** keep the raw corpus for citation
   (cold layer) *and* maintain a curated capped distillate for injection (hot layer) —
   the hot/warm/cold split already in `bounded-tiered-memory-...md`. These are different
   layers, not competing whole-architectures.

2. **Write-time vs query-time synthesis.**
   `write-time-vs-query-time-synthesis-kb-poisoning.md` favors immutable originals +
   query-time synthesis and is marked *contradicts* against automatic-fact-extraction and
   agentic-search; yet `session-history-import-as-memory-bootstrap.md` and
   `bounded-tiered-memory-...md` both rely on write-time (cheap-model) distillation.
   **Resolution:** distillation is allowed as a *navigation aid* over immutable,
   source-linked originals — never as a replacement that gets re-indexed as new ground
   truth.

3. **Converged single substrate vs the trichotomy's separate stores.**
   `converged-memory-substrate-vs-patchwork.md` (one store, many access patterns) vs
   `memory-wiki-world-kb-trichotomy.md` (three stores, distinct ingestion paths). The
   trichotomy finding itself notes converged designs "collapse the trichotomy into
   access patterns." **Resolution:** logically distinct (route each datum to the right
   store by kind) but physically shareable (one filesystem substrate, scoped) — which is
   also the Unknown-1 verdict.

4. **Isolation vs cross-pollination.** `memory-bank-isolation-per-agent-per-project.md`
   and `scoped-memory-model.md` warn that shared banks pollute recall; both also warn the
   *opposite* — over-isolation creates knowledge silos where a lesson learned by one
   actor is invisible to another. The spec must set the default (isolate) and the opt-in
   cross-actor path deliberately.

### Spec questions the KB does NOT answer (drives the external gap-check)

- **G1 — Tool-call accumulation surface.** No finding argues that a *standalone*
  tool-call telemetry surface pays off, or how to structure one. The KB only supports
  tool-call detail as `event` entries inside the run log. If the spec wants first-class
  tool-call memory, that is an external gap-check.
- **G2 — Reflection cadence for a human-gated, low-frequency single-operator governance
  engine.** Every cadence finding (`sleeptime-background-memory-agent.md`,
  `memory-decay-compaction-convergence.md`) is drawn from high-frequency
  conversational/production agents with async background workers. None addresses the
  engine's actual profile: episodic, human-gated, session-bounded. Whether a background
  "sleeptime" agent even fits (vs a scan run triggered at session close, which is what
  `/self-improve` already does) is unanswered by the KB.
- **G3 — Whether to build semantic recall at all.** The recall ladder
  (`memory-recall-ladder-...md`, P3, Not Yet Started) requires a local embedding stack
  (PGlite + pgvector), which its own failure-modes section flags as per-machine
  maintenance and index-drift risk against the markdown source of truth.
  `memory-system-evaluation-triad-storage-injection-recall.md` names recall as *parked*
  in the engine. The KB describes the design but does not answer whether the engine
  should build embeddings-based recall or stay with deterministic grep/glob over
  markdown. This is the single biggest open design decision the KB defers.
- **G4 — Concrete supersession mechanism for a markdown store.** Multiple findings flag
  that append-only + write-back without supersession accumulates contradictory,
  confidently-cited stale facts (`no-single-memory-architecture-workload-alignment.md`,
  `write-back-discipline-memory-is-not-the-brain.md`,
  `memory-system-evaluation-triad-...md`'s missing fourth axis), but none gives a concrete
  supersession mechanism for a markdown/git store beyond the engine's existing DD-44
  status-field pattern. Whether DD-44-style supersession generalizes to the memory layer
  is unvalidated.
- **G5 — Coding/governance-agent memory bottleneck.**
  `no-single-memory-architecture-workload-alignment.md` explicitly states its benchmark
  suite is conversational-agent-centric and that coding-agent memory (repo state, plans,
  governance) "may have bottlenecks the suite doesn't measure." The workload-alignment
  rule therefore *cannot be applied* to pick the engine's structure, because the engine's
  bottleneck isn't in the measured taxonomy.
- **G6 — Validated store-health thresholds.** The concrete numbers in the KB (~50-open
  pruning trigger; 2,200 / 1,375 / 2,500-char ceilings) are borrowed from CareerBuddy and
  Hermes (`append-only-lesson-store-owning-surface-identity.md`,
  `bounded-tiered-memory-inference-driven-curation.md`), not derived for the engine's
  corpus. They are starting points, not answers.

---

## Appendix — findings consulted (27)

Core cluster (PRD-named): `memory-system-evaluation-triad-storage-injection-recall`,
`memory-recall-ladder-staged-deepening-with-citation-and-abstention`,
`session-history-import-as-memory-bootstrap`,
`append-only-lesson-store-owning-surface-identity` (+ source
`rebuilt-hermes-memory-in-claude-code`, a research-source).

Store shape / per-actor-vs-shared: `converged-memory-substrate-vs-patchwork`,
`scoped-memory-model`, `memory-bank-isolation-per-agent-per-project`,
`subagent-persistent-memory-directory`, `database-as-shared-memory-coordination`,
`typed-shared-memory-handoff-slots`, `agent-memory-architecture-multi-agent-layered`,
`memory-wiki-world-kb-trichotomy`, `memory-vs-rag-product-distinction`,
`four-tier-agent-memory-model-with-write-policy`, `verbatim-storage-thesis-for-memory`,
`no-single-memory-architecture-workload-alignment`,
`four-module-agent-memory-decomposition`,
`llm-statelessness-as-a-superpower-agent-memory-fi`.

Write/read mechanics & reflection: `append-only-run-log-as-working-memory`,
`write-time-vs-query-time-synthesis-kb-poisoning`,
`write-back-discipline-memory-is-not-the-brain`,
`memory-cross-layer-promotion-governance`, `sleeptime-background-memory-agent`.

Decay / compaction / health: `importance-based-decay-permanent-exemption`,
`memory-decay-compaction-convergence`, `surprisal-novelty-as-memory-write-gate`,
`bounded-tiered-memory-inference-driven-curation`.
