# Improvement Loop — Progress

**Last Updated:** 2026-05-25 (session 100)

## Current Focus

Session 97 re-synthesized 4 guides (G3, G2, G5, G8) incorporating 45 newly classified pattern findings. Split proposal emitted for G3 (42 findings, 2+ practitioner questions). Harvest queue updated for G3 (+4 rows). 45 findings back-annotated.

**KB totals:** ~717 findings (45 synthesized this session), ~177 sources, 25 watched libraries, 24 analysis docs. 10 guides re-synthesized to date (G3:42, G2:64, G5:23, G8:20, plus 6 prior). 2 split proposals (G2 at nick-gate, G3 new). 19 harvest queue candidates across 2 queue files.

**Next session target:** Continue guide re-synthesis — G4 (+10 findings, largest remaining delta), G9 (+3), G1 (+3), G11 (+3), G10 (+2). Plus deferred harvest queue scans for G2, G5, G8.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **~~`[active]` Guide re-synthesis cycle (batch 1)~~** — Completed session 97. G3 (24→42), G2 (48→64), G5 (16→23), G8 (16→20). 45 findings synthesized.
- **`[trigger]` Guide re-synthesis cycle (batch 2)** — G4 (+10), G9 (+3), G1 (+3), G11 (+3), G10 (+2). G3b and G7 have 0 new classified findings — no regen needed.
- **`[nick-gate]` G2 bifurcation** — Split proposal at `operations/split-proposals/2026-05-24-managing-agent-context-split-proposal.md`. Now at 64 findings. Requires per-split DD to execute.
- **`[nick-gate]` G3 bifurcation** — Split proposal at `operations/split-proposals/2026-05-25-agent-architecture-decisions-split-proposal.md`. At 42 findings. Codifier rec: re-evaluate bifurcation.

---

## Logged-for-future

Trigger-gated carryover. Don't action unless trigger fires.

1. **G7 split evaluation** — Both DD-98 thresholds met at last synthesis (27 findings, 2 questions). Evaluate on next G7 regen.
2. **G3b DD-98 watch** — Would cross 25-finding threshold after next synthesis (~25 with 5 new pattern findings).
3. ~~**Edit-tool stale-read pattern** — codify sequential-edits-per-file workaround for subagent-batched workflows.~~ — **Resolved session 100.** Already codified in `/extract-artifacts` SKILL.md Step 4.8 (partition-by-queue-file rule, session 85). Only skill that hits the pattern. Audit trail in session 83-85 SL entries + Codifier reflection. No general rule needed per tolerate-one-off principle.
4. ~~Did we have skills to monitor and archive/delete tmp files across the workflows?~~ — **Resolved session 100.** Created `/cleanup-cache` Owner skill. Repo-cache (976MB) is the only unmanaged target; other workflows self-clean.
5. ~~Do we have a diagram in docs/ that includes the artifacts created/edited by each agent in the IL system? What about one that showcases which steps include subagents, so we can identify where in the workflows we have subagent prompts that we need to monitor for quality.~~ — **Resolved session 100.** Two new docs in `docs/2026-05-25/`: `skill-artifact-map.md` (per-skill C/E/R file paths) and `subagent-topology.md` (7 skills spawn subagents, 3-tier prompt sensitivity ranking). 
6. **New `/research-loop`** to replenish harvest queues after this large re-extraction cycle.