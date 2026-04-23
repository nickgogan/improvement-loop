---
name: Specification-as-Governance — Fourth Enforcement Philosophy
summary: 'Beyond structural, psychological, and economic enforcement, a fourth governance philosophy encodes rules as executable specifications: conformance test suites that implementations must pass (LangGraph)
  and spec-driven development skills that enforce bidirectional sync between specs and code (n8n). Governance by contract — compliance is verified, not just instructed.'
implementation_notes: 'MetaSystem already has Design Decisions and Build Specs that serve a similar intent — but without automated bidirectional enforcement. The gap is: DDs are read by agents as soft constraints,
  not verified as conformance tests. n8n''s spec-driven development pattern is the most directly applicable — specs as living documents with bidirectional sync.'
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- General
adopted_in: []
sources: []
related_findings:
- file: structural-vs-psychological-vs-economic-governance.md
  rel: extends
- file: rationalization-prevention-pattern.md
  rel: same-problem
- file: superpowers-plugin-spec-driven-sub-agent-orchestra.md
  rel: extends
- file: declared-transformations-contract-conformance.md
  rel: extended-by
proposals: []
date_discovered: '2026-04-09'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---

## What It Is

A fourth governance enforcement philosophy, distinct from the three previously identified in cross-repo analysis:

1. **Structural** (GSD, BMAD, OpenClaw, Archon, n8n) — tool allowlists, validator rules, CI boundaries, SDK contracts
2. **Psychological** (Superpowers) — persuasion engineering, rationalization prevention
3. **Economic** (Paperclip) — budget hard-stops, atomic checkout exclusion
4. **Specification-based** (LangGraph, n8n) — conformance tests, spec-driven development

The specification-based approach encodes governance as executable contracts rather than instructions, persuasion, or resource limits. Two concrete implementations:

**LangGraph's conformance test suite:** `libs/checkpoint-conformance/` defines a test suite that any checkpoint implementation must pass. The interface owns the tests, not the implementation. This inverts the typical relationship — instead of each module defining its own tests, the specification defines what compliance means and implementations prove it.

**n8n's spec-driven development skill:** `.claude/specs/` files serve as living architectural decisions. The skill enforces bidirectional sync between specs and implementation code. Core loop: read spec → implement → verify alignment → update spec or code. TODO checkboxes track completion, with strikethrough+annotation for deliberately skipped items. Specs are the source of truth, not the code.

## Why It Matters

The first three governance philosophies all have the same weakness: they can be bypassed or eroded without detection. Structural rules can be worked around. Psychological guardrails can be rationalized away. Economic limits can be gamed by underestimating effort.

Specification-based governance is different: compliance is **verified**, not just instructed. A conformance test either passes or fails — there's no "rationalize your way past the test suite." Spec-driven development creates a continuous alignment check, not a one-time gate.

This is particularly relevant for agentic systems where:
- Agent behavior drifts across sessions (no memory of prior governance instructions)
- Constraints expressed as prose are subject to interpretation
- Automated verification scales better than human review

## Why People Are Using It

Observed in [LangGraph](https://github.com/langchain-ai/langgraph) v1.1.6 and [n8n](https://github.com/n8n-io/n8n) v2.16.0 — see [[langgraph-analysis]] and [[n8n-analysis]] for structural details.

LangGraph's conformance suite is used by all checkpoint implementations (Postgres, SQLite, Memory). n8n's spec-driven development is an active Claude Code skill used by the n8n engineering team.

## Potential Alternatives

- **Structural enforcement** — tool restrictions, CI gates. Effective but coarse-grained.
- **Psychological enforcement** — persuasion engineering. Creative but not verifiable.
- **Economic enforcement** — budget limits. Effective for resource governance but doesn't cover behavioral compliance.

## Potential Improvements

Combining specification-based governance with the other three philosophies would create a layered defense:
- Specs define what compliance means (specification)
- Tool restrictions prevent obvious violations (structural)
- Rationalization prevention catches agent drift (psychological)
- Resource limits cap total cost (economic)

No repo currently uses all four.

## Potential Failure Modes

- **Spec maintenance burden**: Specs that drift from reality become governance theater — the spec passes but doesn't reflect actual behavior
- **Over-specification**: Too-detailed specs become brittle and resist legitimate evolution
- **False confidence**: Passing a conformance test doesn't guarantee correctness — only conformance to what the test checks
- **Applicability scope**: Works best for interface contracts and architectural decisions; less applicable to behavioral or stylistic governance
