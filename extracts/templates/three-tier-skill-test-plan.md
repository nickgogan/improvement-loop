---
title: "Three-Tier Skill Test Plan"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "skill-testing-three-tier-trigger-functional-perf"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "eval-driven-improvement-loops.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "authors evaluating a new or revised trigger-based capability before shipping it to end users"
    - "teams that need to prove a capability beats baseline, not just that it runs"
    - "reviewers who need a repeatable, three-part test structure rather than an ad-hoc pass/fail check"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "trivial — the scaffold produces a test-plan document; discarding or revising it has no migration cost. Re-running tiers after a change is cheap; only the accumulated baseline history has any continuity cost."
  auditability: "high — each tier has a named pass/fail shape (should-trigger/should-not-trigger sets, given/when/then cases, baseline-vs-comparison numbers) that a reviewer can check independently of the author's self-report"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Documented and operationalized in a major vendor's official skill-authoring guidance, including a companion iteration tool that runs paired with/without comparisons automatically; no adoption recorded in this system yet."
contract:
  preconditions: "A trigger-based capability (a skill, tool, or workflow the agent invokes conditionally) exists in a testable form. A baseline behavior — what happens without the capability — can be produced for comparison. The author can run repeatable queries against the capability, either manually or via a test harness."
  invariants: "All three tiers are addressed before the capability is considered validated: triggering (does it activate correctly), functional (does it produce correct outputs), and performance (does it beat baseline). Each tier is scored independently — a capability is not called 'validated' on the strength of one tier alone. Triggering tests include both should-trigger and should-NOT-trigger cases, not only positive examples. The performance-comparison baseline reflects a realistic without-capability condition, not a deliberately weakened one."
  governance: "Owner: the author or team responsible for the capability being tested. Consumer-side audit or review tooling that gates capability shipment should check that all three tiers are present and that the performance baseline is disclosed, not just claimed. Rigor level (manual, scripted, or programmatic) is an explicit author choice, declared alongside the results — not silently defaulted to the easiest option."
  recovery: "If a capability passes triggering and functional tiers but not performance → treat it as a no-op; do not ship on triggering/functional success alone. If triggering tests were not re-run after a description or trigger-condition change → treat triggering status as unverified and re-run before shipping. If the performance baseline used an unrealistic 'no context at all' comparison → redo the baseline against a realistic without-capability condition before trusting the comparison numbers. If measurement is noisy (token counts, message counts vary run to run) → run each test case multiple times and report a range or median, not a single sample."
tags:
  - "extracted-artifact"
  - "template"
  - "evaluation"
  - "skill-testing"
  - "baseline-comparison"
---

# Three-Tier Skill Test Plan

**Source:** [[skill-testing-three-tier-trigger-functional-perf]]
**Form:** template
**Extraction date:** 2026-07-19

A fillable test-plan scaffold for validating a trigger-based capability across three independent tiers — does it activate correctly, does it work correctly, and does it actually help. Each tier has its own pass/fail shape and its own failure mode; combining them into a single "quality" score loses signal. Complete one scaffold per capability before treating it as validated.

## Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `{{CAPABILITY_NAME}}` | Name of the capability under test | Yes |
| `{{SHOULD_TRIGGER_N}}` | A query, obvious or paraphrased, that must activate the capability | Yes (≥3) |
| `{{SHOULD_NOT_TRIGGER_N}}` | A query, from an unrelated or adjacent-but-distinct topic, that must NOT activate the capability | Yes (≥3) |
| `{{FUNCTIONAL_TEST_N_GIVEN}}` | Preconditions/input state for functional test case N | Per case |
| `{{FUNCTIONAL_TEST_N_WHEN}}` | The action or invocation performed | Per case |
| `{{FUNCTIONAL_TEST_N_THEN}}` | Expected outcome, including error-free execution | Per case |
| `{{BASELINE_MESSAGES}}` | Back-and-forth message count without the capability | Yes |
| `{{BASELINE_FAILED_CALLS}}` | Failed API/tool calls without the capability | Yes |
| `{{BASELINE_TOKENS}}` | Tokens consumed without the capability | Yes |
| `{{WITH_CAPABILITY_MESSAGES}}` | Back-and-forth message count with the capability | Yes |
| `{{WITH_CAPABILITY_FAILED_CALLS}}` | Failed API/tool calls with the capability | Yes |
| `{{WITH_CAPABILITY_TOKENS}}` | Tokens consumed with the capability | Yes |
| `{{RIGOR_LEVEL}}` | `manual` \| `scripted` \| `programmatic` — the rigor level used for this run | Yes |
| `{{RUN_COUNT}}` | Number of times each test case was repeated (for noise handling) | Yes |

## Body

```markdown
# Test Plan: {{CAPABILITY_NAME}}

**Rigor level:** {{RIGOR_LEVEL}}
**Runs per test case:** {{RUN_COUNT}}

## Tier 1: Triggering Tests
Goal: does the capability activate at the right times?

**Should trigger:**
- {{SHOULD_TRIGGER_1}}
- {{SHOULD_TRIGGER_2}}
- {{SHOULD_TRIGGER_3}}
<!-- include paraphrased/reworded variants, not only obvious phrasings -->

**Should NOT trigger:**
- {{SHOULD_NOT_TRIGGER_1}}
- {{SHOULD_NOT_TRIGGER_2}}
- {{SHOULD_NOT_TRIGGER_3}}
<!-- include adjacent-but-distinct topics, not only obviously unrelated ones -->

**Tier 1 verdict:** pass / fail — [rate of correct trigger/non-trigger across cases]

## Tier 2: Functional Tests
Goal: does the capability produce correct outputs?

| Case | Given | When | Then |
|------|-------|------|------|
| 1 | {{FUNCTIONAL_TEST_1_GIVEN}} | {{FUNCTIONAL_TEST_1_WHEN}} | {{FUNCTIONAL_TEST_1_THEN}} |

**Tier 2 verdict:** pass / fail — [cases passed / total, error-handling notes]

## Tier 3: Performance Comparison
Goal: does the capability beat a realistic baseline?

| Metric | Without capability | With capability |
|--------|---------------------|------------------|
| Messages | {{BASELINE_MESSAGES}} | {{WITH_CAPABILITY_MESSAGES}} |
| Failed calls | {{BASELINE_FAILED_CALLS}} | {{WITH_CAPABILITY_FAILED_CALLS}} |
| Tokens | {{BASELINE_TOKENS}} | {{WITH_CAPABILITY_TOKENS}} |

**Baseline honesty check:** does "without capability" reflect realistic context the user would otherwise provide, not a deliberately blank baseline?

**Tier 3 verdict:** pass / fail — [net improvement or regression]

## Overall Verdict
All three tiers must independently pass for the capability to be considered validated. A pass on 1–2 tiers only is NOT a validated capability — record which tier(s) failed and why.
```

## Usage

1. **Run all three tiers, not a subset.** A capability that triggers but doesn't work fails tier 2. A capability that triggers and works but doesn't beat baseline is a no-op (fails tier 3). A capability that beats baseline but triggers unreliably fails tier 1.
2. **Cover negative triggering cases.** Should-NOT-trigger cases, especially adjacent-but-distinct topics, catch over-eager triggering that should-trigger cases alone will miss.
3. **Use given/when/then for functional cases.** Concrete preconditions, action, and expected outcome make functional failures diagnosable, not just detectable.
4. **Keep the performance baseline honest.** The comparison is only informative if "without capability" reflects what a user would realistically provide, not an artificially blank starting point.
5. **Match rigor to deployment.** Manual testing suits fast early iteration; scripted testing suits repeatable validation across changes; programmatic testing suits capabilities consumed by other automated systems. Testing at a lower rigor than the actual deployment leaves the real usage path unverified.
6. **Repeat runs to handle noise.** Token and message counts vary run to run even with an unchanged capability; report `{{RUN_COUNT}}` repetitions rather than a single sample, especially for tier 3.
7. **Re-run tier 1 after any trigger-relevant change.** Changing a capability's description or invocation condition can regress triggering silently while functional behavior stays stable — don't assume tier 1 still holds just because tiers 2–3 do.

## Variation Axis

What drives different renderings of this scaffold:

- **Rigor level.** Manual runs render as a short checklist filled in by hand; scripted runs render as a repeatable test file; programmatic runs render as a structured eval-suite definition (e.g., a JSON/YAML case list consumed by a harness).
- **Capability shape.** Simple single-action capabilities need few functional cases; multi-step workflow capabilities need one functional case per meaningful branch (success path, each error-handling path, edge cases).
- **Baseline availability.** When a true "without capability" baseline is hard to reconstruct (the capability replaces something with no clean predecessor), tier 3 renders as an estimate with the estimation method documented, rather than a measured comparison.
- **Maturity stage.** Early iteration favors a light version of this scaffold (few cases, manual rigor); a capability nearing wide deployment favors the full scaffold with repeated runs and programmatic rigor.

## Contract

### Preconditions
A trigger-based capability (a skill, tool, or workflow the agent invokes conditionally) exists in a testable form. A baseline behavior — what happens without the capability — can be produced for comparison. The author can run repeatable queries against the capability, either manually or via a test harness.

### Invariants
All three tiers are addressed before the capability is considered validated: triggering (does it activate correctly), functional (does it produce correct outputs), and performance (does it beat baseline). Each tier is scored independently — a capability is not called "validated" on the strength of one tier alone. Triggering tests include both should-trigger and should-NOT-trigger cases, not only positive examples. The performance-comparison baseline reflects a realistic without-capability condition, not a deliberately weakened one.

### Governance
Owner: the author or team responsible for the capability being tested. Consumer-side audit or review tooling that gates capability shipment should check that all three tiers are present and that the performance baseline is disclosed, not just claimed. Rigor level (manual, scripted, or programmatic) is an explicit author choice, declared alongside the results — not silently defaulted to the easiest option.

### Recovery
If a capability passes triggering and functional tiers but not performance → treat it as a no-op; do not ship on triggering/functional success alone. If triggering tests were not re-run after a description or trigger-condition change → treat triggering status as unverified and re-run before shipping. If the performance baseline used an unrealistic "no context at all" comparison → redo the baseline against a realistic without-capability condition before trusting the comparison numbers. If measurement is noisy (token counts, message counts vary run to run) → run each test case multiple times and report a range or median, not a single sample.
