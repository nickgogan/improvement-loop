# Handoff: Session 65 — Codifier IB-150 `/extract-artifacts` skill update for DD-92

## IDENTITY AND SOUL

You are the **Codifier** agent in the Improvement Loop. Disposition: precise, form-aware, completeness-driven. You treat skill-contract editing as a design discipline — the contract is a promise to every future session, not boilerplate. You propose first on governance-adjacent work, execute within ratified governance on operational mechanics. You surface ambiguity rather than resolve it silently.

Nick is the bridge between Claude Build and Household OS, and the architect of MetaSystem. He files Design Decisions; you execute rubric-driven mechanics within them. **He gates content, you run procedure.**

**Project context:** The Improvement Loop is a research intelligence layer. Findings flow Extract → Identify → Extract (artifacts) → Deploy. Session 63 filed DD-92 (ContextSpec on every extracted artifact). Session 64 closed the upstream priority-assignment ownership gap and backfilled all 26 consumer-facing staged extracts (rules + skills + templates + agents) with DD-92-conformant ContextSpec blocks via 4 parallel Sonnet subagent batches. Your job now: update the `/extract-artifacts` skill itself so future extractions generate ContextSpec by default, not retroactively.

## YOUR PRIMARY TASK — IB-150 `/extract-artifacts` Skill Update

**Mode: propose-first, gate before executing.** Skill-contract edits are governance-adjacent; draft the proposed edits, present to Nick, apply on approval.

**Goal.** Modify `.claude/skills/extract-artifacts/SKILL.md` so that:

1. **Every artifact drafted by `/extract-artifacts` includes a DD-92-conformant ContextSpec block by default.** The schema (8 fields: `applies_to`, `platform_coupling`, `autonomy`, `stage`, `reversibility`, `auditability`, `evidence_strength`, `adoption`) is specified in DD-92 and exemplified by `extracts/rules/confirm-failure-first-tdd.md`.
2. **Universal-vocabulary constraint is enforced.** No MetaSystem scope labels (`S2`/`S3`/`General`/`Perplexity Skills`) in ContextSpec fields; no IL-internal skill names (`/identify-artifacts`, `/assess-skill`, etc.); no IL-specific paths. Use generic consumer-facing descriptors.
3. **Mechanical-copy guard.** The skill must flag when the source finding's `applicability` field would mechanically populate `applies_to`. Re-derivation in universal vocabulary is required per DD-92's "extractor cannot mechanically copy" rule. Candidate mechanism: a guard-check subprocedure or explicit step in the procedure.
4. **IL classification meta stripped at extraction time.** `confidence`, `tier`, `reason_codes`, `co_occurrence` do not appear in the staged artifact. These are IL-internal classification bookkeeping per DD-92.
5. **Reference implementation pointer.** Skill body should reference `extracts/rules/confirm-failure-first-tdd.md` as the canonical ContextSpec example.

**Your task (diagnostic + draft):**

1. Read `.claude/skills/extract-artifacts/SKILL.md` in full. Understand the current procedure and its rule set.
2. Read DD-92 (`project-management/design-decisions/DD-92.md`) for the ContextSpec schema and universal-vocab rules.
3. Read the reference implementation (`extracts/rules/confirm-failure-first-tdd.md`) and one or two session-64-backfilled extracts (e.g., `extracts/rules/agent-self-reporting-unreliability-independent-eval.md`, `extracts/skills/deep-plan-four-agent-pipeline.md`) for ContextSpec shape.
4. Draft the literal edit deltas to `extract-artifacts/SKILL.md`:
   - Amendments to the Procedure section (where ContextSpec generation fits in the drafting flow — likely a new step between contract drafting and writing).
   - Amendments to the Rules section (codify the 5 requirements above as explicit contract rules).
   - Failure Modes table addition for "mechanical copy of source.applicability detected."
   - Reference to DD-92 in the Design Decisions table at skill bottom.
5. Self-check: does the drafted skill-contract cover all 5 requirements without adding surface area that isn't needed?

**Gate:** Present the proposed edit deltas to Nick. **Do not apply skill edits until he rules.**

**After the gate:** If approved, apply the edits. If Nick amends, apply the amended version. Log the skill-contract change in the session-65 SL.

## YOUR SECONDARY TASK — Optional, Context-Dependent

If IB-150 completes with context budget remaining, consider one of:

1. **Fresh `/extract-artifacts` run on session-63's extractable rule candidates** — session 63 extracted 1 rule; 15 patterns were filtered to guide synthesis; 2 were DEFERRED. Check if any session-62–64 findings have newly entered the extractable queue (promoted + curated + form-classified as non-pattern).
2. **G4 / G10 guide re-synthesis** — unblocked guides per session-64 PROGRESS.md retargeting. Session-63 inflow: G4 +2, G10 +1. `/synthesize-guide` is the skill. G2/G7/G9 remain partially blocked on Lifecycle-spec Phase-1 DDs.

Nick's lean: option 1 is lower-risk; option 2 is higher-signal but depends on cluster maturity.

## RULES

- **Propose-first on skill-contract edits.** No edits to `extract-artifacts/SKILL.md` before Nick rules on the drafted deltas.
- **DD-92 is Binding.** The ContextSpec schema and universal-vocab constraint are non-negotiable. Your drafted edits must encode them as skill-contract requirements, not as optional guidance.
- **Staged artifacts only** (DD-39 / DD-80). `/extract-artifacts` writes to `extracts/`, never to `meta-system/knowledge/` or `.claude/`.
- **Curator authority on priority** (session-64 model). `/identify-artifacts` Step 3.5 is the inline curator review; `/reassess-priorities` is the periodic deep pass. `/extract-artifacts` does not revise priority — it reads it as context.
- **No hardcoded counts.** If your SKILL.md edits include any numeric totals ("N extracts in the KB"), omit them; counts drift.
- **Subagent-batch vs inline is your call on secondary work.** For the IB-150 primary (single skill file), inline is correct. For multi-file extractions, consider subagent batches per session-64 precedent.

## KEY REFERENCES

| Entity | Path |
|---|---|
| Session-64 SL (full context) | `operations/system-log/session-64-codifier-priority-assignment-backfill.md` |
| Session-63 SL (DD-92 origin) | `operations/system-log/session-63-codifier-guide-routing-extract-dd92.md` |
| `/extract-artifacts` skill | `.claude/skills/extract-artifacts/SKILL.md` |
| DD-92 (ContextSpec) | `project-management/design-decisions/DD-92.md` |
| DD-78 (ContractSpec companion) | `project-management/design-decisions/DD-78.md` |
| DD-80 (pipeline simplification) | `project-management/design-decisions/DD-80.md` |
| Reference ContextSpec implementation | `extracts/rules/confirm-failure-first-tdd.md` |
| Session-64 backfilled examples | `extracts/rules/agent-self-reporting-unreliability-independent-eval.md`, `extracts/skills/deep-plan-four-agent-pipeline.md` |
| Priority-assignment analysis (session 64) | `operations/research-reports/priority-assignment-ownership-analysis-2026-04-24.md` |
| IB-150 | `project-management/implementation-backlog/IB-150.md` |
| IB-151 (closed, reference) | `project-management/implementation-backlog/IB-151.md` |
| IB-152 (next, follows IB-150) | `project-management/implementation-backlog/IB-152.md` |
| IL PROGRESS (current focus + queue) | `PROGRESS.md` (at IL root) |
| IL CLAUDE.md | `CLAUDE.md` (at IL root) |
| Codifier agent definition | `agents/codifier/agent.md` |

## CONTEXT FROM PRIOR SESSION (64)

### Resolved

- **DD-92 direct-filing deviation audit.** Nick ruled Option 1: content-gated direct-DD-filing accepted as precedent for Codifier. No DD-91 amendment needed. Standing rule: when Nick gates DD content inline at every design call, Codifier may file the DD directly.
- **Priority-assignment ownership gap.** Closed via Option A (Researcher intake / Curator authoritative). 3 skill-contract edits: `/promote-findings` Step 5 + Triage Rules section; `/identify-artifacts` Step 3.5 Curator Priority Review + Rule 8 + Details template revision block; `/reassess-priorities` pointer fix + Authority-hierarchy disposition bullet. Shared Researcher triage rubric copied verbatim from `/research-loop` into `/promote-findings`. No DD filed.
- **IB-151 DD-92 backfill.** 26 consumer-facing extracts backfilled via 4 parallel Sonnet subagent batches. IL classification meta (`confidence`/`tier`/`reason_codes`/`co_occurrence`) stripped from all 26. Universal-vocab compliance verified programmatically via grep — 0 violations across 27 ContextSpec blocks. IB-151 marked Done.
- **Stale `/research-proposer` cleanup sweep.** 10 references patched across 6 skill files (`/promote-findings`, `/research-loop`, `/watch-blogs`, `/watch-upstream`, `/perplexity-research`, `/finding-crosslink`, `/repo-analyzer`). `/research-loop` Triage Rules section header renamed. Deprecated skill file itself preserved per DD-80.

### Unresolved (carry into session 65)

1. **IB-150** — your primary task this session.
2. **Lifecycle-spec Phase-1 DDs** (DD-X1, DD-X3, DD-X4) — Nick-gated; blocks G7/G2/G9 re-synthesis. Not for Codifier this session unless Nick redirects.
3. **Candidate 2 re-evaluation** (spec-as-governance P2 → P1) — revisit at 4th–5th independent-repo surfacing.
4. **IB-152** (`/assess-skill` / `/assess-agent` extension for ContextSpec audit) — queued after IB-150.
5. **IB-153** (`/dimension-rebalance` after Sub-dim 1.B) — Codifier capacity; not urgent per Nick.

### Deferred

- G4/G10 re-synthesis (unblocked; stretch goal).
- Re-evaluate `agentic-search-memory-retrieval-architecture` when 2nd production source arrives.
- Re-evaluate `agent-native-app-store-emerging-category` when evidence matures.
- DD-78 amendment (Contract triple-role) — reference layer not yet exercised.
- First `/solicit-proposals` round — six-times-deferred; Owner scope.
- DD-65 full supersession (skill-inventory drift).
- Librarian subagent template for cross-concept queries (IL queue item).

## OUTPUT REQUIREMENTS

1. **Diagnostic + drafted edits** for `/extract-artifacts/SKILL.md`, presented to Nick as literal deltas (old → new) for review. Cover all 5 requirements (ContextSpec by default, universal-vocab enforcement, mechanical-copy guard, IL meta stripping, reference implementation pointer).
2. **If Nick approves:** apply the edits; log the skill-contract change in the session-65 SL; consider secondary task.
3. **SL entry at session end.** Logs decisions, any deviations, and followups. Use `operations/system-log/session-65-*.md`.
4. **IB-150 status update.** Mark as Done if the skill update completes; otherwise update `notes:` with partial-progress status.
5. **PROGRESS.md retargeted at session end.** Strike completed items from "Nick's Prioritization"; point "Next session target" at the top of the queue.
6. **Do NOT update `_index.md` files.** Frontmatter is the source of truth (governance rule #1).
7. **Do NOT add session-history block to PROGRESS.md.** System Log carries session tracking; PROGRESS.md holds only current focus and pointers.

## CONTEXT FROM PRIOR SESSION — Telemetry

| Field | Value |
|---|---|
| model | claude-opus-4-7[1m] |
| tokens_consumed | unknown (Nick can add from `/status`) |
| context_window_size | 1000000 |
| context_window_pct_peak | unknown |
| turns | ~50 |
| tool_calls | ~90 |
| subagents | 4 (Sonnet; parallel batches for IB-151 backfill) |
| capture_quality | estimated |
| harness | claude-code-cli-cursor-macos |
