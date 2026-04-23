---
name: Machine Payments Protocol (MPP) for Agent-to-Service Payments
summary: Stripe and Tempo have co-authored an open Machine Payments Protocol (MPP) that lets agents pay services programmatically — accepted in a few lines via PaymentIntents API, with Shared Payment Tokens (SPTs) for card/BNPL and stablecoin rails. Stripe layered an Agentic Commerce Suite (agent-ready checkout) and Stripe Projects (permissioned agent authentication/provisioning) around the protocol. Cross-vendor convergence with x402-on-Base (Coinbase) indicates an emerging multi-rail agent-payment standard.
implementation_notes: MetaSystem agents do not transact today and this is not on the roadmap. Track the standard for when/if S2 or S3 agents need to provision paid external services (e.g., Perplexity research credits, sandbox compute) without manual billing setup.
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- stripe-machine-payments-protocol.md
- stripe-agents-billing-workflows-docs.md
related_findings:
- file: agent-to-agent-payment-x402-coinbase-wallet.md
  rel: extends
- file: stripe-cli-terminal-based-payment-product-managem.md
  rel: extends
- file: six-layer-agent-infrastructure-stack.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-23'
last_updated: '2026-04-23'
pipeline_status: raw
consumed_by: []
---

# Machine Payments Protocol (MPP) for Agent-to-Service Payments

## What It Is

MPP is an open protocol for programmatic agent payments, co-authored by Stripe and Tempo. Businesses accept payments over MPP in a few lines of code using Stripe's PaymentIntents API. Shared Payment Tokens (SPTs) support card and buy-now-pay-later rails alongside stablecoins. Stripe surrounds the protocol with two complementary offerings:

- **Agentic Commerce Suite** — makes a merchant's catalog discoverable to agents, simplifies checkout, and accepts agentic payments through a single integration.
- **Stripe Projects** — permissioned authentication and provisioning for agents; an agent gets a structured identity and can pay for services without a human in the loop for every transaction.

A parallel track: Stripe announced x402-on-Base (Coinbase Base) support, extending the agentic payment surface to onchain rails.

## Why It Matters for Us

Plain English: if MetaSystem agents ever need to buy things (extra Perplexity budget, E2B sandbox minutes, a paid MCP server), they currently can't do it without Nick in the loop with a credit card. MPP + Stripe Projects + x402 together name the *first concrete standard* for letting an agent pay for services programmatically with per-session budget limits. This is adjacent to, not the same as, agent-to-agent payment (which x402 emphasizes). We don't need this yet, but when we do, the standard will exist.

## Why People Are Using It

Stripe is a Tier-1 payments incumbent; co-authoring MPP with Tempo and launching Agentic Commerce Suite is a clear signal they treat agent economics as a first-class surface, not a marketing concept. Production Stripe merchants can accept agent payments today with trivial SDK changes.

## Potential Alternatives

- Human-in-the-loop billing (current MetaSystem state)
- x402-on-Base only (crypto-only rail, no fiat fallback)
- Per-provider bespoke API keys scoped to an agent identity (what most teams do today)

## Potential Improvements

Track whether MPP survives as an open standard or fragments per-vendor. Watch for SPT revocation tooling (how do you claw back an agent's payment authority if it misbehaves?). Observe which sandbox providers (E2B, Daytona, Modal) adopt MPP for compute billing.

## Potential Failure Modes

- Agent prompt-injection leading to unauthorized spend — the same threat model as the x402/Coinbase finding
- Spec fragmentation: if major LLM vendors build non-MPP payment rails, interoperability erodes
- Regulatory drag on stablecoin/BNPL rails in some jurisdictions
