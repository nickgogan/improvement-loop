---
title: "Harness Adaptation Install Protocol"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "harness-adaptation-protocol-graded-capability-intersection"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "building-agentic-systems.harvest-queue"
identification_report: "building-agentic-systems.harvest-queue.md::harness-adaptation-protocol-graded-capability-intersection::skill::harness-adaptation-install-protocol"
deployed: false
deployed_to: null
context:
  applies_to:
    - "installing a portable agent system onto a new platform or runtime that ships with no pre-built adapter"
    - "handing an agentic toolkit to another team whose harness provides a different capability set"
    - "porting a governance or skill kernel across coding-agent platforms while preserving its guarantees"
    - "any receiving agent that must decide whether it can host a contract-specified system, and how to adapt, degrade, or refuse per capability"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "build"
  reversibility: "medium — install adapts platform wiring and adds skills; rollback is possible because the install report records mechanism, grade, and invariant per row, but backing out means undoing each adaptation in turn"
  auditability: "high — the install report records mechanism/grade/invariant per wiring row and pins contract and skill versions, and each row's invariant becomes a binary probe, so post-install compliance is externally checkable against the report plus the probe and smoke results"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented in one production agentic system's install path; protocol semantics drawn from established agent-interop handshakes (capability negotiation, typed user-config, version pinning). No independent adoptions recorded."
contract:
  preconditions: "An installable system exists as a repository plus a machine-readable system contract whose wiring rows name capability IDs, a required/optional tier, a per-row invariant, and (for optional rows) a named degradation. The receiving agent can introspect its own platform's capabilities and surface them for grading. A human approver is available to gate each adaptation step. Inputs only a human can supply (active user identity, always-on file locations, memory mounts) are obtainable via a typed request list."
  invariants: "Every capability ID is graded honestly as native / partial / absent — a flattering inventory is a contract violation, not a shortcut. A required row that is unsatisfied halts that unit with an explicit refusal naming exactly what would satisfy it; no workaround is applied without the human accepting the risk in writing. An optional row that is unsatisfied applies its named degradation exactly as written and records it. Each wiring row's invariant is preserved under whatever mechanism is chosen — the mechanism may be anything the platform offers; the invariant may not bend. Human-only inputs are elicited as a typed list, never fabricated. Contract and skill versions are pinned in the install report for later drift detection."
  governance: "The human approver owns the per-step gate; the receiving agent proposes and executes but cannot self-approve. The system contract's author owns the invariants and degradations — the receiving platform may upgrade a guard to enforcement (recorded) but never weaken one. Behavioral-smoke failures that also fail on the source system are upstream skill defects: report them, do not patch locally. Residual capability gaps stay declared in the contract's absences; point-in-time probes are evidence, not standing enforcement."
  recovery: "Required-row failure → refuse and name exactly what would satisfy the row; do not proceed for that unit without written human acceptance of the risk. Trigger-eval mismatch that persists → fix the skill's description mapping, never edit the eval queries to match observed behavior. Invariant-probe failure → treat as a mechanism problem and return to the adaptation plan. Behavioral smoke fails on the target but passes on the source → port-side defect; re-adapt. Smoke fails on the source too → upstream skill defect; report it and do not patch locally."
tags:
  - "extracted-artifact"
  - "skill"
  - "adaptation-protocol"
  - "capability-grading"
  - "install-verification"
  - "portability"
---

# Harness Adaptation Install Protocol

**Source:** [[harness-adaptation-protocol-graded-capability-intersection]]
**Form:** skill
**Extraction date:** 2026-07-19

## Purpose

A step-ordered protocol addressed to the receiving agent — "you, the agent on the target platform" — for installing an agentic system onto a harness that has no pre-staged adapter. The agent parses the system's machine-readable contract, grades its own platform's provides per capability, computes the intersection against the contract's wiring rows, proposes a per-step adaptation plan the human approves, executes and writes an install report, then verifies the result with a layered stack. It turns "install my agent system on your setup" from a human reading docs and improvising into a contract-driven port with honest capability grading, explicit refusal on unmet hard requirements, per-step human approval, and per-invariant verification evidence. For any portable kernel, this protocol defines what "done" means.

## Inputs

- The installable system's **repository** — skills, wiring, and per-skill capability sidecars.
- The system's **machine-readable contract** — wiring rows carrying capability IDs, a required/optional tier, a per-row invariant, and (for optional rows) a named degradation.
- The receiving agent's **own platform**, whose capabilities the agent can introspect and name.
- A **human approver** available to gate each adaptation step.
- **Typed elicitation answers** for inputs only the human can supply (active user identity, always-on file locations, memory mounts).

## Outputs

- A **graded capability inventory** — native / partial / absent per capability ID.
- A **per-row adaptation plan** — mechanism, grade, degradation or upgrade, and an explicit statement of how the row's invariant is preserved.
- An **install report** — mechanism/grade/invariant per row; installed-or-not-with-reason per skill; the list of prose-only guards on this platform; pinned contract and skill versions.
- **Verification evidence** — cold-start echo, per-skill trigger evals, per-row invariant probes, per-skill behavioral smokes.
- **Explicit refusals** for any unsatisfied required row, each naming exactly what would satisfy it.

## Steps

1. **Read the contract.** Parse the system contract and the per-skill sidecars; enumerate every capability ID the system requires or optionally uses.
2. **Inventory your platform's provides.** For every capability ID, grade the platform `native` (name the mechanism), `partial` (describe the gap), or `absent`. Grade honestly — a flattering inventory produces a broken install.
3. **Compute the intersection.** For each wiring row: a *required* row unsatisfied → stop for that unit with an explicit refusal naming exactly what would satisfy it (no workaround without the human accepting the risk in writing). An *optional* row unsatisfied → apply the row's named degradation exactly as written and record it. A required *skill* capability unsatisfied → do not install that skill; record why. Where the platform exceeds the source, a guard may be *upgraded* to enforcement (recorded) — never weakened.
4. **Propose an adaptation plan — human gate.** State, per wiring row and per skill: the mechanism, the grade, the degradation or upgrade, and *how the row's invariant is preserved* (the invariant is the acceptance test). Elicit human-only inputs as a typed request list — name, why needed, shape of answer, required/optional; never guess these. The human approves per step, not as one blanket yes.
5. **Execute and write the install report.** Perform the approved adaptations. Record mechanism/grade/invariant per row, installed-or-not-with-reason per skill, the prose-only guard list, and pinned contract and skill versions for later drift detection.
6. **Verify triggering.** Run a cold-start echo (a fresh session states purpose, the active pointer, the next unit of work, and which rows are live vs. degraded) and self-administer per-skill trigger evals. A persistent trigger mismatch means fix the skill's description mapping — never edit queries to match behavior.
7. **Verify behavior.** Run one binary invariant probe per wiring row (the row's invariant *is* the probe spec) plus a behavioral smoke per skill (fictional-specific task, grader separate from drafter). Route failures: a failed row probe → mechanism problem, back to the plan; a smoke that fails here but passes on the source → port-side defect; a smoke that fails on the source too → upstream skill defect, report it and do not patch locally.

## Failure Modes

- **Flattering inventory → broken install.** The protocol's honesty depends on the grader and installer being the same agent with an incentive to ship. The per-step human gate and the source-side smoke baseline are the counterweights.
- **One-off port over-engineered.** The protocol's weight is only justified when installs recur; for a single port, run it as a checklist rather than building it as tooling.
- **Declared-but-unread trust sections.** Skipping the parts of the contract meant to be read reproduces the enforcement-assumption failure the contract exists to prevent.
- **Probes mistaken for standing enforcement.** Invariant probes and smokes are point-in-time evidence, not continuous guards — the residual gap stays declared in the contract's absences.
- **Fabricated human-only inputs.** Guessing an active user identity or memory mount instead of eliciting it is a contract stop-rule, not a convenience.

## Contract

### Preconditions
An installable system exists as a repository plus a machine-readable system contract whose wiring rows name capability IDs, a required/optional tier, a per-row invariant, and (for optional rows) a named degradation. The receiving agent can introspect its own platform's capabilities and surface them for grading. A human approver is available to gate each adaptation step. Inputs only a human can supply (active user identity, always-on file locations, memory mounts) are obtainable via a typed request list.

### Invariants
Every capability ID is graded honestly as native / partial / absent — a flattering inventory is a contract violation, not a shortcut. A required row that is unsatisfied halts that unit with an explicit refusal naming exactly what would satisfy it; no workaround is applied without the human accepting the risk in writing. An optional row that is unsatisfied applies its named degradation exactly as written and records it. Each wiring row's invariant is preserved under whatever mechanism is chosen — the mechanism may be anything the platform offers; the invariant may not bend. Human-only inputs are elicited as a typed list, never fabricated. Contract and skill versions are pinned in the install report for later drift detection.

### Governance
The human approver owns the per-step gate; the receiving agent proposes and executes but cannot self-approve. The system contract's author owns the invariants and degradations — the receiving platform may upgrade a guard to enforcement (recorded) but never weaken one. Behavioral-smoke failures that also fail on the source system are upstream skill defects: report them, do not patch locally. Residual capability gaps stay declared in the contract's absences; point-in-time probes are evidence, not standing enforcement.

### Recovery
Required-row failure → refuse and name exactly what would satisfy the row; do not proceed for that unit without written human acceptance of the risk. Trigger-eval mismatch that persists → fix the skill's description mapping, never edit the eval queries to match observed behavior. Invariant-probe failure → treat as a mechanism problem and return to the adaptation plan. Behavioral smoke fails on the target but passes on the source → port-side defect; re-adapt. Smoke fails on the source too → upstream skill defect; report it and do not patch locally.
