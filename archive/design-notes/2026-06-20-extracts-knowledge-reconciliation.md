---
title: "extracts/ ↔ knowledge/ reconciliation — live-vs-orphaned audit + recommended model"
id: "extracts-knowledge-reconciliation"
type: "design-note"
category: "knowledge-architecture"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-06-20"
updated: "2026-06-20"
author: "claude"
source_ib:
  - "IB-170"
tags:
  - "design-note"
  - "extracts"
  - "knowledge"
  - "librarian-substrate"
  - "rule-11"
---

# extracts/ ↔ knowledge/ reconciliation

## The question

The DD-80 pipeline frames `extracts/` as a **staging area** ("stage before deploying", DD-39/DD-80)
and `knowledge/` as the **deployed destination**. In practice the staging→deploy flow barely ran,
yet `extracts/` is heavily populated and — critically — `extracts/guides/` became the Librarian's
**live Tier-1 substrate**. So the staging label no longer describes what `extracts/` is. This note
audits what `extracts/` actually holds (live substrate vs. orphaned drafts), reframes the
`extracts/` ↔ `knowledge/` relationship, and recommends a target model. **No files move on this
note** — it is the gate input for that decision (per session 124, Nick chose "investigate first").

## Method

For each `extracts/` subtree, count artifacts and test whether each is **slug-referenced by a live
consumer** — defined as: `.claude/skills/` (engine + workspace root), `operations/references/`
(concept docs, guide-routing-table, form-rubric, consumer-abstractions-map), `agents/`,
`governance/`, `knowledge/` (schematics `grounded_in`, patterns, guides, reference), and the
CLAUDE.md / PROGRESS.md set. **Excluded** as non-demand: append-only history (system-log, handoffs,
research-reports, design-notes, DDs) and the `extracts/` tree itself.

"Slug-referenced" = the artifact's filename stem appears in a live file. This **undercounts**
substrate that is reached by *dimension/tag* rather than by filename (see caveat below).

## Findings

| Subtree | Total | Slug-referenced by a live consumer | Orphaned (no slug ref) |
|---|---:|---:|---:|
| **guides** | 14 | **14 (100%)** | 0 |
| patterns | 70 | 7 (10%) | 63 |
| rules | 68 | 5 (7%) | 63 |
| skills | 27 | 2 (7%) | 25 |
| templates | 24 | 0 | 24 |
| agents | 2 | 0 | 2 |

Slug-pinned non-guide artifacts (the live tail):
- **patterns (7):** `context-rot-attention-budget-depletion`, `autonomy-gradient-not-binary-delegation`,
  `prompt-caching-for-stable-agent-context`, `effort-scaling-rules-embedded-in-orchestrator`,
  `tool-shaped-object-evaluation-lens`, `acceptance-criteria-as-verifiable-eval-anchor`,
  `independent-eval-and-scoped-authority` — cited by concept docs and the workcell schematics.
- **rules (5):** cited by `/extract-artifacts`, `/finding-crosslink`, the form-rubric, a schematic,
  a codifier reflection.
- **skills (2):** `agentic-harness-self-assessment` (form-rubric), `multi-agent-proportional-content-summarization`
  (concept docs).

### Caveat — orphaned ≠ dead

The concept docs reference patterns/findings at **Tier 2 by category and dimension**, not by filename
(e.g. `skill.md` §Composition: *"Tier 2 (patterns / findings)"*; `harness.md`: *"Patterns under the
Tools dimension"*). So the 63 "orphaned" patterns are still reachable as Tier-2 substrate via a
tag/dimension browse — they are **un-pinned, not unused**. The same is **not** true for
rules/skills/templates/agents: the Librarian composes **guides + patterns + findings**; it does not
compose extracted *rules/skills/templates* as substrate. For those subtrees, orphaned really does
mean "un-promoted draft."

## The reframed model — two bodies, three substrate tiers

`extracts/` and `knowledge/` are **not the same artifacts at two pipeline stages**. They are two
different bodies of knowledge that happen to share folder names (`guides/`, `patterns/`, `templates/`):

- **`extracts/` = the research-substrate library** — distilled external best-practice on agentic
  coding. It is what the Librarian advisory layer (`/assess-*`, `/design-*`, `/ask-kb`,
  `/audit-artifacts`) composes. It is **product/substrate, consumed pull-style — not a drafts staging
  bin.**
- **`knowledge/` = the engine's self-knowledge** — how *this* engine is built and operates
  (`reference/` fractal-pattern, principles, vocabulary; `schematics/`; the curated `patterns/`
  capability-type-selection + upstream-dependency-spectrum; `guides/` pipeline + SKILL.md mechanics;
  `templates/` scaffolding).

Within the substrate body the audit reveals three tiers:

| Tier | Subtree | Access pattern | Status |
|---|---|---|---|
| **Tier 1 — composed directly** | `extracts/guides/` (14) | slug-referenced from concept docs, guide-routing-table, skills | **Live substrate.** The "staging" label is simply wrong here. |
| **Tier 2 — browsed by dimension** | `extracts/patterns/` (70) | category/tag/dimension browse; ~10% slug-pinned | **Live corpus.** Individual files un-pinned but reachable. |
| **Staging residue** | `extracts/{rules,skills,templates,agents}/` (121) | ~5% slug-pinned; not composed as substrate | **Un-promoted drafts.** The staging→deploy flow that never ran. |

## Recommended target

A two-part move, each gated separately:

1. **Recognize `extracts/guides/` + `extracts/patterns/` as substrate, not staging.** The cleanest
   expression is to stop calling `extracts/` a staging area and name it for what it is. Two ways to
   do that — pick one at gate time:
   - **(1a) Rename in place (framing-only).** Keep paths; rewrite the pipeline guide + `extracts/CLAUDE.md`
     + DD-80 framing so guides/patterns are documented as the Librarian's substrate library, and only
     `rules/skills/templates/agents` are "staging." **Zero pointer churn** (~15 live substrate refs
     stay valid). Lowest risk. Rule-11-faithful (fixes the incoherence with words, tolerates the
     folder name).
   - **(1b) Relocate to a substrate home.** Move `extracts/guides/` + `extracts/patterns/` to a
     first-class home (e.g. `knowledge/substrate/` or a renamed top-level `substrate/`). Cleaner
     conceptual map, but rewrites ~15 live pointers across concept docs + skills + the
     guide-routing-table — a spec'd migration of its own. Higher risk.
2. **Promote-or-prune the staging residue** (`rules/skills/templates/agents`, ~121 files, ~5% pinned).
   This is the genuine un-promoted backlog. Recommended handling: a follow-up review pass that, per
   subtree, either (a) promotes the few that earn a live home (`.claude/rules/`, `.claude/skills/`,
   `knowledge/templates/`) or (b) leaves them as an explicitly-labeled **harvest archive** — raw
   finding-derivatives kept for future `/synthesize-guide` input, not pretending to be deployable.
   Do **not** silently delete: each traces to a source finding.

**Recommendation:** **1a + a scoped promote-or-prune pass (2).** It resolves the actual incoherence
(substrate mislabeled as staging) at near-zero risk, and quarantines the real backlog without a
high-churn relocation. Reserve 1b for a later dedicated migration only if the folder name keeps
causing confusion (Rule 11: wait for recurrence before paying the move cost).

## Open decisions for Nick (gates)

1. **Substrate framing: 1a (rename in place) or 1b (relocate)?** — recommend **1a**.
2. **Staging residue: promote-or-prune now, or defer to its own session?** The audit gives the
   work-list; the pass itself is sizable (121 files).
3. **Does `knowledge/patterns/` (2 curated) stay separate from `extracts/patterns/` (70 substrate),
   or merge?** They serve different roles (engine self-knowledge vs. research substrate) — recommend
   keep separate, cross-link.

## Relationship to IB-170 (concept-doc placement)

IB-170's original symptom — concept docs split between `operations/references/librarian/` and
`knowledge/reference/harness.md` — is a **sub-case of this same two-bodies confusion**: the Librarian
substrate (concept docs, routing tables) lives under `operations/references/`, while engine
self-knowledge lives under `knowledge/`. Resolving the `extracts/` ↔ `knowledge/` model first gives a
principled frame for the concept-doc question (substrate vs. self-knowledge), so IB-170's placement
decision should follow this note, not precede it.

## Cross-references

- DD-80 (pipeline simplification), DD-39 (stage-before-deploy), DD-29 (human gates).
- `knowledge/guides/research-to-codification-pipeline.md` — the pipeline doc (Current State updated
  session 124 to point here).
- `operations/references/consumer-abstractions-map.md` — the abstraction demand map (altitudes).
- IB-170 — concept-doc / agent-helper / knowledge-folder rationalization (the parent backlog item).
