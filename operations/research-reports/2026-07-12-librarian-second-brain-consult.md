# Librarian Builder-Mode Consult — Second-Brain Proposal (IB-172 near-term slice)

*(Reconstructed verbatim from session-142 context after scratchpad rotation; original written 2026-07-12. NOTE: this consult was fed a wrong "~150-file KB" premise — measured reality is findings 907 / sources 238 / authorities 91 / extracts 209. The corrected verdicts are in `2026-07-13-librarian-memory-architecture-consult.md`; this report's B/C/D/E sections remain valid, its A-section scale claim does not.)*

Scope: gate question — does the DD-116 routing-loss inventory (stranded calibration
data, boundary-case encounters, pre-DD-116 closure-note overflow) justify a store
mechanism beyond DD-116 routing, and if so, what is the minimum viable mechanism.
All claims cited to `research-findings/<slug>.md` unless otherwise noted.

---

## A. Is a distinct curated memory layer justified at our scale?

**No, not as a system-wide layer.** Three independent, corroborating findings converge
on "stay simple, upgrade only on felt pain":

- `scale-threshold-heuristic-obsidian-vs-rag` (Medium, multi-channel corroborated): markdown
  file-traversal is the right architecture for a solo operator under ~1000 documents.
  The engine's KB (~150 files) is deep inside this threshold. "Just try it... migrate
  when it breaks" is the explicit decision rule, not "build ahead of need."
  *(Scale premise corrected 2026-07-13: findings corpus alone is at ~907 — see the
  architecture consult.)*
- `per-folder-heterogeneous-retrieval-levels` (Medium): the correct grain for a retrieval/
  storage upgrade decision is **per-folder**, not system-wide, and upgrades are
  **pain-driven only** — "if there's not pain, then why create more?" Nate Herk's own
  production business brain deliberately sits at level 2 (curated wiki) and declines
  levels 4-5. This directly matches Rule 11 (abstractions must earn their keep):
  recurrence evidence required, "might want later" is not evidence.
- `evergreen-vs-volatile-ingestion-rule` (Medium): the ingestion-time test is "in a year,
  will it be good to have this memory in here?" — a gate against building infrastructure
  for data that hasn't demonstrated durable value yet.

Applying the heuristic to the three drop-inventory items:
- **Calibration data** — already-occurred, already-durable measurement (recurrence
  evidence exists: ~10 historical SL entries). Passes the evergreen test. A *minimal*
  reference artifact is justified (see B) — not a new store, not infrastructure.
- **Boundary-case encounters** — zero base rate in 27+ sessions is the *absence* of
  recurrence evidence, not its presence. Per `per-folder-heterogeneous-retrieval-levels`'s
  own pain-diagnostic table, "no felt pain" maps to no upgrade (see C).
- **Pre-DD-116 closure-note overflow** — the consult brief itself notes this is "arguably
  already solved by DD-116 routing." No KB finding contradicts closing this as resolved.

**Verdict: no new store mechanism justified at the system level.** At most, one small,
existing-pattern-conforming artifact for calibration data (B); nothing new for
boundary-case encounters until the base rate moves off zero (C).

---

## B. Storage shape for low-volume calibration/measurement data

Evaluated against `query-shape-first-storage-design` (Medium): storage format should be
reverse-engineered from anticipated query shape, not from topic or volume alone. The
calibration numbers (crosslink error-rate table, transcript-extraction density
hierarchy, YAML defect-class taxonomy) are **whole-object synthesis** queries — "what
were our crosslink error rates last time we calibrated this skill?" — read as a whole
small table, not pinpoint-looked-up across a bulk corpus. That query shape maps
directly to a plain markdown file, not a vector store or DB
(`query-shape-first-storage-design`; corroborated by
`markdown-git-system-of-record-derived-disposable-db`, which flags a derived DB as a
"not-yet-needed upgrade path" absent per-folder retrieval pain).

`docs-split-by-lifespan-not-topic` (Medium) supplies the placement rule: partition by
truth-lifespan, not topic. Calibration numbers are **reference** — they don't expire,
they ground future recalibration, and they are not "living plans" (`active/`) or
frozen point-decisions (`decisions/`, i.e., DDs). That is exactly the shape the engine's
`operations/references/` folder already exists to hold (research-dimensions.md,
guide-routing-table.md are the existing precedent — not cited findings, but structural
fact from `systems/improvement-loop/CLAUDE.md`).

`okf-open-knowledge-format-curated-bundle-spec` (Medium) supplies the file-granularity
convention worth reusing even without adopting OKF wholesale: **one concept per file**,
YAML frontmatter, no required schema beyond a `type` field. Applied here: one
calibration-registry doc per measured skill/pipeline (or one registry file with
per-entry dated sections), not a monolithic append-only log and not scattered
frontmatter fields.

**Recommendation, ranked against the brief's four options:**
1. **An `operations/references/` calibration registry (winner).** Matches existing
   engine convention, matches the whole-object query shape, matches the
   reference-lifespan bucket. Minimal — a markdown file (or one per topic if entries
   diverge structurally), not a new folder taxonomy.
2. Frontmatter on the owning skill — rejected. Frontmatter is metadata-shaped
   (single current value), not a good fit for a time-series of historical
   measurements the KB explicitly frames as "numbers that would ground future
   recalibration" (multiple dated observations, not one field).
3. A knowledge/ pattern doc per topic — rejected as the primary shape. `knowledge/`
   is positioned (per `docs-split-by-lifespan-not-topic`'s reference/decisions split,
   and the engine's own knowledge/ vs operations/references/ convention) for
   generalizable patterns, not engine-internal operational measurement. A pattern
   *could* later cite the registry as evidence, but the registry itself is
   operational reference data.
4. A new store — no KB finding supports this at ~10 stranded entries. Directly
   contradicted by A.

---

## C. Sparse telemetry-like records (boundary-case encounters, ~0-2/session, base rate zero in 27+ sessions)

Evaluated against `per-skill-contribution-scoring-telemetry` (Medium, empirical): this
finding is the KB's closest analog to a telemetry-store design, and it is explicit that
the pattern is calibrated for **high-volume** systems — "naive adoption in a high-volume
system multiplies cost," and its own Improvements section flags "cheap proxies for
low-volume libraries where 100-trial evidence floors are unreachable" as an *open,
unvalidated* problem, not a solved one. The KB does not have a validated append-file
telemetry pattern sized for a near-zero event rate.

Cross-checked against `evergreen-vs-volatile-ingestion-rule` (Medium): the ingestion
test is "in a year, will it be good to have this memory in here?" Applied per-instance,
a single boundary-case encounter record is volatile — it's one event, not a durable
fact — and copying every instance is exactly the "noise that demands monthly deletion
sweeps" pattern the finding warns against.

The KB's `write-back-discipline-memory-is-not-the-brain` (Medium) resolves the tension:
write-back happens **at the moment something becomes durable** — i.e., at the moment a
*pattern* is recognized, not at the moment of each raw event. This matches the existing
`boundary-cases.md` §3 feedback-routing table's own qualifier structure — several
encounter types already route to "IB item" specifically **when frequent** (e.g.
`hop-ceiling-hit` (frequent) → IB item; `redirect` (frequent to same target) → scope
proposal). That routing table already encodes exactly the "recurrence, not instance"
threshold the KB substrate independently argues for.

**Recommendation, ranked against the brief's four options:**
1. **Defer-until-nonzero-rate, combined with IB-item-on-recurrence (winner, and this
   is close to what `boundary-cases.md` §3 already specifies).** Keep the current
   report-surfacing behavior. Do not build a persistence mechanism for a base rate of
   zero. When any single encounter-type crosses a recurrence threshold the Librarian
   (or Nick) notices in run reports, that's the trigger for an IB item — not a standing
   log file maintained on spec.
2. Append-file per taxonomy — rejected. No KB finding validates a per-instance store at
   this volume; `evergreen-vs-volatile-ingestion-rule` and Rule 11 both argue against it
   directly. This is the "might want later" case Rule 11 explicitly excludes.
3. IB-item-on-recurrence alone (no defer framing) — acceptable as the *action* path,
   but needs the defer framing as the *default state*, since recurrence hasn't
   happened yet.
4. Run-report-only status quo, unchanged forever — close, but incomplete: it has no
   mechanism to *notice* recurrence across sessions since nothing persists. The
   improvement worth making (if any) is procedural/cheap — e.g., a human or Owner
   glancing across recent run reports periodically — not a new file format or store.

---

## D. What to copy vs not copy from Hermes/OpenClaw/Gbrain-derived findings, at our scale

**Copy (already partially adopted, worth reinforcing explicitly):**
- `write-back-discipline-memory-is-not-the-brain` — durable calls made in
  conversation get written back at decision time. The engine already does this
  structurally (session decisions → DDs/findings/IB items, not chat residue,
  per `systems/improvement-loop/CLAUDE.md` Session Ops). Frame the second-brain
  proposal as *continuing* this discipline for the calibration-data case (B), not
  inventing a new one.
- `evergreen-vs-volatile-ingestion-rule` — the "would I want this in a year" test is
  directly reusable as the gate for both B and C above.
- `markdown-git-system-of-record-derived-disposable-db`'s **top layer only**: plain
  markdown in git as the system of record. The engine already has this. No derived
  layer is being proposed here.

**Do NOT copy:**
- The **derived disposable database** (PG-lite, vector + keyword + self-wiring graph)
  itself. `markdown-git-system-of-record-derived-disposable-db`'s own implementation
  framing labels this "the not-yet-needed upgrade path if per-folder retrieval pain
  ever appears" — no pain observed, no upgrade warranted.
- **Always-on autonomous ingestion (Gbrain-style crons / "level 5").**
  `per-folder-heterogeneous-retrieval-levels` explicitly reports Herk declining this
  even in a mature production system, and `evergreen-vs-volatile-ingestion-rule`
  quotes his rationale directly: "I am in complete control of what my second brain
  ingests." Matches Nick's human-gate preference; do not propose automated ingestion
  of calibration data or encounter records.
- **The full memory/wiki/world-KB trichotomy as a three-store architecture**
  (`memory-wiki-world-kb-trichotomy`, Medium). Gbrain's world-KB layer (typed pages
  for people/companies/meetings/decisions with a graph) is a different-shaped problem
  than "~10 stranded numbers and a taxonomy of encounter types." Building a world-KB
  for this drop-inventory would be over-scoped relative to the actual gap — this
  finding is the right vocabulary for *future* Household-OS-adjacent world-KB
  questions, not for this consult.
- **Governance/audit-log layer** (`governance-memory-append-only-audit-layer`, Medium)
  — this is a compliance-grade append-only audit trail (EU AI Act framing, "why did the
  agent do that"). It is a different problem than calibration-data grounding or
  boundary-case telemetry; do not conflate. Not relevant to this gate question.

---

## E. Findings that CONTRADICT building a new store now

No KB finding carries a typed `contradicts` edge aimed at this specific proposal, but
three findings, taken together, function as the strongest counter-evidence:

1. **`scale-threshold-heuristic-obsidian-vs-rag`** — the engine is deep under the
   documented threshold for staying on plain markdown/file-traversal; adding storage
   infrastructure now is explicitly the over-engineering case the heuristic warns
   against ("Just try it... migrate only when it breaks"). *(Premise corrected
   2026-07-13 — findings corpus is at ~907, near the ceiling; see architecture consult.)*
2. **`per-folder-heterogeneous-retrieval-levels`** — upgrades require *felt pain*; the
   boundary-case-encounter base rate (zero in 27+ sessions) is the diagnostic table's
   own "no pain" signal, arguing directly against building anything for it now.
3. **`evergreen-vs-volatile-ingestion-rule`** — warns that ingesting non-durable data
   "is just adding noise" requiring recurring maintenance sweeps; applies most sharply
   against an append-file-per-encounter design (option rejected in C).

A fourth, softer signal: `write-time-vs-query-time-synthesis-kb-poisoning` (Medium) —
if any new store were agent-authored and re-consumed as ground truth (e.g., an agent
summarizing its own boundary-case patterns into a "curated" registry without review),
it inherits the write-time-synthesis poisoning risk. Not a direct contradiction of
building *a* store, but a reason any new artifact here should stay close to raw
recorded numbers (B's registry) rather than LLM-synthesized narrative, and should get
periodic human review if it accumulates entries.

---

## Coverage note

The KB has no finding specifically about "minimum viable calibration/measurement
registries at solo-operator scale" — this consult synthesizes across
query-shape-first-storage-design, docs-split-by-lifespan-not-topic, and the OKF
one-concept-per-file convention to reach the operations/references/ recommendation;
that synthesis is not itself a cited finding. If Nick adopts this, it would be a good
future `research-findings/` candidate in its own right (the gap is real: telemetry
findings in the KB are sized for high-volume systems, not near-zero-volume ones).
