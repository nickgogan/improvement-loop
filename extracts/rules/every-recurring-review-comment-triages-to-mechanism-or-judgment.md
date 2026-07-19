---
title: "Every Recurring Review Comment Triages to Mechanism or Judgment-Only — Review-Obsolescence Triage Rule"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "review-obsolescence-as-design-goal"
identification_report: "agent-governance-and-trust.harvest-queue.md::review-obsolescence-as-design-goal::rule::every-recurring-review-comment-triages-to-mechanism-or-judgment"
extraction_date: "2026-04-27"
last_change_session: 103
last_change_sl: "session-103-codifier-complete-extract-artifacts-write-phase"
deployed: false
deployed_to: null
context:
  applies_to:
    - "code review processes that produce comments at non-trivial volume"
    - "engineering teams adopting review-as-quality-mechanism rather than review-as-bottleneck"
    - "any change-review system where reviewer attention is finite and comments recur across changes"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — the triage record is metadata; rolling back the rule means stopping the triage step, not undoing existing decisions"
  auditability: "high when triage decisions and their downstream mechanisms are recorded as a reviewable table; medium when tracked verbally; low when the rule is aspirational"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Production-tested in ecosystems that adopted automated formatting and linting (go fmt, prettier) — those are mechanism-triages of historically recurring whitespace and style comments. Explicit triage-as-discipline practice is less common as a stated rule but is the logical generalization of those well-documented cases."
contract:
  preconditions: "A code review process exists that produces comments. Comments are observable to a tracking surface (PR thread, review tool, comment log). The team has authority to introduce mechanism (linter, schema constraint, CI rule, generator, type system) or to mark a class as judgment-only."
  invariants: "Every review comment that recurs (the same comment or class of comment appearing across two or more changes) triages to one of exactly two terminal states: (a) **mechanism** — a linter, schema, CI rule, type, generator, or automated check that prevents the comment class from being authorable, with the mechanism implemented or scheduled before the next recurrence; or (b) **judgment-only** — an explicit declaration that this class requires human evaluation and cannot be automated, with stated reasoning. No third state exists. Comments left in 'we'll deal with it later' or 'recurring annoyance, no action' limbo are violations."
  governance: "Owner: the team or function that runs the review process. The rule must be embedded in review-process policy with a stated cadence (e.g., 'recurring comments triaged within N reviews'). A tracking surface (a Review Obsolescence table or equivalent) records each triaged class, its terminal state, and — for mechanism-triaged classes — a link to the implementing change. Audit verifies that recurring comments either have a mechanism shipped or carry a judgment-only declaration with reasoning."
  recovery: "If a comment class has recurred without triage past the stated cadence: triage it now; the recurrence count is the load-bearing signal, not the calendar date. If a previously-triaged-as-judgment-only class becomes mechanizable later (a new tool, language feature, or check makes prevention possible): re-triage to mechanism and ship the prevention. If a mechanism is introduced but the comment class still recurs: the mechanism is incomplete or wrongly-scoped — re-open the triage and either widen the mechanism or accept that the residual cases are judgment-only."
tags:
  - "extracted-artifact"
  - "rule"
  - "code-review"
  - "review-obsolescence"
  - "process-governance"
  - "quality-at-source"
---

# Every Recurring Review Comment Triages to Mechanism or Judgment-Only — Review-Obsolescence Triage Rule

**Source:** [[review-obsolescence-as-design-goal]]
**Source (additional):** [[pattern-scale-signals-systemic-not-individual-failure]]
**Source (additional):** [[garbage-collection-day-persona-review-agents]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A code review process produces comments at any non-trivial volume. Some comments recur — the same comment, or comments in a clearly recognizable class, appear across multiple changes by multiple authors. The team has authority to introduce mechanisms (linters, schema constraints, CI rules, generators, type systems) and to declare a class as judgment-only.

Scope of application: any review-comment surface where recurrence is observable and where the team can act on the triage decision. Includes traditional PR review, design review with recurring architectural comments, and security review with recurring vulnerability classes.

## Action

**Required:** When a review comment recurs (same comment, or recognizable class, across two or more changes), triage the class to exactly one terminal state:

1. **Mechanism** — implement or schedule a linter, schema constraint, CI rule, type, generator, or automated check that makes the comment class unauthorable. The mechanism is shipped or has a tracked plan with a deadline before the next recurrence.

2. **Judgment-only** — record an explicit declaration that this class requires human evaluation and cannot be reduced to a mechanism, with stated reasoning. The declaration covers the scope of the judgment (what specifically requires human attention).

Record the triage decision on a tracking surface (a Review Obsolescence table or equivalent) with the class name, its terminal state, the implementing change link (for mechanism), or the reasoning (for judgment-only).

**Forbidden:** Leaving a recurring comment class in an undeclared state — no mechanism, no judgment-only declaration, just "we keep seeing this." Treating the same class as judgment-only in some reviews and mechanism-eligible in others without re-triaging. Letting "we'll automate it later" carry forward across more recurrences without a tracked plan.

## Boundary

Enforced at the review-process level, not the per-PR level. A single comment in a single PR is fine; the rule fires when a class shows up across reviews. The triage cadence (how many recurrences before triage is required) is set by the team — but the cadence must be stated, and the limit must be load-bearing (overruns trigger triage, not procrastination).

Out of scope: one-off comments that don't recur, comments specific to a single author's specific bug (educational, not systematic), comments on experimental or pre-merge code that doesn't reach the shared review process.

## Enforcement

- **Mechanism:** A periodic review-process audit reads the comment history (or a tagged subset), clusters by recurrence, and verifies every recurring class has a triage record. Comments that exceed the recurrence cap without triage are flagged. The Review Obsolescence table is the tracking surface; a comment class without a row is a violation.
- **Check (deterministic):** For every comment class `K` with recurrence `r >= cap`: `triage_record(K) != null` AND `triage_record(K).terminal_state in {mechanism, judgment-only}` AND (`mechanism ⟹ implementing_change != null OR scheduled_plan_with_deadline != null`) AND (`judgment-only ⟹ reasoning != null`). Any branch false → violation; the class is in undeclared limbo.
- **Violation response:**
  - *Recurring class without a triage record:* triage now; do not let the class continue recurring while waiting for an arbitrary future moment.
  - *Mechanism declared but not shipped past deadline:* re-evaluate — either ship the mechanism, push the deadline with a stated reason, or reclassify to judgment-only if the mechanism turned out to be infeasible.
  - *Judgment-only declared but a new tool makes mechanism feasible:* re-triage to mechanism and ship.
  - *Mechanism shipped but class still recurs:* the mechanism is incomplete or wrongly-scoped — open a follow-up to widen the mechanism or accept residual cases as judgment-only.
- **Cannot be silently exempted:** A review-process owner who keeps a class in "we keep seeing this, no action" indefinitely is in violation. The rule does not require fast triage — it requires *eventual, deliberate, recorded* triage with a stated rationale for delay if any.

## Rationale

The rule exists because review processes accumulate friction by default. Each recurring comment class is a tax on every future change in that area; ignoring recurrences makes review the perpetual bottleneck instead of a transient quality gate.

The rule's structure — triage to mechanism *or* judgment-only — is the positive-space restatement of the let-it-recur anti-pattern. The two terminal states cover the full space: either the comment can be eliminated by an automated check (mechanism) or it cannot (judgment-only). There is no legitimate third state. "We haven't decided" is a failure mode masquerading as a position.

The rule does not demand that all comments become mechanisms. Architectural and design judgment is real and valuable; declaring a class as judgment-only is a first-class triage outcome, not a defeat. The rule's discipline is about being *explicit* about which classes are which — not about eliminating human judgment from review.

The rule respects mechanism-feasibility over time. A class can move from judgment-only to mechanism when new tools become available; the rule accommodates this with re-triage. The audit cost is bounded — only recurring classes trigger the triage; one-off comments and class-specific bugs don't.

### Additional Evidence

The pattern-scale diagnostic framework ([[pattern-scale-signals-systemic-not-individual-failure]]) broadens the application scope of this rule beyond code review to any recurring failure at governance scale. When the same gap appears across multiple governance surfaces — not just PR threads — the diagnostic is the same: a recurring pattern signals a process failure, not individual error. The triage rule applies: the pattern triages to mechanism (a structural default that prevents the gap) or judgment-only (an explicit declaration that the class requires human evaluation). "Count the instances" is the trigger; three or more recurrences of the same governance gap is the threshold for architectural intervention rather than per-instance fixing. Training or per-file remediation is the wrong mitigation at pattern scale; the correct response is the same as for recurring review comments — ship a mechanism or declare judgment-only with reasoning.

The garbage-collection-day pattern ([[garbage-collection-day-persona-review-agents]]) supplies a concrete, named cadence implementation of this rule's "stated cadence" governance requirement — a fixed weekly ritual (every Friday) rather than an ad-hoc or purely count-triggered check-in. It also broadens the trigger condition: rather than waiting for a comment class to recur across two or more changes, the ritual triages *every* piece of review friction observed within the week, once, on a fixed schedule — a stricter cadence variant teams may adopt when they want zero-lag conversion rather than a recurrence-count threshold. It corroborates the judgment-only terminal state's implementation as living documentation: bucketing recurring feedback by the reviewing engineer's persona (front-end architect, reliability engineer, scalability engineer) and consulting that persona's accumulated "what good looks like" doc is one concrete shape a judgment-only triage record can take, subsequently machine-enforced by a per-persona review agent that runs on every push.

## Failure Modes

- **Triage theater.** The Review Obsolescence table is created and entries are added, but no mechanisms ship and no judgment-only declarations carry meaningful reasoning. Mitigation: enforce that mechanism entries have a linked change or a scheduled plan; enforce that judgment-only entries have non-trivial reasoning, not just "needs human review."
- **Cap drift.** The recurrence cap is loose at first ("triage anything that recurs more than 5 times") and gradually relaxes ("we'll get to it eventually"). Mitigation: keep the cap stated and load-bearing; treat overruns as triage triggers, not as cap-relaxation triggers.
- **Mechanism-bias overreach.** Every comment class is forced into mechanism when many are legitimately judgment-only; the result is brittle linting that fights legitimate variation. Mitigation: judgment-only is a first-class outcome, not a fallback when mechanism fails — declare it deliberately.
- **Judgment-bias underreach.** Every comment class is declared judgment-only and the team avoids the engineering effort of building mechanisms. Mitigation: track the ratio of mechanism vs judgment-only triages over time; a sustained skew toward judgment-only is a signal that mechanism work is being avoided, not that all comments are genuinely judgment.
- **Class-boundary disagreement.** Reviewers disagree on whether two comments are the same class or two distinct classes. Mitigation: the triage record names the class explicitly; ambiguity is resolved by the triage owner; new comments that don't fit the named class become candidates for a new triage.
- **Mechanism that creates new comment classes.** A linter is shipped but flags edge cases that turn into a new recurring comment class. Mitigation: the new class is a new triage; the mechanism's existence is not a free pass for follow-on classes.

## Contract

### Preconditions
A code review process exists that produces comments. Comments are observable to a tracking surface (PR thread, review tool, comment log). The team has authority to introduce mechanism (linter, schema constraint, CI rule, generator, type system) or to mark a class as judgment-only.

### Invariants
Every review comment that recurs (the same comment or class of comment appearing across two or more changes) triages to one of exactly two terminal states: (a) mechanism — a linter, schema, CI rule, type, generator, or automated check that prevents the comment class from being authorable, with the mechanism implemented or scheduled before the next recurrence; or (b) judgment-only — an explicit declaration that this class requires human evaluation and cannot be automated, with stated reasoning. No third state exists. Comments left in 'we'll deal with it later' or 'recurring annoyance, no action' limbo are violations.

### Governance
Owner: the team or function that runs the review process. The rule must be embedded in review-process policy with a stated cadence (e.g., 'recurring comments triaged within N reviews'). A tracking surface (a Review Obsolescence table or equivalent) records each triaged class, its terminal state, and — for mechanism-triaged classes — a link to the implementing change. Audit verifies that recurring comments either have a mechanism shipped or carry a judgment-only declaration with reasoning.

### Recovery
If a comment class has recurred without triage past the stated cadence: triage it now; the recurrence count is the load-bearing signal, not the calendar date. If a previously-triaged-as-judgment-only class becomes mechanizable later (a new tool, language feature, or check makes prevention possible): re-triage to mechanism and ship the prevention. If a mechanism is introduced but the comment class still recurs: the mechanism is incomplete or wrongly-scoped — re-open the triage and either widen the mechanism or accept that the residual cases are judgment-only.
