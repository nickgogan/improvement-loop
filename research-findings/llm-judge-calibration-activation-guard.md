---
name: 'LLM-Judge Calibration Activation Guard — Human Rows First, Deterministic Bias Always'
summary: |-
  Plain English: don't automate grading with an LLM judge until you have enough
  human-scored rows to prove the judge agrees with humans — measured with
  precision/recall (not raw agreement, which flatters judges on imbalanced
  failure classes). Until then, subjective quality is human-scored through a
  typed verdict schema so it still trends in the same ledger as everything else.
  The companion authoring ruling: bias eval cases as far toward deterministic
  checks (regex/string/exit-code) as possible — judge- and human-scored checks
  are a narrow carve-out for genuinely subjective quality, never a default.
implementation_notes: |-
  Adopted 2026-07-22 via the meta-skill-eval import: the `score` mode appends
  human verdicts under judge-verdict schema v1; no LLM judge exists anywhere in
  the harness by design. The activation guard is the engine's answer to "add an
  LLM judge?" — not until precision/recall against accumulated human rows
  validates one, and then one isolated judge per dimension (per the existing
  grading-hierarchy finding), versioned and of a different model family than
  the generator. The deterministic-bias ruling cites DeepMind's finding on how
  far regex-based evals carry.
category: Evaluation
evidence_strength: Medium (practitioner-documented; corroborated by Hamel Husain's eval guidance and DeepMind's regex-eval finding)
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
- file: three-tier-grading-hierarchy.md
  rel: extends
- file: eval-rubric-carve-outs-subjective-and-script-core-skills.md
  rel: extends
pipeline_status: raw
tags:
- llm-as-judge
- judge-calibration
- precision-recall
- deterministic-first
- human-in-the-loop
---
# LLM-Judge Calibration Activation Guard — Human Rows First, Deterministic Bias Always

## What It Is

Two rulings that together bound where model-based grading may enter an eval
system. **The activation guard:** no LLM judge is added until it is calibrated
against accumulated human labels/critiques, using precision and recall per
failure class rather than raw agreement (imbalanced classes make raw agreement
flatter a judge that misses the rare failures that matter). Until that bar is
met, subjective-class output is scored by a human through a typed verdict schema
(overall_pass, 0–100 score, typed failure category, scorecard pointer) appended
to the same attributed ledger as automated verdicts — subjective skills trend
like everyone else, without pretending automation exists. **The deterministic
bias:** case authoring pushes as far toward regex/string/exit-code assertions as
possible, even on subjective-class skills (structure, ban-term, and gate
assertions stay deterministic; only genuine output-quality judgment gets the
human carve-out).

## Why It Matters

The common failure in eval systems is premature judge automation: an uncalibrated
LLM judge produces scores that look like measurement but carry unknown error,
and grading bugs are common and costly (the practice corpus's canonical example:
a benchmark's 42%→95% swing that was grader bugs, not model improvement). The
guard sequences the investment correctly — deterministic checks first (cheap,
debuggable, no calibration debt), human scoring where judgment is genuinely
needed, judge automation only once its accuracy is a measured quantity.

## How It Could Fail

Human scoring that references imagined output corrupts the ledger — the score
mode must refuse verdicts that don't reference a real prior run. If human-scored
rows never accumulate (because scoring feels like overhead), the activation bar
is never met and the guard reads as a permanent "no" — the fix is scoring the
runs that already happen, not lowering the bar. Deterministic bias overdone
forces binary assertions onto genuinely subjective quality, the exact failure the
class carve-outs exist to prevent.
