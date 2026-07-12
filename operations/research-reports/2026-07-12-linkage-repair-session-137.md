---
title: "Linkage Repair Report — 2026-07-12 (session 137, batch scope)"
type: "research-report"
category: "linkage-repair"
created: "2026-07-12"
author: "improvement-loop"
scope: "session-136 batch — authority backfill + source↔finding asymmetries"
repairs_executed: 30
---

# Linkage Repair Report — 2026-07-12 (session 137)

Scoped pass executing the session-136 delta report's linkage follow-ups. All repairs
completed one-way links already recorded in the KB (mechanics precedent, session 132);
nothing content-new was invented. Writes via `kb_parser.write_frontmatter` (round-trip
validated); corpus-wide `validate_frontmatter.py` exit 0 after.

## Executed repairs

| Class | Count | What was done |
|---|---|---|
| Source→authority backfill | 21 | Sources with empty `authority` whose covering authority entry already listed them: Anthropic (8), Cloud Codes (4), Matt Pocock (2), and one each AI LABS, Devsplainers, Mark Kashef, Kun Chen, Prompt Engineering, Chase AI, AI Code That Works |
| Finding→source asymmetries | 8 | Finding listed the source; source's `findings` array lacked the back-ref (targets: anthropic-skills-repo ×2, anthropic-claude-code-skills-docs, anthropic-effective-context-engineering, anthropic-demystifying-evals, oracle-agent-memory-amnesia-blog, two Obsidian-setup sources) |
| Source→finding asymmetries | 1 | `anthropic-claude-code-session-management-1m-context` claimed `fork-subagent-parallel-trajectory-exploration`; source ref added to the finding |

## Held for Nick's gate (not touched)

1. **Duplicate source pair (known):** `karpathys-obsidian-rag-claude-code.md` vs
   `karpathy-obsidian-rag-markdown-knowledge-base.md`. 4 asymmetric links route through
   the older file (`scale-threshold-heuristic-obsidian-vs-rag`,
   `karpathy-llm-knowledge-base-obsidian-rag`, `claudemd-as-knowledge-base-traversal-guide`,
   `index-file-navigation-as-rag-replacement`). Fixing them mechanically would deepen the
   duplicate — they resolve automatically in the merge. **Merge recommendation:** keep
   `karpathys-obsidian-rag-claude-code.md` (referenced by more findings), fold the other's
   `findings` array in, delete, and repoint.
2. **Duplicate authority pair (surfaced session 136):** `nate-b-jones.md` vs
   `ai-news-strategy-daily-nate-b-jones.md` — same person/channel; merge candidate,
   same shape as the source pair.

## Checked, no repair needed

- **17 batch-touched findings with empty `sources`** — all repo-analysis-born
  (session-131/132 omnigent/opencode promotions, e.g. `permission-channel-as-escalation-steering-bus`,
  `label-taint-tracking-composable-policy-state`). Per skill calibration, repo-born
  findings legitimately trace to `watched-libraries/analysis/` docs, not `research-sources/`.

## Remaining corpus-level debt (pre-existing, out of batch scope)

| Metric | Before | After | Note |
|---|---|---|---|
| Orphaned findings | 150 | 150 | Bulk are repo-born/legacy; needs a triage pass to separate legitimate from broken |
| Unlinked sources | 12 | 11 | Old arXiv/Willison-era entries |
| Asymmetric links | 46 | 37 | The 4 karpathy holds + 33 legacy |
| Broken references | 24 | 24 | Untouched — needs filename adjudication |

These ride the same proposed corpus-hygiene sweep as the crosslink debt (see
`2026-07-12-crosslink-reciprocity-session-137.md` §Out of scope) — one gated sweep
session covering reciprocals, typed mismatches, vocabulary strays, broken refs, and
the orphan triage together.
