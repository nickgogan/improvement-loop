---
title: Iterative Refinement Loop with Quality Gate
type: extracted-artifact
assigned_form: skill
source_finding: iterative-refinement-loop-with-quality-gate
extraction_date: '2026-04-26'
identification_report: 2026-04-26-identification-report.md
deployed: false
deployed_to: null
context:
  applies_to:
  - skills or workflows that produce quality-sensitive outputs where single-pass generation is unreliable (customer responses, compliance summaries, structured reports, generated code)
  - any agent pipeline that needs an internal quality gate without requiring human review of every output
  - teams that want measurable, auditable evidence of output quality rather than relying on human spot-checks
  platform_coupling: agnostic
  autonomy: all
  stage: verify
  reversibility: trivial — the skill is a prompt-level pattern; removing it from a workflow requires no migration and leaves no persistent state
  auditability: high when iteration logs are retained and stored externally; low when scores are only surfaced inline in non-logged sessions — the log destination field is the key compliance control
  evidence_strength: Strong
  adoption:
    status: Not Yet Started
    notes: null
contract:
  preconditions: A scoring rubric with named criteria and explicit pass thresholds is available before invocation. The caller has defined the scale (e.g., 1–5) and the max iteration cap. The task is well-specified
    enough that the agent can produce a meaningful first draft. The rubric criteria are specific enough to generate actionable failure reasons.
  invariants: 'The loop terminates: either all criteria pass at or above threshold, or the max iteration cap is reached. The iteration log is produced regardless of pass/fail outcome. The pass/fail verdict
    is explicit — the skill does not self-report "pass" without all criteria meeting threshold. Criteria definitions do not change between iterations within a single invocation.'
  governance: 'Owner: the caller (skill, workflow, or human operator) that defines the rubric and invokes the skill. Rubric definitions are caller-owned — the skill does not modify criteria or thresholds
    during execution. Iteration logs are the primary audit artifact; they must be retained if the output is used in a downstream decision. If the skill is used in a regulated context (compliance, customer
    communications), the rubric and iteration log must be reviewable by a human before the output is deployed.'
  recovery: 'If the loop reaches max iterations without passing: surface the final draft and the list of still-failing criteria with their last scores; do not emit the output as a passing artifact; escalate
    to human review with the iteration log as evidence. If oscillation is detected (same criteria failing alternately): halt; report the conflicting criteria; do not continue looping. If the rubric is discovered
    to be too vague for actionable scoring: halt before generating; prompt the caller to refine the criterion definition.'
tags:
- extracted-artifact
- skill
---

# Iterative Refinement Loop with Quality Gate

**Source:** [[iterative-refinement-loop-with-quality-gate]]
**Form:** skill
**Extraction date:** 2026-04-26

## Inputs

- **Draft task:** A description of the output to generate (e.g., "write a customer support response", "generate a compliance summary", "produce a code review").
- **Scoring rubric:** A set of named criteria, each with a description and a pass threshold. Example: `{tone: {description: "professional and empathetic", threshold: 4}, accuracy: {description: "factually correct against source", threshold: 4}, brevity: {description: "under 150 words", threshold: 3}}`. Criteria and thresholds are defined by the caller before invocation — they are not inferred by the agent.
- **Scale definition:** The numeric scale used for scoring (e.g., 1–5, where 1 = does not meet criterion, 5 = fully meets criterion).
- **Max iterations:** An integer cap on the number of refinement loops (recommended default: 3). Prevents runaway token consumption.
- **Optional — log destination:** A file path or structured output location where per-iteration scores and failure reasons are recorded. If omitted, scores are surfaced inline.

## Outputs

- **Final draft:** The output that passed all criteria at or above threshold, or the best-scoring output after max iterations if the threshold was not reached.
- **Iteration log:** For each iteration: the draft produced, the score for each criterion, the failure reason for any criterion below threshold, and whether the loop continued or terminated.
- **Pass/fail verdict:** A boolean and summary: "All criteria passed at iteration N" or "Max iterations reached; criteria not fully met: [list of failing criteria with final scores]".

## Steps

1. **Generate initial draft.** Produce the first draft in response to the task description. Do not apply criteria yet — generate as if responding normally.

2. **Score the draft against all criteria.** For each criterion in the rubric: assign a score on the defined scale; record the score and a one-sentence justification. If using a 1–5 scale with threshold 4, a score of 3 must include a specific failure reason (e.g., "tone: 3 — response opens with a defensive statement that undercuts empathy").

3. **Check pass condition.** If all criteria scores meet or exceed their thresholds → terminate loop, emit final draft and iteration log, verdict: pass.

4. **If any criterion fails:** identify the specific failure reasons for all failing criteria. Rewrite the draft targeting only the failing criteria — do not regress passing criteria.

5. **Increment iteration counter.** If iteration count has reached max iterations → terminate loop, emit the current draft as final, verdict: max-iterations-reached with list of still-failing criteria.

6. **Return to step 2** with the revised draft.

## Failure Modes

- **Self-evaluation bias.** The same model that generates the output also scores it. Models may be systematically lenient toward their own outputs, producing inflated scores that mask real quality gaps. Mitigation: use externally defined, specific criteria with concrete examples of each score level; consider a separate evaluation pass where the model is instructed to score critically without seeing its own generation context.

- **Criterion regress during rewrite.** Fixing a failing criterion causes a previously passing criterion to drop below threshold. The loop can oscillate rather than converge. Mitigation: in step 4, explicitly state which criteria are passing and instruct the rewrite to preserve them. If oscillation is detected (same criteria failing on alternating iterations), halt and surface the conflict to the caller.

- **Max-iteration cap too low for complex outputs.** 3 iterations may be insufficient when multiple criteria are failing simultaneously and each rewrite only addresses one. Mitigation: tune max iterations based on the number of criteria and expected difficulty; or restructure the rubric to address criteria in priority order across iterations.

- **Vague criteria produce uninformative scores.** If a criterion is defined as "good quality" with no operationalization, the model cannot produce actionable failure reasons, and rewrites are not targeted. Mitigation: each criterion must have a concrete description and, ideally, an example of a score-1 and score-5 response.

- **Audit trail lost when log destination is omitted.** If scores and failure reasons are only surfaced inline and the session is not logged, there is no external record of what passed or failed. Mitigation: always specify a log destination for quality-sensitive pipelines; treat the iteration log as a required output, not optional.

## Contract

### Preconditions
A scoring rubric with named criteria and explicit pass thresholds is available before invocation. The caller has defined the scale (e.g., 1–5) and the max iteration cap. The task is well-specified enough that the agent can produce a meaningful first draft. The rubric criteria are specific enough to generate actionable failure reasons.

### Invariants
The loop terminates: either all criteria pass at or above threshold, or the max iteration cap is reached. The iteration log is produced regardless of pass/fail outcome. The pass/fail verdict is explicit — the skill does not self-report "pass" without all criteria meeting threshold. Criteria definitions do not change between iterations within a single invocation.

### Governance
Owner: the caller (skill, workflow, or human operator) that defines the rubric and invokes the skill. Rubric definitions are caller-owned — the skill does not modify criteria or thresholds during execution. Iteration logs are the primary audit artifact; they must be retained if the output is used in a downstream decision. If the skill is used in a regulated context (compliance, customer communications), the rubric and iteration log must be reviewable by a human before the output is deployed.

### Recovery
If the loop reaches max iterations without passing: surface the final draft and the list of still-failing criteria with their last scores; do not emit the output as a passing artifact; escalate to human review with the iteration log as evidence. If oscillation is detected (same criteria failing alternately): halt; report the conflicting criteria; do not continue looping. If the rubric is discovered to be too vague for actionable scoring: halt before generating; prompt the caller to refine the criterion definition.
