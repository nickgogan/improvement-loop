---
type: "drift-report"
target_system:
  - "improvement-loop"
generated_by: "/detect-drift"
date: "2026-04-26"
invocation_context: "session-73 first smoke-test against live extracts corpus"
total_scanned: 31
drift_hits: 1
clean_count: 30
enumeration_gaps: 0
unresolvable_sources: 0
forms_scanned:
  - "rules"
  - "skills"
  - "templates"
  - "agents"
---

# Source Drift Report — 2026-04-26

**Invocation context:** session-73 first smoke-test against live extracts corpus

**Scan summary:** 31 artifacts scanned across 4 forms (rules: 12 / skills: 12 / templates: 5 / agents: 2); 1 drift hit; 30 drift-clean; 0 enumeration gaps; 0 unresolvable sources.

## Drift Hits

### agent-self-reporting-unreliability-independent-eval
- Source: [[agent-self-reporting-unreliability-independent-eval]]
- Source updated: 2026-04-20 (post-extraction)
- Artifact extracted: 2026-04-19
- Recommendation: dismiss as cosmetic

Source body shows post-extraction administrative updates: an `Extraction Note — 2026-04-19` section pointing to the new artifact; `consumed_by` list grown to include the rule extract and downstream guide `building-agent-evaluation-suites.md`; `pipeline_status: synthesized`. The artifact's Condition / Action / Enforcement / Contract sections remain faithful to the finding's substance ($14K voice agent case study, independent-evaluation requirement, self-report-isn't-verification rule). One-day gap is a strong signal of post-extraction bookkeeping rather than substance shift.

## Smoke-Test Observations

This is the first end-to-end run of `/detect-drift` (IB-157, session 71). Observations against the five smoke-test signals from the session-73 handoff:

1. **Enumeration coverage** — 31 / 31 artifacts enumerated across 4 forms (12 rules, 12 skills, 5 templates, 2 agents). No skips, no duplicates. `_index.md` exclusion working as specified. Clean.

2. **Source-pointer resolution** — 31 / 31 source findings resolved against `research-findings/`. 0 unresolvable. Clean.

3. **Field-name alignment (DD-96 amendment, session 71)** — 0 findings carry the legacy `updated` field; all 31 carry `last_updated`. The session-71 amendment to DD-96 (`source.updated` → `source.last_updated`) holds against live data. Clean.

4. **Recommendation enum distribution** — 1 hit, 1 `dismiss as cosmetic`. Single data point. Distribution across the three closed-enum values (`re-run /extract-artifacts on this finding`, `dismiss as cosmetic`, `reclassify`) cannot be validated from this run; needs accumulation across multiple drift-encountering runs.

5. **Lifecycle-pointer presence (DD-95, IB-156)** — 31 / 31 artifacts carry `last_change_*` pointers; 31 / 31 carry `deployed` markers. The pre-DD-95 graceful-degradation path was **not exercised** — the live corpus has been fully backfilled. Future validation against a pre-DD-95 artifact (archive, or a deliberate test fixture) is needed to confirm degrade-not-crash behavior.

### Additional Smoke-Test Finding — YAML Quote-Style Heterogeneity

Among the 31 artifacts scanned: 27 carry double-quoted `extraction_date` (`"2026-04-19"`) and 4 carry single-quoted (`'2026-04-19'`). This was first surfaced when an inline LLM-driven scan returned a false-clean (0 drift hits) — a quote-stripping bug in the inline parser silently masked the real drift hit (lexical compare of `"'2026-04-20'"` vs `"2026-04-19"` returns False because `'` is ASCII 0x27 < `2` 0x32). The codified `scan.py` helper (added this session — see `operations/system-log/session-73-codifier-detect-drift-smoke-test.md` for design rationale) handles both quote styles correctly.

Quote-style heterogeneity is a corpus-wide observation, not a `/detect-drift` issue — it potentially affects any skill that reads frontmatter (`/identify-artifacts`, `/extract-artifacts`, `/synthesize-guide`). Not blocking for this skill.

---

**Next:** Nick reviews this report and rules per entry. Re-extraction on the flagged artifact requires explicit ruling — this skill does not invoke `/extract-artifacts`.
