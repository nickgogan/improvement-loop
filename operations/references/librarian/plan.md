---
operation: plan
type: operation
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "claude"
stage: "draft"
tags:
  - "librarian-operation"
  - "plan"
  - "lifecycle-sequencing"
aliases:
  - "Plan"
  - "Roadmap"
  - "Sequence build"
  - "In what order"
  - "Build-order"
---

# Plan

## Short definition

**Plan** produces a sequenced build order for an artifact (or artifact pair) across the full lifecycle — *specify → build → verify → secure → operate* — naming the substrate to consult at each phase. Input is the target artifact plus known constraints and scope. Output is a phase-ordered roadmap: each phase lists its goal, the substrate to pull (concept-file aspect + guide subsection pointer), and the handoff gate that the consumer must clear before entering the next phase.

Plan is a *consumption* operation: read-only on substrate; the Librarian does not commit phases, track progress, or verify handoff-gate completion — it produces the recipe across lifecycle boundaries, not the execution.

Plan and design are siblings. Design produces within-phase step guidance for a named aspect ("design my tool registry"). Plan produces *across-phase* sequencing for a whole artifact or multi-artifact stack ("how do I sequence building a new agent from scratch" — UC-9.1; "I want an agent + hybrid second brain — in what order" — UC-9.2). When the consumer's scope fits in one phase, design is the right operation; when it spans the lifecycle, plan is.

## Default composition rule

`plan` composes three inputs:

1. **Concept file(s)** for the target artifact(s) — provides the composition table and variant selection. For variant-carrying concepts (agent, memory, second-brain), resolve the variant before composition; the variant narrows the guide union for the lifecycle map.
2. **Lifecycle axis** — the fixed five-phase ordering *specify → build → verify → secure → operate*. Each phase maps to a guide-subsection kind (see §Lifecycle axis mapping below). Plan does not re-derive the axis; it reads it.
3. **Cross-concept dependencies** (for UC-9.2) — when the plan spans two concepts (agent + second-brain, memory + harness), load both concept files and identify phases where one concept's decision constrains another. Order dependencies before dependents; flag explicit gating.

### Lifecycle axis mapping

Each phase reads the named subsection kinds from the variant's composed guide union:

| Phase | Phase goal | Primary guides & subsection kinds |
|---|---|---|
| **Specify** | Produce the spec the rest of the lifecycle builds against — objectives, desired outcomes, constraints, acceptance criteria. | G1 `writing-agent-specifications.md` §Step subsections + §Contract §Preconditions (as handoff gate). |
| **Build** | Implement against the spec — context files, prompt composition, tool registry, memory wiring, governance scaffolding. | Variant-scoped guide union's `### Procedure` / `### Step N` sections. Prompt-based agent variant: G2a + G2b + G8. Harness-based variant: add G3 + G3b + G5 + G6. Autonomous-vs-supervised: add G7 + G9. |
| **Verify** | Wire evaluation; establish that specified capabilities are implemented. | G4 `building-agent-evaluation-suites.md` §Step sections + §Contract §Invariants (as handoff gate). |
| **Secure** | Apply permission model, sandboxing, blast-radius gates, governance hooks. | G6 `agent-safety-and-permissions.md` §Contract §Invariants + §Procedure; G9 `agent-governance-and-trust.md` when the artifact touches governance. |
| **Operate** | Deploy operationally — session handoff, crash recovery, cross-session state, observability. | G3b `agent-workflow-and-execution.md` §State / §Termination; G7 `session-persistence-and-memory.md` §Handoff / §Crash Recovery. |

Plan reads Contract subsections from each phase's source guide to derive **handoff gates** — the minimal acceptance checks that must pass before the next phase starts. These are not full audits; they are the minimum the next phase assumes as input.

### Composition details

**(a) Phase scoping.** Not every artifact's plan touches all five phases. A consumer scaffolding an `agent.md` stub may stop at *specify*; a production-deploy roadmap spans all five. Walk phases top-to-bottom against the consumer's declared scope; prune out-of-scope phases and state which were skipped and why. Do not emit a five-phase roadmap when the consumer asked for a build-order.

**(b) Variant overlay.** For variant-carrying concepts, the plan's phase-by-phase guide union is the *variant's* union, not the full concept guide set. A Variant A (prompt-based) agent plan pulls {G1, G2a, G2b, G8, G4} across phases specify → build → verify; Variant B (harness-based) adds {G3, G3b, G5, G6}; Variant C (autonomous-vs-supervised) adds {G7, G9}. Variant overlay narrows the plan without losing phase structure.

**(c) Cross-concept dependency surfacing.** For UC-9.2-style plans, produce *one sequenced roadmap*, not two parallel lists. Dependency flow typically: upstream concept's *specify* → downstream concept's *specify* → upstream *build* ↔ downstream *build* (interleaved by dependency direction) → joint *verify* → joint *secure* → joint *operate*. Flag explicit gating: "choose second-brain Variant C before the agent *build* phase starts — hybrid curation requires HITL scaffolding in the agent spec."

**(d) Handoff gates, not audits.** Each phase closes with a minimal gate — one or two acceptance checks from the source guide's Contract (e.g., specify → build gate: "objectives and acceptance criteria are written"; build → verify gate: "all specified capabilities are implemented; eval harness is wired in"). These are not full Contract audits (that is `audit.md`'s job); they are the minimum the next phase assumes and the natural seam for an `audit` handoff.

**(e) Handoffs to `design`, `audit`, `decide`.** Plan is a high-level roadmap; it does not produce within-phase step-by-step guidance. When the consumer zooms into a phase ("what do the *build* steps look like for the tool registry?"), hand off to `design`. When the consumer wants to verify a phase's output, hand off to `audit`. When a phase's substrate carries a design debate (e.g., *build* phase for memory carries the `mongodb-single-store` ↔ `triple-storage-memory` `contradicts` pair), flag it and hand off to `decide` — do not expand the debate inline.

## Procedure

Four phases (the Librarian's procedure for producing the plan; not the consumer's build lifecycle).

### Phase 0 — Parse the query

Parse verb + noun(s). Verb must be `plan` or a synonym ("sequence," "in what order," "phases," "roadmap for building," "build-order," "how do I sequence"). Noun(s) identify the target artifact(s); for cross-concept queries, extract both.

If the consumer has not stated at least one scope signal (which phases they care about, whether it's a scaffold vs production roadmap, rough timeline or team size), ask *one* qualifying question before composing. Unscoped plans over-cover — the consumer usually wants near-term build guidance, not a full five-phase deployment roadmap.

### Phase 1 — Load composition

Read the concept file(s) for the noun(s). For variant-carrying concepts, resolve the variant from the consumer's phrasing (re-using the variant-selection heuristics in the concept file; do not reinvent them). Read the lifecycle-axis mapping (above) and, for each in-scope phase, read §Contract §Preconditions / §Invariants of that phase's source guide — enough to populate per-phase handoff gates, not full guide bodies.

Do not read §Procedure / §Step N subsections in full at plan time — that level of depth is design's job. Plan pulls the *pointer* (e.g., "G5 §Step 3 line 134 'Implement Discovery and Loading'"), not the full step sequence.

### Phase 2 — Sequence across the lifecycle axis

Build the phase-ordered roadmap. For each in-scope phase:

1. State the phase goal in one sentence.
2. List the substrate to pull — concept-file aspect + guide subsection pointer. Format: `<guide>.md#<anchor>` (heading-match fallback until the section manifest lands).
3. State the handoff gate — the one or two Contract preconditions / invariants that must be satisfied before the next phase begins.

Prune out-of-scope phases per composition step (a); apply variant overlay per (b).

### Phase 3 — Surface cross-concept dependencies (if applicable)

For cross-concept plans (UC-9.2), run composition step (c): interleave the two concepts' phase orders and flag the gating points where one concept's decision constrains another. Do not emit two parallel plans and ask the consumer to merge them.

### Phase 4 — Tier + provenance + debate-flag + next-step pass

- Every phase's substrate pointer cites the guide anchor. Tier 1 is the default.
- Plan escalates to Tier 2 **only to flag** design debates — not to expand them. If a phase has known `contradicts`-bearing substrate (memory build phase, single-vs-multi-agent decision in *specify*), surface the pair in a "Design debates flagged" section and hand off to `decide`.
- Plan does not silently escalate to Tier 3. Reference-implementation comparisons across the lifecycle ("how does Claude Code sequence these phases?") are consumer-request-gated.
- Attach **next-step suggestions** at the end: `design` handoff for a named phase's internal steps; `audit` handoff after the artifact is built; `decide` handoff for any flagged debates.

## Consumer input handling

Expected input:

- **What they're building.** Artifact or artifact pair (agent, skill, second-brain, memory + agent, agent + hybrid second-brain, etc.).
- **Scope.** Which phases matter. If unstated, ask — "do you want the full specify → operate roadmap, or just the near-term build sequence?"
- **Variant or constraint hints.** Prompt-based vs harness-based agent; Variant C (hybrid) vs Variant A (human-curated) second-brain; team size / timeline when it meaningfully narrows the plan.

If the consumer provides an existing partial artifact alongside the plan question ("here's my spec so far"), treat it as scenario grounding — *not* as input to audit. Plan from the artifact's current phase forward; offer the audit handoff separately if the consumer wants to evaluate the partial artifact.

Scoping heuristics:

| Query shape | How to read |
|---|---|
| Single-artifact, full-lifecycle (UC-9.1: "sequence building a new agent from scratch") | Cross-phase thread across the variant's guide union; state per-phase goal + substrate pointer + handoff gate. |
| Single-artifact, partial-scope ("I have the spec; what comes next?") | Skip *specify*; start at *build*; state exit conditions for each remaining phase. |
| Cross-concept (UC-9.2: "agent + hybrid second brain — in what order") | Load both concept files; interleave phases; flag gating points where one concept's decision constrains another. |
| Variant-ambiguous ("plan out my agent's memory") | Route through the concept file's variant-selection heuristics first; ask which tier the consumer is planning before sequencing. Plan a variant-ambiguous memory stack typically does not serve the consumer. |

## Output shape

```
## Plan — <artifact(s) under build>

**Interpreted as:** (verb: plan, noun(s): <n> [variant: <var>], scope: <phases in-scope>)
**Composed guides:** <variant-scoped list>
**Phases out of scope:** <list, with one-line reason each>

### Roadmap

#### Phase 1 — Specify
- **Goal:** <one sentence>
- **Substrate:** G1 §<anchor> (<line range>); concept-file aspect: `<aspect>`
- **Handoff gate:** <one or two Contract preconditions / invariants>

#### Phase 2 — Build
- **Goal:** <one sentence>
- **Substrate:** <variant-scoped guide subsection pointers>
- **Handoff gate:** …

#### Phase 3 — Verify
…

#### Phase 4 — Secure
…

#### Phase 5 — Operate
…

### Cross-concept dependencies (if applicable)

<Surfaced for UC-9.2: gating points where one concept's decision constrains another; cite both concept files.>

### Design debates flagged (if any)

<Phases whose substrate carries `contradicts` pairs. One-line summary + `decide.md` handoff pointer. Do not expand inline.>

### Next-step suggestions

<`design` handoff for deep-dive on a named phase; `audit` handoff after the artifact is built; `decide` handoff for flagged debates.>
```

## Governance and boundaries

- Plan is **read-only on substrate**. The Librarian does not author the artifact, commit phases, or track progress.
- Plan does not produce within-phase step-by-step guidance — that is `design`. When the consumer asks for both ("plan this and also show me the build steps"), produce the plan and offer the `design` handoff; do not smuggle design output into a plan response.
- Plan does not apply rubric criteria — that is `audit`. Handoff gates are minimal Contract preconditions, not full audits.
- Plan does not invent phases the lifecycle axis does not carry. If the consumer's scope fits none of *specify / build / verify / secure / operate* (e.g., a pure refactor with no spec change), state that the lifecycle axis is wrong-fit and redirect to `design` for the affected phase.
- Plan does not over-scope. Defaulting to a five-phase roadmap when the consumer asked for a near-term build-order is a cost leak; ask for scope before expanding.
- Plan does not expand design debates inline. Flag the debate and hand off to `decide` — one operation, one output shape.

## Cross-references

- Read-contract (§Step 3.1 names plan's subsection kinds; §8.5 input handling for plan): `operations/references/librarian/read-contract.md`.
- Guide routing table (lifecycle axis source): `operations/references/guide-routing-table.md`.
- Related operations: `design.md` (within-phase deep-dive — plan's primary handoff); `audit.md` (post-phase and post-build verification); `decide.md` (for design debates flagged during planning) (this directory).
- Related concepts: `agent.md`, `memory.md`, `second-brain.md`, `harness.md`, `skill.md`, `prompt.md`, `mcp.md` (this directory) — any concept file can anchor a plan.
- Use-case registry (UC-9.1, UC-9.2): `operations/references/librarian/use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role — Procedure as authored build sequence; Preconditions as handoff gates), DD-82 (IL 4-agent architecture).
