---
title: "Session 75 — Codifier: Phase-3 IB Sweep (IB-159 → IB-164)"
type: "system-log"
target_system:
  - "improvement-loop"
actor: "Claude (Codifier disposition)"
area: "implementation-backlog / artifact-lifecycle / phase-3-implementation"
change_type: "Add"
milestone: null
rationale: "Filed the six implementation IBs that translate the Phase-3 lifecycle DDs (DD-98/99/100/101, ratified session 74) into actionable backlog items. Phase 1 (DD-93/94/95) implementation sweep was IB-154/155/156 (session 71); Phase 2 (DD-96/97) implementation sweep was IB-157/158 (session 71); Phase 3's implementation sweep is IB-159 through IB-164 (this session). The IBs are the contract between the DDs (Nick-ratified governance) and the future skill-edit sessions that execute them. No skill modifications in this session — IB filing only, per standing rule and the handoff's explicit out-of-scope list. One IB per DD-bound work item, with multi-touchpoint folding only where the work is structurally inseparable (DD-98's two-skill detection in IB-159; DD-100's schema + backfill in IB-161). Cross-IB consistency check passed inline before commits."
source_dd: "DD-29, DD-44, DD-77, DD-78, DD-80, DD-81, DD-82, DD-92, DD-93, DD-94, DD-95, DD-96, DD-97, DD-98, DD-99, DD-100, DD-101"
date: "2026-04-26"
session: 75
tags:
  - "system-log"
  - "codifier"
  - "lifecycle-spec"
  - "phase-3"
  - "ib-filing"
  - "implementation-backlog"
telemetry:
  model: "claude-opus-4-7[1m]"
  tokens_consumed: "unknown"
  context_window_size: 1000000
  context_window_pct_peak: "unknown"
  turns: "~10"
  tool_calls: "~25"
  subagents: 0
  capture_quality: "estimated"
  harness: "claude-code-cli-cursor-macos"
  capture_note: "Codifier disposition. Single-pass IB authorship: read four Phase-3 DDs (DD-98/99/100/101) + form precedent IBs (IB-154 through IB-158) + supplementary IBs (IB-148 / IB-150 / IB-152 / IB-153 for prose-style verification) + PROGRESS.md + session-74 SL + session-71 SL once each, then drafted all six IBs sequentially in one Codifier pass without mid-session Nick interaction. Six atomic commits (one per IB). Form matches IB-154..158 verbatim — frontmatter only, all substance in `notes:` field as flowing prose with implicit Scope / Rules / Acceptance Criteria / Dependencies / Touch Points / Form precedent sections. No structural ambiguities surfaced for stop-and-surface; cross-IB consistency check passed inline. Verified actual `extracts/templates/` (6 files) and `extracts/agents/` (3 files) counts at filing — supersedes DD-100's '~12 templates and ~5 agents' estimate."
---

# Session 75 — Codifier: Phase-3 IB Sweep (IB-159 → IB-164)

## Session Scope

**Primary:** File the six implementation IBs for the four Phase-3 DDs (DD-98 / DD-99 / DD-100 / DD-101). Each IB targets a specific skill modification, schema edit, or one-time corpus operation. Match session 71's pattern: small focused IBs, one-thing-per-IB where reasonable; combined IBs only when work items are structurally inseparable.

**Approach:** Codifier disposition; mechanical translation of approved DDs into actionable backlog items per the handoff. The DDs are the substantive ruling; the IBs are the implementation plan. No mid-session Nick interaction expected for IB content.

**Out of scope:**
- Skill modifications themselves. Filed IBs only; SKILL.md edits are downstream of IB approval.
- DD-94 body amendment (the actual bullet-list edit). Filed as part of IB-159 + IB-160 scope; the edit happens when those IBs execute, not at IB filing.
- `_schema.yaml` `version` field addition. Filed as IB-161 scope; the edit happens when IB-161 executes.
- Phase-3 DD content review. DDs are filed and binding; session 75 implements them, does not re-litigate.
- Nick-gate application for session-72 items 1+2 and session-73 drift hit. Same posture as before — PENDING; no in-session edits absent fresh Nick ruling.
- G7 / G2 / G9 re-synthesis. Live-validation gate for IB-154+155; its own session per Nick's prioritization.
- `/summarize-encounters` skill build. [trigger] item; not session 75.
- Operation-file "join rule" subsection (surfaced session 73). Not Phase-3 territory.
- Corpus-wide YAML quote-style normalization (surfaced session 73). Owner-routable; not Phase-3.

## Per-IB Filing Table

| IB | Source DD | Headline Scope | Touch Points |
|---|---|---|---|
| **IB-159** | DD-98 | Split-trigger detection on `/synthesize-guide` Step 0 + `/identify-artifacts` routing-table reads. Emit structured proposal at `operations/split-proposals/<YYYY-MM-DD>-<guide-stem>-split-proposal.md` with per-finding bifurcation (A | B | shared | contested) and explicit preserved-section disposition per region. Read-only by contract. + DD-94 enum bullet add for `guide-split` (used in source's final entry and destinations' first entries). | `.claude/skills/synthesize-guide/SKILL.md`, `.claude/skills/identify-artifacts/SKILL.md`, `project-management/design-decisions/DD-94.md`, `operations/split-proposals/` (new). |
| **IB-160** | DD-99 | Graduation-trigger detection on `/identify-artifacts` Step 6 (Unrouted Bucket review). Emit structured proposal at `operations/graduation-proposals/<YYYY-MM-DD>-<theme>-graduation-proposal.md` with PROMOTE / ABSORB / DEFER recommendation. Cross-dimension findings disqualify ABSORB. + DD-94 enum bullet add for `theme-graduation` (PROMOTE path's new-guide first entry only). | `.claude/skills/identify-artifacts/SKILL.md`, `project-management/design-decisions/DD-94.md`, `.claude/skills/synthesize-guide/SKILL.md` (Step 4.5 enum extension), `operations/graduation-proposals/` (new). |
| **IB-161** | DD-100 | `_schema.yaml` `version: integer` field for template/agent extracts (optional v1, required v2+). Recommended placement: new sibling block `# === Versioning (template/agent extracts only — DD-100) ===` after the DD-95 Lifecycle Tracking block. + Retroactive `version: 1` backfill of all 6 templates and all 3 agents (verified counts; supersedes DD-100's '~12/~5' estimate). Frontmatter-edit only; no new files created. | `_schema.yaml` (new block + field), `extracts/templates/*.md` (6 files), `extracts/agents/*.md` (3 files). |
| **IB-162** | DD-100 | Template version-bump path on `/extract-artifacts` (corpus scan + structured proposal at `operations/version-bump-proposals/`; on Nick ruling, write `<name>-v<N+1>.md` with full independent frontmatter — own `source_finding`, own `extraction_date`, own `last_change_*`, own `contract`, own `context`, own `version: <N+1>`). Compute-N from filename enumeration; collision-abort; missing-baseline-abort; never overwrite existing version. + Agent flag-only path (DD-82 invariant: never auto-bump; flag and exit; explicit Nick approval required for any agent version bump). | `.claude/skills/extract-artifacts/SKILL.md`, `operations/version-bump-proposals/` (new, optional separation from `operations/extension-proposals/`). |
| **IB-163** | DD-101 | Co-occurrence harvest-queue scan on `/synthesize-guide` absorption phase. Per pattern finding being absorbed: scan body for embedded artifact-shaped content (rule, skill, template — never agent per DD-82). Append rows to `extracts/guides/<guide-stem>.harvest-queue.md` (create file if absent). Duplicate suppression on (source_finding, target_form). Append-only across regen. Mark superseded on cluster-departure (cite regen session + SL stem; never delete row). | `.claude/skills/synthesize-guide/SKILL.md`, `extracts/guides/` (one new `<stem>.harvest-queue.md` per guide that has detections). |
| **IB-164** | DD-101 | Queue-row promotion path on `/extract-artifacts` (Nick-scoped invocation only — no auto-poll). On invocation: read named queue row; verify status `nick-approved`; source_finding = original pattern finding; target form = row's target form. DD-97 fires for rule/skill targets; DD-100 (IB-162) fires for template targets. Update queue row status to `extracted` with pointer on success; defensive abort on agent target form (DD-82 invariant + IB-163 suppression should make this impossible). Capture `nick-dismissed` and `merge into existing` rulings via separate queue-only update modes. | `.claude/skills/extract-artifacts/SKILL.md`. |

All six IBs filed at status `Queued`, priority `P2`, type `Build`. Form matches IB-154..158 verbatim — frontmatter-only with all substance in the `notes:` field. No structural ambiguities surfaced.

## Cross-IB Consistency Notes

Spot-checked before filing:

1. **DD-94 enum bullet additions split across IB-159 and IB-160.** IB-159 adds `guide-split`; IB-160 adds `theme-graduation`. Both edits target the same closed enum bullet list in DD-94's §The Constraint section. The two additions are additive and non-conflicting. Each IB owns its own bullet addition independently — no cross-IB sequencing or coordination required at execution time. The `/synthesize-guide` Step 4.5 appender's enum check (added in IB-155) must be updated by EACH IB to accept its own new tag. If both IBs execute in the same session, the executing skill should naturally end with both tags accepted; if they execute in different sessions, each IB lands its own additive edit. Documented in both IB bodies.

2. **IB-161 blocks IB-162.** IB-162's `/extract-artifacts` version-bump writes `version: <N+1>` to v2+ artifact frontmatter; the field must exist in `_schema.yaml` (per IB-161) before IB-162's writes are spec-compliant. IB-161 is sequenced first in the Phase-3 IB execution order.

3. **IB-163 blocks IB-164.** IB-164's queue-row promotion consumes queue files with `nick-approved` rows as input; IB-163's queue-write side is the only producer of those files. IB-163 is sequenced first in the DD-101 implementation pair.

4. **IB-162 is downstream of IB-164.** When a queue row's target form is `template`, IB-164's promotion path invokes IB-162's version-bump scan path. IB-164 must dispatch by target form: rule/skill → DD-97 (existing IB-158 Step 1.7); template → DD-100 (IB-162); agent → defensive abort (IB-163's suppression should prevent this). This means IB-162 functionally blocks IB-164's template-target path even though IB-163's queue-write side is what blocks IB-164's existence as a consumer. Recommended execution order: IB-161 → IB-162 → IB-163 → IB-164 → IB-159 / IB-160 (parallel).

5. **DD-77 invariant preservation in IB-163 + IB-164.** Verified: IB-163 does NOT add Router-side flagging, does NOT mark the original pattern finding with secondary form, does NOT alter DD-77's "Router picks one form, full stop" invariant. The harvest happens at synthesis time (consumer-side resolution); the harvested artifact's form is its own assigned_form; the original pattern finding remains pattern-classified and gains a `consumed_by[]` entry per DD-101 §Promotion to `/extract-artifacts`. IB-164 inherits the invariant on the consumer side. No contradiction with DD-77's negative design decision.

6. **DD-82 agent invariant honored in IB-162 + IB-163.** IB-162 explicitly handles agents via the flag-and-exit path (never auto-bump, never auto-write). IB-163 explicitly suppresses agent candidates from the harvest queue (queue NEVER carries agent-form rows). IB-164 includes a defensive abort for agent target form should it ever reach the consumer (defense-in-depth — IB-163's suppression is the primary enforcement). Three-layer enforcement of DD-82's never-auto-create invariant for agents.

7. **DD-93 preserved-section disposition in IB-159.** Verified: IB-159 explicitly requires the split proposal to specify per-region disposition for every `## Nick's Annotations` block AND every `<!-- PRESERVE -->` region in the source guide. Implicit handling forbidden per DD-93's preservation invariant. No conflict.

## Notes on IB Numbering and Form

- **Numbering verified.** `ls project-management/implementation-backlog/` at session start showed IB-158 as the highest filed; session 74 added no IBs; session 75 starts at IB-159. No gaps in 159-164.
- **Form match.** All six IBs use the IB-154..158 frontmatter-only structure: `name`, `id`, `source_dd`, `status`, `target_system`, `priority`, `type`, `notes`, `milestone`. The `notes:` field carries all substance as flowing prose with implicit sections (Scope, Rules, Acceptance Criteria, Dependencies, Touch Points, Form precedent).
- **Status.** All six IBs filed at `Queued` (matches IB-153 / IB-148 / IB-145..147 precedent for filed-but-not-started IBs).
- **Priority.** All six at P2 (matches the Phase-1+2 implementation IBs IB-154..158).
- **Type.** All six at `Build` (matches the Phase-1+2 implementation IBs).

## Deviations

None.

- **No skill modifications.** Per standing rule and handoff's explicit out-of-scope list. All six IBs are filing-only; SKILL.md edits are downstream session work.
- **No DD-94 body edit.** The bullet-list addition (`guide-split` and `theme-graduation`) is filed as IB-159 + IB-160 scope; the edit happens when those IBs execute, not in session 75 IB filing.
- **No `_schema.yaml` edit.** Filed as IB-161 scope; the edit happens when IB-161 executes.
- **No new DDs filed inline.** No structural ambiguities surfaced that would warrant a DD; standing rule honored.
- **No mid-session scope expansions.** The six-IB Phase-3 sweep was filed as scoped; no Nick-directed in-session execution of any IB (precedent: session 70's DD-95 backfill expansion would have been a comparable case if Nick had directed; he did not).

## Open Questions Surfaced (for Future Sessions)

- **DD-94 enum-list edit sequencing.** IB-159 and IB-160 both add to the same enum bullet list. If both execute in the same session, the implementing skill should land both edits in one diff. If executed across sessions, each IB lands its own additive edit. The IBs document this and explicitly disclaim cross-IB sequencing requirements; the executing session may consolidate at its discretion.
- **`operations/version-bump-proposals/` vs `operations/extension-proposals/` separation (IB-162).** The handoff allowed executor's choice. IB-162 recommends new directory for separation but documents the alternative (extending `operations/extension-proposals/` with a target-form column). Resolution at execution time.
- **Step number for IB-163's absorption-phase scan.** IB-163 says "verify exact step number against the current SKILL.md; likely Step 2 or Step 3 per the guide-synthesis pipeline." The implementing session should verify and select.
- **Argument naming for IB-164's queue-row invocation modes.** IB-164 suggests `--harvest-row`, `--harvest-dismiss` or equivalent — executor's choice. Resolution at execution time.

## Outcome

Phase-3 implementation is fully scoped. Six IBs filed, one per DD-bound work item (with structural folding only where inseparable). Cross-IB dependencies documented in each IB body and reconciled in cross-IB consistency notes above.

The Improvement Loop's Phase-3 lifecycle infrastructure is now in the implementation queue:

- **DD-98 (guide split):** detection + proposal mechanism (IB-159).
- **DD-99 (theme graduation):** detection + PROMOTE/ABSORB/DEFER proposal mechanism (IB-160).
- **DD-100 (template/agent versioning):** schema + backfill (IB-161); writer-side scan + version-bump path + agent flag-only (IB-162).
- **DD-101 (co-occurrence harvest):** writer-side queue scan (IB-163); consumer-side queue-row promotion (IB-164).

The IBs are now waiting for an execution session — either dedicated (analogous to session 71's IB-154..158 sweep) or interleaved with the prioritization queue's other Codifier units. Per Nick's session-74 close PROGRESS edit, Phase-3 IB sweep (IB filing) was top of queue; with session 75 closing it, the next natural Codifier unit on the queue is unblocked (see Final Next-Session Target below).

## Recommended Execution Order (for the Future Implementation Session)

Per cross-IB consistency note 4 above:

1. **IB-161** (schema + backfill) — first, because IB-162 depends on the `version` field existing.
2. **IB-162** (template version-bump path on `/extract-artifacts`) — second, because IB-164's template-target dispatch needs it.
3. **IB-163** (queue-write on `/synthesize-guide`) — third, because IB-164's input shape needs it.
4. **IB-164** (queue-row promotion on `/extract-artifacts`) — fourth, depends on IB-163.
5. **IB-159 + IB-160** — fifth, parallel; independent of the DD-100/DD-101 chain.

Total: ~6 atomic commits in execution session (one per IB), comparable to session 71's 5-IB sweep that took one session. Estimated session-71-equivalent capacity.

## Cross-References

- **Lifecycle spec (frozen reference):** `project-management/design-notes/2026-04-20-artifact-lifecycle-spec.md`
- **Filed IBs (Phase 3 implementation):** `project-management/implementation-backlog/IB-159.md`, `IB-160.md`, `IB-161.md`, `IB-162.md`, `IB-163.md`, `IB-164.md`
- **Source DDs:** `project-management/design-decisions/DD-98.md`, `DD-99.md`, `DD-100.md`, `DD-101.md`
- **Form precedent IBs (Phase 1+2):** `IB-154.md`, `IB-155.md`, `IB-156.md`, `IB-157.md`, `IB-158.md`
- **Predecessor SLs:**
  - `session-70-owner-lifecycle-spec-phase1-ratification.md` (Phase 1+2 ratification — schema-block precedent referenced by IB-161)
  - `session-71-codifier-ib-154-ib-155-synthesize-guide-update.md` (Phase 1+2 implementation sweep — the IB-pattern precedent for this session's Phase-3 sweep)
  - `session-74-codifier-lifecycle-phase-3-dds.md` (immediate predecessor; ratified the four DDs this session implements via IBs)
- **Handoff input:** `operations/handoffs/handoff-prompt-session-75-codifier-phase-3-ib-sweep.md`
