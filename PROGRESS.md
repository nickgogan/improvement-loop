# Improvement Loop — Progress

**Last Updated:** 2026-04-27 (session 85 close — subagent queue-mutation discipline architectural ruling: Option A end-to-end + partition-by-queue-file rule applied; `/extract-artifacts` SKILL.md amended in 3 places; IB-164 notes appended; no new IB filed)

## Current Focus

Codifier disposition. Session 85 resolved the subagent queue-mutation discipline architectural decision logged-for-future across sessions 83 + 84. Nick ruled **Option A** (end-to-end subagent mode) plus a partition-by-queue-file concurrency rule. Three SKILL.md amendments applied to `/extract-artifacts`; IB-164 notes appended with the amendment record; no new IB filed.

**Outcomes:**

- **SKILL.md amendment 1** — Step 4.8 preamble now carries the **End-to-end execution invariant**: Step 4.8 runs in the same process as the artifact write (Step 3) and source back-annotation (Step 4); the harvest-mode pipeline is end-to-end per invocation; orchestrators that spawn `/extract-artifacts --harvest-row` invocations as subagents MUST NOT post-batch-write the queue file. The skill — wherever it runs — owns Step 4.8.
- **SKILL.md amendment 2** — new trailing subsection of Step 4.8: **Concurrency for parallel harvest-row batches**. Partition-by-queue-file rule: at most one active invocation per `extracts/guides/<stem>.harvest-queue.md` at any moment; within a queue, sequential; across queues, unbounded parallelism. Rationale: each Step 4.8 is per-process atomic read-modify-write of the entire queue file; two concurrent invocations against the same queue file race (last-writer-wins; loser's row update silently lost). Skill itself does not enforce — orchestrator contract when batching.
- **SKILL.md amendment 3** — Step 2 preamble now carries a two-subagent-pattern disambiguation table separating drafting-subagent (identification-report mode; intra-invocation; JSON output; no file writes; no queue touches) from whole-skill-invocation-as-subagent (harvest-mode parallel batches; full end-to-end pipeline including Step 4.8; spawned-skill-instance owns its own Step 4.8 per contract).
- **IB-164 notes appended** with a Session-85 amendment block recording the ruling, the partition-by-queue-file rule, and the three SKILL.md amendment locations. IB stays `status: Done`.

The session-83 contention pattern is now contract-resolved: half-compliant subagents (those that respected the orchestrator's "DO NOT modify the queue file" instruction and skipped Step 4.8) were the procedural violation; full-compliant subagents (e.g., row 13) were honoring the skill contract. The race condition that end-to-end subagent mode would have implied is now contract-mitigated by the partition-by-queue-file rule. Future bulk promotions can spawn whole-skill-invocation subagents in parallel, partitioning by queue, without contention.

**Logged-for-future (carryover; subagent-discipline item removed):**

1. **Codifier reflection on calibration** — still deferred. Cumulative S81-84 calibration data substantial enough for a focused reflection round.
2. **Bidirectional cross-refs hygiene pass** (carryover from session 82). G2/G7/G3b/G5/G9 should have `[[building-agentic-systems]]` entries in their Related Guides sections.
3. **DD-98 split-trigger watch** on G11's first re-synthesis. Count threshold met (≥25 findings).
4. **Edit-tool stale-read pattern** — session 84 validated sequential-edits-per-file workaround for orchestrator-direct execution; pattern still needs codification for subagent-batched workflows.
5. **New `/research-loop` or guide regen** to replenish harvest queues.

**Next session target:** open-ended. Session 85 closed the third-priority item from session 84's carryover; the next item up Nick's Prioritizaton is Codifier calibration reflection (cumulative S81-84 evidence base; trigger-gated since session 81). Codifier disposition; ready when Nick is.


---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

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
