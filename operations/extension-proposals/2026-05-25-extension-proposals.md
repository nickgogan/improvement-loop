---
type: "extension-proposals-report"
target_system:
  - "improvement-loop"
generated_by: "/extract-artifacts"
date: "2026-05-25"
identification_report: "harvest-queue-batch-session-102"
total_rule_skill_candidates: 35
proposals_emitted: 11
no_match_passthrough: 24
forms_scanned:
  - "rules"
  - "skills"
---

# Extension Proposals — 2026-05-25 (Session 102)

Corpus scan of 33 harvest-queue rule candidates against 43 existing rules and 2 skill candidates against 26 existing skills. 11 semantic overlaps detected; 24 rule and 1 skill candidates pass through to drafting.

## Rule Extension Proposals

### pattern-scale-triggers-process-fix

**Form:** rule
**Existing artifact (primary match):** [[every-recurring-review-comment-triages-to-mechanism-or-judgment]]
**Codifier recommendation:** extend existing
**Why this match:** Both enforce the same invariant: recurrence at scale is a systemic signal requiring a process-level response, not repeated individual handling. The existing rule covers recurring review comments; this candidate generalizes to any recurring pattern.
**Diff sketch:** Append evidence row citing `pattern-scale-signals-systemic-not-individual-failure`. Body unchanged — the existing rule already captures the principle; this new evidence broadens the application scope.

### tool-enablement-is-security-boundary

**Form:** rule
**Existing artifact (primary match):** [[explicit-permission-allow-listing-for-agent-resource-access]]
**Codifier recommendation:** extend existing
**Why this match:** Both treat tool/resource access as a security gate requiring explicit authorization. The existing rule encodes allow-listing as the mechanism; this candidate reinforces that tool enablement is a security boundary, not a feature toggle.
**Diff sketch:** Append evidence row citing `tool-access-as-security-boundary-not-feature-toggle`. Consider strengthening invariant language: "Tool access changes are security decisions, not feature decisions."

### never-trust-agent-summaries

**Form:** rule
**Existing artifact (primary match):** [[agent-self-reporting-unreliability-independent-eval]]
**Codifier recommendation:** extend existing
**Why this match:** Both enforce independent verification over agent-produced reports. The existing rule covers self-reporting of task completion; this candidate extends to agent-produced summaries of evidence.
**Diff sketch:** Append evidence row citing `goal-backward-verification`. Body delta: add explicit mention of summaries alongside self-reports as untrusted agent outputs.

### build-context-before-capabilities

**Form:** rule
**Existing artifact (primary match):** [[fix-data-schema-before-automating]]
**Codifier recommendation:** extend existing
**Why this match:** Both enforce a sequencing constraint: establish the foundational layer before building on top. The existing rule covers data/schema; this candidate covers context infrastructure for agentic systems.
**Diff sketch:** Append evidence row citing `context-first-build-sequencing-for-agentic-systems`. Body delta: generalize the sequencing principle to include context infrastructure alongside data/schema.

### mutation-interceptors-own-output-validity

**Form:** rule
**Existing artifact (primary match):** [[hook-based-enforcement-for-agent-outputs]]
**Codifier recommendation:** extend existing
**Why this match:** Both govern tool-call interception as the ownership boundary for output validity. The existing rule covers PostToolUse hooks; this candidate extends to any mutation interceptor owning its output's validity.
**Diff sketch:** Append evidence row citing `tool-call-event-interception-pattern`. Body unchanged — the existing rule's invariants already cover this; new evidence reinforces.

### apply-hard-ceilings-to-agent-memory-files

**Form:** rule
**Existing artifact (primary match):** [[token-budget-pre-turn-projection]]
**Codifier recommendation:** create new (false positive)
**Why this match:** Both enforce bounded limits on context/memory to prevent degradation. However, the existing rule is about per-turn projection of token usage within a session; this candidate is about persistent memory file size ceilings across sessions. Different enforcement boundary (session turns vs. file system).
**Notes:** Despite semantic overlap in the "bounded limits" principle, the enforcement mechanisms are distinct enough that a new rule may be warranted. Nick decides.

### synthesize-at-query-time-never-re-index-llm-output

**Form:** rule
**Existing artifact (primary match):** [[never-ask-claude-to-compact-claudemd]]
**Codifier recommendation:** extend existing
**Why this match:** Both forbid LLM-driven reprocessing of accumulated content. The existing rule covers CLAUDE.md and load-bearing documents; this candidate extends the same invariant to KB indices and search layers.
**Diff sketch:** Append evidence row citing `write-time-vs-query-time-synthesis-kb-poisoning`. Body delta: generalize from "load-bearing documents" to include "accumulated knowledge indices and search layers."

### compact-proactively-at-checkpoints

**Form:** rule
**Existing artifact (primary match):** [[context-degradation-40-percent-threshold]]
**Codifier recommendation:** extend existing
**Why this match:** Both enforce action before context degrades. The existing rule says "dispatch at 40-50%"; this candidate says "compact proactively at checkpoints." Same invariant: act before quality loss, not reactively.
**Diff sketch:** Append evidence row citing `proactive-compaction-before-intelligence-degradation`. Body delta: add checkpoint-based compaction as a complementary trigger alongside percentage-based thresholds.

### never-inline-ephemeral-into-cached-layers

**Form:** rule
**Existing artifact (primary match):** [[never-ask-claude-to-compact-claudemd]]
**Codifier recommendation:** create new (false positive)
**Why this match:** Both protect stable content layers from contamination. However, the existing rule is about LLM-driven rewriting of documents; this candidate is about prompt assembly (ephemeral turn state vs. cached API layers). Different enforcement boundary (document editing vs. prompt construction).
**Notes:** The protection principle overlaps but the domains are distinct: document maintenance vs. API prompt caching. Nick decides.

### extract-snippets-via-shell

**Form:** rule
**Existing artifact (primary match):** [[agent-self-reporting-unreliability-independent-eval]]
**Codifier recommendation:** create new (false positive)
**Why this match:** Both enforce deterministic tools over agent-produced output. However, the existing rule is about task completion verification; this candidate is specifically about code snippet extraction methodology. Different enforcement boundary (completion assessment vs. code quoting).
**Notes:** Shares the broad principle of "environmental ground truth over LLM output" but the specific rule (use shell tools for code extraction) is distinct enough to stand alone. Nick decides.

## Skill Extension Proposal

### headless-subprocess-dispatch-procedure

**Form:** skill
**Existing artifact (primary match):** [[build-loop-skill-autonomous-phase-driver]]
**Codifier recommendation:** extend existing
**Why this match:** Both describe dispatching headless subprocess invocations with fresh, isolated context windows. Build Loop's core invariant is exactly "each phase dispatches as a fresh headless session — no context inherited," which is the defining mechanic of this candidate.
**Diff sketch:** Review whether `orchestrator-headless-dispatch-context-isolation`'s specific isolation techniques (per-subagent MCP scoping, explicit context boundary) add value beyond what Build Loop already captures. If so, parameterize as a context-isolation mode variant.

## Summary

| Recommendation | Count |
|---|---|
| extend existing | 7 |
| create new (false positive) | 3 |
| parameterize as mode variant | 1 |

**Next:** Nick rules per proposal. For "extend existing" — apply the diff sketch manually or await future skill-mode. For "create new" — re-route to drafting as new artifact. For "parameterize" — design the mode variant.
