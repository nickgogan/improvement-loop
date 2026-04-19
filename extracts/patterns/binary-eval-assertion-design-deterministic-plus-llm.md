---
title: "Binary Eval Assertion Design -- Deterministic + LLM-as-Judge Dual Layer"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "binary-eval-assertion-design-deterministic-plus-ll"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "An agent skill or task produces outputs that need automated quality evaluation. Both structural requirements (format, length, required fields) and semantic requirements (tone, coherence, factual accuracy) exist. An LLM is available for judge calls."
  invariants: "Every assertion returns exactly true or false -- never a numeric score. Deterministic assertions are evaluated before LLM-as-judge assertions. Eval files are locked from agent modification. Assertions are mutually satisfiable."
  governance: "Assertion suites are reviewed when task requirements change. LLM-as-judge consistency is monitored for threshold drift. New assertions require a justification that they test a real failure mode, not a theoretical one. Eval file write access is restricted to human reviewers."
  recovery: "If assertions are discovered to be mutually unsatisfiable, disable the conflicting subset, fix the conflict, then re-enable. If LLM-as-judge drift is detected, recalibrate with fresh reference examples. If an agent modifies its own eval files, revert from version control and investigate the access control failure."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Binary Eval Assertion Design -- Deterministic + LLM-as-Judge Dual Layer

**Source:** [[binary-eval-assertion-design-deterministic-plus-ll]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent output evaluation typically relies on either deterministic checks alone (missing semantic quality issues like tone, coherence, and hallucination) or LLM-as-judge alone (expensive, slow, hard to debug, and prone to threshold drift). Neither layer by itself catches both structural and semantic failures. Scored metrics (1-10 scales) compound the problem: a score of 6.2 tells the agent nothing actionable about what to fix.

## Forces

- **Structural correctness vs. semantic quality:** Deterministic checks validate format, length, and required fields cheaply and unambiguously, but cannot assess whether the content is coherent, well-toned, or factually accurate. LLM judges can assess semantics but are expensive and noisy.
- **Speed vs. coverage:** Deterministic checks run instantly; LLM judge calls add latency and cost. Running only fast checks misses quality issues; running only slow checks wastes resources on structurally broken outputs.
- **Binary clarity vs. scored nuance:** Binary pass/fail points directly to the problem and enables automated self-improvement loops. Scored metrics feel richer but provide no actionable signal -- the agent cannot determine what a "6" means or how to reach a "7."
- **Eval integrity vs. agent autonomy:** If the agent can modify its own evaluation files, it will "fix" the tests rather than fixing the skill. But locking eval files creates a maintenance bottleneck.

## Solution

Build eval suites with two assertion layers, where every assertion returns exactly true or false:

**Layer 1 -- Deterministic checks (run first):**
- String matching for structural requirements: section headers present, required fields populated
- Word/character count within defined range
- Markdown validity, schema compliance
- Forbidden phrases absent
- Date formats, owner fields, and other typed constraints

These checks are fast, cheap, unambiguous, and debuggable. If a deterministic check fails, the output is structurally broken and there is no point running expensive LLM checks.

**Layer 2 -- LLM-as-judge evals (run after Layer 1 passes):**
- Tone consistency with the target persona
- Coherence and logical flow
- Hallucination detection against source material
- Actionability of recommendations
- Each judge call returns a binary yes/no decision, not a score

**Design constraints:**
- Run deterministic checks first; only invoke LLM judges if all deterministic checks pass (fail-fast, save cost)
- Each assertion is independently debuggable -- a failing assertion identifies the exact requirement that was violated
- Target 15-30 test inputs with diverse coverage: typical cases, edge cases, and assertion-targeted examples
- Verify that all assertions are mutually satisfiable before deploying the eval suite -- conflicting requirements create infinite improvement loops
- Lock eval files from agent write access -- the agent under evaluation must not be able to modify its own tests

## Consequences

**Positive:**
- Catches both structural and semantic failures in a single eval pass
- Binary pass/fail provides clear, actionable signal for self-improvement loops -- the agent knows exactly which requirement it broke
- Fail-fast layering (deterministic first) saves LLM judge costs on structurally broken outputs
- Individual assertion debuggability makes it straightforward to identify and fix specific quality gaps

**Negative:**
- Assertions that are too easy (always pass) create false confidence -- they do not drive improvement
- Conflicting assertions that are mutually unsatisfiable create infinite improvement loops where the agent oscillates between fixing one and breaking another
- LLM-as-judge threshold drift: the judge model may shift its pass/fail boundary over time, creating inconsistent evaluations across runs
- Building a comprehensive assertion suite requires domain knowledge about what actually goes wrong -- premature assertions test theoretical rather than observed failure modes

## Known Uses

- MindStudio: standard pattern for overnight autonomous skill improvement loops using binary eval suites
- Anthropic Skills 2.0: Grader sub-agent implements the same dual-layer architecture with deterministic + LLM judge assertions
- The pattern scales to 15-30 test inputs as documented in the test-input-coverage-design finding
- Conceptually aligned with MetaSystem's three-tier grading hierarchy finding, which distinguishes deterministic, heuristic, and semantic evaluation tiers

## Contract

### Preconditions
An agent skill or task produces outputs that need automated quality evaluation. Both structural requirements (format, length, required fields) and semantic requirements (tone, coherence, factual accuracy) exist for the output. An LLM is available for judge calls. At least 3 test inputs with known-good outputs exist for baseline comparison.

### Invariants
Every assertion returns exactly true or false -- never a numeric score. Deterministic assertions are evaluated before LLM-as-judge assertions (fail-fast ordering). Eval files are locked from modification by the agent under evaluation. All assertions in a suite are mutually satisfiable -- no conflicting requirements.

### Governance
Assertion suites are reviewed when task requirements change or new failure modes are observed. LLM-as-judge consistency is monitored for threshold drift by periodically rerunning against stable reference inputs. New assertions require justification that they test an observed failure mode, not a theoretical one. Eval file write access is restricted to human reviewers or a designated eval-maintenance role, never the agent under evaluation.

### Recovery
If assertions are discovered to be mutually unsatisfiable: disable the conflicting subset, resolve the conflict (typically by making one requirement conditional on the other), then re-enable and verify satisfiability. If LLM-as-judge drift is detected: recalibrate by rerunning against reference inputs with known-correct verdicts and adjusting the judge prompt. If an agent modifies its own eval files: revert from version control, investigate the access control failure, and strengthen the lockdown mechanism.
