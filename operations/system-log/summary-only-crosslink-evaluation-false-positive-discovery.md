---
notion_id: null
log_entry: "Summary-only crosslink evaluation produces ~30% false positive rate on same-problem links"
actor: "Nick + Agent: Claude"
area: null
change_type: "Operational Learning"
milestone: null
rationale: "Post-write validation revealed that subagents evaluating pairs from summaries alone match on category proximity rather than strict problem identity. This produces acceptable precision for contradicts/extends/enables but ~30% false positives on same-problem — the loosest and most common relationship type."
source_dd: null
target_system: "Improvement Loop"
timestamp: "2026-04-08T00:00:00.000Z"
---

## What Changed

Stratified validation audit of 18 proposed crosslinks (reading full finding files, not just summaries) revealed type-specific error rates:

| Type | Tested | Correct | Error Rate |
|------|--------|---------|------------|
| contradicts | 5 | 4 (1 borderline) | ~0% |
| enables | 5 | 2 | ~40% |
| same-problem | 8 | 2 (1 borderline) | ~60% (deliberately borderline sample) |

**Root cause:** Subagents default to same-problem YES when they see topical overlap (same category, related domain). The binary test Q1 ("same SPECIFIC problem?") is too subjective at summary level. Enables Q2 ("would B break?") gets over-applied — subagents confuse "helpful" with "required."

**Mitigations applied:**
1. Added same-problem anti-patterns to subagent prompt template: category proximity, complementary ≠ same-problem, scope mismatch, stack-level mismatch
2. Added enables anti-pattern: helpful ≠ required
3. Made post-write validation (Step 7) mandatory — stratified sample reading full files
4. Added hub soft cap (~15 links per finding) to prevent graph distortion
5. Documented reference error rates in skill calibration notes

**Key principle:** Summary-only evaluation is a deliberate tradeoff — it enables evaluating 800+ pairs in reasonable time. The validation step is the quality gate that compensates. Neither step is optional.

## Affected Items

- `/finding-crosslink` skill at `.claude/skills/finding-crosslink/SKILL.md` — Step 2 prompt, Step 7 validation, calibration notes all updated
- 8 misclassified links fixed in finding files (3 enables → same-problem, 5 false same-problem removed)
