---
name: 'Paired Output Uplift Is a Different Question than Retirement'
summary: |-
  Plain English: running the same execution cases with the skill present and
  with it masked answers two different questions, and conflating them loses
  both. The retirement question — "does the model still need this skill?" —
  reads the masked pass rate alone (≥80% sustained = retire signal). The value
  question — "does this skill actually improve output?" — needs the PAIRED
  comparison: same cases, same model, same harness, matched case-by-case, with
  uplift = with-skill rate minus masked rate. High trigger accuracy proves
  neither; many failures happen after the skill loads.
implementation_notes: |-
  Adopted 2026-07-22 via the meta-skill-eval import (`report --paired` compares
  the latest matched execution and retirement rows by case id — unmatched
  rosters never manufacture a delta) and the meta-skill-author 1.19 sync
  (optional capability-uplift vs encoded-preference classification at eval
  authoring: uplift-class skills are retirement candidates as models improve;
  preference-class skills encode a chosen workflow and are durable — the
  baseline question differs by class). SkillsBench's headline caution applies:
  AI-generated skills can measurably HURT — a negative uplift is a real result,
  not an eval bug, and triggers trajectory diagnosis.
category: Evaluation
evidence_strength: Medium (benchmark-derived — SkillsBench matched-pair methodology; adopted in one production system)
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
- file: generator-assessor-separation-in-skill-iteration.md
  rel: same-problem
pipeline_status: raw
tags:
- paired-evaluation
- output-uplift
- skill-retirement
- ablation
- skillsbench
---
# Paired Output Uplift Is a Different Question than Retirement

## What It Is

A separation of two reads over the same skill-masked run data. **Retirement**
(tier 3): run the execution cases with the skill omitted from every discovery
path; a sustained high masked pass rate (≥80%) signals the model has absorbed
the skill's value — retire it. **Paired output uplift:** match the latest
with-skill execution run and the latest masked run case-by-case (only ids
present in both compare — an unmatched roster never manufactures uplift) and
report the rate delta per skill×model. The classification companion: at
authoring time, optionally class a skill as *capability-uplift* (tests skill
value; retirement-eligible as models improve) or *encoded-preference* (tests
fidelity to a chosen workflow; durable regardless of model capability — masking
it measures the wrong thing).

## Why It Matters

Trigger success is neither a quality proxy nor the right baseline — a skill can
fire perfectly and still produce output no better (or measurably worse) than the
bare model. The paired read is the only honest answer to "is this skill worth
carrying?", and per-model attribution makes it a standing migration tool: a new
model that aces the masked run flips the skill to a retirement candidate with
evidence, not vibes. The negative direction is equally load-bearing: benchmark
data shows heavyweight recipes and displaced native strategies producing
*negative* uplift — a skill that hurts is a finding the paired read surfaces and
nothing else does.

## How It Could Fail

Comparing unmatched case rosters manufactures phantom uplift — matching by case
id is the integrity rule. Masking an encoded-preference skill and reading its
masked failures as "still needed" conflates value classes: the model was never
supposed to reproduce the preference bare. Retirement calls from one run ignore
trial variance; the signal is sustained, not single-shot.
