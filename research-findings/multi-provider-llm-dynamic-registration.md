---
name: "Multi-Provider LLM Abstraction with Dynamic Registration"
summary: "Extensions can register entirely new LLM providers at runtime — specifying base URL, models, API type, OAuth flows, custom stream handlers, and per-model configuration. Registration is queued during init and takes effect immediately after binding, enabling mid-session provider switching without restart."
implementation_notes: null
category: "Model Selection"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "auxiliary-model-slot-architecture.md"
    rel: "enables"
proposals: null
date_discovered: "2026-05-24"
last_updated: "2026-05-24"
pipeline_status: "raw"
---

# Multi-Provider LLM Abstraction with Dynamic Registration

## Pattern

A unified LLM API layer that:
1. Abstracts across provider APIs (Anthropic Messages, OpenAI Responses, Google, etc.)
2. Allows runtime provider registration via extension API (`registerProvider()`)
3. Supports: base URL override, custom models, OAuth login flows, custom stream handlers, per-model headers
4. Queues registrations during extension load; applies immediately after runtime binding
5. Supports `unregisterProvider()` to remove providers and restore built-in defaults

Configuration per provider:
- `name`, `baseUrl`, `apiKey` (or env var name)
- `api` type (anthropic-messages, openai-responses, etc.)
- `models[]` with id, name, reasoning support, input types, cost, context window, max tokens
- `oauth` with login/refresh/getApiKey callbacks
- `streamSimple` for custom API stream handling

## Why It Matters

Enables agent harnesses to work with any LLM provider without code changes. Extensions can add corporate proxies, self-hosted models, or experimental providers. Combined with the auxiliary model slot pattern, this means each task-type can use a different provider/model combination — all configurable at runtime.

## How It Could Fail

- Provider API differences that don't map cleanly to the unified abstraction
- OAuth complexity for providers with non-standard flows
- Model capability differences (reasoning, vision) that surface as runtime errors
- Custom stream handlers that don't handle edge cases (timeouts, partial responses)

## Evidence

Pi agent harness (earendil-works/pi) — `packages/ai/` providing unified API across 5+ providers, `ProviderConfig` type in extension types, `registerProvider`/`unregisterProvider` in ExtensionAPI.
