---
title: "Log-Based Cost Accounting Over Harness Readouts"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "harness-cost-readout-unreliability-independent-log-accounting"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "verifying-agent-output.harvest-queue"
identification_report: "verifying-agent-output.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "any process that records, reports, or reasons about the cost of an AI-agent run on a subscription-billed harness"
    - "telemetry capture pipelines that log cost or token usage for later analysis or routing decisions"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — swapping the accounting source is a measurement-method change with no artifact migration cost"
  auditability: "high — log-derived tools compute from local logs and are independently reproducible; a harness's self-reported figure is a black box the operator cannot re-derive"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "A subscription-plan or otherwise abstracted-billing harness (an agentic coding CLI or similar) displays its own cost or usage figures, and that figure is about to be recorded, cited, or used to drive a decision (routing, budgeting, model comparison, reporting)."
  invariants: "Any cost claim that enters a record, report, or decision is derived from an independent log-based accounting source (a local-log usage tool, or pure API metering via a gateway) rather than solely from the harness's self-reported display. If the harness's own readout and the independent log-based figure disagree, both are treated as suspect rather than either being trusted outright."
  governance: "Owner: whoever authors telemetry capture, cost reporting, or model-routing logic that consumes cost figures. Cost fields derived from harness self-report only must be explicitly marked as an estimate, never presented as an authoritative figure."
  recovery: "If no log-based tool exists for a given harness, mark the resulting cost field as 'estimated' or 'unverified' rather than treating the harness readout as ground truth. If a divergence between the harness readout and the log-based figure is discovered after a cost claim has already driven a decision, flag that decision for review rather than silently overwriting the number."
tags:
  - "extracted-artifact"
  - "rule"
  - "measurement-provenance"
  - "cost-accounting"
---

# Log-Based Cost Accounting Over Harness Readouts

**Source:** [[harness-cost-readout-unreliability-independent-log-accounting]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A cost or usage figure produced by a subscription-plan (or otherwise abstracted-billing) harness's own display is about to be recorded in a log, report, or the knowledge base, or used to drive a routing, budgeting, or comparison decision.

## Action

**Required:** Derive the cost claim from an independent, log-based accounting source — a tool that computes usage from local session logs, or pure API metering through a gateway — rather than the harness's self-reported cost surface. Mark any cost field sourced from harness self-report only as an estimate, not an authoritative number. Treat disagreement between a harness's own readout and the log-based figure as a signal to distrust both, not a tie-break in favor of either.

**Forbidden:** Citing a harness's `/cost`, `/usage`, or equivalent display as an authoritative cost figure in a report, comparison, or decision without corroborating it against a log-based source when one exists.

## Boundary

Enforced wherever cost or token figures are captured for telemetry, reported in comparisons or KB entries, or consumed by routing/budgeting logic. Applies specifically to subscription-plan or abstracted-billing contexts; pure API metering through a gateway is itself already a log-based source and satisfies the rule directly.

## Enforcement

- **Mechanism:** Telemetry capture or reporting code paths that touch a cost field must cite their source (log-derived tool vs. harness self-report) alongside the number.
- **Check (deterministic):** any persisted or reported cost field either (a) traces to a log-based accounting source, or (b) is explicitly tagged as an estimate derived from harness self-report.
- **Violation response:** an untagged cost figure sourced only from harness self-report is treated as unverified; retag it as an estimate or replace it with the log-derived figure before it is used in a decision.

## Rationale

On subscription plans, a harness's own cost display is a UI feature layered over billing abstraction, not an accounting system — it can disagree with itself between two surfaces on the same session, or omit a cost line entirely. Since cost numbers drive routing decisions, plan-vs-API tradeoffs, and budget claims that enter the knowledge base as evidence, an unreliable measurement instrument silently propagates its error into every downstream decision. Preferring log-based, independently reproducible accounting removes the harness's display from the trust chain.

## Failure Modes

- **Log tools drift with harness log formats.** Log-derived accounting tools break silently when the harness changes its internal log schema between versions — treat a sudden zero or missing figure from the log tool as a possible tool-drift signal, not confirmation of zero cost.
- **Subscription-plan accounting is inherently notional.** Even a correct token count converted to "what this would cost via API" is a modeled number, not a billed one, on a flat-rate subscription — label it accordingly.
- **Single-instance evidence.** The specific discrepancy pattern this rule is grounded in is one practitioner's observation on one harness version pair; treat any given harness/version combination's reliability as unverified until checked, not assumed broken or assumed fine.

## Contract

### Preconditions
A subscription-plan or otherwise abstracted-billing harness (an agentic coding CLI or similar) displays its own cost or usage figures, and that figure is about to be recorded, cited, or used to drive a decision (routing, budgeting, model comparison, reporting).

### Invariants
Any cost claim that enters a record, report, or decision is derived from an independent log-based accounting source (a local-log usage tool, or pure API metering via a gateway) rather than solely from the harness's self-reported display. If the harness's own readout and the independent log-based figure disagree, both are treated as suspect rather than either being trusted outright.

### Governance
Owner: whoever authors telemetry capture, cost reporting, or model-routing logic that consumes cost figures. Cost fields derived from harness self-report only must be explicitly marked as an estimate, never presented as an authoritative figure.

### Recovery
If no log-based tool exists for a given harness, mark the resulting cost field as "estimated" or "unverified" rather than treating the harness readout as ground truth. If a divergence between the harness readout and the log-based figure is discovered after a cost claim has already driven a decision, flag that decision for review rather than silently overwriting the number.
