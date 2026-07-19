---
title: "Skill Description Optimization Loop"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "skill-description-optimization-loop-held-out-test"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "eval-driven-improvement-loops.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "authors tuning a skill's trigger/description field so it fires on the right requests and stays silent on near-miss requests"
    - "teams that want triggering accuracy measured empirically instead of hand-tuned by intuition"
    - "anyone who has seen a capability over-trigger or under-trigger and wants a repeatable optimization procedure with built-in overfit protection"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "trivial — the loop updates a description/trigger field; reverting is a one-line change back to the prior text, and the eval set plus score history are additive artifacts with no migration cost"
  auditability: "high — the eval set, the per-iteration train and test trigger rates, and the before/after description with scores are all preserved; a reviewer can re-run the eval set independently and reproduce the verdict"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Ships in a major vendor's official skill-creator tooling as a bundled optimization script and is presented as the rigor floor for description quality; no adoption recorded in this system yet."
contract:
  preconditions: "A skill (or trigger-gated capability) with an editable description/trigger field exists. The model used for evaluation matches the model that will govern triggering in production. The author can invoke the same query repeatedly and observe whether the capability triggers. An eval set of realistic, substantive queries can be authored and reviewed."
  invariants: "The held-out test split is never used to propose description improvements — only the train split drives proposals. Each query is run multiple times (default 3) so the trigger rate averages out model stochasticity. The winning description is selected by test-set score, never by train-set score. should-not-trigger queries include near-misses that share keywords with should-trigger queries, not only obviously-irrelevant queries. Iteration is bounded by a maximum count (default 5)."
  governance: "Owner: the author or team maintaining the skill's description. The eval set is author-owned and must be reviewable before the loop runs — bad eval queries produce bad descriptions. The loop must be re-run after a major model change, because a description tuned for one model's triggering behavior may regress on another. Consumer-side review tooling that gates skill shipment may require that a shipped description carry an eval-set and a recorded test score."
  recovery: "If the first-run trigger rate is suspiciously perfect on very simple queries → the queries are not substantive enough to make the agent consult a skill; rewrite them as multi-step realistic tasks and re-run. If train scores climb while test scores stall or fall → overfitting; stop iterating and select the best test-score description, or enlarge the eval set. If every should-not-trigger query is obviously irrelevant → the loop is optimizing a non-problem; add near-miss distractors and re-run. If a model upgrade regresses triggering → re-run the loop against the new model."
tags:
  - "extracted-artifact"
  - "skill"
  - "evaluation"
  - "skill-authoring"
  - "triggering-accuracy"
---

# Skill Description Optimization Loop

**Source:** [[skill-description-optimization-loop-held-out-test]]
**Form:** skill
**Extraction date:** 2026-07-19

A structured loop for tuning a skill's `description` (trigger) field to maximize triggering accuracy without overfitting. It treats "does this description trigger on the right requests" as a model-evaluated classification problem: author a labelled eval set, split it into train and held-out test, let the model propose description improvements against the train split, and select the winner by test-set score. Originating implementation: a major vendor's official skill-creator tooling, which runs the loop via a bundled script.

## Inputs

- **Target description.** The current `description`/trigger field of the skill being tuned.
- **Eval set (20 queries).** 8–10 should-trigger and 8–10 should-not-trigger queries. Focus on edge cases over clear-cut ones; mix lengths, casual/formal phrasing, abbreviations, and typos. Queries must be realistic and specific (file paths, personal context, company names) — never abstract. `"Format this data"` is a bad query; `"ok my boss just sent me this xlsx (in my downloads, 'Q4 sales final FINAL v2.xlsx') and wants a profit-margin column"` is a good one. The most valuable should-not-trigger queries are **near-misses** that share keywords with should-trigger queries but need something different — not obviously-irrelevant queries.
- **Evaluation model ID.** Use the model that governs triggering in production, so the test reflects real user experience.
- **Iteration cap.** Maximum optimization rounds (default 5).

## Outputs

- **Optimized description**, selected by held-out test score.
- **Before/after report** showing the original and winning descriptions with their train and test trigger rates.
- **Persisted eval set** (e.g., `eval_set.json`) that can grow with usage and be re-run later.

## Steps

1. **Generate eval queries.** 20 total (8–10 should-trigger, 8–10 should-not-trigger), weighted toward edge cases and near-misses.
2. **Author review.** Present the eval set for the author to edit queries, toggle should-trigger labels, add/remove entries, and export. This step catches bad eval queries before they corrupt the optimization.
3. **Split 60/40.** Train = 60%, held-out test = 40%. The test split is sequestered.
4. **Evaluate the current description.** Run each train query 3 times to get a reliable trigger rate (a single run is not reliable given model stochasticity).
5. **Model-proposed improvement.** Ask the model to propose a new description based on which train queries failed.
6. **Re-evaluate.** Run train and test on the new description.
7. **Iterate.** Repeat steps 5–6 up to the iteration cap.
8. **Select best by TEST score** — never train score. Train-best descriptions almost always lose to test-best ones in production; this is the overfit guard.
9. **Apply.** Update the skill's description field; show the author the before/after with scores before committing.

Reference invocation shape (from the originating tooling): `run_loop --eval-set <path> --skill-path <path> --model <id> --max-iterations 5`.

**Triggering mechanism note.** The agent only consults a skill for tasks it cannot easily handle on its own. Simple single-step queries may not trigger a skill even with a perfect description match — so eval queries must be substantive, multi-step tasks that would actually benefit from consulting the skill. Misunderstanding this baseline behavior causes authors to misread false negatives as description-quality problems.

## Failure Modes

- **Bad eval set ruins everything.** If should-not-trigger queries are too obvious (not near-misses), the loop optimizes against a problem the description never had. Mitigation: the author-review step (2) and deliberate near-miss authoring.
- **Overfitting despite the held-out test.** A small test set (40% of 20 ≈ 8 queries) is itself noisy; a description that scores well on those 8 may not generalize. Mitigation: enlarge the eval set at later iterations.
- **Too-simple queries return false negatives.** The "agent only consults skills for hard tasks" behavior means trivial queries under-trigger regardless of description quality. Mitigation: author substantive multi-step queries.
- **Model-version dependency.** A description tuned for one model may regress after a model upgrade. Mitigation: re-run the loop after major model changes — nothing automates this.
- **Triggering ≠ effectiveness.** The loop optimizes only the triggering layer. A skill that triggers reliably but produces poor output still scores high here. Mitigation: pair with a functional/output-quality evaluation.

## Contract

### Preconditions
A skill (or trigger-gated capability) with an editable description/trigger field exists. The model used for evaluation matches the model that will govern triggering in production. The author can invoke the same query repeatedly and observe whether the capability triggers. An eval set of realistic, substantive queries can be authored and reviewed.

### Invariants
The held-out test split is never used to propose description improvements — only the train split drives proposals. Each query is run multiple times (default 3) so the trigger rate averages out model stochasticity. The winning description is selected by test-set score, never by train-set score. should-not-trigger queries include near-misses that share keywords with should-trigger queries, not only obviously-irrelevant queries. Iteration is bounded by a maximum count (default 5).

### Governance
Owner: the author or team maintaining the skill's description. The eval set is author-owned and must be reviewable before the loop runs — bad eval queries produce bad descriptions. The loop must be re-run after a major model change, because a description tuned for one model's triggering behavior may regress on another. Consumer-side review tooling that gates skill shipment may require that a shipped description carry an eval-set and a recorded test score.

### Recovery
If the first-run trigger rate is suspiciously perfect on very simple queries → the queries are not substantive enough to make the agent consult a skill; rewrite them as multi-step realistic tasks and re-run. If train scores climb while test scores stall or fall → overfitting; stop iterating and select the best test-score description, or enlarge the eval set. If every should-not-trigger query is obviously irrelevant → the loop is optimizing a non-problem; add near-miss distractors and re-run. If a model upgrade regresses triggering → re-run the loop against the new model.
