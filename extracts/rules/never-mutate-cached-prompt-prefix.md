---
title: "Never Mutate the Cached Prompt Prefix — Append-Only Context Updates"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "append-only-context-updates-system-reminder-injection"
identification_report: "defending-agent-context.harvest-queue.md::append-only-context-updates-system-reminder-injection::rule::never-mutate-cached-prompt-prefix"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "defending-agent-context.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "harness or agent-runtime developers assembling multi-turn prompts against inference APIs with prefix caching"
    - "agent designs that rewrite system prompts, instruction files, or session context mid-run and silently pay cache-invalidation costs"
    - "subagent prompt assembly for long sessions where state (time, file contents, modes) changes between turns"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — reverting to prefix mutation is a code change with no data migration; the only cost is the restored cache misses"
  auditability: "high — prefix byte-identity across consecutive requests is machine-checkable; provider cache hit-rate metrics corroborate compliance independently"
  evidence_strength: "Strong (production-tested, first-party)"
  adoption:
    status: "Not Yet Started"
    notes: "First-party production practice in Claude Code (the team partly credits resulting cache hit rates for its ability to offer generous rate limits); a second production harness independently formalized the identical discipline as immutable context epochs with mid-conversation system messages."
contract:
  preconditions: "An agent runs multi-turn sessions against an inference API with prefix caching. The prompt is assembled in layers (system prompt, tool definitions, project instruction file, session context) ahead of a growing message list. An append channel exists — subsequent user messages or tool results — through which mid-session updates can reach the model."
  invariants: "The prompt prefix is byte-identical across turns within a session. All mid-session state changes (timestamps, changed file contents, mode toggles, budget or governance reminders) travel as appended message content — e.g., a system-reminder block inside a later user message or tool result — never as edits to earlier layers. Tool definitions and their ordering are stable within a session. Compaction rolls a new prefix; it never rewrites the old one in place."
  governance: "Owner: the prompt-assembly layer of the harness or agent runtime. Any feature that needs to change agent-visible state mid-session must use the append channel; a design that edits the prefix mid-run requires explicit review with measured cache impact. Layer order follows change frequency: the most static content (system prompt, tools) outermost, per-project context next, per-session context after that, messages last."
  recovery: "If cache hit rate drops unexpectedly: diff consecutive requests' prefixes byte-for-byte to locate the mutation source (common culprits: embedded timestamps, non-deterministic tool ordering, tool parameter changes). If prefix content is genuinely wrong (e.g., a deleted file still described as present): countermand it with an appended correction — it cannot be removed until compaction or a new session. If appended reminders accumulate and bloat the message log: compact the session into a fresh prefix rather than editing the old one."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
  - "prompt-caching"
  - "append-only"
---

# Never Mutate the Cached Prompt Prefix — Append-Only Context Updates

**Source:** [[append-only-context-updates-system-reminder-injection]]
**Form:** rule
**Extraction date:** 2026-07-13

## Condition

An agent or harness runs multi-turn sessions against an inference API with prefix caching. The prompt prefix — system prompt, tool definitions, project instruction file, session context — was established at session start, and information inside it goes stale mid-session: the current time changes, a file described in context is edited on disk, a mode is toggled, a budget threshold is crossed.

The rule fires at every turn's request assembly, from session start until the session ends or is compacted.

## Action

**Required:** Treat the prefix as append-only. Keep it byte-identical across turns. Deliver every mid-session state change to the model as appended message content — canonically, a `<system-reminder>` block injected into a subsequent user message or tool result carrying the updated fact. Order prefix layers static-first, by change frequency: global static content (system prompt, tool definitions) outermost, per-project context next, per-session context after that, conversation messages last — so each layer changes less often than everything below it and the maximal shared prefix survives across turns and sessions.

**Forbidden:** Rewriting the system prompt or any earlier prompt layer mid-session. Reordering or redefining tools within a session. Embedding per-turn dynamic values (timestamps, counters) in static prompt layers. Editing the old prefix in place during compaction instead of rolling a new one. Any "update the system prompt mid-run" design — redesign it to append instead.

## Boundary

Enforced at the request-assembly step of every turn. The unit of enforcement is the token prefix ahead of the message list: from the first byte of the system prompt through the end of the last pre-message layer. Within-session only — a new session or a compaction legitimately establishes a new prefix.

## Enforcement

- **Mechanism:** The harness's prompt assembler builds each turn's request from the cached prefix object plus the grown message list; state updates are written only to the message channel. Features have no write path to the prefix after session start.
- **Check (deterministic):** For consecutive requests `R_n`, `R_{n+1}` in one session: `bytes(prefix(R_{n+1})) == bytes(prefix(R_n))`. Any inequality is a violation. Prefix byte-identity across turns is lintable in request logs.
- **Observable signal:** Provider cache hit-rate metrics. A compliant harness shows stable prefix cache hits; a persistent miss on the prefix indicates an undetected mutation (timestamp, tool reordering, parameter change).
- **Violation response:** Locate the mutating feature via prefix diff; reroute its update through the append channel; re-verify hit rates.

## Rationale

Any mutation of the prefix invalidates the inference cache from the edit point forward, forcing full-price re-processing of everything after it — on long agent sessions, a large cost and latency multiplier paid silently. Append-only updates make prefix stability *structural* rather than a discipline each feature must independently remember. This is the parent rule of the other cache mechanics (static tool sets, no mid-session model switches, cache-safe compaction): all are special cases of "never touch the prefix."

Evidence is first-party and production-tested, with independent convergence: one major harness team documented the discipline (and the fragility lessons — non-deterministic tool ordering, embedded timestamps, and tool parameter changes all silently broke caching until eliminated), and a second production harness formalized the same design as named architecture — an immutable "context epoch" baseline, mid-run changes admitted only as chronological mid-conversation system messages, and compaction rolling a new epoch rather than mutating the old.

**Distinction from [[never-inline-ephemeral-into-cached-layers]]:** that rule governs *assembly-time block composition* — which segments may share a cache-marked block when the prompt is constructed. This rule governs the *mid-session mutation path* — once the prefix is established, it is never rewritten; updates travel through the message channel. A system can satisfy either while violating the other; adopt both.

## Failure Modes

- **Reminder blindness:** corrections appended late in a long conversation compete with the (stale) cached statement; the model may keep trusting the prefix. Mitigate by making reminders explicit contradictions ("X previously stated in context is no longer true") rather than bare new facts.
- **Reminder accumulation:** repeated reminders bloat the message log, spending the tokens the cache saved. Mitigate with compaction (roll a new epoch) when accumulation is detected.
- **Stale-prefix hazards:** genuinely wrong prefix content can only be countermanded, never removed, until compaction — plan compaction cadence accordingly.

## Contract

### Preconditions
An agent runs multi-turn sessions against an inference API with prefix caching. The prompt is assembled in layers (system prompt, tool definitions, project instruction file, session context) ahead of a growing message list. An append channel exists — subsequent user messages or tool results — through which mid-session updates can reach the model.

### Invariants
The prompt prefix is byte-identical across turns within a session. All mid-session state changes (timestamps, changed file contents, mode toggles, budget or governance reminders) travel as appended message content — e.g., a system-reminder block inside a later user message or tool result — never as edits to earlier layers. Tool definitions and their ordering are stable within a session. Compaction rolls a new prefix; it never rewrites the old one in place.

### Governance
Owner: the prompt-assembly layer of the harness or agent runtime. Any feature that needs to change agent-visible state mid-session must use the append channel; a design that edits the prefix mid-run requires explicit review with measured cache impact. Layer order follows change frequency: the most static content (system prompt, tools) outermost, per-project context next, per-session context after that, messages last.

### Recovery
If cache hit rate drops unexpectedly: diff consecutive requests' prefixes byte-for-byte to locate the mutation source (common culprits: embedded timestamps, non-deterministic tool ordering, tool parameter changes). If prefix content is genuinely wrong (e.g., a deleted file still described as present): countermand it with an appended correction — it cannot be removed until compaction or a new session. If appended reminders accumulate and bloat the message log: compact the session into a fresh prefix rather than editing the old one.
