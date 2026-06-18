---
title: "Seven-Layer Prompt Assembly with Cache-Control Annotations"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "layered-prompt-assembly-stable-segment-caching"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "multi-turn agent systems that assemble system prompts programmatically at each API call"
    - "prompt assembly modules for any agent with stable identity/memory and ephemeral task state"
  platform_coupling: "specific:anthropic-claude"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — removing cache_control annotations requires updating prompt assembly code; no data migration needed, but cache hit rates drop immediately"
  auditability: "high — cache_control annotations are explicit in prompt assembly code; stable vs. ephemeral layer classification is documented in the template"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Hermes agent (NousResearch) uses this architecture with a dedicated prompt_caching.py module. MetaSystem CLAUDE.md files are loaded as system context but not marked with cache_control. Design work required before implementation."
contract:
  preconditions: "An agent system makes multi-turn API calls to Anthropic Claude. A prompt assembly step constructs the system prompt before each call. The system has identifiable stable segments (identity, memory, skills) and ephemeral segments (task state, budget warnings, context pressure)."
  invariants: "Layers 1-5 (stable) are assembled in order and the last stable layer is marked with cache_control. Layer 7 (ephemeral) is never marked with cache_control. No ephemeral content is included in any cached block. Layer order is preserved; stable layers never follow ephemeral layers in the assembled prompt."
  governance: "Owner of the prompt assembly module for each agent. Cache_control annotation placement is documented in code comments or adjacent spec. When stable layers change (e.g., new skill added to metadata), the cache boundary is reviewed. Ephemeral-to-stable reclassification requires explicit justification — semi-dynamic content marked as stable will serve stale context."
  recovery: "If cache hit rate is unexpectedly low → check whether ephemeral content is included in cached blocks (invalidates cache every call). If stale context is observed → review stable layer classification; over-caching semi-dynamic content is the likely cause. If cache_control is not supported for a provider → remove annotations and fall back to uncached layered assembly; template structure remains valid."
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

[cache_control: {"type": "ephemeral"}]  ← CACHE BOUNDARY: mark the last stable layer

---

# Layer 6 — Provider Instructions
{{PROVIDER_INSTRUCTIONS}}

---

# Layer 7 — Ephemeral State
{{EPHEMERAL_STATE}}
```

**Cache boundary placement:** The `cache_control` marker goes on the last stable content block (Layer 5 in the default configuration). If Layer 6 is also stable for a given session, move the marker to Layer 6. Never mark Layer 7.

---

## Usage

**When to use this template:**
- Building or refactoring a prompt assembly module for a multi-turn agent
- Auditing an existing prompt assembly for cache efficiency
- Designing a new agent with stable identity and ephemeral task state

**How to instantiate:**
1. Identify which layers are present for the agent (not all agents use all seven).
2. Classify each layer as stable, conditional, or ephemeral.
3. Assemble layers in order (stable → conditional → ephemeral). Never reverse this order.
4. Place `cache_control: {"type": "ephemeral"}` on the final stable content block in the Anthropic API call.
5. Send ephemeral layers as separate content blocks without cache markers.

**Anthropic API implementation note:** Cache control is set on individual content blocks in the `system` parameter array, not as a top-level field. The last block with `cache_control` set defines the cache boundary — all content up to and including that block is cached.

```python
# Example: prompt_caching.py module (schematic)
def assemble_system_prompt(agent_role, soul, memory, user, skills, project, provider_instructions, ephemeral):
    stable_blocks = [
        {"type": "text", "text": agent_role},
        {"type": "text", "text": soul},
        {"type": "text", "text": memory + "\n" + user},
        {"type": "text", "text": skills},
        {"type": "text", "text": project, "cache_control": {"type": "ephemeral"}},  # cache boundary
    ]
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
| Agent has no SOUL.md | Collapse Layer 2 into Layer 1; cache boundary moves with last stable layer |
| Skills are session-variable (selected per task) | Reclassify Layer 4 as conditional; move cache boundary to Layer 3 |
| Provider instructions are stable for the session | Mark Layer 6 with cache_control instead of Layer 5 |
| Single-turn use (no cache benefit) | Remove cache_control annotations; layer order and content remain valid |
| Non-Anthropic provider | Remove cache_control annotations entirely; template structure is provider-agnostic otherwise |
| MetaSystem agents (CLAUDE.md as project context) | Layer 5 = CLAUDE.md content; Layer 7 = session state, task assignments, progress updates |

---

## Contract

### Preconditions
An agent system makes multi-turn API calls to Anthropic Claude. A prompt assembly step constructs the system prompt before each call. The system has identifiable stable segments (identity, memory, skills) and ephemeral segments (task state, budget warnings, context pressure).

### Invariants
Layers 1-5 (stable) are assembled in order and the last stable layer is marked with cache_control. Layer 7 (ephemeral) is never marked with cache_control. No ephemeral content is included in any cached block. Layer order is preserved: stable layers never follow ephemeral layers in the assembled prompt.

### Governance
Owner of the prompt assembly module for each agent. Cache_control annotation placement is documented in code comments or adjacent spec. When stable layers change (new skill added, SOUL.md updated), the cache boundary is reviewed. Ephemeral-to-stable reclassification requires explicit justification.

### Recovery
If cache hit rate is unexpectedly low → check whether ephemeral content is included in cached blocks (invalidates cache every call). If stale context is observed → review stable layer classification; over-caching semi-dynamic content is the likely cause. If cache_control is not supported → remove annotations and fall back to uncached layered assembly; template structure remains valid.
