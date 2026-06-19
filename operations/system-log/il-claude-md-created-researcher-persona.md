---
notion_id: null
log_entry: "IL CLAUDE.md created — Researcher persona formalized as system identity"
actor: "Nick + Agent: Claude"
area: null
change_type: "Implementation"
milestone: null
rationale: "The Improvement Loop was the only graduated system without a CLAUDE.md. Created one that establishes the Researcher as the default persona (analytical, evidence-first, neutral-on-implementation), documents the pipeline stages, inlines 6 binding DD constraints (DD-29, 30, 31, 36, 39, 41), and maps the data layout. The Proposer persona is intentionally excluded — it lives in the research-proposer skill definition."
source_dd: "DD-29, DD-30, DD-31, DD-36, DD-39, DD-41, DD-52"
target_system: "improvement-loop"
date: "2026-04-07"
---

## What Changed

- Created `systems/improvement-loop/CLAUDE.md` (126 lines, 9 sections)
- Established Researcher persona as system-level cognitive disposition: evidence over intuition, expansive intake with ruthless extraction, neutral on implementation, source diversity, deduplication discipline, transcript-first
- Documented pipeline: Sources → Extract → KB → [human gate] → Propose → [human gate] → Codify
- Inlined key constraints from 6 binding DDs so agents don't need to read the DD files to know the rules
- Explicitly scoped out the Proposer persona and prompt-evaluator/enhancer skills
- Noted fractal compliance gaps (governance/, agents/, app/, archive/ not yet created)

## Affected Items

- `systems/improvement-loop/CLAUDE.md` — created
- `PROGRESS.md` — updated to reference new file
