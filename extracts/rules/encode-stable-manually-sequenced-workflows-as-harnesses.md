---
title: "Encode Stable Manually-Sequenced Workflows as Harnesses"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "ai-shepherding-anti-pattern-manual-workflow-sequencing"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "any operator manually sequencing multi-step agent workflows (invoking each skill or command in order, deciding when to proceed, and kicking off each next step)"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "low — encoding a sequence as a harness requires design work to undo if the sequence changes; individual skill invocations remain available as fallback"
  auditability: "high when harness produces per-step artifacts and logs; low when manual shepherding leaves no durable trace between steps"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Partially Adopted"
    notes: "MetaSystem's research pipeline (research-loop → identify-artifacts → extract-artifacts) is a documented instance of AI shepherding. GSD /autonomous addresses the same problem at a harness level."
contract:
  preconditions: "A multi-step workflow has been run manually at least three times with the same sequence. Each step is a discrete agent skill or command. The sequence is stable (same order, same hand-off points) across runs. At least one step has no required human judgment — it fires automatically when the prior step completes."
  invariants: "A workflow that has run stably three or more times without sequence variation is a harness candidate. Once encoded, the harness handles sequencing, context hand-off, model selection, and branching; the operator only intervenes at declared human gates. Individual skills and MCP servers used within the workflow are not rewritten — they are composed. The diagnostic question 'are you the orchestrator?' must be asked before each manual workflow invocation."
  governance: "Owner: the system or team maintaining the workflow. The rule fires at three confirmed stable runs — not before (first-occurrence tolerance). Harness candidates are filed as IB items and reviewed before encoding. Human gates within the harness are explicit and cannot be removed without a DD. Shepherding is permitted for novel or exploratory sequences that have not yet stabilized."
  recovery: "If a harness step fails → halt the harness, surface the failure with step context, wait for human intervention before retrying. If the underlying sequence changes (new step added, order altered) → pause the harness, update the workflow definition, re-run validation before resuming automation. If a harness encodes a sequence that turns out to require human judgment at every step → decompose back to manual invocation and document the judgment requirement as a finding."
tags:
  - "extracted-artifact"
  - "rule"
  - "harness-engineering"
  - "workflow-automation"
  - "agent-orchestration"
---

# Encode Stable Manually-Sequenced Workflows as Harnesses

**Source:** [[ai-shepherding-anti-pattern-manual-workflow-sequencing]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An operator is manually invoking agent skills or commands in sequence — invoking step 1, waiting for output, invoking step 2, and so on — for a workflow that has run in the same order at least three times. The operator is acting as the orchestrator: remembering what comes next, deciding when to proceed, and kicking off each step. This is the "AI shepherding" pattern.

Scope: applies to any multi-step workflow with a stable sequence, regardless of domain. Does not apply to novel or exploratory sequences where the order is still being discovered.

## Action

**Required:** After three stable runs of the same sequence, evaluate the workflow as a harness candidate. File an IB item. Ask: "Am I the orchestrator here?" If yes and the sequence is stable, design a harness that runs the full sequence end-to-end with explicit human gates at judgment-requiring steps.

**Forbidden:** Continuing to manually sequence a workflow that has run stably three or more times without evaluating it for harnessing. Encoding a harness without preserving explicit human gates at steps that require judgment. Rewriting the underlying skills or MCP servers during harness construction — compose, do not rewrite.

## Boundary

The three-run threshold is the trigger point. Evaluation must happen at or after that threshold, not before. The rule does not prevent manual invocation for runs 1 and 2 (learning the sequence) or for genuinely novel sequences that have not yet stabilized. Exploratory work and harness-eligible work are distinct.

## Enforcement

- **Mechanism:** The diagnostic question "are you the orchestrator?" is asked before each manual multi-step workflow invocation. If the answer is yes and the workflow has run stably three or more times, the operator files an IB item before the next run.
- **Check (deterministic):** `(workflow_run_count >= 3) AND (sequence_stable == true) AND (harness_candidate_filed == false)` → violation.
- **Violation response:**
  - *Below threshold:* no action required; continue manual invocation.
  - *At or above threshold, not yet evaluated:* pause before the next run; file the IB item; schedule the harness design.
  - *Harness built without human gates:* treat as incomplete; add human gates at judgment steps before next run.
- **Self-assessment tool:** Instrument skill invocations to detect recurrence. When the same N-step sequence appears three or more times in session logs, surface it as a harness candidate automatically.

## Rationale

Manual workflow sequencing (AI shepherding) produces four compounding failure modes: process amnesia (a step is skipped), inconsistency (the sequence varies between runs), a human bottleneck (the process only runs when the operator is available), and context fragmentation (structured handoff artifacts are not produced between steps). None of these are unique to AI agents — they are the same failure modes that motivated CI/CD pipelines, make recipes, and runbooks in traditional software engineering.

The three-run threshold is not arbitrary: it distinguishes genuine recurrence from coincidence. A first run discovers the sequence. A second run validates it. A third run establishes a pattern. At three, the marginal cost of another manual run exceeds the fixed cost of encoding a harness.

The key asymmetry: harness construction is a one-time cost. Every subsequent manual run is a recurring cost that compounds. At three runs the crossover point is typically reached for any workflow that will run more than a handful of times.

## Failure Modes

- **Premature harnessing.** Encoding an unstable sequence locks in a workflow before it has been validated. The harness then becomes a maintenance burden. Mitigation: enforce the three-run threshold strictly; do not harness after one or two runs.
- **Over-automating judgment steps.** Removing human gates from steps that genuinely require review. The harness runs without error but produces unreviewed outputs that are accepted silently. Mitigation: human gates are explicit and mandatory; they cannot be removed without a DD.
- **Reliable step chaining of unreliable steps.** Automating a sequence of skills that individually produce inconsistent outputs. The harness runs faster and fails more consistently. Mitigation: validate each step individually before composing into a harness.
- **Diagnostic label as dismissal.** Calling a workflow "AI shepherding" to justify deprioritizing legitimate manual orchestration of novel tasks. The label applies to stable sequences, not to exploratory work. Mitigation: the three-run stability check is required before the label applies.

## Contract

### Preconditions
A multi-step workflow has been run manually at least three times with the same sequence. Each step is a discrete agent skill or command. The sequence is stable (same order, same hand-off points) across runs. At least one step has no required human judgment — it fires automatically when the prior step completes.

### Invariants
A workflow that has run stably three or more times without sequence variation is a harness candidate. Once encoded, the harness handles sequencing, context hand-off, model selection, and branching; the operator only intervenes at declared human gates. Individual skills and MCP servers used within the workflow are not rewritten — they are composed. The diagnostic question "are you the orchestrator?" must be asked before each manual workflow invocation.

### Governance
Owner: the system or team maintaining the workflow. The rule fires at three confirmed stable runs — not before (first-occurrence tolerance). Harness candidates are filed as IB items and reviewed before encoding. Human gates within the harness are explicit and cannot be removed without a DD. Shepherding is permitted for novel or exploratory sequences that have not yet stabilized.

### Recovery
If a harness step fails → halt the harness, surface the failure with step context, wait for human intervention before retrying. If the underlying sequence changes (new step added, order altered) → pause the harness, update the workflow definition, re-run validation before resuming automation. If a harness encodes a sequence that turns out to require human judgment at every step → decompose back to manual invocation and document the judgment requirement as a finding.
