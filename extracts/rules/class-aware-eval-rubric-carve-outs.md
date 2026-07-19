---
title: "Class-Aware Eval Rubric Carve-Outs"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "eval-rubric-carve-outs-subjective-and-script-core-skills"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "verifying-agent-output.harvest-queue"
identification_report: "verifying-agent-output.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "scored audit or quality rubrics applied uniformly across a population of skills, tools, or artifacts with different output types"
    - "assessment tooling that risks penalizing judgment-based or script-wrapping artifacts for lacking a binary assertion suite"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "trivial — a scoring-rubric amendment; re-scoring already-audited artifacts under the corrected rubric is the only migration cost"
  auditability: "high — each carve-out's re-anchored scale is itself binary-checkable (does a named qualitative review method exist? does a runnable test or golden-output check exist?)"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "A scored audit or eval rubric evaluates a population of skills, tools, or similar artifacts against a uniform binary pass/fail assertion-suite requirement, and that population includes both subjective-output artifacts (judgment-based output such as tone, design, or writing voice) and script-core artifacts (a deterministic program wrapped by the artifact, already covered by its own tests)."
  invariants: "Subjective-output artifacts are never scored down for lacking a functional assertion suite; they are instead scored on a documented qualitative method (a named review rubric or scorecard plus a human-in-the-loop review step). Script-core artifacts are never required to carry an additional LLM-judge eval suite duplicating what the wrapped program's own tests already verify; they are scored on a runnable verification of the program (its tests or a golden-output check) alongside structural validation. Description/trigger optimization remains mandatory and is scored identically for every artifact regardless of output class, because triggering correctness is always objectively measurable. Hybrid artifacts (deterministic core plus genuine judgment) are scored on both axes independently."
  governance: "Owner: whoever maintains the audit/eval rubric. Classifying an artifact as subjective-output or script-core is not left to the artifact's own author claim — the rubric documents the output-type criterion the classification must satisfy, and an auditor applies it against the artifact's actual behavior."
  recovery: "If an artifact is scored down under the uniform binary-assertion requirement despite qualifying for a carve-out, correct the score using the class-appropriate re-anchored scale rather than accepting the misdiagnosis. If a carve-out is claimed but the artifact does not actually meet the class criterion (e.g., a 'script-core' artifact's bundled tests are stale or do not run), treat the carve-out as forfeited and apply the standard rubric until the underlying test suite is restored to a runnable state."
tags:
  - "extracted-artifact"
  - "rule"
  - "eval-rubric"
  - "skill-audit"
---

# Class-Aware Eval Rubric Carve-Outs

**Source:** [[eval-rubric-carve-outs-subjective-and-script-core-skills]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A scored audit or eval rubric applies a uniform "binary pass/fail assertion suite required" criterion across a heterogeneous population of skills or similar artifacts, and the population includes artifacts whose output is inherently judgment-based (subjective-output) and/or artifacts whose core is a deterministic, already-tested program (script-core).

## Action

**Required:** Re-anchor the evaluation-design dimension per artifact class rather than applying one fixed definition of a top score to every artifact:
- **Subjective-output artifacts:** score on a documented qualitative method. Top score requires triggering optimization completed AND a named review rubric/scorecard with a human-in-the-loop review loop. Do not require a functional assertion suite.
- **Script-core artifacts:** score on a runnable verification of the underlying program. Top score requires triggering optimization completed AND a runnable verification (the program's own tests, or a golden-output check) passing alongside structural validation. Do not require a separate LLM-judge eval suite that duplicates the script's own test coverage.
- **Every artifact, regardless of class:** description/trigger optimization is mandatory and scored the same way — this is always objectively measurable.
- **Hybrid artifacts** (deterministic core plus genuine LLM judgment over part of the output): score both axes independently — script tests for the deterministic part, assertions or the qualitative method for the judgment part.

**Forbidden:** Scoring a subjective-output artifact down solely for lacking binary assertions. Requiring a script-core artifact to duplicate its own program's test coverage with an LLM-judge suite. Accepting a "subjective" or "script-core" classification claim without checking it against the artifact's actual output type and test state.

## Boundary

Enforced at the point an audit or assessment rubric scores the Evaluation Design (or equivalent) dimension of a skill, tool, or artifact. Applies to any rubric maintaining binary-assertion or capability/regression requirements across a heterogeneous artifact population.

## Enforcement

- **Mechanism:** the rubric's scoring guide states the two carve-out scales explicitly, alongside the standard scale, keyed to a documented classification test (output type: judgment-based vs. deterministic-with-tests vs. objectively-verifiable).
- **Check (deterministic):** for a claimed subjective-output carve-out — does a named qualitative review method with a human-in-the-loop step exist? For a claimed script-core carve-out — does a runnable test or golden-output check for the wrapped program exist and pass? Either "no" forfeits the carve-out for that artifact.
- **Violation response:** re-score the artifact under the applicable carve-out (if a misdiagnosis is found) or under the standard rubric (if a forfeited carve-out is found).

## Rationale

A uniform rubric feels rigorous but punishes the wrong artifacts: forcing binary assertions onto genuinely judgment-based output produces a brittle, misleading gate bolted on to satisfy the audit rather than to measure anything real; forcing an LLM-judge suite onto a script-core artifact asks a model to re-verify behavior its own tests already verify deterministically. Both outcomes are misdiagnoses that erode trust in the audit itself. The fix is not a weaker rubric — it is the same dimension re-anchored to what a top score actually means for that artifact class, while keeping the one criterion that is always objective (does it trigger correctly) mandatory for everyone.

## Failure Modes

- **Classification gaming.** Authors claim "subjective" or "script-core" to dodge eval work; the classification must be checked against the artifact's actual output type and test state by an auditor, not accepted on the author's assertion.
- **Stale-test carve-out laundering.** The script-core carve-out assumes the bundled tests are real and currently run; a stale or broken test suite converts what should be a real functional guarantee into an unverified pass. Verify the tests run, not just that they exist.
- **Over-broad hybrid classification.** An artifact with even a small amount of genuine judgment can be mis-filed as pure script-core to avoid the qualitative-method requirement on that portion — hybrid artifacts need both axes evaluated, not the more convenient one.

## Contract

### Preconditions
A scored audit or eval rubric evaluates a population of skills, tools, or similar artifacts against a uniform binary pass/fail assertion-suite requirement, and that population includes both subjective-output artifacts (judgment-based output such as tone, design, or writing voice) and script-core artifacts (a deterministic program wrapped by the artifact, already covered by its own tests).

### Invariants
Subjective-output artifacts are never scored down for lacking a functional assertion suite; they are instead scored on a documented qualitative method (a named review rubric or scorecard plus a human-in-the-loop review step). Script-core artifacts are never required to carry an additional LLM-judge eval suite duplicating what the wrapped program's own tests already verify; they are scored on a runnable verification of the program (its tests or a golden-output check) alongside structural validation. Description/trigger optimization remains mandatory and is scored identically for every artifact regardless of output class, because triggering correctness is always objectively measurable. Hybrid artifacts (deterministic core plus genuine judgment) are scored on both axes independently.

### Governance
Owner: whoever maintains the audit/eval rubric. Classifying an artifact as subjective-output or script-core is not left to the artifact's own author claim — the rubric documents the output-type criterion the classification must satisfy, and an auditor applies it against the artifact's actual behavior.

### Recovery
If an artifact is scored down under the uniform binary-assertion requirement despite qualifying for a carve-out, correct the score using the class-appropriate re-anchored scale rather than accepting the misdiagnosis. If a carve-out is claimed but the artifact does not actually meet the class criterion (e.g., a "script-core" artifact's bundled tests are stale or do not run), treat the carve-out as forfeited and apply the standard rubric until the underlying test suite is restored to a runnable state.
