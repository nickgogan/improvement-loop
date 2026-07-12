---
name: Skill Description Optimization Loop with Held-Out Test Set
summary: 'Anthropic''s skill-creator skill ships a description-optimization loop that treats skill triggering as a model-evaluated classification problem. Author generates 20 eval queries (8-10 should-trigger,
  8-10 should-not-trigger, focusing on near-misses), the loop splits 60/40 into train/test, runs each query 3 times for reliable trigger rate, asks Claude to propose description improvements based on failures,
  re-evaluates, iterates up to 5 times. Best description selected by TEST score (not train score) to avoid overfitting. Implementation: `python -m scripts.run_loop --eval-set <path> --skill-path <path>
  --model <id> --max-iterations 5`.'
implementation_notes: 'Eval-set design rules from skill-creator: queries must be realistic and specific (file paths, personal context, company names, casual speech). ''Format this data'' is BAD. ''ok so
  my boss just sent me this xlsx file (its in my downloads, called something like "Q4 sales final FINAL v2.xlsx") and she wants me to add a column for profit margin'' is GOOD. For should-not-trigger queries,
  the most valuable ones are near-misses sharing keywords but needing something different — NOT obviously irrelevant. ''Write a fibonacci function'' for a PDF skill is too easy and tests nothing. Use the
  model ID from your current session so triggering test matches user experience. Triggering mechanism note: Claude only consults skills for tasks it can''t handle on its own — simple single-step queries
  may not trigger a skill even with perfect description match. Substantive multi-step queries reliably trigger.'
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-skills-repo.md
related_findings:
- file: skill-md-frontmatter-as-discovery-trigger-primitive.md
  rel: extends
- file: skill-description-budget-context-overflow.md
  rel: same-problem
- file: machine-framework-for-agentic-coding-skill-asses.md
  rel: same-problem
- file: generator-assessor-separation-in-skill-iteration.md
  rel: enabled-by
- file: meta-skill-for-skill-authorship.md
  rel: extended-by
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-07-12'
pipeline_status: raw
consumed_by: []
---

# Skill Description Optimization Loop with Held-Out Test Set

## What It Is

Anthropic's skill-creator skill includes a structured loop for tuning a skill's `description` field to maximize triggering accuracy without overfitting. The loop:

1. **Generate eval queries.** 20 total: 8-10 should-trigger, 8-10 should-not-trigger. Focus on edge cases over clear-cut. Mix lengths, casual/formal phrasing, abbreviations, typos. Specific to realistic (file paths, personal context, company names) — never abstract.

2. **Author review.** Present eval set in HTML reviewer; user can edit queries, toggle should-trigger, add/remove entries, export to `eval_set.json`.

3. **Split 60/40.** Train = 60%, held-out test = 40%.

4. **Evaluate current description.** Run each train query 3 times for reliable trigger rate.

5. **Model-proposed improvements.** Claude proposes a new description based on what failed.

6. **Re-evaluate.** Run train + test on the new description.

7. **Iterate.** Up to 5 iterations.

8. **Select best by TEST score** — not train score. This prevents overfitting to train queries.

9. **Apply.** Update SKILL.md frontmatter; show user before/after with scores.

Implementation: `python -m scripts.run_loop --eval-set <path> --skill-path <path> --model <id> --max-iterations 5 --verbose`.

A crucial mechanism note from skill-creator: Claude only consults skills for tasks it can't easily handle on its own. Simple single-step queries like "read file X" may not trigger a skill even with perfect description match. The eval queries must be substantive enough that Claude would actually benefit from consulting a skill.

## Why It Matters

This is the most operationalized "skill-as-classification-problem" treatment in Anthropic's public skill substrate. It demonstrates that triggering accuracy is empirically measurable, model-tunable, and overfittable — which means it should be measured, tuned, and held out against.

The 60/40 train/test split is the ML-bootstrapped insight: if you let the model see your should-trigger queries and tune description to them, you'll get great train numbers and degraded behavior on never-seen queries. Held-out test set is the discipline that catches this.

The "3 runs per query" handles model-side stochasticity. A single run tells you nothing reliable about whether a description triggers.

The "best description by test score" rule is the punchline: train-best descriptions almost always lose to test-best ones in production.

## Why People Are Using It

Built into Anthropic's official skill-creator skill (`anthropics/skills/skills/skill-creator`). The loop is executed via a bundled script (`scripts/run_loop.py`), making it a Tier-1 production tool. The Complete Guide PDF lists skill-creator as the recommended path to "a functional skill in a single sitting - often in 15-30 minutes." The loop is the rigor floor for description quality.

## Potential Alternatives

Manual description tuning (subjective, doesn't scale, no overfit detection). Description templates ("Use when user says X, Y, or Z") — works for simple cases but doesn't probe near-miss queries. Embedding-based skill routing (precomputed semantic vectors instead of in-prompt description match — different architecture). LLM-as-judge for description quality (judges description quality in abstract, doesn't measure triggering accuracy).

## Potential Improvements

Continuous online optimization — log real user queries that did or didn't trigger the skill, feed back into the eval set. Cross-skill optimization — when multiple skills compete for similar queries, jointly tune their descriptions. Persistent eval sets per skill that grow with usage. Confidence intervals on trigger rate (current: point estimate from 3 runs).

## Potential Failure Modes

**Bad eval set ruins everything.** The skill-creator explicitly says: "bad eval queries lead to bad descriptions." If should-not-trigger queries are too obvious (not near-misses), the loop optimizes against a problem the description didn't have. The user-review step exists to catch this.

**Overfitting despite held-out test set.** A small test set (40% of 20 = 8 queries) is itself noisy; a description that happens to score well on those 8 may not generalize. Mitigation: larger eval sets at later iterations.

**Sub-step "Claude only consults skills for tasks it can't easily handle" is opaque.** This baseline behavior means triggering tests on too-simple queries return false negatives that aren't description-quality issues. Authors not understanding this misread their results.

**Model-version dependency.** Running the loop with model X produces a description tuned for X's triggering behavior. A model upgrade may regress triggering accuracy. The loop should be re-run after major model changes; nothing automates that.

**Triggering ≠ effectiveness.** A skill that triggers reliably but produces poor output gets a high trigger score but is a bad skill. The loop optimizes only the triggering layer.
