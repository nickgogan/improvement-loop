---
name: "PR-Review-Mined Rules Corpus with Per-Rule Provenance"
summary: |-
  Plain English: instead of hand-writing style guides for coding agents, mine the
  project's own PR-review history for the corrections maintainers actually make, compile
  them into agent-loadable rule files, and tag every rule with a provenance ID so it can
  be traced, audited, and retired. Pydantic AI's `agent_docs/` guideline set is
  explicitly "extracted from PR review patterns"; each rule carries an HTML-comment
  `rule:NNN` ID, the corpus is chain-loaded by the root AGENTS.md (index always, topic
  guides on demand), and directory-scoped AGENTS.md files layer location-specific rules
  on top. Review history becomes a machine-maintained rules corpus rather than a
  hand-curated style doc.
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "session-history-mining-for-skill-discovery.md"
    rel: "same-problem"
  - file: "battle-scar-anti-pattern-documentation.md"
    rel: "same-problem"
  - file: "claudemd-context-rot-from-indiscriminate-rule-accu.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "context-engineering"
  - "governance"
  - "rules-corpus"
---

# PR-Review-Mined Rules Corpus with Per-Rule Provenance

## What It Is

An agent-guideline corpus whose content source is the repository's own review history.
Three properties distinguish it from a conventional CLAUDE.md rules file:

1. **Mined, not authored** — the guidelines are "extracted from PR review patterns":
   corrections maintainers repeatedly made become codified rules, so the corpus tracks
   observed failure modes rather than aspirational style.
2. **Per-rule provenance IDs** — every rule is tagged `<!-- rule:NNN -->`, giving each an
   addressable identity for referencing, deduplicating, auditing, and retiring.
3. **Layered loading** — root AGENTS.md always chain-loads the index; four topic guides
   load on demand; 12 directory-scoped AGENTS.md files add location-specific rules only
   when an agent works there.

(`agent_docs/index.md`, root `AGENTS.md`)

## Why It Matters

Rules files accrete by anecdote and rot silently — the KB's context-rot findings
document the failure mode. Mining review history fixes the *intake* problem (rules
correspond to real recurring corrections, by construction) and provenance IDs fix the
*lifecycle* problem (a rule can be traced to its origin and retired when the pattern
stops recurring). It is the review-time sibling of session-history mining: both convert
interaction exhaust into curated, loadable guidance instead of relying on humans to
remember what keeps going wrong.

## Why People Are Using It

Maintained as the primary coding-guideline layer for contributor agents on a
high-traffic production framework repo. Source: Observed in
[pydantic-ai](https://github.com/pydantic/pydantic-ai) v2.9.0 — see
[[pydantic-ai-analysis]] for structural details.

## Potential Alternatives

- **Hand-curated style docs** — cheaper to start, but content reflects author intuition
  rather than observed corrections, and there is no retirement signal.
- **Session-history mining** (skill discovery) — same exhaust-to-guidance move on agent
  transcripts instead of human review comments.
- **Lesson stores** (append-only operational lessons) — per-incident granularity with a
  promotion lifecycle; the rules corpus is the already-promoted end state.

## Potential Improvements

- Closing the loop mechanically: an agent that watches merged-PR review threads and
  proposes rule additions/retirements with the `rule:NNN` bookkeeping done.
- Frequency metadata per rule (how often the pattern recurs) to drive pruning.

## Potential Failure Modes

- **Staleness inversion** — mined rules encode past codebase eras; without retirement
  discipline the corpus fights current architecture.
- **Overfitting to reviewer idiosyncrasy** — one maintainer's preferences become
  system-wide law.
- **Unbounded growth** — provenance makes rules auditable, not small; the corpus still
  needs the same token-budget discipline as any always-loadable context.
