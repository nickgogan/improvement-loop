---
title: "Knowledge Capture Must Be a Byproduct of Work, Not a Separate Act"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "signal-capture-as-byproduct-of-work"
identification_report: "building-agentic-systems.harvest-queue.md::signal-capture-as-byproduct-of-work::rule::capture-must-be-byproduct-of-work"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
    - "ingestion-pattern selection for any organizational knowledge system or agentic world model"
    - "tool/workflow choices where signal must accumulate over time (decision logs, session memory, post-mortems, briefings, ticket systems)"
    - "agentic systems whose long-term value depends on compounding context"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "moderate — adopting an active-documentation pattern is recoverable by replacing the path with a passive-capture pattern, but accumulated gaps in historical signal cannot be retroactively filled"
  auditability: "high when each capture path is named in a spec and classified byproduct/separate-act; low when ingestion choices are implicit in tool selection"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Surfaced as one of five principles for building world models that compound; practitioner-documented but not yet applied to MetaSystem ingestion patterns at extraction time."
contract:
  preconditions: "A knowledge system, world model, or agentic system is being designed (or modified) and a new ingestion path is being specified — i.e., a tool, workflow, or behavior that is supposed to feed signal into the system over time. The path has at least one human contributor whose context is the target signal."
  invariants: "Every named ingestion path produces signal as a natural byproduct of doing the work. No ingestion path requires a separate documentation act distinct from the work itself. For each path, the byproduct/separate-act classification is recorded in the spec at design time and re-checked when the path is modified."
  governance: "Owner: any skill, agent, CLAUDE.md section, or system spec that introduces or modifies an ingestion path. The byproduct/separate-act classification must appear in the spec and survive review. Specs proposing separate-act capture must explicitly justify the choice and accept the documented failure modes (strategic withholding, benign forgetfulness)."
  recovery: "If a deployed ingestion path is found to require separate-act capture and signal is not accumulating → redesign the path so the work itself produces the signal (commit messages over docs, ticket updates over status emails, in-system decisions over pasted-in summaries), or replace the path. If passive capture is producing low-signal noise at high volume → add a filter/digest layer downstream; do not revert to active documentation. If incentives are missing (contributors see no personal advantage to feeding the system) → address the incentive layer; do not assume technical fixes alone will close the gap."
tags:
  - "extracted-artifact"
  - "rule"
  - "knowledge-systems"
  - "ingestion"
  - "agentic-systems"
  - "world-model"
  - "compounding"
---

# Knowledge Capture Must Be a Byproduct of Work, Not a Separate Act

**Source:** [[signal-capture-as-byproduct-of-work]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A knowledge system, world model, or agentic system is being designed (or modified) and a new ingestion path is being specified — i.e., a tool, workflow, or behavior intended to feed signal into the system over time. At least one human contributor's context is the target signal.

Scope of application: any ingestion-pattern adoption decision for systems whose long-term value depends on compounding context (decision logs, session memory, post-mortems, briefings, ticket systems, agent world models).

## Action

**Required:** Design each ingestion path so that doing the work itself produces the signal. The act of working — committing code, updating a ticket, recording a decision in the system, sending a message in the canonical channel — must be the same act that feeds the model. For every named path, classify it byproduct vs. separate-act in the spec at design time, and re-check on modification.

**Forbidden:** Specifying or deploying ingestion paths that require a separate documentation effort distinct from the work itself (e.g., post-hoc status reports, parallel doc-writing sessions, "feed the model" as its own ritual). Treating active documentation as an acceptable default. Leaving the byproduct/separate-act classification implicit or undocumented.

## Boundary

Enforced at the design-time choice gate for every ingestion path. Applies from the moment a path is proposed (in a spec, skill, agent, CLAUDE.md, or workflow doc) until either:
- the path is classified byproduct and approved, *or*
- the path is classified separate-act, justified explicitly, and the documented failure modes are accepted in writing.

Does not govern read paths, downstream filters, or post-ingestion processing — those are separate concerns. Does not retroactively forbid existing separate-act paths; it governs new paths and modifications.

## Enforcement

- **Mechanism:** Every spec or workflow doc introducing an ingestion path includes a one-line classification: `capture_mode: byproduct` or `capture_mode: separate-act` (with justification). The choice gate question — *"is this a byproduct of work, or a separate act?"* — appears in the spec template for any tool or workflow whose purpose includes feeding signal into a model.
- **Check (deterministic):** `(path_classified == true) AND (classification == "byproduct" OR (classification == "separate-act" AND justification_present == true))`. Any branch false → violation.
- **Violation response:**
  - *Unclassified path:* spec is rejected at review; classification must be added before approval.
  - *Separate-act without justification:* spec is rejected; either redesign as byproduct or document why separate-act is necessary and which failure modes are accepted.
  - *Deployed separate-act path with thin signal:* trigger redesign — replace with a byproduct alternative, not a stricter documentation policy.
- **Cannot be self-certified at runtime:** Ideally enforced by a review-time gate (skill assessment, spec review, design decision intake) since the failure surfaces as missing signal, which is hard to detect from within the system once deployed.

## Rationale

Organizational knowledge systems only compound if signal feeds them over time. Ingestion paths that require a separate documentation act fail in two compounding ways:

1. **Strategic withholding.** Contributors with the most valuable context — those whose information is load-bearing — have the strongest incentive to retain that information advantage. They will not voluntarily feed a system that erodes it.
2. **Benign forgetfulness.** Even non-strategic contributors skip documentation under time pressure. Back-channel conversations route around the system, keeping critical context in heads.

The result is asymmetric population: knowledge systems fill with low-stakes, easy-to-document material and miss the judgment-rich context that would make them useful. The absence of signal looks like "no signal" rather than "missing signal," which is undetectable from within the model.

Passive capture closes the gap by removing the choice. If using the tool to do the work also produces the record, contributors do not opt in or out — they just work. This is the human-side analogue of the technical signal-fidelity problem: even with perfect technical architecture, a knowledge system is only as good as the organizational behaviors that feed it.

This rule is the positive-space invariant. Rather than enumerating failure modes (every kind of skipped documentation), it states the bounded check: every ingestion path is a byproduct, or it is justified and its failures are accepted.

## Failure Modes

- **Passive-capture noise.** Byproduct capture can produce low-signal noise at high volume (every commit message, every Slack thread). Mitigation: design downstream filtering or digest layers; do not respond by reverting to active documentation.
- **Tool lock-in.** Optimizing one tool stack for byproduct capture makes migration painful. Mitigation: prefer canonical, exportable formats (markdown, structured logs, plain commit messages) over vendor-proprietary capture surfaces.
- **Privacy / compliance.** Automatic capture of work conversations may be inappropriate in regulated domains. Mitigation: scope automatic capture to artifacts the contributor would author publicly anyway; require explicit opt-in for ambient capture.
- **Skewed coverage.** If only some kinds of work are naturally logged (e.g., code commits) but others are not (architecture discussions, judgment calls), the model accumulates a distorted picture. Mitigation: audit which work types feed the model; design byproduct paths for the missing ones rather than backfilling with separate-act capture.
- **Missing incentive layer.** Even with byproduct capture, contributors need to perceive personal advantage to feeding the model. Pure technical solutions without an incentive story underperform. Mitigation: pair the rule with an incentive design — make the model visibly useful to the people feeding it, not just to whoever consumes the outputs.

## Contract

### Preconditions
A knowledge system, world model, or agentic system is being designed (or modified) and a new ingestion path is being specified — i.e., a tool, workflow, or behavior that is supposed to feed signal into the system over time. The path has at least one human contributor whose context is the target signal.

### Invariants
Every named ingestion path produces signal as a natural byproduct of doing the work. No ingestion path requires a separate documentation act distinct from the work itself. For each path, the byproduct/separate-act classification is recorded in the spec at design time and re-checked when the path is modified.

### Governance
Owner: any skill, agent, CLAUDE.md section, or system spec that introduces or modifies an ingestion path. The byproduct/separate-act classification must appear in the spec and survive review. Specs proposing separate-act capture must explicitly justify the choice and accept the documented failure modes (strategic withholding, benign forgetfulness).

### Recovery
If a deployed ingestion path is found to require separate-act capture and signal is not accumulating → redesign the path so the work itself produces the signal (commit messages over docs, ticket updates over status emails, in-system decisions over pasted-in summaries), or replace the path. If passive capture is producing low-signal noise at high volume → add a filter/digest layer downstream; do not revert to active documentation. If incentives are missing (contributors see no personal advantage to feeding the system) → address the incentive layer; do not assume technical fixes alone will close the gap.
