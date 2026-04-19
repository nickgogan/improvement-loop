---
title: "Two-Level Verification (Agent Run + Harness Integrity)"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "two-level-verification-agent-run-plus-harness-inte"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "An agentic harness exists with configuration files (CLAUDE.md, rules, skills, hooks, settings) that govern agent behavior. The harness has at least one safety property or behavioral constraint that must hold across modifications."
  invariants: "Level 1 and Level 2 verification are treated as independent concerns -- passing one does not imply passing the other. Harness modifications trigger Level 2 checks before the modified harness is used for production agent runs. Safety properties are enumerated explicitly, not assumed."
  governance: "The Level 2 test suite is maintained alongside the harness configuration. New safety constraints require corresponding Level 2 test cases before deployment. Level 2 results are reviewed by the harness owner, not the agent."
  recovery: "If a Level 2 regression is detected after a harness change, revert the change, document the broken property, add a targeted test case for that property, then re-apply the change with the fix included."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Two-Level Verification (Agent Run + Harness Integrity)

**Source:** [[two-level-verification-agent-run-plus-harness-inte]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Teams verify whether individual agent runs produce correct output (Level 1) but rarely verify whether modifications to the agentic harness itself -- configuration files, permission boundaries, safety constraints, skill definitions -- break previously working properties (Level 2). Harness changes affect every subsequent agent run, not just one, so a broken permission boundary or disabled safety check propagates silently until it causes a visible failure. The harness evolves over time, and each evolution is a potential regression.

## Forces

- **Run verification vs. harness verification:** Level 1 (did the agent do the right thing?) is well-understood. Level 2 (did my harness change break something?) is rarely considered because it requires a different mental model -- testing configuration, not output.
- **Modification frequency vs. test coverage:** Harness files (CLAUDE.md, rules, skills, hooks) change frequently during active development, but maintaining a test suite that keeps pace creates friction.
- **Silent propagation vs. visible failure:** Harness regressions do not produce immediate errors. A broken permission boundary only surfaces when an agent attempts an action that should have been blocked -- which may not happen for many sessions.
- **Test cost vs. regression risk:** Running extensive verification on every minor configuration edit slows development, but skipping verification risks safety regressions that compound over time.
- **False security vs. genuine coverage:** Passing a smoke test suite does not guarantee the harness works for all edge cases, but it catches the most common regressions.

## Solution

Implement verification at two distinct levels, each with its own purpose and test suite:

**Level 1 -- Agent Run Verification:** After an agent completes a task, verify that the work product meets acceptance criteria. This is the familiar pattern: a verification step (human or automated) checks the output. Existing patterns like builder-validator chains and cross-model verification address this level.

**Level 2 -- Harness Integrity Verification:** When any harness configuration is modified (CLAUDE.md, settings.json, rules files, skill definitions, hooks), run a regression suite that validates known safety and behavioral properties still hold. This is a test suite for the harness, not for any specific agent run.

Level 2 test cases should cover:
- **Permission enforcement:** Do destructive tools still require approval after this configuration change?
- **Graceful degradation:** When tokens run out or errors occur, does the agent stop safely rather than crash or produce partial output?
- **Boundary preservation:** Are system scope boundaries still enforced after adding a new skill or rule?
- **Persistence integrity:** Does session state persistence still work after updating hooks?
- **Constraint propagation:** Do hard constraints defined in governance documents still reach the agent's effective context?

The key design principle: Level 2 tests are owned by the harness maintainer, not by individual task requesters. They run automatically (or are triggered manually) after harness modifications, before the modified harness is used for production work.

## Consequences

**Positive:**
- Catches silent regressions in safety properties, permission boundaries, and behavioral constraints before they propagate
- Makes harness evolution deliberate rather than accidental -- each modification is validated against known invariants
- Separates two fundamentally different verification concerns, allowing each to be optimized independently
- Creates an explicit inventory of safety properties that the harness must maintain

**Negative:**
- Maintenance burden: as the harness grows in complexity, the Level 2 test suite must grow proportionally
- Over-testing friction: running full verification on every minor edit slows iteration during active development
- False confidence: passing smoke tests does not guarantee full correctness, but may reduce vigilance
- Level 2 tests themselves require design effort -- poorly designed tests catch nothing while consuming resources

## Known Uses

- Anthropic's production Claude Code system, identified by Nate B Jones as one of 12 critical primitives
- MetaSystem modifies CLAUDE.md, rules, skills, and hooks regularly -- each modification is a candidate for Level 2 regression that currently goes unverified
- Standard software engineering practice (CI/CD regression suites) applied to the novel domain of agent configuration management

## Contract

### Preconditions
An agentic harness exists with configuration files that govern agent behavior. The harness has at least one safety property or behavioral constraint that must hold across modifications. The harness owner can enumerate the properties that matter (permissions, boundaries, degradation behavior).

### Invariants
Level 1 and Level 2 verification are treated as independent concerns -- passing one does not imply passing the other. Harness modifications trigger Level 2 checks before the modified harness is used for production agent runs. Safety properties are enumerated explicitly and tracked alongside the harness configuration. The agent under test cannot modify the Level 2 test suite.

### Governance
The Level 2 test suite is maintained alongside the harness configuration, versioned in the same repository. New safety constraints or behavioral boundaries require corresponding Level 2 test cases before deployment. Level 2 results are reviewed by the harness owner, not delegated to the agent. Test suite coverage is reviewed when new harness components are added.

### Recovery
If a Level 2 regression is detected after a harness change: revert the change immediately, document the specific broken property and its manifestation, add a targeted test case for that property to prevent future regression, then re-apply the change with the fix included. If a safety regression is discovered in production (Level 2 was not run or did not catch it), treat it as a P0 incident: revert, add the missing test case, and audit the test suite for similar gaps.
