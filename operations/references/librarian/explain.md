---
operation: explain
type: operation
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "claude"
stage: "draft"
tags:
  - "librarian-operation"
  - "explain"
  - "mechanism"
aliases:
  - "Explain"
  - "Why does X"
  - "What is X"
  - "Mechanism"
---

# Explain

## Short definition

**Explain** produces a mechanism + evidence response to a "why" or "how does this work" question — "why does context rot happen?"; "why do agent Contracts need Preconditions?"; "why does prompt caching reduce cost so dramatically?". Input is a topic / phenomenon. Output is a short narrative grounded in the relevant guide's `### Key Concepts` and, where load-bearing, the pattern or finding that carries the mechanism at one layer deeper than the guide's summary.

Explain is a *consumption* operation: read-only on substrate; the Librarian does not speculate beyond the substrate. When the KB covers the mechanism partially, Explain states what's covered + what's inferred + what's not known. Padding from training data is forbidden.

## Default composition rule

`explain` composes two inputs:

1. **Concept file** for the topic being explained — provides the composition table pointing to the guide that carries the mechanism and any Tier-2 findings that go one layer deeper.
2. **Key Concepts subsection(s)** of the named guide(s) — the authoritative mechanism summary. Secondary reads: `### Pitfalls` (when the explanation is "what goes wrong without this"), `### Mechanism` / `### Why this works` subsections (if the guide has them under other names — G2 §Step 5 item 1 explains *why* state objects beat prose, for example).

Key Concepts sections function as emergent mechanism explainers by construction — they were authored to carry the "why" at one level above the procedure. The Librarian reads them; it does not re-derive.

### Composition details

**(a) Guide-first, finding-second.** Start with the guide's Key Concept summary; it's the curated mechanism. Escalate to Tier 2 only when the guide's summary is surface-level and the consumer's question implies depth ("why does X *really* happen, at the mechanism level").

**(b) Mechanism layering.** When a mechanism has multiple layers (surface cause → proximal mechanism → underlying principle), state them in order. Example for context rot: surface (agent loses constraints) → proximal (attention-budget depletion) → underlying (larger contexts have thinner per-token attention). Each layer cites its substrate.

**(c) Evidence surfacing on ask.** If the consumer asks "show me the evidence" or "how do we know this," surface the finding file directly — Librarian does not paraphrase when the consumer asked for the primary source.

**(d) Don't pad.** If the KB covers mechanism partially, state the gap. Do not supplement from training data per Librarian governance contract.

## Procedure

Four phases.

### Phase 0 — Parse the query

Parse verb + noun(s). Verb must be `explain` or a synonym ("why does," "how does X work," "what is," "mechanism behind"). Noun identifies the topic — a concept, a phenomenon, a design rationale, a cost behavior.

If the question blends "explain X" with "decide A vs B," the primary verb is explain; offer the decide handoff as a next step ("once you understand the mechanism, ask me to compare A vs B on these axes").

### Phase 1 — Load composition

Read the concept file for the noun. Read the `### Key Concepts` subsection of the named guide(s). If the consumer's question specifically asks about failure-mode-as-rationale ("why does this matter" / "what goes wrong without this"), also read `### Pitfalls`.

Do not read full guide bodies — Key Concepts is short by design (≤10 numbered concepts per guide in the current substrate).

### Phase 2 — Compose mechanism narrative

Produce a short narrative (typically 3–8 sentences or a small numbered list):

1. **Surface answer.** One-sentence direct response to the consumer's question.
2. **Mechanism.** 2–4 sentences from the Key Concept summary, cited to `<guide>.md#<anchor>`.
3. **Underlying principle (optional).** When the Key Concept invokes a deeper principle (e.g., "attention-budget depletion" invokes an underlying transformer attention mechanism), state it briefly and cite the Tier-2 finding that carries the specifics.

Do not turn the response into a full guide excerpt. The consumer asked "why," not "give me everything on this."

### Phase 3 — Escalate to Tier 2 (if applicable)

If the consumer asked for depth ("really," "mechanism," "show me the evidence") or if the Key Concept summary is thin relative to the question, pull the Tier-2 finding named in the concept's composition table. Quote the finding's `Key insight` or `Mechanism` line and cite the slug. Stop at one Tier-2 hop unless the consumer asks for more.

### Phase 4 — Gap + next-step pass

- If substrate coverage is partial, state it: "G2 Key Concepts covers X but does not unpack Y. If you want Y-specifics, ask and I'll flag it as a KB gap."
- If the explanation naturally leads to a follow-up operation (design, decide, diagnose), offer one next-step suggestion.

## Consumer input handling

Expected input: a topic or phenomenon, phrased as a "why" or "what is" question. The Librarian does not require the consumer to specify depth — depth is inferred from phrasing ("why does this happen" = mechanism depth; "what is X" = definition depth).

No artifact is consumed. Explain operates on substrate, not on consumer-supplied content.

| Query shape | How to read |
|---|---|
| Mechanism (UC-6.1: "why does context rot happen?") | `context-rot.md` → G2 §Key Concepts + §Step 5 mechanism layer + Tier-2 `context-rot-attention-budget-depletion` |
| Design rationale (UC-6.2: "why do agent Contracts need Preconditions?") | `agent.md` → G1 §Key Concepts + DD-78 framing note + Contract triple-role rationale |
| Cost mechanism (UC-6.3: "why does prompt caching reduce cost so dramatically?") | `prompt-caching.md` → G2 §Step 6 mechanism + pricing arithmetic + Anthropic caching docs (Tier 3 if pressed) |

## Output shape

```
## Explain — <topic>

**Interpreted as:** (verb: explain, noun(s): <n>, depth: <surface / mechanism / evidence>)

### Answer

<1 sentence direct response.>

### Mechanism

<2-4 sentences from Key Concept summary, inline-cited to the guide anchor.>

### Underlying principle / evidence (if applicable)

<1-2 sentences + Tier-2 finding citation if depth was asked for.>

### Gap (if any)

<If the KB covers partially — state what's covered, what's not.>

### Next-step suggestion (optional)

<One line: "next you might want to decide / design / diagnose <X>".>
```

## Governance and boundaries

- Explain is **read-only on substrate**. The Librarian does not invent mechanisms the substrate does not cover.
- No general-knowledge padding. If the KB is thin on a mechanism, state the gap — do not supplement from training data (per Librarian agent governance contract).
- Explain does not turn into a lecture. Short is the discipline — consumers who want depth can ask; consumers who asked "why" deserve the answer, not a guide excerpt.
- Explain does not file gap reports autonomously. Gaps surface as part of the response per read-contract §Step 6.4.

## Cross-references

- Read-contract (Step 1 verb extraction, §8.5 input handling for explain): `project-management/design-notes/2026-04-21-librarian-read-contract.md`.
- Related operations: `decide.md` (explain often precedes decide), `diagnose.md` (diagnose's optional mechanism layering is a narrower version of explain).
- Related concepts: `context-rot.md`, `prompt-caching.md`, `agent.md`, `memory.md`, `agentic-systems.md` (this directory) — any concept file can route an explain query to its Key Concepts substrate.
- Use-case registry (UC-6.1–6.3): `project-management/design-notes/2026-04-21-librarian-use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role — Key Concepts as emergent mechanism explainers), DD-82 (IL 4-agent architecture).
