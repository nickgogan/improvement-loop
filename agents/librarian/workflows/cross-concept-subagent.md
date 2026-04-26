---
title: "Cross-Concept Subagent Template"
type: "workflow"
target_system:
  - "improvement-loop"
agent: "librarian"
created: "2026-04-26"
updated: "2026-04-26"
source_design:
  - "project-management/design-notes/2026-04-21-librarian-read-contract.md (§1.4, §9.5, Q4)"
  - "project-management/design-notes/2026-04-21-librarian-use-case-registry.md (UC-9.2)"
  - "project-management/design-notes/2026-04-22-librarian-boundary-case-tracking.md (cross-concept encounter)"
tags:
  - "workflow"
  - "librarian"
  - "subagent-template"
  - "cross-concept"
  - "compound-query"
  - "read-contract-q4"
---

# Cross-Concept Subagent Template

The Librarian's protocol for compound queries — `(operation × concept₁ × concept₂ [× …])`. Resolves read-contract §Open question Q4: each constituent `(operation × concept)` runs as a parallel subagent (Lucene-style); the parent Librarian recombines results into the consumer's answer.

This file is **two things at once**:

1. A **workflow** — what the parent Librarian does when it detects a compound query (decompose, dispatch, recombine).
2. A **prompt template** — the literal subagent prompt the parent passes to each child via the `Task` tool. The template lives in §"Subagent Prompt Template" below; the parent substitutes parameters and invokes.

## When to Use

The parent Librarian invokes this workflow when query parsing (read-contract §Step 1) yields **two or more concept nouns** for a single verb:

- "Design (an agent + a hybrid second brain) — in what order?" → `(plan, agent) + (plan, second-brain[hybrid])`. UC-9.2.
- "Diagnose (memory loss + context rot) in my long-running agent." → `(diagnose, memory) + (diagnose, context-rot)`.
- "Audit my agent.md and my SKILL.md." → `(audit, agent) + (audit, skill)`.

If the query has one verb + one concept (the common case), use the standard read-contract flow — do NOT invoke this template. Single-concept queries don't need parallelism.

If the query has multiple verbs (e.g., "audit my agent and design a successor"), the parent runs the primary verb's flow first per read-contract §1.1, then asks before running the secondary verb. Don't fan out across verbs silently.

---

## Decomposition Rules

After the parent parses the query into `(verb, [concept₁, concept₂, …])`:

1. **One subagent per concept.** Each `(operation, concept)` pair becomes one subagent invocation. Variants (e.g., `second-brain[hybrid]`) ride on the concept they belong to — same subagent.
2. **Same operation across all subagents.** All children share the verb. The operation file is loaded once per child (cheap; cached by the harness if applicable).
3. **Cap at 4 subagents.** If a query names more than 4 concepts, ask the consumer to scope. Beyond 4, recombination loses signal and Token cost grows superlinearly.
4. **Skip duplicates.** If two consumer-named nouns resolve to the same concept file (e.g., "agent and AI agent"), collapse to one subagent.
5. **Variant resolution before dispatch.** If a concept has variants (Agent, Memory, Second-Brain), the parent runs the variant heuristics from the concept file before constructing the subagent prompt — the child receives the resolved variant, not "ambiguous." If variant resolution is ambiguous, the parent asks the consumer **once** before dispatching (per read-contract §1.2(b)).

---

## Invocation

The parent dispatches subagents in parallel via the `Task` tool with `subagent_type: general-purpose`. One `Task` call per `(operation, concept)` pair, all in a single message for true parallelism (per the harness's parallel-tool-call discipline).

**Parameters substituted into the template:**

| Placeholder | Type | Source | Required |
|---|---|---|---|
| `{{OPERATION}}` | string (verb) | Parsed verb (read-contract §1.1 canonical) | yes |
| `{{CONCEPT}}` | string (concept slug) | Resolved concept file stem (e.g., `agent`, `second-brain`) | yes |
| `{{VARIANT}}` | string or `none` | Resolved variant if applicable; `none` otherwise | yes |
| `{{ORIGINAL_QUERY}}` | string | Verbatim consumer query — for grounding | yes |
| `{{SIBLINGS}}` | comma-separated list | Other `(op,concept[var])` pairs being dispatched in this round; lets the child flag cross-concept hooks for the parent | yes |
| `{{TIER_2_PERMITTED}}` | `yes` / `no` | `yes` only when the consumer's query carries an explicit Tier-2 trigger (per read-contract §4.1 signals 1–3); `no` by default | yes |

The parent constructs the prompt by substituting placeholders, then invokes:

```
Task(
  subagent_type="general-purpose",
  description="Librarian cross-concept: ({{OPERATION}}, {{CONCEPT}})",
  prompt=<rendered template body>
)
```

All N child invocations go in **one message** so they run concurrently.

---

## Subagent Prompt Template

Everything in the fenced block below is the literal prompt body. Substitute `{{...}}` placeholders before invocation. Do not include the fence in the rendered prompt. (Outer fence uses 4 backticks so the nested JSON shape parses correctly.)

````
You are a focused, read-only sub-Librarian dispatched to handle ONE constituent of a
compound consumer query. Another instance of you is handling a parallel constituent;
you do not coordinate. The parent Librarian will recombine your output with theirs.

## Inputs

- Operation (verb):  {{OPERATION}}
- Concept (noun):    {{CONCEPT}}
- Variant:           {{VARIANT}}     # may be "none"
- Original query:    {{ORIGINAL_QUERY}}
- Sibling subagents: {{SIBLINGS}}    # other (operation, concept[variant]) pairs running in parallel
- Tier-2 permitted:  {{TIER_2_PERMITTED}}   # yes | no

## Your Identity

You are a Librarian (improvement-loop knowledge-base interface) constrained to a single
(operation × concept) pair. The full Librarian read-contract governs you, but Steps 1
(query parsing) and 9.5 (cross-concept join) are handled by your parent — you handle
load → read → assemble → cite for your one pair only.

## Hard Constraints

- READ-ONLY. Never write, edit, or create any file. Never modify the KB. Never modify
  the consumer's submitted artifact (if any).
- NO clarifying questions. You run asynchronously in parallel — questions would block
  the dispatch round. If your inputs are ambiguous, surface the ambiguity in your
  output as a gap; do not stall.
- NO Tier-3 reads. Watched-library reads are gated by the parent Librarian after
  recombination (cost discipline per read-contract §5.3). If a Tier-3 read would
  resolve a question, surface it as a `tier_3_candidate` in your output.
- NO general-knowledge padding. KB-grounded only. If the substrate is thin, return a
  `gap` entry — never fill from training data.
- Respect the Tier-2 gate. If `Tier-2 permitted: no`, do not traverse `related_findings`
  edges. If `yes`, follow the read-contract §4.2 traversal rules with the 3-hop ceiling.
- DO NOT recombine across concepts. The parent does that. Your output is single-concept
  scoped, with `cross_concept_hooks` flagging dependencies/conflicts for the parent.

## Procedure

1. **Load operation file.** Read systems/improvement-loop/operations/references/librarian/{{OPERATION}}.md.
   Capture: default composition rule (which guide subsection kinds to read),
   procedure, output shape, consumer-input expectations.

2. **Load concept file.** Read systems/improvement-loop/operations/references/librarian/{{CONCEPT}}.md.
   If `{{VARIANT}}` is not "none", read the variant subsection within the concept file.
   Capture: composition table (aspect → guide anchors / patterns / watched-libs),
   Librarian read rule, depth-escalation default.

3. **Tier-1 reads.** For each aspect surfaced by the operation × concept composition,
   read ONLY the operation-specified subsection kind from the concept-specified guide
   anchor (per read-contract §3.1). Use anchor IDs if available; fall back to
   heading-match (`grep -n "^## <heading>"`) and flag the provenance caveat.

4. **Tier-2 reads (gated).** Only if `Tier-2 permitted: yes` and a §4.1 signal fires:
   traverse `related_findings` edges. Quote findings; cite by slug. Hard-stop at 3
   hops total or when leaving the concept's territory.

5. **Assemble.** Compose the operation's per-concept output shape. Apply the
   operation's composition rules (e.g., for `audit`: precondition gating + de-dup +
   hierarchical overlap annotation). Tag every claim with confidence (H/M/L) per
   read-contract §6.1 and a citation per §7.

6. **Cross-concept hooks.** Scan your output for places where a sibling concept (from
   `{{SIBLINGS}}`) is named, depended on, or contradicted. Surface each as a
   `cross_concept_hooks` entry (see Output below) — the parent uses these to weave the
   joined response.

7. **Return structured output.** Emit the JSON-serializable shape below. Do not write
   it to a file — return it as your final message body.

## Output Shape

Return a fenced JSON block with EXACTLY this shape (no extra fields, no missing fields).
Use empty arrays for empty sections; do not omit keys.

```json
{
  "operation": "{{OPERATION}}",
  "concept": "{{CONCEPT}}",
  "variant": "{{VARIANT}}",
  "tier_trace": {
    "tier_1_sections": <int>,
    "tier_2_findings": <int>,
    "tier_3_reads": 0
  },
  "claims": [
    {
      "claim": "<one-sentence claim>",
      "confidence": "H | M | L",
      "citations": [
        { "tier": 1, "ref": "<guide-file>#<anchor-or-heading>" },
        { "tier": 2, "ref": "<finding-or-pattern-slug>" }
      ],
      "inference_note": "<empty if quoted verbatim; one line if Librarian inferred>"
    }
  ],
  "operation_specific_output": {
    "<key>": "<value>",
    "_note": "Shape determined by the operation file. Examples: audit → findings table; plan → ordered phase list; design → composition table; decide → tradeoff matrix; explain → mechanism narrative; diagnose → symptom→cause map; fetch → anchored content; whats-new → date-filtered listing; coverage → counts."
  },
  "cross_concept_hooks": [
    {
      "sibling": "<sibling concept slug from {{SIBLINGS}}>",
      "kind": "depends-on | conflicts-with | shares-invariant | sequences-before | sequences-after",
      "detail": "<one line — what the parent needs to weave>",
      "citation": "<tier-1-or-2 ref>"
    }
  ],
  "gaps": [
    { "kind": "missing-substrate | broken-pointer | ambiguous-input | thin-coverage", "detail": "<one line>" }
  ],
  "tier_3_candidates": [
    { "watched_lib": "<lib name>", "rationale": "<why a Tier-3 read would help>" }
  ],
  "degradation_notes": [
    "<one line per fallback used: missing operation file → runtime aggregation, anchor-pointer-not-resolved → heading-match, etc.>"
  ]
}
```

## What "Done" Looks Like

You return one message containing:
1. A one-paragraph natural-language summary (≤80 words) of what you found for this
   (operation, concept[variant]) pair — for the human reading parallel subagent runs.
2. The JSON output block above — for the parent's recombination logic.

That's it. No file writes. No follow-up offers. No recommendations beyond what your
operation_specific_output naturally produces.
````

---

## Recombination Logic (Parent Side)

After all child subagents return, the parent Librarian:

1. **Validate JSON shape.** If a child returned malformed JSON (missing required keys, extra keys), treat that subagent's output as degraded — surface in the final response's gap report under "subagent malformed output" and recombine with what's parseable.

2. **Apply the operation's join rule.** Read the operation file's join section (each operation file's procedure tells the Librarian how to compose multiple concept outputs). Examples:
   - `plan`: order the per-concept phase lists, weaving cross-concept dependencies from `cross_concept_hooks` into the sequence; surface `sequences-before` / `sequences-after` as explicit ordering constraints.
   - `audit`: union the per-concept rubrics; collapse `shares-invariant` hooks into single rows; preserve concept-specific findings as separate rows with concept-tagged columns.
   - `design`: union composition tables; flag aspects where `conflicts-with` hooks fire; surface `depends-on` as prerequisite ordering.
   - `decide`: present per-concept tradeoffs side-by-side; surface contradicting claims (different concepts, same aspect, opposing recommendations) as design debates.
   - `diagnose`: merge symptom→cause maps; cluster causes that recur across concepts.
   - `explain`: weave per-concept mechanism narratives, calling out interactions where hooks fire.
   - `fetch`: per concept, return its anchored content; do not synthesize across concepts.
   - `whats-new`: union date-filtered listings; date-order globally.
   - `coverage`: aggregate counts; surface concept-pair coverage gaps.

3. **Resolve confidence conflicts.** When two children's claims overlap (same substrate, different children):
   - Same claim, different confidence → take the lower confidence; note the divergence as a `divergence_note`.
   - Contradicting claims, both H → surface as a contradiction in the final response (read-contract §6.4 gap-report style) with both citations.
   - Contradicting claims, mixed confidence → take the higher-confidence claim; surface the lower-confidence dissent in the gap report.

4. **Merge tier traces.** Sum `tier_1_sections` and `tier_2_findings` across children. Tier-3 stays at zero by construction.

5. **Merge gaps and Tier-3 candidates.** Deduplicate; cluster by `kind`. Tier-3 candidates surface to the consumer as a single "ask if you want a Tier-3 look" prompt — never auto-fetched (read-contract §5.1).

6. **Construct final response.** Per read-contract §Step 10 output shape:
   - **Query restatement** — explicitly note the decomposition. Format: `Interpreted as a compound query, decomposed into: {(op, c1[v1]), (op, c2[v2]), …}`.
   - **Tier trace** — one line, summed.
   - **Per-operation output** — joined per the operation's rule above.
   - **Cross-concept synthesis** — short section calling out interactions (depends-on chains, conflicts, shared invariants).
   - **Confidence tags** — per claim, post-resolution.
   - **Citations** — per claim.
   - **Gap report** — merged + concept-tagged.
   - **Next-step suggestions** — at most two.

---

## Worked Example: UC-9.2

**Consumer query:** "I want an agent + hybrid second brain — in what order?"

**Parent parse:** `(verb=plan, concepts=[agent (variant=ambiguous → ask), second-brain (variant=hybrid)])`. Variant resolution for `agent` is ambiguous; parent asks one disambiguating question per read-contract §1.2(b). Suppose consumer answers "harness-based agent."

**Parent dispatch (single message, two parallel `Task` calls):**

- Subagent A: `(plan, agent[harness-based])` — reads `plan.md` + `agent.md` (harness-based variant section) + Tier-1 lifecycle phase guides. Returns claims, phase list, cross-concept hooks pointing at `second-brain`.
- Subagent B: `(plan, second-brain[hybrid])` — reads `plan.md` + `second-brain.md` (hybrid variant section) + Tier-1 lifecycle phase guides. Returns claims, phase list, cross-concept hooks pointing at `agent`.

**Likely cross-concept hooks A→B:** `depends-on` (agent's "operate" phase consumes the second-brain), `sequences-after` (second-brain's "specify" phase precedes agent's "build" phase — the agent needs the schema first).

**Likely cross-concept hooks B→A:** mirror of above, plus `shares-invariant` (read-contract's "no autonomous KB modification" applies to both).

**Parent recombines via plan.md's join rule:** weaves a single phase-ordered roadmap, with each phase tagged for which concept it advances and explicit dependency arrows for the cross-concept hooks. Surfaces shared invariants once, not per concept.

**Final response shape:**
```
Interpreted as a compound query, decomposed into:
  (plan, agent[harness-based]), (plan, second-brain[hybrid])

Read: 6 Tier-1 sections; 0 Tier-2 findings; 0 Tier-3 reads.

# Phase-ordered roadmap

Phase 1 — Specify (second-brain) [H]
  Define the second-brain's schema and read/write policy. Citation: G1#step-2-spec ...
  This precedes the agent's build phase — the agent depends on the schema. [cross-concept: sequences-before agent.build]

Phase 2 — Build (second-brain) [H]
  ... [citations]

Phase 3 — Specify (agent) [H]
  ... [citations]

Phase 4 — Build (agent) [M]
  Now the agent can be built against the materialized second-brain. [cross-concept: depends-on second-brain]
  ...

[further phases ...]

## Cross-concept synthesis
- The second-brain's schema is a precondition for the agent's specification — sequence the second-brain's specify+build phases before the agent's specify phase.
- Both concepts inherit the read-contract's "no autonomous KB modification" invariant — the agent cannot rewrite the second-brain at runtime without an explicit gate.

## Gaps
- No Tier-1 substrate covers hybrid-second-brain ↔ harness-based-agent boundary explicitly. Tier-2 escalation candidate if the consumer wants depth.

## Next-step suggestions
- If you want depth on the operate-phase consumption pattern, ask for `(explain, agent[harness-based] × second-brain[hybrid])`.
- If you want to scope the second-brain schema specifically, run `(design, second-brain[hybrid])`.
```

---

## Constraints and Boundaries

**The template enforces (parent's responsibility to honor):**

- One subagent per `(operation × concept[variant])` pair — no fan-out within a child.
- Cap at 4 children per dispatch round. If 5+ concepts, scope with the consumer first.
- All children dispatched in a single parent message for true parallelism.
- Tier-2 permission set at the parent level per read-contract §4.1 — children do not unilaterally escalate.
- Tier-3 always zero at child level — parent gates after recombination.

**The template cannot enforce (and does not try to):**

- Whether the consumer's query is well-formed (parent handles via read-contract §Step 1).
- Whether the resulting recombined output is what the consumer wanted (consumer feedback per §Step 10).
- Token-budget compliance of the children's output (judgment call; if a child returns excessive content, parent trims at recombination).

---

## Failure Modes

| Failure | Detection | Recovery |
|---|---|---|
| Child returns malformed JSON | Parent JSON parse | Surface in final gap report; recombine with parseable children. |
| Child times out / errors | `Task` tool error | Re-dispatch once with the same parameters; if it fails again, surface as a degraded-subagent gap and recombine with the rest. |
| Two children return contradicting H-confidence claims | Recombination step 3 | Surface as a contradiction in the final response with both citations; do not silently pick one. |
| Cross-concept hooks reference a sibling that wasn't dispatched | Recombination step 1 validation | Drop the hook; flag in the parent's degradation notes. (Indicates the consumer named more concepts than the parent decomposed — surface for re-parse next time.) |
| Operation file lacks a documented join rule for the operation | Recombination step 2 | Fall back to per-concept side-by-side output with cross-concept hooks called out as a separate "interactions" section. Flag as a reference-layer gap (needs operation-file amendment). |
| Variant resolution still ambiguous after one ask | Pre-dispatch | Dispatch with both variants as parallel sub-children, label them, surface in restatement; or ask the consumer to pick — parent's call based on operation cost. |

---

## Cross-References

- **Read-contract** (governing protocol): `project-management/design-notes/2026-04-21-librarian-read-contract.md` — §1.4 cross-concept query case, §9.5 boundary handling, Q4 design intent.
- **Use-case registry** (UC-9.2 worked example): `project-management/design-notes/2026-04-21-librarian-use-case-registry.md`.
- **Boundary-case tracking** (cross-concept encounter type, §"cross-concept" → Subagent template work): `project-management/design-notes/2026-04-22-librarian-boundary-case-tracking.md`.
- **Reference layer** (operation + concept files): `operations/references/librarian/`.
- **Librarian agent definition** (governance carry-through): `agents/librarian/agent.md`.
- **Sibling workflow** (single-concept queries): `agents/librarian/workflows/kb-query.md`.
- **Governing DDs:** DD-78 (ContractSpec), DD-82 (IL 4-agent architecture), DD-86 (Owner / Librarian responsibilities).
