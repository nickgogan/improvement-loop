---
title: "Session 85 — Codifier: Subagent queue-mutation discipline architectural decision (Option A end-to-end + partition-by-queue-file rule)"
type: "system-log"
target_system:
  - "improvement-loop"
actor: "Claude (Codifier disposition)"
area: "extract-artifacts / harvest-queue / dd-101 / ib-164 / subagent-discipline / concurrency"
change_type: "Update"
milestone: null
rationale: "Single-task Codifier session resolving the subagent queue-mutation discipline architectural decision logged-for-future across sessions 83 + 84. Nick ruled Option A (end-to-end subagent mode) plus a partition-by-queue-file concurrency rule. SKILL.md amendments applied to /extract-artifacts: (1) Step 4.8 preamble — End-to-end execution invariant clarifying same-process execution and atomicity from artifact write through queue flip; orchestrators MUST NOT post-batch-write the queue file. (2) New Step-4.8 trailing subsection — Concurrency for parallel harvest-row batches — partition-by-queue-file rule with race-condition rationale (per-process atomic read-modify-write; two concurrent writers to same file race; last-writer-wins). (3) Step 2 preamble — two-subagent-pattern disambiguation table separating drafting subagent (identification-report mode; intra-invocation; JSON output; no file writes; no queue touches) from whole-skill-invocation-as-subagent (harvest-mode parallel batches; full end-to-end pipeline including Step 4.8). IB-164 notes appended with the architectural amendment record (no new IB filed; the decision is a contract clarification of an already-closed work item, not a new work item). PROGRESS.md retargeted: subagent queue-mutation discipline removed from Nick's Prioritizaton; current focus advanced. Single atomic commit at session close."
source_dd: "DD-29, DD-78, DD-97, DD-101, IB-164"
date: "2026-04-27"
session: 85
tags:
  - "system-log"
  - "codifier"
  - "extract-artifacts"
  - "harvest-queue"
  - "dd-101"
  - "ib-164"
  - "subagent-discipline"
  - "concurrency"
  - "skill-amendment"
---

# Session 85 — Codifier: Subagent queue-mutation discipline architectural decision

## Summary

Single-task session resolving the architectural decision logged-for-future across sessions 83 + 84. Nick ruled **Option A** (end-to-end subagent mode); Codifier surfaced one additional architectural rule (partition-by-queue-file concurrency) to close a race-condition gap implied by Option A. Three SKILL.md amendments applied. IB-164 notes appended with the amendment record. No new IB filed.

## The decision

**Option A — End-to-end subagent mode.** Each `/extract-artifacts --harvest-row <id>` invocation runs the full harvest-mode pipeline (Step 0a → 1 → 1.7/1.8 → 2 → 2.5 → 2.7 → 3 → 4 → 4.8 → 5) end-to-end in a single process. The skill — wherever it runs — owns Step 4.8 (queue write-back). When a higher-level orchestrator spawns these invocations as subagents in parallel, the orchestrator MUST NOT itself post-batch-write the queue file (contradicts the skill contract, splits atomicity across processes, creates contention).

**Plus a partition-by-queue-file concurrency rule.** Parallel batches MUST be partitioned by queue file — at most one active invocation per `extracts/guides/<stem>.harvest-queue.md` at any moment. Within a queue file: sequential. Across queue files: unbounded parallelism.

## Why Option A over (b) defensive abort or (c) hybrid

| Anchor | Option A (end-to-end) | Option B (defensive abort) | Option C (hybrid; orchestrator owns queue) |
|---|---|---|---|
| **SKILL.md Step 4.8 design intent** | Honors directly — Step 4.8 stays inside the skill | Adds a contradicting branch | Breaks it — Step 4.8 must become orchestrator-only or conditional |
| **Atomic-write invariant** | Preserved per-subagent (one process owns read-modify-write) | Preserved but split-brain (orchestrator does the write, subagent observes) | **Broken** — artifact write and queue flip in different processes with inter-process window |
| **Session-83 empirical evidence** | Row 13 demonstrated end-to-end works cleanly when honoring the skill contract | The compliant subagents were violating SKILL.md to comply with orchestrator prompt | No empirical data |
| **Complexity / prompt cost** | Lowest — orchestrator's prompt simply stops over-specifying | Heaviest — subagent must observe queue pre-state, judge own row, route accordingly | Medium — needs a `--skip-queue-writeback` flag; Step 4.8 becomes conditional |

The session-83 contention was a workflow smell rooted in the orchestrator's prompt instructing subagents to skip Step 4.8 (intending to batch queue updates post-subagent-completion); some subagents complied (procedural violation against SKILL.md), some honored the skill contract. Cleanup ran via match-then-skip semantics that masked the divergence; net: no data loss, but the architecture was incoherent.

## The race condition that motivated the partition rule

End-to-end subagent mode introduces a concurrent-writers-to-same-queue-file failure mode that the orchestrator-batched plan was implicitly avoiding. Within a guide (e.g., G11 — 7 G11 rows in session 83), all rows live in one queue file. The Edit tool's read-modify-write is per-process atomic, but two processes both reading the same file then both writing can lose row updates: subagent A reads pre-state; subagent B reads pre-state; A modifies its row in its in-memory copy and writes whole-file; B modifies its row in its in-memory copy (stale w.r.t. A's change) and writes whole-file; A's row update is silently overwritten.

Session 83 didn't lose data because the orchestrator-batched updater used match-then-skip semantics, but that's a recovery path, not a guarantee. The partition rule eliminates the race at the orchestration layer: serialize all writers to a given queue file; parallelism remains across distinct queue files.

## SKILL.md amendments applied

### Amendment 1 — Step 4.8 preamble: End-to-end execution invariant

Inserted between the existing `--harvest-row` mode-sequencing paragraph and the `**Inputs.**` paragraph. States that Step 4.8 runs in the same process as the artifact write (Step 3) and source back-annotation (Step 4); the harvest-mode pipeline is end-to-end per invocation; orchestrators that spawn `/extract-artifacts --harvest-row` invocations as subagents MUST NOT post-batch-write the queue file; the skill — wherever it runs — owns Step 4.8.

### Amendment 2 — Step 4.8 trailing subsection: Concurrency for parallel harvest-row batches

Inserted after the existing `**Run-report summary**` paragraph at the end of Step 4.8 and before the `### Step 5` heading. States the partition-by-queue-file rule: at most one active invocation per `extracts/guides/<stem>.harvest-queue.md` at any moment; within a queue file, rows are sequential; across queue files, parallelism is unbounded. Rationale: each Step 4.8 is per-process atomic read-modify-write; two concurrent writers to the same file race; last-writer-wins. Skill itself does not enforce; it is the orchestrator's contract when batching. References session 83 as the surfacing event.

### Amendment 3 — Step 2 preamble: two-subagent-pattern disambiguation table

Inserted between the `### Step 2: Draft Artifacts (Subagents)` heading and the existing `**Filter out extension-proposed findings**` paragraph. Adds a table separating two patterns:

| Pattern | Where it runs | What it does | Step 4.8 ownership |
|---|---|---|---|
| Drafting subagent (this Step 2) | Inside one `/extract-artifacts` invocation (identification-report mode) | Drafts artifact body + ContractSpec + ContextSpec; outputs JSON; **does not write files**; **does not touch queue files** | Skill orchestrator (single process; Steps 3–5 of the same invocation) |
| Whole-skill-invocation-as-subagent (harvest-mode parallel batches) | Higher-level orchestrator spawns N parallel `/extract-artifacts --harvest-row <id-i>` processes | Full end-to-end harvest-mode pipeline including Step 4.8 | Spawned skill instance (each invocation owns its own Step 4.8 per skill contract; higher-level orchestrator MUST NOT post-batch-write the queue file) |

Trailing prose cross-links to the new Step 4.8 invariant and partition rule.

## IB-164 amendment

IB-164 (`status: Done`, closed session 76) had its `notes:` field appended with a Session-85 amendment block recording the architectural ruling, the partition-by-queue-file rule, and the three SKILL.md amendment locations. No new IB filed — the decision is a contract clarification of an already-closed work item, not a new work item.

## What this contract-resolves

- The session-83 procedural-deviation observation is now contract-resolved. Half-compliant subagents (those that respected the orchestrator's "DO NOT modify the queue file" instruction and skipped Step 4.8) were the procedural violation; full-compliant subagents (e.g., row 13) were honoring the skill contract.
- The race condition that end-to-end subagent mode would have implied is now contract-mitigated by the partition-by-queue-file rule. Future bulk promotions can spawn whole-skill-invocation subagents in parallel, partitioning by queue, without contention.
- The two-subagent-pattern ambiguity is now explicit in SKILL.md. Future operators reading Step 2 will see the distinction between drafting-subagent (intra-invocation; JSON output) and whole-skill-invocation-as-subagent (parallel batches; full pipeline).

## Logged-for-future (carryover; subagent-discipline item removed)

1. **Codifier reflection on calibration** — still deferred. Cumulative S81-84 calibration data substantial enough for a focused reflection round.
2. **Bidirectional cross-refs hygiene pass** (carryover from session 82). G2/G7/G3b/G5/G9 should have `[[building-agentic-systems]]` entries in their Related Guides sections.
3. **DD-98 split-trigger watch** on G11's first re-synthesis. Count threshold met (≥25 findings).
4. **Edit-tool stale-read pattern** — session 84 validated sequential-edits-per-file workaround for orchestrator-direct execution; pattern still needs codification for subagent-batched workflows.
5. **New `/research-loop` or guide regen** to replenish harvest queues.

## Session telemetry

- **model:** claude-opus-4-7[1m]
- **context_window_size:** 1,000,000
- **turns:** ~3 user↔assistant exchanges
- **tool_calls:** ~12 (sequential Reads + 4 Edits + 1 Write + 1 atomic commit pending)
- **subagents:** 0 (orchestrator-direct execution; this session deliberately avoided subagents — focused architectural decision)
- **harness:** claude-code-cli-cursor-macos
- **capture_quality:** estimated
- **parallel_session:** no
