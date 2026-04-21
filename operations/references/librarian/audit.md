---
operation: audit
type: operation
target_system:
  - "improvement-loop"
created: "2026-04-21"
updated: "2026-04-21"
author: "claude"
stage: "draft"
tags:
  - "librarian-operation"
  - "audit"
  - "assess"
aliases:
  - "Audit"
  - "Assess"
  - "Review against criteria"
---

# Audit

## Short definition

**Audit** evaluates a consumer-submitted artifact (an `agent.md`, a system prompt, a `SKILL.md`, a harness configuration, etc.) against criteria derived from relevant guides' Contract sections. It reports findings — each tied to a specific invariant — and surfaces follow-up questions for invariants it cannot verify from the artifact alone.

Audit is a *consumption* operation: the Librarian reads the artifact the consumer provides plus the substrate pointed to by the matching concept file. Audit does not modify any artifact, does not write to the KB, and does not propose redesigns (that's the `design` operation).

## Default composition rule

`audit` composes two inputs:

1. **Concept file** for the artifact under audit — provides the composition table (which guides' Contract sections are load-bearing for this artifact type). Examples: `agent.md` concept → {G1, G2, G3, G5, G6, G9, G10}; skill audit → {G1, G3b, G5, G6, G8}; prompt audit → {G1, G2, G5, G8}; harness audit → cross-guide thread in `harness.md`.
2. **Contract sections** of the named guides — specifically:
   - `### Preconditions` → used as *applicability gates* (see §Procedure).
   - `### Invariants` → the rubric criteria. Each invariant becomes one audit check.
   - `### Recovery` → optional escalation material for findings (what to do when a check fails).

Contract invariants function as emergent audit criteria by construction (DD-78's invariants are declarative testable statements — validated empirically in `2026-04-21-contract-section-spotcheck-agent-audit.md`). No view-artifact curation required.

### Composition details

**(a) Invariant de-duplication.** When the composed guide set contains near-duplicate invariants (canonical example: G3.I4 and G8.I4 both state "Model selection is task-based, not provider-based"), collapse to a single rubric row. Normalize invariant text; record source guides as a list rather than a single citation. Report the merged finding, not two.

**(b) Hierarchical overlap annotation.** When invariants are in an umbrella/specialization relationship (e.g., G1.I3 "hard constraints have enforcement outside the prompt layer" ⊃ G6.I2 "safety-critical constraints are enforced structurally"), keep both. Apply the specialization to the scoped aspect first; let the umbrella catch anything the specialization does not reach. Annotate the relationship in the report so the consumer sees why both fired.

**(c) Conditional applicability via Preconditions.** Fire an invariant only if its guide's Contract Preconditions are satisfied by the audit target. A prompt that embeds no context directives does not fire G2 (G2 preconditions require context-affected agent output). A skill that defines no tools does not fire G5 (G5 preconditions require tools). Preconditions were authored as authorial guardrails and double as audit gates — no new authoring required.

**(d) File-verifiable vs system/process-verifiable split.** Each invariant is one of two kinds:
   - **File-verifiable** — inspectable directly from the submitted artifact. Fires a *finding* (violated / missing / satisfied).
   - **System/process-verifiable** — requires runtime evidence or attested cadence ("stable context is cached"; "complexity audits run on major model releases"). Fires a *follow-up question* to the consumer — never silently skip, never falsely pass.

   The audit report distinguishes the two columns so the consumer knows which findings are concrete versus which need their own evidence to close.

## Procedure

Five phases. The Librarian executes top-to-bottom and produces a single report at the end. Do not stream partial results mid-phase.

### Phase 0 — Parse the query

Parse verb + noun(s). Verb must be `audit` or a synonym (review, assess, evaluate, critique). Noun identifies the artifact type — agent, prompt, skill, harness, or other concept-file noun. If no noun resolves to a concept file, ask the consumer one disambiguating question.

### Phase 1 — Load composition

Read the concept file for the noun(s). Read the `### Preconditions`, `### Invariants`, and `### Recovery` subsections of each guide named in the concept's composition table. Do not read full guide bodies at this phase — only the Contract subsection. Deploy-by-anchor from the section manifest when available; otherwise match on heading text.

### Phase 2 — Build rubric

Pool invariants from all composed guides. Apply:

1. **Precondition gating (composition step c).** For each guide, evaluate its Preconditions against the submitted artifact. If a Precondition is unsatisfied, mark the guide's invariants *latent* — they will not fire during audit but will be surfaced at the end of the report as "aspects not in scope for this audit."
2. **De-duplication (step a).** Collapse near-duplicates; merge source-guide lists.
3. **Hierarchical overlap annotation (step b).** Mark umbrella/specialization pairs.
4. **File-verifiable vs system-verifiable split (step d).** Tag each invariant.

Emit the composed rubric as the first section of the working report.

### Phase 3 — Apply rubric

For each **file-verifiable** invariant:

1. Locate the aspect of the submitted artifact the invariant governs.
2. Check: does the artifact satisfy the invariant? Possible outcomes: **Satisfied** / **Partial** / **Violated** / **Missing** (aspect absent entirely).
3. Record the check as a finding: invariant text, source guide, outcome, evidence quote from the artifact, suggested recovery reference (from the guide's `### Recovery` if applicable).

For each **system/process-verifiable** invariant:

1. Do not attempt to answer from the artifact.
2. Record a follow-up question the consumer must answer: invariant text, source guide, and a concrete question shape (e.g., G2.I2 "stable context is cached" → "Is your harness applying prompt caching to the stable portion of context? What is the observed cache-hit rate?").

### Phase 4 — Assemble report

Produce the audit report in the output shape below.

### Phase 5 — Confidence + provenance pass

- Attach **tier** to every finding (Tier 1 for guide-Contract evidence; Tier 2 if the finding was strengthened by a pattern/finding reference; Tier 3 if a watched-library comparison was pulled).
- Attach **confidence** to each finding: high (direct invariant violation visible in the artifact), medium (invariant violation inferred from absence), low (invariant applies but the artifact's coverage is ambiguous). Low-confidence findings must include the ambiguity reason.
- If any load-bearing aspect of the artifact's domain went unaudited because its guide's Preconditions were unsatisfied, state that explicitly ("G2 not in scope for this prompt because it embeds no context directives — if it should, re-submit with context included").

## Consumer input handling

The consumer submits the artifact inline as text (or a file path the Librarian can Read). For artifacts larger than ~500 lines, the Librarian requests a scoping clarification rather than auditing everything ("Should I audit the full CLAUDE.md or specific sections?").

Artifacts may be of these forms:

| Artifact | Noun concept file | Composed guides |
|---|---|---|
| `agent.md` | `agent.md` (planned) | G1, G2, G3, G5, G6, G9, G10 (also G3b, G7 if agent delegates or persists) |
| System prompt / user prompt | `prompt.md` (planned) | G1, G2, G5, G8 |
| `SKILL.md` | `skill.md` (planned) | G1, G3b, G5, G6, G8 (add G9.I6 for safety-critical skills) |
| Harness config | `harness.md` (this directory) | G2, G3b, G5, G6, G8, G4 cross-guide thread |
| Generic code artifact | Reject — audit operation is scoped to agent-system artifacts. Redirect to `/prompt-evaluator` / `/security-review` / language-specific review tools. |

If the consumer submits an artifact type not covered by an existing concept file, the Librarian states this and offers the closest-adjacent composition, explicitly noting the gap.

## Output shape

```
## Audit — <artifact type>

**Artifact:** <path or summary>
**Composed guides:** <list with role of each>
**Rubric size:** <N file-verifiable invariants, M system-verifiable invariants, K latent (out-of-scope)>

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | … | … | G1.I1 | Missing | — | G1 §Recovery | 1 | High |
| … |

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|---|---|---|---|
| a | … | G2.I2 | Is stable context cached? | Cache-hit rate; caching config |
| … |

### Aspects out of scope

| Guide | Why latent |
|---|---|
| G2 | Prompt embeds no context directives — G2 Preconditions unsatisfied. |

### Summary

<1–3 sentences: what's solid, what's load-bearing to fix, what hinges on consumer follow-ups>
```

## Governance and boundaries

- Audit is **read-only on the submitted artifact and on the KB**. The Librarian never rewrites the artifact.
- Audit does not propose a redesign. If the consumer asks for one, hand off to the `design` operation (planned).
- Audit does not file DDs, update the KB, or deploy anything. Any gap in IL coverage surfaced during audit is a *Librarian gap report* — reported to the consumer, not fixed.

## Cross-references

- Contract-section spot check (validation for this operation's composition mechanism): `project-management/design-notes/2026-04-21-contract-section-spotcheck-agent-audit.md`.
- Substrate audit §"The Librarian Reference Layer" + §"Three-Tier Access Model".
- Related concept files: `harness.md`, `second-brain.md` (in this directory); `agent.md`, `prompt.md`, `skill.md` (planned).
- Librarian agent contract: `agents/librarian/agent.md`.
- Guide routing table (source of guide IDs and practitioner-question mapping): `operations/references/guide-routing-table.md`.
- Workspace-root `/prompt-evaluator` skill: coordination target for `audit + prompt` — Phase 6 skill design decides wrap vs. extend.
- Governing DDs: DD-78 (ContractSpec; Contract invariants as emergent audit criteria), DD-82 (IL 4-agent architecture; Librarian role).
