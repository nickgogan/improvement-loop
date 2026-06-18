---
title: "Untyped Links as Token Waste — Typed Edges Required"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "untyped-links-as-token-waste-anti-pattern"
extraction_date: "2026-05-25"
last_change_session: 96
last_change_sl: "session-96-codifier-extract-non-pattern-artifacts"
identification_report: "2026-05-25-identification-report-session-95.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "knowledge bases designed for AI agent traversal (markdown vaults, graph databases, structured wikis)"
    - "any system where an LLM navigates between linked documents and must determine relationship semantics"
    - "teams building retrieval layers where link traversal consumes tokens proportional to documents loaded"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "medium — retroactive typing of existing links requires reading both endpoints to classify; new links are trivially typed at creation time"
  auditability: "high — compliance is verifiable by scanning all links in the KB and checking for the presence of a type annotation"
  evidence_strength: "Medium"
  adoption:
    status: "Partially Adopted"
    notes: "MetaSystem's IL KB uses typed relationships (enables, contradicts, extends, same-problem) on research findings. Obsidian wiki-links elsewhere in the workspace remain untyped."
contract:
  preconditions: "A knowledge base exists with inter-document links that will be traversed by an AI agent. The KB has a defined vocabulary of relationship types appropriate to its domain. The link-creation mechanism (editor, script, agent) supports annotating links with type metadata."
  invariants: "Every link between documents in the AI-traversed KB carries a relationship type from the defined vocabulary. The type is stored at the link site (not derived at read time). The vocabulary is bounded (recommended: 4-12 types) and each type has a clear semantic definition. Agents can filter traversals by type without loading linked documents."
  governance: "Owner: the KB maintainer or team responsible for the knowledge architecture. The relationship vocabulary is defined once and versioned; additions require review. Agents creating links must select from the vocabulary — a catch-all type (e.g., 'related-to') exists for genuinely ambiguous cases but its usage rate is monitored."
  recovery: "If an untyped link is discovered: classify it by reading both endpoints to determine the relationship, then annotate. If the vocabulary proves insufficient (frequent use of catch-all): evaluate whether a new type is needed or whether the catch-all cases are genuinely ambiguous. If a link is mis-typed: correct the type; mis-typing is worse than no type because agents trust the annotation."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
  - "token-efficiency"
---

# Untyped Links as Token Waste — Typed Edges Required

**Source:** [[untyped-links-as-token-waste-anti-pattern]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

A link is being created between two documents in a knowledge base that will be traversed by an AI agent. The link connects document A to document B without specifying the nature of the relationship.

## Action

**Required:** Annotate the link with a relationship type from the KB's defined vocabulary at creation time. The type must be semantically meaningful (e.g., enables, contradicts, extends, depends-on, same-problem) — not merely "linked."

**Forbidden:** Creating links between documents in AI-traversed knowledge bases without a relationship type. Deferring type assignment to "later" (untyped links accumulate; retroactive typing is expensive). Using only a generic "related" type for all links (defeats the purpose of typing).

## Boundary

Enforced at link-creation time — whether the link is created by a human in an editor, by an agent during extraction, or by a script during migration. The check is: does this link carry a type from the vocabulary?

## Enforcement

Deterministic check: scan link syntax for type annotation. For markdown-based KBs with YAML frontmatter links, verify the `rel:` field is present and contains a value from the vocabulary enum. For wiki-link-based KBs, verify the link includes type metadata in whatever format the KB uses.

## Rationale

Untyped links force agents into exhaustive document loading — the agent must read both endpoints to determine whether the relationship is supportive, contradictory, prerequisite, or merely tangential. Typed links enable pruned traversal: an agent investigating contradictions can skip "enables" links without loading the target documents. Practitioner measurement shows 15x token reduction when comparing untyped PARA-style links to typed graph edges on the same data and query.
