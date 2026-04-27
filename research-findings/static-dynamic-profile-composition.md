---
name: "Static + Dynamic User Profile Composition in One API Call"
summary: "At write time, each memory is flagged `isStatic: true` (permanent — name, role, preferences) or `isStatic: false` (ephemeral — recent activity, current project). A single profile API call composes both layers into a response shape `{ profile: { static: [...], dynamic: [...] } }` in ~50ms. The split formalizes 'identity context' vs 'state context' at the storage API layer rather than leaving it to consumer code."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: null
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: typed-relationship-memory-graph.md
    rel: enables
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-27"
pipeline_status: raw
consumed_by: []
---

## What It Is

A two-layer profile shape returned by a single API call:

```
client.profile({ containerTag: "user_123", q: "..." })
→ {
    profile: {
      static:  [ "Senior engineer at Acme", "Prefers dark mode", "Uses Vim" ],
      dynamic: [ "Working on auth migration", "Debugging rate limits" ]
    },
    searchResults: [ ... ]
  }
```

Each memory carries an `isStatic: bool` flag at write time. Static memories are permanent facts — identity, long-term preferences, stable attributes. Dynamic memories are time-weighted and reflect current context. The profile endpoint composes them into separate lists; system prompts typically inject both with different preambles ("User Profile: ..." vs "Recent Context: ...").

The architectural distinction: *what the user IS* (static) vs *what the user IS DOING* (dynamic). Both are always returned; consumers decide how to present them.

## Why It Matters

Our session-handoff prompts already do this implicitly — the "Project context" section carries identity-shaped facts, and the "Context from prior session" section carries state-shaped facts. Formalizing the split at the storage API layer has three advantages:

1. **Reusable shape.** Any agent or skill querying user context gets the same structure back; no per-consumer logic for "what's permanent vs recent."
2. **Retrieval priority can differ.** Static memories can get retrieval priority (they always matter); dynamic memories get time-weighting (recent-first). The split lets the storage optimize without consumers hand-tuning it.
3. **Governance surface.** User-facing "what does this system know about me?" views can show `static` (long-term retention, audit) separately from `dynamic` (ephemeral, auto-expired).

Directly relevant to:
- **Household OS** — household members have stable attributes (name, allergies, school schedule) and ephemeral state (current projects, recent conversations). This shape fits natively.
- **IL agents** — agent reflections have stable character (disposition, scope) and recent observations (what this week's session uncovered). Same split.
- **Session handoffs** — we can formalize the two sections and generate the handoff from the profile API rather than hand-authoring.

## Why People Are Using It

Observed in [Supermemory](https://github.com/supermemoryai/supermemory) latest — see [[supermemory-analysis]] for structural details. The `isStatic: true` flag is documented in `skills/supermemory/SKILL.md` §"Best Practices" ("Mark permanent facts as isStatic: true for better performance") and in `skills/supermemory/references/architecture.md` §"Static vs Dynamic Memories." The profile endpoint is the canonical call for agents consuming user context — Supermemory's SKILL recommends calling `profile()` before every response and injecting both layers into the system prompt. Used by every plugin in their ecosystem (`claude-supermemory`, `openclaw-supermemory`, etc.).

## Potential Alternatives

- **Flat memory with time-decay only.** No static flag; every memory decays based on recency. Simpler, but permanent facts get pushed out by noise.
- **Separate stores for identity vs state.** Two databases, two queries. Stricter separation but loses the single-call efficiency.
- **Tag-based filtering.** `type: identity` / `type: state` tags with filter-at-query. Functionally equivalent but loses the first-class API semantic.
- **System-prompt-level split by agent logic.** Agents categorize memories into static/dynamic at read time. Works but requires per-consumer logic.

## Potential Improvements

- **Third layer — `seasonal`.** Memories that are neither permanent nor ephemeral (e.g., "working from Lisbon for the next 3 months") don't fit cleanly in either bucket. A third tier with explicit valid-window could close the gap.
- **Auto-promotion from dynamic to static.** When a dynamic memory appears consistently across many sessions (e.g., "mentions preferring TypeScript" 10 times across a month), auto-promote to static. Requires heuristic + confirmation.
- **User-facing edit surface.** Expose the static list as a user-editable "About Me" view; let users correct the system's inferences directly.

## Potential Failure Modes

- **Mis-tagged at write time.** If the extractor flags a temporary fact as static ("User is stressed about deadline tomorrow"), it persists incorrectly. Needs either an extractor confidence threshold or a user-facing correction path.
- **Stale static memories.** A user changes jobs; old "Senior engineer at Acme" is still `isStatic: true`. The contradiction-resolution pattern (see [[content-derived-temporal-expiration-contradiction-resolution]]) must work at the static tier too, not only dynamic.
- **Over-reliance on the split.** Some facts are genuinely ambiguous — "prefers dark mode" is static-ish, "prefers dark mode this week because bright light is bothering my eyes" is dynamic. The binary flag forces a choice; a confidence score or seasonal tier would help.
- **Response-shape lock-in.** The `{ static: [], dynamic: [] }` shape is simple but not all consumers want both — some just want a single ranked list. A flag parameter to collapse would help flexibility.
