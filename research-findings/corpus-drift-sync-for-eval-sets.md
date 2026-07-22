---
name: 'Corpus-Drift Sync — Eval Sets Must Cover Real Captured Phrasings'
summary: |-
  Plain English: the phrases people actually use to invoke a skill are captured
  live into a corpus; a deterministic check then fails the audit whenever a
  skill's eval set no longer covers what the corpus has accumulated. Real usage
  supplies the test cases; the sync check makes ignoring that supply impossible.
  A missing corpus is a clean pass (fresh hosts legitimately start empty), so the
  check ports without friction.
implementation_notes: |-
  Adopted 2026-07-22 via the meta-skill-eval import (`sync` mode; corpus seam
  mapped to the engine's /self-improve store at operations/self/, currently
  absent = clean pass). The supplier side is the interesting engine gap: the
  /self-improve capture hook already logs queries — routing eval-candidate
  phrasings into a corpus file the sync check reads would close the loop the
  upstream system has (its self-improvement loop harvests phrasings and
  failures; the eval layer turns them into standing regression checks).
category: Evaluation
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Already Adopted
priority: P1 (Implement Now)
applicability:
- General
adopted_in:
- meta-skill-eval (imported 2026-07-22; supplier side not yet wired)
sources:
- careerbuddy-skill-eval-harness.md
proposals: null
date_discovered: '2026-07-22'
last_updated: '2026-07-22'
related_findings:
- file: skill-testing-three-tier-trigger-functional-perf.md
  rel: extends
pipeline_status: raw
tags:
- corpus-drift
- eval-coverage
- live-capture
- failure-driven-coverage
- deterministic-check
---
# Corpus-Drift Sync — Eval Sets Must Cover Real Captured Phrasings

## What It Is

A deterministic check pairing two artifacts: a live-capture corpus of real
invocation phrasings (harvested by the system's self-improvement loop, keyed by
session) and each skill's structured eval set. Every corpus row must appear in
some case's `source` field or in an explicit `corpus_waivers` list; any uncovered
row is drift and fails the audit (exit 1, hookable). Failure moments harvested
from real runs seed the negative-assertion side the same way — every real-world
miss becomes a permanent case row.

## Why It Matters

Eval sets written once from imagination go stale as real usage accumulates
phrasings the authors never anticipated — the upstream system measured exactly
this (sampled sets had drifted from the corpus with no mechanism noticing). The
sync check converts "keep eval sets current" from a discipline into a mechanical
gate, and it encodes the strongest convergent finding across eval practice:
real failures drive coverage, and the prompt set is a living record.

## How It Could Fail

Waivers used as an escape hatch instead of a considered exclusion turn the check
vacuous — waiver additions deserve the same review as case additions. If the
capture side stops running, the check silently passes forever on a frozen corpus;
the supplier and the checker are one loop, not two features. Session-key matching
is only as good as the capture format's stability.
