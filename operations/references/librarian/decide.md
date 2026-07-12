---
operation: decide
type: operation
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "claude"
stage: "draft"
tags:
  - "librarian-operation"
  - "decide"
  - "decision-support"
aliases:
  - "Decide"
  - "Tradeoff"
  - "A vs B"
---

# Decide

## Short definition

**Decide** produces a tradeoff comparison between two or more options the consumer is weighing — "single-agent or multi-agent?"; "MongoDB single-store or triple-storage memory?"; "Claude Code or Cursor for this workflow?"; "Opus or Sonnet for a background review agent?". Input is the set of options plus (ideally) the consumer's priorities. Output is a tradeoff table with each axis cited from substrate, a `contradicts`-link surface when substrate carries the debate directly, and a recommendation only if the consumer asked for one or if the substrate points to a dominant answer.

Decide is a *consumption* operation: read-only; the Librarian does not decide *for* the consumer when the tradeoff is context-dependent. When the substrate dominates (e.g., role-mirroring decomposition is ruled out by G3 §Key Concept 3), the Librarian states that — but it never invents a preference the substrate does not support.

## Default composition rule

`decide` composes three inputs:

1. **Concept file(s)** for the noun(s) the options attach to — provides the composition table. For variant-carrying concepts (agent, memory, second-brain), decide usually compares *variants* or compares *within a variant* — e.g., UC-5.1 "single-agent or multi-agent" is a decision at the agentic-systems level, not the agent-variant level.
2. **Key Concepts subsections** of the named guides — the tradeoff axes. G3 §Key Concepts carries the single-agent vs multi-agent tradeoff; G7 §Key Concepts carries memory-architecture tradeoffs; G3b and G5 carry workflow/tool tradeoffs.
3. **Tier-2 `contradicts` pairs** — highest signal for decision queries. When substrate has a typed `contradicts` edge (e.g., `mongodb-single-store-polymorphic-evidence-memory` ↔ `triple-storage-memory-architecture`), the debate lives at Tier 2 and must surface proactively for UC-5.2-style queries.

Key Concepts sections function as emergent decision rubrics by construction — they were authored to distinguish tradeoffs. `contradicts` links function as substrate-native debate surfaces. Neither needs view-artifact curation.

### Composition details

**(a) Option enumeration.** The consumer names options; the Librarian does not silently add alternatives. If the substrate suggests an option the consumer omitted (e.g., consumer says "Opus or Sonnet?" and Haiku is viable), the Librarian surfaces the missing option as a clarifying note *before* producing the table.

**(b) Axis derivation.** Axes come from Key Concepts subsections and `contradicts` pair evidence — not from Librarian invention. Typical axes: cost, latency, accuracy, information-loss risk, governance cost, operational complexity, reversibility. If the substrate only covers two axes, the table has two axes — do not pad.

**(c) Tier-2 escalation is default for `contradicts`-bearing decisions.** UC-5.2, UC-5.3, UC-5.4 all have known design-debate substrate. Load Tier 2 proactively when the noun / aspect has `contradicts`-typed findings.

**(d) No recommendation without consumer ask or substrate dominance.** If the tradeoff is context-dependent and the consumer did not ask "what should I pick?", stop at the table. If the consumer asked, or if substrate rules out one side (G3 §Key Concept 3 rules out role-mirroring decomposition), state the dominant answer with the ruling-out citation.

## Procedure

Four phases.

### Phase 0 — Parse the query

Parse verb + noun(s) + options. Verb must be `decide` or a synonym ("A or B," "should I use," "when would I pick," "tradeoff between," "which one"). Nouns identify the concept(s); options are the named alternatives.

If options are named imprecisely ("multi-agent or not" — not vs *what*?), ask one clarifying question. If the consumer named only one option ("should I use X?") — "X versus what?" is the clarifying ask.

### Phase 1 — Load composition

Read the concept file(s) for the noun(s). Read `### Key Concepts` subsections of each guide named in the concept's composition table's tradeoff-relevant rows. Load Tier-2 `contradicts` findings proactively if the concept's depth-escalation default flags it (e.g., memory single-vs-multi-store; second-brain Variant C debates).

For cross-concept decisions (harness-level: "Claude Code vs Cursor"), load both concepts' composition tables and aggregate.

### Phase 2 — Build tradeoff table

Derive axes from the loaded Key Concepts + contradicts evidence. For each axis:
- State each option's position (qualitative — "high," "low," "variable — depends on X").
- Cite the source: `<guide>.md#<anchor>` for Tier 1, `<finding-slug>` for Tier 2.
- If substrate is silent on an axis the consumer cares about, state that explicitly ("Substrate does not cover <axis>; both options likely comparable but unverified").

Deduplicate overlapping axes: if G3 and G8 both carry model-selection invariants, collapse to a single row.

### Phase 3 — Surface debate (if applicable)

If Tier-2 `contradicts` pairs are in scope, add a "Design debate" subsection — quote the `Key insight` / `Mechanism` line from each side, cite both slugs, and state that they contradict. Do not paper over.

### Phase 4 — Recommendation pass (only if requested or dominant)

- **Consumer asked "what should I pick?"** — produce a recommendation anchored to the consumer's stated priorities and the substrate axes. State the reasoning explicitly (e.g., "you prioritized cost → Option B wins on cost axis").
- **Substrate dominance** — if one option is ruled out by substrate (invariant, Pitfall, contradicts-pair with consensus leaning), state the dominant answer with the ruling-out citation.
- **Otherwise** — stop at the table. "This depends on your priorities across <axes>; the table above lets you decide."

## Consumer input handling

Expected input: the options the consumer is weighing, and (ideally) at least one priority (cost-sensitive, latency-sensitive, governance-critical, etc.). If only options are provided, ask one clarifying question about priorities before producing the table — unprioritized tradeoff tables are rarely actionable.

If the consumer's options are a *variant* comparison within a single concept (memory Variant A vs Variant B), route through the concept file's variant selection — "these aren't really alternatives; they're tiers of one architecture. You probably want to decide Variant C vs D for the global-learnings layer specifically."

| Query shape | How to read |
|---|---|
| Architecture A vs B (UC-5.1) | `agent.md` (+ `agentic-systems.md`) + G3 §Key Concepts + `legitimate-multi-agent-domains-taxonomy` |
| Design debate on `<concept>` (UC-5.2) | Concept file + Tier-2 `contradicts` pair proactively |
| Harness A vs B (UC-5.3) | `harness.md` cross-guide thread + Tier-3 watched-lib pointers (consumer-request-gated) |
| Model A vs B (UC-5.4) | `agent.md` (model aspect) + G3.I4 / G8.I4 merged invariant + cost / latency / capability table |

## Output shape

```
## Decide — <option A> vs <option B> [vs …]

**Interpreted as:** (verb: decide, noun(s): <n>, options: <A, B, …>, priorities: <if stated>)
**Composed guides:** <list>
**Debate substrate:** <Tier-2 contradicts pair if applicable>

### Tradeoff table

| Axis | <Option A> | <Option B> | Source |
|---|---|---|---|
| Cost | … | … | G3 §Key Concepts §2 |
| Information-loss risk | … | … | `legitimate-multi-agent-domains-taxonomy` |
| … |

### Design debate (if substrate carries one)

<Brief: "Finding X says Y; Finding Z (contradicts X) says W. Both are in the KB because both have evidence; the debate is unresolved.">

### Missing coverage (if any)

<Axes the consumer likely cares about that the substrate does not cover.>

### Recommendation (only if requested or substrate-dominant)

<1-2 sentences: pick + reasoning anchored to priorities or ruling-out citation. Skip if table suffices.>
```

## Governance and boundaries

- Decide is **read-only on substrate**. The Librarian does not file DDs, modify findings, or update the KB.
- Decide does not invent axes the substrate does not support.
- Decide does not pad recommendations with general-knowledge reasoning when the KB is thin — state the gap instead.
- Decide does not smuggle `design` output into the response. If the consumer's follow-up is "OK I picked A, now build it," that's a `design` handoff.

## Cross-references

- Read-contract (Step 1 verb extraction, §8.5 input handling for decide): `operations/references/librarian/read-contract.md`.
- Related operations: `audit.md`, `design.md`, `explain.md` (this directory) — explain often precedes decide when the consumer doesn't yet understand the mechanism behind the tradeoff.
- Related concepts: `agent.md`, `agentic-systems.md`, `harness.md`, `memory.md`, `second-brain.md` (this directory).
- Use-case registry (UC-5.1–5.4): `operations/references/librarian/use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role — Key Concepts as emergent tradeoff rubrics), DD-82 (IL 4-agent architecture).
