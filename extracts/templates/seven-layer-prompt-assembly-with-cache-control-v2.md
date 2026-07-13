---
title: "Seven-Layer Prompt Assembly with Cache-Control Annotations (v2)"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "append-only-context-updates-system-reminder-injection"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "defending-agent-context.harvest-queue"
version: 2
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "multi-turn agent systems that assemble prompts programmatically at each model call, on any provider"
    - "prompt assembly modules for any agent with a stable identity/memory prefix and ephemeral per-turn state"
    - "teams mapping prompt layers to provider cache tiers (global / project / session / turn) to maximize the shared prefix"
    - "harness or subagent designs deciding where mid-session state updates enter the conversation without disturbing the cached prefix"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — the layered ordering and append-only discipline are provider-agnostic and cost nothing to keep; removing the optional cache_control annotations (the Anthropic instantiation) requires updating prompt assembly code and drops cache hit rates immediately, but needs no data migration"
  auditability: "high — layer stability classification and cache-tier assignment are documented in the template; prefix byte-identity across turns is lintable; on Anthropic, cache-read vs. cache-write token counts are visible in API response usage"
  evidence_strength: "Strong (production-tested, first-party)"
  adoption:
    status: "Not Yet Started"
    notes: "The Claude Code team runs the four-tier static-first stack in production (Thariq Shihipar, April 2026), attributing part of their generous rate limits to the resulting cache hit rates. opencode independently formalized the same discipline as named domain concepts (Context Epoch, Mid-Conversation System Messages). Hermes (NousResearch) uses a dedicated prompt_caching.py module for the Anthropic instantiation. MetaSystem CLAUDE.md files load as project context but are not yet cache-annotated. Design work required before implementation."
contract:
  preconditions: "An agent system makes multi-turn model calls. A prompt assembly step constructs the prompt (or system-parameter array) before each call. The system has identifiable stable segments (identity, memory, skills, project context) and ephemeral segments (task state, budget warnings, context pressure). If the provider supports explicit cache breakpoints (Anthropic), cache_control annotations may be added as the concrete instantiation; if it caches by prefix-prefix match, the layering alone is sufficient."
  invariants: "Layers are assembled stable-first, deepest-stable-last, so the maximal shared prefix survives across turns and (where the provider supports it) across sessions. Layer order is preserved: stable layers never follow ephemeral layers in the assembled prompt. STALE PREFIX CONTENT IS COUNTERMANDED VIA APPENDED MESSAGES, NEVER EDITED IN PLACE — when content in a stable/cached layer goes stale mid-session (timestamps, changed files on disk, a toggled mode), it is injected as a <system-reminder> block in a later user message or tool result, not rewritten in the prefix (see [[never-mutate-cached-prompt-prefix]]). On Anthropic, the last stable layer carries cache_control and the ephemeral layer never does; breakpoints anchor at the deepest reliably-stable boundaries (last tool definition, last stable system part, latest user message), at most four per API limits. No ephemeral content is included in any cached block."
  governance: "Owner of the prompt assembly module for each agent. Layer stability classification and cache-tier assignment are documented in code comments or an adjacent spec. When stable layers change (new skill added to metadata, memory updated), the cache boundary and the prefix-immutability assumption are reviewed. Ephemeral-to-stable reclassification requires explicit justification — semi-dynamic content marked stable will serve stale context that can then only be countermanded, never removed, until compaction."
  recovery: "If cache hit rate is unexpectedly low → check for prefix mutation (a dynamic timestamp, per-turn tool reordering, or an edited stable layer invalidates the cache every call), for ephemeral content inside cached blocks, or for a breakpoint anchored too shallow (short reusable prefix). If stale context is observed → confirm the update was appended as a <system-reminder>, not edited into the prefix; if the prefix was mutated, restore byte-identity and re-append. If cache_control is unsupported for a provider → drop the annotations and fall back to prefix-prefix-match caching on the same layered ordering; the template structure remains valid."
tags:
  - "extracted-artifact"
  - "template"
  - "prompt-engineering"
  - "context-engineering"
  - "caching"
  - "prompt-assembly"
  - "append-only"
---

# Seven-Layer Prompt Assembly with Cache-Control Annotations (v2)

**Source:** [[append-only-context-updates-system-reminder-injection]]
**Form:** template
**Extraction date:** 2026-07-13
**Version:** 2 — evolves v1 ([[seven-layer-prompt-assembly-with-cache-control]]) along three axes: (1) a harness-scope cache-tier column mapping each layer to global/project/session/turn; (2) an append-only update-discipline section + invariant countermanding stale prefix content via appended messages rather than in-place edits (see [[never-mutate-cached-prompt-prefix]]); (3) a provider-agnostic four-layer default in the Variation Axis, with the Anthropic cache_control annotations recast as one instantiation of a provider-neutral layering model.

> **v1 → v2 in one line:** v1 was an Anthropic API implementation scaffold (content blocks + `cache_control` + a `prompt_caching.py` schematic). v2 keeps that as one instantiation and lifts the conceptual model to harness scope: a four-tier cache hierarchy (global → project → session → turn) plus the append-only prefix discipline that is the parent rule of every cache mechanic below it.

## Variables

| Variable | Description | Stable? | Cache scope (tier) |
|----------|-------------|---------|--------------------|
| `{{AGENT_ROLE}}` | Core role definition and persona statement | Yes | **global** — system prompt, cached across sessions |
| `{{SOUL_MD}}` | Global personality and behavioral principles (SOUL.md or equivalent) | Yes | **global** — system prompt |
| `{{MEMORY_MD}}` | Persistent user/system facts (MEMORY.md) | Yes | **global** — system prompt (changes per deployment, not per session) |
| `{{USER_MD}}` | User preferences and profile (USER.md) | Yes | **global** — system prompt |
| `{{SKILLS_METADATA}}` | Skill titles and "When to use" summaries for relevant skills | Yes | **global** — system prompt |
| `{{TOOL_DEFINITIONS}}` | Tool/function schemas sent with the request | Usually Yes | **global** — cached across sessions; carries its own breakpoint at the last def |
| `{{PROJECT_CONTEXT}}` | Project-specific context file (AGENTS.md, .hermes.md, CLAUDE.md) | Yes | **project** — cached per project |
| `{{PROVIDER_INSTRUCTIONS}}` | Provider-specific tool-calling format and constraints | Conditional | **global**/session — with the system stack unless it varies per session |
| `{{SESSION_CONTEXT}}` | Session-scoped baseline context (the immutable "epoch": working set, task framing, resolved config) | Semi | **session** — cached per session; stable within a session, re-rolled on compaction |
| `{{EPHEMERAL_STATE}}` | Budget warnings, context-pressure hints, session flags, and appended `<system-reminder>` updates | No | **turn** — the growing message channel; never cached |

**Stability classification:** Stable = changes infrequently (per deployment, not per call). Conditional = changes per provider but not per call within a session. Semi = stable within a session, re-rolled at session/compaction boundaries. Ephemeral = changes every call or turn.

**Cache-tier hierarchy (harness scope).** Each layer changes less often than everything below it, so the maximal shared prefix survives across turns and sessions. The four tiers, deepest-cached first:

1. **global** — static system prompt & tool definitions; cached across sessions.
2. **project** — CLAUDE.md / project context; cached per project.
3. **session** — the session-context baseline (opencode's "Context Epoch"); cached per session, stable within it.
4. **turn** — conversation messages; grows turn by turn, never cached.

The seven named layers below instantiate these four tiers: Layers 1–4 + tool defs + provider instructions sit in **global**, Layer 5 in **project**, the session-context baseline in **session**, and Layer 7 (ephemeral + appended reminders) in **turn**.

---

## Body

```
# Layer 1 — Core Role / Persona                          [tier: global]
{{AGENT_ROLE}}

---

# Layer 2 — Global Personality (SOUL.md)                 [tier: global]
{{SOUL_MD}}

---

# Layer 3 — Persistent Memory                            [tier: global]
## System Memory
{{MEMORY_MD}}

## User Profile
{{USER_MD}}

---

# Layer 4 — Skills Metadata                              [tier: global]
Available skills (titles and when-to-use summaries):
{{SKILLS_METADATA}}

# (Tool definitions, if sent, carry their own breakpoint at the LAST tool def)
{{TOOL_DEFINITIONS}}  [cache_control on the last tool definition — Anthropic instantiation]

---

# Layer 5 — Project Context                              [tier: project]
{{PROJECT_CONTEXT}}

[cache_control: {"type": "ephemeral"}]  ← BREAKPOINT: last stable system/project part (Anthropic)

---

# Layer 6 — Session-Context Baseline (the epoch)         [tier: session]
{{SESSION_CONTEXT}}
# Immutable within the session; re-rolled (not edited) on compaction.

---

# Layer 7 — Ephemeral State & Appended Updates           [tier: turn]
{{EPHEMERAL_STATE}}
# Per-turn state AND every mid-session correction to a stale upper layer arrives
# here as an appended <system-reminder> block — never as an edit to Layers 1-6.
```

**Cache boundary placement (opencode heuristic — Anthropic instantiation).** Anthropic supports up to four cache breakpoints; place them at the deepest reliably-stable boundaries rather than on a single arbitrary layer:

1. **Last tool definition** — tool schemas are usually stable across a session; anchor a breakpoint on the final tool def so the whole tool block is read-cached (global tier).
2. **Last stable system/project part** — the marker on Layer 5 (or the deepest stable layer present) caches identity + memory + skills + project context in one prefix (global + project tiers).
3. **Latest user message** — for cross-turn reuse, a breakpoint at the most recent user turn lets the next call read-cache everything up to and including it (extends the reusable prefix into the session/turn boundary).

Never mark Layer 7. The cached prefix should always extend as deep as stability allows; a breakpoint placed before a genuinely stable layer leaves cheap reads on the table.

**Provider-agnostic note.** On a provider that caches by prefix-prefix match rather than explicit markers, drop the `cache_control` lines entirely — the four-tier layered ordering alone preserves the reusable prefix. The cache_control annotations are one instantiation of the layering model, not the model itself.

---

## Append-Only Update Discipline

**The parent rule.** Everything above — the tier ordering, the breakpoint placement — is downstream of one invariant: **the prefix is append-only.** When information in a stable/cached layer goes stale mid-session (the current time, a file that changed on disk, a mode that was toggled), the assembly step does **not** rewrite that layer. It injects a `<system-reminder>` block into a subsequent user message or tool result carrying the corrected fact. The cached prefix stays byte-identical; the model receives the correction through the conversation channel (Layer 7 / turn tier). See the companion rule [[never-mutate-cached-prompt-prefix]].

**Why this is load-bearing.** Any mutation of the prefix invalidates the cache from that point forward, forcing full-price re-processing of everything after the edit — a large, silent cost/latency multiplier on long agent sessions. Append-only updates make prefix stability structural rather than a discipline each feature must remember. Every other cache mechanic (static tool sets, no mid-session model switches, cache-safe compaction) is a special case of "never touch the prefix."

**How to apply it:**

1. Treat Layers 1–6 (system prompt, tool definitions, project context, session-context baseline) as an immutable static-first stack once the session opens.
2. Pass all mid-session state changes — progress updates, budget warnings, governance reminders, corrected facts — as appended message content in Layer 7, never as edits to earlier layers.
3. Redesign any skill/agent step that "updates the system prompt" mid-run to append instead.
4. Roll a new session-context epoch (Layer 6) on compaction rather than editing the old one; the epoch is replaced wholesale, not mutated.

**Failure modes to watch (from the source finding):**

- **Reminder blindness** — corrections appended late in a long conversation compete with the still-cached (stale) prefix; the model may keep trusting the cached statement.
- **Reminder accumulation** — repeated `<system-reminder>`s bloat the message log, spending the tokens the cache saved.
- **Stale-prefix hazard** — genuinely wrong prefix content (e.g., a deleted file still described as present) can only be countermanded, never removed, until the next compaction re-rolls the epoch.

---

## Usage

**When to use this template:**
- Building or refactoring a prompt assembly module for a multi-turn agent, on any provider
- Auditing an existing prompt assembly for cache efficiency AND prefix-mutation hazards
- Designing a new agent with stable identity and ephemeral task state
- Mapping prompt layers onto a provider's cache tiers (global / project / session / turn)

**How to instantiate:**
1. Identify which layers are present for the agent (not all agents use all layers).
2. Classify each layer as stable, conditional, semi, or ephemeral, and assign its cache tier (global / project / session / turn).
3. Assemble layers stable-first, deepest-stable-last (global → project → session → turn). Never reverse this order.
4. Commit to the append-only discipline: Layers 1–6 are immutable within the session; every mid-session correction is an appended `<system-reminder>`.
5. **If the provider supports explicit breakpoints (Anthropic):** place `cache_control: {"type": "ephemeral"}` at the deepest stable boundaries — last tool definition, last stable system/project part, and (optionally) the latest user message — up to the four-breakpoint limit. Send ephemeral layers as separate blocks without cache markers.
6. **If the provider caches by prefix-prefix match:** skip the annotations; the layered ordering alone preserves the reusable prefix.

**Why default-on pays (opencode economics).** A cache *write* costs roughly 1.25× base input tokens; a cache *read* costs roughly 0.1×. A cached prefix therefore breaks even once it is read about 1.4 times — a threshold every multi-turn session clears — which is why opencode ships caching default-on rather than per-feature opt-in. The template's payoff scales with how deep the stable prefix runs, so anchoring breakpoints (or simply keeping the prefix byte-identical) at the last stable boundary maximizes the reusable prefix.

**Anthropic API implementation note (the v1 instantiation).** Cache control is set on individual content blocks in the `system` parameter array (and on tool definitions), not as a top-level field. The last block with `cache_control` set defines that breakpoint's boundary — all content up to and including it is cached.

```python
# Example: prompt_caching.py module (schematic) — the Anthropic instantiation of the four-tier model
def assemble_system_prompt(agent_role, soul, memory, user, skills, project,
                           tool_defs, provider_instructions, session_context, ephemeral):
    # global tier (cached across sessions) + project tier
    stable_blocks = [
        {"type": "text", "text": agent_role},
        {"type": "text", "text": soul},
        {"type": "text", "text": memory + "\n" + user},
        {"type": "text", "text": skills},
        {"type": "text", "text": project, "cache_control": {"type": "ephemeral"}},  # breakpoint: last stable system/project part
    ]
    # tool_defs carry their own breakpoint on the last definition (global tier)
    # session tier — the immutable epoch; re-rolled on compaction, never edited
    session_blocks = [
        {"type": "text", "text": session_context},
    ]
    # turn tier — ephemeral state AND appended <system-reminder> corrections; never cached
    dynamic_blocks = [
        {"type": "text", "text": provider_instructions},
        {"type": "text", "text": ephemeral},
    ]
    return stable_blocks + session_blocks + dynamic_blocks
```

---

## Variation Axis

| Scenario | Adjustment |
|----------|------------|
| Agent has no SOUL.md | Collapse Layer 2 into Layer 1; breakpoint moves with the last stable layer |
| Skills are session-variable (selected per task) | Reclassify Layer 4 as conditional; move the system breakpoint to Layer 3 |
| Agent sends tool definitions | Add a dedicated breakpoint on the last tool definition (opencode heuristic); independent of the system-part breakpoint |
| Provider instructions are stable for the session | Include Layer 6/provider block inside the cached prefix; move the system breakpoint accordingly |
| Long multi-turn conversation | Add a breakpoint at the latest user message for cross-turn read reuse (up to the four-breakpoint limit) |
| Single-turn use (no cache benefit) | Remove cache_control annotations; the first write costs ~1.25× with no read to amortize it; layer order and content remain valid |
| **Provider-agnostic four-layer default (no explicit cache markers)** | Collapse the seven named layers into the finding's four provider-neutral tiers — **(1) system prompt + tool definitions / (2) project memory (CLAUDE.md) / (3) session context / (4) messages** — with NO `cache_control` annotations. For harnesses whose provider caches by prefix-prefix match rather than explicit breakpoints, the layered ordering plus the append-only discipline is the whole mechanism; the Anthropic markers are one instantiation, not a requirement. This is the conceptual core of v2. |
| Non-Anthropic provider with explicit cache API | Keep the four-tier ordering; translate the breakpoint placements to the provider's cache primitive |
| MetaSystem agents (CLAUDE.md as project context) | Layer 5 = CLAUDE.md content (project tier); Layer 6 = session state/task assignment (session tier); Layer 7 = per-turn progress updates and appended reminders (turn tier) |

---

## Contract

### Preconditions
An agent system makes multi-turn model calls. A prompt assembly step constructs the prompt (or system-parameter array) before each call. The system has identifiable stable segments (identity, memory, skills, project context) and ephemeral segments (task state, budget warnings, context pressure). If the provider supports explicit cache breakpoints (Anthropic), `cache_control` annotations may be added as the concrete instantiation; if it caches by prefix-prefix match, the layering alone is sufficient.

### Invariants
Layers are assembled stable-first, deepest-stable-last, so the maximal shared prefix survives across turns and (where the provider supports it) across sessions. Layer order is preserved: stable layers never follow ephemeral layers in the assembled prompt. **Stale prefix content is countermanded via appended messages, never edited in place** — when content in a stable/cached layer goes stale mid-session (timestamps, changed files on disk, a toggled mode), it is injected as a `<system-reminder>` block in a later user message or tool result, not rewritten in the prefix (see [[never-mutate-cached-prompt-prefix]]). On Anthropic, the last stable layer carries `cache_control` and the ephemeral layer never does; breakpoints anchor at the deepest reliably-stable boundaries (last tool definition, last stable system part, latest user message), at most four per API limits. No ephemeral content is included in any cached block.

### Governance
Owner of the prompt assembly module for each agent. Layer stability classification and cache-tier assignment are documented in code comments or an adjacent spec. When stable layers change (new skill added, memory updated), the cache boundary and the prefix-immutability assumption are reviewed. Ephemeral-to-stable reclassification requires explicit justification — semi-dynamic content marked stable will serve stale context that can then only be countermanded, never removed, until compaction.

### Recovery
If cache hit rate is unexpectedly low → check for prefix mutation (a dynamic timestamp, per-turn tool reordering, or an edited stable layer invalidates the cache every call), for ephemeral content inside cached blocks, or for a breakpoint anchored too shallow (short reusable prefix). If stale context is observed → confirm the update was appended as a `<system-reminder>`, not edited into the prefix; if the prefix was mutated, restore byte-identity and re-append. If `cache_control` is unsupported for a provider → drop the annotations and fall back to prefix-prefix-match caching on the same layered ordering; the template structure remains valid.
