---
name: assess-agent
description: >-
  Audit a consumer-submitted agent artifact (agent.md, CLAUDE.md, system prompt
  for an agent) against Contract-derived criteria from the relevant IL guides.
  Composes audit.md × agent.md from the Librarian reference layer. Produces a
  findings report (file-verifiable checks) plus a follow-up list (system/
  process-verifiable checks). Read-only; never modifies the artifact or the KB.
user-invocable: true
allowed-tools: Read Grep Glob
argument-hint: "<artifact-path|inline-text> [--variant prompt-based|harness-based|autonomous]"
---

# Assess Agent

Load-and-apply wrapper over `audit.md` (operation) × `agent.md` (concept) from
the Librarian reference layer. Intelligence lives in those two files; this skill
parses input, invokes the composition, and formats the output.

## When to Use This Skill

- Consumer wants an IL-KB-grounded audit of an agent artifact.
- Consumer submits an `agent.md`, `CLAUDE.md`, or system prompt for an agent-
  class artifact and asks for evaluation / review / critique / audit.
- Use *after* variant selection is clear; if ambiguous, ask one disambiguating
  question per `agent.md`'s variant-selection heuristics.

## What This Skill Does NOT Do

- Does not rewrite the artifact. Read-only.
- Does not propose a redesign (that's a `design` operation, planned).
- Does not write to the KB.
- Does not audit non-agent artifacts. For prompts, use `/assess-prompt`; for
  skills, `/assess-skill`; for generic code, redirect to `/security-review`
  or language-specific tools.

## Cognitive Disposition

The Librarian's Audit disposition — read-only, citation-grounded, gap-honest.
Every finding cites its source invariant (`<guide>.md#<anchor>`). Unverifiable
invariants become follow-up questions, never silent passes.

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/operations/references/librarian/audit.md` | Operation file — procedure and composition rules |
| `systems/improvement-loop/operations/references/librarian/agent.md` | Concept file — composition table per variant |
| `systems/improvement-loop/extracts/guides/` | Substrate — Contract subsections for {G1, G2, G3, G3b, G5, G6, G7, G9, G10} |
| Consumer-provided path | Artifact under audit |

## Procedure

### Step 0: Parse input

1. Accept artifact as inline text or file path. If path, `Read` it.
2. If artifact > ~500 lines, ask for scoping clarification before proceeding.
3. Determine variant: from `--variant` flag if provided; else infer from
   artifact content per `agent.md` §"Variant selection" heuristics; else ask
   one disambiguating question.

### Step 1: Load composition

1. `Read` `operations/references/librarian/audit.md` — obtain the 5-phase
   procedure (parse, load, build rubric, apply, report) and composition rules
   (a/b/c/d: de-duplication, hierarchical overlap, precondition gating,
   file-verifiable vs system-verifiable split).
2. `Read` `operations/references/librarian/agent.md` — obtain the composition
   table. Extract the guide set for the selected variant:
   - Variant A (prompt-based): {G1, G2, G3, G10}
   - Variant B (harness-based): {G1, G2, G3, G3b, G5, G6, G9, G10}
   - Variant C (autonomous-vs-supervised): {G1, G2, G3, G7, G9, G10} (+ G3b, G5, G6 if tool/harness-enabled)
3. `Read` the `### Contract` subsection of each guide in the set. Use
   heading-match (`Grep -n "^### Contract"` then read the line range) until
   the guide section manifest lands.

### Step 2: Build rubric

Follow `audit.md` Phase 2 mechanically:
1. Apply precondition gating — mark guides whose Preconditions are unsatisfied
   by the artifact as latent.
2. De-duplicate near-identical invariants across guides.
3. Annotate hierarchical overlaps.
4. Tag each invariant as file-verifiable or system/process-verifiable.

Emit the composed rubric as the working header of the report.

### Step 3: Apply rubric

For each file-verifiable invariant: check the artifact, record Satisfied /
Partial / Violated / Missing with evidence quote.

For each system/process-verifiable invariant: record a follow-up question —
never a silent pass.

### Step 4: Assemble report

Produce the audit report per `audit.md` §"Output shape". Add the read-contract
elements:
1. Query restatement (one line): "Interpreted as: (verb: audit, noun: agent,
   variant: <selected>)."
2. Tier trace: "Read: N Tier-1 sections; 0 Tier-2 findings; 0 Tier-3 reads."
   (Most agent audits stay Tier-1 unless the consumer asks for depth.)
3. Confidence tag on each finding (H/M/L).
4. Citation on each finding (`<guide>.md#<anchor>` with line range).
5. Trailing gap report if any KB gap was encountered.

### Step 5: Confidence + provenance pass

Per `audit.md` Phase 5. Attach tier label to every finding; state ambiguity
reason for any low-confidence finding; declare latent guides explicitly.

## Output Shape

See `audit.md` §"Output shape" for the canonical table structure. Do not invent
a new shape; adopt it as authored.

## Boundaries

- If the submitted artifact is not an agent artifact, state that and redirect.
- If `agent.md` concept file is unavailable (e.g., broken read), fall back to
  runtime aggregation against the guide routing table and state the
  degradation.
- If the consumer asks for a redesign, stop and hand off to a `design`
  operation (planned).

## Cross-References

- Operation file: `systems/improvement-loop/operations/references/librarian/audit.md`
- Concept file: `systems/improvement-loop/operations/references/librarian/agent.md`
- Read-contract: `systems/improvement-loop/project-management/design-notes/2026-04-21-librarian-read-contract.md`
- Librarian agent definition: `systems/improvement-loop/agents/librarian/agent.md`
- Governing DDs: DD-78, DD-82
