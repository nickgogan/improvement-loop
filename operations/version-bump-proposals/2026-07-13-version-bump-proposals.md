---
type: "version-bump-proposals-report"
target_system:
  - "improvement-loop"
generated_by: "/extract-artifacts"
date: "2026-07-13"
identification_report: "defending-agent-context.harvest-queue.md::append-only-context-updates-system-reminder-injection::template::static-first-prompt-layering-stack; session-persistence-and-memory.harvest-queue.md::append-only-lesson-store-owning-surface-identity::template::lesson-store-entry-schema"
total_template_candidates: 2
proposals_emitted: 2
no_match_passthrough: 0
---

# Version-Bump Proposals — 2026-07-13

Two template candidates scanned across two harvest-queue promotion runs (session 146). The DD-100 Branch A corpus scan of `extracts/templates/` found a semantic match for each; two proposals emitted, zero no-match pass-throughs. Sources: `defending-agent-context.harvest-queue.md` (row `append-only-context-updates-system-reminder-injection::template::static-first-prompt-layering-stack`) and `session-persistence-and-memory.harvest-queue.md` (row `append-only-lesson-store-owning-surface-identity::template::lesson-store-entry-schema`). This report proposes only — no versioned template is written until Nick rules per DD-100 §Rules #4.

## Proposals

### append-only-context-updates-system-reminder-injection

**Form:** template
**Existing template (primary match):** [[seven-layer-prompt-assembly-with-cache-control]] (current version: v1)
**Secondary matches:** none

**Proposed filename:** `seven-layer-prompt-assembly-with-cache-control-v2.md`

**Codifier recommendation:** version-bump

**Why this match:** Both templates codify the same abstraction — a layered prompt-assembly stack ordered stable/static-content-first so the shared prefix survives across turns for cache preservation. The KB itself marks the two source findings as related with `rel: same-problem` (`append-only-context-updates-system-reminder-injection` ↔ `layered-prompt-assembly-stable-segment-caching`). The existing v1 already carries the layers the four-layer stack names (identity/memory, skills metadata, project context = CLAUDE.md, ephemeral state = messages/session) and even a "MetaSystem agents (CLAUDE.md as project context)" variation-axis row. The candidate is the harness-native expression of the same stack.

**Diff sketch:**

The candidate finding evolves v1 along three structural axes; folding them produces v2:

1. **Add a harness-scope cache-tier column to the Variables/Stability table.** v1 classifies layers only as stable/conditional/ephemeral. The four-layer static-first stack adds the *cache-scope tier* the Claude Code harness uses — global (system prompt & tool definitions, cached across sessions) → project (CLAUDE.md) → session (session context) → turn (conversation messages). Add a "Cache scope" column mapping each layer to global/project/session/turn.
2. **Add an "Append-only update discipline" section to the Body/Usage.** v1's invariants stop at "no ephemeral content in cached blocks." The candidate adds the load-bearing companion rule: when content in a stable/cached layer goes stale mid-session (timestamps, changed files, mode toggles), it is *never edited in place* — the update is injected as a `<system-reminder>` block into a later message or tool result. Add this as a new Usage subsection and a new invariant ("stale prefix content is countermanded via appended messages, never edited"). Cross-reference the rule extract `[[never-mutate-cached-prompt-prefix]]`.
3. **Add a provider-agnostic four-layer default to the Variation Axis.** v1 is `platform_coupling: specific:anthropic-claude` (cache_control content blocks). Add a variation-axis row: a harness-agnostic four-layer collapse (system+tools / project-memory / session / messages) with no cache_control annotations, for harnesses whose provider caches by prefix-prefix-match rather than explicit markers. This broadens v1's coupling toward `agnostic` for the conceptual layering while keeping the cache_control implementation as one instantiation.

**Notes:** Altitude nuance for the gate — v1 is an API implementation scaffold (content blocks + cache_control + a `prompt_caching.py` schematic); the candidate is a conceptual layering model at harness scope. If Nick judges the altitude gap large enough, "create new" (a distinct conceptual-model template) is the alternative to version-bump. Recommendation leans version-bump because v1 already spans both altitudes via its variation axis and MetaSystem row.

### append-only-lesson-store-owning-surface-identity

**Form:** template
**Existing template (primary match):** [[skill-self-improvement-lessons-log-template]] (current version: v1)
**Secondary matches:** none

**Proposed filename:** `skill-self-improvement-lessons-log-template-v2.md`

**Codifier recommendation:** create new (false positive)

**Why this match:** Both are markdown-native lesson-record templates in the self-improvement/memory domain, and the existing template's Variant B (a companion `learning.md` journal written by a dedicated improvement-loop agent) is the nearest neighbor to the candidate's central store — same "durable lesson record maintained by an improvement process" shape. The DD-100 loose corpus scan flags this thematic overlap; it is the only lessons-domain template in `extracts/templates/`.

**Diff sketch:**

The candidate does NOT cleanly evolve the existing template's scaffold — the two differ at the backbone, which is why the recommendation is create-new rather than version-bump. Structural divergences:

1. **Unit of record.** v1 is *per-skill* (one lessons record co-located with each skill file; identity = the skill). The candidate is a single *central, cross-cutting* store (`ops/self/lessons.md`) whose entry identity is the pair `(owning surface, failure pattern)` — the workspace path that, if edited, prevents recurrence. Different keying model.
2. **Entry schema.** v1's entry is a 4-column table row `| Date | Session | What happened | Rule change |` (Variant A) or a free-form journal round (Variant B). The candidate's entry is a headed block `## L-<seq> · <date> · <high|normal> · <open|promoted|declined|pruned>` with required fields Lesson / Owning surface / Source (session ref, commit sha, or artifact path — at least one) / Occurrences. Monotonic `L-<seq>` IDs never reused.
3. **Lifecycle + dedup.** v1 has no formal status enum and no recurrence-dedup. The candidate adds a closed status lifecycle (`open → promoted|declined`, `open|declined → pruned`) and an occurrence-dedup rule (a recurrence appends a date to the existing entry's Occurrences list, never a second entry).

**Notes:** Recommendation is **create new (false positive)** — the candidate is a distinct object (central operational lesson STORE with owning-surface identity, status lifecycle, and occurrence-dedup) that would coexist with the per-skill lessons LOG template, not supersede it. Surfaced per DD-100's loose-calibration bias (surface plausible domain overlap rather than silently land a second lessons-template). If Nick concurs, re-invoke `/extract-artifacts --harvest-row append-only-lesson-store-owning-surface-identity::template::lesson-store-entry-schema` to write the new baseline template (no version suffix). If Nick instead rules version-bump, the proposed `-v2.md` filename above applies.
