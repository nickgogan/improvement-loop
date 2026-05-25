---
name: assess-prompt
description: >-
  Extend a /prompt-evaluator run with IL-KB-grounded additions that fire only
  where the prompt invokes them — G2a/G2b Contract specifics if the prompt embeds
  context, G5 Contract specifics if it embeds tool directives, G1 spec-level
  invariants if it is a spec document, plus Tier-2 IL findings surfaced against
  weak 4-discipline dimensions. Does not duplicate /prompt-evaluator's rubric.
  If no IL extension fires, reports that the 4-discipline scorecard is
  sufficient and exits.
user-invocable: true
allowed-tools: Read Grep Glob Skill Write
argument-hint: "<prompt-text|file-path> [--evaluator-output <path-to-prior-/prompt-evaluator-output>]"
---

# Assess Prompt

Extension wrapper over `/prompt-evaluator`. Does not re-run the 4-discipline
rubric; adds only IL-specific findings that `/prompt-evaluator` structurally
cannot produce. Intelligence lives in `audit.md` (operation) × `prompt.md`
(concept) in the Librarian reference layer.

## When to Use This Skill

- Consumer wants an IL-KB-grounded *addition* to a `/prompt-evaluator` run —
  not a replacement for it.
- Consumer's prompt embeds context (long CLAUDE.md, system prompt with pre-
  loaded material, spec document), tool directives, or is harness-specific
  (Claude-tuned caching or model selection).
- Consumer has already run `/prompt-evaluator` and wants the mechanism-level
  substrate behind any weak dimension.

## When to Use `/prompt-evaluator` Alone Instead

- One-shot prompts with no embedded context and no tool directives.
- Generic prompts targeting multiple model providers.
- Quick best-practice scorecard without IL overlays.

If the consumer asks for "a prompt audit" without qualification, default to
`/prompt-evaluator` alone and ask whether the IL extension is wanted.

## What This Skill Does NOT Do

- Does not duplicate `/prompt-evaluator`'s 4-discipline rubric.
- Does not rewrite the prompt. Read-only.
- Does not fire G2a/G2b or G5 invariants on prompts whose Preconditions are
  unsatisfied — precondition gating (audit.md composition rule c) is
  non-negotiable.

## Cognitive Disposition

Librarian Audit — read-only, citation-grounded, *minimal*. The bias is
toward reporting "no IL additions apply" rather than inventing redundant
findings. Every firing invariant must be something `/prompt-evaluator`'s
rubric could not reach.

## Paths

| Path | Purpose |
|------|---------|
| `.claude/skills/prompt-evaluator/SKILL.md` (workspace root) | Baseline — invoked first |
| `systems/improvement-loop/operations/references/librarian/audit.md` | Operation file — composition rules, procedure |
| `systems/improvement-loop/operations/references/librarian/prompt.md` | Concept file — IL-extension composition table |
| `systems/improvement-loop/extracts/guides/` | Substrate — Contract subsections for {G1, G2a, G2b, G5} when they fire |
| Consumer-provided path | Prompt under audit |

## Procedure

### Step 0: Parse input and classify triggers

1. Accept prompt as inline text or file path. If path, `Read` it.
2. Classify the prompt against the IL-extension firing conditions:
   - **Embeds context?** — prompt loads source material, references documents,
     pre-loads factual content, or contains a long stable context block.
   - **Embeds tool directives?** — prompt instructs how to call tools, use
     MCP servers, invoke skills, or routes work to sub-agents.
   - **Is a spec document?** — > ~500 lines, document-scale, CLAUDE.md-
     equivalent.
   - **Targets Claude / a specific harness?** — prompt names a Claude model,
     uses Claude-specific mechanisms (prompt caching, thinking, tool-use API),
     or is tied to a harness config.
3. Record the classification. If **no** triggers fire, proceed to Step 1 —
   but the IL extension will exit early in Step 3.

### Step 1: Obtain the `/prompt-evaluator` baseline

Two modes:

- **Consumer supplies prior output** (`--evaluator-output <path>`): `Read` it.
  Proceed.
- **No prior output**: invoke `/prompt-evaluator` via the `Skill` tool on the
  same prompt. Capture its scorecard output. Proceed.

If the consumer explicitly declines the `/prompt-evaluator` baseline, note
that decision in the output and proceed to Step 2 regardless — but the
integrated output will carry only IL findings, not the 4-discipline
scorecard.

### Step 2: Load IL composition

1. `Read` `operations/references/librarian/audit.md` — procedure and
   composition rules.
2. `Read` `operations/references/librarian/prompt.md` — IL-extension
   composition table.
3. For each firing trigger, load the corresponding Contract subsection:
   - Embeds context → `Read` G2a §Contract in `structuring-agent-context.md`
     (structuring) and G2b §Contract in `defending-agent-context.md` (degradation).
   - Embeds tool directives → `Read` G5 §Contract in `designing-agent-tools.md`.
   - Spec document → `Read` G1 §Contract in `writing-agent-specifications.md`.
   - Harness-specific → Tier-2 only; skip Tier-1 load.

If **no** triggers fired in Step 0 and the consumer did not ask for Tier-2
mechanism surfacing, skip Step 2 entirely and proceed to early-exit in Step 3.

### Step 3: Apply IL extensions (or early-exit)

**Early-exit path.** If no IL-extension trigger fired AND no `/prompt-evaluator`
dimension scored weakly in a way that the IL has mechanism substrate for, the
skill reports:

> "IL audit adds no further findings beyond `/prompt-evaluator`'s output.
> The 4-discipline scorecard is sufficient for this prompt. Trigger conditions
> checked: context-embedding (false), tool-directives (false), spec-document
> (false), harness-specific (false). Weak 4-discipline dimensions with IL
> mechanism substrate: none."

And exits.

**Extension path.** For each firing trigger, apply the loaded Contract
invariants per `audit.md` Phases 2–3:
1. Precondition gating — confirm the guide's Preconditions are satisfied.
2. De-duplication — skip any IL invariant that restates a 4-discipline
   dimension's finding.
3. File-verifiable vs system-verifiable split — IL findings become either
   concrete findings against the prompt text OR follow-up questions to the
   consumer.

For any 4-discipline dimension that scored weakly in Step 1, check whether the
IL has a Tier-2 finding that explains the weakness at mechanism level. If so,
surface it as a mechanism pointer (not as a duplicate finding).

### Step 4: Assemble integrated output

Single integrated report. Not two separate scorecards.

```
## Prompt audit — integrated view

**Prompt:** <path or summary>
**Triggers fired:** <list of IL extensions that fired, or "none">

---

### 4-discipline scorecard (from /prompt-evaluator)

<paste /prompt-evaluator's scorecard table verbatim>

---

### IL extensions

#### Context specifics (G2a/G2b) — <fired | not applicable | exited-no-preconditions>

<If fired: table of IL findings with citations, confidence tags, and evidence
quotes from the prompt. If not fired: one-line statement of why.>

#### Tool-directive specifics (G5) — <fired | not applicable>

<Same shape as above.>

#### Spec-document quality (G1) — <fired | not applicable>

<Same shape as above.>

#### Mechanism substrate for weak 4-discipline dimensions

<If /prompt-evaluator flagged weak dimensions and IL has mechanism findings
for them: Tier-2 pointer list. Otherwise: "No mechanism substrate surfaced.">

---

### Summary

<1–3 sentences: what the 4-discipline scorecard told us, what the IL extension
added on top, what is load-bearing to fix.>
```

### Step 5: Confidence + provenance pass

Per `audit.md` Phase 5. Every IL-extension finding carries a confidence tag
(H/M/L) and a citation (`<guide>.md#<anchor>` with line range; Tier-2 as
finding file path + slug). Include a tier trace at the bottom: "Read: N
Tier-1 sections; M Tier-2 findings; 0 Tier-3 reads."

## Output Shape

See Step 4. Integrated view is the only acceptable shape — no separate IL-only
output when `/prompt-evaluator` has run.

## Boundaries

- If the submitted artifact is clearly an agent artifact (has architecture /
  workflow / governance sections), suggest `/assess-agent` as the better fit.
- If the submitted artifact is a skill, suggest `/assess-skill`.
- If the consumer wants only the IL lens without `/prompt-evaluator`, honor
  that but state the coverage gap explicitly ("running IL extension only;
  4-discipline baseline was skipped at consumer request").

## Boundary-Case Encounter Logging

On any deviation from the Tier-1 happy path (the 13-type encounter taxonomy — missing concept/operation, ambiguous verb/variant, cross-concept, verb-noun-mismatch, oversized-artifact, hop-ceiling-hit, tier-3-read, low-confidence, kb-gap, redirect, clarification-asked), append a structured record to `operations/system-log/session-<N>-librarian-encounters.md` per the entry schema. Create the file on the session's first encounter; append thereafter. `<N>` matches the session's SL entry number (infer from most recent `session-<N>-*.md` in the folder).

- Schema, controlled vocabulary of 13 encounter types, per-encounter body shape, and feedback routing: `systems/improvement-loop/project-management/design-notes/2026-04-22-librarian-boundary-case-tracking.md`
- Write scope is narrowed to `operations/system-log/` only — do not write elsewhere.

## Cross-References

- Baseline skill: `.claude/skills/prompt-evaluator/SKILL.md` (workspace root)
- Operation file: `systems/improvement-loop/operations/references/librarian/audit.md`
- Concept file: `systems/improvement-loop/operations/references/librarian/prompt.md`
- Read-contract: `systems/improvement-loop/project-management/design-notes/2026-04-21-librarian-read-contract.md`
- Boundary-case tracking: `systems/improvement-loop/project-management/design-notes/2026-04-22-librarian-boundary-case-tracking.md`
- Librarian agent definition: `systems/improvement-loop/agents/librarian/agent.md`
- Governing DDs: DD-78, DD-82, DD-89
