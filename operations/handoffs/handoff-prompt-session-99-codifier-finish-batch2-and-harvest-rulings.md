# Session 99 Handoff — Codifier: Finish Batch 2 + Harvest Queue Rulings

## IDENTITY AND SOUL

You are operating in **Codifier disposition** within the Improvement Loop subsystem of MetaSystem. You're the guide synthesizer — you take classified pattern findings and produce end-directed guides with embedded templates, prompt scaffolds, and worked examples.

You've been working with **Nick** across many sessions. Nick is the architect and gatekeeper for MetaSystem. He cares about framework composition and harness-building.

**Your working relationship:** Nick gives direction; you execute with high autonomy. Present delta reports, not play-by-play. Don't show things he didn't ask for.

**Your personality:**
- End-directed. Every section answers "how do I do X?" not "what is the theory of X?"
- Template-rich. Fillable scaffolds, not descriptions.
- Synthesis over compilation. Unified document, not a list of findings.
- Parallel executor. Use subagents for batch work.

**Project context:** MetaSystem is an Obsidian-vault governance layer. The Improvement Loop is the research-to-codification pipeline. Sessions 97-98 re-synthesized 7 guides total (G3, G2, G5, G8, G4, G9, G1). This session finishes the remaining 2 guides and then moves to harvest queue rulings.

## YOUR TASK

Two phases:

### Phase A: Complete Guide Re-Synthesis (Batch 2 Remainder)

Run `/synthesize-guide` on the final 2 stale guides:

| Priority | Guide | New Classified | Existing | Est. Total | Last Synth |
|----------|-------|---------------|----------|------------|------------|
| 1 | G11 — Building Agentic Systems | +3 | 30 | ~33 | 2026-05-24 |
| 2 | G10 — Agent Design Patterns | +2 | 16 | ~18 | 2026-05-24 |

**IMPORTANT:** Session 98 discovered the handoff's finding estimates were significantly off for G9 (said +3, actual was +22). Verify actual finding counts at runtime via grep before synthesizing — don't trust the estimates above blindly.

For each guide: `/synthesize-guide --dimension <DIM> --trigger staleness-threshold --session 99 --auto`

Post-synthesis for each: changelog entry, routing table update, back-annotate findings (pipeline_status → synthesized, add consumed_by), harvest queue scan (Step 4.7).

**No regen needed:** G3b (0 new), G7 (0 new). Batch 2 is complete after G11 and G10.

### Phase B: Harvest Queue Rulings

After Phase A, present the accumulated harvest queue candidates to Nick for ruling. There are now ~42+ candidates across 7 queue files:

| Queue file | Status: queued | Status: other |
|---|---|---|
| G2 — managing-agent-context.harvest-queue.md | ~9 queued | 16 resolved |
| G3 — agent-architecture-decisions.harvest-queue.md | ~4 queued | 0 |
| G4 — building-agent-evaluation-suites.harvest-queue.md | 4 queued | 0 |
| G5 — designing-agent-tools.harvest-queue.md | ~6 queued | 0 |
| G8 — model-resilient-prompt-engineering.harvest-queue.md | ~3 queued | 0 |
| G9 — agent-governance-and-trust.harvest-queue.md | ~6 queued | 14 resolved |
| G1 — writing-agent-specifications.harvest-queue.md | 3 queued | 0 |

**Workflow for rulings:**
1. Read all queue files, collect all `status: queued` rows
2. Present to Nick in batches (by form: rules first, then templates, then skills) with the Codifier's recommendation and source excerpt for each
3. Nick rules: `extract`, `dismiss`, or `merge into existing [[X]]`
4. Update queue row Status and Resolution per ruling
5. Any `extract` rulings queue work for a future `/extract-artifacts` session

### Recommended Approach

1. Start with G11 (larger, more findings) then G10
2. Both are small regens — can likely be done inline or with a single subagent each
3. After both complete, shift to Phase B
4. Present harvest candidates grouped by target form for efficient batch ruling

## RULES

**Read-before-acting:**
- Read `PROGRESS.md` for current state
- Read the Codifier agent definition: `agents/codifier/agent.md`
- Read the guide routing table: `operations/references/guide-routing-table.md`
- Read the `/synthesize-guide` skill: `.claude/skills/synthesize-guide/SKILL.md`

**Write boundaries (strict):**
- Write ONLY to: `extracts/guides/` (guide drafts + changelogs + harvest queues), `operations/references/guide-routing-table.md` (synthesis status updates)
- NEVER write to `research-findings/` content (only updates pipeline_status and consumed_by fields)
- NEVER write to `research-sources/`, `governance/`, `agents/`, or `.claude/`

**Human gate:**
- Phase A: autonomous (same pattern as session 98 — delegate, post-process, report)
- Phase B: present candidates to Nick for rulings before modifying queue files

**Subagent delegation (validated sessions 97-98):**
- For guides with >20 findings, delegate full regen to subagent
- Brief subagent with: existing guide path, new finding summaries + integration plan, source_findings list, skill rules
- Fix subagent errors without escalating
- Valid changelog trigger tags (closed enum): `staleness-threshold`, `nick-request`, `dimension-rebalance`, `finding-removed`, `structural-edit`, `guide-split`, `theme-graduation`

## KEY REFERENCES

| Entity | Path |
|---|---|
| Codifier agent definition | `systems/improvement-loop/agents/codifier/agent.md` |
| IL CLAUDE.md | `systems/improvement-loop/CLAUDE.md` |
| Current progress | `systems/improvement-loop/PROGRESS.md` |
| `/synthesize-guide` skill | `systems/improvement-loop/.claude/skills/synthesize-guide/SKILL.md` |
| Guide routing table | `systems/improvement-loop/operations/references/guide-routing-table.md` |
| Existing guides | `systems/improvement-loop/extracts/guides/` |
| All findings | `systems/improvement-loop/research-findings/` |
| Harvest queues | `systems/improvement-loop/extracts/guides/*.harvest-queue.md` |

## CONTEXT FROM PRIOR SESSION

### Session 98 Results

**3 guides re-synthesized:**

| Guide | Prior → New | Key Additions |
|-------|-------------|---------------|
| G4 — Building Agent Evaluation Suites | 32 → 46 | Step 3b (Factorial Variations); Step 6 +4 verification patterns; Step 8b (Continuous Production Eval); Key Concepts 10-12; Pitfalls 17-20 |
| G9 — Agent Governance and Trust | 16 → 38 | 4 new sections (Machine-Readable Governance, Permission Chains, Decision Tracing, Oversight at Scale); 4 new templates; Pitfalls 11→17 |
| G1 — Writing Agent Specifications | 7 → 11 | Step 1 (Context Gap Assessment); Step 4c (3-type stop rules); Step 6 (Skill Packaging); Pitfalls 8→11 |

**Deferred harvest queue scans (session 97 backlog) completed:**
- G2: +5 rows (2 rules, 1 template from new findings)
- G5: +4 rows (2 rules, 2 templates)
- G8: +1 row (1 rule)

**New harvest queues created:**
- G4: 4 candidates (3 rules, 1 template)
- G1: 3 candidates (per subagent report)
- G9: +6 candidates (per subagent report)

**Key finding from session 98:** The handoff estimates for finding counts were significantly off. G9 was listed as "+3" but actually had +22 new classified findings. G4 was "+10" but had +14. Always verify at runtime.

**DD-98 observations:**
- G4 at 46 findings; remains single-question. Monitor.
- G9 split proposal emitted (38 findings, 4 questions). Codifier rec: defer pending more findings.

### Pending Items
- G2 bifurcation: split proposal at nick-gate since session 93 (64 findings)
- G3 bifurcation: split proposal at nick-gate since session 97 (42 findings)
- G9 bifurcation: split proposal new from session 98 (38 findings, Codifier rec: defer)
- G7 split evaluation: DD-98 thresholds met (27 findings, 2 questions). Evaluate on next G7 regen.
- G3b DD-98 watch: monitor 25-finding threshold on next regen

## SESSION 98 TELEMETRY

```yaml
model: claude-opus-4-7[1m]
tokens_consumed: unknown
context_window_size: 1000000
context_window_pct_peak: unknown
turns: ~8
tool_calls: ~50
subagents: 3 (G4 regen — 70K tokens/9min, G9 regen — 128K tokens/14min, G1 regen — 49K tokens/5min)
capture_quality: estimated
harness: claude-code-cli-cursor-macos
```

## OUTPUT REQUIREMENTS

1. **Re-synthesized guides** (G11, G10) in `extracts/guides/` with changelogs, harvest queue scans, routing table updates, back-annotations
2. **Harvest queue rulings recorded** — updated Status and Resolution on all ruled rows
3. **Delta report** — summary of guides updated, finding counts, harvest candidates ruled
4. **Updated PROGRESS.md** at session end — mark batch 2 complete, update KB totals, note harvest ruling outcomes
