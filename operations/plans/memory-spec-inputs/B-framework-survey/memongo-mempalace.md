---
title: "B — Framework Survey: Memongo & MemPalace"
author: Researcher (cross-framework survey)
date: 2026-07-16
consumes: watched-libraries/memongo.md, watched-libraries/analysis/memongo-analysis.md, watched-libraries/mempalace.md, watched-libraries/analysis/mempalace-analysis.md, KB findings citing either project, live GitHub state (2026-07-16)
status: design-input (read-only synthesis; not a decision)
---

# B — Framework Survey: Memongo & MemPalace

**Scope.** Design-input dossier for the E1 memory-architecture spec, surveying the
engine's two memory-focused watched libraries. Internal grounding is the KB
(`watched-libraries/{memongo,mempalace}.md`, their `analysis/` docs, and every
`research-findings/` entry citing either project). External grounding is a live
check of both GitHub repos (API metadata, releases, commits, current README /
CHANGELOG / HISTORY / benchmark docs) plus targeted web search for practitioner
commentary, run 2026-07-16. Both projects are small relative to the engine's
other watched libraries; external coverage is proportionate, not exhaustive —
where a claim has no dated external corroboration, this dossier says so rather
than padding.

**Recency note.** The KB's last full analysis passes were 2026-04-20/04-22
(Memongo) and 2026-04-23 (MemPalace) — roughly three months stale relative to
today. Both projects moved meaningfully in that window (Memongo shipped its
first public release; MemPalace shipped three minor versions). Every claim
below is dated; where KB evidence and live-repo evidence conflict or the KB is
silent, this is flagged explicitly rather than silently overwritten — the KB
itself is out of scope to edit here (this task is read-only outside the one
dossier file).

---

## Part 1 — Memongo

### 1. Snapshot

MongoDB-native long-term memory framework, sole-maintained by `romiluz13`.
KB intake (2026-04-20) described it as a "MongoDB-native long-term memory
framework for AI agents" at pre-audience scale (1 GitHub star). Live repo
state as of 2026-07-16 (`gh api repos/romiluz13/Memongo`):

- **29 stars, 3 forks, 4 open issues** — still functionally pre-audience
  despite a public release in the interim.
- **License changed MIT → Apache-2.0** at the v1.1.0 release (2026-06-25).
  The KB's `memongo.md` still records "MIT licensed" — this is now stale.
- **First public npm release, v1.1.0, 2026-06-25**: six packages published
  (`@memongo/lib`, `memory-engine`, `memory-bridge`, `memory`, `client`,
  `tools`), plus a Cloudflare Workers landing/console deployment
  (`memongo.rom-88f.workers.dev`).
- **Repositioning**: README and framework docs now describe Memongo as a
  "MongoDB-native **Company Brain** memory framework for AI apps, agents,
  and teams" — broadened from the April framing ("long-term memory for AI
  agents") to explicitly include non-coding-agent use cases (customer
  support, sales, product ops). "Company Brain" is corroborated as a real,
  actively-contested 2026 industry term by independent market-survey pages
  (e.g. vectorize.io's "Brain Stack" piece, 2026) — several startups are
  racing to define it — though none of those pieces name Memongo.
- **Activity has gone quiet since launch.** Last commit 2026-06-27
  ("docs: define memory framework"); `pushed_at` is 2026-06-27, i.e. no
  commits in the ~19 days before this dossier (2026-07-16), following a
  concentrated launch-week burst (2026-06-24/25/27).
- Currency of this section: live GitHub API + repo-file reads, 2026-07-16.
  KB structural analysis (`memongo-analysis.md`) is from 2026-04-22 and
  covers only three companion docs at Pass-2 depth; this pass does not
  redo a full structural analysis, only verifies the memory-architecture
  surface and checks for drift.

### 2. Memory model by type

Memongo now publishes an explicit **memory taxonomy and lifecycle-verb
contract** (`apps/docs/concepts/framework.mdx`, read 2026-07-16) that is
more structured than what the April KB intake captured — the April finding
set describes conversation turns / session evidence / userfact evidence /
QA evidence inside one polymorphic collection; the current docs frame the
same substrate as six typed memory kinds (episodic events, semantic facts,
procedures, profile preferences, workspace knowledge, provenance) behind
six lifecycle verbs (**Recall, Context bundle, Remember, Update, Forget,
Feedback, Trace**) and a six-level scope model (`session` / `user` /
`agent` / `workspace` / `tenant` / `global`). This is a real architectural
delta since April, not just copy — a `Forget` verb (explicit lifecycle
delete) did not appear in the April intake at all.

- **Working / short-term.** Scoped to `session`. No separate short-term
  buffer is described; "working memory" is effectively the context bundle
  assembled per-turn via `/v1/context-bundle` / `memongo_build_context_bundle`,
  not a distinct storage tier.
- **Episodic.** First-class type ("episodic events"), written via
  `/v1/write-event`. Stored in the single `chunks` collection using
  MongoDB's `$jsonSchema` `oneOf` polymorphic validator alongside the other
  evidence types (`mongodb-single-store-polymorphic-evidence-memory.md`).
- **Semantic.** "Semantic facts" + "workspace knowledge" + "profile
  preferences." Written via `/v1/write-structured`. Populated at ingest by
  a lightweight LLM (GPT-4-mini) that extracts structured facts and QA
  pairs from every incoming turn (`structured-fact-extraction-from-conversations.md`).
- **Procedural.** First-class type ("procedures"), written via
  `/v1/write-procedure`, revised via lifecycle update endpoints — the only
  one of the four canonical types MemPalace does *not* have an equivalent
  for (see Part 2 §2).
- **Storage substrate.** One MongoDB `chunks` collection, polymorphic
  schema; 29 collections / 84 standard indexes / 14 search indexes total
  per the April structural pass (not re-verified at file level this pass —
  flagged as unconfirmed-current).
- **Write path.** Turn arrives → GPT-4-mini structured-fact + QA-pair
  extraction → **surprisal-based novelty gate** (`mongodb-novelty.ts`)
  scores the candidate against the existing corpus; low-novelty candidates
  merge into an existing memory or are dropped, high-novelty candidates
  write as new (`surprisal-novelty-as-memory-write-gate.md`).
- **Injection / recall.** Query decomposed by GPT-4-mini into sub-queries →
  parallel fan-out across `$vectorSearch` (Voyage 4 Large auto-embed) and
  Atlas `$search` (lexical) → native `$rankFusion` / `$scoreFusion` merge →
  weighted post-retrieval rerank (quoted-phrase 0.60, temporal 0.40,
  entity 0.40, keyword-overlap 0.30) → packaged into a context bundle for
  prompt injection (`query-decomposition-sub-query-rrf-merge.md`,
  `rank-fusion-hybrid-retrieval-mongodb-atlas.md`,
  `post-retrieval-reranking-weighted-signal-composition.md`).
- **Consolidation / reflection.** A background "Dreamer" process
  (`mongodb-consolidator.ts` → `POST /v1/consolidate`) is named in
  Memongo's own docs. **Caveat on KB grounding:** the KB finding filed
  under this pattern (`dreaming-memory-consolidation.md`) describes a
  specific three-phase Light/Deep/REM structure, but its own body text
  attributes that structure to a *different* watched library (OpenClaw
  v2026.4.5), not to Memongo, despite listing the Memongo source in its
  frontmatter. This dossier does not carry the Light/Deep/REM structure
  forward as a confirmed description of Memongo's Dreamer — only the
  entry point (`POST /v1/consolidate`) is independently confirmed.
- **Decay / forgetting / supersession.** Importance-based decay via
  `computeImportanceDecay()` — no wall-clock TTL; memories tagged
  `permanent` or `ongoing` are exempt entirely
  (`importance-based-decay-permanent-exemption.md`). **Still open as of
  this pass:** importance-score *provenance* (fixed at write time vs.
  recomputed) is undocumented — the same gap the April intake flagged is
  still unresolved in the current docs. New since April: an explicit
  **Forget** lifecycle verb (lifecycle-delete endpoints / MCP tools) gives
  users/apps an explicit removal path alongside automatic decay — this
  did not exist in the April surface.

### 3. Lifecycle trace

*User says, mid-session: "I prefer TypeScript and concise release notes."*

1. Turn hits the ingestion path (`/v1/add`-equivalent). GPT-4-mini extracts
   a structured fact — `{type: preference, text: "user prefers TypeScript
   and concise release notes", involving: [User]}` — and a QA pair.
2. `mongodb-novelty.ts` computes surprisal against the nearest neighbors
   already in `chunks`. If a near-duplicate preference fact exists, it
   merges; otherwise it writes as new.
3. The candidate is written into `chunks` as a `userfact`-type evidence
   document (polymorphic `oneOf` schema), auto-embedded on write via
   Voyage, indexed for both `$vectorSearch` and Atlas `$search`.
4. An importance score is assigned (mechanism still undocumented — see
   §2). No `permanent`/`ongoing` tag is applied unless the fact is
   flagged as identity-level.
5. Later, the user asks "what does the user prefer?" — the query is
   decomposed, fanned out through `$rankFusion`, RRF-merged across
   sub-queries, reranked by the four weighted signals, and returned as a
   context bundle injected into the agent's prompt.
6. In the background, the Dreamer periodically consolidates evidence.
   Importance-based decay applies over time unless the fact is
   permanent/ongoing; if the user later retracts the preference, an
   explicit `Forget` call can remove it — otherwise it persists
   indefinitely (no TTL).

### 4. Practitioner sentiment

**No independent external sentiment was found.** Despite the 2026-06-25
public npm launch, targeted web search (2026-07-16) for "Memongo" reviews,
opinions, or comparisons returned nothing specific to the project — general
2026 agent-memory landscape surveys (mem0, Zep, Letta, LangMem, Hindsight)
do not mention it. This is consistent with the repo's own metrics: 29
stars, no GitHub Discussions enabled, 4 open issues, sole maintainer.

The one dated, substantive signal is **self-authored, not external**:
Memongo's own team produced a forensic methodology audit of MemPalace's
public benchmark claims (`docs/benchmarks/mempalace-forensic-audit.md`,
dated 2026-05-11) — a 12-point neutralization checklist (dataset SHA,
retrieval-unit disclosure, NDCG, embedding-model disclosure, per-case
outputs, no un-pinned competitor estimates, etc.) explicitly modeled on
MemPalace's own self-disclosed "teaching to the test" episode. By
2026-06-24 (`docs/benchmarks/BENCHMARKS.md`, "Last reviewed: 2026-06-24"),
Memongo had rewritten its own benchmark page to match that discipline: the
April intake's headline "98.1%" R@5 number is explicitly retracted
("No old `98.1%` README number is used"), replaced with narrow,
unit-labeled rows quoting Memongo's own reproduction of MemPalace's
retrieval-lane numbers (e.g. LongMemEval raw session R@5: Memongo 99.15%
vs. MemPalace 96.60%, labeled "Scoped retrieval win"), and an explicit
refusal to claim a win over Mem0 ("The latest full judged rehearsal
remained below Mem0's committed top-50/top-200 rows. That work is
preserved privately... and should not be used as launch marketing.").
This is evidence of *rigor*, not of *adoption* — it says nothing about
whether anyone outside the maintainer is using Memongo.

### 5. Verdict

**Strengths.** Single-store polymorphic architecture keeps operations
simple (one backup, one query plane). Native MongoDB Atlas `$rankFusion`
avoids app-side hybrid-retrieval plumbing. The lifecycle-verb contract
(Remember / Recall / Update / Forget / Feedback / Trace) plus the
six-level scope model is a clean, general memory API shape. The
benchmark-claim discipline matured substantially between April and June —
from an unlabeled README number to a forensic-audit-driven, unit-labeled,
self-limiting claim set — directly mirroring the discipline the engine
wants for its own eval work.

**Failure modes.** Importance-score provenance is still undocumented three
months after the gap was first flagged — a real, unaddressed design hole.
Single MongoDB collection is a single point of failure; the stack requires
MongoDB Atlas + Voyage embeddings + a small LLM in the write path, which is
materially heavier infrastructure than a markdown+git substrate. The
project is solo-maintained and effectively pre-audience even post-launch
(29 stars, quiet for 19+ days as of this writing) — real continuity risk
for anything built to depend on it. The Dreamer consolidation process's
internal structure is not independently confirmed at the depth this
dossier would want (KB source-attribution gap, §2).

**Transferability to a markdown+git, single-operator, human-gated
engine.** The *lifecycle-verb vocabulary* (remember/recall/update/forget/
feedback/trace) and the *scope model* (session/user/agent/workspace/
tenant/global) are the most portable ideas — they describe a governed
memory API independent of MongoDB, and map cleanly onto Actor-scoped
memory (per `A1-kb-design-brief.md`'s per-actor-and-shared conclusion)
without requiring a database. The write-time novelty gate (surprisal) and
importance-decay-with-permanent-exemption are both conceptually portable
to a git-diff-based store (e.g. "is this content materially new relative
to existing frontmatter/findings" and "never prune anything tagged
foundational"). The retrieval stack itself ($rankFusion, Voyage
embeddings, GPT-4-mini decomposition) is not portable — it requires
MongoDB Atlas infrastructure the engine doesn't run. Net: adopt the
*vocabulary and governance pattern*, not the *stack*.

---

## Part 2 — MemPalace

### 1. Snapshot

Local-first, verbatim-storage AI memory, org-owned (`MemPalace` GitHub org;
founders Milla Jovovich, Ben Sigman, Igor Lins e Silva, plus a large
contributor base). Tagline: "the best-benchmarked open-source AI memory
system. And it's free." Live repo state as of 2026-07-16
(`gh api repos/MemPalace/mempalace`):

- **57,399 stars, 7,399 forks, 627 open issues** — up from ~49k stars at
  the KB's 2026-04-23 analysis (v3.3.2), roughly +8.4k stars (~17%) over
  ~3 months. Still growing, at a lower rate than the initial viral week.
- **Extremely active.** Latest tagged release **v3.6.0 shipped
  2026-07-14** (two days before this dossier); hotfix PRs merged the same
  day as this research (2026-07-16, e.g. #2027, #2034). `pushed_at` is
  2026-07-16T22:08Z.
- **Storage backends expanded** since April: ChromaDB-only →
  ChromaDB + Milvus (embedded/self-hosted/Zilliz Cloud) + Qdrant +
  pgvector (v3.5.0/v3.6.0), each behind the same `backends/base.py`
  pluggable interface the April analysis already flagged as a notable
  pattern.
- **MCP tool count grew 29 → 36.** New harness surfaces added:
  `.antigravity-plugin/`, `.cursor-plugin/` alongside the original
  `.claude-plugin/` / `.codex-plugin/` — the "single authored-once
  instruction source, N thin plugin wrappers" pattern now covers four
  harnesses instead of two.
- **New in v3.6.0:** opt-in local write daemon (serializes background
  mines/diary-saves/hook-ingests through one process instead of racing
  for the palace handle) and opt-in HTTP transport for the MCP server
  (loopback-default, DNS-rebinding guard, optional bearer token) — aimed
  at team/remote deployment, a use case the April analysis's "single-agent
  internal" framing did not anticipate.
- **No new `docs/HISTORY.md` retraction entries since 2026-04-14**,
  despite three minor version bumps (v3.4, v3.5, v3.6) — read as a signal
  the April correction cycle's claims discipline has held, though this
  pass did not re-audit every current headline number against source.
- Currency of this section: live GitHub API + repo-file reads (README,
  CHANGELOG, HISTORY, BENCHMARKS.md, releases, commits), 2026-07-16. KB's
  full 5-dimension structural analysis is from 2026-04-23 (v3.3.2); this
  pass does not redo a full structural analysis.

### 2. Memory model by type

- **Working / short-term.** No distinct architectural tier. Session
  start injects recent context via `mempalace wake-up` / `mempalace_status`
  (documented in the agent SKILL.md session protocol); MemPalace relies on
  the host harness's own context window plus on-demand retrieval, not a
  separate short-term store.
- **Episodic.** No first-class typed "event" object (contrast Memongo).
  The nearest analogues are (a) per-agent **diaries**
  (`mempalace_diary_write`/`read`) and (b) verbatim **drawers** tagged
  with `authored_at` — v3.6.0 added true transcript-authored-time
  metadata distinct from ingest time, plus tie-breaking toward
  more-recently-authored content on score ties. Episodic in the sense of
  "dated, session-scoped verbatim record," not a distinct typed schema.
- **Semantic.** The local SQLite **knowledge graph**: typed
  entity-relationship facts with temporal validity windows. v3.5.0 added
  **atomic fact supersession** (`supersede()` /
  `mempalace_kg_supersede`) — closes an open fact and opens its
  successor at one shared instant, replacing what was previously a
  manual invalidate-then-add operation that could race. This is
  MemPalace's most semantic-memory-like layer and the piece that changed
  most substantively since April.
- **Procedural. Explicitly not handled as a first-class type.**
  Confirmed by direct grep of the current `CLAUDE.md` and `README.md`:
  no "procedure" concept appears anywhere in the memory model. This is
  architecturally consistent with the verbatim-always design principle —
  synthesizing a procedural abstraction from raw sessions would itself be
  a lossy-extraction step, which CONTRIBUTING.md explicitly rejects.
  "How we do X" knowledge lives only as verbatim drawers plus whatever
  the knowledge graph captures as entities/relationships, not as a
  distinct procedural memory.
- **Storage substrate.** Pluggable backend interface, default ChromaDB;
  now also Milvus, Qdrant, pgvector (see §1) — all "raw text + embedding"
  stores; none add schema polymorphism the way Memongo's single collection
  does.
- **Write path.** Verbatim ingestion via `mempalace mine` (manual) or the
  `Stop`/`PreCompact` background hooks (automatic); a precision-biased,
  **no-LLM** structural extractor (new in v3.6.0) records code symbols,
  URLs, paths, and qualified identifiers to populate the graph. No
  LLM-based fact extraction or summarization ever runs at write time —
  the core, still-unchanged design invariant.
- **Injection / recall.** Semantic search over raw drawers (default
  ChromaDB embeddings), scoped by wings (people/projects) and rooms
  (topics). Optional heuristic hybrid boosts (keyword overlap, temporal
  proximity, regex-based preference-pattern extraction) and optional LLM
  rerank (Haiku/Sonnet) lift the benchmark ceiling; raw mode needs zero
  LLM calls end to end.
- **Consolidation / reflection.** None, in the autonomous-reflection
  sense. No background re-scoring, no theme extraction, no sleep-cycle
  analogue. "Consolidation" here is purely mechanical capture (the hooks
  file what happened), never model-driven synthesis — a direct
  consequence of the verbatim-always principle.
- **Decay / forgetting / supersession.** No decay mechanism. Append-only
  / incremental-only is a stated non-negotiable design principle (a crash
  mid-operation must leave the existing palace untouched). Deletion is
  narrow and surgical, not policy-driven: v3.5.0 added
  `mempalace_delete_by_source` specifically to purge mined
  benchmark/eval contamination (drawers *and* their index entries) —
  not a general forgetting policy. Superseded knowledge-graph facts are
  closed (temporal end-date) rather than deleted, so historical/temporal
  queries against them still resolve.

### 3. Lifecycle trace

*User tells the agent, mid-session, that they changed employers from
Company A to Company B.*

1. The turn happens in the chat window; no in-band save action is
   required from the model.
2. At `Stop` (or `PreCompact`), the hook fires: counts human messages
   since the last save (threshold 15); once met, it auto-mines the raw
   JSONL transcript directly into the palace — capturing tool output and
   text regardless of what the model would have chosen to summarize —
   tagged with wing (the person), room (topic), and `authored_at`
   (transcript time, not ingest time, since v3.6.0).
3. The same hook call returns `{"decision":"block","reason":"save tool
   output verbatim..."}`, coercing the model into an explicit save turn:
   it writes a diary entry and, recognizing the employer change as a
   structured fact, calls `mempalace_kg_supersede` to atomically close
   the "Company A" fact and open "Company B" at one instant.
4. `stop_hook_active` flips true on the model's second stop attempt;
   the hook returns `{}` and the session ends — the infinite-loop guard.
5. On a later session's wake-up, the new employer fact resolves via
   `mempalace_kg_query`; the original verbatim conversation is still
   retrievable via `mempalace_search` if the agent needs the *why* behind
   the change (context the KG fact alone doesn't carry).
6. The old "Company A" fact is never deleted — only closed with a
   validity end-date — so a query like "who did they work for last year"
   still resolves correctly against history.

### 4. Practitioner sentiment

Dense, dated, largely first-party-community rather than trade-press:

- **2026-04 launch week.** Viral: ~19.5k stars in the first week,
  front-paged on Hacker News
  ([HN item 47672792](https://news.ycombinator.com/item?id=47672792)) as
  "MemPalace, the highest-scoring AI memory system ever benchmarked" —
  read by the community as validation of retrieval-first,
  non-summarizing memory as a design stance.
- **2026-04-07/08.** A critical independent technical review (gist,
  "mempalace-critical-review.md") found real, dated bugs at that
  version — `collection_name` config silently ignored, `mempalace init
  --yes` still prompted interactively and crashed, `pyproject.toml`
  vs. `__init__.py` version mismatch (3.0.0 vs 2.0.0) — alongside praise
  ("a real OSS tool, not vaporware," installs cleanly, retrieval "delivers
  useful results on realistic datasets"). Verdict at the time: 7/10 as
  usable software, 4/10 as a rigorously presented research story.
- **2026-04-10.** danilchenko.dev published "MemPalace Review: The 100%
  Score Was Fake. 96.6% Is Real." — external corroboration, independent
  of MemPalace's own retraction, that the community treated 96.6% as the
  honest number and 100% as inflated.
- **2026-04-14.** MemPalace's own `docs/HISTORY.md` records the
  full-surface benchmark-table retraction (already captured in the KB's
  `retraction-log-as-governance-artifact.md` finding) — the team's
  response to the above criticism was public correction, not dispute.
- **2026-04-30 → 2026-05-13.** GitHub Discussion #1277 ("Will MemPalace be
  updated to scale?") raised scaling doubts — "small-project bias," no
  BEAM/ultra-long-context benchmarks, weaker entity resolution versus
  Hindsight/Supermemory. Maintainer `jphein` responded (2026-05-11/13)
  pointing to community work-in-progress (pgvector backend, search
  hardening, hierarchical pruning, KG caching, a four-layer
  storage/encoder/retrieval/consumption architectural model) rather than
  a finished answer — an open, acknowledged gap as of that date.
- **2026-06-19.** Red Hat Developer published a deployment guide for
  running MemPalace's MCP server on OpenShift AI, explicitly flagging it
  as "under active development" and recommending thorough testing of the
  new HTTP transport before production use — a vendor-adjacent
  enterprise-evaluation signal, with an appropriate caveat rather than an
  endorsement.
- **Net read.** Sentiment through the correction cycle (April) was
  positive-with-caveats and MemPalace's own response (public retraction)
  is repeatedly cited approvingly. No comparably dated negative signal was
  found after the April cycle; the scaling-doubt thread (April–May) reads
  as open-and-being-worked, not resolved-and-dismissed.

### 5. Verdict

**Strengths.** The verbatim-storage thesis is architecturally simple and
matches or beats extraction-based competitors on retrieval recall at zero
marginal LLM cost. The background-hooks token-economy pattern (near-zero
chat-window cost for memory bookkeeping, quantified at ~$1.13/session →
$0) is directly transferable. Governance discipline — retraction log,
tool-enforced dev/held-out split, self-disclosed teaching-to-the-test,
declared-transformations-with-conformance-tests, multi-harness plugin
architecture over a single authored-once instruction source — is
best-in-class among the engine's watched libraries, and is *still holding*
three months and three minor versions later (no new retraction entries
since 2026-04-14 despite continued rapid shipping).

**Failure modes.** Retrieval recall is not end-to-end answer quality
(self-acknowledged in `BENCHMARKS.md`). No procedural-memory type at all.
No decay/forgetting policy beyond append-only supersession — the corpus
grows monotonically forever; both the April KB analysis and this pass
flag this as an open question the maintainers are still answering
piecemeal (community fork work, no centralized roadmap doc as of
2026-05-13) rather than architecturally. 627 open issues against a
small core team plus a large contributor base is a real triage-load
signal, though not evidence of quality decline on its own.

**Transferability to a markdown+git, single-operator, human-gated
engine.** Very high, and mostly already recognized — 9 of 10 candidate
findings from the April analysis were promoted into the KB. Three
patterns are the highest-value transfers the engine has not yet fully
exploited: (1) **the retraction log** (`docs/HISTORY.md`) as a first-class
governance artifact, distinct from a changelog, with a full per-entry
audit trail of every surface a retracted claim was removed from — directly
adoptable for the engine's own DD-supersession and findings-correction
cases; (2) **declared-transformations with conformance tests** (RFC 002) —
converts a social contract ("Researcher writes to Findings/Sources/
Authorities only," DD-30/DD-82) into a machine-checked property, the same
move the engine would need to make agent-write-boundary claims testable
rather than asserted; (3) **the tool-enforced dev/held-out split with
public self-disclosure of teaching-to-the-test** — reusable close to
verbatim for any future IL eval round. None of these three require the
verbatim-memory *architecture* itself; they are governance/eval patterns
separable from the storage thesis, and the engine's markdown+git substrate
already resembles MemPalace's "no cloud, no extraction, local files" stance
more than it resembles Memongo's MongoDB-native one.

---

## Memongo vs. MemPalace — contrast

Both are 2026 counter-positions against the dominant LLM-extraction memory
pattern (mem0/Mastra/Supermemory), but they disagree with each other on
*how*: Memongo keeps extraction but collapses storage into one polymorphic
MongoDB collection; MemPalace drops extraction entirely and stores raw
text. Scale differs by roughly three orders of magnitude in adoption
(Memongo: 29 stars, solo-maintained, quiet since 2026-06-27; MemPalace:
57.4k stars, org-owned, shipped a release two days before this dossier and
merged hotfixes the same day it was written) — treat Memongo's
architecture as a citable design pole, not a load-bearing dependency
candidate. Memory-type coverage is a clean four-vs-three split: Memongo
has explicit episodic/semantic/procedural/working-adjacent types behind a
lifecycle-verb API; MemPalace has no procedural type and no distinct
working-memory tier by design (verbatim-always forbids the synthesis a
procedural abstraction would require). Decay policy is the sharpest
architectural difference: Memongo actively decays by importance with a
permanent-exemption escape hatch; MemPalace never decays, only supersedes
and surgically purges contamination — unbounded growth is an accepted
trade for zero-extraction fidelity. Governance maturity is the strongest
transferable signal from both: Memongo's benchmark-claim discipline visibly
matured between April and June specifically *by auditing MemPalace's own
2026-04 correction cycle* — a second-order data point that MemPalace's
retraction-log pattern is already propagating to peer projects, which is
independent evidence for adopting it in the engine.
