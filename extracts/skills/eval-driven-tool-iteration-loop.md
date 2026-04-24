---
title: "Eval-Driven Tool Iteration Loop"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "eval-driven-tool-iteration-loop"
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic coding systems with tool interfaces that can be iteratively refined"
    - "teams building or maintaining MCP tool definitions, skill procedures, or agent APIs"
    - "any workflow where agent tool performance is measurable via transcripts"
  platform_coupling: "specific:claude-code"
  autonomy: "hitl-only"
  stage: "verify"
  reversibility: "medium — refactoring changes tool interfaces and implementations; rollback requires reverting to prior implementation; held-out test set provides the safety net"
  auditability: "high — transcript corpus, refactoring rationale document, and before/after metric delta report are all preserved as first-class artifacts"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Anthropic internally applied this process to Slack MCP tools, which outperformed human-written baselines after agent-driven refactoring."
contract:
  preconditions: "Prototype tool is implemented and locally validated. Evaluation task set is defined, diverse, and representative. Held-out test set is prepared and sequestered."
  invariants: "Held-out test set is never used during optimization phases. Every refactoring cycle is followed by a held-out test run. Transcript corpus is preserved as an artifact."
  governance: "Owner: MetaSystem / Claude Build system. Human gate required before deploying a refactored tool to production. Based on Anthropic internal process."
  recovery: "If held-out validation fails: discard the refactoring, expand the evaluation task set, re-run from scratch. If transcript corpus is too small: run additional evaluation trials before refactoring."
tags:
  - "extracted-artifact"
  - "skill"
---

# Eval-Driven Tool Iteration Loop

**Source:** [[eval-driven-tool-iteration-loop]]
**Form:** skill
**Extraction date:** 2026-04-19

## Purpose

A three-phase iterative process for developing and refining agent tools by running evaluations with realistic multi-step tasks, analyzing transcripts, and using Claude Code to drive tool refactoring. Based on Anthropic's internal process — Slack MCP tools improved beyond human-written baselines after Claude-driven optimization.

## Inputs

- Prototype tool implementation (code, schema, documentation)
- Evaluation task set: realistic multi-step tasks representative of actual agent use
- Held-out test set (separate from evaluation; never used during optimization)
- Metrics definition: accuracy, runtime, tool call count, token consumption, error rate
- Claude Code access for transcript analysis and tool refactoring

## Outputs

- Refined tool implementation with measurable improvement on evaluation metrics
- Concatenated transcript corpus used for refactoring
- Refactoring rationale document
- Held-out test set results confirming generalization
- Delta report: before/after metric comparison

## Steps

**Phase 1: Prototype and Local Validation**

1. Build prototype tools. Define the tool's interface, schema, and documentation.
2. Test locally against simple, deterministic cases.
3. Document the prototype's known limitations and design assumptions.

**Phase 2: Evaluation**

1. Run the evaluation task set against the prototype. Tasks must be realistic and multi-step.
2. Collect transcripts for every evaluation run: tool calls, sequences, arguments, responses, errors, outcomes.
3. Record metrics per run: accuracy, runtime, tool call count, token consumption, error rate.
4. Do not use the held-out test set during this phase.

**Phase 3: Claude Code-Driven Refactoring**

1. Concatenate all evaluation transcripts into a single corpus.
2. Feed the corpus to Claude Code with a refactoring prompt: identify patterns, surface consolidation opportunities, flag unexpected sequences, recommend interface changes.
3. Review recommendations. Prioritize changes observed across multiple transcripts.
4. Implement the recommended refactoring.
5. Re-run the evaluation task set. Confirm metric improvement.
6. Run the held-out test set. Confirm generalization.
7. Iterate phases 2-3 until diminishing returns or held-out set plateau.

## Failure Modes

- **Evaluation task overfitting.** Mitigate with a large, diverse, realistic task set and mandatory held-out validation.
- **Eval-specific shortcuts.** Review transcripts manually for shortcut patterns before accepting recommendations.
- **Transcript corpus size.** Too few transcripts produce low-signal recommendations.
- **Metric gaming.** Define a balanced metric set before Phase 2 begins.
- **Refactoring regression.** Held-out test set is the primary guard; supplement with edge case tests.

## Contract

### Preconditions
Prototype tool is implemented and locally validated. Evaluation task set is defined, diverse, and representative. Held-out test set is prepared and sequestered.

### Invariants
Held-out test set is never used during optimization phases. Every refactoring cycle is followed by a held-out test run. Transcript corpus is preserved as an artifact.

### Governance
Owner: MetaSystem / Claude Build system. Human gate required before deploying a refactored tool to production. Based on Anthropic internal process.

### Recovery
If held-out validation fails: discard the refactoring, expand the evaluation task set, re-run from scratch. If transcript corpus is too small: run additional evaluation trials before refactoring.
