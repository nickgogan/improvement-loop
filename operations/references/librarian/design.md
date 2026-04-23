---
operation: design
type: operation
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "claude"
stage: "draft"
tags:
  - "librarian-operation"
  - "design"
  - "build"
aliases:
  - "Design"
  - "Build"
  - "How should I design"
---

# Design

## Short definition

**Design** produces step-by-step guidance for building an artifact or architecture the consumer hasn't built yet. Input is a design intent — "how should I design my agent's context files," "how should I sequence the tool registry for my harness-based agent," "what should my agent's memory architecture look like." Output is an ordered step list composed from the `### Procedure` / `### Step N` subsections of the relevant guide(s), with templates and examples pulled inline where available, and any preconditions flagged that the consumer has not yet committed to.

Design is a *consumption* operation: read-only on substrate; the Librarian does not author the consumer's artifact, does not write to the KB, and does not propose deploys. Design produces the recipe; the consumer follows it.

Design and audit are siblings. Audit applies invariants *retroactively* to an existing artifact; design applies the authored build sequence *prospectively* to an artifact-to-be. The composition table for an artifact type is shared — the same concept file (e.g., `agent.md`) routes both operations to the same guide set; they differ in *which subsection kind* they read (audit reads `### Contract`; design reads `### Procedure` / `### Step N`).

## Default composition rule

`design` composes three inputs:

1. **Concept file** for the artifact (or concept) under design — provides the composition table. For variant-carrying concepts (agent, memory, second-brain), variant selection happens before composition; the variant narrows the guide set (e.g., Variant A of agent pulls {G1, G2, G3, G10}; Variant B adds {G3b, G5, G6}; Variant C adds {G7, G9}).
2. **Step subsections** of the named guides — specifically:
   - `### Procedure` (or `### Step N` sequences where the guide is step-structured) → the ordered build sequence. This is the spine of the response.
   - `### Preconditions` (from the guide's Contract) → applicability gates. If a Precondition is not satisfied in the consumer's scenario, flag it; if it *cannot* be satisfied, the guide is wrong-tool and the Librarian says so.
   - `### Templates` and `### Examples` → lifted inline as scaffolds when the consumer's scenario matches a template's variables or an example's shape.
3. **Cross-concept dependencies (for UC-9.2 cross-concept design)** — when the design spans two concepts (agent + second-brain, memory + harness), load both concept files and surface the aspects where they interact or disagree.

Procedure sections function as emergent build specifications by construction — they were authored as end-directed playbooks. The Librarian re-orders / filters based on the consumer's scenario but does not re-derive the build sequence.

### Composition details

**(a) Aspect scoping.** Most design queries name an aspect ("design the tool registry," "design my context files") rather than the whole artifact. Scope the read to the aspect's Step subsections first — e.g., "tool registry" → G5 §Procedure §Step on tool registry. When the consumer asks at whole-artifact level (UC-1.2: "how should I design my agent?"), read the cross-guide thread across the variant's composed guide set, ordered lifecycle-first (specify → build → verify → secure → operate).

**(b) Precondition gating.** Before returning the design, walk the composed guides' Preconditions against the consumer's scenario. For each Precondition:
- **Already satisfied** — silent; proceed.
- **Satisfiable but not yet committed** — flag for the consumer ("G2 assumes you've decided on a context-budget ceiling; if you haven't, decide first or the G2 steps will be under-constrained").
- **Unsatisfiable** — the guide is wrong-tool. State this and suggest the right guide/concept.

**(c) Template and example embedding.** Where the guide has `### Templates` (G1, G2, G3, G3b, G5, G7, G10 all carry them) or `### Worked Examples` (G1, G2, G3, G7 carry these), lift the specific section that matches the consumer's scenario. For agent.md scaffolding, G10's Core Truths / Boundaries / Vibe / Continuity template is canonical; for context files, G2's Tiered CLAUDE.md template is canonical. Do not dump the template wholesale — fill in the variable slots the consumer has committed to and leave `{{REMAINING}}` placeholders visible.

**(d) Variant overlay.** For variant-carrying concepts, the design composition reads the variant's *specific* guide union — not the full concept-file guide set. A Variant A (prompt-based) agent design does not pull G5 / G6 / G9 unless the consumer's scenario invokes them. This keeps designs scoped; over-inclusion of guides dilutes the step sequence.

**(e) Cross-concept dependency surfacing.** For UC-9.2-style cross-concept designs ("agent + hybrid second brain — in what order?"), load both concept files and produce *sequenced* steps, not two parallel lists. Dependency order typically follows: intent → architecture → components → safety → operations. Flag explicitly where one concept's decision constrains another's (e.g., "choose Variant C second-brain before committing to Variant B agent — hybrid curation requires HITL scaffolding in the agent spec").

## Procedure

Four phases. The Librarian executes top-to-bottom and produces a single design response. Do not stream partial steps mid-phase.

### Phase 0 — Parse the query

Parse verb + noun(s). Verb must be `design` or a synonym ("how should I build," "how do I set up," "recommend an approach for," "architect"). Noun identifies the artifact / concept under design; the aspect (if named) narrows the scope.

If the consumer has not stated at least one constraint (deployment target, team size, existing infrastructure, autonomy envelope), ask *one* qualifying question before composing. Unconstrained design requests produce generic step lists that the consumer must rediscover how to apply.

### Phase 1 — Load composition

Read the concept file(s) for the noun(s). For variant-carrying concepts, resolve the variant from the consumer's phrasing (re-using the variant selection heuristics in the concept file). Read the `### Procedure` / `### Step N` subsections of each guide named in the concept's composition table's design-relevant rows, plus `### Preconditions` from the Contract, plus the `### Templates` and `### Worked Examples` sections if the consumer's scenario is template-shaped.

Do not read full guide bodies — only the aspect-relevant steps plus preconditions / templates / examples.

### Phase 2 — Scope and gate

Apply composition steps (a), (b), (d), and (e): aspect-scope the step list; walk Preconditions against the consumer's scenario; apply variant overlay; surface cross-concept dependencies if applicable.

Emit a *scoped* step sequence — not the guide's full procedure, but the subset relevant to the consumer's aspect + scenario. Include the precondition flags as a prelude to the step list.

### Phase 3 — Lift templates and examples

Walk the step list. For each step that has a `### Templates` or `### Worked Examples` entry in the source guide, lift it inline with the consumer's named variables substituted. Keep the `{{placeholder}}` pattern for slots the consumer has not committed to — explicit placeholders are better than invented defaults.

If the consumer's scenario does not match any template or example, proceed without embedding — do not invent templates.

### Phase 4 — Tier + provenance + next-step pass

- Every step cites its source guide section. Format: `<guide>.md#<anchor>` (heading-match fallback until the section manifest lands). Tier 1 is the default; escalate to Tier 2 patterns only when:
  - A step's guidance has known design-debate substrate (memory single-store vs triple-storage, single-agent vs multi-agent architecture) — surface the debate via `contradicts` links proactively when the step hinges on the disputed choice.
  - The step involves the Agentic Systems or Memongo pattern clusters — practitioner patterns there are load-bearing depth beyond guide summary.
- **Design does not silently escalate to Tier 3.** If the consumer wants a reference-implementation comparison (e.g., "show me how Claude Code does this"), they ask explicitly — then Tier 3 fires per read-contract §Step 5.
- Attach **next-step suggestions** at the end: audit the built artifact when done (hand off to `audit`); re-design-mode after the first increment if the scenario evolved; planning for multi-phase builds (hand off to `plan`, planned).

## Consumer input handling

The consumer submits a design intent inline. Expected shape:

- **What they're building.** Artifact or concept (agent, skill, second-brain, memory architecture, etc.).
- **Aspect, if any.** Tool registry, context files, workflow, permissions, retrieval strategy, etc.
- **At least one constraint.** Deployment target (CLI agent vs API agent vs cursor agent), team size, existing infrastructure, autonomy envelope, budget. If none provided, ask one clarifying question before composing.

If the consumer provides an existing partial artifact alongside the design question ("here's what I have so far"), treat the artifact as scenario grounding — *not* as input for audit. Design from the artifact's stated intent forward; the consumer can request an audit separately.

Scoping heuristics:

| Query shape | How to read |
|---|---|
| Aspect-named (UC-1.1, UC-1.3: "design my agent's context files / tool registry") | Read the aspect's Step subsection from the single relevant guide; lift template if present. |
| Whole-artifact, variant-resolvable (UC-1.2: "design my agent" + context that resolves variant) | Cross-guide thread ordered lifecycle-first, pulled from the variant's guide union. |
| Variant-ambiguous (UC-1.5: "what should my agent's memory architecture look like") | Read concept file's architecture-level overview (G7 §Key Concepts + §Part 1 for memory); ask whether the consumer wants per-tier depth next. |
| Cross-concept (UC-9.2: "agent + hybrid second brain — in what order") | Load both concept files; produce sequenced steps with dependency flags. |
| Debate-surfacing (UC-1.4: "hybrid second brain my agent curates" — second-brain Variant C, which carries HITL design debate) | Step list + Tier-2 `contradicts` pair if the debate affects a step's choice. |

## Output shape

```
## Design — <artifact or concept under design>

**Interpreted as:** (verb: design, noun(s): <n> [variant: <var>], aspect: <aspect or "whole artifact">)
**Composed guides:** <list; variant-scoped>
**Precondition check:** <brief — all satisfied | N flagged | wrong-tool redirect>

### Preconditions (flagged if not yet committed)

<Only the flagged ones. Short — "decide X before Step N"; cite the guide's Precondition line.>

### Design steps

1. **<Step title>.** <1-2 lines of guidance.> *Source:* G<N>.md#<anchor>. *Template/example (if lifted):* <inline or pointer>.
2. …

### Design debates surfaced (if any)

<Tier-2 `contradicts` pair(s) that bear on a step's choice, with a one-line summary of each side. Cite by slug.>

### Cross-concept dependencies (if applicable)

<Surfaced when the design spans two concepts; order dependencies first.>

### Next-step suggestions

<Audit after build; hand off to plan for multi-phase builds; re-design-mode after increment 1.>
```

## Governance and boundaries

- Design is **read-only on substrate**. The Librarian does not author the consumer's artifact, does not write to the KB, and does not deploy anything.
- Design does not apply rubric criteria — that is audit's job. If the consumer blurs the two ("design and evaluate"), produce the design first and offer the audit handoff separately (per read-contract §1.1 on blended verbs).
- Design does not silently pick variant or aspect when the consumer's phrasing is ambiguous. One clarifying question is allowed; more than that is interrogation.
- Design does not invent templates or examples. If the guide has none, state it — do not fabricate.

## Cross-references

- Read-contract (Step 1 verb extraction, §8.5 input handling for design): `project-management/design-notes/2026-04-21-librarian-read-contract.md`.
- Related operations: `audit.md` (this directory) — sibling composition; `plan.md` (planned) — lifecycle-sequenced version of design for multi-phase builds.
- Related concepts: `agent.md`, `memory.md`, `context-rot.md`, `skill.md`, `prompt.md`, `harness.md`, `second-brain.md` (this directory).
- Use-case registry (UC-1.1–1.5): `project-management/design-notes/2026-04-21-librarian-use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role — Procedure as authored build sequence), DD-82 (IL 4-agent architecture).
