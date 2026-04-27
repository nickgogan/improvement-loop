---
notion_id: 32b1e08b-9b34-81fd-80b5-eb1940b16a9a
name: CLAUDE.md Context Rot from Indiscriminate Rule Accumulation
summary: Continuously appending behavioral rules to CLAUDE.md causes silent model performance degradation ('context rot') because every rule loads into every conversation regardless of relevance. Over 100
  lines, aggregate noise dilutes the attention given to actually relevant tokens.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- why-your-coding-agent-keeps-getting-dumber.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: context-file-instruction-bloat-eth-zurich.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: context-curation-over-context-stuffing.md
  rel: extends
- file: ace-delta-updates-over-monolithic-rewrites.md
  rel: same-problem
- file: pointers-over-copies-in-context-files.md
  rel: same-problem
- file: tiered-context-injection-over-monolithic-files.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
- claudemd-minimum-viable-rule-only-add-globally-true-lines.md
---
# CLAUDE.md Context Rot from Indiscriminate Rule Accumulation

## What It Is
As users add rules to CLAUDE.md each time something goes wrong, the file grows and loads in full at the start of every session. The accumulation of context noise gradually reduces instruction-following quality and increases hallucination rates -- a process called 'context rot'. Users frequently blame model providers for 'nerfing' models when the actual cause is their own bloated CLAUDE.md.

## Why It Matters
Context rot is insidious because it is invisible -- there is no error message, no warning, just a gradual decline in output quality.

## Why People Are Using It
CLAUDE.md rule accumulation is the default, naive approach because it feels productive -- each addition seems like a useful refinement.

## Potential Alternatives
Keep CLAUDE.md to 3-5 globally true, universally relevant lines. Use ACE for domain-specific behavioral knowledge.

## Potential Improvements
Tooling that auto-analyzes CLAUDE.md for token cost vs. relevance per session type could flag bloat early.

## Potential Failure Modes
Users who don't understand context rot continue the cycle indefinitely. Periodic 'compaction' of CLAUDE.md by Claude itself introduces a different risk: catastrophic context collapse.

## Extraction Note — 2026-04-27 (Session 84)
Merged as DD-97 extension into **rule**: [[claudemd-minimum-viable-rule-only-add-globally-true-lines]] in `extracts/rules/`. The volume-cap mechanism (Tier-0: 3-5 lines; Tier-1: 60-80 line band) was added as an operate-stage backstop to the existing per-line global-truth test. Extension proposal: `operations/extension-proposals/2026-04-27-claudemd-global-rule-cap-extension-proposal.md` (Option A applied).
