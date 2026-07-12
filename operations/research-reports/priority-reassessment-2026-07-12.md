---
title: "Priority Reassessment Report — 2026-07-12"
type: "research-report"
category: "priority-reassessment"
created: "2026-07-12"
author: "improvement-loop"
findings_scanned: 6
candidates_flagged: 1
---

# Priority Reassessment Report — 2026-07-12

Scoped pass (session 132) over the findings whose evidence base grew in sessions
131–132: the two named in the session-132 handoff plus the C4/C5/C7 fold targets and
the new cross-repo synthesis. Not a full-KB scan.

## Summary

- Findings scanned: 6
- Reassessment candidates: 1
- Proposed priority bumps: 1 (a null→P3 triage normalization, not an evidence bump)
- Proposed evidence upgrades: 0
- Proposed adoption status changes: 0

## Candidates

### Verbatim-Storage Thesis for Long-Term Agent Memory
- **Current priority:** null
- **Proposed priority:** P3 (Monitor)
- **Criteria triggered:** none formally — this is a triage normalization, not a threshold crossing
- **Evidence summary:** 1 independent source (MemPalace repo; the LongMemEval benchmark evidence ships in the same repo, so it is not independent), 8 related_findings links (2 extended-by, 3 contradicts, 3 same-problem), ~49k stars, benchmark reproducibility documented
- **Rationale:** `priority: null` means un-triaged, and single-source repo intake defaults to P3 under the shared triage contract. The finding is heavily cross-linked and directly relevant to the Memongo iteration, but remains single-source — P3 is the honest tier. Proposing the normalization so the finding stops reading as unprocessed.

## No Change (Confirmed)

| Finding | Priority | Evidence movement 131–132 | Why no change |
|---|---|---|---|
| gpt-54-tool-search-deferred-tool-loading | P1 (Implement Now) | 3 independent instances (OpenAI API, Anthropic tool-search, Claude Code `defer_loading`) — the KB's best-evidenced tool-scaling pattern | Already at ceiling; evidence Strong |
| static-tool-set-mode-changes-as-callable-tools | P2 (Design Required) | C4 fold: opencode independent cross-harness implementation (1→2 independent sources) | 2 < the 5-source P1 bar; already Strong first-party |
| append-only-context-updates-system-reminder-injection | P2 (Design Required) | C5 fold: opencode Context Epoch / Mid-Conversation System Message as named independent implementation (1→2) | Same — threshold for P1 not crossed |
| loop-detection-hash-based-sliding-window | P2 | C7 fold: opencode doom-loop-as-permission is the third response-strategy variant; detection mechanism now corroborated in 2 production harnesses + GSD's trajectory variant | Already P2; Medium→Strong has no defined criterion and the three variants differ in response, not just corroborate |
| permission-channel-as-escalation-steering-bus | P3 (Monitor) | Born cross-repo (omnigent + opencode, 3 mechanisms) — 2 independent sources at creation | One repo short of the 3-source P2 threshold. **Watch item:** a third independent implementation crosses it |

## Gate

Proposals await Nick's approval (skill Rule 1 — no auto-changes). On approval, the
single edit is `verbatim-storage-thesis-for-memory.md` frontmatter: `priority: null`
→ `"P3 (Monitor)"` + `last_updated` bump.
