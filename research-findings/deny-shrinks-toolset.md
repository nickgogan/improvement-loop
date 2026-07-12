---
name: "Deny Shrinks the Advertised Toolset"
summary: |-
  opencode removes blanket-denied tools from the model's advertised tool list entirely
  (visibleTools) instead of letting the model call them and rejecting — and filters denied
  subagents out of the task tool's options the same way. The model never wastes attempts,
  never sees refusal noise, and its perceived capability surface IS its permitted surface.
  This takes the opposite position from the Claude Code team's static-tool-set rule, which
  keeps the surface fixed for prompt-cache stability and enforces at the permission layer —
  the two findings bound a real design axis: shape the surface vs gate the calls.
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "static-tool-set-mode-changes-as-callable-tools.md"
    rel: "contradicts"
  - file: "progressive-skill-loading.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
---

## What It Is

In opencode's permission engine, a blanket `deny` on a tool (action `deny` on pattern `*`) does more than block calls: `disabled()` / `visibleTools()` (`packages/opencode/src/permission/index.ts`) remove the tool from the tool list advertised to the model, so the model cannot attempt it at all. The same logic filters which subagents are even listed as `task` options (`tool/registry.ts`) — a denied delegate simply doesn't exist from the model's perspective. Agents being named permission rulesets in opencode, this means each agent's *visible* capability surface is computed from its *permitted* surface; plan mode's model genuinely sees no edit tools.

## Why It Matters

There are two coherent positions on denied capability, and this finding is the cleaner statement of the shrink side. Shrinking the surface saves the model from wasted attempts and refusal-error noise, keeps prompts smaller, and eliminates a class of prompt-injection bait ("call the tool you're not supposed to"). The cost is the one the Claude Code team's static-tool-set rule ([[static-tool-set-mode-changes-as-callable-tools]]) is built around: tool definitions live in the cached prompt prefix, so a per-mode or mid-session toolset change invalidates the prompt cache — that finding keeps every tool advertised and moves enforcement to the permission layer precisely to keep the prefix byte-identical. opencode pays the cache cost knowingly (its per-agent surfaces are computed at session/agent construction, where a fresh prefix is expected anyway). The design axis for any harness: **shape the surface** (accuracy of the model's world-model, smaller prompts) versus **gate the calls** (cache stability, mode fluidity, tools-as-mode-transitions). Where the surface changes only at session or agent boundaries, shrinking is nearly free; where modes toggle mid-session, gating wins.

## Why People Are Using It

Observed in [opencode](https://github.com/anomalyco/opencode) dev branch (`34e5809`, 2026-07-11) — see [[opencode-analysis]] for structural details. It composes with opencode's asymmetric subagent inheritance (denies flow down) so child agents' advertised toolsets are automatically narrower than their parents'.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Static surface + permission gate | All tools always advertised; denies enforced at call time | Mid-session mode changes; cache-sensitive long sessions (the Claude Code position) |
| Deferred/stub loading | Tools present as name-only stubs, schemas load on demand | Cost pressure from large tool inventories without any deny semantics |
| Prompt-only restriction | Instructions say "don't use X"; tool stays callable | Never as an enforcement boundary; acceptable only for soft preferences |

## Potential Improvements

- Hybrid: shrink at session/agent construction, gate for anything that must change mid-session — capturing both findings' wins
- Surface a "hidden by policy" note to the *user* (not the model) so humans aren't confused by capability the UI shows but the agent lacks

## Potential Failure Modes

- **Prompt-cache invalidation:** any mid-session surface change breaks the cached prefix — the core objection from the contradicting finding
- **Model confusion at boundaries:** transcripts spanning an agent switch reference tools that no longer "exist"
- **False security:** surface shaping is a UX/accuracy measure; without call-time enforcement underneath, anything that re-injects a tool definition re-opens the capability
