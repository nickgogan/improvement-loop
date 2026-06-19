---
notion_id: null
log_entry: "Bulk migration enables classification produced 85% error rate — 'helpful ≠ required' threshold not enforced at scale"
actor: "Nick + Agent: Claude"
area: null
change_type: "Operational Learning"
milestone: null
rationale: "Session 14 migrated 102 legacy untyped crosslinks. 34 were classified as 'enables' (33% rate vs KB historical 5%). Spot-check of all 34 found only 5 correct (14.7%). The 29 incorrect pairs were either removed (21) or reclassified to same-problem (6) or extends (2). Root cause: migration subagents applied a weaker Q2 threshold ('would B be somewhat less effective?') instead of the strict test ('would B break or degrade significantly?')."
source_dd: null
target_system: "improvement-loop"
timestamp: "2026-04-08T00:00:00.000Z"
---

## What Changed

Validated all 34 enables links from the session 14 legacy migration. Results:

| Verdict | Count | % |
|---------|-------|---|
| Correct | 5 | 14.7% |
| Reclassified → same-problem | 6 | 17.6% |
| Reclassified → extends | 2 | 5.9% |
| Removed | 21 | 61.8% |

46 finding files corrected. Net effect: KB crosslinks dropped from 1,087 to 1,054 (-33).

## Operational Learning

1. **Bulk classification amplifies enables over-reach.** When subagents classify many pairs quickly, they default to "enables" for any finding that is useful-to another. The strict Q2 ("would B break?") requires slow, deliberate evaluation.
2. **Default to same-problem during migrations.** Unless the evaluator can articulate what specific mechanism in B breaks without A, the relationship is same-problem at best.
3. **Enables error rate compounds:** Session 13 found ~40% enables errors. This migration produced 85%. The difference is scrutiny level — dedicated crosslink evaluation (session 13) vs bulk migration classification (session 14).
4. **Correct enables share a pattern:** All 5 correct pairs involved a finding that is an explicit sub-component or internal mechanism of the enabling finding (e.g., ACE framework enables ACE-specific mechanisms, layered memory stack enables cross-layer governance). The dependency is definitional, not just functional.
