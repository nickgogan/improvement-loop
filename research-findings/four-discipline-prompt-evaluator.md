---
notion_id: 32b1e08b-9b34-81ab-8a83-eb858dec654b
name: Four-Discipline Prompt Evaluator
summary: A four-discipline rubric assessing prompts in dependency order — Prompt Craft → Context Engineering → Intent Engineering → Specification Engineering — producing scorecards with per-dimension ratings
  and enhancement handoff blocks.
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Already Adopted
priority: Not Flagged
applicability:
- Perplexity Skills
adopted_in:
- Perplexity Skills
sources:
- nate-b-jones-videos-feb-mar-2026.md
- anthropic-prompt-evaluation-framework.md
- careerbuddy-meta-skill-author-references.md
proposals: []
date_discovered: '2026-03-16'
last_updated: '2026-07-12'
related_findings:
- file: the-four-discipline-prompting-stack-nate-b-jones.md
  rel: extends
- file: multidimensional-success-criteria-smart.md
  rel: same-problem
- file: three-tier-grading-hierarchy.md
  rel: enabled-by
- file: volume-over-quality-eval-principle.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- writing-agent-specifications.md
---
# Four-Discipline Prompt Evaluator

## What It Is
A structured evaluation rubric that scores a prompt across four disciplines in a fixed dependency order: Prompt Craft first, then Context Engineering, Intent Engineering, and finally Specification Engineering. Each dimension receives a rating and the output includes a handoff block that the prompt-enhancer can act on directly. Built as the prompt-evaluator skill (ID: 4a586bac).

## Why It Matters
Prompts fail in different ways at different layers. Evaluating them in dependency order prevents misdiagnosing a context problem as a craft problem, or an intent problem as a spec problem. The structured handoff block makes evaluation actionable, not just diagnostic.

## Why People Are Using It
Built on the Anthropic eval framework and the Nate B. Jones four-discipline model, and tested against live S2/S3 prompts including the content placement prompt. It is a core component of the Improvement Loop, making it one of the most exercised patterns in the system.

## Potential Improvements
Could add domain-specific sub-criteria — for example, household prompts might weight relationship and intent dimensions more heavily, while coding prompts weight specification precision more heavily.

## Potential Failure Modes
High rubric scores do not guarantee good agent behavior in practice. A prompt can score well on all four dimensions and still fail at runtime due to model behavior, tool limitations, or context not captured in the prompt itself.

## Extension — Operationalization as a Skill-Audit Gate (CareerBuddy meta-skill-author, 2026-07-12)

CareerBuddy's `audit-rubric.md` hardens the evaluator from a scorecard into a promotion gate, adding three production mechanics:

1. **Per-dimension minimum deploy thresholds.** Prompt Craft becomes six pass/fail elements (Role, Task clarity, Output format, Constraints, Success criteria, Self-check — self-check being the most commonly missing); the other three disciplines are scored 1–5 across four dimensions each, with explicit floors to deploy (e.g. Context source-scoping and signal-to-noise ≥ 4; Intent stop-rules ≥ 4; Spec acceptance-criteria ≥ 4; decomposition and eval-design ≥ 3). Any single dimension below floor blocks promotion — no cross-dimension trade-offs.
2. **A structured Enhancement Handoff Block format** as the Grader→Generator protocol: audit result, per-discipline scores with named bottleneck dimension, priority fixes in dependency order with quoted evidence from the artifact, a "What Not to Change" section preserving elements that scored well, eval coverage gaps, and checkbox clearance conditions for re-submission.
3. **A grader-context signature requirement:** the handoff block must record it was produced in a context distinct from the authoring session — governance evidence for generator-assessor separation ("the skill-creator NEVER both generates and assesses the same artifact in the same context"), designed against convenience erosion under deadline pressure.

Calibration notes carried with it: score in dependency order but author iteratively (a Specification change often reopens Prompt Craft); domain weighting shifts what a "5" means (coding skills weight Spec precision, conversational skills weight Intent) without changing the dimensions; and rubric pass remains the authoring-time gate only — behavioral verification is the separate deployment-time gate.
