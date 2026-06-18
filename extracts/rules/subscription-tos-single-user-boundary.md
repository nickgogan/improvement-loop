---
title: "Subscription ToS Single-User Boundary for Agent SDKs"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "subscription-tos-single-user-boundary-for-agent-sdks"
extraction_date: "2026-05-25"
last_change_session: 96
last_change_sl: "session-96-codifier-extract-non-pattern-artifacts"
identification_report: "2026-05-25-identification-report-session-95.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams building agents on SDK subscription plans (Anthropic Max, OpenAI Plus/Pro, similar flat-rate offerings)"
    - "any agent architecture where the deployment target may eventually serve multiple users"
    - "build-vs-buy decisions where subscription economics influence SDK vs framework vs API-key architecture"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "high — discovering this constraint after building on a subscription plan requires re-architecting for API-key economics (10-50x cost increase) or restricting deployment to single-user"
  auditability: "high — compliance is verifiable by checking: does this agent serve only the subscriber? If multiple users interact with it, is the underlying inference on API keys rather than subscription?"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "An agent is being built using an SDK that operates under a subscription plan. The agent may be deployed to serve users beyond the individual subscriber."
  invariants: "Agents built on SDK subscription plans serve only the individual subscriber. Multi-user agents use API-key billing, not subscription billing. The deployment boundary (single-user vs multi-user) is determined before architecture is committed. The 10-50x cost multiplier of switching from subscription to API keys is factored into architecture decisions at design time, not discovered at deployment time."
  governance: "Owner: the team or individual making the build-vs-buy decision. This constraint must be surfaced during architecture review as a first-class deployment boundary. Any plan to deploy an SDK-built agent to multiple users triggers the graduation path: subscription → API keys → framework (if token-efficient patterns are needed). Account bans for ToS violations are real and documented in the ecosystem."
  recovery: "If a multi-user agent is discovered running on a subscription plan: immediately plan migration to API-key billing before enforcement action. If cost shock occurs at migration: evaluate framework adoption for token-efficient patterns that reduce per-query cost. If the team built a full product on subscription before discovering the constraint: treat as architecture debt requiring a phased migration plan, not a quick fix."
tags:
  - "extracted-artifact"
  - "rule"
  - "governance"
  - "economics"
  - "deployment"
---

# Subscription ToS Single-User Boundary for Agent SDKs

**Source:** [[subscription-tos-single-user-boundary-for-agent-sdks]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent is being built using an SDK subscription plan (Anthropic Max, OpenAI Plus/Pro, or equivalent flat-rate offering). The agent's deployment target may serve users beyond the individual subscriber — team members, clients, or the public.

## Action

**Required:** Determine the deployment boundary (single-user vs multi-user) before committing architecture. If multi-user: design for API-key economics from the start. Factor the 10-50x cost multiplier into architecture decisions at design time.

**Forbidden:** Deploying an SDK-subscription-built agent to serve multiple users. Assuming that because the SDK technically works for multi-user, it is permitted. Building a full product on subscription economics and discovering the ToS boundary at deployment time.

## Boundary

Enforced at the architecture decision point — specifically when the team decides who the agent will serve. The boundary is legal/contractual (Terms of Service), not technical. The SDK works fine for multiple users; the ToS prohibits it.

## Enforcement

Deterministic check at design review: "Who will use this agent? Just the subscriber, or multiple people?" If the answer is "multiple people" and the current plan uses subscription billing, the architecture must change before implementation begins. Secondary check: "Is the inference cost model subscription-based or API-key-based?" Multi-user + subscription = violation.

## Rationale

SDK subscription plans provide 10-50x cost efficiency over API keys (e.g., Claude Max at $200/month provides ~$2,500-$5,000 in API-equivalent usage). This subsidy is funded by the single-user restriction. Providers actively enforce this boundary — account bans for violations are documented. The constraint is the primary economic forcing function for the SDK-to-framework graduation decision, and discovering it post-build is the most expensive possible timing.
