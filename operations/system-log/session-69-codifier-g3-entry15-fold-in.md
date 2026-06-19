---
title: "Session 69 — Codifier: G3 Entry-15 Fold-In (Harness Spectrum)"
type: "system-log"
target_system:
  - "improvement-loop"
actor: "Claude (Codifier disposition)"
area: "guide-synthesis / harness-spectrum / dd-81-pipeline"
change_type: "Update"
milestone: null
rationale: "Re-synthesized G3 (Agent Architecture Decisions) to fold in the entry-15 reflection from session 66 — Nick's amplification on `specialized-harness-engineering-deterministic-rail` that 'harnesses lie on a spectrum from entirely LLM-initiated & driven via just prompts to mostly deterministic where workflows are instantiated and wired together with code'. Net change: +1 source finding (specialized-harness-engineering), +1 Key Concept (#6 — harness determinism spectrum), +1 Step (8 — Position on the Harness Spectrum), +1 Pitfall (#10 — Premature harness engineering), Step 6 augmented with productive-tension paragraph linking impermanence to the spectrum bet, worked example given a Spectrum Position annotation, contract.invariants/recovery extended. New Step 8 surfaced to Nick before write and approved. Source finding back-annotated (`pipeline_status: synthesized`); routing-table Synthesis Status row bumped (21 → 22, 2026-04-26)."
source_dd: "DD-29, DD-44, DD-78, DD-80, DD-81, DD-86"
date: "2026-04-26"
session: 69
tags:
  - "system-log"
  - "codifier"
  - "guide-synthesis"
  - "g3"
  - "harness-spectrum"
  - "entry-15"
telemetry:
  model: "claude-opus-4-7[1m]"
  tokens_consumed: "unknown"
  context_window_size: 1000000
  context_window_pct_peak: "unknown"
  turns: "~10"
  tool_calls: "~18"
  subagents: 0
  capture_quality: "estimated"
  harness: "claude-code-cli-cursor-macos"
  capture_note: "Session 69 ran in the same conversation as session 68 (G4/G10 re-synthesis closed). Treated as a separate logical session because it consumed a separate handoff input (the entry-15 reflection carried since session 66) and produced a separate atomic commit. Inline Codifier work; no subagents."
---

# Session 69 — Codifier: G3 Entry-15 Fold-In (Harness Spectrum)

## Session Scope

**Primary:** Re-synthesize G3 (Agent Architecture Decisions) to incorporate the entry-15 reflection — Nick's amplification on the `specialized-harness-engineering-deterministic-rail` finding that introduced the "harness determinism spectrum" framing.

**Out of scope (deferred per queue):**
- G2 / G7 / G9 re-synthesis — partially blocked on Lifecycle-spec Phase-1 DDs.
- `/solicit-proposals` first round, IB-153 (`/dimension-rebalance`), Librarian subagent template — all available, none directed this session.
- Promoting `harness-engineering-third-evolution` from `raw` to `classified` — adjacent and reinforcing but out of scope (synthesis session, not intake).

## What Changed

### G3 — Agent Architecture Decisions (+1 finding, near-pure addition)

**Finding integrated:** `specialized-harness-engineering-deterministic-rail` (P1, Strong) — Python scaffolding around LLM calls with phase-gating, structured output schemas, sub-agent delegation per unit, state DB, virtual file system, model tier routing. Production-tested at Stripe (1,300 PRs/week against 3M tests).

**Nick's amplification (entry-15, session 66):** "harnesses lie on a spectrum from entirely LLM-initiated & driven via just prompts to mostly deterministic where workflows are instantiated and wired together with code." This spectrum framing is orthogonal to topology (Step 3) and to layer impermanence (Step 6) — it deserves its own dedicated step.

**Edits applied:**

1. **Key Concept #6 added** — "Harnesses lie on a determinism spectrum -- choose position deliberately." Frames topology decisions (single vs multi, Pattern A-E) as *inside the harness*; the spectrum position is the wrapper-level choice.
2. **Step 8 added: "Position on the Harness Spectrum."** Three-zone table (prompt-driven / generic harness / specialized harness) with reliability, engineering cost, brittleness, examples. Specialized-harness primitives extracted from the source finding (phase-gating, schema validation, sub-agent delegation, state DB, virtual FS, model tier routing). When-to-invest table (4 triggers); when-not-to-invest list (4 contraindications). Migration paths between zones (forward and reverse).
3. **Productive tension with Step 6** — the `contradicts` link between `specialized-harness-engineering-deterministic-rail` and `agent-architecture-layer-impermanence` was treated as a feature, not a bug. New paragraph in Step 6 (after "The bitter lesson for agents") names the tension: don't over-build scaffolding the model will absorb, *and* if reliability requires it, build it anyway with bet-vs-shim classification and a planned review trigger.
4. **Pitfall #10 added** — "Premature harness engineering." Decision rule: only commit to specialized harness when (a) generic-harness baseline measured and insufficient, (b) workflow runs >100 times, *and* (c) cost-of-failure justifies the brittleness tradeoff.
5. **Worked Example annotated** — MetaSystem Research Pipeline gained a "HARNESS SPECTRUM POSITION" block (zone: generic harness; rationale: weekly cadence well below >100-run amortization threshold; bet-vs-shim split for skills/slash-commands vs. PROGRESS.md-as-persistence; trigger to reconsider).
6. **Contract block extended** — `preconditions` (spectrum position is a deliberate decision); `invariants` (spectrum position tied to explicit reliability requirement; specialized investments classified bet vs shim with intended life or removal trigger); `recovery` (two new entries — specialized-harness brittleness on real-world inputs → reconsider zone; surpassed-by-model-native checks → retire those checks not the whole harness); frontmatter `contract.preconditions/invariants/recovery` updated to mirror.
7. **Frontmatter** — `updated: 2026-04-26`; `source_findings` += `specialized-harness-engineering-deterministic-rail`.

**Same-problem cluster cited inline (not added to source_findings):** `archon-yaml-defined-harness-workflows`, `bmad-v6-builder-custom-agent-workflow-creation`, `ide-first-claude-code-with-deterministic-hooks` are referenced by example in Step 8 prose. `harness-engineering-third-evolution` (currently `raw`) reinforces the framing but is excluded from `source_findings` per the synthesis rule that primary sources must be at least `classified`.

### Routing Table — Synthesis Status Updated

| Row | Before | After |
|-----|--------|-------|
| G3 | 2026-04-19 / 21 | 2026-04-26 / 22 |

Frontmatter `updated` left at 2026-04-26 (already current from session 68).

### Source Finding Back-Annotated

| Finding | Before | After |
|---------|--------|-------|
| `specialized-harness-engineering-deterministic-rail` | `pipeline_status: classified`, `consumed_by: []`, `last_updated: 2026-04-19` | `pipeline_status: synthesized`, `consumed_by: ["guides/agent-architecture-decisions.md"]`, `last_updated: 2026-04-26` |

Prior `consumed_by: []` — no append-vs-overwrite ambiguity (DD-77 / DD-81 multi-consumer rule did not fire).

## Artifacts Produced

| # | Type | Path | Action |
|---|---|---|---|
| 1 | Guide (re-synthesized) | `extracts/guides/agent-architecture-decisions.md` | updated (+1 KC, +1 step, +1 pitfall, Step 6 tension paragraph, worked-example annotation, contract extended, frontmatter) |
| 2 | Routing table | `operations/references/guide-routing-table.md` | G3 Synthesis Status row |
| 3 | Finding back-annotation | `research-findings/specialized-harness-engineering-deterministic-rail.md` | `pipeline_status` + `consumed_by` + `last_updated` |
| 4 | SL entry | this file | new |

## Key Decisions (by actor)

1. **Step 8 surfaced before write.** Codifier + Nick. Adding a new procedural step is on the boundary between pure addition and structural change. Pre-approved by Nick after the merge-shape proposal.
2. **Spectrum framing as orthogonal to Step 3 (topology) and Step 6 (impermanence).** Codifier. The entry-15 reflection introduces an axis that is wrapper-level, not topology-level. Folding it into Step 3 as "Pattern F" would mis-frame it as a peer of the topology patterns; folding it into Step 6 would conflate determinism with layer-impermanence. Step 8 keeps the axes clean.
3. **Productive tension with Step 6 named explicitly.** Codifier. The `contradicts` link between specialized-harness and layer-impermanence is real but resolvable: both can be correct depending on where you sit on the spectrum and what reliability your task demands. Surfacing the tension is more useful than hiding it.
4. **Cluster citations inline; source_findings stays minimal.** Codifier. `harness-engineering-third-evolution` (raw), `archon-yaml-defined-harness-workflows`, `bmad-v6-builder-custom-agent-workflow-creation`, `ide-first-claude-code-with-deterministic-hooks` reinforce the spectrum but were cited as in-text examples rather than added to `source_findings`. Maintains the synthesis-rule constraint that sources be at least `classified` and avoids inflating provenance for findings the guide draws on lightly.
5. **No new IB or DD surfaced.** Codifier. The fold-in revealed no governance gap requiring proposal. Nick's amplification was self-contained input; the synthesis structure already accommodated it without architectural change.
6. **Session-numbering: 69 (not 68b).** Codifier. Same conversation as session 68's G4/G10 close, but a separate handoff input (entry-15 reflection carried since session 66), separate primary task, and separate atomic commit. Treated as discrete sessions per the session-as-unit-of-work convention rather than the session-as-conversation-window convention.

## Acceptance Verification

| Test | Expected | Result |
|---|---|---|
| G3 updated | New finding cited in `source_findings`; integrated into body (KC, Step, Pitfall, Step-6 tension, worked example, contract); existing structure preserved | PASS — Step 8 added, Step 6 augmented in place; KC #6, Pitfall #10, source_findings extended; contract.invariants/recovery extended |
| Routing table — G3 row | `Last Synthesized` = today; finding count reflects current cluster (21 → 22) | PASS |
| Source finding — pipeline_status / consumed_by | `classified` → `synthesized`; consumed_by populated; append-not-overwrite if prior entries | PASS — prior `consumed_by: []`; new entry added |
| Deployment | Guide remains in `extracts/guides/` as a draft; not deployed | PASS — no writes to `meta-system/knowledge/guides/` |
| Step 8 pre-approval | Surfaced to Nick before write | PASS — proposal posted; Nick approved |

## Deviations from Skill Contract

None substantive. Like session 68, the `/synthesize-guide` skill was followed procedurally (Step 0 routing-table read; Step 1 finding analysis; Step 3 draft; Step 5 cross-references and back-annotation) without being invoked as a slash-command. Inline Codifier execution was cheaper than spawning the skill for a single-finding fold-in. Documented as a transparent deviation, not a violation.

## Observations Carried Forward

- **`harness-engineering-third-evolution` is `raw` and reinforcing.** Should be reviewed in the next intake or `/identify-artifacts` pass — likely classifies as a pattern (it's a framing for the practice maturation, not a rule/skill/template/agent). When promoted, it can join G3's `source_findings` retroactively if a future re-synthesis touches the spectrum step.
- **Specialized-harness pattern is referenced from G3 but not yet from G3b.** G3b (Agent Workflow and Execution) is the production-runtime guide; specialized-harness primitives (state DB, phase-gating) overlap. Cross-reference may want to flow both directions; defer to next G3b touch.
- **Subagent-governance theme cross-cut continues.** Session 63's note about `subagent-isolation-contract` hubbing five findings across G2/G7/G9/G10 still pending — G2/G9 cross-reference back to G10 Step 7 will land when they're next re-synthesized (Lifecycle-spec gate permitting).

## Telemetry

| Field | Value |
|---|---|
| model | claude-opus-4-7[1m] |
| session | 69 |
| agent | Codifier |
| guides_resynthesized | 1 (G3) |
| findings_integrated | 1 (`specialized-harness-engineering-deterministic-rail`) |
| structural_changes | +1 KC, +1 Step (#8), +1 Pitfall (#10), Step 6 tension paragraph, worked-example annotation, contract extended. New step pre-approved by Nick. |
| ib_filed | 0 |
| dd_filed | 0 |
| subagents | 0 |
| harness | claude-code-cli-cursor-macos |
