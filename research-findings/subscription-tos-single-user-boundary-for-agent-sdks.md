---
name: Subscription ToS Single-User Boundary for Agent SDKs
summary: SDK subscriptions (Anthropic Max, OpenAI Plus/Pro) restrict usage to the individual subscriber. Deploying an SDK-built agent to multiple users violates terms of service and risks account bans.
  Multi-user agents must use API keys, jumping costs 10-50x. This hidden constraint is the primary economic forcing function for the SDK-to-framework graduation decision.
implementation_notes: null
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- sdk-vs-framework-decision-ai-agents.md
related_findings:
- file: sdk-vs-framework-decision-for-agent-building.md
  rel: enables
- file: claude-code-max-plan-subsidy-vs-api-cost-tool.md
  rel: same-problem
- file: agent-cost-blowup-mitigation-strategies.md
  rel: same-problem
- file: sdk-to-framework-graduation-path.md
  rel: enables
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- extracts/rules/subscription-tos-single-user-boundary.md
- designing-agent-tools.md
tags:
- session-95-reextract
---

## What It Is

A critical deployment constraint that many agent builders discover too late: all major SDK subscription plans (Anthropic Max, OpenAI Plus/Pro, similar offerings) include terms of service that restrict usage to the individual subscriber. Building an agent with the Claude Agent SDK and deploying it for your team, your company, or your clients is a ToS violation if the agent runs on your subscription.

The enforcement mechanism is real -- Anthropic and OpenAI have banned accounts for violations (documented in the OpenClaw ecosystem). The workaround is API key usage, but API pricing is 10-50x more expensive than the effective per-token rate of subscription plans. The Claude Code Max plan ($200/month) provides an estimated $2,500-$5,000 in API-equivalent usage. Switching to API keys for a multi-user agent immediately changes the economics from "nearly free" to "significant ongoing cost."

This creates a hard boundary in agent architecture: single-user agents can leverage subscriptions; multi-user agents must be designed for API-key economics from the start, which typically means using a framework with token-efficient patterns rather than a batteries-included SDK.

## Why It Matters

The subscription subsidy is the hidden variable in the SDK-vs-framework decision. Practitioners who build on SDKs because they're "simpler and cheaper" often don't realize the cost model changes completely at the deployment boundary. The decision isn't just "SDK vs framework" -- it's "who pays for inference."

For MetaSystem, this is directly relevant: our current agent system runs on a single Claude Max subscription. Any future scenario involving other users (household members, team members) would hit this boundary. Architecture decisions made now about skill portability and framework independence are forward-looking hedges against this constraint.

## Why People Are Using It

This isn't a pattern people "use" -- it's a constraint they navigate. Practitioners report:
- Building agents on SDK for personal use, then discovering they can't deploy to teams
- Transitioning entire agent architectures to frameworks specifically to switch from subscription to API pricing
- Using "just me" as the first question in the SDK-vs-framework decision framework
- Treating the ToS boundary as the primary graduation trigger

## Potential Improvements

- SDK providers offering team/enterprise subscription tiers with multi-user agent permissions
- Usage-based SDK pricing that preserves the simplicity of SDK while allowing multi-user deployment
- Clearer documentation from SDK providers about what constitutes "single user" vs. "multi-user" usage

## Potential Failure Modes

- Account bans from inadvertent ToS violations (e.g., sharing an agent URL with colleagues)
- Building a full product on SDK before discovering the ToS constraint, requiring expensive rewrite
- Assuming that because the SDK works, it's permitted -- conflating technical capability with legal permission
- Cost shock when switching from subscription to API keys mid-project
