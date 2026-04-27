---
name: "Content-Derived Temporal Expiration and Automatic Contradiction Resolution"
summary: "Third memory-decay strategy in the KB, alongside importance-based decay and surprisal-gated writes. (1) Parse date-references from content at write time ('I have an exam tomorrow' → extracted date + TTL), and auto-expire after the referenced date passes. (2) Detect contradictions between new and existing memories; resolve automatically via the Updates relationship (new memory marked `isLatest: true`; old retained with `isLatest: false`). Together: noise doesn't become permanent memory, and state evolves without manual cleanup."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: importance-based-decay-permanent-exemption.md
    rel: same-problem
  - file: surprisal-novelty-as-memory-write-gate.md
    rel: same-problem
  - file: typed-relationship-memory-graph.md
    rel: enables
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-27"
pipeline_status: classified
consumed_by: []
---

## What It Is

Two paired mechanisms for keeping a memory store coherent over time:

**1. Content-derived temporal expiration.** At write time, the extractor parses natural-language date references in the memory content. Examples:

- "I have an exam tomorrow" → extract `tomorrow` → compute `expiresAt = today + 1 day`.
- "Booking a flight for the 15th" → extract `15th` → compute `expiresAt = next 15th`.
- "Working on Q2 planning" → extract `Q2` → compute `expiresAt = end of Q2`.

After `expiresAt` passes, the memory is either soft-expired (hidden from retrieval unless explicitly queried for history) or hard-deleted (depending on policy). Unlike importance-based decay (Memongo's pattern), expiration is *content-derived* — the memory itself tells the system when it becomes irrelevant.

**2. Automatic contradiction resolution.** At write time, the extractor checks whether the new memory contradicts an existing one on the same subject. Examples:

- Existing: "User lives in NYC" + New: "I just moved to SF" → contradiction detected → Updates relationship created; NYC memory marked `isLatest: false`.
- Existing: "User prefers Vue" + New: "User now uses React" → Updates relationship created; Vue memory retained but flagged superseded.

The older memory is not deleted — it's retained as historical context. Queries can request latest-only (default) or full-history. The resolution mechanism is the Updates relationship from the [[typed-relationship-memory-graph]] finding; this pattern is about *what triggers* the relationship (semantic contradiction detection at write time).

Together, these mechanisms make the memory store self-maintaining. Noise (temporary facts, outdated state) doesn't accumulate. Contradictions don't require manual deconfliction.

## Why It Matters

Third strategy in the memory-decay design space:

| Strategy | Trigger | Behavior | Example |
|---|---|---|---|
| [[importance-based-decay-permanent-exemption]] (Memongo) | Importance score computed at write | Low-importance decays over wall-clock time; permanent/ongoing exempt | "I dislike pineapple" (low importance) → decays; "My wife's name is Anna" (permanent) → never |
| [[surprisal-novelty-as-memory-write-gate]] (Memongo) | Surprisal at write | Redundant agreement not written at all | "I like React" + "React is great" (high-agreement, low-surprisal) → skip |
| **Content-derived temporal expiration + contradiction resolution** (Supermemory) | **Parsed dates + semantic contradiction at write** | **Auto-expire on referenced date; supersede via Updates** | **"Exam tomorrow" → gone in 2 days; "now in SF" → NYC superseded** |

The three are complementary, not competing. A full memory system could use all three: surprisal to filter at write, content-derived expiration for time-referenced facts, importance-based decay for the rest. Directly relevant to Nick's active Memongo work and to any Household OS memory layer.

For the Household OS specifically: "I have a dentist appointment Thursday" is a time-scoped fact. Importance-based decay would treat it the same as any other low-importance fact. Content-derived expiration handles it naturally — the appointment reference is the expiration signal.

## Why People Are Using It

Observed in [Supermemory](https://github.com/supermemoryai/supermemory) latest — see [[supermemory-analysis]] for structural details. The pattern is declared in the README ("Automatic forgetting" block) and detailed in `skills/supermemory/references/architecture.md` §"Automatic forgetting" and §"Memory Versioning." Contradiction resolution is paired with the Updates relationship mechanic (`isLatest: true/false` flag). Production-deployed as part of Supermemory's SaaS offering; observable in their MCP server tool `memory` with action `save` (contradiction detection runs at write) and action `forget` (explicit expiration trigger).

## Potential Alternatives

- **TTL fields at write time.** Caller specifies `expiresAt` explicitly. Works when callers know the TTL; fails when the TTL is embedded in the content and not in the caller's context.
- **Importance-based decay only.** [[importance-based-decay-permanent-exemption]]. Handles the general case but not content-referenced time.
- **Manual curation.** Periodic human review flags stale memories. Doesn't scale past single-user systems.
- **Delete on read if stale.** Lazy expiration at query time. Storage accumulates; reads slow as history grows.
- **Append-only with query-time filter.** Keep everything; filter by current-date-relevant at query. Unbounded growth; slower reads.

## Potential Improvements

- **Confidence on extracted dates.** "I have an exam tomorrow" is clear; "I have an exam sometime this semester" is not. Low-confidence date extractions should prefer importance-based decay as the fallback.
- **Multi-date semantics.** "I'm at this conference Monday through Thursday" has a range, not a point. Range-based expiration needs explicit modeling.
- **Contradiction confidence threshold.** Two memories may appear contradictory to an extractor but actually coexist ("I live in NYC and SF" — bi-coastal). Low-confidence contradiction-detection should be human-gated rather than auto-resolved.
- **Combine with surprisal for writes** and **importance-based decay** for the no-content-date fallback. The three together map the decay design space.

## Potential Failure Modes

- **Extractor misses the date reference.** "My kid's birthday is next week" — if the extractor doesn't parse "next week," the memory never expires. Fallback to importance-decay or TTL.
- **False-positive contradiction detection.** Two memories tagged `contradicts` when they coexist (bi-coastal example). Resolution flips the wrong one to `isLatest: false`. User sees the wrong state.
- **Timezone mismatch.** "Tomorrow" is ambiguous without the user's timezone. Misparsed timezones silently mis-expire memories.
- **Ambiguous references.** "Q2" in one org means April-June; in another, July-September (fiscal year). Content-derived expiration with ambiguous references fires at wrong times.
- **Superseded-not-deleted bloat.** Every update creates a new memory and retains the old. Without a pruning layer, history grows unboundedly. Needs a separate pruning discipline (e.g., archive Updates chains older than N generations).
