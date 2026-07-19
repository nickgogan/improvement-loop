---
name: Static Tool Set with Mode Changes as Callable Tools
summary: 'Adding or removing tools mid-conversation breaks the prompt cache because tool definitions

  live in the cached prefix. Claude Code therefore never swaps tool sets: plan mode is not a

  restricted toolset but a pair of always-present tools (EnterPlanMode/ExitPlanMode) plus a

  system message explaining the constraints. For us this is a design rule for any mode-bearing

  agent: represent modes as state the model toggles via tools, not as different tool surfaces.'
implementation_notes: 'When designing agents/skills with modes (plan vs execute, read-only vs write, teacher vs

  builder): (1) declare the full tool set once at session start and keep it static; (2) express

  mode as a callable transition tool plus behavioral instructions, with enforcement in the

  harness/permission layer rather than by hiding tools; (3) this also lets the model enter a

  mode autonomously (Claude Code''s model can call EnterPlanMode itself). Complements deferred

  tool loading: stubs keep rarely-used tools present-but-cheap instead of removing them.'
category: Tool Integration
evidence_strength: Strong (production-tested, first-party)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- Improvement Loop
- General
adopted_in: []
sources:
- claude-code-prompt-caching-is-everything.md
related_findings:
- file: deny-shrinks-toolset.md
  rel: contradicts
proposals: null
date_discovered: '2026-07-11'
last_updated: '2026-07-12'
consumed_by:
- designing-agent-tools.md
- rules/never-mutate-cached-prompt-prefix.md
pipeline_status: synthesized
extraction_note: |-
  Mode-as-callable-tool facet merged into
  [[never-mutate-cached-prompt-prefix]] as a new "Special Case: Mode as Callable
  Transition Tool" section, parallel to the existing byte-stable-catalog special
  case (session 152, 2026-07-19, Nick-delegated DD-97 extend-existing ruling). The
  rule's `applies_to` gained a mode-switching clause. Elaborates the existing
  static-tool-set invariant rather than creating a twin rule.
---

## What It Is

A Claude Code harness pattern: tool definitions are part of the cached prompt prefix, so any mid-session change to the tool list — adding, removing, or editing a parameter — invalidates the cache. Instead of implementing plan mode by swapping in a read-only toolset, the team keeps every tool present for the whole session and models the mode itself as two callable tools, `EnterPlanMode` and `ExitPlanMode`. Mode semantics (what the model may and may not do while planning) are communicated through system messages; the tool surface never changes.

## Why It Matters

Mode-as-toolset-swap is the obvious implementation and it silently destroys caching every time the user toggles modes. Mode-as-tool keeps the prefix stable, and has a second-order benefit: because the transition is a tool the model can call, the agent can decide to enter plan mode on its own rather than waiting for a user toggle. Restriction enforcement moves from "tool absent" to "tool call rejected/permission layer," which is where enforcement belongs anyway — tool absence was never a security boundary.

## Why People Are Using It

First-party production design in Claude Code's Plan Mode. The same post pairs this with `defer_loading` stubs for large MCP tool inventories: rarely-used tools stay in the prefix as name-only stubs and their full schemas load on demand via tool search, so neither cost pressure nor mode changes ever force the tool list to mutate.

**Independent cross-harness corroboration (opencode, 2026-07-12):** opencode implements the same mode-as-tool architecture from the opposite starting point — an agent there *is* a named permission ruleset (plan mode denies all edits except plan-file globs), and the transitions are the always-present `plan_enter`/`plan_exit` tools whose effect is asking the user to switch, with a `<system-reminder>` (`build-switch.txt`) stating the new permission reality after the switch (`packages/opencode/src/agent/agent.ts` — see [[opencode-analysis]]). Both harnesses agree that mode transitions are callable tools + injected instructions with enforcement in the permission layer; they diverge on whether denied tools stay advertised — opencode shrinks the visible toolset per mode (see the contradicts link), Claude Code keeps it static for cache stability.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Toolset swap per mode | Different tool lists per mode | Stateless single-turn calls where caching is irrelevant |
| Prompt-only modes | Modes expressed purely as instructions, no transition tools | Modes that only shade behavior and need no auditable transition |
| Separate sessions per mode | New session (new cache) per mode | Long-lived modes where a fresh, smaller context is itself valuable |

## Potential Improvements

- Adopt as a rule in our agent/skill design substrate: "tool surface is session-static; modes are tools + instructions"
- Audit existing skill designs for implicit toolset-swap assumptions

## Potential Failure Modes

- **Instruction-only enforcement:** if the harness does not actually reject out-of-mode tool calls, mode discipline rests on model compliance alone
- **Prefix bloat:** keeping all tools always present raises the static prefix size — mitigated by deferred-loading stubs, but not free
- **Mode-state drift:** with mode as conversational state, a compaction or confused turn can desynchronize the model's belief about the current mode
