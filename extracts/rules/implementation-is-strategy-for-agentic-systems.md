---
title: "Assess Implementation Feasibility Before Committing Architecture"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "implementation-is-strategy-for-agentic-systems"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent workflow design when the workflow crosses system or permission boundaries"
    - "any decision to build or buy a new agent integration before architecture is committed"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "trivial — the rule applies at design time; running the four checks before committing costs negligible effort; abandoning is costless"
  auditability: "high — each of the four viability tests produces a discrete finding (pass/fail/unknown) that is logged as part of the design record"
  evidence_strength: "Strong (production-tested)"
  adoption:
    status: "Partially Adopted"
    notes: "MetaSystem's spec-before-build constraint (DD-29) and verify-before-build principle partially instantiate this. The four specific viability tests are not yet codified as a pre-design checklist."
contract:
  preconditions: "A new agent workflow is being designed or a new integration is being considered. The workflow crosses at least one system, permission, or organizational boundary."
  invariants: "Before architectural commitment, all four viability tests are assessed: (1) Authentication — can the agent authenticate against every required system? (2) Permission model — does the permissions model account for agents, not just humans? (3) Context assembly cost — is per-run context assembly economically viable? (4) Auditability — can the agent's actions be attributed and proven to a regulator? A single failing test is sufficient to change the shape of the roadmap."
  governance: "The four viability tests are assessed by a technical architect (not solely a product or business owner) before design is committed. Results are recorded in the design record. A failing test is not a blocker — it is a constraint that shapes the design. Assessment must precede capital commitment, not follow it."
  recovery: "If a viability test fails after architecture is committed, treat as a design defect requiring roadmap revision. Do not attempt to work around a failed authentication or permission model test with agent-level hacks (e.g., screen scraping, credential sharing). If context assembly cost renders a strategy uneconomical, re-scope the workflow before continuing."
tags:
  - "extracted-artifact"
  - "rule"
  - "architecture"
  - "agent-design"
  - "feasibility"
  - "pre-design"
---

# Assess Implementation Feasibility Before Committing Architecture

**Source:** [[implementation-is-strategy-for-agentic-systems]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

A new agent workflow is being designed, a new tool or integration is being evaluated, or a strategic decision is being made that depends on an agent reaching one or more external systems. The workflow crosses at least one system, permission, or organizational boundary.

## Action

**Required:** Before committing architecture, assess all four viability tests:

1. **Authentication** — Can the agent authenticate against every system it needs to touch? (Not: "we assume the API exists." Confirm the specific auth mechanism works for an agent identity, not a human login.)
2. **Permission model** — Does the target system's permission model account for agents acting on behalf of users, not just humans clicking through screens? (Screen-based permission models fail when agents bypass the screen.)
3. **Context assembly cost** — Does every agent run need to reassemble business context from scratch? What is the token cost per run at target volume? Is it economically viable?
4. **Auditability** — Can you produce a log attributing each agent action to a specific user, session, and business context that would satisfy a regulator or incident review?

**Forbidden:** Treating any of the four tests as "implementation details to be worked out later." Committing capital, team time, or roadmap space before the four tests are assessed.

## Boundary

Enforced at the specification stage — before design is committed, before implementation begins, before build-vs-buy decisions are finalized. The rule does not apply to single-system automations that do not cross boundaries; it is specifically triggered by cross-system, cross-permission, or cross-organizational agent workflows.

## Enforcement

- **Mechanism:** Design records for agent workflows that cross boundaries must include a four-test viability assessment section. Each test has three possible results: Pass, Fail (with specific constraint identified), or Unknown (with a plan to resolve before implementation).
- **Check (deterministic):** No test may remain Unknown at the point of architectural commitment. Pass or Fail are both acceptable — Unknown is not. A Fail is a design constraint to be addressed, not a disqualifier.
- **Violation response:** If architectural commitment is made before all four tests are assessed, treat the design as provisional. Do not begin implementation until the assessment is complete and constraints are incorporated into the design.
- **Cannot be self-certified:** The assessment must be performed by someone with access to the target system's actual authentication and permission mechanisms — not based on vendor documentation alone.

## Rationale

For agentic systems, implementation constraints are strategy constraints. The traditional enterprise sequence — strategy at the top, implementation at the bottom — was designed for bounded SaaS tools with published APIs and clean role-based permission models. Agents are not bounded: they act across systems, they are not human users, and their actions must be attributable at scale. When these constraints are discovered during implementation rather than before design, the result is a failed strategy discovered 6 months in — after capital and team time have been committed.

The Lilly/McKinsey incident (the source's canonical example) was not a security failure but a procurement/build failure that surfaced as a security incident. Technical teams were not at the table when the platform's architecture was shaped. The platform was designed for humans clicking screens. When agents arrived, the architectural assumptions failed. The cheapest intervention is moving the architectural review earlier — before commitment, not after.

For MetaSystem: this rule validates the spec-before-build constraint and the verify-before-build principle as applied to agent workflow design specifically. Any new skill or agent workflow that crosses system boundaries should be assessed against the four tests before the design is committed.

## Failure Modes

- **Analysis paralysis.** The four tests become a heavyweight feasibility study that slows experimentation. Mitigation: the tests are lightweight pre-checks — yes/no/unknown with a one-line rationale — not full feasibility studies. Time-box to 30 minutes.
- **False negatives.** A test flags a constraint that is actually solvable with modest engineering effort. Mitigation: a Fail result triggers constraint documentation and design adjustment, not abandonment. The test identifies the constraint; the architect decides what to do with it.
- **Scope creep of "strategic."** If every workflow is subject to the four tests, the distinction loses meaning. Mitigation: the rule triggers specifically on cross-boundary workflows — any workflow touching more than one system, permission domain, or organizational boundary.
- **Assessment based on vendor documentation only.** Authentication and permission models described in docs may not reflect actual agent-identity behavior. Mitigation: require hands-on verification (proof-of-concept auth call) before recording a Pass on the Authentication test.

## Contract

### Preconditions
A new agent workflow is being designed or a new integration is being considered. The workflow crosses at least one system, permission, or organizational boundary.

### Invariants
Before architectural commitment, all four viability tests are assessed: (1) Authentication, (2) Permission model, (3) Context assembly cost, (4) Auditability. A single failing test is sufficient to change the shape of the roadmap. No test may remain Unknown at the point of architectural commitment.

### Governance
The four viability tests are assessed by a technical architect before design is committed. Results are recorded in the design record. Assessment must precede capital commitment, not follow it.

### Recovery
If a viability test fails after architecture is committed, treat as a design defect requiring roadmap revision. Do not attempt to work around a failed authentication or permission model test with agent-level hacks. If context assembly cost renders a strategy uneconomical, re-scope the workflow before continuing.
