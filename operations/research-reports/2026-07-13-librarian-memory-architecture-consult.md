# Librarian Builder-Mode Consult — Full Layered-Memory Architecture (IB-172, pulled forward)

Scope: map the engine's actual memory surfaces onto KB memory vocabulary, resolve the
RAG boundary, evaluate OKF conformance, name promotion/retirement/loop-consumer
policy per layer. All claims cited to `research-findings/<slug>.md` unless marked
"engine fact" (given in the brief) or "synthesis" (this consult's own inference, not
a KB citation).

**CORRECTION (mid-consult, coordinator-supplied):** the earlier "~150-file KB" premise
used in the prior (residue-triage) consult and in this consult's first draft was wrong.
Measured counts: `research-findings/` = **907**, `research-sources/` = 238,
`research-authorities/` = 91, `extracts/` = 209 total (guides 15, patterns 72, rules 69,
skills 28, templates 25), DDs 91, IB 76, frozen SL corpus 153, `watched-libraries/` = 37.
This is corrected explicitly in §1 and §2 below — **not softened**. The earlier "deep
under threshold" verdict for `research-findings/` was wrong; it is now the one folder in
the vault sitting *at* the KB's own named ceiling, not comfortably below it. Every other
folder (sources, authorities, extracts, DDs, IB, SL, watched-libraries) remains
comfortably under any threshold the KB names, individually.

---

## 1. Layer Model

### The KB's two vocabularies (state both, per the brief)

**Four-tier canonical model** (`operations/references/librarian/memory.md` §Short
definition, citing G7; corroborated by `four-tier-agent-memory-model-with-write-policy`,
Strong/production-tested): **working → episodic → semantic → governance**, plus a widely
cited practitioner fifth surface, **global-learnings**, that sits at the
episodic/semantic boundary. `memory-cross-layer-promotion-governance` (Medium) adds the
promotion/demotion detail per tier.

**Trichotomy vocabulary** (`memory-wiki-world-kb-trichotomy`, Medium): **memory**
(remembers conversations — architectural boundary, only what passed through the agent),
**wiki** (knows one domain, curated, human-gated), **world-KB** (knows the world — typed
pages for people/orgs/meetings/decisions, ingests what never touched chat). The
trichotomy's own Potential Improvements section flags a fourth column it leaves
implicit: **procedural knowledge (skills/how-to)** — the KB does not have a canonical
name for this tier; this consult uses "procedural" per the brief's own framing.
**Prospective memory** (intentions for future action, cross-session) has **no KB
finding at all** — flagged as a coverage gap below.

### The retrieval-level ladder (`per-folder-heterogeneous-retrieval-levels`, Medium — stated explicitly per instruction)

1. **Routing files + folders** — CLAUDE.md as router, exact word/name lookup.
2. **LLM wiki** — index files + concept pages + backlinks, whole-page reads.
3. **Semantic search** — embeddings, meaning-match instead of keyword-match.
4. **Knowledge graph** — typed relationship chains, token-efficient for entity questions.
5. **Always-on autonomous brain** — constant sync/refresh/ingest (Gbrain-style crons).

Rule: assign the *lowest* level that fits per folder; upgrade only on felt pain. Herk's
own production brain sits at level 2 and declines 4–5.

### Mapping table

| Engine surface | Memory kind (four-tier / trichotomy) | Ladder level (current) | KB verdict: match / under / over |
|---|---|---|---|
| PROGRESS.md (pinned, line-capped) + CLAUDE.md chain | Working (four-tier); router-shaped, not "wiki" | Level 1 (routing) | **Match.** `four-tier-agent-memory-model-with-write-policy` implementation_notes names PROGRESS.md as the engine's working-memory instance; hard line-cap + compaction is exactly the working-tier demotion rule (`memory-cross-layer-promotion-governance`: "strict token budget + compaction after each session"). |
| git + HISTORY.md (append-only) | Ambiguous — episodic *or* governance (see §5) | Level 1–2 (plain files, changelog navigation) | **Match if classified as governance-memory** (see §5); would be **under-built** if classified as episodic (no summarization/pruning per that tier's rule) — the classification itself is the open question. |
| Frozen SL corpus | Episodic archive (retired producer, DD-116) | Level 1 (flat files, no longer navigated by index) | **Match for a closed archive** per `docs-split-by-lifespan-not-topic`'s archive/ bucket — but see §6 for whether anything still reads it. |
| Run reports in operations/ | Episodic telemetry | Level 1 (ephemeral, report-only, not persisted — per `boundary-cases.md`) | **Under-built relative to structured-fact-extraction, but KB-endorsed at this volume.** `structured-fact-extraction-from-conversations` wants typed facts, not raw prose; at near-zero base rate, `per-folder-heterogeneous-retrieval-levels`'s pain rule says don't upgrade yet. |
| research-findings/ (907) + sources (238) + authorities (91) | Semantic (wiki leg of trichotomy) | **Hybrid Level 2–4**: whole-file wiki reads (Level 2) *plus* typed `related_findings` edges (contradicts/enables/extends/same-problem) that already function as a lightweight knowledge graph (Level 4) — without embeddings. | **`research-findings/` alone is now AT the KB's named ceiling — see the per-folder scale audit below; this is a corrected verdict, not a match.** `sources/` and `authorities/` individually remain comfortably under threshold. |
| extracts/guides + extracts/patterns | Semantic, distilled (Tier-1 per Librarian read rule) | Level 2, with the guide-routing-table functioning as an index.md equivalent | **Match.** Already OKF-index-shaped in practice (see §3) without having adopted OKF. |
| knowledge/ (patterns/templates/reference/schematics) | Semantic, engine self-knowledge (DD-111's second body, distinct from extracts/) | Level 2 | **Match**, gated by DD-121's cache criteria (see §4) rather than free accumulation. |
| DDs | Closest to semantic (durable policy fact), but with a formal supersession lifecycle stronger than typical semantic-memory governance | Level 1 (frontmatter-filtered, `status: Binding`) | **Match, arguably ahead of the KB's generic guidance** — see §5, DD-44 vs. `content-derived-temporal-expiration-contradiction-resolution`. |
| IB | **Prospective** (no KB vocabulary — gap) / workflow state | Level 1 | No finding to compare against; flagged gap. |
| operations/references/ | Semantic, reference-shaped specifically | Level 1–2 | **Match.** Precisely `docs-split-by-lifespan-not-topic`'s reference/ bucket, and DD-121's exclusion criterion for what stays *out* of knowledge/. |
| .claude/skills + agents/ | Procedural (KB's own named gap) | Level 1 (path-pointer, not embedded copies) | **Match on structure** — `skills-as-pointers-to-second-brain-files` (Medium) is the exact pattern (SKILL.md as pointer, not embedded context copy); consumed_by shows the engine already extracted this as `skills-reference-shared-context-by-path`. **Gap on lifecycle** — see §5/§6, no outcome-scored retirement exists. |
| feedback/ | Inbound episodic (human-driven ingestion funnel) | Level 1 | **Match.** G7 Step 6.1 dual-ingestion-funnel pattern: feedback/ is the human-driven `raw/`-staging leg; `/process-feedback` is the quality gate before promotion. |

### Per-folder scale audit against the real counts (correction, not the original draft)

`per-folder-heterogeneous-retrieval-levels` is explicit that the threshold question is
**per-folder**, not vault-wide — so this audit runs folder-by-folder against the real
counts, not the vault total (~1,765 documents across all governance/research folders
combined, which is well past every threshold the KB names, but that aggregate number is
the wrong unit per the KB's own framing).

| Folder | Count | KB's named ceiling(s) | Verdict |
|---|---|---|---|
| **research-findings/** | **907** | `index-file-navigation-as-rag-replacement`: "**Scale ceiling around ~1000 docs before vector search outperforms**." `scale-threshold-heuristic-obsidian-vs-rag`: recommends Obsidian/file-traversal "under ~1000 documents." `file-search-outperforms-rag-for-small-corpora`: file search wins below "thousands of documents"; that finding's own now-stale implementation note ("threshold reached if the KB grew to thousands... not imminent") is the exact claim this correction overturns. | **AT the ceiling, not under it.** 907 is inside every "stay on file traversal" band the KB names but is the closest any engine folder has come to the boundary where the KB says its own heuristic starts to strain. This is the one folder where "no action needed" is no longer the honest reading. |
| research-sources/ | 238 | Same ceilings | Comfortably under. |
| research-authorities/ | 91 | Same ceilings | Comfortably under. |
| extracts/ (guides 15, patterns 72, rules 69, skills 28, templates 25 = 209 total) | 209 (largest sub-folder: patterns, 72) | Same ceilings | Comfortably under, and Tier-1-pinned besides (routing-table navigation, not corpus-scale traversal). |
| DDs | 91 | Same ceilings | Comfortably under; also frontmatter-filtered (`status: Binding`) rather than traversed. |
| IB | 76 | Same ceilings | Comfortably under. |
| Frozen SL corpus | 153 | Same ceilings | Comfortably under, and closed to new writes (DD-116). |
| watched-libraries/ | 37 (registry entries; the cloned repo cache under it is a different, much larger, externally-owned corpus not counted here) | Same ceilings | Comfortably under at the registry level; the repo-cache subtree is out of scope for this audit (external code, not curated KB content). |

**Direct answer to "is the findings corpus at/over the grep→index boundary now":** it is
**at** the boundary the KB names for the file-traversal-is-fine zone (<~1000,
`scale-threshold-heuristic-obsidian-vs-rag`; ~1000 ceiling,
`index-file-navigation-as-rag-replacement`), and **still under** the boundary the KB
names for RAG becoming empirically superior ("thousands of documents,"
`file-search-outperforms-rag-for-small-corpora`). Those are two different lines, and 907
sits between them — past the point where "no action needed" is accurate, short of the
point where the KB says vector search actually wins.

**What the KB prescribes as the first upgrade step — and it is not RAG.** Three findings
converge on the same answer: the move at this point on the ladder is **Level 2
reinforcement, not a jump to Level 3.** `index-file-navigation-as-rag-replacement`'s own
Potential Improvements name exactly this moment: **"hierarchical indices for larger
vaults"** and **"health checks for index staleness and broken links"** — i.e.,
strengthen and structure the index-file layer before adding any embedding
infrastructure. The 2026-07 restatement embedded in that same finding (Chase AI) makes
the mechanism explicit: an index.md **"at every single level"** of the vault, not one
flat index — "faster and cheaper navigation... as folders grow to thousands of
documents." `per-folder-heterogeneous-retrieval-levels`'s ladder agrees structurally:
the diagnostic for Level 3 is a felt symptom — "whiffing on notes you know exist despite
routing" — not a raw document count; 907 alone, absent that symptom, is not yet a Level-3
trigger by the KB's own pain-driven rule. And `curated-spine-plus-rag-hybrid-query-router`
/ `query-shape-first-storage-design` both point the same direction: only the specific
*query shapes* that need pinpoint lookup should ever route to retrieval; the dominant
Librarian query shape today (whole-finding reads, per §2's table) still wants file
reads, not vector chunks, regardless of corpus size.

**Does the KB prescribe re-organization before indexing, or BM25/hybrid first?**
Re-organization first, unambiguously. No finding recommends BM25 or lexical indexing as
a mandatory intermediate step *before* Level 3 — BM25/lexical-plus-semantic only appears
in the KB as a *component of* Level 3 itself once Level 3 is warranted
(`hybrid-retrieval-pattern-semantic-lexical-graph`'s three-mode routing;
`rank-fusion-hybrid-retrieval-mongodb-atlas`'s fusion mechanics — both Medium evidence,
both describing what a future vector layer would compose with, not a rung between Level
2 and Level 3). The prescribed order is: **(1) verify/strengthen the index-file layer
now that 907 is close to the named ceiling — hierarchical indexing, staleness checks,
possibly per-subfolder indices rather than one flat `research-findings/` traversal
surface; (2) watch for the Level-3 pain symptom (agent fails to find findings it should
know exist despite correct routing); (3) only then consider semantic search, and even
then hybrid (lexical+semantic+graph) rather than semantic-only**, per
`hybrid-retrieval-pattern-semantic-lexical-graph`'s explicit rejection of single-mode
retrieval ("no single retrieval method covers all query types well").

**Practical read for the engine today:** `research-findings/` does not currently have a
hierarchical or per-category index — retrieval is frontmatter grep plus the 3-hop
`related_findings` traversal (engine fact). That is Level 1–2 without the Level-2
reinforcement `index-file-navigation-as-rag-replacement` names as the correct next step
at this scale. Building a richer index layer (even a lightweight one — category-scoped
index files, or a generated table of contents by `category`/`priority`) is the
KB-prescribed action *now*, ahead of and instead of any RAG/vector work, and is a much
smaller lift than what §2 originally (and still) concludes about RAG readiness.

### Retrieval mechanisms given, mapped

- **Cold-start injection** (PROGRESS.md/CLAUDE.md) = auto-recall, the KB's preferred
  strategy over tool-based lookup (G7 Step 2.1, "prefer auto-recall... fails at exactly
  the moment it is most needed" for the tool-based alternative). Correct pattern.
- **Frontmatter grep** = Level-1/2 structured-metadata query, deliberately not
  embeddings — matches the scale-threshold heuristic's default.
- **Slug/routing-table pinning** = the OKF index.md convention, arrived at independently
  (see §3).
- **Link traversal, Tier1→2→3 escalation** = a direct instance of
  `escalating-search-order-routing` (see §2).
- **Dataview (human-side)** — no KB finding covers a human-facing query layer
  distinct from agent retrieval; flagged as an uncited engine-specific tool (gap, minor).

---

## 2. Retrieval + RAG Boundary

`escalating-search-order-routing` (Medium) states the order that should govern any
"vague question": **(1) curated file most likely to hold the answer → (2) broader
wiki/transcript layer → (3) live external system of record**, cheapest-and-curated
first. This is *structurally identical* to the engine's read-contract Tier-1 → Tier-2 →
Tier-3 escalation (engine fact): Tier-1 guides ≈ step 1, Tier-2 findings/link-traversal
(3-hop ceiling) ≈ step 2, Tier-3 watched-libraries/external reads ≈ step 3. No design
change indicated — the engine already implements the KB's recommended shape.

`curated-spine-plus-rag-hybrid-query-router` (Weak/theoretical) supplies the vocabulary
for what the "spine" and "reach" would be if the engine ever needed both: **spine** =
research-findings/ + extracts/ + knowledge/ (the curated ~80% canonical core); **reach**
= the candidate long tail — `watched-libraries/_tmp/repo-cache` (cloned external repos,
large and uncurated), a hypothetical grown transcript archive, or run-report history if
it ever accumulates past readability. None of these are currently vector-indexed.

**Concrete trigger signals for crossing to RAG** (per the KB, not invented here):
- `scale-threshold-heuristic-obsidian-vs-rag`'s explicit "migrate to true RAG when"
  list: corpus scaling to thousands/millions of documents; need for sub-second
  retrieval across a massive corpus; **multiple concurrent users** querying the same
  base; heterogeneous document types (PDFs, images, structured data mixed with text).
- `query-shape-first-storage-design`: the query-shape trigger specifically is
  **pinpoint lookup in bulk text** ("what was rule 17 of our 1,000 rules") — whole-object
  synthesis queries (which describe nearly all current Librarian queries: "explain
  finding X," "what does guide G7 say") actively *fail* on vector chunking and should
  stay markdown.
- `per-folder-heterogeneous-retrieval-levels`'s pain diagnostic: "whiffing on notes you
  know exist despite correct routing" is the concrete symptom that signals Level 3.

**Which folder crosses first, if any ever does — corrected against the real counts (see
§1's per-folder scale audit):** `research-findings/` (907 documents) is now the folder
closest to a boundary, but it is the *file-traversal-ceiling* boundary
(`index-file-navigation-as-rag-replacement`'s "~1000 docs"), not the
*RAG-becomes-superior* boundary (`file-search-outperforms-rag-for-small-corpora`'s
"thousands of documents"; `scale-threshold-heuristic-obsidian-vs-rag`'s "multiple
concurrent users" / "heterogeneous document types"). None of those RAG-trigger
conditions hold for `research-findings/` today — it is single-operator, text-only,
frontmatter-typed, and still an order of magnitude under "thousands." So the corrected
answer is: **no folder crosses to RAG next; `research-findings/` is the folder that
needs its Level-2 (index) layer reinforced next**, per §1's prescribed first-step
analysis — a materially smaller and different intervention than adding retrieval
infrastructure. `watched-libraries/_tmp/repo-cache` (large, heterogeneous, external
code) remains the more plausible long-run RAG candidate *if* it ever needs bulk
pinpoint lookup, but the same scale-threshold finding notes that even the coding-agent
ecosystem (Claude Code included) dropped vector DBs there in favor of grep/file-search
(`file-search-outperforms-rag-for-small-corpora`), so this candidate is weaker than it
looks, too.

**Derived-index position** (`markdown-git-system-of-record-derived-disposable-db`,
Medium): if a derived index (vector/graph/DB) is ever built for any folder, the KB's
position is unambiguous — **markdown-in-git stays the system of record; the derived
layer is disposable and rebuildable from it, never the reverse.** "Every layer is
inspectable: the markdown is yours, the database is a local file... nothing about your
knowledge is trapped in the database." The engine already conforms structurally
(nothing is DB-primary today); this is a constraint to preserve, not a gap to close.

**Query-shape → storage-format catalog** (`query-shape-first-storage-design`):

| Query shape | Storage need | Engine instance today |
|---|---|---|
| Whole-object synthesis | One markdown file, read in full | Findings, guides, DDs — the dominant shape in the KB |
| Pinpoint lookup in bulk text | Vector/semantic snippet retrieval | None built; no folder yet needs it |
| Relationship trace | Typed-edge knowledge graph | `related_findings` typed edges (contradicts/enables/extends/same-problem) — already present, cheaply, without embeddings |

---

## 3. OKF Conformance

Both `okf-open-knowledge-format-curated-bundle-spec` and
`knowledge-substrate-standardization-cross-agent-interop` are Medium-evidence, P2
(Design Required), and explicitly `pipeline_status: raw` — the KB itself frames this as
an open, Nick-gated question, not a settled recommendation ("no engine change is
proposed here").

**What conformance would require of frontmatter/`_schema.yaml`:**
- **One concept per file** — already true; findings are already this shape.
- **`type` as the only required field** — the engine's schema is richer (category,
  evidence_strength, priority, pipeline_status, etc.); conformance means adding or
  aliasing a `type` field, not replacing the existing schema (OKF's floor is
  deliberately minimal — everything else is optional).
- **`index.md` navigation** — the engine has partial equivalents
  (guide-routing-table.md, research-dimensions.md) but no single per-folder
  table-of-contents in OKF's reserved sense; would need generation.
- **`log.md` append-only changelog** — the engine's git history (plus the now-retired
  SL) is already a superset of this; could be emitted as a derived, git-log-sourced
  artifact rather than hand-maintained.
- **Ordinary markdown links forming a graph** — the engine already has something
  *richer*: typed YAML `related_findings` edges, not plain inline `[[links]]`. This
  over-delivers relative to OKF's floor but isn't literally what the spec asks for.

**What it buys:** interop — "what MCP did for agent-to-tool communication, OKF does for
agent-to-knowledge-base communication" (`knowledge-substrate-standardization-cross-agent-interop`).
Concretely: any conformant external agent could navigate the KB without reverse-
engineering `_schema.yaml`; unlocks spec-as-skill one-shot conformant refactors,
subagent-parallelized migration, multi-bundle two-tier indexing with a thin CLI, and
shareable-bundle distribution (a git-cloneable KB export) — relevant chiefly to the
portfolio-presenter/practitioner-friend consumer archetypes the finding names, not to
internal Librarian operation, which already works fine unconformant.

**Maturity risk:** v0.1, weeks old, single vendor (Google). The OKF finding's own
guidance: "bookmark it, don't bet the company on it." The interop finding's Failure
Modes are directly relevant: "the standard doesn't win" (early conformance work could be
stranded); "too simple critique" (a minimal floor still lets two conformant KBs diverge
enough to frustrate search); **"refactor risk"** — a one-shot, subagent-parallelized
refactor of a large bespoke KB "can silently drop schema semantics the standard has no
slot for — **for us, fields like evidence_strength or typed related_findings edges**"
(the finding names our own fields); "shared-bundle trust" (imported third-party bundles
would be unreviewed content an agent treats as curated truth).

**Export-time conformance vs. native adoption:** the interop finding poses this exact
fork as the live question — "should the KB be OKF-conformant, or more conservatively
OKF-*exportable* (keep `_schema.yaml` internally, emit a conformant bundle as a
distribution/consumption surface)." Given (a) DD-121's anti-redundancy invariant (a
single agent-readable home per piece of wisdom — native OKF adoption would fork that),
and (b) the refactor-risk failure mode naming `evidence_strength`/typed-edges as fields
OKF has no slot for, **export-time conformance is the lower-risk fit**: `_schema.yaml`
stays the authoritative internal schema (preserves fields OKF can't represent), and a
generated OKF bundle becomes a derived, disposable, rebuildable projection —
structurally the same shape `markdown-git-system-of-record-derived-disposable-db`
already endorses for any derived layer (system of record stays the richer internal
format; anything else is regenerable). Native adoption would require either dropping or
awkwardly re-anchoring `evidence_strength`/`priority`/typed edges into OKF's optional
metadata — the exact risk the KB's own Failure Modes section warns against. Both source
findings stop short of recommending either path; this is this consult's synthesis
applying DD-121 and the derived-DB pattern to their open question, not a KB citation for
"export-time wins."

---

## 4. Transitions

`memory-cross-layer-promotion-governance` (Medium) frames promotion as the
**highest-risk operation** in any layered memory system and demands, at every boundary:
explicit ownership, an approval level, and a rollback path. `write-back-discipline-memory-is-not-the-brain`
(Medium) adds the trigger condition: write back **at the moment something becomes
durable**, not per-instance. `evergreen-vs-volatile-ingestion-rule` (Medium) supplies
the ingestion-time test ("would I want this in a year?").

### Transitions that exist

| Transition | Engine mechanism | KB match |
|---|---|---|
| Episodic (session) → semantic (DD/knowledge) or prospective (IB) | DD-116 shape-based routing: decision-shaped → DD, pattern-shaped → knowledge/, work-shaped → IB | **Strong match.** This *is* the policy-gated promotion `memory-cross-layer-promotion-governance` calls for — explicit ownership (Nick/Owner), rollback path (DD-44 supersession or IB status change). Also matches `structured-fact-extraction-from-conversations`: converting raw session prose into typed governance artifacts is the engine's (human-mediated, not automated) version of structured fact extraction. |
| PROGRESS.md → HISTORY.md/DD/IB | `/session-handoff` route-then-compact | **Match.** Working→episodic (HISTORY.md entries cite commits = evidence pointers, per the tier's promotion rule) fanned out by the same DD-116 shape classification. |
| Findings → extracts | DBDO-style: `/identify-artifacts` classify → `/extract-artifacts` draft, human-gated | **Match, with an epistemic caveat.** This is an internal semantic→semantic promotion (raw curated → distilled curated) — the Karpathy-style "compile" step. It is exactly the write-time-synthesis case `write-time-vs-query-time-synthesis-kb-poisoning` (Medium) warns about: LLM-authored content re-indexed as *higher-trust* Tier-1 substrate. The finding's own carve-out — "for personal wikis with active review, write-time synthesis remains superior" — is satisfied by the human gate before writing, but this is the one transition in the engine most exposed to that named failure mode if the gate is ever skipped. |
| Extracts → knowledge/ | DD-121: four-hold cache test (cross-cutting, reference-shaped, engine self-knowledge, stable) + three exclusions, Owner-owned, no auto-cache mechanism | **Match, and this IS the promotion-governance pattern the KB asks for**, arrived at independently: explicit ownership (Owner, DD-86), no blanket mechanism (Rule 11 applied at the transition itself, "~88% of DDs correctly have no cache"). |

### Transitions that do NOT exist yet

- **Semantic (findings) decay/demotion.** No importance-decay, TTL, or automatic
  contradiction-resolution among findings — cross-links (`contradicts` edges) are
  human/skill-run (`/finding-crosslink`), not write-time-automatic. The KB supports
  building this (`importance-based-decay-permanent-exemption`,
  `content-derived-temporal-expiration-contradiction-resolution`,
  `memory-decay-compaction-convergence`, all Medium) but `localized-memory-maintenance-over-global-reorganization`
  (Medium, empirical: localized maintenance ~3.7 sec/query vs. graph-wide
  consolidation ~116 sec/query for modest utility gain) plus the scale-threshold
  heuristic argue the engine's current periodic, targeted sweeps
  (`/detect-drift`, `/reassess-priorities`) are the right-sized answer *now* — building
  automated decay is KB-supported but not yet KB-warranted.
- **Episodic telemetry (run reports) → semantic (calibration registry).** No promotion
  path exists from ephemeral run-report data into any durable store — this is exactly
  the gap the prior (residue-triage) consult's Answer B addressed. The KB supports
  building it: `per-skill-contribution-scoring-telemetry` (Medium) gives the shape
  (evidence log → contribution score → registry), gated by the recurrence threshold
  that consult's Answer C established.
- **Procedural (skills/agents) retirement/promotion.** No Ratchet-Recipe-equivalent
  (evidence floor + capacity cap) exists for the skill/agent roster.
  `ratchet-recipe-skill-retirement`'s own implementation_notes call this out directly:
  "a candidate blueprint for lifecycle rules over our own roster and extracts... trials-
  based scoring needs a usage-outcome signal we do not currently log." The paper's
  defaults (Nmin=100 trials) don't fit the engine's invocation volume without a proxy —
  the finding's own Potential Improvements section flags "adapting 'trials' for low-
  frequency libraries... may need time-decay or proxy signals instead of raw counts" as
  unsolved.
- **World-KB-shaped promotion** (session decision → typed page for a person/org/
  meeting). Does not exist, and per `memory-wiki-world-kb-trichotomy` this is *the*
  named gap: "the piece the engine does NOT have." Out of scope for this engine's shape
  (Household-OS-adjacent territory); not recommended to build now — consistent with the
  prior consult's rejection of a full world-KB layer.

---

## 5. Retirement

`memory-cross-layer-promotion-governance` supplies per-tier demotion rules; three other
findings supply decay *mechanisms* (importance-based, temporal/contradiction-based,
multi-strategy compaction); `governance-memory-append-only-audit-layer` supplies the
one *no-decay-is-correct* case; DD-44 and `skill-library-drift-failure-mode` supply the
engine-specific counter-evidence.

| Layer | KB guidance | Engine mechanism | Verdict |
|---|---|---|---|
| Working (PROGRESS.md/CLAUDE.md) | "Strict token budget + compaction after each session" (`memory-cross-layer-promotion-governance`) | Hard line-cap + `/session-handoff` compaction | **Fully covered.** |
| Episodic — git/HISTORY.md | "Months of retention with summarization; importance/recency scoring for garbage collection" | Kept forever, append-only, no summarization | **Open classification question, not a clean gap.** If HISTORY.md/git is genuinely episodic-task-memory, it's under-governed against the KB's own rule. But its actual behavior — append-only, audit-shaped, "why did we do that" — matches `governance-memory-append-only-audit-layer` far better: "retention policy often longer than teams initially expect" is that finding's explicit guidance, and append-only *is* correct there. **Recommend resolving this classification explicitly** (governance-memory, not episodic) — it dissolves the apparent gap. |
| Episodic — frozen SL corpus | Archive, no further writes | `archive/` move, DD-116 retirement | **Match** structurally (`docs-split-by-lifespan-not-topic`'s archive/ bucket) — but see §6 for whether it's read back at all. |
| Episodic — run reports | No formal policy; base rate near zero | Report-only, not persisted | **KB-endorsed non-build** at this volume (per-folder-heterogeneous-retrieval-levels pain rule; consistent with prior consult's Answer C). |
| Semantic — DDs | Contradiction resolved via an "Updates" relationship: old record retained, marked not-latest, never deleted (`content-derived-temporal-expiration-contradiction-resolution`) | DD-44: Superseded status, never deleted, explicit predecessor/successor cross-references | **Strong match — arguably ahead of the KB's generic pattern.** DD-44's Superseded status is functionally identical to that finding's `isLatest: false` marker, formalized earlier and more rigorously (immutability + explicit chain-traceability) than the generic finding describes. |
| Semantic — findings/sources/authorities/extracts | Same three decay mechanisms as above | **No formal policy** — only periodic, human/skill-triggered sweeps (`/detect-drift`, `/reassess-priorities`, `/finding-crosslink`) | **Gap that is currently KB-sanctioned as acceptable, but with a corrected margin.** `localized-memory-maintenance-over-global-reorganization`'s cost argument (localized writes stay cheap regardless of total store size — it's propagation scope, not corpus size, that drives cost) still favors triggered/localized sweeps over standing decay infrastructure even at 907 findings. But the corrected count (§1/§2) removes the comfortable-margin framing: this is the layer whose corpus just crossed into "large enough to actually need the sweep cadence to be reliable," not "small enough that the question is moot." First place to build real decay machinery if evidence_strength entries start visibly rotting — and that trigger is now plausibly closer than the original ~150-file premise implied. |
| Procedural — skills/agents | Outcome-driven retirement, evidence floor + capacity cap (`ratchet-recipe-skill-retirement`) | **None.** No scoring, no retirement path | **Real gap, with a caveat from the KB itself.** `skill-library-drift-failure-mode`'s own "Misapplied to curated libraries" note: "a human-gated library (like this engine's) has a quality gate at intake and may drift far slower — the risk shifts to staleness, not junk." The engine's exposure is stale-but-unretired skills, not runaway accumulation of junk — a milder version of the paper's target failure, but still unaddressed. |
| Prospective — IB | No KB finding (vocabulary gap) | Status lifecycle (open/done/etc.) | Functions as its own demotion mechanism; nothing to compare it against in the KB. |

**Layers with no retirement policy at all today:** findings/sources/authorities/extracts
(semantic-distilled) and procedural (skills/agents). The KB supports building policy for
both, but both citations carry the identical caveat — designed/validated at volumes far
above the engine's current scale (100+ trials for skills; large corpora for decay
functions) — so any adoption needs a proxy/time-decay substitute for raw trial-count or
document-count evidence floors, not a direct port.

---

## 6. Self-Improvement Wiring

Findings that speak to memory feeding a self-improvement loop:
`compounding-knowledge-loop-internal-data` (Medium — the outcome-encoding requirement:
"what happened, what was done about it, what resulted... without element 3, month six
looks like month one... most implementations skip this, which is why compounding fails
to materialize in practice"), `per-skill-contribution-scoring-telemetry` (Medium —
telemetry consumed by retirement decisions), `ratchet-recipe-skill-retirement` /
`skill-library-drift-failure-mode` (outcome-linked lifecycle), `dreaming-memory-consolidation`
(Medium — REM-phase reflection over promoted memories, human-reviewable Dream Diary),
`memory-cross-layer-promotion-governance` (promotion itself is the mechanism that feeds
the loop).

| Memory layer | Loop consumer in the engine today | Write-only / graveyard risk |
|---|---|---|
| Working (PROGRESS.md/CLAUDE.md) | `/session-handoff` (reconciles, routes deltas out) | None — actively loop-connected. |
| Episodic — git/HISTORY.md | `/governance-audit` (proposes DDs/IB from git+PROGRESS diff), Owner session-close review | None — actively loop-connected. |
| Episodic — frozen SL corpus | **None found.** Read-only archive, no skill queries it today | **Medium risk.** Acceptable if genuinely closed (`docs-split-by-lifespan-not-topic` archive/ bucket); becomes real graveyard risk specifically because the residue-triage consult's calibration-data proposal (crosslink error rates, defect-class taxonomy) depends on reading exactly this corpus back — if that registry is never built, the numbers stay permanently write-only. |
| Episodic telemetry — run reports | **None.** Surfaced in report text once, then discarded (`boundary-cases.md`: "surface-in-run-report, write nothing") | **Highest risk in the map.** This is the closest real-world instance of `compounding-knowledge-loop-internal-data`'s named failure — outcomes are generated but nothing closes the loop between action and result. |
| Semantic — research-findings | `/reassess-priorities`, `/finding-crosslink`, `/promote-findings`, Codifier guide-synthesis | None — well-instrumented, textbook example of the compounding pattern actually working. |
| Semantic — extracts/guides, patterns | Every Librarian query (Tier-1 read rule reads guides first) | None — high-reuse, the clearest working instance of `compounding-knowledge-loop-internal-data`'s intended effect ("each session incrementally smarter"). |
| Semantic — knowledge/ | `/maintain-docs`, `/translate-governance`, `/system-health` (Owner-only, DD-121) | Low — loop-connected but narrow (single-consumer class). |
| Decision memory — DDs | `/governance-audit`, DD-44 chain, every skill/DD citing `source_dd` | None — probably the best-instrumented layer in the engine. |
| Prospective — IB | `/track`, `/ib`, PROGRESS.md's "next unit of work" | None — loop-connected. |
| Procedural calibration/reference — operations/references/ | **None yet** — the registry the prior consult proposed does not exist | **Design-time risk, not yet realized.** If built without naming a specific consumer skill/agent that reads the numbers back to actually recalibrate something, it becomes exactly the graveyard `compounding-knowledge-loop-internal-data` warns against. The consumer must be named at design time, not left implicit. |
| Procedural — skills/agents | **None** for outcome-based improvement. `/process-feedback` handles qualitative feedback but doesn't score usage outcomes | **Real, standing risk.** No per-skill-contribution-scoring-telemetry equivalent exists, so there's no signal a retirement mechanism (§5's gap) could even consume if built. Compounded by `skill-library-drift-failure-mode`'s core point: this kind of drift is silent by construction — "nothing errors when a stale skill misleads." |
| Inbound episodic — feedback/ | `/process-feedback` | None — matches G7's dual-funnel pattern with an actual quality gate. |

**Summary of write-only/graveyard-risk layers, ranked:** (1) run-report telemetry —
near-total write-only today, highest risk; (2) procedural/skills roster — no outcome
loop exists at all, silent-by-construction per the KB's own framing; (3) frozen SL
corpus — low risk while genuinely closed, rises if a calibration registry is proposed
without a read-back path; (4) any future calibration registry — pure design-time risk,
fully avoidable by naming the consumer before building (this is the single actionable
takeaway for the second-brain proposal specifically).

---

## Coverage notes

Two vocabulary gaps surfaced repeatedly and are worth naming once: the KB has **no
finding for prospective memory** (IB's shape) and **no finding that names procedural
memory as a first-class tier** (the trichotomy names the gap itself). Both are candidate
future `research-findings/` entries if this architecture work continues.
