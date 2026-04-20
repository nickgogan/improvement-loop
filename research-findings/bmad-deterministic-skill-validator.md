---
name: Deterministic Skill Validator
summary: Deterministic inference-based skill validator with 19 rules across 6 categories, CI-integrated, replacing adversarial LLM review for skill quality assurance.
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General / Cross-System
adopted_in: []
sources:
- bmad-v610-v622-changelog.md
related_findings:
- file: llm-as-judge-pattern-for-verification-agents.md
  rel: same-problem
- file: agent-self-reporting-unreliability-independent-eval.md
  rel: same-problem
- file: four-layer-production-eval-stack-with-golden-traces.md
  rel: same-problem
- file: ace-execution-feedback-no-labels-required.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: 2026-04-08
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---
# Deterministic Skill Validator

## What It Is
A deterministic, inference-based validation system for skill files that applies 19 rules across 6 categories: naming conventions, variable usage, path references, invocation syntax, sequence correctness, and encapsulation boundaries. Integrated into CI pipelines to run automatically on skill file changes. Introduced in the BMAD Method to replace adversarial CodeRabbit (LLM-based) review for skill quality assurance. Example rules include REF-03 (skill invocation language correctness) and PATH-05 (skill encapsulation — no leaking of internal paths). In v6.2.0, the validator was used for a validation pass across 32 skill files.

## Why It Matters
LLM-based code review (e.g., adversarial CodeRabbit) is non-deterministic — the same file may pass or fail on different runs, and the review quality depends on prompt engineering and model capability. For a well-defined domain like skill file structure, deterministic rules produce consistent, reproducible results with zero inference cost. The 19-rule, 6-category structure demonstrates that skill quality can be decomposed into checkable invariants rather than requiring holistic LLM judgment. CI integration means violations are caught before merge, not after deployment.

## Why People Are Using It
The BMAD Method found that adversarial CodeRabbit review, while useful for general code review, was outperformed by deterministic validation for the specific domain of skill file correctness. The 19 rules encode the team's accumulated knowledge about what makes a skill file correct — naming, variable scoping, path hygiene, invocation patterns, sequencing, and encapsulation. Running the validator across 32 files in v6.2.0 caught issues that the adversarial LLM review had missed, validating the approach. The deterministic nature also means the rules serve as living documentation of skill file conventions.

## Potential Improvements
The rule set could be extended with severity levels (error vs. warning) to allow progressive adoption. An auto-fix mode for mechanically correctable violations (e.g., naming convention mismatches) would reduce manual remediation. The 6 categories could be made extensible so that individual projects can add domain-specific rule categories without forking the validator.

## Potential Failure Modes
Deterministic rules cannot catch semantic errors — a skill file that passes all 19 structural rules may still produce incorrect behavior when executed. The rule set requires manual maintenance as skill conventions evolve; stale rules produce false positives or miss new violation patterns. Over-reliance on the validator may create a false sense of quality if the rules don't cover the actual failure modes encountered in production.
