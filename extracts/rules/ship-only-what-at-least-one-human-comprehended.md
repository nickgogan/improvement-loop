---
title: "Ship Only What At Least One Human Comprehended — Comprehension-at-Merge Rule"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "dark-code-organizational-capability-problem"
identification_report: "agent-governance-and-trust.harvest-queue.md::dark-code-organizational-capability-problem::rule::ship-only-what-at-least-one-human-comprehended"
extraction_date: "2026-04-27"
last_change_session: 82
last_change_sl: "session-82-codifier-extract-artifacts-harvest-promotion-batch"
deployed: false
deployed_to: null
context:
  applies_to:
    - "AI-assisted development workflows where merge/deploy is the visible boundary between authored work and shipped state"
    - "engineering organizations adopting AI code generation at velocity that exceeds default human review capacity"
    - "any pull-request, change-request, or deploy gate covering AI-generated code, config, schema, or infrastructure"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "low — the rule sits at the merge/deploy gate; relaxing it later is cheap, but each ship-event of un-comprehended code accrues organizational comprehension debt that is expensive to retire"
  auditability: "high when the gate signal is captured as a structured artifact on the change record (commit trailer, PR field, deploy-ledger row); medium when only a human approval click is recorded; low when comprehension is implied by review-tool defaults"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner framing positions this as a competitive differentiator (founders/teams that understand their own code) rather than a published, deployed practice. Comprehension-gate tooling exists in early form at AI-native labs but is not widely productized."
contract:
  preconditions: "A change is queued for merge or deploy. The change includes one or more artifacts that were AI-generated (in whole or substantial part). A change-record surface exists where a comprehension signal can be attached (PR trailer, deploy-ledger field, commit metadata, or equivalent)."
  invariants: "No AI-generated artifact ships unless at least one human has produced a structured comprehension signal against it. The signal is a positive declaration tied to a specific human identity, not a default-on review-tool state. The signal records what was understood — not merely that the change was looked at — by capturing at minimum: the artifact identifiers covered, the human identity, and a non-trivial statement of what the change does and why (or an answer to a comprehension-gate prompt of equivalent depth)."
  governance: "Owner: any merge/deploy gate covering AI-generated work — PR review configurations, deploy-ledger schemas, change-management policy. The rule must be embedded explicitly at the gate (a structured comprehension field, a required check, or equivalent) rather than delegated to the implicit hope that reviewers comprehend before approving. Audit tooling reads the change record and verifies the comprehension signal was non-default and tied to an identity. Exemptions (purely mechanical changes, regenerated lockfiles, formatter-only diffs) must be declared explicitly in the gate's policy with a stated scope; silent exemption is a violation."
  recovery: "If a change merges without a comprehension signal: treat the resulting state as un-comprehended and require retroactive comprehension before any further change to the same surface area. If the signal turned out to be default-on or pro-forma (reviewer did not actually engage): retire the signal, escalate the gate (require structured prompt response), and re-comprehend. If the change is already in production and breaks: do not treat the post-incident comprehension as the recovery — the post-hoc understanding is a separate event and does not retroactively satisfy the pre-merge invariant."
tags:
  - "extracted-artifact"
  - "rule"
  - "ai-code-review"
  - "comprehension-gate"
  - "merge-gate"
  - "dark-code"
---

# Ship Only What At Least One Human Comprehended — Comprehension-at-Merge Rule

**Source:** [[dark-code-organizational-capability-problem]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A change is queued for merge or deploy. One or more artifacts in the change are AI-generated (in whole or substantial part). The change is about to cross the boundary from authored to shipped state — merge to a long-lived branch, deploy to a production environment, or equivalent.

Scope of application: AI-generated code, config, schema, infrastructure-as-code, and similar load-bearing artifacts. Mechanical changes (formatter output, regenerated lockfiles, vendor-bumped versions with no logic change) may be exempted *if* the exemption is declared explicitly in the gate's policy with a stated scope.

## Action

**Required:** Before merge or deploy completes, capture a structured comprehension signal tied to at least one human identity. The signal records what the human understood — at minimum: the artifacts covered, the human's identity, and a non-trivial statement of what the change does and why (or an answer to a comprehension-gate prompt of equivalent depth).

**Forbidden:** Merging or deploying AI-generated artifacts on the basis of (a) default-on review-tool states, (b) automated checks alone, (c) pro-forma approval clicks with no structured comprehension content, or (d) "the agent ran the tests" as the sole signal. None of these constitute the comprehension required by this rule.

## Boundary

Enforced at the merge or deploy gate — the visible transition between authored work and shipped state. Applies from the moment an AI-generated change is queued for that transition until either:

- a structured comprehension signal is attached to the change record, *or*
- the change is rejected, withdrawn, or sent back for further work.

Out of scope: pre-merge experimentation, scratch branches, exploratory code that never reaches the merge/deploy boundary. Mechanical changes that are exempted by stated policy are out of scope by design.

## Enforcement

- **Mechanism:** A structured field on the change record (PR trailer, deploy-ledger row, commit metadata) carries the comprehension signal. The field is non-optional for AI-generated changes; a missing or default-valued field blocks the gate.
- **Check (deterministic):** `(comprehension_signal != null) AND (signal.identity != "system" or default-on bot) AND (signal.body satisfies depth-minimum: covers artifacts + states what + why)`. Any branch false → gate blocked.
- **Violation response:**
  - *Missing signal:* gate blocked; the change cannot merge until a human comprehension signal is attached.
  - *Default-on or pro-forma signal:* retire the signal, escalate the gate (require structured prompt response), re-comprehend before unblocking.
  - *Already-shipped without signal:* retroactive comprehension required before any further change to the same surface area; record the comprehension debt explicitly in the change record and operations log.
- **Cannot be self-certified by the AI:** The comprehension signal must come from a human identity. AI self-attestation ("I generated this code and understand it") does not satisfy the rule. If the only available signal is the agent's, the gate is blocked.

## Rationale

The rule exists because AI velocity structurally decouples comprehension from authorship. AI generates a working artifact; the human who would otherwise have written it (and therefore understood it) is no longer in the loop. Without an explicit comprehension gate at merge or deploy, the default outcome is shipped code that no human understood — "dark code" — accumulating across the system as an organizational capability debt.

The rule is the positive-space restatement of the dark-code anti-pattern. Rather than enumerating ways comprehension can fail (default-on review, rubber-stamp approval, agent self-attestation, observability-as-substitute), the positive invariant is "at least one human comprehended, on the record, before ship." One rule, bounded enforcement.

The rule is not "every reviewer must comprehend every line." That formulation is unenforceable and produces theater. The minimum is one human, with a structured signal at depth — enough to anchor downstream debugging, audit, and accountability when the artifact later behaves unexpectedly.

## Failure Modes

- **Comprehension theater.** Reviewers fill in the structured field with templated language that satisfies the depth check but does not reflect actual engagement. Mitigation: rotate comprehension prompts; sample-audit signals against the actual artifacts; treat repeated templated responses as a signal of gate degradation.
- **Bottleneck inversion.** The comprehension gate becomes slower than the AI generation rate it was meant to discipline; teams route around it. Mitigation: scope the gate's depth to the change's blast radius (deeper for high-blast-radius changes); track gate latency as a first-class metric; resist the urge to weaken the rule when the gate is congested — congestion is a signal that AI velocity has outrun human comprehension capacity, not that the gate is wrong.
- **Default-on signal degradation.** Tooling defaults to "approved" or "comprehended" unless the reviewer explicitly opts out. Mitigation: enforce non-default values at the schema level; treat default values as missing signals; audit tooling configuration as part of the gate's governance.
- **Agent self-attestation creep.** The agent attaches a comprehension signal under its own identity, satisfying the field check but violating the human-identity invariant. Mitigation: gate the signal field to human identities at the schema level; reject any signal whose identity matches the change's authoring agent.
- **Exemption sprawl.** The "mechanical changes" exemption widens over time to cover non-mechanical AI-generated work. Mitigation: keep the exemption list explicit, narrow, and reviewed periodically; treat any change that includes a logic edit as non-mechanical regardless of how it was generated.

## Contract

### Preconditions
A change is queued for merge or deploy. The change includes one or more artifacts that were AI-generated (in whole or substantial part). A change-record surface exists where a comprehension signal can be attached (PR trailer, deploy-ledger field, commit metadata, or equivalent).

### Invariants
No AI-generated artifact ships unless at least one human has produced a structured comprehension signal against it. The signal is a positive declaration tied to a specific human identity, not a default-on review-tool state. The signal records what was understood — not merely that the change was looked at — by capturing at minimum: the artifact identifiers covered, the human identity, and a non-trivial statement of what the change does and why (or an answer to a comprehension-gate prompt of equivalent depth).

### Governance
Owner: any merge/deploy gate covering AI-generated work — PR review configurations, deploy-ledger schemas, change-management policy. The rule must be embedded explicitly at the gate (a structured comprehension field, a required check, or equivalent) rather than delegated to the implicit hope that reviewers comprehend before approving. Audit tooling reads the change record and verifies the comprehension signal was non-default and tied to an identity. Exemptions (purely mechanical changes, regenerated lockfiles, formatter-only diffs) must be declared explicitly in the gate's policy with a stated scope; silent exemption is a violation.

### Recovery
If a change merges without a comprehension signal: treat the resulting state as un-comprehended and require retroactive comprehension before any further change to the same surface area. If the signal turned out to be default-on or pro-forma (reviewer did not actually engage): retire the signal, escalate the gate (require structured prompt response), and re-comprehend. If the change is already in production and breaks: do not treat the post-incident comprehension as the recovery — the post-hoc understanding is a separate event and does not retroactively satisfy the pre-merge invariant.
