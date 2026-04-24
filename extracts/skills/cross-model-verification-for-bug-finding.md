---
title: "Cross-Model Verification for Bug Finding"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "cross-model-verification-for-bug-finding"
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic code review pipelines where high-precision bug detection is required"
    - "multi-model agent harnesses with access to at least two distinct LLM providers"
    - "high-value review surfaces where false negatives carry significant risk"
  platform_coupling: "specific:claude-code"
  autonomy: "hitl-only"
  stage: "verify"
  reversibility: "trivial — skill produces a structured findings report; no code is modified"
  auditability: "high — disagreement signal is a first-class output; all findings are classified by inter-model agreement and preserved as artifacts"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "Codex headless mode is available and budgeted. Claude Code sub-agent spawning is available. Review surface is scoped before invocation. Sub-agents execute in parallel with no shared state during the finding phase."
  invariants: "Finding phase and verification phase remain strictly separated — no sub-agent reads another sub-agent's output until finding is complete. Disagreement signal is never discarded; it is always surfaced as a first-class output. Human review is required for all disagreement-class findings before any remediation action."
  governance: "Owner: MetaSystem / Claude Build system. Modification requires a Design Decision if the verification protocol or sub-agent count changes. Human gate is mandatory before acting on any bug list produced by this skill."
  recovery: "If Codex headless is unavailable: fall back to single-model (Claude-only) fleet review; document the fallback in the output header; treat all findings as low-confidence. If sub-agent independence is violated: discard the affected finding batch and re-run with corrected isolation."
tags:
  - "extracted-artifact"
  - "skill"
---

# Cross-Model Verification for Bug Finding

**Source:** [[cross-model-verification-for-bug-finding]]
**Form:** skill
**Extraction date:** 2026-04-19

## Purpose

A fleet review skill that deploys parallel sub-agents from two distinct models — Claude Code and Codex (headless mode) — to find bugs independently, then cross-verifies each model's findings using the other model as verifier. Exploits differing model blind spots to achieve higher-precision bug detection than any single-model approach.

## Inputs

- Target codebase or diff under review
- Access to Claude Code (3 sub-agent slots)
- Access to Codex in headless mode (3 sub-agent slots)
- Scope definition: files, modules, or change surface to review
- Bug classification taxonomy (optional; improves cross-verification alignment)

## Outputs

- **High-confidence bug list:** Bugs confirmed by both models
- **Human-attention list:** Bugs where one model confirmed and the other refuted (disagreement signal)
- **Low-confidence list:** Bugs found by only one model, not yet cross-verified
- **Disagreement summary:** Structured record of all inter-model conflicts with context

## Steps

1. **Scope definition.** Define the review surface: specific files, a diff, or a module boundary. Ambiguous scope inflates token cost without proportional benefit.

2. **Parallel independent finding.** Spawn three Claude sub-agents and three Codex sub-agents concurrently. Each sub-agent independently searches the review surface for bugs. Sub-agents must not share findings during this phase — independence is required for the disagreement signal to be meaningful.

3. **Findings aggregation.** Collect all findings from each model fleet. Deduplicate within each fleet. Produce two lists: Claude findings, Codex findings.

4. **Cross-model verification.** Pass Claude's findings to Codex verifiers. Pass Codex's findings to Claude verifiers. Each verifier assesses whether the bug is real, a false positive, or indeterminate.

5. **Signal classification.** Classify each finding by inter-model agreement:
   - Both confirm → high-confidence bug
   - One confirms, one refutes → disagreement; escalate to human review
   - Both refute → discard
   - Only one model found it, other is indeterminate → low-confidence; include with flag

6. **Output assembly.** Produce structured output per the Outputs section. Preserve the disagreement summary as a first-class artifact.

## Failure Modes

- **Correlated blind spots.** Both models may share blind spots on certain bug classes. Cross-verification catches divergent biases, not shared ones.
- **Token cost.** Running six sub-agents plus verification approximately doubles or triples token expenditure. Apply to high-value review surfaces only.
- **Codex headless availability.** Skill degrades to single-model fleet review; disagreement signal is lost.
- **Verification drift.** Verifiers may assess findings differently depending on prompt framing.

## Contract

### Preconditions
Codex headless mode is available and budgeted. Claude Code sub-agent spawning is available. Review surface is scoped before invocation. Sub-agents execute in parallel with no shared state during the finding phase.

### Invariants
Finding phase and verification phase remain strictly separated — no sub-agent reads another sub-agent's output until finding is complete. Disagreement signal is never discarded; it is always surfaced as a first-class output. Human review is required for all disagreement-class findings before any remediation action.

### Governance
Owner: MetaSystem / Claude Build system. Modification requires a Design Decision if the verification protocol or sub-agent count changes. Human gate is mandatory before acting on any bug list produced by this skill.

### Recovery
If Codex headless is unavailable: fall back to single-model (Claude-only) fleet review; document the fallback in the output header; treat all findings as low-confidence. If sub-agent independence is violated: discard the affected finding batch and re-run with corrected isolation.
