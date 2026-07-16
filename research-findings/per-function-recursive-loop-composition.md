---
name: Per-Function Recursive Loop Composition
summary: 'Treat every organizational function (product, support, engineering, sales) as its own independent self-improving recursive AI loop, each running the same five-layer architecture (sensor → policy
  → tool → quality gate → learning). The company becomes N parallel loops that independently optimize their domain. This is a composition pattern: the same loop template instantiated per function, not one
  global loop.'
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- self-improving-company-yc-five-layer-loop.md
related_findings:
- file: five-layer-recursive-ai-loop-architecture.md
  rel: extends
- file: cross-domain-transfer-of-meta-improvements.md
  rel: same-problem
- file: time-window-proactive-agent-loop.md
  rel: same-problem
- file: agent-sprawl-anti-pattern-microservices-redux.md
  rel: contradicts
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
tags:
- session-95-reextract
---

# Per-Function Recursive Loop Composition

## What It Is

A composition pattern where the five-layer recursive AI loop architecture is instantiated once per organizational function, creating N parallel self-improving loops that operate independently:

**Product optimization loop:**
- Sensor: product analytics, funnel metrics
- Policy: what experiments to run, what thresholds trigger action
- Tool: A/B testing framework, deployment APIs
- Quality gate: statistical significance checks, user impact bounds
- Learning: pick best version, deploy, repeat

**Customer service loop:**
- Sensor: customer suggestions, support tickets
- Policy: alignment with roadmap, cost/benefit thresholds for implementation
- Tool: code generation, deployment, customer notification
- Quality gate: "CPO/CTO agent" that triages suggestions (discard, defer, implement)
- Learning: customer satisfaction feedback after deployment

**Engineering improvement loop:**
- Sensor: failed queries, error logs, performance metrics
- Policy: what constitutes a "failure," what fixes are safe to auto-deploy
- Tool: code generation, PR creation, database operations
- Quality gate: agent code review, test suites
- Learning: track fix success rate, refine diagnostic accuracy

Each loop runs the same structural template but with domain-specific sensors, policies, tools, and quality criteria. The loops are independent — one function's loop failing doesn't block another's improvement.

## Why It Matters

A single global self-improvement loop creates a bottleneck: one system trying to improve everything at once, with competing priorities and shared resources. Per-function decomposition allows each domain to optimize at its own pace, with its own metrics, and its own failure tolerance. It also maps cleanly to organizational ownership — each function's loop can have its own DRI.

For MetaSystem: the IL currently has one pipeline (research → extraction → synthesis → deployment). This pattern suggests considering parallel pipelines per concern — one loop for skill quality improvement, one for governance drift detection, one for knowledge freshness. Each could run independently on its own cadence.

## Why People Are Using It

Described by YC group partner as the architectural vision for startups (2026). Explicit examples given for product, customer service, and engineering functions. Framed as the replacement for hierarchically organized companies.

## Potential Improvements

- Add cross-loop learning: improvements discovered in one function's loop may apply to others (meta-learning across loops).
- Shared policy layer: certain policies (safety, ethics, brand) should apply across all loops, enforced centrally.
- Loop health monitoring: a meta-loop that monitors whether individual function loops are actually improving.

## Potential Failure Modes

- Per-function loops can optimize locally while creating global incoherence (product loop ships features that support loop can't handle).
- Without cross-loop coordination, different functions may make conflicting changes to shared resources (databases, APIs, customer-facing systems).
- Proliferation of loops increases total system complexity and monitoring burden — the "agent sprawl" anti-pattern applied to improvement loops.
- Each loop needs its own quality gate calibration — a gate calibrated for engineering (code review) won't work for product (A/B test significance).
