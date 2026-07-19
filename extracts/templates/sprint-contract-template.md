---
title: "Sprint Contract Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "sprint-contract-negotiation-pattern"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "production-agent-execution.harvest-queue"
identification_report: "production-agent-execution.harvest-queue.md::sprint-contract-negotiation-pattern::template::sprint-contract-template"
deployed: false
deployed_to: null
context:
  applies_to:
    - "a generator-evaluator pair (two agents, or an agent and a human reviewer) that needs to agree on what 'done' means before a unit of work starts"
    - "iterative build loops where evaluation has drifted toward subjective quality judgments and generators can game vague standards"
    - "teams that want to reduce wasted iteration cycles by surfacing scope disagreements before coding begins rather than after review"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — a negotiated document; renegotiating or discarding a sprint contract has no downstream migration cost beyond re-running the sprint it governed"
  auditability: "high — every criterion is stated as a testable pass/fail condition; a third party can independently check the generator's output against the contract without needing the negotiation history"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Production-tested across multiple application types (retro games, DAWs, museum websites) by one harness-design team; one retro-game sprint carried 27 testable criteria for a single feature (the level editor)."
contract:
  preconditions: "A generator and an evaluator (two agents, or an agent and a human) both have visibility into the unit of work about to start. The evaluator is able to reject or renegotiate scope before the generator begins — the contract must be agreed before coding, not written after the fact to justify what was already built."
  invariants: "Every success criterion is granular and testable — stated so that a third party can check pass/fail without subjective judgment. Both generator and evaluator explicitly agree to the contract before work starts; an unagreed draft is not a contract. The evaluator scores only against the agreed criteria, never against unstated preferences discovered after the fact. Scope disagreements are negotiated and resolved in the contract, not carried silently into implementation."
  governance: "Owner: the evaluator role holds veto over contract acceptance — the generator proposes, the evaluator negotiates and must agree before work starts. Neither party may unilaterally add or drop criteria mid-sprint; changes require renegotiation and a new agreed contract."
  recovery: "If the generator's output fails a criterion at review: score it as failed against that specific criterion — do not accept a subjective override in either direction. If a criterion turns out to be untestable or ambiguous once work has started: pause, renegotiate that criterion specifically, and record the correction rather than silently reinterpreting it at scoring time. If over-specification makes evaluation brittle (too many criteria for the sprint's actual size): cut to the criteria that matter for this sprint's stated goal and note the trim in the contract's amendment log. If a criterion becomes 'testable but not meaningful' (teaching-to-the-test effect observed): replace it with a criterion that captures the underlying intent, don't just keep testing the proxy."
tags:
  - "extracted-artifact"
  - "template"
  - "generator-evaluator"
  - "acceptance-criteria"
  - "intent-engineering"
---

# Sprint Contract Template

**Source:** [[sprint-contract-negotiation-pattern]]
**Form:** template
**Extraction date:** 2026-07-19

A pre-work agreement between a generator and an evaluator that turns "what does done look like" into a negotiated list of granular, testable criteria — agreed before coding begins, not inferred afterward. Evaluation then scores against the specific agreed criteria rather than subjective quality judgment, which is what makes the evaluation deterministic and keeps generators from gaming vague standards. Production sprints have carried over two dozen criteria for a single feature; the contract is meant to hold that level of granularity without collapsing into either under-specification (vague, subjective) or over-specification (brittle, teaching-to-the-test).

## Variables

| Variable | Type | Description |
|----------|------|-------------|
| `{{SPRINT_GOAL}}` | string | One-sentence statement of what this sprint delivers. |
| `{{SCOPE_ITEM}}` | string, repeating | A discrete piece of implementation scope proposed by the generator for this sprint. |
| `{{CRITERION}}` | string, repeating | One granular, testable success criterion — phrased so pass/fail is checkable without subjective judgment. |
| `{{CRITERION_TEST}}` | string, per criterion | How the criterion is checked (the concrete test, inspection, or observable condition). |
| `{{NEGOTIATION_NOTE}}` | string, optional, repeating | A scope or criterion point the generator and evaluator disagreed on and how it was resolved before agreement. |
| `{{AGREED_BY}}` | (generator, evaluator) | Explicit sign-off marker from both parties — the contract is not active until both have agreed. |

## Body

```markdown
# Sprint Contract — {{SPRINT_GOAL}}

**Status:** DRAFT until both parties sign off below.

## Proposed Scope

- {{SCOPE_ITEM}}
- {{SCOPE_ITEM}}

## Success Criteria

<!-- Each criterion must be testable — a third party could check pass/fail without
     asking either the generator or evaluator what they meant. -->

| # | Criterion | Test |
|---|---|---|
| 1 | {{CRITERION}} | {{CRITERION_TEST}} |
| 2 | {{CRITERION}} | {{CRITERION_TEST}} |

## Negotiation Notes

<!-- Record scope or criterion disagreements and how they were resolved.
     Omit if the first proposal was accepted as-is. -->
- {{NEGOTIATION_NOTE}}

## Agreement

- [ ] Generator agrees this scope and these criteria are achievable and complete for the stated goal.
- [ ] Evaluator agrees these criteria, if all met, constitute "done" — no additional unstated criteria will be applied at review.

**Agreed by:** {{AGREED_BY}}

<!-- Work does not start until this section is checked and signed. -->
```

## Usage

Render before any coding starts for the sprint. The generator drafts Proposed Scope and an initial Success Criteria list; the evaluator reviews, pushes back on anything vague, untestable, or missing, and the two negotiate until both can check the Agreement boxes. At review time, the evaluator scores strictly against the agreed criteria table — no criteria are added after the fact, and no criteria are silently dropped because they turned out inconvenient. If a criterion is discovered to be wrong or untestable mid-sprint, pause and renegotiate rather than reinterpreting it at scoring time.

## Variation Axis

What drives different renderings of this template:

- **Criterion count** — small sprints may need only a handful of criteria; larger or higher-risk sprints (the source example ran 27 criteria for one feature) need enough granularity that nothing material is left to subjective judgment, without drifting into criteria that test trivia.
- **Negotiation depth** — a well-understood, low-risk sprint may go through the contract in one pass; a novel or ambiguous sprint may need multiple negotiation rounds recorded in the Negotiation Notes before agreement.
- **Party composition** — generator and evaluator can be two agents, an agent and a human reviewer, or two humans; the contract's discipline (testable criteria, explicit sign-off, no post-hoc criteria) holds regardless of who is on each side.
- **Amendment policy** — some deployments freeze the contract entirely once agreed (any needed change forces a new negotiation); others allow narrowly-scoped amendments logged in Negotiation Notes if both parties agree mid-sprint. State the policy explicitly per deployment.

## Contract

### Preconditions
A generator and an evaluator (two agents, or an agent and a human) both have visibility into the unit of work about to start. The evaluator is able to reject or renegotiate scope before the generator begins — the contract must be agreed before coding, not written after the fact to justify what was already built.

### Invariants
Every success criterion is granular and testable — stated so that a third party can check pass/fail without subjective judgment. Both generator and evaluator explicitly agree to the contract before work starts; an unagreed draft is not a contract. The evaluator scores only against the agreed criteria, never against unstated preferences discovered after the fact. Scope disagreements are negotiated and resolved in the contract, not carried silently into implementation.

### Governance
Owner: the evaluator role holds veto over contract acceptance — the generator proposes, the evaluator negotiates and must agree before work starts. Neither party may unilaterally add or drop criteria mid-sprint; changes require renegotiation and a new agreed contract.

### Recovery
If the generator's output fails a criterion at review: score it as failed against that specific criterion — do not accept a subjective override in either direction. If a criterion turns out to be untestable or ambiguous once work has started: pause, renegotiate that criterion specifically, and record the correction rather than silently reinterpreting it at scoring time. If over-specification makes evaluation brittle (too many criteria for the sprint's actual size): cut to the criteria that matter for this sprint's stated goal and note the trim in the contract's amendment log. If a criterion becomes 'testable but not meaningful' (teaching-to-the-test effect observed): replace it with a criterion that captures the underlying intent, don't just keep testing the proxy.
