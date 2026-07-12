---
name: 'Audit Rubric Carve-Outs — Subjective-Output and Script-Core Skills Get Re-Anchored Eval Dimensions'
summary: 'A scored audit rubric that demands binary pass/fail eval assertions for every skill misdiagnoses two whole skill classes: subjective-output skills (writing voice, tone, design) where forcing assertions onto judgment produces brittle, misleading gates, and script-core skills (renderers, parsers, validators wrapping tested code) where the functional guarantee already lives in the script''s own tests. CareerBuddy''s audit rubric formalizes both as explicit carve-outs that re-anchor the Evaluation Design dimension — while keeping description/trigger optimization mandatory for every skill, because triggering is objective regardless of output type.'
implementation_notes: 'Directly patches a known failure shape in rubric-based assessment: /assess-skill audits against Contract-derived criteria and could score a script-wrapping skill (e.g. /transcript-fetcher, /pdf-to-markdown) or a judgment skill down for lacking an LLM eval suite — exactly the misdiagnosis this carve-out prevents. The re-anchoring move (keep the dimension, swap what a 5/3/1 means for the skill class) is the generalizable mechanic, applicable to any engine rubric with heterogeneous artifact classes. Overlap with the imported /meta-skill-author toolchain''s audit-rubric.md vs /assess-skill is a flagged open question for the restructure program''s Phase 2 audit.'
category: Evaluation
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Not Yet Started
priority: P1 (Direct Adoption)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-meta-skill-author-references.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: raw
consumed_by: []
tags:
- evaluation
- audit-rubric
- skill-authoring
- carve-outs
---

# Audit Rubric Carve-Outs — Subjective-Output and Script-Core Skills Get Re-Anchored Eval Dimensions

## Why It Matters

Uniform rubrics feel rigorous but punish the wrong skills. If your audit demands "binary pass/fail assertions + capability/regression eval split" from *every* skill, then a resume-renderer that wraps a fully tested script fails the audit for not shipping an LLM judge, and a writing-voice skill gets a brittle fake assertion suite bolted on to satisfy the gate. Both outcomes are misdiagnoses that erode trust in the audit itself. The fix is not weakening the rubric — it's class-aware re-anchoring: same dimension, different definition of what a top score means.

## What It Is

Two explicit carve-outs on the Evaluation Design dimension (Specification Engineering, dimension 4) of CareerBuddy's four-discipline audit rubric:

- **Subjective-skill carve-out.** Skills whose primary output is inherently judgment-based (writing style, tone, design, art) are evaluated qualitatively and must NOT be scored down for lacking a functional assertion suite. Mirrors Anthropic's own skill-creator guidance: "Skills with subjective outputs... often don't need [test cases]... don't force assertions onto things that need human judgment." Re-anchored scale: 5 = triggering optimization completed AND a documented qualitative method (named review rubric/scorecard + human-in-the-loop review loop); 3 = one of the two; 1 = neither.
- **Script-core carve-out.** Skills whose core is a deterministic program (renderer, parser, formatter, validator) get their functional guarantee from the script's own tests — asking an LLM judge to re-verify behavior a script already verifies deterministically is itself a misdiagnosis. Re-anchored scale: 5 = triggering optimization completed AND a runnable verification of the program (its tests or a golden-output check) passing alongside structural validation; 3 = one; 1 = neither.

## How It Works

- The binary-assertion and capability/regression requirements still apply in full to skills with objectively verifiable output (file transforms, data extraction, code generation, fixed workflow steps).
- **The invariant that survives every carve-out:** description/trigger optimization is objective and required of *every* skill regardless of output type — a subjective skill can't measure output quality with assertions, but whether it fires on the right queries is always measurable.
- Hybrid skills (deterministic core + genuine LLM judgment, e.g. a script renders but a model selects content) are evaluated on both axes: script tests for the deterministic part, assertions or qualitative review for the judgment part.

## How It Could Fail

Carve-outs are an escape hatch: authors will claim "subjective" to dodge eval work, so classification itself needs a gate (the source anchors it to output type, not author preference). And the script-core carve-out assumes the bundled tests are real and run — a stale test suite converts the carve-out into an unverified pass.
