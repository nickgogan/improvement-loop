---
operation: diagnose
type: operation
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "claude"
stage: "draft"
tags:
  - "librarian-operation"
  - "diagnose"
  - "debug"
aliases:
  - "Diagnose"
  - "Debug"
  - "Symptom to cause"
---

# Diagnose

## Short definition

**Diagnose** takes a consumer-reported symptom and maps it to likely causes, with recovery pointers. Input is a natural-language symptom description — "my agent keeps losing track of constraints," "my tool calls are erratic," "my skill isn't being triggered." Output is a hypothesis-ranked cause list with citations back to the Pitfalls section(s) of the governing guide(s) plus any patterns/findings that carry the mechanism.

Diagnose is a *consumption* operation like audit: read-only on substrate, read-only on anything the consumer provides. Diagnose does not fix, does not redesign, does not deploy. If the consumer wants a redesign after the diagnosis, hand off to `design` (planned) or to the specific sub-operation the cause indicates.

## Default composition rule

`diagnose` composes three inputs:

1. **Concept file** for the noun the symptom attaches to — provides the composition table (which guides carry the Pitfalls and mechanism material for this artifact/domain). Examples: "agent forgets across sessions" → `memory.md` (Variant B/D); "agent loses constraints mid-session" → `context-rot.md`; "skill not triggered" → `skill.md`; "tool calls erratic" → `agent.md` (tool aspect).
2. **Pitfalls + Recovery subsections** of the named guides — guides' Pitfalls sections are authored as symptom→cause enumerations; Recovery gives the remediation pointers. These are the rubric.
3. **Key Concepts** subsections of the named guides (optional) — pulled when the consumer asks "why does this happen" alongside "how do I fix it."

Pitfalls sections function as emergent diagnostic criteria by construction (they were authored to catch known failure modes; the Librarian re-reads them at query time rather than re-deriving the symptom map). No view-artifact curation required.

### Composition details

**(a) Symptom-anchor matching.** The consumer's symptom usually anchors to a small number of Pitfalls entries — 1 to 4 across one or two guides. The Librarian matches by phrase (symptom → Pitfalls heading) first; if no heading matches, falls back to keyword search across the composed Pitfalls sections and reports the looseness of the match.

**(b) Mechanism layering (optional Key Concepts pull).** When the consumer explicitly asks "why" (or when the Librarian's confidence on a cause is medium), pull the relevant Key Concept to explain the mechanism behind the Pitfall. Do this sparingly — most diagnoses do not need mechanism depth.

**(c) Tier-2 escalation on low Tier-1 confidence.** If a Pitfalls match is vague or summarized, escalate to a pattern/finding that carries the mechanism directly. `context-rot-silent-killer-and-mitigations` and `context-rot-attention-budget-depletion` are canonical examples for context-rot symptoms; `gsd-global-learnings-store-cross-session-persistence` is canonical for cross-session forgetting.

**(d) Confidence discipline.** Diagnoses are inherently probabilistic — the same symptom can have multiple causes. Rank causes by likelihood from substrate evidence; label each with a confidence level; never ship a single cause as certain unless the symptom maps cleanly to one Pitfalls entry with one Recovery path.

## Procedure

Five phases. The Librarian executes top-to-bottom and returns a single diagnosis report. No partial streaming mid-phase.

### Phase 0 — Parse the query

Parse verb + noun. Verb must be `diagnose` or a synonym (debug, troubleshoot, "my agent keeps …", "why is … failing"). Noun identifies the domain the symptom attaches to — memory, context, tool use, skill loading, etc.

If the symptom is ambiguous on a dimension that changes the diagnosis ("my agent is slow" — latency? throughput? convergence?), ask *one* qualifying question. Do not chain interrogations. Per read-contract §8.2: reproduction steps are not required — consumers may not have them.

### Phase 1 — Load composition

Read the concept file for the noun. Read the `### Pitfalls` and `### Recovery` subsections of each guide named in the concept's composition table's "diagnose" / "symptom" / "failure mode" rows. Do not read full guide bodies at this phase. Heading-match (`^## Pitfalls`) until the anchor manifest lands.

If the symptom spans multiple concepts (e.g., "my autonomous agent forgets constraints across handoffs" — context-rot + memory + agent autonomy), load all relevant concept files and pool their composed Pitfalls sections. Cross-concept diagnosis is first-class.

### Phase 2 — Build symptom map

Pool Pitfalls entries from all composed guides. Apply:

1. **Symptom-anchor matching (step a).** Match the consumer's symptom against Pitfalls headings + body text.
2. **Rank by match strength.** High (headings match nearly verbatim), medium (body text matches), low (keyword-only match — flag the looseness).
3. **Deduplicate overlapping causes.** When two guides flag the same cause (e.g., "stale context" in G2b and G7), collapse to one row citing both guides.

Emit the ranked cause list as the core of the working report.

### Phase 3 — Attach recovery

For each cause in the ranked list:

1. Locate the matching `### Recovery` entry in the source guide (or the closest-adjacent entry when Recovery is not indexed by Pitfall).
2. Pull the remediation pointer — typically a cross-reference to a Steps subsection (the "how to fix it" content) or to a template/example.
3. If the consumer's follow-up will likely be `(design, same-concept)` or `(audit, same-artifact)`, preview that handoff — "once you pick a fix, re-audit with X" or "design-mode pass will walk the fix sequence."

### Phase 4 — Mechanism layering (optional)

If the consumer asked "why," or if any cause's confidence is medium, pull the relevant Key Concept(s) from the composed guides and attach as a short mechanism gloss — one or two lines per cause, not a restatement of the guide.

### Phase 5 — Tier + confidence + provenance pass

- Attach **tier** to every cause: Tier 1 for guide-Pitfalls evidence; Tier 2 if the cause was strengthened by a pattern/finding; Tier 3 only when the consumer explicitly asked for a reference-implementation comparison.
- Attach **confidence** per cause: high (symptom matches a Pitfalls entry nearly verbatim, one Recovery path), medium (Pitfalls match is body-level not heading-level, or two Pitfalls co-fire), low (symptom is ambiguous or the Pitfalls match is keyword-only — state the looseness). Low-confidence diagnoses must be labeled as hypotheses, not claims.
- If no Pitfalls entry in the composed guides maps to the symptom, state it: "No IL guide Pitfall covers this symptom directly. Closest-adjacent: X." Never force a diagnosis.

## Consumer input handling

The consumer submits the symptom inline as free text. The Librarian does **not** require reproduction steps, traces, or logs — a serviceable symptom description is typically a sentence or two. If the symptom depends on context that disambiguates the concept mapping (single-session vs cross-session, latency vs convergence), ask one clarifying question before loading.

Inputs expected:

| Symptom domain | Noun concept file | Composed guides |
|---|---|---|
| Losing constraints, drifting quality mid-session, degradation after N turns | `context-rot.md` | G2b Pitfalls + Session Discipline / Compaction Timing (recovery) |
| Forgetting across sessions, re-doing work, losing facts | `memory.md` (Variants B, D) | G7 Pitfalls + Part 1/2 (recovery), G2b §Memory File Discipline |
| Erratic tool calls, wrong arguments, wrong sequencing | `agent.md` (tool aspect) | G5 Pitfalls + Procedure (recovery), G8 Pitfalls (prompt-side of tool calling) |
| Skill not triggered when it should be, skill mis-loaded | `skill.md` | G3b Pitfalls + Procedure (trigger quality is G8 Pitfalls) |
| Agent autonomy / HITL gap surfaced at runtime | `agent.md` (autonomous variant) | G9 Pitfalls + Sections 1–3 (trust ledger / review process) |
| Harness-wide symptom (permissions leak, hook mis-fire) | `harness.md` | Cross-guide sweep: G6, G3b, G5 Pitfalls |

For symptoms with no concept file match, state the gap and fall back to the guide routing table — walk the practitioner questions there and attempt a best-effort diagnosis with the gap flagged.

## Output shape

```
## Diagnose — <symptom restated>

**Interpreted as:** (verb: diagnose, noun(s): <n> [variant: <var>])
**Composed guides:** <list>
**Rubric size:** <N Pitfalls entries considered, K matched>

### Likely causes (ranked)

| # | Cause | Source Pitfall | Mechanism (1 line, if pulled) | Recovery pointer | Tier | Confidence |
|---|---|---|---|---|---|---|
| 1 | … | G2b Pitfalls §"…" | Attention-budget depletion (G2b §Key Concepts) | G2b §Compaction Timing (proactive compaction) | 1 | High |
| 2 | … | G7 Pitfalls §"…" | — | G7 §Part 1 §Step 1.2 | 1 | Medium |
| … |

### Unmatched aspects (if any)

<If the consumer's symptom has facets that no Pitfalls entry covers — state them, don't pretend. Suggest what additional detail would raise confidence.>

### Next-step suggestion

<One line: typically either "re-audit after the top fix" or "if the top cause doesn't match, the second-ranked is <X>". Never a dump.>
```

## Governance and boundaries

- Diagnose is **read-only on substrate and on anything the consumer provides**. The Librarian never modifies the consumer's artifact or the KB.
- Diagnose does not propose a redesign beyond the Recovery pointers. If the consumer wants a redesign, hand off to `design`.
- Diagnose does not file gap reports autonomously — if a symptom surfaces a KB gap, report it to the consumer (per Librarian agent Recovery contract) and include in the trailing gap-report section per read-contract §Step 6.4.
- If the symptom implies a destructive action is at fault (e.g., "my agent deleted files it shouldn't have"), pivot the diagnosis toward G6 (safety) and G9.I6 (destructive-action gating) regardless of the surface concept. This is a standing lift-safety rule.

## Cross-references

- Read-contract (Step 1 verb extraction, §8.2 input handling): `project-management/design-notes/2026-04-21-librarian-read-contract.md`.
- Related operation: `audit.md` (this directory) — similar procedure shape; audit fires Invariants as criteria, diagnose fires Pitfalls as criteria.
- Related concepts: `memory.md`, `context-rot.md`, `agent.md`, `skill.md`, `harness.md` (this directory).
- Use-case registry (UC-4.1–4.5): `project-management/design-notes/2026-04-21-librarian-use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role; Pitfalls as emergent diagnostic criteria — same mechanism as Invariants-as-audit-criteria), DD-82 (IL 4-agent architecture).
