---
operation: design
type: operation
target_system:
  - "improvement-loop"
created: "2026-06-11"
updated: "2026-06-11"
author: "claude"
stage: "draft"
tags:
  - "librarian-operation"
  - "design"
  - "construct"
aliases:
  - "Design"
  - "Construct"
  - "Author a new artifact"
---

# Design

## Short definition

**Design** drafts a new artifact (an `agent.md`, a system prompt, a `SKILL.md`, a harness configuration, etc.) from designer intent plus construction substrate composed from the relevant concept file. It produces a complete draft of the artifact, gated for designer review, and is the constructive peer of the `audit` operation.

Design is a *construction* operation: the Librarian reads the concept file's §Construction subsections and the substrate they point to, elicits designer intent for unresolved choices, and produces a draft. Design does not deploy the artifact, does not write it to a system's enforcement location, and does not propose changes to the IL's own substrate. The draft is the designer's to accept, modify, or reject.

Per IL rule 10 (generator-assessor separation), `design` does not self-assess the artifact it produces. After producing the draft, it invokes the corresponding assess-* skill (`/assess-skill`, `/assess-agent`, `/assess-prompt`) as a subagent in fresh context, surfaces the audit findings alongside the draft, and lets the designer decide whether to revise.

**Predecessor.** An earlier `design.md` (2026-04-22) operated in *advisor mode* — produced step guidance for the consumer to follow rather than a draft artifact. That shape was authored before §Construction substrate existed in concept docs (sessions A.4a/A.4b, 2026-06-11) and before rule 12 (audit/design symmetry) codified the bilingual-reading model. Author mode (this spec) is the constructive peer audit needs. If advisor-mode guidance is later shown to be a recurring need (rule 11 evidence: 2–3 distinct consumer requests), a separate `advise.md` operation can be drafted.

## Default composition rule

`design` composes two inputs:

1. **Concept file** for the artifact under construction — provides §Construction (Decision sequence, Template skeleton, Scoping heuristics, Authoring-time anti-patterns) plus §Composition (the audit-side composition table, read here as a forward-reference to the audit surface the draft will face — see Phase 1).
2. **Construction substrate** referenced from the concept file:
   - `### Decision sequence` → ordered authoring steps; structures Phase 2 of the procedure.
   - `### Template skeleton` → canonical artifact shape; structures Phase 4 output.
   - `### Scoping heuristics` → consulted during Phase 2 when a step surfaces a split/collapse decision.
   - `### Authoring-time anti-patterns` → consulted during Phase 3; named in the report's risk surface.

§Construction functions as design-time substrate by construction (Librarian A.2 audit, session 106). No view-artifact curation required.

### Composition details

**(a) Variant-aware composition.** For variant-carrying concepts (`agent.md`), Decision-sequence step 1 selects the variant; subsequent steps' applicability depends on the selection. Carry the variant tag forward into Template skeleton (common core + variant overlay).

**(b) Hard-gate steps.** Some Decision-sequence steps are hard gates (safety-critical classification for skills; autonomy-envelope sizing for Variant C agents). These cannot be deferred — Phase 2 must reach a concrete decision before proceeding. Soft steps may be skipped with explicit "N/A" annotation.

**(c) Conditional applicability via §Composition Preconditions.** The same Preconditions that gate audit invariants gate design-time substrate loading: a Variant A agent draft does not load G5/G6 substrate unless authoring surfaces tool directives. If the draft acquires the trigger condition mid-design, re-evaluate variant assignment (variant-drift anti-pattern).

**(d) Generator-assessor separation (rule 10).** Design produces; assess-* assesses. Design never internally inspects its own draft against rubric criteria; that work is delegated.

## Procedure

Six phases. The Librarian executes top-to-bottom and produces a single report at the end. Do not stream partial draft sections mid-phase — the designer needs the full draft alongside the audit findings.

### Phase 0 — Parse the query

Parse verb + noun(s). Verb must be `design` or a synonym (construct, author, create, draft, build). Noun identifies the artifact type — agent, skill, prompt, harness, or other concept-file noun. If no noun resolves to a concept file, ask the designer one disambiguating question and stop until answered.

### Phase 1 — Load construction substrate

Read the concept file for the noun. Read its §Construction subsections in this order: Decision sequence, Template skeleton, Scoping heuristics, Authoring-time anti-patterns. Also read §Composition.

§Composition is read here as a *forward-reference to the audit surface the draft will face* — so the designer can anticipate which guides will fire at audit time. It is **not** design-time input; design's load-bearing substrate is §Construction. A Librarian that confuses §Composition for design substrate would import audit-time rubric criteria into the authoring procedure, collapsing the construction/composition distinction the concept docs were structured to preserve.

For variant-carrying concepts, do not pre-load all variant overlays. The variant is selected in Phase 2 step 1; only then load the relevant overlay.

### Phase 2 — Elicit designer intent (Decision sequence walk)

Walk the §Decision sequence step by step. For each step:

1. State the step and its purpose (one line).
2. Ask the designer the questions the step requires. Defaults are acceptable only when the step explicitly allows N/A.
3. Record the answer. If the answer surfaces a scoping question (split / collapse / decompose), consult §Scoping heuristics and ask the disambiguating question.
4. Apply hard gates immediately (a safety-critical-classified skill cannot proceed without a stated HITL gate; a Variant C agent cannot proceed without a sized autonomy envelope).

Phase 2 produces a **Decision record**: the answered Decision sequence, one row per step, including which scoping decisions were made and why.

### Phase 3 — Surface authoring-time risks

Compare the Decision record against §Authoring-time anti-patterns. For each anti-pattern the current draft posture could fall into, name it explicitly ("Variant declared A but step 3 surfaced tool directives — variant-drift risk; promoted to Variant B").

§Authoring-time anti-patterns is *construction substrate* (part of the concept doc), not an audit rubric. Phase 3 produces forward-looking *warnings* against the in-progress design posture; it does not produce findings, does not assign tier/confidence, and does not substitute for the Phase 5 audit. The audit runs against the completed draft with a fresh-context assessor (rule 10).

### Phase 4 — Draft the artifact

Apply the §Template skeleton, filling placeholders from the Decision record. For variant-carrying concepts, compose common core + declared variant's overlay.

The draft must be complete — frontmatter populated, all required sections present, no `<placeholder>` text remaining for required fields. Optional fields may be left empty with an explicit `# optional, omit if unused` comment.

Write the draft to the designer's chosen location *only if explicitly approved* in the Output shape (see below). By default, the draft is presented inline for review.

### Phase 5 — Delegate audit (rule 10)

Invoke the corresponding assess-* skill as a subagent in fresh context: `/assess-skill` for SKILL.md, `/assess-agent` for agent.md, `/assess-prompt` for prompts. Pass the draft as input. Do not internally inspect the draft against rubric criteria — the assessor must run with fresh context to preserve the epistemic gap.

Collect the assess-* report. Attach as a separate report block.

### Phase 6 — Assemble report

Produce the design report in the output shape below. Surface the Decision record, the Authoring-time risk surface, the draft artifact, and the assess-* findings — all four are deliverables to the designer.

## Designer input handling

The designer submits intent inline (what the artifact should do, who consumes it, what's in/out of scope). For under-specified intent, the Librarian asks one clarifying question per Decision-sequence step rather than demanding upfront completeness — the Decision sequence walk *is* the intent-elicitation protocol.

Designers may submit a partial draft they want completed. The Librarian parses the partial against the Template skeleton, identifies missing sections, and runs Phase 2 only for the missing material.

For partial drafts larger than ~500 lines, the Librarian requests scoping clarification before beginning Phase 2 (mirrors `audit.md`'s ~500-line threshold). Designer intent over 500 lines of narrative is rare and usually signals over-scoping — point the designer to §Scoping heuristics in the concept doc before proceeding.

## Output shape

```
## Design — <artifact type>

**Artifact:** <intended path or summary>
**Concept:** <noun concept file>
**Variant (if applicable):** <A / B / C / overlap>

### Decision record (Phase 2)

| Step | Decision | Source / scoping note |
|---|---|---|
| 1 | … | … |
| … |

### Authoring-time risks surfaced (Phase 3)

| # | Risk (from §Authoring-time anti-patterns) | Why it applies here | Mitigation in draft |
|---|---|---|---|
| 1 | … | … | … |

### Draft artifact (Phase 4)

<full draft, in the artifact's native format — markdown for SKILL.md / agent.md, prompt text for prompts, JSON/YAML for harness config>

### Audit findings (Phase 5 — delegated to /assess-*)

<embedded /assess-* report, including its Findings table, Follow-ups table, Aspects-out-of-scope table, and Summary>

### Summary

<1–3 sentences: what the draft does well, what risks remain, what the audit flagged, what the designer should decide next.>
```

## Governance and boundaries

- Design is **read-only on the KB and on concept docs**. It produces drafts of new artifacts; it does not modify substrate.
- Design does not deploy the draft. Writing the draft to an enforcement location (`.claude/skills/<name>/SKILL.md`, `agents/<name>/agent.md`) is the designer's decision, not the Librarian's. Default behavior is present inline.
- Design does not internally assess the draft (rule 10). Delegate to assess-* in fresh context. The assess-* report is surfaced alongside the draft, not substituted for it.
- If the designer's intent surfaces a gap in IL substrate (the concept doc doesn't cover the requested artifact type, or a Decision-sequence step has no guidance for an emerging variant), it is a *Librarian gap report* — reported to the designer, not fixed by design.

## Cross-references

- Symmetric audit operation: `audit.md` (this directory) — design is the constructive peer. Rule 12 (audit/design symmetry) governs how the two operations stay aligned at the concept-doc level.
- Concept files providing §Construction substrate: `skill.md`, `agent.md` (this directory). `prompt.md` adds §Construction when moderate demand becomes strong (currently weak per `consumer-abstractions-map.md`).
- Concept files with §Construction debt (§Composition only): `harness.md`, `second-brain.md`, `memory.md`, and other concept files in this directory. These remain auditable but not yet constructible; tracked per rule 12 operational guidance.
- Librarian agent contract: `agents/librarian/agent.md`.
- Governing rules: IL `agent-rules.md` rule 10 (generator-assessor separation — design delegates assessment), rule 11 (abstractions must earn their keep — design must not invent constraints not in substrate), rule 12 (audit/design symmetry — concept docs must support both operations).
- Governing DDs: DD-78 (ContractSpec; Construction substrate complements Contract), DD-82 (IL 4-agent architecture; Librarian role).
