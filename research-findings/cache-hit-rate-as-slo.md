---
name: "Cache Hit Rate as an SLO with SEV-Grade Alerting"
summary: |-
  The Claude Code team monitors prompt-cache hit rate like uptime — alerts fire on low hit
  rates and the team declares SEVs when they drop, treating a cache regression as an incident
  equal in severity to an outage. For us the transferable idea is that cache breakage is a
  silent, unmonitored failure mode by default: everything still works, it just quietly costs
  multiples more. Making hit rate an observed number is what makes all the other prefix
  disciplines enforceable.
implementation_notes: null
category: "Agentic Systems"
evidence_strength: "Strong (production-tested, first-party)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "claude-code-prompt-caching-is-everything.md"
related_findings: []
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

## What It Is

An operational stance from the Claude Code team: prompt-cache hit rate is a Service Level Objective. The team runs continuous alerting on hit rates and "declare[s] SEVs if they're too low," handling a cache-break incident with the same process weight as a system outage. The rationale is economic: cache efficiency is a direct cost and latency multiplier, and at Claude Code's scale high hit rates are what fund "more generous rate limits" for subscription plans.

## Why It Matters

Cache regressions are the canonical silent failure: a stray timestamp in a system prompt or a non-deterministically ordered tool list produces no error, no test failure, and no user-visible bug — just a step-function increase in cost and latency. Without a monitored metric, every prefix-stability discipline (append-only updates, static tool sets, cache-safe compaction) erodes unnoticed as the codebase evolves. The SLO closes the loop: the disciplines are the mechanism, the hit-rate alert is the enforcement.

## Why People Are Using It

First-party production practice on a product where inference cost dominates unit economics. The post frames it as the difference between treating caching as an optimization and treating it as infrastructure.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Periodic cost review | Notice regressions in monthly spend | Low-volume usage where an alert pipeline isn't worth building |
| Per-release cache tests | Assert prefix stability in CI instead of production monitoring | Teams without production telemetry access |
| No monitoring | Rely on discipline alone | Prototypes; accept silent drift |

## Potential Improvements

- For our scale: a lightweight equivalent is periodically inspecting cache-read vs input token counts in API/usage telemetry rather than a full alerting stack
- Pair with a prefix-stability checklist in code review for harness-touching changes

## Potential Failure Modes

- **Metric without ownership:** an alert nobody triages is monitoring theater
- **Over-rotation at small scale:** SEV-grade process for a single-user harness costs more than the cache misses it prevents
- **Aggregate masking:** a healthy global hit rate can hide a fully-broken cache path in one low-traffic feature
