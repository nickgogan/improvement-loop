# Improvement Loop — Progress

**Last Updated:** 2026-05-24 (session 87 close — handoff prepared for session 88)

## Current Focus

Session 87 executed the deferred visualization brainstorm (top of Nick's Prioritizaton since session 62). Three artifacts in `docs/2026-05-24/`: D (`agent-interaction-model.md`), B (`pipeline-trace.md`), C (`ownership-map.md`). Target A (DD graph) deferred to next session as a *digestibility brainstorm* — uncertain whether the artifact's value justifies the maintenance cost at the current corpus size. Mermaid established as docs/ default format. `handoff-protocol.md` drift cleaned up (4-state `pipeline_status` documented; skill tables refreshed). No-hardcoded-counts sweep applied across session outputs plus adjacent surfaces.

**Next session target:** DD-graph digestibility brainstorm in **Owner disposition**. Handoff prompt: `operations/handoffs/handoff-prompt-dd-graph-digestibility.md`.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **DD-graph digestibility brainstorm** — [deferred] decide whether Target A (DD graph) is worth producing, and if so in what form. `docs/` conventions established session 87.
- **Drift sweep** — [deferred] `target_system` case inconsistency · `scope_category` enum verification against `_schema.yaml` · quoted-YAML `pipeline_status` normalization. Surfaced session 87. Trigger: fold into A brainstorm if scope permits, or separate sweep session.

---

## Logged-for-future

Trigger-gated carryover. Don't action unless trigger fires.

1. **Bidirectional cross-refs hygiene pass** — G2/G7/G3b/G5/G9 should have `[[building-agentic-systems]]` entries in their Related Guides sections.
2. **DD-98 split-trigger watch** on G11's first re-synthesis. Count threshold (≥25) met.
3. **Edit-tool stale-read pattern** — codify sequential-edits-per-file workaround for subagent-batched workflows.
4. **New `/research-loop` or guide regen** to replenish harvest queues.
5. **DD `title:` slug field** — backfill a 5-8 word `title:` on each DD's frontmatter across IL and Meta-System. Filenames are bare `DD-XX.md`; `decision:` text is too long for compact labels. Trigger: first surface that needs compact DD labels (visualization, listings, search UIs). Surfaced session 87 during visualization brainstorm.
