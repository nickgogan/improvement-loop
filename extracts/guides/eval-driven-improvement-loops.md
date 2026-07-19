---
title: "Eval-Driven Improvement Loops"
type: "guideline"
category: "Evaluation"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-07-19"
updated: "2026-07-19"
author: "claude"
source_findings:
  - "claude-code-skills-20-four-mode-skill-lifecycle-wi"
  - "ace-execution-feedback-no-labels-required"
  - "eval-driven-development-autonomous-quality"
  - "karpathy-autoresearch-self-improvement-loop"
  - "iterative-refinement-loop-with-quality-gate"
  - "with-without-skill-ab-baseline-measurement"
  - "convergence-loop-optimizer-family-contract"
  - "eval-driven-tool-iteration-loop"
  - "self-evolving-loop-pattern"
  - "skill-description-optimization-loop-held-out-test"
  - "skill-popularity-vs-measured-efficacy"
  - "skill-smells-triage-layer-before-full-audit"
  - "skill-testing-three-tier-trigger-functional-perf"
  - "garbage-collection-day-persona-review-agents"
  - "capability-vs-regression-eval-lifecycle"
  - "generator-assessor-separation-in-skill-iteration"
  - "eval-rubric-carve-outs-subjective-and-script-core-skills"
source_dd:
  - "DD-81"
  - "DD-123"
tags:
  - "guide"
  - "evaluation"
  - "improvement-loop"
contract:
  preconditions: "You can already verify an agent's output works (see Verifying Agent Output, G4a) -- you have a binary assertion suite or a mechanical grader for the target skill/tool/agent. You can run the target repeatedly in fresh, headless sessions. You can hold and revert versions (git or equivalent). You have a held-out test set or can build one."
  invariants: "The generator never assesses its own output in the same context -- each loop role (executor, grader, comparator, analyzer) is a separate agent definition in an independent context. Every improvement iteration makes exactly one logical change, runs the eval suite, and is kept only if it does not regress -- reverted otherwise. Descriptions and skills are selected by held-out test score, never train score. Capability evals graduate to regression suites at saturation. No third-party component claiming performance gains is adopted without published evaluation or a local with/without baseline. Convergence loops re-audit in fresh context (blind), fix Medium+ findings in place, and terminate on no-Medium-or-higher or an iteration cap. Review feedback is converted into durable automated checks on a protected cadence rather than re-given each session. Class-aware carve-outs apply to skill audits: triggering/routing correctness is required of every skill regardless of output class."
  governance: "Improvement loops are versioned alongside the artifact they improve, with a full git history of each kept change. Skill test plans are re-run at tier 1 (triggering) after every description change and re-measured at tier 3 (marginal impact) after model upgrades; skills whose baseline catches up are retired. Severity definitions in convergence loops are shared across all artifact optimizers. Description-optimization loops are re-run after major model changes (descriptions are tuned per model version). The with/without baseline is re-measured periodically -- model improvements erode a skill's marginal value toward zero. This guide is owned by the engine's knowledge layer."
  recovery: "If an improvement loop stalls after 40+ iterations: review assertions for mutual satisfiability before increasing the cap; check whether the skill has hit its capability ceiling or execution-feedback signals are too weak. If a convergence loop keeps converging but quality doesn't improve: check that re-audits are blind (fresh context) -- an auditor that remembers its own fixes converges by memory. If a description tuned to best train score loses in production: you selected on train, not held-out test score -- re-select. If a skill measures worse than no skill: retire it; run the with/without baseline before re-adopting. If the same review feedback recurs across sessions: convert its cause into a durable test/lint/doc with a protected slot and a structured intake queue. If a subjective-output or script-core skill fails an assertion-based audit: apply the class carve-outs -- re-anchor criteria rather than adding fake assertions."
---

# Eval-Driven Improvement Loops

How to use evals to drive autonomous improvement of your agent and its skills -- so the agent gets better while you sleep, not just proves it works today. This guide covers the keep/revert improvement loop, the four-mode skill lifecycle, generator-assessor separation as the load-bearing rule, convergence contracts with a termination condition, skill lifecycle evaluation (smells triage, three-tier testing, held-out description optimization, with/without baselines), eval-driven tool iteration, no-label improvement from execution feedback, and converting review feedback into durable checks.

This is the "make it better" half of the evaluation practice. Its sibling -- *Verifying Agent Output* (G4a) -- answers the prerequisite question: how do you prove the output works in the first place. This guide assumes you can already verify output; it uses that verification capability as the fuel for improvement. Three findings are shared substrate across both guides (the capability/regression lifecycle, generator-assessor separation, and class-aware rubric carve-outs).

## When to Use This Guide

- You want to measure whether agent changes actually improve performance
- You are building an autonomous improvement loop for a recurring skill
- You are testing whether a skill actually helps (does it trigger, does it work, does it beat baseline?)
- You are optimizing a skill's description so it fires at the right times
- You are deciding whether to adopt a third-party skill, prompt, agent, or MCP server
- You are running an audit-fix-verify loop and need a termination condition
- You want the agent to self-improve using naturally available execution feedback (no labels)
- You are iterating on the agent's tools, not just its skills
- You keep re-giving the same review feedback and want it enforced automatically

**Do not use for:** proving an agent's output is correct in the first place (see *Verifying Agent Output*, G4a), designing the agent's architecture (see *Agent Architecture Decisions*, G3), or writing acceptance criteria (see *Writing Agent Specifications*, G1). You need G4a's verification capability *before* the loops here have anything to optimize against.

## Key Concepts

**1. The improvement loop is keep-or-revert.** The core mechanism of autonomous improvement is simple and monotonic: make exactly one change, run the eval suite, keep the change only if all assertions still pass (or a target metric improved) -- revert otherwise. Revert-on-failure prevents regressions from accumulating and makes the trajectory monotonically positive within the eval scope. Everything else in this guide is elaboration on that loop.

**2. Generator-assessor separation is the load-bearing rule.** The generator never both produces and assesses the same artifact in the same context. Each loop role -- executor, grader, comparator, analyzer -- is a separate agent definition spawned in an independent context. This architecture has been arrived at independently by multiple production teams (Anthropic's skill-creator, adversarial build/attack workflows, this engine's own governance), which marks it as a recurring solution to a recurring problem. The cheapest form is the *task flip*: flip a reviewer from "fix" to "only enumerate," and forbid fixing. (Shared substrate with G4a, where the same invariant governs verifier isolation.)

**3. Select by held-out test score, never train score.** Any loop that tunes against visible cases overfits them. Split your eval set train/test (60/40) and select the winning skill, description, or tool by held-out test score. Train-best almost always loses to test-best in production.

**4. Evals gate the loop, not just the ship.** In G4a evals prove the current output works. Here the *same* evals become the fitness function of an optimization loop: a binary assertion suite stored in `evals.json` is what the loop optimizes against, iteration after iteration. The quality of that suite is the binding constraint on how good the loop can get.

**5. Capability evals drive improvement; regression evals protect it.** Capability evals start low (the agent struggles) and are what an improvement loop pushes upward; when one saturates at 100%, graduate it to the regression suite and replace it with a harder eval. The loop always targets the current capability frontier. (The capability/regression lifecycle is shared substrate with G4a.)

**6. A convergence loop needs a termination condition.** "Audit" and "improve" are usually two separate unreliable activities -- reports pile up, fixes regress things, nobody knows when to stop. Fuse them: multi-pass audit -> severity rating -> fix in place -> verify gate -> blind re-audit, repeated until no Medium-or-higher finding remains or an iteration cap hits. The verify gate is what licenses autonomy; blind re-audit is what prevents convergence theater.

**7. Skills are eval targets in three tiers.** A skill can be structurally valid and still hurt performance. Evaluate it on three orthogonal tiers -- triggering (does it load at the right times?), functional (does it produce correct outputs?), performance (does it beat baseline?). Combining them into one "skill quality" score loses signal; each tier has its own failure mode.

**8. Popularity is not efficacy.** A skill from a 177k-star repo measured +5% token usage with worse results than no skill at all. Stars measure virality. The only honest signal is a measured marginal impact: run the same task with and without the component and diff the outcomes. Never adopt a third-party component that claims gains without published rigorous evaluation or your own baseline run.

**9. Agents can self-improve without labels.** Naturally available execution feedback -- code execution success/failure, API response codes, test pass/fail -- is sufficient to drive meaningful improvement. The ACE framework achieves +14.8% over baseline using only execution signals. For domains where ground-truth labels are expensive, binary execution signals are enough.

**10. Convert feedback into durable checks, or re-give it forever.** Review feedback given once as a comment is re-given every session unless it becomes a check the system enforces automatically. Convert each recurring feedback item into a failing test, a lint, or an addition to a review agent's documentation -- on a protected, time-boxed cadence -- so the next occurrence catches itself with no human back in the loop.

**11. Match the rubric to the skill's output class.** When auditing a skill, demanding binary assertions from a subjective-output skill (voice, tone, design) produces brittle fake gates, and demanding an LLM judge for a script-core skill re-verifies what the script's tests already guarantee. Re-anchor criteria per class -- with one universal invariant: triggering/routing correctness is objective and required of every skill. (Shared substrate with G4a's assertion-design carve-outs.)

---

## Procedure

### Step 1: Build the Improvement Loop

For recurring skills, implement the four-mode lifecycle:

```
Create  -->  Eval  -->  Improve  -->  Benchmark
  ^                       |
  +-----------------------+  (iterate 40-50 cycles)
```

1. **Create:** write the skill with acceptance criteria.
2. **Eval:** build the binary assertion suite (deterministic Layer 1 + LLM-judge Layer 2 -- see G4a Step 3). This suite is the loop's fitness function.
3. **Improve:** the agent iterates -- one logical change at a time, runs the suite, repeats. Two improvement dimensions: trigger/description tuning and output-quality improvement.
4. **Benchmark:** compare before/after using blind A/B testing on three metrics -- Pass Rate, Elapsed Time, Token Usage. The Comparator never knows which version is old vs. new.

**Four parallel sub-agents:**
- **Executor** -- runs the skill against test inputs
- **Grader** -- evaluates outputs against binary assertions
- **Comparator** -- performs blind A/B comparison between skill versions
- **Analyzer** -- synthesizes results and produces improvement recommendations

**Generator-assessor separation is the load-bearing rule.** Each role above is a separate agent definition in an independent context. Operational mechanics that make it work:

- The grader receives assertions and outputs, never the skill definition itself -- the assessor doesn't decide what good looks like, the spec does. A grader that knows intent judges on intent rather than result.
- Blind comparison hides which output is which (defeats positional bias); run multiple comparisons with shuffled order.
- The analyzer explains the win post-hoc, in fresh context -- useful for humans, but discount it as causal evidence (post-hoc rationalization risk).
- Watch for convenience erosion: under deadline pressure, authors "grade inline" and the separation collapses exactly when it matters most.

**Karpathy's autoresearch pattern.** Binary assertions stored in `evals.json` drive a tight autonomous loop: make exactly one change, run the eval suite, keep the change only if all assertions pass -- revert otherwise. Two loops operate in concert: an inner skill-description loop (refining what the skill does) and an outer main improvement loop (refining how it does it). Revert-on-failure makes the trajectory monotonically positive within the eval scope. Design for overnight autonomous execution.

**The overnight loop.** Configure the loop with an iteration cap (40-50), point it at the assertion suite, and let it run. Wake up to a refined skill with full git history of each change. Review the first 5-10 iterations before running unattended, and set the cap to prevent cost overruns.

**No-label improvement.** Where ground-truth labels are expensive, drive the loop with naturally available execution feedback -- code execution success/failure, API response codes, test pass/fail. The ACE framework reaches +14.8% over baseline using only execution signals.

### Step 2: Add a Convergence Contract (audit-fix-verify with a termination condition)

Fuse "audit" and "improve" under one contract so the loop knows when to stop:

1. **Multi-pass audit** -- each pass a distinct lens (structure, accuracy, security, ...), independent passes in parallel.
2. **Severity rating** -- every finding rated on a shared scale (Blocker > High > Medium > Low > Nit). Severity is the control signal: Medium is the fix/ignore boundary, High is the ship/block boundary.
3. **Fix in place** -- every Medium+ finding is fixed, not just reported.
4. **Verify gate** -- re-build/lint/test/re-eval after fixing; any change that regresses is backed out. The verify gate is what licenses autonomy -- fix-in-place without it converts an audit tool into a regression generator.
5. **Convergence loop** -- blind re-audit and repeat until no Medium+ finding remains, or an iteration cap hits (typically 3, extended to 5 while findings still drop >=50% per iteration).

Define the contract once and stamp out per-artifact members that differ only in lens set and verify gate (code: build+lint+tests; prose: fact-check; prompts: held-out eval; skills: trigger eval + collision check; SQL: EXPLAIN parity). **Guard against convergence theater:** if re-audits are not blind (fresh context), the loop converges because the auditor remembers its own fixes, not because the artifact is clean.

**In-skill quality gates (lightweight variant).** For quality-sensitive generation inside a single skill, embed a `draft -> score against explicit criteria (e.g., 4 dimensions rated 1-5, threshold >=4) -> rewrite-addressing-the-specific-failure -> re-score` loop, capped at ~3 iterations. Make the scorer a separate adversarial role where possible (self-scoring is biased toward self-approval), define criteria externally, and log scores and failure reasons per iteration for audit.

### Step 3: Evaluate Skills as First-Class Eval Targets

Skills are the primary distribution unit of agent capability -- and a skill can be structurally valid and still hurt performance. Layer the evaluation from cheap to expensive.

#### Triage first: the smells check (30 seconds)

Before any full audit, skim a symptom-to-cause smells table against the skill:

- **Triggering smells:** body edited but description untouched; no should/should-not-trigger queries ever written
- **Sizing smells:** body over 500 lines; pasted documentation blocks instead of pointers
- **Authoring smells:** deterministic logic written as prose instead of a script; obsolete scaffolding
- **Evaluation smells:** author graded their own skill in the same context; "output is good" acceptance criteria; saturated capability evals never graduated
- **Safety smells:** destructive operations with no autonomy gating

**Verdict rule:** 0 smells -> run the deterministic validator and proceed; 1-2 smells in one category -> patch locally; 3+ smells across categories -> run the full audit before shipping; **any safety smell -> block, never ship-and-fix-later.** Smells are behavioral and editorial -- invisible to deterministic structural validators -- which is exactly why this scannable layer must exist between the linter and the rubric.

#### Three-tier skill testing

| Tier | Question | Test cases | Failure meaning |
|------|----------|------------|-----------------|
| **1. Triggering** | Does it load at the right times? | Should-trigger (obvious + paraphrased) AND should-not-trigger (near-misses) | Skill is invisible or noisy |
| **2. Functional** | Does it produce correct outputs? | Valid outputs, API success, error handling, edge cases | Skill triggers but doesn't work |
| **3. Performance** | Does it beat baseline? | Same task with skill vs. without: messages, failed calls, tokens, clarifying questions | Skill is a no-op or a tax |

Each tier has its own failure mode and measurement -- combining them into one score loses signal. Rigor scales with maturity: manual testing for early iteration, scripted for repeatable validation, programmatic eval suites for mature skills. Re-run tier 1 after every description change; triggering regresses silently while function stays stable.

Match the audit rubric to the skill's output class: for subjective-output skills, do not score down for lacking a functional assertion suite (require a named qualitative method instead); for script-core skills, take the functional guarantee from the script's own tests. Triggering/routing optimization is objective and required of *every* skill regardless of output type.

#### Description optimization with a held-out test set

Treat triggering as a measurable classification problem:

1. Generate ~20 realistic eval queries (8-10 should-trigger, 8-10 should-not-trigger near-misses; specific and casual, never abstract -- "format this data" is a bad query, a messy real request naming a file is a good one).
2. Split 60/40 train/test.
3. Run each query 3 times for a reliable trigger rate.
4. Let the model propose description improvements from failures.
5. Iterate up to 5 times.
6. **Select the best description by held-out test score, never train score.**

Two caveats: models only consult skills for tasks they can't easily handle, so too-simple queries produce false negatives that aren't description problems; and descriptions are tuned per model version -- re-run the loop after major model changes.

#### The with/without baseline: measuring marginal impact

Skill portfolios accumulate on faith. The cheapest honest experiment: run the same task in fresh headless sessions twice -- once with the skill loaded, once without -- and diff the outcomes. The delta pins down what the skill actually contributes. Run multiple task samples (a single pair is noise), log lessons per round, and trend the delta over time: model improvements erode a skill's marginal value toward zero, and a skill whose baseline has caught up should be retired. The honest baseline is "the model with whatever context the user would otherwise provide," not "the model with nothing."

#### Adoption rule for third-party components

Do not install any external skill (or prompt, agent, MCP server) that claims to improve performance but has published no rigorous evaluation of that claim -- run your own with/without baseline first. Stars and virality carry zero efficacy information and can be anti-correlated. The security half is stricter: skills can instruct the agent to execute anything, so installation is a trust decision, not a convenience.

### Step 4: Extend the Loop to Tools and the System

**Eval-driven tool iteration.** The same loop applies to the agent's tools, not just its skills. Run structured evaluations on tools with realistic multi-step tasks (tracking accuracy, runtime, tool calls, tokens, errors), then feed the eval transcripts back to the model to refactor the tools. Transcripts reveal patterns human intuition misses -- unexpected tool-calling sequences, consolidation opportunities. Anthropic's Slack MCP tools beat human-written baselines after this treatment. Use held-out test sets to prevent tools overfitting to eval-specific shortcuts.

**Periodic self-evolution at the system level.** Above per-skill loops, run a recurring maintenance cadence: research scan -> compare current system state against the frontier -> delta report -> human-gated changes. Without a structured loop, drift accumulates silently; the human gate at deploy keeps the loop from making unvalidated autonomous changes. Watch for loop fatigue -- if reports consistently show little change, the reviewer starts rubber-stamping and the gate becomes ceremonial.

**Reliability math for improvement targets.** Use the march-of-nines framework (G4a Step 2) to set improvement targets. If your 10-step workflow needs 90% overall reliability, each step needs 99% (0.99^10 = 0.90). If your eval shows a step at 95% per-trial, that step alone brings overall reliability to 0.95 x 0.99^9 = 86%. Focus improvement investment on the lowest-reliability steps -- a 5% improvement on your worst step outweighs a 1% improvement across all steps.

### Step 5: Convert Review Feedback into Durable Checks

Review feedback given once as a comment is re-given every session unless it is converted into a check the system enforces automatically. A production ritual ("garbage collection day") time-boxes that conversion: on a fixed weekly cadence, every reviewer's sole job is to take every piece of slop observed that week and eliminate its *cause* durably -- as a failing test, a lint, or an addition to a review agent's documentation -- so the next occurrence catches itself with no human in the loop. The payoff is knowledge transfer: one reviewer's judgment, captured once in writing, benefits every agent-driver forever.

Disciplines and failure modes:

- **Time-box the conversion.** Durable-fix work competes with feature work and gets deferred indefinitely without a protected slot -- the exact failure the ritual prevents.
- **Give the ritual a structured intake.** A running "slop observed this week" log so the session works from a queue, not memory -- otherwise the ritual inherits the context-loss problem it exists to fix.
- **Garbage-collect the garbage-collectors.** Review-criteria docs accumulate contradictory or superseded guidance the same way any long-lived CLAUDE.md does; version or expire them, or stale criteria silently keep blocking.
- **Coverage tracks team composition, not task risk.** A review dimension nobody currently embodies never gets a durable check. In this engine the analogous mechanism is `/self-improve`'s capture-and-promote loop: recurring feedback converted into a durable check rather than re-given each session -- compare the fixed weekly cadence against scan-mode's on-demand retro.

*(Note: the source finding also describes a persona-review-agent facet -- one review agent per reviewer persona, triggered on every push. That facet is agent-shaped and belongs to agent-design/orchestration guidance, not this eval guide; only the durable-conversion discipline is carried here.)*

---

## Templates

### Improvement Loop Configuration

```markdown
## Improvement Loop -- {{SKILL_NAME}}

### Baseline (before improvement)
- Pass rate: {{BASELINE_PASS_RATE}}
- Elapsed time: {{BASELINE_TIME}}
- Token usage: {{BASELINE_TOKENS}}

### Loop Configuration
- Iteration cap: {{MAX_ITERATIONS}} (default: 40-50)
- Eval suite: {{EVAL_SUITE_PATH}}  (the loop's fitness function)
- Train/test split: 60/40 -- winner selected by HELD-OUT TEST score
- Improvement dimensions: {{TRIGGER_TUNING / OUTPUT_QUALITY / BOTH}}
- Execution feedback signals: {{CODE_PASS_FAIL / API_RESPONSE / TEST_RESULTS / TASK_COMPLETION}}
- Loop style: {{AUTORESEARCH_KEEP_REVERT / FOUR_MODE_LIFECYCLE}}

### Sub-Agents (generator-assessor separation)
- Executor: {{MODEL}} -- runs skill against test inputs
- Grader: {{MODEL}} -- evaluates against assertions (never sees skill definition)
- Comparator: {{MODEL}} -- blind A/B between versions (shuffled order)
- Analyzer: {{MODEL}} -- synthesizes results (post-hoc; discount as causal evidence)

### Convergence Contract (if audit-fix loop)
- Lenses: {{LENS_SET}}
- Severity scale: Blocker > High > Medium > Low > Nit  (Medium = fix/ignore boundary)
- Verify gate: {{BUILD_LINT_TESTS / FACT_CHECK / HELD_OUT_EVAL / ...}}
- Re-audit blind (fresh context): YES (required -- else convergence theater)
- Termination: no Medium+ finding OR {{ITERATION_CAP}} iterations

### Reliability Target
- Workflow steps: {{N}}
- Required overall reliability: {{TARGET_PERCENT}}
- Required per-step reliability: {{PER_STEP_PERCENT}} (= TARGET^(1/N))
- Current weakest step: {{STEP_NAME}} at {{CURRENT_PERCENT}}

### Gates
- Review first {{N}} iterations before running unattended
- Escalation: no progress after {{STALL_THRESHOLD}} iterations
- Abort: {{ABORT_CONDITION}}

### Post-Loop
- Compare against baseline: pass rate, time, tokens (blind comparator)
- If regression on any metric: revert to last passing version
- Graduate saturated capability evals to regression suite
```

**Worked example -- MetaSystem `/identify-artifacts` improvement loop:**

```
Baseline: 94.7% calibration match (session 24)
Target: >= 95% pass^3 across calibration set
Eval suite: Router calibration set (50 hand-classified findings), train/test 60/40
Iteration cap: 40; loop style: autoresearch keep/revert (one change per iteration)
Sub-agents: Executor + Grader (blind to rubric intent) + Comparator (blind A/B) + Analyzer
Execution feedback: binary match/mismatch against ground truth (no separate labels needed)
Convergence: N/A (single-metric optimization, not audit-fix)
Reliability target: 3-step (classify -> validate -> report), 95% overall, 98.3% per-step
Post-loop: winner selected by held-out test score; saturated capability evals -> regression
```

### Skill Test Plan (Three-Tier)

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `SKILL_NAME` | string | Yes | Skill under test |
| `OUTPUT_CLASS` | enum | Yes | objective / subjective-output / script-core / hybrid (selects assertion style per the class carve-outs) |
| `SHOULD_TRIGGER_QUERY` | string | Yes (8-10) | Realistic, specific queries the skill must fire on |
| `SHOULD_NOT_TRIGGER_QUERY` | string | Yes (8-10) | Near-miss queries sharing keywords but needing something different |
| `BASELINE_METRICS` | list | Yes | Metrics compared with vs. without skill (messages, failed calls, tokens, clarifying questions) |
| `RUNS_PER_QUERY` | number | Yes | Trials per query for reliable trigger rate (default 3) |

```markdown
## Skill Test Plan -- {{SKILL_NAME}}

### Smells triage (30 seconds, before anything else)
- Triggering / sizing / authoring / evaluation / safety smells found: {{SMELL_LIST_OR_NONE}}
- Verdict: {{PROCEED / PATCH_LOCALLY / FULL_AUDIT / BLOCK_ON_SAFETY}}

### Output class and assertion style
- Class: {{OUTPUT_CLASS}}
- If subjective-output: qualitative method = {{NAMED_RUBRIC_PLUS_HITL_LOOP}}
- If script-core: runnable verification = {{SCRIPT_TESTS_OR_GOLDEN_OUTPUT_CHECK}}

### Tier 1 -- Triggering
- Should-trigger ({{N}}): {{SHOULD_TRIGGER_QUERY}}, ...
- Should-not-trigger near-misses ({{N}}): {{SHOULD_NOT_TRIGGER_QUERY}}, ...
- Runs per query: {{RUNS_PER_QUERY}} | Train/test split: 60/40 | Winner selected by: TEST score
- Target trigger rate: {{TARGET}} (e.g., 90% of relevant queries)

### Tier 2 -- Functional
| # | Given | When | Then (binary) |
|---|-------|------|---------------|
| 1 | {{PRECONDITION}} | {{ACTION}} | {{ASSERTION}} |

### Tier 3 -- Performance vs. baseline
- Baseline (without skill): {{BASELINE_METRICS}}
- With skill: {{WITH_SKILL_METRICS}}
- Marginal impact verdict: {{KEEP / IMPROVE / RETIRE}}
- Re-measure cadence: {{CADENCE}} (model improvements erode skill deltas)
```

**Worked example -- `/transcript-fetcher` (script-core class):**

```
Smells triage: none found -> proceed
Output class: script-core (wraps tested Python fetcher)
  Runnable verification: fetcher's own test suite + golden-output
  check on one known video ID -- no LLM judge re-verifying parsing
Tier 1: should-trigger: "grab the transcript for this yt link",
  "need full text of this video for extraction", ...
  should-not-trigger near-misses: "summarize this video's comments",
  "what does this channel usually cover", ...
  3 runs/query, 60/40 split, select by test score
Tier 2: Given a valid video URL -> When skill runs -> Then markdown
  file exists at expected path with non-empty transcript body (binary)
Tier 3: baseline = manual fetch instructions per session
  (12 messages, 2 failed attempts) vs. skill (1 invocation, 0 failures)
  Verdict: KEEP; re-measure after next model upgrade
```

---

## Pitfalls

### 1. The generator grades its own work
Under deadline pressure authors "grade inline" and generator-assessor separation collapses exactly when it matters most. Spawn each loop role (executor, grader, comparator, analyzer) in an independent context; the grader must never see the skill definition, only assertions and outputs.

### 2. Selecting on train score
A description or skill tuned to the best score on visible cases almost always loses in production to the one selected on held-out test score. Always split 60/40 and select by test score.

### 3. The improvement loop that never converges
Mutually unsatisfiable assertions create infinite loops where the agent oscillates between fixing one assertion and breaking another. Before raising the iteration cap past 40, review assertions for mutual satisfiability and check whether the skill has hit its capability ceiling.

### 4. Convergence theater
A convergence loop "converges" because the same auditor remembers its own fixes, not because the artifact is clean. Route every re-audit through fresh context (or a different model family) so convergence reflects artifact quality, not auditor memory.

### 5. Fix-in-place without a verify gate
An audit loop that fixes Medium+ findings but doesn't re-build/lint/test/re-eval afterward is a regression generator, not an improvement loop. The verify gate -- back out any change that regresses -- is what licenses autonomy.

### 6. Adopting components by popularity
GitHub stars measure virality, not efficacy -- a skill from a 177k-star repo measured +5% tokens with worse results than no skill. Unvetted skills are also a security surface. Require published rigorous evaluation or run your own with/without baseline before installing anything that claims to improve performance.

### 7. A skill portfolio that accumulates on faith
Skills pile up and never get re-measured, so a skill whose marginal value has decayed to zero (or gone negative) keeps loading. Run the with/without baseline periodically; retire skills whose baseline has caught up. The honest baseline is "the model with whatever context the user would otherwise provide."

### 8. Description regressions after a body edit
Triggering regresses silently while function stays stable. Re-run tier-1 triggering tests after *every* description change, and re-run the description-optimization loop after major model upgrades (descriptions are tuned per model version).

### 9. Combining the three skill tiers into one score
Rolling triggering, functional, and performance into a single "skill quality" number loses signal -- each tier has a distinct failure mode and measurement. Keep them separate.

### 10. Forcing assertions on subjective or script-core skills during audit
Scoring a writing-voice skill down for lacking a functional assertion suite, or LLM-judging a renderer that wraps a tested script, erodes trust in the audit itself. Apply the class carve-outs; keep the universal invariant that triggering/routing correctness is always required.

### 11. Feedback re-given every session instead of converted to a durable check
Review feedback delivered as a one-off comment is re-delivered next session unless its cause is durably eliminated -- as a failing test, a lint, or a review-agent doc. Without a protected, time-boxed conversion slot with a structured intake queue, the same slop recurs and the durable-fix work loses to feature work indefinitely.

### 12. Trusting the analyzer's post-hoc explanation as causal evidence
The analyzer explains the win after the fact, in fresh context -- useful for humans, but a post-hoc rationalization, not proof of causation. Keep the keep/revert decision anchored to the eval suite, not the analyzer's narrative.

---

## Related Guides

- **Verifying agent output (G4a):** the prerequisite. *Verifying Agent Output* covers how to prove output works (assertions, metrics, verification architectures, benchmark discipline, production evaluation); those evals are the fuel this guide's loops optimize against. The capability/regression lifecycle, generator-assessor separation (the task flip), and the class-aware rubric carve-outs are shared substrate across both guides.
- **Tool design (G5):** the eval-driven tool iteration loop (Step 4) is the improvement half of *Designing Agent Tools*' tool design procedure -- transcripts from tool evals feed refactoring. G4b is a note-level secondary guide for the Tools dimension.
- **Prompt engineering (G8):** description optimization (Step 3) is prompt engineering under a held-out eval; prompt versioning survives model upgrades the way descriptions must be re-tuned per model version.
- **Governance and self-improvement:** converting review feedback into durable checks (Step 5) parallels the engine's own `/self-improve` capture-and-promote loop; the human gate at deploy (Step 4 self-evolution) is the DD-29 stage-boundary gate.
- **Architecture (G3):** march-of-nines reliability math for improvement targets (Step 4) informs where in a multi-agent architecture to invest improvement effort.

---

## Contract

### Preconditions
- You can already verify the target's output works (see *Verifying Agent Output*, G4a) -- you have a binary assertion suite or a mechanical grader.
- You can run the target repeatedly in fresh, headless sessions.
- You can hold and revert versions (git or equivalent) so keep/revert is real.
- You have a held-out test set or can build one (60/40 split).

### Invariants
- The generator never assesses its own output in the same context -- each loop role is a separate agent definition in an independent context.
- Every improvement iteration makes exactly one logical change, runs the eval suite, and is kept only if it does not regress -- reverted otherwise.
- Descriptions and skills are selected by held-out test score, never train score.
- Capability evals graduate to regression suites at saturation.
- No third-party component claiming performance gains is adopted without published evaluation or a local with/without baseline.
- Convergence loops re-audit in fresh context (blind), fix Medium+ findings in place, verify-gate, and terminate on no-Medium-or-higher or an iteration cap.
- Review feedback is converted into durable automated checks on a protected cadence rather than re-given each session.
- Class-aware carve-outs apply to skill audits; triggering/routing correctness is required of every skill.

### Governance
- Improvement loops are versioned alongside the artifact they improve, with a full git history of each kept change.
- Skill test plans are re-run at tier 1 (triggering) after every description change and re-measured at tier 3 (marginal impact) after model upgrades; skills whose baseline catches up are retired.
- Severity definitions in convergence loops are shared across all artifact optimizers; severity inflation silently moves the fix and ship boundaries.
- Description-optimization loops are re-run after major model changes.
- The with/without baseline is re-measured periodically -- model improvements erode a skill's marginal value toward zero.
- The capability/regression lifecycle is shared with G4a; graduation criteria are maintained in one place.
- This guide is owned by the engine's knowledge layer and updated when new improvement-loop findings are integrated.

### Recovery
- If an improvement loop produces no gains after 40+ iterations: review assertions for mutual satisfiability before increasing the cap; check whether the skill has hit its capability ceiling or execution feedback signals are too weak.
- If a convergence loop keeps "converging" but quality doesn't improve: check whether re-audits are blind (fresh context). An auditor that remembers its own fixes converges by memory.
- If a description tuned to best train score loses in production: you selected on train, not held-out test score -- re-select by test score.
- If a skill measures worse than no skill: retire it; run the with/without baseline before re-adopting anything.
- If the same review feedback recurs across sessions: convert its cause into a durable test, lint, or review-agent doc; give the conversion a protected slot and a structured intake queue.
- If a subjective-output or script-core skill fails an assertion-based audit: apply the class carve-outs -- re-anchor the criteria (qualitative method or script-test verification) rather than adding fake assertions.
- If the self-evolution cadence produces rubber-stamped reviews: the gate has become ceremonial (loop fatigue) -- reduce cadence or raise the bar for what surfaces to the human.
