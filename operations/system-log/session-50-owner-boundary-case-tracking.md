---
title: "Session 50 — Owner: Librarian Boundary-Case Tracking + Four-Zone Architecture Migration"
type: "system-log"
target_system:
  - "improvement-loop"
actor: "Agent: Claude (Owner disposition)"
area: null
change_type: "Design + Migration"
milestone: null
rationale: "Executed session-50 handoff. Stream A — produced boundary-case tracking mechanism proposal for the Librarian reference layer (13-type encounter taxonomy, per-session encounter log in SL with distinct type tag, feedback routing by encounter type, six Nick-gated Proposal-First items including a new /summarize-encounters archival skill). Stream A-companion — produced DD proposal for design-artifact placement; Nick's mid-session reframe scaled the proposal from Owner-vs-Codifier split to a four-zone fractal architecture (project-management/design-notes/ for deliberative specs, governance/proposals/ for governance-rule proposals, governance/ root for ratified rules, operations/ for runtime events). Full cleanup executed per Nick's gate: seven existing design notes migrated from operations/design-notes/ to project-management/design-notes/, 27 files cross-reference-updated via sed, deprecated folder removed, new index files created, parent indexes updated. Stream B not invoked this session."
source_dd: "DD-29, DD-44, DD-52, DD-55, DD-56, DD-59, DD-80, DD-82, DD-86"
timestamp: "2026-04-22T00:00:00.000Z"
session: 50
tags:
  - "system-log"
  - "owner"
  - "librarian"
  - "governance"
  - "migration"
  - "architecture"
---

# Session 50 — Owner: Librarian Boundary-Case Tracking + Four-Zone Architecture Migration

## What Changed

### Stream A — Librarian boundary-case tracking proposal

- Produced `governance/proposals/2026-04-22-librarian-boundary-case-tracking.md`.
- **13-type encounter taxonomy** consolidated from read-contract §9 + §Steps 1–8: `missing-concept`, `missing-operation`, `ambiguous-verb`, `ambiguous-variant`, `cross-concept`, `verb-noun-mismatch`, `oversized-artifact`, `hop-ceiling-hit`, `tier-3-read`, `low-confidence`, `kb-gap`, `redirect`, `clarification-asked`. Each is independently detectable at the step where it fires.
- **Location recommended: Option B** — per-session encounter log co-located in `operations/system-log/` with `type: librarian-encounter-log` frontmatter distinguishing it from session-SL entries. Honors Nick's session-49 "lives in SL" framing while isolating pattern-detection substrate from session-shape SL. File naming: `session-<N>-librarian-encounters.md`. Nick gated: Accept.
- **Entry schema** — per-encounter body shape with required fields (timestamp, encounter-type(s), query, parsed-as, resolution) and optional fields (substrate read, gap, consumer disposition). Controlled vocabulary of 13 encounter types.
- **Pattern-surfacing workflow** — primary: Owner workflow on Nick's brief (Stream B). Deferred: `/system-audit` dimension for periodic scanning. Not building: dedicated `/librarian-patterns` skill — adds ceremony without the problem.
- **Feedback routing table** — each encounter type routes to a specific surface (use-case registry / IB item / `next-scan-notes.md` / concept-file update / parser refinement / subagent template work). Owner proposes routing; Nick gates reprioritization; Codifier/Researcher/Owner act.
- **Nick-gated Proposal-First items (6):** (1) file-type convention, (2) entry schema, (3) skill contract update with Write-permission expansion to `operations/system-log/`, (4) feedback routing table, (5) new `/summarize-encounters` Owner skill (archival: summarize + archive old logs + report for review), (6) controlled-vocabulary amendment path.
- **Nick's session-50 gate resolutions** (all 5 open questions resolved in §7):
  - Q1 Location → Accept Option B.
  - Q2 Skill Write-permission → Acceptable.
  - Q3 Retroactive capture from deferred assess-* testing → Acceptable.
  - Q4 Vocabulary amendment path → Accept.
  - Q5 Expiration/compaction → new Owner skill required (integrated into §6 item 5).
- **Not built this session:** no skills, no directories, no DDs. The proposal is the deliverable.

### Stream A-companion — Four-zone architecture DD proposal

- Produced `governance/proposals/2026-04-22-dd-proposal-owner-design-artifact-placement.md`.
- **First draft** proposed an Owner-vs-Codifier placement rule (Owner output → `governance/`, Codifier output → `operations/design-notes/`). **Nick rejected** mid-session: *"I don't like the concept of having design notes in the `operations/` folder for IL. I think the closest existing thing is actually `project-management/`, which would fall under the governance/provenance of Owner agent actually."*
- **Revised proposal** scaled to the **four-zone architecture**:
  - `project-management/design-decisions/` — ratified DDs.
  - `project-management/implementation-backlog/` — tracked work.
  - `project-management/design-notes/` (new) — deliberative specifications (substrate audits, read contracts, use-case registries, rubrics, lifecycle specs, pipeline-mechanics proposals).
  - `governance/` (root) — ratified governance rules.
  - `governance/proposals/` — Owner-authored governance-rule proposals.
  - `operations/` — runtime event output only (SL, handoffs, reports).
  - `operations/design-notes/` — **deprecated and removed.**
- **Placement rule:** shape governs placement; author role is a heuristic, not authority. Deliberative spec → `project-management/design-notes/`; governance-rule proposal → `governance/proposals/`; ratified rule → `governance/` root; runtime event → `operations/`.
- **Relationship to existing DDs:** refines DD-52 (fractal pattern), extends DD-55/56/59 logic to design artifacts, clarifies DD-86 (Owner responsibility). Supersedes nothing.
- **Open questions left for Nick:** DD number assignment, title phrasing, whether Codifier agent-constitution edit batches into this session's DD or a separate Proposal-First pass, archive conventions for superseded design notes, cross-system generalization scope.

### Stream A-companion — Full cleanup migration (executed per Nick's gate)

- **Seven files migrated** from `operations/design-notes/` to `project-management/design-notes/` — no content changed:
  - `2026-04-20-artifact-acceptance-rubric.md` (session 46)
  - `2026-04-20-artifact-lifecycle-spec.md` (session 46)
  - `2026-04-20-pipeline-collapse-proposal.md` (session 47)
  - `2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md` (session 47)
  - `2026-04-21-contract-section-spotcheck-agent-audit.md` (session 48)
  - `2026-04-21-librarian-read-contract.md` (session 49)
  - `2026-04-21-librarian-use-case-registry.md` (session 49)
- **27 files cross-reference-updated** via `sed` — all references to `operations/design-notes/` rewritten to `project-management/design-notes/` across SL entries (sessions 46–49), handoffs (sessions 46–50), reference-layer files (`operations/references/librarian/*.md`), deployed SKILL.md files (`assess-agent`, `assess-prompt`, `assess-skill`), pattern-identification report (session 45), both PROGRESS.md files (IL and workspace root), and the moved design notes' internal cross-references.
- **Deprecated folder removed.** `operations/design-notes/` no longer exists.
- **Index files created/updated:**
  - `project-management/design-notes/_index.md` — created, catalogs the seven migrated files with provenance note.
  - `project-management/_index.md` — updated to enumerate the three subfolders (design-decisions, implementation-backlog, design-notes).
  - `governance/_index.md` — updated to include the `proposals/` subfolder with its role description.

### Stream B — Not invoked

Nick did not invoke Stream B (SL pattern-recognition on brief) this session. Stream B remains available for future sessions.

## Counts

| Metric | Value |
|--------|-------|
| Proposals produced | 2 (boundary-case tracking, four-zone architecture DD) |
| Design notes migrated | 7 |
| Files cross-reference-updated | 27 (within IL) + 1 (workspace-root PROGRESS.md) = 28 |
| Directories removed | 1 (`operations/design-notes/`) |
| Directories created | 1 (`project-management/design-notes/`) |
| Index files created | 1 (`project-management/design-notes/_index.md`) |
| Index files updated | 2 (`project-management/_index.md`, `governance/_index.md`) |
| Mid-session reframes | 1 (DD proposal: Owner-vs-Codifier → four-zone architecture) |
| Nick gates cleared | 2 (Stream A decision set, Stream A-companion cleanup authorization) |

## Design Decisions Applied

| DD | How Applied |
|----|-------------|
| DD-29 | Human gate honored. No DDs filed — both proposals are Owner-authored and Nick-gated; Nick files DDs separately. |
| DD-44 | DD immutability preserved — no DD modification attempted; proposed amendments (if any from this session's DD) are Nick's to file. |
| DD-52 | Fractal pattern made operative for design artifacts. `project-management/design-notes/` aligns with the "what we're deciding" zone; `operations/` returns to its "what happened" shape. |
| DD-55/56/59 | Governance-to-operations distinction extended to design artifacts. Deliberative specs are tracked-work-shape → `project-management/`. |
| DD-80 | Pipeline simplification unchanged. Reference layer unaffected by the migration; cross-references preserved. |
| DD-82 | 4-agent architecture preserved. Owner authored governance-shape proposals; Codifier's historical design notes kept (at new canonical home). Librarian role-expansion amendment remains deferred. |
| DD-86 | Owner responsibility enacted — folder governance of `project-management/design-notes/` proposed for Owner; `governance/proposals/` confirmed as Owner's Proposal-First destination. |

## Affected Items

### Created this session

- `governance/proposals/2026-04-22-librarian-boundary-case-tracking.md` — Stream A proposal.
- `governance/proposals/2026-04-22-dd-proposal-owner-design-artifact-placement.md` — Stream A-companion DD proposal (rewritten mid-session after Nick's reframe).
- `project-management/design-notes/_index.md` — created.
- `operations/system-log/session-50-owner-boundary-case-tracking.md` — this file.

### Moved this session (content unchanged)

- `project-management/design-notes/2026-04-20-artifact-acceptance-rubric.md` (was: `operations/design-notes/...`)
- `project-management/design-notes/2026-04-20-artifact-lifecycle-spec.md` (was: `operations/design-notes/...`)
- `project-management/design-notes/2026-04-20-pipeline-collapse-proposal.md` (was: `operations/design-notes/...`)
- `project-management/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md` (was: `operations/design-notes/...`)
- `project-management/design-notes/2026-04-21-contract-section-spotcheck-agent-audit.md` (was: `operations/design-notes/...`)
- `project-management/design-notes/2026-04-21-librarian-read-contract.md` (was: `operations/design-notes/...`)
- `project-management/design-notes/2026-04-21-librarian-use-case-registry.md` (was: `operations/design-notes/...`)

### Modified this session (cross-reference-only)

- `project-management/_index.md` — enumerates subfolders.
- `governance/_index.md` — describes `proposals/` subfolder.
- `PROGRESS.md` (IL) — path updates only.
- `PROGRESS.md` (workspace root) — path updates only.
- `operations/system-log/session-46-codifier-session-45-identification-and-lifecycle-spec.md` — path updates.
- `operations/system-log/session-47-codifier-pipeline-collapse-substrate-audit-librarian-reference-layer.md` — path updates.
- `operations/system-log/session-48-codifier-librarian-reference-layer-build.md` — path updates.
- `operations/system-log/session-49-codifier-use-cases-read-contract-assess-skills.md` — path updates.
- `operations/handoffs/handoff-prompt-session-46-codifier-session-45-identification.md` — path updates.
- `operations/handoffs/handoff-prompt-session-47-pipeline-collapse-librarian-design.md` — path updates.
- `operations/handoffs/handoff-prompt-session-48-codifier-librarian-reference-layer-build.md` — path updates.
- `operations/handoffs/handoff-prompt-session-49-codifier-use-cases-read-contract-assess-skills.md` — path updates.
- `operations/handoffs/handoff-prompt-session-50-owner-boundary-case-tracking.md` — path updates.
- `operations/pattern-identification-reports/2026-04-20-session-45-identification-report.md` — path updates.
- `operations/references/librarian/_index.md` — path updates.
- `operations/references/librarian/agent.md` — path updates.
- `operations/references/librarian/audit.md` — path updates.
- `operations/references/librarian/harness.md` — path updates.
- `operations/references/librarian/prompt.md` — path updates.
- `operations/references/librarian/skill.md` — path updates.
- `.claude/skills/assess-agent/SKILL.md` — path updates.
- `.claude/skills/assess-prompt/SKILL.md` — path updates.
- `.claude/skills/assess-skill/SKILL.md` — path updates.
- `project-management/design-notes/2026-04-21-librarian-read-contract.md` — internal path updates (references to other design notes).
- `project-management/design-notes/2026-04-21-librarian-use-case-registry.md` — internal path updates.
- `project-management/design-notes/2026-04-21-contract-section-spotcheck-agent-audit.md` — internal path updates.
- `project-management/design-notes/2026-04-20-pipeline-collapse-proposal.md` — internal path updates.
- `project-management/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md` — internal path updates.
- `project-management/design-notes/2026-04-20-artifact-acceptance-rubric.md` — internal path updates.

### Removed

- `operations/design-notes/` (deprecated folder; empty after migration).

## Deferred to Session 51+

### Primary scope (pending Nick's gates)

1. **File DD for four-zone architecture.** Nick files when ready; next available DD number (post-DD-88).
2. **`agents/codifier/agent.md` edit** — add line in Output Artifacts pointing Codifier design output to `project-management/design-notes/`. Proposal-First edit; deferred per DD proposal §Implementation item 5.
3. **Build `/summarize-encounters` Owner skill.** Not this session — build trigger is accumulated volume or Nick's direct request.
4. **Expand Write-permission on the three assess-* skills** to `operations/system-log/` — enables encounter-log writes per Stream A §6 item 3. Waits on Nick's gate on the tracking proposal.
5. **Test the three assess-* skills against real artifacts.** Deferred per session-49 SL; now also the seed for the first encounter log per Stream A §5.1 resolution.

### Secondary scope (carried from earlier sessions, still deferred)

6. **Session-45 identification Status fields** — Nick's APPROVED/REJECTED/REDIRECTED edits still pending.
7. **Lifecycle spec Phase 1 DDs** (DD-X1, DD-X3, DD-X4) — still pending. Blocks G7/G2/G9 re-syntheses.
8. **DD-78 amendment proposal** (Contract triple-role) — defer until further reference-layer exercise.
9. **DD-82 amendment proposal** (Librarian role expansion) — defer until reference layer is exercised.
10. **References-by-agent reorg IB** — authoring needed.
11. **`/dimension-rebalance` on 2 P2 Agentic Systems findings** whose `category:` still reads "Agentic OS."
12. **MetaSystem-as-canonical-hybrid framing** — Nick's harness-builder framing still in flux. Do not reintroduce canonical framing.

### Session-50 scope (new this session)

13. **P2 operation/concept files** (`diagnose.md`, `design.md`, `memory.md`, `context-rot.md`) — session 51+ Codifier work.
14. **Librarian subagent template** for cross-concept queries (read-contract Q4) — not authored.
15. **SL entry shape for Tier-3 reads** (read-contract Q2) — structured frontmatter vs free-form; still open. Likely resolves alongside first encounter-log writes.
16. **Weight calibration timing** for the use-case registry's core/long-tail estimates — becomes meaningful once encounter tracking exists.

## Cross-References

- Session 49 SL entry (predecessor): `operations/system-log/session-49-codifier-use-cases-read-contract-assess-skills.md`
- Session 50 handoff (the plan executed): `operations/handoffs/handoff-prompt-session-50-owner-boundary-case-tracking.md`
- Stream A proposal: `governance/proposals/2026-04-22-librarian-boundary-case-tracking.md`
- Stream A-companion DD proposal: `governance/proposals/2026-04-22-dd-proposal-owner-design-artifact-placement.md`
- New design-notes home: `project-management/design-notes/`
- New design-notes index: `project-management/design-notes/_index.md`
- Source question for Stream A: `project-management/design-notes/2026-04-21-librarian-read-contract.md` §9
- Owner agent definition: `agents/owner/agent.md`
- Governing DDs: DD-29, DD-44, DD-52, DD-55, DD-56, DD-59, DD-80, DD-82, DD-86
