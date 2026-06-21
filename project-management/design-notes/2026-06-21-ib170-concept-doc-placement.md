---
title: "IB-170 concept-doc placement — home rule + harness consolidation"
id: "ib170-concept-doc-placement"
type: "design-note"
category: "knowledge-architecture"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-06-21"
updated: "2026-06-21"
author: "claude"
source_ib:
  - "IB-170"
source_dd:
  - "DD-111"
  - "DD-104"
  - "DD-103"
tags:
  - "design-note"
  - "concept-docs"
  - "knowledge"
  - "librarian-substrate"
  - "rule-11"
  - "rule-12"
---

# IB-170 concept-doc placement

## The question (now that the two-bodies frame is settled)

IB-170's immediate symptom: concept docs split across two homes. With DD-111 settling the two-bodies
frame (`extracts/` = research substrate; `knowledge/` = engine self-knowledge), this note resolves the
*concept-doc* placement sub-case. **Spec only — no files move on this note** (IB-170: discuss-first,
Nick gates the taxonomy).

## Current state (verified session 126)

| Home | Contents |
|---|---|
| `operations/references/librarian/` | The concept docs: `skill.md`, `agent.md`, `prompt.md`, `memory.md`, `harness.md`, `second-brain.md`, `context-rot.md`, `agentic-systems.md`, plus mode/axis docs (`audit.md`, `design.md`, `coverage.md`, `decide.md`, `diagnose.md`, `explain.md`, `fetch.md`, `plan.md`, `mcp.md`, `prompt-caching.md`, `whats-new.md`) |
| `knowledge/reference/` | Engine self-knowledge: `fractal-pattern.md`, `vocabulary.md`, `dbdo-pipeline.md` — **plus** `harness.md` (the lone concept doc here) |

### The precise inconsistency — it is narrower than "concept docs are scattered"

Every middle-altitude concept doc unifies **§Composition + §Construction in one file** in
`operations/references/librarian/` (rule 12). The **harness concept is the sole exception**: its
§Construction lives in `knowledge/reference/harness.md` (230 lines, top-altitude framing) while a
separate `operations/references/librarian/harness.md` (97 lines) holds the audit-time §Composition
substrate. The `consumer-abstractions-map` documents this split as intentional (altitude-driven), but
it is the exact anomaly IB-170 named.

Worse, the two files are not clean halves of one concept — they describe **two related-but-distinct
things that share the name "harness":**

- `librarian/harness.md` — **harness-as-runtime-environment**: the CLI/IDE/API an agent operates
  *inside* (Claude Code, Cursor, the API). A middle-altitude configuration axis, sibling to
  skill/agent/prompt/memory.
- `knowledge/reference/harness.md` — **harness-as-whole-system**: the unit `/audit-artifacts` audits
  and `/design-harness` constructs (a fractal-unit system composing skills+agents+prompts). A
  top-altitude composition unit.

## The principle

**A concept doc's home is determined by WHAT IT IS, not by which altitude's operation consumes it.**
Altitude determines which operations *read* a doc (`/assess-*` vs `/audit-artifacts`); it should not
scatter the same class of artifact across two folders. Applying the two-bodies test (DD-111):

- `knowledge/reference/` = **engine self-knowledge** — how *this* engine is built/operates
  (fractal-pattern, vocabulary, DBDO pipeline; the curated engine patterns/schematics). Read-and-judge
  design-wisdom about the engine itself.
- `operations/references/` = **operational reference the engine's skills/agents consult at runtime** —
  concept docs (what a skill/agent/prompt/harness *is*, in general), rubrics, routing tables,
  dimensions, the consumer-abstractions-map.

Concept docs describe **external abstractions** the Librarian audits/designs *consumer* artifacts
against — they are not "how this engine is built." By the principle they belong in
`operations/references/`, **not** `knowledge/reference/`.

## Recommendation (gated)

1. **Adopt the home rule above** as the placement taxonomy: `knowledge/reference/` = engine
   self-knowledge; `operations/references/` = operational reference (incl. all concept docs). This is
   the minimum-viable taxonomy — it resolves the concrete split without inventing new buckets
   (Rule 11).
2. **Consolidate the harness concept into `operations/references/librarian/`**, removing the lone
   `knowledge/reference/harness.md` outlier. One harness concept doc, carrying both §Composition and
   §Construction like every other concept doc (Rule 12). ~3 live pointers to update
   (`consumer-abstractions-map.md`, and the map's two harness rows).
3. **Resolve the name collision** (the genuine content gate): the whole-system unit and the
   runtime-environment axis are distinct enough to need distinct names. Recommended: **keep `harness.md`
   for the whole-system unit** (the dominant, `/audit-artifacts`-/`/design-harness`-facing meaning) and
   **rename the runtime-environment axis → `runtime-environment.md`** (a cleaner name for "the surface
   an agent runs inside"). Alternative: merge into one `harness.md` with the runtime-env as a facet
   section — rejected, because the two are read by different operations and conflating them re-creates
   the ambiguity.
4. **Agent helper files (IB-170 item 2): no change.** Material under `agents/{name}/` that supports a
   disposition stays agent-scoped and agent-private; it is not shared concept-doc substrate. No
   evidence of confusion here — Rule 11: leave it, flag for revisit only if a concrete collision
   appears.

## Why not relocate concept docs into `knowledge/reference/` instead

The inverse move (pull all concept docs *into* `knowledge/`) fails the two-bodies test: concept docs
are about external abstractions, not engine self-knowledge, and they are consumed pull-style by the
Librarian's runtime operations — `operations/references/` is their natural home. Moving one file out of
`knowledge/` (recommendation 2) is far less churn than moving ~20 files into it.

## Open decisions for Nick (gates)

1. **Adopt the home rule** (knowledge/ = self-knowledge; operations/references/ = operational
   reference incl. concept docs)? — recommend **yes**.
2. **Consolidate `knowledge/reference/harness.md` → `operations/references/librarian/`** (one concept
   doc, both Contract halves)? — recommend **yes**.
3. **Name collision:** rename the runtime-env axis → `runtime-environment.md`, keep `harness.md` for
   the whole-system unit? — recommend **yes** (vs. merge).

## Cross-references

- DD-111 (two bodies: extracts substrate vs. knowledge self-knowledge — the frame this applies).
- DD-104 (three altitudes), DD-103 (single-engine collapse).
- `operations/references/consumer-abstractions-map.md` — documents the current altitude-driven harness
  split (to be updated if recommendations adopted).
- `2026-06-20-extracts-knowledge-reconciliation.md` — established that IB-170 is a sub-case of the
  two-bodies confusion.
- IB-170 — parent backlog item.
