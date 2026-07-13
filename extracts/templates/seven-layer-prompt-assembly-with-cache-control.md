---
title: "Seven-Layer Prompt Assembly with Cache-Control Annotations"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "layered-prompt-assembly-stable-segment-caching"
extraction_date: "2026-05-25"
last_change_session: 146
last_change_report: "2026-07-13-source-drift"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "multi-turn agent systems that assemble system prompts programmatically at each API call"
    - "prompt assembly modules for any agent with stable identity/memory and ephemeral task state"
    - "teams choosing where to place cache breakpoints in a tool-using, multi-turn prompt"
  platform_coupling: "specific:anthropic-claude"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — removing cache_control annotations requires updating prompt assembly code; no data migration needed, but cache hit rates drop immediately"
  auditability: "high — cache_control annotations are explicit in prompt assembly code; stable vs. ephemeral layer classification is documented in the template; cache-read vs. cache-write token counts are visible in API response usage"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Hermes agent (NousResearch) uses this architecture with a dedicated prompt_caching.py module; opencode ships an equivalent default-on policy that auto-places breakpoints at the last tool definition, last system part, and latest user message, with documented ~1.25x-write / ~0.1x-read economics. MetaSystem CLAUDE.md files are loaded as system context but not marked with cache_control. Design work required before implementation."
contract:
  preconditions: "An agent system makes multi-turn API calls to Anthropic Claude. A prompt assembly step constructs the system prompt before each call. The system has identifiable stable segments (identity, memory, skills) and ephemeral segments (task state, budget warnings, context pressure)."
  invariants: "Layers 1-5 (stable) are assembled in order and the last stable layer is marked with cache_control. Layer 7 (ephemeral) is never marked with cache_control. No ephemeral content is included in any cached block. Cache breakpoints are anchored at the deepest stable boundaries (last tool definition, last stable system part, and — for cross-turn read reuse — the latest user message); at most four breakpoints per Anthropic API limits. Layer order is preserved; stable layers never follow ephemeral layers in the assembled prompt."
  governance: "Owner of the prompt assembly module for each agent. Cache_control annotation placement is documented in code comments or adjacent spec. When stable layers change (e.g., new skill added to metadata), the cache boundary is reviewed. Ephemeral-to-stable reclassification requires explicit justification — semi-dynamic content marked as stable will serve stale context."
  recovery: "If cache hit rate is unexpectedly low → check whether ephemeral content is included in cached blocks (invalidates cache every call) or whether the breakpoint is anchored too shallow (short reusable prefix). If stale context is observed → review stable layer classification; over-caching semi-dynamic content is the likely cause. If cache_control is not supported for a provider → remove annotations and fall back to uncached layered assembly; template structure remains valid."
tags:
  - "extracted-artifact"
  - "template"
  - "prompt-engineering"
  - "context-engineering"
  - "caching"
  - "prompt-assembly"
---

# Seven-Layer Prompt Assembly with Cache-Control Annotations

**Source:** [[layered-prompt-assembly-stable-segment-caching]]
**Form:** template
**Extraction date:** 2026-05-25

## Variables

| Variable | Description | Stable? |
|----------|-------------|---------|
| `{{AGENT_ROLE}}` | Core role definition and persona statement | Yes |
| `{{SOUL_MD}}` | Global personality and behavioral principles (SOUL.md or equivalent) | Yes |
| `{{MEMORY_MD}}` | Persistent user/system facts (MEMORY.md) | Yes |
| `{{USER_MD}}` | User preferences and profile (USER.md) | Yes |
| `{{SKILLS_METADATA}}` | Skill titles and "When to use" summaries for relevant skills | Yes |
| `{{PROJECT_CONTEXT}}` | Project-specific context file (AGENTS.md, .hermes.md, CLAUDE.md) | Yes |
| `{{TOOL_DEFINITIONS}}` | Tool/function schemas sent with the request | Usually Yes |
| `{{PROVIDER_INSTRUCTIONS}}` | Provider-specific tool-calling format and constraints | Conditional |
| `{{EPHEMERAL_STATE}}` | Budget warnings, context pressure hints, session-specific flags | No |

**Stability classification:** Stable = changes infrequently (per deployment, not per call). Conditional = changes per provider but not per call within a session. Ephemeral = changes every call or every turn.

---

## Body

```
# Layer 1 — Core Role / Persona
{{AGENT_ROLE}}

---

# Layer 2 — Global Personality (SOUL.md)
{{SOUL_MD}}

---

# Layer 3 — Persistent Memory
## System Memory
{{MEMORY_MD}}

## User Profile
{{USER_MD}}

---

# Layer 4 — Skills Metadata
Available skills (titles and when-to-use summaries):
{{SKILLS_METADATA}}

---

# Layer 5 — Project Context
{{PROJECT_CONTEXT}}

[cache_control: {"type": "ephemeral"}]  ← BREAKPOINT: last stable system part

---

# Layer 6 — Provider Instructions
{{PROVIDER_INSTRUCTIONS}}

# (Tool definitions, if sent, carry their own breakpoint at the LAST tool def)
{{TOOL_DEFINITIONS}}  [cache_control on the last tool definition]

---

# Layer 7 — Ephemeral State
{{EPHEMERAL_STATE}}
```

**Cache boundary placement (opencode heuristic).** Anthropic supports up to four cache breakpoints; place them at the deepest reliably-stable boundaries rather than on a single arbitrary layer:

1. **Last tool definition** — tool schemas are usually stable across a session; anchor a breakpoint on the final tool def so the whole tool block is read-cached.
2. **Last stable system part** — the marker on Layer 5 (or the deepest stable layer present) caches identity + memory + skills + project context in one prefix.
3. **Latest user message** — for cross-turn reuse, a breakpoint at the most recent user turn lets the next call read-cache everything up to and including it.

Never mark Layer 7. The cached prefix should always extend as deep as stability allows; a breakpoint placed before a genuinely stable layer leaves cheap reads on the table.

---

## Usage

**When to use this template:**
- Building or refactoring a prompt assembly module for a multi-turn agent
- Auditing an existing prompt assembly for cache efficiency
- Designing a new agent with stable identity and ephemeral task state

**How to instantiate:**
1. Identify which layers are present for the agent (not all agents use all layers).
2. Classify each layer as stable, conditional, or ephemeral.
3. Assemble layers in order (stable → conditional → ephemeral). Never reverse this order.
4. Place `cache_control: {"type": "ephemeral"}` at the deepest stable boundaries — last tool definition, last stable system part, and (optionally) the latest user message — up to Anthropic's four-breakpoint limit.
5. Send ephemeral layers as separate content blocks without cache markers.

**Why default-on pays (opencode economics).** A cache *write* costs roughly 1.25× base input tokens; a cache *read* costs roughly 0.1×. A cached prefix therefore breaks even once it is read about 1.4 times — a threshold every multi-turn session clears — which is why opencode ships caching default-on rather than per-feature opt-in. The template's payoff scales with how deep the stable prefix runs, so anchoring breakpoints at the last stable boundary (not a shallow one) maximizes the reusable prefix.

**Anthropic API implementation note:** Cache control is set on individual content blocks in the `system` parameter array (and on tool definitions), not as a top-level field. The last block with `cache_control` set defines that breakpoint's boundary — all content up to and including it is cached.

```python
# Example: prompt_caching.py module (schematic)
def assemble_system_prompt(agent_role, soul, memory, user, skills, project,
                           tool_defs, provider_instructions, ephemeral):
    stable_blocks = [
        {"type": "text", "text": agent_role},
        {"type": "text", "text": soul},
        {"type": "text", "text": memory + "\n" + user},
        {"type": "text", "text": skills},
        {"type": "text", "text": project, "cache_control": {"type": "ephemeral"}},  # breakpoint: last stable system part
    ]
    # tool_defs carry their own breakpoint on the last definition
    dynamic_blocks = [
        {"type": "text", "text": provider_instructions},
        {"type": "text", "text": ephemeral},
    ]
    return stable_blocks + dynamic_blocks
```

---

## Variation Axis

| Scenario | Adjustment |
|----------|------------|
| Agent has no SOUL.md | Collapse Layer 2 into Layer 1; breakpoint moves with the last stable layer |
| Skills are session-variable (selected per task) | Reclassify Layer 4 as conditional; move the system breakpoint to Layer 3 |
| Agent sends tool definitions | Add a dedicated breakpoint on the last tool definition (opencode heuristic); this is independent of the system-part breakpoint |
| Provider instructions are stable for the session | Include Layer 6 inside the cached prefix; move the system breakpoint to Layer 6 |
| Long multi-turn conversation | Add a breakpoint at the latest user message for cross-turn read reuse (up to Anthropic's four-breakpoint limit) |
| Single-turn use (no cache benefit) | Remove cache_control annotations; the first write costs ~1.25× with no read to amortize it; layer order and content remain valid |
| Non-Anthropic provider | Remove cache_control annotations entirely; template structure is provider-agnostic otherwise |
| MetaSystem agents (CLAUDE.md as project context) | Layer 5 = CLAUDE.md content; Layer 7 = session state, task assignments, progress updates |

---

## Contract

### Preconditions
An agent system makes multi-turn API calls to Anthropic Claude. A prompt assembly step constructs the system prompt before each call. The system has identifiable stable segments (identity, memory, skills) and ephemeral segments (task state, budget warnings, context pressure).

### Invariants
Layers 1-5 (stable) are assembled in order and the last stable layer is marked with cache_control. Layer 7 (ephemeral) is never marked with cache_control. No ephemeral content is included in any cached block. Cache breakpoints are anchored at the deepest stable boundaries (last tool definition, last stable system part, and — for cross-turn read reuse — the latest user message); at most four breakpoints per Anthropic API limits. Layer order is preserved: stable layers never follow ephemeral layers in the assembled prompt.

### Governance
Owner of the prompt assembly module for each agent. Cache_control annotation placement is documented in code comments or adjacent spec. When stable layers change (new skill added, SOUL.md updated), the cache boundary is reviewed. Ephemeral-to-stable reclassification requires explicit justification.

### Recovery
If cache hit rate is unexpectedly low → check whether ephemeral content is included in cached blocks (invalidates cache every call) or whether the breakpoint is anchored too shallow (short reusable prefix). If stale context is observed → review stable layer classification; over-caching semi-dynamic content is the likely cause. If cache_control is not supported → remove annotations and fall back to uncached layered assembly; template structure remains valid.
