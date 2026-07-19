---
name: Confirm-Failure-First TDD Discipline for Coding Agents
summary: 'When a coding agent runs the red/green TDD cycle, the red-state verification step is non-negotiable — confirm the test actually fails before moving to implementation. Without this, the agent can
  accidentally write tests that already pass (false red), and the green step becomes meaningless. Plain English: if the test passes on its first run, the test isn''t testing anything. Make the agent prove
  the test fails first, then prove the fix makes it pass.'
implementation_notes: Embed the verification requirement in any TDD-adjacent skill prompt. 'Use red/green TDD — confirm red before green' is a more reliable instruction than just 'Use red/green TDD' for
  agents.
category: Evaluation
evidence_strength: Strong (production-tested practitioner discipline)
adoption_status: Not Yet Started
priority: P2
applicability:
- General
- S3 (Claude Code Build)
adopted_in: []
sources:
- simon-willison-red-green-tdd.md
related_findings:
- file: test-driven-development-as-counterweight-to-agenti.md
  rel: extends
- file: agent-self-reporting-unreliability-independent-eval.md
  rel: same-problem
- file: tdd-step-ordering-in-plan-tasks.md
  rel: enables
proposals: null
date_discovered: '2026-04-23'
last_updated: '2026-04-24'
pipeline_status: synthesized
consumed_by:
- rules/confirm-failure-first-tdd.md
- verifying-agent-output.md
---

## What It Is

A discipline-layer rule added to red/green TDD when the implementer is a coding agent rather than a human. The textbook TDD cycle is three steps:

1. **Red** — write a test that describes the desired behavior.
2. **Green** — implement code that makes the test pass.
3. **Refactor** — clean up.

The agent-specific addition: between steps 1 and 2, the agent MUST run the test suite and confirm the new test fails. Only then can it move to implementation. If the test passes on first run, stop — the test was malformed (matching existing behavior, or matching nothing), and any green afterward is a false victory.

Simon Willison's framing: *"It's important to confirm that the tests fail before implementing the code to make them pass."* The risk he names: agents can produce tests that already pass because the agent's understanding of "what should fail" doesn't automatically map to "what needs implementation."

## Why It Matters

Classical TDD assumes a thinking human who would notice a test passing immediately. Agents don't reliably notice this — they follow the recipe literally. A red-skip produces silent false-positives: tests that look like they're validating new code but are actually validating nothing, which then give confidence that the implementation works when it doesn't.

For MetaSystem / the IL:
- **Any `/*-spec` or test-generation skill** should embed the red-verification requirement explicitly. "Write a failing test, run it, confirm it fails, then implement" is the full contract.
- **`/assess-skill` and `/assess-agent` rubrics** that evaluate a skill's testing discipline should check for red-verification language in the skill definition, not just for test-writing language.
- **Existing testing patterns in the KB** (e.g., [[test-driven-development-as-counterweight-to-agentic-randomness]]) gain a specific enforcement point here. This finding is the concrete enforcement step for agent-driven TDD.

This is also a positive-space reformulation of a known anti-pattern: instead of listing failure modes (agents write passing tests, agents skip verification, agents assume their test is correct), the positive invariant is "red verified, then green." One rule; bounded enforcement.

## Why People Are Using It

Observed in [Simon Willison's Agentic Engineering Patterns guide, Red/green TDD chapter](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/) — see [[simon-willison-red-green-tdd]] for the source. Simon notes that "every good model understands 'red/green TDD' as shorthand" for the complete test-first workflow including the red-verification step. The sample prompt: *"Build a Python function to extract headers from a markdown string. Use red/green TDD."* — implicitly delegates to the model's internalized definition, which Simon observes does include red verification.

The implicit-definition approach is evidence of partial adoption but not reliable enforcement. For load-bearing use (e.g., agent-driven code that gets merged), making the verification step explicit reduces model-dependence.

## Potential Alternatives

- **BDD (given-when-then)** as an alternative to red/green. Same core discipline with different vocabulary; can be adapted with the same red-verification step.
- **Test-after development.** Write the code first, write the test second. Doesn't protect against the "test passes on first run" failure mode at all.
- **Property-based testing.** Generate test cases randomly; harder to "accidentally pass" but complex to set up for most agent workflows.
- **Human verification of red.** Have a human confirm the test fails before letting the agent proceed. Doesn't scale; defeats the purpose of agent-driven TDD.
- **CI-enforced red verification.** Configure the test runner to log "test failed as expected" before allowing the agent's next step. Closest to a hard gate; requires tooling.

## Potential Improvements

- **Formalize red-verification in the TDD prompt library.** A reusable prompt "Use strict red/green TDD (confirm red before green)" saves the full instruction as a first-class prompt asset.
- **Log the red-state artifact.** Agents should write down (to a session log) the specific failure message they observed. This produces a checkable audit trail.
- **Skill-contract requirement.** Any skill that claims to follow TDD should declare its red-verification protocol in its SKILL.md. `/assess-skill` can then validate this.
- **Red-verification as a hook.** PostToolUse hook on test commands that checks whether a new test was expected to fail and emits a warning if it didn't.

## Potential Failure Modes

- **Red-verification passes for the wrong reason.** The test fails because the file doesn't exist, not because the logic is missing. Agent interprets "test fails" as confirmation; implements; test still fails. Mitigation: failure message should be inspected, not just the exit code.
- **Model skips verification silently.** Agent says "I confirmed the test fails" without actually running it. Mitigation: require the agent to produce the specific error message in its response.
- **Red-verification on non-determinism.** Flaky tests may fail on one run and pass on another; red-verification doesn't distinguish. Mitigation: run multiple times or use only deterministic tests for this discipline.
- **Overzealous application.** Not every test needs red verification — regression tests exist specifically to pass on the current code. Blanket "always verify red first" fails for retrofit testing. Mitigation: scope the discipline to new-behavior tests, not pre-existing regression coverage.

## Extraction Note — 2026-04-24
Extracted as **rule**: [[confirm-failure-first-tdd]] in `extracts/rules/`
