---
name: Prompt Cache Stability as Correctness
summary: OpenClaw treats deterministic ordering of model payloads as performance-critical correctness. Truncation prefers mutating newest content first to keep the prefix byte-identical for cache hits.
  Most frameworks ignore prompt caching implications entirely.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: Not Flagged
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: prompt-caching-for-stable-agent-context.md
  rel: extends
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
## What It Is

OpenClaw treats the deterministic ordering of model payloads as a performance-critical correctness concern, not a cosmetic detail. Specific rules govern how the context payload is constructed:

- **Stable prefix preservation**: The system prompt and foundational context are placed at the beginning of the payload and must remain byte-identical across turns. Any change to the prefix invalidates the prompt cache for that session.
- **Truncation strategy**: When context must be reduced to fit budget, the system truncates by mutating the newest content first (end of payload) and preserves the oldest content (beginning of payload). This keeps the cached prefix intact.
- **Deterministic ordering**: Elements within the payload are ordered deterministically — no random or non-deterministic sorting that would cause the same logical content to produce different byte sequences across turns.

The goal is to maximize prompt cache hit rates. API providers (Anthropic, OpenAI) cache the prefix of prompts; if the first N tokens are identical to a previous request, the cached computation is reused, reducing latency and cost.

## Why It Matters

Prompt caching is an increasingly important optimization as context windows grow and per-token costs compound. A cache miss on a 100K-token prompt means reprocessing the entire prefix — at scale, this translates to significant latency and cost differences.

Most frameworks construct their model payloads without considering cache implications. Reordering messages, injecting dynamic content early in the payload, or non-deterministic assembly all break cache hits without any visible signal. The failure mode is silent: everything works, it just costs more and takes longer.

OpenClaw makes this a first-class engineering concern with explicit rules, treating cache stability as a correctness property rather than an optimization afterthought.

## Why People Are Using It

Observed in [OpenClaw](https://github.com/openclaw/openclaw) v2026.4.5 — see [[openclaw-analysis]] for structural details.

The explicit rules about prefix preservation and truncation order indicate this was learned through performance measurement — the team observed cache miss rates caused by payload instability and designed rules to prevent it. This level of attention to caching behavior is absent from all other analyzed frameworks.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Ignore caching entirely | Assemble payloads without cache consideration | Prototypes, low-volume usage, or when API provider doesn't support prompt caching |
| Manual prefix pinning | Developer manually designates the cacheable prefix | When automatic ordering is too complex but cache benefits are wanted |
| Provider-level cache management | Rely on the API provider to handle caching transparently | When the provider offers robust caching that doesn't require client-side optimization |
| Session-level context persistence | Keep the entire context in-memory server-side rather than re-sending | When latency matters more than cost and the agent runs as a long-lived service |

## Potential Improvements

- Instrument cache hit/miss rates to quantify the actual cost savings from stable prefixes
- Define a "cache boundary" marker in the payload — content above the marker is immutable per session, content below is mutable
- Explore whether provider caching APIs (e.g., Anthropic's cache control headers) can be leveraged to make prefix stability less fragile

## Potential Failure Modes

- **Premature optimization**: If the workload is low-volume, the engineering effort for cache stability may exceed the cost savings
- **Stale prefix rigidity**: If the stable prefix contains information that should be updated (e.g., time-sensitive context), preserving it for cache hits means serving stale data
- **Provider behavior changes**: Prompt caching is provider-specific and may change without notice, making client-side optimization fragile
- **Content vs. cache conflict**: The optimal content ordering (most relevant first) may conflict with the optimal cache ordering (most stable first)
- **Byte-level sensitivity**: Even small changes to the prefix (whitespace, formatting) invalidate the cache, making the system fragile to seemingly innocuous modifications
