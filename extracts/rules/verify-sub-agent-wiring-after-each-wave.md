---
title: "Verify Sub-Agent Wiring After Each Wave"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "orchestrated-execution-one-task-per-sub-agent-wit"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "orchestrators managing waves of parallel sub-agents that each produce code or configuration"
    - "any multi-agent build workflow where sub-agent outputs must integrate into a shared application"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "low — embedding the verification step into a wave-based workflow requires adding a checkpoint gate; removing it later means undetected integration failures may have accumulated"
  auditability: "high when wiring-verification output (connectivity check results, test runner output) is captured verbatim per wave; low when only a final pass/fail is retained"
  evidence_strength: "Strong (production-tested)"
  adoption:
    status: "Not Yet Started"
    notes: "Pattern documented from production wave-based orchestration workflows. Automated wiring tests (connectivity checks from application entry point) are the recommended enforcement mechanism but are not yet implemented in MetaSystem."
contract:
  preconditions: "A wave of sub-agents has completed. Each sub-agent was assigned exactly one implementation task. The main application has an identifiable entry point from which reachability can be tested. A connectivity or integration test is runnable against the current codebase state."
  invariants: "After every wave of sub-agents completes — before the next wave begins or before the session is closed — the orchestrator runs a connectivity or integration test from the application's entry point. Every module produced by the wave is verified to be reachable from that entry point. Any module that is not reachable is flagged as an isolated island and must be wired before the next wave is started."
  governance: "Owner: the orchestrator agent or the session manager (human or automated) responsible for the wave-based build workflow. The verification check must be a non-bypassable gate between waves. The orchestrator must surface the specific reachability evidence (not just a pass/fail assertion) in its working log. If the orchestrator cannot run the check itself, a human must perform it manually before the next wave is authorized."
  recovery: "If a module is found unreachable after a wave → do not start the next wave; dispatch a targeted wiring task to connect the isolated module before proceeding. If multiple modules are unreachable → fix them sequentially in dependency order before re-running verification. If the connectivity test itself is broken → fix the test harness before using it as a gate; do not skip the gate because the test is broken. If wiring failures have already accumulated across multiple unverified waves → audit all wave outputs systematically before resuming forward progress."
tags:
  - "extracted-artifact"
  - "rule"
  - "orchestration"
  - "multi-agent"
  - "integration"
  - "verification"
---

# Verify Sub-Agent Wiring After Each Wave

**Source:** [[orchestrated-execution-one-task-per-sub-agent-wit]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An orchestrated, wave-based build workflow has just completed a wave: one or more sub-agents have each finished their assigned implementation task and returned results. The orchestrator is about to start the next wave or close the session.

Scope: applies to all wave-based sub-agent workflows where sub-agent outputs are code or configuration that must integrate into a shared application. Does not apply to sub-agents producing purely standalone artifacts (reports, standalone scripts, isolated data) with no integration dependency.

## Action

**Required:** Before starting the next wave (or before closing the session after the final wave), run a connectivity or integration test from the application's entry point. Verify that every module produced in the completed wave is reachable from that entry point. Record the verification output (not just pass/fail — the specific reachability evidence) in the session log.

**Forbidden:**
- Starting the next wave without completing wiring verification for the previous wave.
- Accepting a sub-agent's self-report that its output "is wired" as a substitute for an independent connectivity check.
- Skipping the gate because the test harness is temporarily broken — fix the harness first.

## Boundary

Enforced at the transition point between waves. The rule fires at the end of each wave, not mid-wave. It applies until either:
- The verification check confirms all wave outputs are reachable from the entry point, or
- Isolated modules are identified, wiring tasks are dispatched, and a subsequent verification check passes.

## Enforcement

- **Mechanism:** The orchestrator must produce verification output (connectivity check log, integration test output, or equivalent) as an artifact in the session log before the next wave begins. Downstream review (human or automated post-wave hook) checks for this artifact.
- **Check (deterministic):** `(wiring_verification_run == true) AND (all_wave_outputs_reachable == true)`. Either branch false → wave boundary violation.
- **Violation response:**
  - *Isolated module detected:* halt wave progression; dispatch a targeted wiring task; re-run verification before proceeding.
  - *Verification skipped:* treat all subsequent work as unverified; audit all wave outputs before accepting any further progress.
  - *Test harness broken:* fix the harness; do not substitute manual assertion for the automated check unless the manual check produces the same reachability evidence.
- **Recommended automation:** Connectivity checks run from the application's entry point after each wave; CI/CD integration that blocks wave progression on failed reachability.

## Rationale

Isolated code islands are the most common failure pattern in wave-based sub-agent orchestration. Sub-agents reliably complete their assigned building task but frequently fail to connect their output to the rest of the application. Without an explicit gate, these failures accumulate silently across waves: each wave builds on the previous wave's unverified state, compounding integration debt. By the time the failure is discovered, it spans multiple waves and is expensive to diagnose.

The verification step must be explicit because sub-agents do not have visibility into the full application state. Each sub-agent's context contains only its assigned task and the relevant code — it cannot verify cross-module reachability. The orchestrator, which holds the build plan, is the only actor positioned to verify integration after each wave.

## Failure Modes

- **Wiring failure accumulated across multiple unverified waves.** If the rule is not applied and several waves run without verification, integration failures compound. The application may build successfully but fail to function end-to-end. Mitigation: retroactive wave audit to identify the first point of disconnection.
- **Connectivity test passes but integration is shallow.** A module is reachable from the entry point (passes the connectivity check) but its runtime behavior is broken. Mitigation: combine reachability checks with functional smoke tests after each wave.
- **Sub-agents writing conflicting implementations.** Two sub-agents in the same wave both modify a shared interface. Wiring verification detects the conflict only if the integration test exercises the shared interface. Mitigation: wave design should minimize shared-interface overlap; the orchestrator's build plan is the single source of truth for interface ownership.
- **Orchestrator bypasses the gate to meet a deadline.** Under time pressure, the gate is skipped with an intention to "verify later." Mitigation: treat the gate as non-negotiable; the cost of a skipped gate compounds with each subsequent wave.

## Contract

### Preconditions
A wave of sub-agents has completed. Each sub-agent was assigned exactly one implementation task. The main application has an identifiable entry point from which reachability can be tested. A connectivity or integration test is runnable against the current codebase state.

### Invariants
After every wave of sub-agents completes — before the next wave begins or before the session is closed — the orchestrator runs a connectivity or integration test from the application's entry point. Every module produced by the wave is verified to be reachable from that entry point. Any module that is not reachable is flagged as an isolated island and must be wired before the next wave is started.

### Governance
Owner: the orchestrator agent or the session manager (human or automated) responsible for the wave-based build workflow. The verification check must be a non-bypassable gate between waves. The orchestrator must surface the specific reachability evidence (not just a pass/fail assertion) in its working log. If the orchestrator cannot run the check itself, a human must perform it manually before the next wave is authorized.

### Recovery
If a module is found unreachable after a wave → do not start the next wave; dispatch a targeted wiring task to connect the isolated module before proceeding. If multiple modules are unreachable → fix them sequentially in dependency order before re-running verification. If the connectivity test itself is broken → fix the test harness before using it as a gate; do not skip the gate because the test is broken. If wiring failures have already accumulated across multiple unverified waves → audit all wave outputs systematically before resuming forward progress.
