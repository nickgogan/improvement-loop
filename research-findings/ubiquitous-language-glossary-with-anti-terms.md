---
name: "Ubiquitous-Language Glossary with Explicit Anti-Terms"
summary: |-
  opencode's CONTEXT.md defines ~30 domain terms for its v2 session runtime, each carrying an
  explicit "_Avoid_:" list of near-synonyms not to use ("System Context", not "system prompt";
  "Context Epoch", not "compaction snapshot"), plus ~110 relationship invariants between the
  terms. The anti-terms are the novel part: they pin vocabulary for LLM agents and humans
  simultaneously during a rewrite, where drift into casual synonyms quietly re-introduces the
  old model's assumptions. For us — a vault whose vocabulary.md serves the same convergence
  goal — the transferable move is stating what NOT to call a thing, per term, right where the
  term is defined.
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
---

## What It Is

A DDD-style ubiquitous-language document (`CONTEXT.md`, 32k) written for agents and humans working on opencode's v2 session-runtime rewrite. Roughly 30 glossary terms are each defined with an explicit `_Avoid_:` line listing the near-synonyms that must not be used — "System Context", not "system prompt"; "Context Epoch"; "Session Drain" — and the terms are bound together by ~110 relationship invariants ("a Session Drain is process-local", "context changes are admitted only at Safe Provider-Turn Boundaries"). The document also carries an example dev/domain-expert dialogue and flagged ambiguities. Distilled invariants graduate from CONTEXT.md into the auto-loaded AGENTS.md ("V2 Session Core" section), so the deep document is referenced on demand while its hardest rules ride in always-on context.

## Why It Matters

Vocabulary drift is a real defect channel when LLM agents write code and docs: the model reaches for the ecosystem-common term ("system prompt"), and the common term carries the old architecture's semantics, quietly re-importing assumptions the rewrite exists to kill. A positive glossary alone does not stop this — the model happily uses both the blessed term and its synonym. The per-term anti-term list is what makes the glossary enforceable in review and followable by an agent: for each concept there is exactly one name, and the tempting wrong names are enumerated where the right one is defined. Bounded negative space (a short avoid-list per term) rather than an open-ended banned-words list.

## Why People Are Using It

Observed in [opencode](https://github.com/anomalyco/opencode) dev branch (`34e5809`, 2026-07-11) — see [[opencode-analysis]] for structural details. The engine's own `knowledge/reference/vocabulary.md` pursues the same human/agent terminology convergence — hence Partially Adopted; per-term anti-terms and relationship invariants are the parts we lack.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Positive-only glossary | Terms and definitions, no avoid-lists | Stable domains where no competing vocabulary exists to drift into |
| Linter-enforced terminology | CI greps for banned terms in code/docs | Terms with low false-positive collision risk |
| Naming in code review | Humans police vocabulary | Small teams, low agent involvement |

## Potential Improvements

- Pair the glossary with a translation-time check for agent-authored artifacts (the same role opencode's locale glossaries play for docs translation)
- Record *why* each anti-term is wrong — the imported assumption — so the rule survives its author

## Potential Failure Modes

- **Glossary staleness:** once the rewrite ships, invariant lists rot unless ownership continues
- **Anti-term sprawl:** avoid-lists that grow unboundedly become their own maintenance tax; keep them to the genuinely tempting synonyms
- **Shadowed loading:** opencode's own first-filename-wins chain means CONTEXT.md is not auto-loaded — a glossary nobody loads converges nothing
