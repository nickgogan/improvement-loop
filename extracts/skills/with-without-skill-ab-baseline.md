---
title: "With/Without-Skill A/B Baseline"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "with-without-skill-ab-baseline-measurement"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "eval-driven-improvement-loops.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "authors who want to know whether a skill actually improves output, not merely assert that it does"
    - "teams maintaining a capability portfolio that accumulates skills on faith and never re-measures them"
    - "anyone who needs a cheap counterfactual measurement of a capability's value without building a labelled eval suite first"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "trivial — the skill produces a measurement (a with/without delta plus a lessons journal); it changes no production state, so there is nothing to roll back beyond discarding the report"
  auditability: "high — the two runs (with-skill and without-skill), their diffed outputs, and the recorded lessons journal are preserved artifacts a reviewer can inspect, and the counterfactual is reproducible by re-running the task pair"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented by a practitioner team from their own product work as the measurement core of a skill-improvement loop; single-source for the exact A/B mechanic, though it composes two well-corroborated patterns (headless verification runs and per-skill lessons journals). No adoption recorded in this system yet."
contract:
  preconditions: "The skill under test can be loaded or omitted for a given run. A small, representative task corpus for the skill exists (a single task pair is noisy). Fresh, isolated execution sessions are available so the with-skill and without-skill runs do not contaminate each other. A definition of 'better' exists for the skill's output type. The scorer of the comparison is a separate role from the author/improver of the skill (generator ≠ assessor)."
  invariants: "Each measurement runs the same task twice — once with the skill loaded, once without — in fresh, isolated sessions. The comparison (the scorer) is not the skill's author. Marginal impact is read from the diff between the two runs, not from the with-skill run alone. Results and lessons are recorded to a persistent journal that lives with the skill."
  governance: "Owner: the author or team maintaining the skill. The scorer must be distinct from the author — an agent must not grade its own output. In unverifiable domains, 'with is better than without' is itself a model judgment and must be labelled as such, not treated as a hard metric. Cost is real — every round doubles execution — so task-corpus size and round count are deliberate budget choices."
  recovery: "If a single with/without pair is used and the delta looks large or zero → suspect single-run noise; add more task samples and re-run before trusting the signal. If the with-skill and without-skill runs share state → the counterfactual is invalid; re-run in fully isolated sessions. If the skill's delta has shrunk toward zero over time → the baseline model may have caught up; consider retiring the skill. If output quality has no hard check → treat the comparison as a biased model judgment and corroborate with a human or a second assessor."
tags:
  - "extracted-artifact"
  - "skill"
  - "evaluation"
  - "counterfactual-baseline"
  - "skill-efficacy"
---

# With/Without-Skill A/B Baseline

**Source:** [[with-without-skill-ab-baseline-measurement]]
**Form:** skill
**Extraction date:** 2026-07-19

The cheapest honest experiment for measuring a skill's marginal impact: run the same task twice — once **with** the skill loaded and once **without** it — in fresh, isolated sessions, then diff the outputs. The delta pins down exactly what the skill contributes, where it helps, and where it does nothing or hurts. It answers the question a skill portfolio otherwise never answers — "is this skill actually working the way it should?" — without a labelled eval framework. Documented as the measurement core of a practitioner team's skill-improvement loop, where an improver agent edits the skill and a separate headless session executes the counterfactual each round.

## Inputs

- **Skill under test.** A capability that can be loaded or omitted for a given run.
- **Task corpus.** A small set of representative tasks for the skill. One task pair is noisy; use several.
- **Isolated run harness.** The ability to launch fresh sessions (e.g., headless, no permission stops, reporting output back) so the with-skill and without-skill runs do not share state.
- **Definition of "better."** What counts as an improvement for this skill's output type — an assertion, a metric, or, where nothing hard exists, a labelled model/human judgment.
- **Separate scorer.** A comparison role distinct from the skill's author/improver (generator ≠ assessor).

## Outputs

- **Marginal-impact delta.** The diffed comparison of with-skill vs without-skill outputs, per task.
- **Lessons journal.** Structured observations (e.g., a `learning.md` living inside the skill) that drive the next round of edits.
- **Optional trend.** Deltas persisted over time so a skill's marginal value can be trended — and the skill retired when the baseline catches up to it (an improving model can erode a skill's delta to zero).

## Steps

1. **Assemble a task corpus.** Pick several representative tasks for the skill; a single pair is too noisy to trust.
2. **Run without the skill.** Execute each task in a fresh, isolated session with the skill omitted. Capture the output.
3. **Run with the skill.** Execute the same task in a separate fresh session with the skill loaded. Capture the output.
4. **Diff and score.** A scorer distinct from the author compares the two outputs and reads the marginal impact from the difference — not from the with-skill run alone.
5. **Record lessons.** Write the observations to the skill's journal; feed them into the next improvement round.
6. **Repeat under a budget.** Each round doubles execution (two runs per task); cap the corpus size and round count deliberately.

## Failure Modes

- **Single-run noise mistaken for signal.** One lucky/unlucky baseline run misattributes impact. Mitigation: multiple task samples per round.
- **Cost blow-up.** Every improvement round doubles execution, multiplied by rounds. Mitigation: bound corpus size and round count.
- **Contaminated counterfactual.** If the two runs share state, the comparison is invalid. Mitigation: fully isolated sessions per run.
- **Unverifiable domains.** Where output quality has no hard check, "with is better than without" is a model judgment and inherits its biases. Mitigation: label it as a judgment; corroborate with a human or a second assessor.
- **Self-scoring bias.** If the skill's author also scores the comparison, the measurement is compromised. Mitigation: keep the scorer distinct from the generator (rule: an agent must not grade its own output).

## Contract

### Preconditions
The skill under test can be loaded or omitted for a given run. A small, representative task corpus for the skill exists (a single task pair is noisy). Fresh, isolated execution sessions are available so the with-skill and without-skill runs do not contaminate each other. A definition of "better" exists for the skill's output type. The scorer of the comparison is a separate role from the author/improver of the skill (generator ≠ assessor).

### Invariants
Each measurement runs the same task twice — once with the skill loaded, once without — in fresh, isolated sessions. The comparison (the scorer) is not the skill's author. Marginal impact is read from the diff between the two runs, not from the with-skill run alone. Results and lessons are recorded to a persistent journal that lives with the skill.

### Governance
Owner: the author or team maintaining the skill. The scorer must be distinct from the author — an agent must not grade its own output. In unverifiable domains, "with is better than without" is itself a model judgment and must be labelled as such, not treated as a hard metric. Cost is real — every round doubles execution — so task-corpus size and round count are deliberate budget choices.

### Recovery
If a single with/without pair is used and the delta looks large or zero → suspect single-run noise; add more task samples and re-run before trusting the signal. If the with-skill and without-skill runs share state → the counterfactual is invalid; re-run in fully isolated sessions. If the skill's delta has shrunk toward zero over time → the baseline model may have caught up; consider retiring the skill. If output quality has no hard check → treat the comparison as a biased model judgment and corroborate with a human or a second assessor.
