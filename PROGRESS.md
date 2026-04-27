# Improvement Loop — Progress

**Last Updated:** 2026-04-27 (session 84 close — DD-97 sweep ruling complete: 3/3 Branch-C proposals ruled Option A and applied; parallel-session reconciliation complete; IB-164 `/extract-artifacts --harvest-row` path fully closed for current 4-guide harvest-queue corpus)

## Current Focus

Codifier disposition. Session 84 ran a two-phase pass per the piped handoff: (1) reconciled parallel-session outputs from session 83; (2) swept all 3 accumulated DD-97 Branch-C extension proposals. Both phases complete. The IB-164 promotion path is fully closed for the current corpus.

**Outcomes:**

- **Phase 1 — parallel-session reconciliation.** Confirmed canonical session-83 SL is correct. The 2 "untracked" SLs Nick flagged were complementary DD-59 single-change SLs documenting a parallel queue-hygiene stream (6 dropped queue items + G2/G7 disambiguation lifted to `guide-routing-table.md`), not orphaned session-83 drafts. The parallel session's PROGRESS.md prune was already absorbed into session 83's commit (`9e0524b`). Per Nick's Option-1 choice, the still-uncommitted complementary work (2 SLs + PROGRESS.md +2 Key Files rows + guide-routing-table.md Disambiguation Notes) was committed as its own atomic commit `8515af8` ahead of Phase 2.
- **Phase 2 — DD-97 sweep ruling.** Nick ruled Option A on all 3 proposals (rows 10, 12, 16); Codifier-reco match: 3/3 (100%). Codifier drafted merge-amendments and presented for Nick's gate; Nick approved defaults. Applied:
  - **Row 10 (G2):** `claudemd-global-rule-cap` → merged into `claudemd-minimum-viable-rule-only-add-globally-true-lines`. Volume cap (Tier-0: 3-5 lines; Tier-1: 60-80 line band) added as operate-stage backstop alongside per-line global-truth test.
  - **Row 12 (G2):** `evolving-docs-use-delta-updates` → merged into `never-ask-claude-to-compact-claudemd`. Title shifted to "Evolving Load-Bearing Documents: No In-Place LLM Rewrite + Delta-Update Discipline"; scope generalized; ACE delta-update mechanism promoted to fully-specified positive-space sub-rule.
  - **Row 16 (G7):** `verify-with-environmental-feedback-not-self-assessment` → merged into `agent-self-reporting-unreliability-independent-eval`. Title shifted to "Agent Self-Report Is Insufficient: Environmental Feedback During Execution + Independent Verification at Completion"; per-step environmental-feedback obligation added as build-stage mechanism alongside verify-stage post-task gate; stage shifted to `[build, verify]`.
- **Atomic-write invariant verified** post-batch on both queues (G2: 9 extracted per-row blocks ↔ 9 extracted summary-table rows; G7: 5 ↔ 5; zero `nick-approved` leftover).
- **3 source findings back-annotated** (`consumed_by[]` extended; "Extraction Note — Session 84" appended).
- **3 extension-proposal status flips** (`proposed → applied`) with ruling metadata + body Status section update.
- **DD-95 lifecycle pointers** updated on all 3 amended artifacts (`last_change_session: 84`, `last_change_sl: session-84-codifier-reconcile-and-dd97-sweep`).

**IB-164 path closure.** The IB-164 `/extract-artifacts --harvest-row` promotion path is fully complete for the current 4-guide harvest-queue corpus (G2 + G7 + G9 + G11). Cumulative artifacts produced across sessions 82-84: 28 Branch-B (19 rules + 6 skills + 3 templates) + 3 Branch-C merge-extensions = 31 total. All accumulated DD-97 Branch-C proposals resolved (3/3 ruled Option A; 3/3 applied). Next harvest-queue activity depends on a new `/research-loop` or guide regen replenishing pattern-finding co-occurrences.

**DD-97 calibration (cumulative S82-84):** 22 rules drafted; 3 Branch-C proposals (14% rate); 3/3 Codifier-reco match on Branch-C rulings (100%); 0 false-positive proposals to date. v1 calibration empirically validated at this scale; tightening deferred per DD-97 §Out of scope.

**Logged-for-future (carryover):**

1. **Subagent queue-mutation discipline architectural decision** — still deferred. Session 83's subagent contention pattern is a workflow smell; option (a) drop orchestrator-batched plan / (b) defensive abort. Trigger: next bulk-promotion workflow OR governance audit.
2. **Codifier reflection on calibration** — still deferred. Cumulative S81-84 calibration data is now substantial enough for a focused reflection round.
3. **Bidirectional cross-refs hygiene pass** (carryover from session 82). G2/G7/G3b/G5/G9 should have `[[building-agentic-systems]]` entries in their Related Guides sections.
4. **DD-98 split-trigger watch** on G11's first re-synthesis. Count threshold met (≥25 findings).
5. **Edit-tool stale-read pattern** — session 84 validated sequential-edits-per-file workaround for orchestrator-direct execution; pattern still needs codification for subagent-batched workflows.

**Next session target (session 85):** Resolve the subagent queue-mutation discipline architectural decision (logged-for-future since session 83). Codifier disposition; execution allowed. Three options on the table: (a) end-to-end subagent mode dropping orchestrator-batched plan, (b) defensive abort in subagent prompt, (c) hybrid with subagent forbidden from queue access. Both prior SLs lean toward (a). Output: `/extract-artifacts` SKILL.md amendment + possible IB amendment + atomic commit at session close. Handoff prompt: `operations/handoffs/handoff-prompt-session-85-codifier-subagent-queue-mutation-discipline.md`.


---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **Subagent queue-mutation discipline architectural decision** — `[trigger]` post-session-83 deviation. Session 83 saw multiple `/extract-artifacts` subagents disregard "do not touch queue file" instruction; row 13's subagent went the full SKILL.md Step 4.8 distance (matches design intent). Architectural choice: (a) drop orchestrator-batched plan — make subagents fully responsible for queue + back-annotation + artifact write end-to-end (aligns with SKILL.md Step 4.8); (b) tighten subagent prompt with defensive abort if queue pre-state matches own row. Trigger: next bulk-promotion workflow OR governance audit. Option (a) likely correct.
- **Codifier calibration reflection round** — `[trigger]` deferred since session 81. Cumulative S81-84 evidence base (38 + 10 + 18 Branch-B drafts ratified or accepted-as-is + 3/3 Branch-C verdicts ruled per Codifier's Option A recommendation) is now substantial enough for a focused reflection. Trigger: next `/solicit-proposals` round or Nick request.
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
