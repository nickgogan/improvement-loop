---
name: "AI Gateway: The Model-Traffic Layer (Five Jobs, Adopt-When-Plural)"
summary: |-
  The AI gateway is the shared layer between apps and model providers — the API-gateway
  pattern specialized for model traffic. Five jobs: one standard interface across
  providers, key custody (per-app throwaway keys traded for real ones), retry/failover,
  per-team/app/model token accounting, and unified observability. Adoption heuristic:
  skip it while single-provider/single-app; add it "when your situation turns plural"
  (second provider, second service, first surprise invoice). Costs: an extra hop, a
  single point of failure (mandate a direct-call bypass path), and a key-vault attack
  surface (LightLLM supply-chain attack). Distinct from the MCP gateway (governs an
  agent's tools) and the inference gateway (spreads traffic across owned GPUs).
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "ai-gateway-the-layer-every-ai-stack-eventually-needs.md"
related_findings:
  - file: "six-layer-agent-infrastructure-stack.md"
    rel: "extends"
  - file: "tool-gateway-security-boundary.md"
    rel: "same-problem"
  - file: "smart-model-routing-catch-22.md"
    rel: "extended-by"
  - file: "semantic-caching-failure-modes.md"
    rel: "extended-by"
  - file: "credential-isolation-bundled-auth-vault-proxy.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

A shared infrastructure layer that sits between every app and every model provider —
the decade-old API-gateway pattern specialized for model traffic (it reads prompts and
understands tokens, streaming, and model names, where a plain API gateway just sees web
requests). Stripped of marketing, it does five jobs:

1. **One standard interface.** Hides per-provider request formats and quirks behind a
   single API (in practice, the OpenAI-compatible format); swapping models becomes a
   string edit.
2. **Key custody.** Real provider keys live only in the gateway; each app gets a
   throwaway key the gateway trades for the real one — lose one, revoke it, nothing else
   notices.
3. **Retry and failover.** Retries provider errors and reroutes to a backup model on
   rate limits before users notice.
4. **Accounting.** Every token in/out tagged by team, app, and model — budgets become
   enforceable instead of discovered on the invoice.
5. **Observability.** The natural single place for latency, errors, and spend.

Naming disambiguation worth keeping: "AI gateway" vs "LLM gateway" are interchangeable in
practice (enterprise-governance vs developer-routing connotations). Both are distinct
from the **MCP gateway** (governs what an agent may *do* — its tools) and the
**inference gateway** (load-spreads across owned GPUs). Also, the term bundles two
different products: a unified proxy (keys/cost/logging) and a smart per-request model
router — the router half has sharp limits (see the smart-routing catch-22 finding).

**Adoption heuristic:** if one app calls one provider, call the model directly and skip
all of this. Add the gateway when the situation turns plural — a second provider, a
second service calling models, the first surprise invoice, or the first "which team spent
all the money?" The one-key-for-many-models demo is the least interesting reason the
layer exists.

**Costs and risks:** an added hop (usually negligible next to model latency, but measure
on latency-critical paths); a deliberate single point of failure — if the gateway falls
over, every AI feature falls with it, so plan a code path that bypasses the gateway and
calls providers directly in a pinch; and a concentrated trust cost — the box holding
every API key is the box attackers most want (the most popular open-source gateway,
LightLLM, took a supply-chain attack targeting exactly those keys).

## Why It Matters

This is the one infrastructure layer the KB previously named nowhere: the six-layer agent
infrastructure stack finding (compute, identity, memory, tools, provisioning,
orchestration) has no model-traffic layer, and this finding extends it with that missing
layer. Decision-relevant for any multi-model agentic OS: the gateway is where model
plurality, spend accountability, and key custody consolidate — or deliberately don't.

## Why People Are Using It

Framed as the layer "every team hits about 3 months in": the same plumbing problems
(copied retry logic, hardcoded keys, unattributable spend, provider outage taking down
half the product) that produced API gateways a decade ago. Adoption is need-driven rather
than fashion-driven, which is why the source's when-not-to-adopt guidance is as concrete
as its feature list.

## Potential Alternatives

- **Direct provider calls** — correct default for single-provider/single-app (the
  source's own advice).
- **Provider-native SDK abstractions / thin client wrappers** — solve interface
  unification without the shared-infrastructure (and SPOF) commitment.
- **Old API gateway with AI plugins** — exists, but lacks prompt/token awareness.

## Potential Improvements

- Cache-aware and budget-aware routing policies (see companion findings).
- The layer may not survive as a distinct product — it could be swallowed into existing
  infra tooling; the *jobs* persist even if the category name doesn't.

## Potential Failure Modes

- **SPOF without a bypass:** the reliability layer becomes the outage; a
  gateway-skipping direct-call path is mandatory, not optional.
- **Key-vault concentration:** one compromise exposes every provider credential
  (LightLLM precedent).
- **Premature adoption:** taking on shared-infrastructure operational burden while still
  single-provider/single-app.
- **Two-products confusion:** buying "a gateway" for proxy jobs and unknowingly getting
  opinionated smart routing (or vice versa).
