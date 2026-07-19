---
title: "Reuse-Before-Write Decision Ladder"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "seven-rung-minimal-code-decision-ladder"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "model-resilient-prompt-engineering.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "coding agents about to generate new code in response to a feature request or task"
    - "codebases where agents have previously reinvented existing components, standard-library functionality, or platform features instead of reusing them"
    - "teams trying to reduce both the token cost of code generation and the long-term maintenance surface of AI-authored code"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — a prompt/skill-level checklist; removing it costs nothing but forgoes the reuse discipline"
  auditability: "medium — a code-review or repo-audit pass can check whether new code duplicates something that already existed (standard library, platform feature, existing component), which is the checkable trace of ladder compliance; the agent's in-the-moment reasoning through the rungs is not directly observable"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Shipped as a Claude Code plugin's core mechanism; vendor-claimed large token/cost reductions are single-model (Haiku-class); one independent-ish cross-model replication measured a smaller but still material cost reduction and better-than-claimed results on a more capable model."
contract:
  preconditions: "A coding agent is about to generate new code in response to a request. The agent has access to the existing codebase, standard library documentation, platform feature documentation, and a mechanism to identify installable dependencies."
  invariants: "Before generating new code, the agent works through a fixed ordered checklist and stops at the first rung that resolves the need: (1) is this needed at all — could the request be satisfied by not building anything (YAGNI); (2) does equivalent functionality already exist in the codebase and can it be reused; (3) does a standard library cover it; (4) does a native platform feature cover it; (5) can an installed or installable dependency cover it; (6) can it be a one-line fix calling something that already exists; (7) only if none of the above apply, write minimal new code. The agent does not skip directly to writing new code without having worked through the earlier rungs."
  governance: "Owner: whoever maintains the coding agent's skill, prompt, or plugin definition for code-generation tasks. The ladder is prompt/skill content, not a build-time gate — it governs the reasoning path, not a separate approval step. Repo-wide audits (dead code, unused abstractions, hand-rolled reimplementations of standard-library functionality, single-implementation interfaces) can retroactively check for ladder violations across a codebase."
  recovery: "If the agent generates new code without evidence of working through the ladder → flag in review; ask whether an earlier rung (existing component, standard library, platform feature, dependency, one-line fix) would have sufficed, and refactor if so. If the YAGNI check (rung 1) is found to have silently dropped genuinely needed scope → the need-check judgment was delegated to the model incorrectly; add an explicit scope confirmation step rather than trusting the agent's YAGNI call unchecked. If aggressive reuse (rung 2) has coupled unrelated features to a shared component → decouple; reuse should not create unintended cross-feature dependencies. If a repo-wide simplification pass based on this ladder introduces regressions → treat the audit's findings as a proposal, not an automatic edit — verify each simplification against tests or a staged clone before merging."
tags:
  - "extracted-artifact"
  - "rule"
  - "prompt-craft"
  - "token-economy"
  - "code-generation"
---

# Reuse-Before-Write Decision Ladder

**Source:** [[seven-rung-minimal-code-decision-ladder]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A coding agent has received a request that could plausibly be satisfied by writing new code, and is about to begin generating it.

## Action

**Required:** Work through a fixed, ordered checklist before writing anything new, stopping at the first rung that resolves the need: (1) is this needed at all — YAGNI; (2) does it already exist in the codebase and can existing components be reused; (3) does a standard library cover it; (4) does a native platform feature cover it; (5) can an installed or installable dependency cover it; (6) can it be a one-line fix calling an existing function; (7) only then write minimal new code.

**Forbidden:** Jumping directly to writing new code without working through the earlier rungs. Treating the ladder as optional guidance rather than a required pre-generation step.

## Boundary

Enforced at the moment a coding agent is about to generate code — inside the code-generation skill or prompt, before any new file or function is written. Applies per generation task, not once per session.

## Enforcement

- **Mechanism:** The ladder is embedded as ordered checklist content in the code-generation skill or prompt. A retroactive repo-audit pass (dead code, unused abstractions, hand-rolled standard-library reimplementations, single-implementation interfaces/factories) can surface violations after the fact.
- **Check (deterministic):** No single field marks compliance at generation time. **Check (retroactive, pattern-level):** newly generated code that duplicates an existing component, standard-library function, or platform feature is a checkable violation signal in review or audit.
- **Violation response:** Refactor the new code to use the existing component, library, feature, dependency, or one-line fix that should have been found at an earlier rung.
- **Cannot be fully self-certified:** the agent's reasoning through the rungs is not directly observable; compliance is inferred from the absence of duplicated functionality in review or audit, not from an in-the-moment attestation.

## Rationale

The largest token savings in AI-assisted coding come from not writing code at all, not from writing terser code — a distinct mechanism from prose-brevity constraints. Every rung climbed instead of writing new code saves that code's tokens both at generation time and at every future read of the codebase, while also countering a known agentic failure mode: reinventing functionality that already exists rather than finding and reusing it. The ladder gives that instinct a fixed, ordered structure so the check happens consistently rather than depending on the model noticing reuse opportunities unprompted.

## Failure Modes

- **YAGNI over-reach.** The need-check (rung 1) is delegated to the model's judgment, and an agent can silently drop genuinely needed scope while believing it applied YAGNI correctly. Mitigation: treat rung-1 judgment calls as needing confirmation on non-trivial requests, not blind trust.
- **Reuse coupling.** Aggressively satisfying rung 2 by reusing an existing component can couple unrelated features to a shared piece of code, creating unintended cross-feature dependencies. Mitigation: weigh reuse against the coupling cost before committing to it.
- **Unverified repo-wide simplification.** Audit-driven simplification passes across a codebase carry real regression risk; the source practice itself does not trust unverified audit output. Mitigation: verify each simplification against tests or a staged clone before merging, rather than applying audit findings automatically.
- **Unreplicated vendor numbers.** Large headline token/cost reductions are reported by a single vendor on a single model class; treat them as directional, not guaranteed, until independently replicated on the model in use.

## Contract

### Preconditions
A coding agent is about to generate new code in response to a request. The agent has access to the existing codebase, standard library documentation, platform feature documentation, and a mechanism to identify installable dependencies.

### Invariants
Before generating new code, the agent works through a fixed ordered checklist and stops at the first rung that resolves the need: (1) is this needed at all — could the request be satisfied by not building anything (YAGNI); (2) does equivalent functionality already exist in the codebase and can it be reused; (3) does a standard library cover it; (4) does a native platform feature cover it; (5) can an installed or installable dependency cover it; (6) can it be a one-line fix calling something that already exists; (7) only if none of the above apply, write minimal new code. The agent does not skip directly to writing new code without having worked through the earlier rungs.

### Governance
Owner: whoever maintains the coding agent's skill, prompt, or plugin definition for code-generation tasks. The ladder is prompt/skill content, not a build-time gate — it governs the reasoning path, not a separate approval step. Repo-wide audits (dead code, unused abstractions, hand-rolled reimplementations of standard-library functionality, single-implementation interfaces) can retroactively check for ladder violations across a codebase.

### Recovery
If the agent generates new code without evidence of working through the ladder → flag in review; ask whether an earlier rung (existing component, standard library, platform feature, dependency, one-line fix) would have sufficed, and refactor if so. If the YAGNI check (rung 1) is found to have silently dropped genuinely needed scope → the need-check judgment was delegated to the model incorrectly; add an explicit scope confirmation step rather than trusting the agent's YAGNI call unchecked. If aggressive reuse (rung 2) has coupled unrelated features to a shared component → decouple; reuse should not create unintended cross-feature dependencies. If a repo-wide simplification pass based on this ladder introduces regressions → treat the audit's findings as a proposal, not an automatic edit — verify each simplification against tests or a staged clone before merging.
