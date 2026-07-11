---
name: "Meta-Skill Authoring Prior Carries Most of the Gain — Dedup Machinery Unnecessary"
summary: |-
  Constraining HOW skills get written matters more than any downstream cleanup mechanism: in the Ratchet Recipe ablations, removing the meta-skill authoring prior cost 57% of the total gain — the single most valuable component — while removing explicit deduplication (canonicalization, cover-guard clustering) actually slightly IMPROVED results. A strong authoring prior enforces structural homogeneity at skill birth, making dedup machinery redundant and its false positives avoidable. Strong empirical support for our existing bet: invest in design-skill/template substrate (the authoring prior) rather than building dedup or canonicalization layers.
implementation_notes: |-
  Flagged P2 because it validates and sharpens an active engine direction: the design-skill
  Template skeleton and guide substrate ARE an authoring prior; this finding says that layer is
  where the leverage lives. Ablation numbers (share of Default gain): no meta-skill = 57% loss
  (largest single component); no canonicalization = 114% (exceeds Default); no cover-guard dedup
  clusters = 111% (exceeds Default). Refreshing the meta-skill every 10 rounds bought the highest
  peak but +55% wall time — marginal gain unwarranted. Design consideration: before anyone proposes
  dedup/canonicalization machinery for findings or extracts, this is the evidence that a stronger
  authoring template is the cheaper, better-performing alternative. Also consistent with the
  engine's "abstractions must earn their keep" rule — the dedup layer is an abstraction that
  measurably fails to earn its keep once the prior exists.
category: "Agent Design"
evidence_strength: "Medium (empirical benchmarks)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "arxiv-skill-library-drift-ratchet-recipe.md"
related_findings:
  - file: "skill-self-improvement-three-approaches.md"
    rel: "extends"
  - file: "ratchet-recipe-skill-retirement.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

# Meta-Skill Authoring Prior Carries Most of the Gain — Dedup Machinery Unnecessary

## What It Is

An ablation result from arXiv 2605.19576: within the three-mechanism Ratchet Recipe, the **meta-skill authoring prior** — a document constraining the skill synthesizer to produce stylistically and structurally consistent skills — is the single most valuable component. Removing it (ablation A3) loses 57% of the total gain (−0.141 absolute). Meanwhile, the explicit deduplication mechanisms are not just unnecessary but mildly counterproductive: removing canonicalization (A5) scored 114% of Default, and removing cover-guard dedup clustering (A6) scored 111%. The authoring prior already enforces enough homogeneity that explicit filtering only adds false positives. Refreshing the meta-skill every 10 rounds (A8) produced the highest peak (0.725) but at 55% more wall time — judged not worth it.

## Why It Matters

This inverts the intuitive investment order for library health. The instinct is to build cleanup machinery — dedup passes, canonicalization, similarity clustering — for artifacts already in the bank. The evidence says: constrain the generator instead. For this engine, the authoring prior maps directly onto the `/design-skill` Template skeleton, the guide substrate, and finding/extract templates; the finding is empirical backing that strengthening those is worth more than any proposed dedup layer over findings or extracts. It also quantifies a live instance of "abstractions must earn their keep": the dedup abstraction measurably fails to, once the prior exists.

## Why People Are Using It

The result explains, in one mechanism, why human-curated skills outperform ungoverned LLM-authored ones (+16.2pp vs +0.0pp in SkillsBench): human curation implicitly applies an authoring prior. Encoding that prior as an explicit meta-skill document recovers most of the benefit without per-skill human effort.

## Potential Improvements

- Test whether the dominance holds outside single-benchmark code tasks (authors flag multi-step agents and broader domains as future work).
- Characterize what makes an authoring prior effective — the paper shows *that* it works, not which properties (structure, style, scope constraints) carry the effect.

## Potential Failure Modes

- **Prior ossification**: a fixed authoring prior can encode yesterday's conventions; the A8 refresh ablation shows periodic refresh helps peaks but costs heavily — the refresh cadence is a real tradeoff, not free.
- **Overgeneralization**: "dedup unnecessary" is demonstrated *given* a strong prior over homogeneous, machine-authored skills; a heterogeneous human+machine library may still need reconciliation passes.
- **Prior-retirement interaction**: skills authored under an old prior may score poorly under a new one and be retired for style rather than substance.
