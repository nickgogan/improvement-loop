---
name: 'Harness Adaptation Protocol — Graded Capability Intersection with Human-Gated Install'
summary: 'A step-ordered protocol for installing an agentic system onto a harness with no pre-staged adapter: the receiving agent parses the system contract, grades its own platform''s provides (native / partial / absent) per capability ID, computes the intersection against the wiring rows (required unsatisfied → explicit refusal naming what would satisfy it; optional unsatisfied → apply the named degradation and record it), proposes a per-row adaptation plan the human approves step-by-step, executes, writes an install report, then verifies with a layered stack: cold-start echo, per-skill trigger evals, per-row invariant probes, and per-skill behavioral smokes.'
implementation_notes: 'This is the operating manual for the engine''s portable-governance-kernel goal: when the kernel moves to a new harness (or is handed to a builder-friend), this protocol shape — inventory, intersection, human-gated plan, install report, invariant probes — is what "install" means. Key design moves to steal: missing context is elicited from the human as a typed request list, never fabricated; required-row failure is a refusal that names the missing capability; version pinning (contract + skill versions) enables later drift detection; failure routing distinguishes port-side defects from upstream skill defects.'
category: Agentic Systems
evidence_strength: Medium (practitioner-documented, single production system; protocol design research-cited to MCP/A2A/MCPB semantics)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-wiring-canon.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: raw
consumed_by: []
tags:
- adaptation-protocol
- capability-grading
- install-verification
- portability
- conformance-testing
---
# Harness Adaptation Protocol — Graded Capability Intersection with Human-Gated Install

## What It Is

A seven-step protocol addressed to "you, the agent on the target platform" receiving an
installable agentic system with only the repository and its system contract: (1) read
the contract, (2) inventory your platform's provides, (3) compute the intersection,
(4) propose an adaptation plan — human gate, (5) execute and write an install report,
(6) verify triggering via cold-start echo + skill trigger evals, (7) verify behavior via
invariant probes + skill smokes. Its design is explicitly research-cited: intersection
semantics from the MCP `initialize` handshake and A2A's required/optional extension
rules; typed human-input elicitation from MCPB `user_config`; declare-and-adapt (no live
negotiation); version pinning per lock-file discipline.

## Why It Matters

Plain English: "install my agent system on your setup" usually means a human reading
docs and improvising. This protocol makes the *receiving agent* do the port under
contract semantics — with honest capability grading, explicit refusal when a hard
requirement is unmet, a human approving each step, and a verification stack that tests
what actually composed. It is the difference between hoping a port worked and having
per-invariant evidence that it did. For any portable kernel, this defines done.

## How It Works

- **Grading scale:** for every capability ID in the wiring rows and skill sidecars,
  grade the platform `native` (name the mechanism) / `partial` (describe the gap) /
  `absent`. "Grade honestly; a flattering inventory produces a broken install."
- **Intersection semantics:** required row unsatisfied → stop for that unit with an
  explicit refusal naming exactly what would satisfy it (e.g. "no unconditional
  instruction-injection point — provide one and re-run"); no workaround without the
  human accepting the risk in writing. Optional row unsatisfied → apply the row's
  degradation exactly as written and record it. Required skill capability unsatisfied →
  do not install that skill; record why. Platform exceeds the source → guards may be
  *upgraded* to enforcement (recorded), never weakened.
- **Typed elicitation:** inputs only the human can supply (active user-id, always-on
  file location, memory mounts) are requested as a typed list — name, why needed, shape
  of answer, required/optional. "Never guess these"; fabrication is a contract
  stop-rule.
- **Per-step human gate:** the plan states, per wiring row and per skill, the mechanism,
  grade, degradation/upgrade, and *how the row's invariant is preserved* — the invariant
  is the acceptance test; the mechanism may be anything, the invariant may not bend.
  The human approves per step, not as one blanket yes.
- **Install report:** mechanism/grade/invariant statement per row; installed or
  not-with-reason per skill; the list of prose-only guards on this platform; pinned
  contract and skill versions for later drift detection.
- **Verification stack:** cold-start echo (fresh session states purpose, active
  pointer, next unit of work, live-vs-degraded rows); trigger evals self-administered
  per skill (persistent mismatch = fix the description mapping, never edit queries to
  match behavior); one binary invariant probe per wiring row — *the row's invariant is
  the probe spec* — plus a behavioral smoke per skill (fictional-specific task, grader
  separate from drafter). Failure routing: failed row probe → mechanism problem, back
  to the plan; smoke fails here but passes on source → port-side; fails on source too →
  skill defect, report upstream, do not patch locally.
- Probes are point-in-time evidence, not standing enforcement — that residual gap stays
  declared in the contract's absences.

## How It Could Fail

The protocol's weight is only justified when installs recur — for a one-off port it can
be run as a checklist rather than built as tooling. Its honesty depends on the grader
and installer being the same agent with an incentive to ship; the per-step human gate
and the source-side smoke baseline are the counterweights. Declared-but-unread trust
sections reproduce the enforcement-assumption failure the contract exists to prevent.
