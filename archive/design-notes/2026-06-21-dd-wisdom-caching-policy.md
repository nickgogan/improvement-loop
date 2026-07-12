---
title: "DD-wisdom caching policy — coverage map + selection criteria + agent wiring"
id: "dd-wisdom-caching-policy"
type: "design-note"
category: "knowledge-architecture"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-06-21"
updated: "2026-06-21"
author: "claude"
source_ib:
  - "IB-170"
tags:
  - "design-note"
  - "knowledge"
  - "governance"
  - "caching"
  - "rule-11"
---

# DD-wisdom caching policy

## The question (Phase 2, session 125)

Should the design wisdom locked in DDs/IBs be cached into agent-readable `knowledge/`? This note
maps coverage (what DD wisdom is / isn't cached), proposes selection criteria (what to cache, what to
**exclude**), and assigns agent wiring (Owner vs Librarian). **Propose-only: no DD, no IB, no cached
file is written on this note.** It is the gate input for those decisions.

## Frame — the two bodies (from `2026-06-20-extracts-knowledge-reconciliation.md`)

- **`extracts/` = research-substrate library** — external agentic-coding best-practice. What the
  Librarian advisory layer composes. **Not** in scope here.
- **`knowledge/` = the engine's self-knowledge** — how *this* engine is built and operates.

DDs are the engine's own design decisions, so caching DD wisdom into `knowledge/` is squarely a
self-knowledge-body question. The governance record (the DD) and its distilled agent-readable form
(a `knowledge/` doc) are two representations of the same decision — the caching question is *when the
second representation earns its keep* (Rule 11).

## Coverage map

### What `knowledge/` already caches (and correctly)

| Cached doc | Wisdom | Anchored DD |
|---|---|---|
| `reference/fractal-pattern.md` | 7-folder fractal unit | DD-52 |
| `reference/vocabulary.md` | shared terminology | (cross-cutting) |
| `reference/principles.md` | **DBDO pipeline** (mislabeled — see drift below) | DD-45 *(Superseded!)* |
| `patterns/capability-type-selection.md` | skill vs agent vs pattern selection | DD-109 etc. |
| `patterns/upstream-dependency-spectrum.md` | watched-library positioning | — |
| `guides/research-to-codification-pipeline.md` | the DD-80 pipeline | DD-80 cluster (7 DDs) |
| `guides/skill-authoring-guide.md` | SKILL.md mechanics | DD-109 |
| `schematics/*` + `templates/schematic-template.md` | curated workcells | DD-107 |

These share a profile: **cross-cutting, reference-shaped, engine-specific, stable.** That profile is
the policy (below).

### What is correctly NOT cached (the ~88%)

Of 70 Binding DDs, 26 are cited in no `knowledge/`/skill/reference/governance doc. Inspected, almost
all *should* stay uncached because their wisdom already lives in the right place:

- **Governance / structural facts** — `knowledge/` is the wrong home; they live in CLAUDE.md,
  `governance/`, or the DD itself. (DD-38, DD-40, DD-42, DD-47, DD-55, DD-56, DD-57, DD-59, DD-84,
  DD-85, DD-105, DD-108.) Caching = duplication with no consumer.
- **Operationalized inside one owning skill** — the wisdom is executable procedure and belongs in the
  SKILL.md that runs it, where logic and rationale co-locate as a single source of truth. (DD-67 →
  `/research-loop`; DD-71 → `/source-triage`; DD-88 → `/reassess-priorities`; DD-93/98/102 →
  `/synthesize-guide`; DD-69/70 → `/linkage-repair` + `/finding-crosslink`; DD-68/73/87 →
  `research-dimensions.md`; DD-64 → `/bootstrap`.) The traceability remedy here is **the skill should
  cite its source DD**, *not* a parallel `knowledge/` copy that will drift.

**This is the headline result:** caching is the exception, not the rule. A "cache every DD" mechanism
would manufacture duplication and drift against Rule 11 and the token-economy constraint.

### Genuine gaps (cacheable wisdom with no agent-readable home)

| DD | Wisdom | Why it qualifies | Strength |
|---|---|---|---|
| **DD-37** | Five foundational design principles (Spec Before Build; Complementary Tools; Knowledge Serves Expression; Start Lean; Shallow-vs-Deep) | Self-described agent-facing: *"apply these before consulting system-specific DDs."* Cross-cutting, reference-shaped, stable. Cached nowhere. | **Strong** |
| DD-62 | Two-phase development: Explore then Harden | Cross-cutting dev philosophy, no single skill owner. Zero mentions outside the DD. | Medium — confirm it's still active wisdom |
| DD-74 | Token-budget constraints on context files | Authoring constraint applied to every CLAUDE.md/skill/doc; alive in practice (Nick's standing token-economy feedback) but uncodified in `knowledge/`. | Medium |

### Redundancy / drift (the inverse problem)

- **`reference/principles.md` is mislabeled and drifted.** It is the **DBDO pipeline**, not "design
  principles"; its `source_dd: DD-45` is **Superseded** (→ DD-103); and its feedback-loop diagram
  still describes the dead federation ("Household OS → Claude Build → Household OS"). A cached doc
  anchored to a superseded DD with stale content is exactly the debt the anti-redundancy rule targets.
  Bonus: the name `principles.md` would more honestly belong to a DD-37 cache.

## Proposed caching policy

### Cache a DD's wisdom into `knowledge/` only when ALL four hold

1. **Cross-cutting** — applied by multiple skills/agents (or humans+agents broadly), not owned by one
   skill's procedure.
2. **Reference-shaped** — an agent *reads and judges against* it (a heuristic, model, vocabulary,
   pattern), rather than *executes* it as steps.
3. **Engine self-knowledge** — about how *this* engine is built/operates (the `knowledge/` body),
   distinct from external best-practice (the `extracts/` body).
4. **Stable** — the wisdom is settled, not still-churning process detail (which stays in its owning
   skill so it evolves in one place).

### Exclude (do NOT cache) when ANY hold

- It is a **governance / structural fact** → CLAUDE.md / `governance/` / the DD.
- It is **operationalized inside one owning skill** → that SKILL.md (single source of truth); make the
  skill cite its source DD instead.
- It is **external best-practice** → `extracts/` substrate (Librarian-composed), not DD-derived.

### Anti-redundancy invariant (the inverse direction)

Every cached `knowledge/` doc must (a) carry a `source_dd` that is **Binding** (never Superseded), and
(b) be the **single** agent-readable home for that wisdom. A cache anchored to a superseded DD, or one
that duplicates a skill's procedure, is debt — re-anchor or delete.

## Agent wiring (Owner vs Librarian)

The two bodies map cleanly to the two stewards:

- **`knowledge/` (engine self-knowledge) → Owner.** DD-wisdom caching is derived from governance the
  Owner already stewards (DD-86: consistency, governance, evolution, docs). The same drift-detection
  the Owner runs (`/maintain-docs`, `/translate-governance`, `/system-health`) maintains a cached
  principles doc. `fractal-pattern.md` / `vocabulary.md` / `principles.md` are already Owner-maintained
  governance-derived docs — DD-wisdom caches join that set.
- **`extracts/` + concept docs (`operations/references/`) → Librarian.** The Librarian composes
  external substrate and the abstraction-contract concept docs (audit/design × skill/agent, G1–G9).
  Those are **not** DD-wisdom caches; keep the boundary. The Librarian *consumes* a cached design
  principle when relevant (e.g. DD-37 informing `/design-skill`) but does not author or steward it.

**Conclusion: cached DD-wisdom is Owner-owned.** No new agent surface is needed.

## Recommendation (all gated; nothing done this round)

1. **Do not build a cache-every-DD mechanism.** Evidence shows ~88% of DDs correctly need no separate
   cache. Caching stays a per-item exception justified by the four criteria.
2. **DD-37 → an agent-readable home (highest value).** Two options at gate:
   - (a) Fold the five principles into CLAUDE.md / `governance/agent-rules.md` — fits the
     "apply before system-specific DDs" altitude; or
   - (b) A new `knowledge/reference/design-principles.md` (`source_dd: DD-37`).
   Recommend **(a)** — these are constitution-altitude heuristics agents should meet on entry, not a
   doc they must go fetch.
3. **Fix `principles.md` drift** (hygiene + content): re-anchor `source_dd` DD-45 → DD-103, rename to
   `dbdo-pipeline.md` (honest name; frees `principles.md`), and de-federate the feedback-loop diagram.
4. **DD-62 / DD-74 → watch, don't act** (Rule 11). Cache only when recurring demand appears (an agent
   actually needing Explore/Harden guidance; token-budget being re-litigated). Note only.

## Cross-references

- `2026-06-20-extracts-knowledge-reconciliation.md` — the two-bodies frame this note extends.
- DD-86 (Owner steward), DD-89 (four-zone artifact placement), DD-37 (foundational principles),
  DD-45→DD-103 (the superseded anchor on principles.md), DD-52/DD-107 (correctly-cached wisdom).
- IB-170 — concept-doc / knowledge-folder rationalization (parent backlog item).
