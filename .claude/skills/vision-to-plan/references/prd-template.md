# PRD: <system name>

<!-- PROCESS: Draft ONE section at a time; get explicit approval before the next.
Two rejections of the same section → stop and re-elicit. Delete all ELICIT/PROCESS
comments from the final artifact. Keep the whole PRD skimmable — it is a decision
record, not a spec dump. -->

Updated: <date> · Approved by: <human>

## Vision

<!-- ELICIT: Compress the confirmed summary into 3–5 sentences of durable intent.
This is the layer above PROGRESS.md's North Star; they must not contradict (same
claim, two altitudes). It must be consistent with the approved constitution. -->

## Users

<!-- ELICIT: For each user: who they are, their job-to-be-done, and what evidence in
the workspace represents them. Start from the locked archetype set where one exists
(engine: Nick-builder, portfolio-presenter, practitioner-friend, builder-friend,
employer-evaluator) and probe whether all survive as PRD users or some are
constitution-level audience only. -->

## Goals

<!-- ELICIT: 3–6 outcome statements. Each must be observable — if you can't tell
whether it happened, rewrite it. -->

## Non-goals

<!-- ELICIT: Explicit exclusions, each with a one-line "why not". Push for ≥2 — an
empty non-goals list means the scope isn't understood. Probe named candidates
(engine: multi-tenant design, bulk video intake, Household OS as peer). -->

## Epics

<!-- ELICIT: Break goals into epics. Each epic must be executable by an agent with
zero conversation context. Carry named program inputs in explicitly (engine:
capability-as-composition-unit; harness maintenance/fitness DoD; counter-signals).
Repeat the block below per epic. -->

### E<n> — <epic name>

- **Outcome:** what exists/changes when done, one line.
- **Inputs:** authoritative files/sources the executing agent loads.
- **Acceptance criteria (binary):** at least one pass/fail check — no "improved" or
  "better" without a test.
- **Depends on:** other epics or external facts, or "none".
- **Appetite:** small / medium / large.

## Risks & assumptions

<!-- ELICIT: What could invalidate this plan? Separate assumptions (verifiable) from
risks (mitigatable). -->

## Open questions

<!-- PROCESS: Park anything unresolved here rather than blocking approval; each entry
names who decides and by when it matters. -->
