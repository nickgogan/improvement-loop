---
name: 'Attributed Pass-Rate Ledger with Model Provenance'
summary: |-
  Plain English: every eval run appends one row per case×trial to an append-only
  ledger, and every row records which model, which skill version, which eval-set
  version, and which harness version produced it — so when a pass rate moves, the
  cause is always attributable to exactly one thing that changed, never
  confounded. The ledger then answers lifecycle questions as queries: capability
  evals graduate to regression at sustained full-pass, saturation flags at three
  consecutive 100% runs, and a model migration becomes an experiment (re-run the
  suites under the candidate model, diff against the ledger's baselines,
  regressions surface as named failing cases).
implementation_notes: |-
  Adopted 2026-07-22 via the meta-skill-eval import (ledger at
  operations/evals/ledger.jsonl; harness rows carry harness "claude-code" +
  harness_version "2.0.0-claude.1"). The migration read matters most for this
  engine's E4/E7 fitness loop: per-model retirement ("does model X still need
  this skill") is answerable from evidence when new model versions land, and
  volatile pass-rate numbers are never copied into tracked docs — run `report`
  when a number is needed (no-hardcoded-counts alignment).
category: Evaluation
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Already Adopted
priority: P1 (Implement Now)
applicability:
- General
adopted_in:
- meta-skill-eval (imported 2026-07-22)
sources:
- careerbuddy-skill-eval-harness.md
proposals: null
date_discovered: '2026-07-22'
last_updated: '2026-07-22'
related_findings:
- file: skill-testing-three-tier-trigger-functional-perf.md
  rel: extends
- file: manifest-hash-drift-detection-for-derived-docs.md
  rel: same-problem
pipeline_status: raw
tags:
- pass-rate-ledger
- model-provenance
- eval-attribution
- model-migration
- capability-regression-lifecycle
---
# Attributed Pass-Rate Ledger with Model Provenance

## What It Is

An append-only JSONL ledger where every eval run writes one row per case×trial,
each carrying full attribution: timestamp, run id, harness + CLI version, skill +
skill version, eval-set version, harness version, model + model-resolution source,
reasoning effort, tier, verdict, typed failure category, per-check results, and
transcript path. Eval sets version at their own rhythm (a `version` field bumped
on semantic case changes, without forcing skill semver bumps). Corrections are new
rows — the ledger is never rewritten.

## Why It Matters

Without attribution, a pass-rate shift is unexplainable: did the skill change, the
model, the eval set, or the harness? With one attributed row per trial, every
trend read decomposes cleanly, and three hard questions become cheap queries:
**graduation** (capability → regression at sustained full-pass; alert on any drop
after), **saturation** (a 100% eval gives no improvement signal — flag it), and
**model migration** (re-run suites under the candidate model, diff baselines,
run the retirement tier both ways — a per-skill fix/keep/retire gap map with
evidence attached, instead of a leap of faith).

## How It Could Fail

Copying volatile pass-rate numbers into tracked docs recreates the hardcoded-count
maintenance tax the ledger exists to avoid. Hand-editing or pruning rows destroys
the attribution guarantee. Skipping the eval-set version bump on semantic case
changes silently confounds trend reads — the discipline is only as good as the
version hygiene feeding it.
