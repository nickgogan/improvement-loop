---
title: "Author the Validation Contract Before Any Code Exists"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "pre-code-validation-contracts-dual-blind-validators"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "verifying-agent-output.harvest-queue"
identification_report: "verifying-agent-output.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Any workflow where an agent or team plans work and then implements it, and where correctness has to be verified afterward"
    - "Teams that want their tests to define intended behavior rather than ratify whatever the code ended up doing"
    - "Long-running autonomous builds that need a stable, implementation-independent definition of 'done' to check against at each milestone"
    - "Situations where test-coverage percentage is being used as the done-signal and a stronger correctness guarantee is wanted"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — the rule governs when correctness assertions are authored; adopting or dropping it changes process, not shipped artifacts, and is reversible at the next planning cycle"
  auditability: "Strong — compliance is externally checkable: the validation-contract artifact either exists and predates the first implementation commit or it does not, and every feature either maps to at least one assertion or it does not."
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Production account: a commercial multi-agent build system attributes its ability to run for many days without drifting to writing hundreds of assertions before any code exists and validating against them each milestone (validation reportedly 'never succeeds on the first go'). Not yet adopted in this project's own extraction/synthesis pipeline."
contract:
  preconditions: "A planning or specification phase precedes implementation. An author (orchestrator, planner, or human) capable of enumerating correctness assertions for the work is available. A durable location exists to persist the contract artifact. The work decomposes into features or units of work, each of which can be assigned one or more assertions."
  invariants: "The validation contract is authored and persisted before any implementation code exists. Every feature is covered by at least one assertion, and the union of all features' assertions covers the whole contract. Each assertion is phrased as an implementation-independent statement of required behavior, not as a description of what the code does. The contract is not silently amended to match what the code turned out to do — any change after code exists is an explicit, logged decision."
  governance: "Owner: the orchestrator or planner who authors the contract during planning. The contract is the correctness authority and is kept distinct from the implementer. Amendments to the contract after implementation has begun must be explicit and reviewed, specifically to guard against implementation-shaped assertions creeping in."
  recovery: "No contract exists when implementation is about to begin: halt and author it first. A necessary assertion is discovered missing during implementation: add it as an explicit, logged amendment rather than quietly conforming the tests to the code. The contract is found to be under-specified or wrong: fix the contract (re-plan if needed) rather than validating against a known-wrong contract."
tags:
  - "extracted-artifact"
  - "rule"
---

# Author the Validation Contract Before Any Code Exists

**Source:** [[pre-code-validation-contracts-dual-blind-validators]]
**Form:** rule
**Extraction date:** 2026-07-19

A validation contract — the set of correctness assertions that define what "done" means — must be written during planning, before any implementation code exists. For a complex project this can be hundreds of individual assertions, with every feature assigned one or more so that the sum of all features' assertions covers the full contract. The point is provenance: assertions authored before there is any code cannot be shaped by what the code happens to do.

## Condition

A workflow will produce an implementation whose correctness must later be verified, and a planning phase precedes implementation. The rule fires at planning time — the moment before implementation code is written.

## Action

Author the validation contract during planning, before any implementation exists. Assign every feature or unit of work one or more assertions, such that the union of all assertions covers the contract. Do not author or finalize the correctness assertions after implementation, or in a way informed by the implementation.

## Boundary

Enforced at the planning → implementation boundary. The contract must be committed as a persistent artifact before the first line of implementation is written, and it is the reference the validators check against at each milestone.

## Enforcement

Checkable mechanically: (1) the validation-contract artifact exists and predates the first implementation commit (timestamp / commit ordering); (2) coverage completeness — every feature maps to at least one assertion; (3) assertions are phrased as implementation-independent guarantees ("X must happen when Y"), not as descriptions of the code's current behavior. Post-code amendments must appear as explicit, logged changes rather than silent edits.

## Rationale

"Tests written after implementation don't catch bugs, they confirm decisions." Post-hoc tests are shaped by what the code happens to do, not by what it was supposed to do, so coverage percentage alone is an unreliable done-signal. Writing the assertions before any code exists removes the code's ability to shape them. This directive complements — it does not replace — validator blindness (keeping the validator from seeing the implementation) and the red-step discipline of observing a new test fail before implementing; those guard adjacent failure modes.
