---
notion_id: null
log_entry: "Swept IL prioritization queue — 5 trigger entries dropped, G2-vs-G7 disambiguation note lifted to guide-routing-table.md"
actor: "Nick + Agent: Claude"
area: "il / prioritization-queue / queue-hygiene"
change_type: "Operational Learning"
milestone: null
rationale: "Audit pass through 'Nick's Prioritizaton' queue revealed five trigger-gated entries whose substance either duplicated rules already documented at the source of truth, pointed at dead premises, depended on upstream signals that haven't materialized, or was better expressed inside the load-bearing reference doc itself. Each entry was examined against its actual home: rules at research-dimensions.md, gates at agent.md, draft proposals never ratified, encounter-log infrastructure with zero producer-side writes. The exposed pattern: trigger-gated queue items accumulate without triggers ever firing because the trigger description often duplicates mechanisms that fire naturally during normal pipeline operation. The disambiguation note for G2 vs G7 was the one entry carrying genuinely durable signal not captured elsewhere — lifted to guide-routing-table.md's new 'Disambiguation Notes' section so the warning surfaces at read time for /identify-artifacts and /synthesize-guide. Composes with today's earlier dropped-summarize-encounters SL: same audit logic applied at queue scale rather than per-item."
source_dd: null
target_system: "Improvement Loop"
timestamp: "2026-04-27T00:00:00.000Z"
---

# Swept IL prioritization queue — 5 entries dropped, 1 lifted

## What Changed

Five entries removed from `systems/improvement-loop/PROGRESS.md`'s "Nick's Prioritizaton" queue, each for a distinct reason:

1. **Sub-dim 1.B graduation track monitoring** — Dropped. Graduation criteria (≥10 findings + sibling-dim references + Librarian concept file) are codified at `operations/references/research-dimensions.md:145` (and line 109 for 1.A; line 30 for the general elevation rule). The queue line restated the rule and carried a drifting count (4 findings). `/research-loop`, `/identify-artifacts` Step 6, and `/dimension-rebalance` cover the trigger naturally.

2. **G2 vs G7 routing disambiguation audit** — Substance lifted, queue line dropped. The historical context (post-IB-153 the discriminator "Memory Architecture" was removed; G2 and G7 now both carry only Context Engineering) and remediation sketches (`lifecycle: build|operate` field, OR routing-rubric step that consults trigger keywords before Dimensions) were lifted to `operations/references/guide-routing-table.md` under a new "Disambiguation Notes" section after Trigger Keywords. The note now surfaces during the same reads `/identify-artifacts` and `/synthesize-guide` already perform.

3. **Retroactive migration of ~100 non-guide/non-pattern extracts** — Dropped. The "pipeline-collapse Phase M1 audit" referenced in the entry comes from `project-management/design-notes/2026-04-20-pipeline-collapse-proposal.md`, which sits at `stage: "draft"` and was never ratified into a DD. The "~100" was already stale (current state: 56 non-pattern + 72 patterns + 19 guides). Sessions 81-82 actively wrote 8 G9 rules + 3 G2 rules via `/extract-artifacts`, with IB-164 sweeping more — directly counter-producing what the migration would absorb. The collapse is implicitly rejected by behavior. If it ever revives, the entry point is the design note itself.

4. **Weight calibration for use-case-registry core/long-tail estimates** — Dropped. Same root cause as today's earlier drop of `/summarize-encounters`: the trigger ("once encounter tracking accumulates data") cannot fire while assess-* skills haven't written a single `librarian-encounter-log` file across 27 sessions since session-52 deployment. Estimate-pending status is already documented in `2026-04-21-librarian-use-case-registry.md` §286.

5. **`agent.md` variant-depth iteration** — Dropped. The stub-status + iteration-on-demand gate is already in the file consumers read: `operations/references/librarian/agent.md:54-55` instructs "deeper per-variant composition iterates in later sessions. A consumer who needs a variant-specific deep dive should ask for it." The trigger fires naturally during query handling.

Files touched:

- `systems/improvement-loop/PROGRESS.md` — five lines removed from the prio queue.
- `systems/improvement-loop/operations/references/guide-routing-table.md` — new "Disambiguation Notes" section appended after Trigger Keywords; ~3 sentences capturing the G2/G7 weakened-discriminator state + remediation candidates.

## Why

The prio queue had drifted into a long-tail of `[trigger]`-gated watch items that paraphrased mechanisms living elsewhere in the system. Each entry costs per-session attention (they appear in PROGRESS.md, which is read at session start), and several carried hardcoded counts that drift — both anti-patterns flagged in standing feedback memory.

The audit principle: for each queue item, ask *where else* the load-bearing knowledge lives. If the rule is at the source of truth, the entry duplicates. If the trigger fires during normal pipeline reads, the entry is mechanism-on-mechanism. If the premise has been counter-produced, the entry is dead. If the substance is genuinely durable but in the wrong place (G2 vs G7), lift it to the right reference doc — don't keep it queued.

This composes with `dropped-summarize-encounters-from-il-priority-queue.md` (earlier same session): that SL applied the audit to one item; this one extends it across the queue.

## Affected Items

- `systems/improvement-loop/PROGRESS.md` — five entries removed from "Nick's Prioritizaton" queue. The "Current Focus" snapshot and Session 82 sections remain intact.
- `systems/improvement-loop/operations/references/guide-routing-table.md` — new "Disambiguation Notes" section added (the only durable structural change).
- `systems/improvement-loop/operations/references/research-dimensions.md` — referenced as the durable home for graduation criteria; not edited.
- `systems/improvement-loop/operations/references/librarian/agent.md` — referenced as the durable home for variant-iteration gate; not edited.
- `systems/improvement-loop/project-management/design-notes/2026-04-20-pipeline-collapse-proposal.md` — remains at `stage: "draft"`; status unchanged.
- `systems/improvement-loop/project-management/design-notes/2026-04-21-librarian-use-case-registry.md` — referenced as the durable home for estimate-pending status; not edited.
