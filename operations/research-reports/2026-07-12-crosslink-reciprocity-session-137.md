---
title: "Finding Crosslink Report — 2026-07-12 (session 137, batch reciprocity)"
type: "research-report"
category: "finding-crosslink"
created: "2026-07-12"
author: "improvement-loop"
scope: "session-136 extraction batch (findings touched 2026-07-12)"
links_written: 193
files_modified: 131
---

# Finding Crosslink Report — 2026-07-12 (session 137)

Scoped reciprocity pass over the session-136 extraction batch, executing the delta
report's named follow-up: the 8 extraction subagents recorded one-way
`related_findings` links into lanes they didn't own (by design); this pass completed
the reciprocals. Detection was script-based (deterministic scan via `kb_parser`), not
subagent evaluation — no new relationships were invented; every entry written is the
typed inverse of a link already accepted into the KB in session 136.

## Summary

| Metric | Count |
|--------|-------|
| Findings touched 2026-07-12 (batch) | 105 |
| Batch-authored one-way links found | 193 |
| Reciprocal entries written | 193 |
| Target files modified | 131 |
| Write failures | 0 |
| Corpus-wide `validate_frontmatter.py` | exit 0 |

Reciprocal map applied: enables↔enabled-by, extends↔extended-by,
contradicts↔contradicts, same-problem↔same-problem, part-of↔has-part. Session-132
precedent: batch reciprocity completion executes as mechanics (the forward links were
already gated in with the extraction sweep); this report is the audit trail.

## Out of scope — pre-existing corpus debt (surfaced, not fixed)

The detection scan ran corpus-wide and surfaced a much larger pre-existing condition
that this batch pass deliberately did NOT touch:

| Debt class | Count | Nature |
|---|---|---|
| Missing reciprocals (corpus-wide, incl. the 193 fixed) | 1,185 | One-way links from all pre-batch eras; 992 remain after this pass |
| Typed mismatches (both files linked, rel types disagree) | 205 | e.g. A says same-problem, B says extended-by; needs per-pair adjudication |
| Non-canonical rel vocabulary | 53 | companion, depends-on, contrasts-with, feeds-into, related, part-contains, solved-by, mitigates, same-technique — outside the 4-type contract |
| Dangling targets (linked file doesn't exist) | 6 | Likely renames; needs filename repair |
| Over-cap hubs (>15 links, pre-existing) | 16 | Worst: agent-context-kiss-commandments (42), agent-architecture-layer-impermanence (32), ACE evolving-playbook (30) |

**Recommendation (gated):** a dedicated corpus-wide linkage-hygiene sweep session —
reciprocal backfill is scriptable mechanics, but the 205 mismatches and 53
vocabulary strays need typed adjudication (subagent fan-out), and hub findings need
the soft-cap judgment call. Sized like a session-127-style sweep. Not started without
Nick's ruling.

## Isolates among today's new findings (flagged, not forced)

8 findings created 2026-07-12 carry zero `related_findings`:
`bench-verified-harness-capability-flags`, `dev-cost-estimation-bias-correction`,
`injection-observation-split-bridge-forwarder`, `label-taint-tracking-composable-policy-state`,
`plugins-as-sdk-clients`, `time-boxed-automated-pr-compliance`,
`two-tier-tool-contracts-complexity-firewall`, `ubiquitous-language-glossary-with-anti-terms`.

Per the skill's isolate-de-isolation data (subagents reject ~100% of isolate
candidates; manual review historically recovers ~2 per pass), these are flagged for
an opportunistic manual pass, not force-linked here.

## New-link detection

Not run. The delta report's follow-up named reciprocity only; the session-136
subagents already performed relationship detection at extraction time. A speculative
pair-evaluation fan-out over the 65 new findings was skipped on token-economy grounds
— it can ride the proposed corpus-hygiene sweep if Nick wants it.
