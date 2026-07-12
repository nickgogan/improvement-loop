---
operation: fetch
type: operation
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "claude"
stage: "draft"
tags:
  - "librarian-operation"
  - "fetch"
  - "concrete-deliverable"
aliases:
  - "Fetch"
  - "Get template"
  - "Give me a scaffold"
  - "Catalog"
---

# Fetch

## Short definition

**Fetch** returns a concrete artifact the consumer names — a template, a rule, a scaffold, or a catalog of available artifacts. Input is the artifact kind + the name (or description) of the specific one wanted. Output is the artifact itself, lifted inline from the substrate anchor that authored it, with variable slots made explicit.

Fetch is a *consumption* operation with an anchor-lifting shape: it reads a specific named subsection from a named guide and returns its body. The work is in *locating* the right anchor and *substituting* any consumer-named variables — not in synthesis. Fetch has three sub-operations consolidated into one file per session-49 Open-Question 2 (Nick's guidance: prefer collapse for token economy; split only if this file grows past budget).

## Sub-operations

Fetch covers three shapes; the query determines which fires.

### Sub-op A — Fetch-template

Consumer names a template by title or by its function: "Give me a context-budget template"; "Show me the trust-ledger template." The Librarian locates the matching entry under the source guide's `### Templates` section and lifts the body inline with `{{placeholder}}` variables visible.

### Sub-op B — Fetch-rule

Consumer names a rule by slug or description: "Give me the programmatic-snippet-extraction rule"; "Give me the rule on stable context being cached." The Librarian locates the invariant or rule statement and lifts it with source citation — typically a Contract invariant or a §Pitfalls recovery pointer.

### Sub-op C — Fetch-scaffold

Consumer asks for a filled scaffold of an artifact type for a specific variant: "Give me an agent.md scaffold for a code-reviewer agent." The Librarian locates the guide's scaffold template (G10's Core Truths / Boundaries / Vibe / Continuity for agent.md; G1's Objective / Desired Outcomes / Constraints / Acceptance Criteria for spec documents) and fills in variant-appropriate defaults where the concept file provides them, leaving `{{placeholder}}` for consumer-specific slots.

### Sub-op D — Catalog

Consumer asks "what templates / rules / scaffolds exist?" without naming a specific one. The Librarian produces a flat index: each entry is `<guide>.md#<anchor>` + kind + one-line summary. No bodies lifted at this stage — the consumer picks an entry and the Librarian fetches that one next.

## Default composition rule

`fetch` composes two inputs:

1. **Concept file** for the artifact class being fetched — provides the cross-reference to which guide(s) carry the `### Templates` / `### Rules` / `### Examples` sections for that class.
2. **Named subsection** of the guide — specifically `### Templates`, `### Rules` (if the guide has an explicit rule section), `### Worked Examples`, or a specific sub-heading the consumer named. Fetch reads the subsection and lifts its body.

No de-duplication, no cross-guide stitching (fetch is a single-target operation per sub-op A/B/C), no confidence calibration (either the artifact exists and is lifted, or it does not exist and fetch reports the gap).

### Composition details

**(a) Exact vs fuzzy name match.** If the consumer names the template exactly as it appears in the guide's `### Templates` heading, direct anchor match. If the name is approximate, grep across `### Templates` / `### Rules` headings and match on token overlap. If multiple candidates match, list them and ask which.

**(b) Variable substitution.** When the fetched content has `{{placeholder}}` variables and the consumer has committed values for some (e.g., fetch-scaffold for "a code-reviewer agent" → substitute `{{AGENT_NAME}}` with "CodeReviewer"), substitute what's committed, leave the rest as placeholders. Do not invent defaults.

**(c) Source citation.** Every fetch response cites the source anchor at the top: "Lifted from `<guide>.md#<anchor>`." The consumer must be able to navigate back to the guide-native version.

**(d) Catalog sub-op pulls manifests, not bodies.** When fetching a catalog ("show me all templates"), read the `### Templates` headings across the relevant concept's composed guides and list them. Keep the catalog flat — no nested summaries.

## Procedure

Three phases (fetch is lighter than audit / diagnose / design).

### Phase 0 — Parse the query

Parse verb + noun + artifact name (or "catalog"). Verb must be `fetch` or a synonym ("give me," "show me," "where's the," "get"). Artifact noun identifies sub-op: "template" → A; "rule" → B; "scaffold" → C; "all / any / what's available" → D.

If the artifact name is ambiguous (multiple templates could match), list candidates and ask which.

### Phase 1 — Locate and lift

**Sub-ops A/B/C:** Read the concept file to locate the source guide. Read the named subsection in the guide. Apply variable substitution per composition step (b).

**Sub-op D:** Read `### Templates` / `### Rules` headings across the concept's composed guides. Produce a flat index.

### Phase 2 — Emit with citation

Emit the lifted body (for A/B/C) or flat index (for D) with source-anchor citation at the top. Include variable-slot hints (e.g., "Placeholders remaining: `{{T0_BUDGET}}`, `{{AGENT_NAME}}`") so the consumer sees what they still need to fill.

## Consumer input handling

Expected input: artifact kind + name (or "catalog"). If the consumer asked for a scaffold, expect one variant qualifier (e.g., "for a code-reviewer agent" or "for a background review agent"). If the variant is unstated, ask — scaffolds without variant context are generic and low-value.

| Query shape | Sub-op | Substrate |
|---|---|---|
| "Give me a template for X" (UC-2.1) | A (fetch-template) | Concept file → guide's `### Templates` section |
| "Give me the rule about X" (UC-2.3) | B (fetch-rule) | Concept file → guide's Contract invariant or Pitfall recovery |
| "Give me an agent.md scaffold for X" (UC-2.4) | C (fetch-scaffold) | `agent.md` concept → G10 §Templates (Core Truths etc.) + variant-aware substitution |
| "Show me all available templates" (UC-2.2) | D (catalog) | `*` meta — walk `### Templates` headings across guide set |

## Output shape

```
## Fetch — <artifact name or catalog>

**Interpreted as:** (verb: fetch, sub-op: <A/B/C/D>, artifact: <name>, variant: <if applicable>)
**Source:** <guide>.md#<anchor>
**Placeholders remaining:** <list, if any>

---

<lifted body, verbatim from guide, with {{placeholder}} preserved for unfilled slots>

---

### Next-step suggestion (optional)

<One line: "once filled, you can audit this against <rubric>" or "pair this with <adjacent artifact>".>
```

Catalog sub-op emits a flat index instead of a lifted body:

```
## Fetch — Catalog of <artifact class>

| Name | Source | Kind | One-line summary |
|---|---|---|---|
| Context Budget | structuring-agent-context.md#context-budget | Template | Tiered token-budget worksheet with cache markers |
| Trust Ledger | agent-governance-and-trust.md#trust-ledger | Template | Per-agent autonomy-tier ledger |
| … |
```

## Governance and boundaries

- Fetch is **read-only on substrate**. The Librarian does not author new templates / rules / scaffolds when the substrate has none. A missing artifact is a gap report, not a generation task.
- Fetch does not wrap or synthesize. If the consumer asks for "a simplified version" of a template, that is a `design` or future `synthesize` operation — not fetch.
- Fetch does not invent variable defaults. Unfilled placeholders stay visible.
- Fetch cites every lifted body. Uncited lifts are forbidden — consumers must be able to navigate to source.

## Token-budget note

Per read-contract §Token-budget awareness: fetch consolidates three sub-ops into one file today. If the file grows past the ~600-line operation-file threshold as procedures thicken, split into `fetch-template.md` / `fetch-rule.md` / `fetch-scaffold.md` + a thin catalog operation. Nick's session-49 guidance: prefer collapse for now; split only when forced.

## Cross-references

- Read-contract (§8.5 input handling for fetch): `operations/references/librarian/read-contract.md`.
- Related operations: `audit.md`, `design.md` (design often lifts templates inline — the mechanism shared with fetch-template is the same anchor-lifting primitive).
- Related concepts: all concept files — any of them can route a fetch query to its source-guide templates/rules.
- Use-case registry (UC-2.1–2.4): `operations/references/librarian/use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role — rules / templates / examples are three of the four subsection kinds DD-78 standardizes), DD-82 (IL 4-agent architecture).
