---
name: 'Typed Output-Failure Taxonomy + Oracle-Validates-the-Verifier'
summary: |-
  Plain English: when an eval fails, record WHICH KIND of failure it was from a
  small fixed taxonomy (incomplete solution, missing output, specification
  violation, below-threshold quality, domain-knowledge gap, safety/governance,
  runtime error) instead of a bare "fail" — typed categories are actionable and
  aggregate into patterns. And before trusting any deterministic verifier,
  validate it with an oracle: a known-good artifact must pass every check, or
  the verifier is broken/overfitted and every verdict it produced is suspect.
implementation_notes: |-
  Adopted 2026-07-22 via the meta-skill-eval import (FAILURE_CATEGORIES enum on
  ledger rows and score mode) and the meta-skill-author 1.19 sync (oracle
  required at case-authoring time where deterministic artifact verification is
  feasible; parsimonious distinct checks). Selective SkillsBench adoption — the
  taxonomy and oracle rule imported, the large benchmark machinery deliberately
  not. The oracle rule generalizes beyond evals: any deterministic checker the
  engine builds (store checks, descriptor checks) should carry a known-good
  fixture that must pass, alongside the seeded violation that must fail.
category: Evaluation
evidence_strength: Medium (benchmark-derived — SkillsBench; adopted in one production system)
adoption_status: Already Adopted
priority: P1 (Implement Now)
applicability:
- General
adopted_in:
- meta-skill-eval (imported 2026-07-22)
- meta-skill-author @1.20.0 (case-authoring rules)
sources:
- careerbuddy-skill-eval-harness.md
proposals: null
date_discovered: '2026-07-22'
last_updated: '2026-07-22'
related_findings:
- file: binary-eval-assertion-design-deterministic-plus-ll.md
  rel: extends
pipeline_status: raw
tags:
- failure-taxonomy
- oracle-validation
- verifier-integrity
- skillsbench
- eval-authoring
---
# Typed Output-Failure Taxonomy + Oracle-Validates-the-Verifier

## What It Is

Two case-authoring rules imported from SkillsBench's verifier methodology.
**Typed failures:** every failing verdict carries one category from a small
closed enum — incomplete-solution, missing-output, specification-violation,
below-threshold-quality, domain-knowledge-gap, safety-or-governance,
runtime-error — recorded on the ledger row, so failure *shape* aggregates across
runs instead of dissolving into free-text badness. **Oracle validation:** where a
deterministic artifact oracle is possible, a known-good artifact must pass every
verifier check before the verifier is trusted; a verifier that fails its oracle
is broken or overfitted, and its historical verdicts are suspect until fixed.
Companion discipline: parsimonious distinct checks — each check tests one thing,
overlapping checks merge.

## Why It Matters

A bare "fail" forces a transcript read to learn anything; a typed category makes
the ledger queryable by failure shape ("this skill's failures are mostly
domain-knowledge gaps — the skill body needs content, not better triggering").
The oracle rule protects the foundation: verifiers are code, code has bugs, and
a buggy verifier silently converts good output into recorded failure (or worse,
the reverse). Validating the checker with a known-good case is the cheapest
insurance an eval system can buy.

## How It Could Fail

A taxonomy that grows loses its aggregation value — the enum stays closed and
small, with `uncategorized` as the pressure valve. Oracle fixtures that drift
from what "good" currently looks like start failing healthy verifiers; the
fixture is maintained with the verifier, not filed and forgotten. Categories
assigned carelessly at authoring time (everything "specification-violation")
produce clean-looking but meaningless aggregates.
