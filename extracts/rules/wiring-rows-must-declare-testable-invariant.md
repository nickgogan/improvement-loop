---
title: "Wiring Rows Must Declare a Testable Invariant"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "invariant-column-as-contract-field"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "building-agentic-systems.harvest-queue"
identification_report: "building-agentic-systems.harvest-queue.md::invariant-column-as-contract-field::rule::wiring-rows-must-declare-testable-invariant"
deployed: false
deployed_to: null
context:
  applies_to:
    - "authors of installable multi-file agent systems writing per-concern rows into a machine-readable install contract"
    - "reviewers evaluating whether a proposed plan for porting a system to a new host actually preserves what mattered, not just what mechanism was used"
    - "auditors checking whether an install or port succeeded beyond mere file-copy verification"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — a schema/authoring-discipline requirement; dropping it reverts to rows with no acceptance test, at no migration cost"
  auditability: "high — presence of a non-empty, non-mechanism-worded invariant per row is mechanically checkable, and each invariant is designed to double as a binary post-install probe"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented as a design-gate decision in one production agentic system, backed by a field-level survey of adjacent ecosystem formats that found no equivalent construct anywhere."
contract:
  preconditions: "A system-contract-style wiring row exists or is being authored for a harness-integration concern (an entry point, a rule-injection mechanism, a memory scope, a registry, or similar). The row already has tier, capability, purpose, and degradation fields, or is being authored alongside them."
  invariants: "Every wiring row carries a non-empty `invariant` field stating the property that must survive any adaptation of that row, regardless of which mechanism the target platform uses to satisfy it. The invariant is phrased as a guarantee ('X is never Y without Z'), never as a mechanism description ('file X exists at path Y'). The invariant is binary-testable in a fresh session — a reviewer or an automated probe can evaluate it to true/false without needing additional interpretation. A row's `degradation` field, however weak, must still preserve the row's invariant; degradation may weaken the mechanism but never the invariant itself."
  governance: "Owner: whoever authors or reviews the system-contract's wiring section. New or edited rows are rejected at review if the invariant field is missing, restates a mechanism instead of a guarantee, or is too vague to probe. An adaptation or port review additionally requires each row's plan to state how its invariant is preserved under the new mechanism — silence on this point blocks the port review."
  recovery: "If a row has no invariant field: the row is incomplete — return it to authoring before it enters the contract. If the invariant is phrased as a mechanism: rewrite it as the guarantee the mechanism exists to provide, then re-review. If the invariant is unprobeable (vague, subjective): tighten it until a fresh reviewer could evaluate it to true/false, or split it into multiple probeable invariants. If a post-install probe against a row's invariant fails: treat it as a mechanism problem — the row returns to adaptation planning; the invariant itself does not bend to fit whatever the mechanism happened to produce."
tags:
  - "extracted-artifact"
  - "rule"
  - "system-contract"
  - "invariants"
  - "portability"
---

# Wiring Rows Must Declare a Testable Invariant

**Source:** [[invariant-column-as-contract-field]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A wiring row is being authored, reviewed, or ported as part of a machine-readable system contract for an installable multi-file agent system — any row that describes a single harness-integration concern (an entry point, a rule-injection mechanism, a memory scope, a governance registry, and similar).

## Action

**Required:** Every wiring row states an `invariant`: the property that must survive *any* adaptation of that row, no matter which mechanism the target platform uses to satisfy it. The invariant is written as a guarantee, not a mechanism — "governance-tier files are never edited without explicit human approval," not "the registry file exists at `governance/registry.yaml`." When a row's plan is adapted to a new target platform, the plan must state, per row, how the invariant is preserved under the new mechanism.

**Forbidden:** Leaving a row's invariant field empty or absent. Writing an invariant that merely restates the mechanism (reimporting the exact portability problem the field exists to solve). Writing an invariant so vague ("the system stays safe") that no fresh reviewer or automated probe could evaluate it to true or false. Letting a row's degradation path weaken the invariant itself rather than only the mechanism that satisfies it.

## Boundary

Enforced at three points: (1) contract authoring/review — a row is not complete until its invariant field is present and probeable; (2) adaptation-plan review — a proposed port must state, per row, how the invariant is preserved under the new mechanism, before the port proceeds; (3) post-install verification — each row's invariant becomes the spec for a binary self-administrable probe run against the live install.

## Enforcement

- **Mechanism:** A contract-completeness audit checks that every wiring row has a non-empty invariant field, distinct from that row's mechanism/capability fields. A separate binary probe is run per row at post-install verification, using the invariant text directly as the probe spec.
- **Check (deterministic):** `(invariant_field_present == true) AND (invariant_is_not_a_restated_mechanism == true) AND (invariant_is_binary_evaluable == true)`. Any branch false → the row fails completeness review.
- **Violation response:**
  - *Missing invariant:* row is incomplete; return to authoring before it enters the contract.
  - *Mechanism-disguised-as-invariant:* rewrite as the guarantee the mechanism exists to provide, then re-review.
  - *Unprobeable invariant:* tighten the wording, or split into multiple probeable invariants, until a fresh reviewer or automated check can evaluate it.
  - *Failed post-install probe:* treat as a mechanism failure — the row returns to adaptation planning; the invariant itself is never relaxed to match whatever the mechanism produced.

## Rationale

Porting an agent system to a new harness always changes the mechanism — a path-scoped rule becomes a different file convention, a config field, or a prose paragraph depending on the host. What must not change is the guarantee the original mechanism existed to provide. Without a named, testable invariant per row, "did the port work?" collapses into "did we copy the files?" — a question that can be answered yes while the actual guarantee silently disappeared. Declaring the invariant turns every row into a mechanism-independent acceptance test: something a receiving platform's install plan can be checked against, and something a post-install probe can verify without knowing anything about the source platform's original implementation.

A field-level survey of adjacent ecosystem formats (agent-card and installer-manifest conventions) found this construct absent everywhere surveyed — those formats declare *capabilities required*, never *properties preserved under adaptation*. The gap is not incidental: capability declarations describe what a platform must offer, but say nothing about what must still be true after the platform offers it in its own way. The invariant field closes that gap directly.

## Contract

### Preconditions
A system-contract-style wiring row exists or is being authored for a harness-integration concern (an entry point, a rule-injection mechanism, a memory scope, a registry, or similar). The row already has tier, capability, purpose, and degradation fields, or is being authored alongside them.

### Invariants
Every wiring row carries a non-empty `invariant` field stating the property that must survive any adaptation of that row, regardless of which mechanism the target platform uses to satisfy it. The invariant is phrased as a guarantee ("X is never Y without Z"), never as a mechanism description ("file X exists at path Y"). The invariant is binary-testable in a fresh session — a reviewer or an automated probe can evaluate it to true/false without needing additional interpretation. A row's `degradation` field, however weak, must still preserve the row's invariant; degradation may weaken the mechanism but never the invariant itself.

### Governance
Owner: whoever authors or reviews the system-contract's wiring section. New or edited rows are rejected at review if the invariant field is missing, restates a mechanism instead of a guarantee, or is too vague to probe. An adaptation or port review additionally requires each row's plan to state how its invariant is preserved under the new mechanism — silence on this point blocks the port review.

### Recovery
If a row has no invariant field: the row is incomplete — return it to authoring before it enters the contract. If the invariant is phrased as a mechanism: rewrite it as the guarantee the mechanism exists to provide, then re-review. If the invariant is unprobeable (vague, subjective): tighten it until a fresh reviewer could evaluate it to true/false, or split it into multiple probeable invariants. If a post-install probe against a row's invariant fails: treat it as a mechanism problem — the row returns to adaptation planning; the invariant itself does not bend to fit whatever the mechanism happened to produce.
