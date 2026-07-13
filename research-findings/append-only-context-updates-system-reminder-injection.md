---
name: "Append-Only Context Updates via System-Reminder Injection"
summary: |-
  When session state changes (timestamps, file edits, mode toggles), never mutate the cached
  prompt prefix — append the update as a <system-reminder> block inside a later user message or
  tool result instead. This is how the Claude Code team keeps the prefix byte-identical across
  turns, and it explains the system-reminder blocks we see in our own harness sessions. For us
  it is the core discipline behind every other cache mechanic: state flows forward through
  messages, the prefix is immutable.
implementation_notes: |-
  Directly applicable to any harness or subagent prompt we assemble: (1) treat system prompt,
  tool definitions, CLAUDE.md, and session context as an immutable static-first stack; (2) pass
  all mid-session state changes (progress updates, budget warnings, governance reminders) as
  appended message content, never as edits to earlier layers; (3) our own skill/agent designs
  that "update the system prompt" mid-run should be redesigned to append instead. The layering
  order Claude Code uses — static system prompt & tools (global cache) -> CLAUDE.md (project
  cache) -> session context (session cache) -> messages — is the reference layout.
category: "Context Engineering"
evidence_strength: "Strong (production-tested, first-party)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources:
  - "claude-code-prompt-caching-is-everything.md"
related_findings:
  - file: "prompt-cache-stability-as-correctness.md"
    rel: "extends"
  - file: "layered-prompt-assembly-stable-segment-caching.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "defending-agent-context.md"
  - "rules/never-mutate-cached-prompt-prefix.md"
---

## What It Is

A harness design rule from the Claude Code team (Thariq Shihipar, April 2026): the prompt prefix — system prompt, tool definitions, CLAUDE.md, session context — is append-only. When information in it goes stale (current time, file contents changed on disk, a mode was toggled), the harness does not rewrite the prefix; it injects a `<system-reminder>` block into a subsequent user message or tool result carrying the updated fact. The cached prefix stays byte-identical; the model receives the correction through the conversation channel.

The enabling structure is **static-first prompt layering**, ordered by cache scope:

1. Static system prompt & tool definitions — cached globally, across sessions
2. CLAUDE.md — cached per project
3. Session context — cached per session
4. Conversation messages — grows turn by turn

Each layer changes less often than everything below it, so the maximal shared prefix is preserved across turns and across sessions.

## Why It Matters

Any mutation of the prefix invalidates the cache from that point forward, forcing full-price re-processing of everything after the edit — on long agent sessions that is a large cost and latency multiplier paid silently. Append-only updates make prefix stability structural rather than a discipline each feature must remember. This is the parent rule of the other Claude Code cache mechanics (static tool sets, no mid-session model switches, cache-safe compaction): all of them are special cases of "never touch the prefix."

## Why People Are Using It

First-party production practice in Claude Code. The team attributes their ability to offer "more generous rate limits" for subscription plans partly to the resulting cache hit rates. The post also reports fragility lessons learned: non-deterministic tool ordering, timestamps embedded in static prompts, and tool parameter changes all silently broke caching until eliminated.

**Independent cross-harness implementation (opencode, 2026-07-12):** opencode's v2 session design formalizes the identical discipline as named domain concepts — the **Context Epoch** is the immutable baseline system context kept stable for provider-cache hits, mid-run context changes are admitted only at safe provider-turn boundaries as chronological **Mid-Conversation System Messages**, and compaction rolls a new epoch rather than mutating the old one (`CONTEXT.md` §Relationships — see [[opencode-analysis]]). A second production harness independently converging on append-only-prefix-plus-injected-updates, and naming it as architecture rather than treating it as an optimization, upgrades this from one team's practice to an emerging ecosystem invariant.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Mutate prefix, accept cache miss | Rewrite system prompt when state changes | Very short sessions where cache value is negligible |
| Server-side session state | Keep context server-side; never re-send | Long-lived agent services where the provider supports it |
| Dedicated state tool | Model calls a `get_current_state` tool instead of receiving reminders | When state is large or rarely needed |

## Potential Improvements

- Codify the four-layer static-first stack as a template for our subagent prompt assembly
- Lint harness/skill designs for prefix-mutation patterns (dynamic timestamps, per-turn reordering)
- Pair with cache hit-rate observation to verify the discipline is actually holding

## Potential Failure Modes

- **Reminder blindness:** corrections appended late in a long conversation compete with the (stale) prefix; the model may keep trusting the cached statement
- **Reminder accumulation:** repeated system-reminders bloat the message log, spending the tokens the cache saved
- **Stale-prefix hazards:** genuinely wrong prefix content (e.g., a deleted file still described as present) can only be countermanded, never removed, until compaction

## Extraction Note — 2026-07-13
Extracted as **rule**: [[never-mutate-cached-prompt-prefix]] in `extracts/rules/` (harvest-queue promotion, DD-101)
