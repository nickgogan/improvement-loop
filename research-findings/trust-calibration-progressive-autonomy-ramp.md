---
name: Trust Calibration via Progressive Autonomy Ramp
summary: Start agents with minimal autonomy and progressively expand permissions based on demonstrated reliability. Each successful execution builds trust, unlocking broader scope. The ramp is per-task-type,
  not global -- an agent trusted for documentation may not be trusted for infrastructure changes.
implementation_notes: MetaSystem's DD-29 human gate model is static. A progressive ramp could reduce review burden for proven task types.
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- agent-produces-100x-org-reviews-3x.md
- anthropic-trustworthy-agents-in-practice.md
related_findings:
- file: human-on-the-loop-hotl-autonomy-tiering-framework.md
  rel: extends
- file: autonomy-gradient-not-binary-delegation.md
  rel: extends
- file: agent-identity-governance-enforcement-layer.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- agent-governance-and-trust.md
---

# Trust Calibration via Progressive Autonomy Ramp

## What It Is
A governance pattern where agents start with minimal autonomy and earn expanded permissions through demonstrated reliability. Each successful execution of a task type builds trust, which unlocks broader scope for that specific task type. Critically, the trust ramp is per-task-type rather than global -- an agent trusted to write documentation is not automatically trusted to modify infrastructure.

## Why It Matters
Static permission models (always require human approval, or always allow autonomous execution) are both suboptimal. The former creates review bottlenecks for low-risk tasks; the latter creates risk exposure for high-stakes operations. A progressive ramp matches review effort to actual risk, freeing human attention for the decisions that genuinely need it.

## Why People Are Using It
Teams deploying agents at scale find that uniform review requirements are unsustainable. The progressive ramp lets them reduce review overhead for task types where the agent has proven reliable while maintaining strict gates for novel or high-risk operations. This directly addresses the 100x production / 3x review asymmetry.

## Potential Improvements
MetaSystem could implement a lightweight trust ledger that tracks success/failure rates per skill or task type. Once a threshold is reached (e.g., 20 consecutive successful research-loop runs), the human gate for that specific skill could shift from approval-required to spot-check.

## Potential Failure Modes
Trust calibration can create a false sense of security -- an agent reliable on routine tasks may fail catastrophically on edge cases within the same task type. The ramp also requires a reliable mechanism for detecting failures, which itself may be imperfect. Regression risk is real: an agent update could invalidate previously earned trust without the system detecting the change.

## Anthropic Confirmation (April 2026 — Tier 1)
Anthropic's "Trustworthy agents in practice" validates progressive autonomy through their training approach: on complex tasks, user interruptions rise slightly, but Claude's check-in rate doubles — demonstrating effective calibration where the model asks more when stakes are higher. Anthropic trains for this via scenarios simulating ambiguity, reinforcing pauses over assumptions. Claude's Constitution explicitly trains models to "raise concerns, seek clarification, or decline" rather than assume. This is production evidence that progressive autonomy calibration works at scale and can be trained into models, not just enforced by harnesses.
