# Improvement Loop — Progress

**Last Updated:** 2026-04-27 (session 83 close — IB-164 `/extract-artifacts` resume completed: 18 artifacts written across rules + skills + templates; 2 new DD-97 Branch-C proposals filed; 3 accumulated proposals now pending Nick's ruling)

## Current Focus

Codifier disposition. Session 83 completed the IB-164 `/extract-artifacts` promotion path across the consolidated nick-approved pool (residual 20 rows after session 82's 10-row first execution). Per the piped handoff (`handoff-prompt-session-83-codifier-ib164-resume-extract-artifacts.md`) and Nick's session-level "proceed until done" autonomy directive, the session ran end-to-end through Phase A (G11 rulings ratification), Phase B (20-row promotion), and a deferred Phase C (row 10 stays pending per DD-97 auto-merge prohibition).

**Outcomes:**

- **18 artifacts written** — 9 rules (close-irrelevant-ide-files, test-context-strategies-against-actual-model, agent-must-read-and-update-memory-md, tier-based-orchestrator-effort, compounding-loops-must-encode-outcomes, ai-and-human-vaults-must-be-separate, capture-must-be-byproduct-of-work, scheduled-workflows-require-human-checkpoint, reach-l6-before-l7), 6 skills (comprehension-gate-at-pr-review, spec-driven-development-loop, re-fork-and-trim-trajectory-procedure, filesystem-lock-parallel-agent-coordination, structured-fact-extraction-from-agent-turn, time-window-proactive-loop), 3 templates (progressmd-session-bridge-template, tool-response-format-enum, experiment-note-frontmatter-schema). Each carries DD-78 ContractSpec + DD-92 ContextSpec + DD-95 lifecycle pointer (`last_change_session: 83`, `last_change_sl: session-83-codifier-ib164-resume-extract-artifacts`).
- **2 new DD-97 Branch-C extension proposals filed** — `evolving-docs-use-delta-updates` → primary match `never-ask-claude-to-compact-claudemd` (row 12, G2); `verify-with-environmental-feedback-not-self-assessment` → primary match `agent-self-reporting-unreliability-independent-eval` (row 16, G7). Both recommend Option A (merge as extension). Queue rows retain Status `nick-approved` per DD-97 §Acceptance Criteria.
- **G11 Phase A ratification.** All 7 G11 harvest-queue rows already `nick-approved` in working tree at session start — taken as authoritative per Nick's directive; no re-walk.
- **Queue write-back.** 4 queue files updated atomically (G2: 6 row touches; G7: 5; G9: 2; G11: 7). Atomic-write invariant verified (table ↔ per-row block consistency on all 4 queues).
- **18 source-finding back-annotations.** Each Branch-B source finding gained a `consumed_by[]` entry pointing to its extracted artifact.
- **DD-97 / DD-100 corpus-scan calibration.** 18% Branch-C rate on rules (2/11), 0% on skills (0/6), 0% on templates (0/3). Both Branch-C verdicts recommend `extend` not `false positive`. Cumulative session-82+83 rules: 3/22 ≈ 14% Branch-C rate. Calibration tightening deferred per DD-97 §Out of scope.
- **Procedural deviations cleanly resolved.** Several subagents disregarded the orchestrator-batched queue-update plan and updated queue files themselves (matches SKILL.md Step 4.8 design intent — architectural data point for future patches). Stale `-your-actual-model.md` artifact from a prior aborted session-83 attempt deleted. One row-16 contradictory subagent output (wrote both Branch-B artifact AND Branch-C proposal) cleaned up by honoring the Branch-C proposal (artifact deleted; queue row stays nick-approved). Six corrupted trailer fragments cleaned via regex pass; one duplicate Branch-C trailer deduplicated. Edit-tool stale-read failures worked around via Python bulk-edit scripts.

**Three accumulated DD-97 Branch-C proposals now pending Nick's ruling:** rows 10 (session 82), 12 (session 83), 16 (session 83). All three recommend Option A. Sweep-pass recommended at next ruling session.

**Logged-for-future:**

1. **Subagent queue-mutation discipline.** Several subagents disregarded "do not touch queue file" instruction this session; row 13's subagent went the full SKILL.md Step 4.8 distance (matches design intent). Architectural decision pending: (a) make subagents fully responsible for queue + back-annotation + artifact write end-to-end (drop orchestrator-batched plan); (b) tighten prompt with defensive abort. Surface in next IL governance audit. Option (a) feels more aligned with SKILL.md.
2. **Codifier reflection on calibration** — still deferred. Cumulative S81 (38) + S82 (10) + S83 (18) Branch-B verdicts where Codifier recommended `new` and Nick has not overruled. 3 Branch-C verdicts pending Nick's rulings.
3. **Bidirectional cross-refs on adjacent guides** (carryover from session 82). G2/G7/G3b/G5/G9 should have `[[building-agentic-systems]]` entries in their Related Guides sections.
4. **Agentic Systems data hygiene** (carryover from session 82). `flat-root-vault-with-property-based-organization` priority normalization. Worth a sweep.
5. **DD-98 split-trigger watch** (carryover from session 82). G11 count threshold met (≥25 findings); first re-synthesis is the trigger window.
6. **Edit-tool race conditions with subagent + linter mutations.** Multi-tool-call Edit batches against queue files repeatedly hit "modified since read" failures. Python bulk-edit fallback worked. Procedural pattern worth recording for future bulk-promotion workflows.

**Next session target:** Nick rules the 3 accumulated DD-97 Branch-C proposals (rows 10, 12, 16) — sweep-pass at one sitting since all 3 recommend Option A. Then optional cleanup tasks (bidirectional cross-refs, data hygiene). Beyond that, the IB-164 path is fully complete for the current 4-guide harvest-queue corpus; next research-loop or guide-regen will replenish the queues.


---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **Three DD-97 Branch-C extension proposals — sweep ruling** — `[nick-gate]` top unblocked Codifier item post-session-83. Three accumulated proposals all recommending Option A (merge as extension):
  - Row 10 (G2): `claudemd-global-rule-cap` → primary match `claudemd-minimum-viable-rule-only-add-globally-true-lines` (proposal `operations/extension-proposals/2026-04-27-claudemd-global-rule-cap-extension-proposal.md`; carryover from session 82).
  - Row 12 (G2): `evolving-docs-use-delta-updates` → primary match `never-ask-claude-to-compact-claudemd` (proposal `operations/extension-proposals/2026-04-27-evolving-docs-use-delta-updates-extension-proposal.md`; new session 83).
  - Row 16 (G7): `verify-with-environmental-feedback-not-self-assessment` → primary match `agent-self-reporting-unreliability-independent-eval` (proposal `operations/extension-proposals/2026-04-27-verify-with-environmental-feedback-extension-proposal.md`; new session 83).
  Sweep-pass recommended (rule all 3 in one sitting). Per DD-97 v1, Option A (merge) requires manual amendment to the existing artifact then re-invoke `/extract-artifacts --harvest-row <row>` to flip queue Status → `extracted` with `merged into [[<existing>]]`. Auto-merge prohibited per DD-97 §Acceptance Criteria.
- **Subagent queue-mutation discipline architectural decision** — `[trigger]` post-session-83 deviation. Session 83 saw multiple `/extract-artifacts` subagents disregard "do not touch queue file" instruction; row 13's subagent went the full SKILL.md Step 4.8 distance (matches design intent). Architectural choice: (a) drop orchestrator-batched plan — make subagents fully responsible for queue + back-annotation + artifact write end-to-end (aligns with SKILL.md Step 4.8); (b) tighten subagent prompt with defensive abort if queue pre-state matches own row. Trigger: next bulk-promotion workflow OR governance audit. Option (a) likely correct.
- **Visualization brainstorm** — [deferred] boil DDs/architecture into human-visualizable form. Session 62: `interactive-explanations-extend-linear-walkthroughs` finding (P2) is a direct technique for this work.
---

## Open IB Items

Filed items live in `project-management/implementation-backlog/IB-*.md`. Source-of-truth status is the `status:` field in each file's frontmatter.

---

## Key Files

| Entity | Path |
|--------|------|
| IL identity, agents, pipeline | `CLAUDE.md` |
| Agent definitions | `agents/{owner,researcher,codifier,librarian}/agent.md` |
| Agent reflections (agent-private) | `agents/{owner,researcher,codifier,librarian}/reflections/` |
| IL-specific governance | `governance/` |
| Governance proposals (Owner + agent-authored) | `governance/proposals/` |
| Cross-system DD proposals (MetaSystem-level) | `../meta-system/governance/proposals/` |
| Design notes (deliberative specs) | `project-management/design-notes/` |
| Design Decisions | `project-management/design-decisions/` |
| Implementation Backlog | `project-management/implementation-backlog/` |
| Session handoffs | `operations/handoffs/` |
| System Log | `operations/system-log/` |
| Extension proposals (DD-97 v1 manual-apply) | `operations/extension-proposals/` |
| Version-bump proposals (DD-100 manual-apply) | `operations/version-bump-proposals/` |
| Librarian reference layer | `operations/references/librarian/` |
| Guide routing table | `operations/references/guide-routing-table.md` |
| Research dimensions | `operations/references/research-dimensions.md` |
| Form classification rubric | `operations/references/form-classification-rubric.md` |
| Research KB (findings, sources, authorities) | `research-findings/`, `research-sources/`, `research-authorities/` |
| Watched libraries registry | `watched-libraries/_index.md` |
| Staged extracts | `extracts/` |
| IL-scoped skills | `.claude/skills/` |

---

## Session History

Session-by-session narrative lives in `operations/system-log/`. Handoff prompts in `operations/handoffs/` carry session-to-session continuation context. This file carries current focus and pointers only — not a session ledger.
