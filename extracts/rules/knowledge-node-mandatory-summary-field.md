---
title: "Knowledge Node Mandatory Summary Field"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "summary-gate-agent-traversal-pattern"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "knowledge base schemas where agents navigate or retrieve documents"
    - "frontmatter schema for any document store an agent traverses"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — adding a required frontmatter field is a schema amendment; backfilling existing documents is a one-time migration"
  auditability: "high — frontmatter validation can check for presence and length of summary field at lint or pre-commit time"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Partially Adopted"
    notes: "IL research findings already carry a summary frontmatter field, validating the current design. The rule formalizes what is currently an informal convention and adds the one-sentence constraint and agent-triage writing guidance."
contract:
  preconditions: "A knowledge base schema is being defined or audited. Agents are expected to navigate or retrieve documents from this store. The schema has a frontmatter or metadata layer where fields are declared."
  invariants: "Every knowledge node in an agent-navigable document store has a summary field containing exactly one sentence (≤1 sentence, ≤50 tokens). The summary must be written to maximize agent triage utility: it answers 'is this document relevant to the current query?' rather than describing structure. Summary is updated whenever the document body changes materially."
  governance: "Schema owner for any agent-navigable document store. The summary field must be declared as required in the schema. Frontmatter validation checks: (a) field presence, (b) sentence count ≤1, (c) token length ≤50. Backfill required when rule is adopted for an existing corpus."
  recovery: "If summary is absent → document is treated as unindexed; agent cannot triage it without loading full content. If summary is stale (body changed, summary not updated) → agent may skip a relevant document (false negative) or load an irrelevant one (false positive); trigger a summary audit. If summary is too long → truncate to one discriminating sentence; remove structural descriptions ('This document covers...') in favor of substantive content ('X differs from Y because Z')."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
  - "kb-schema"
  - "agent-navigation"
---

# Knowledge Node Mandatory Summary Field

**Source:** [[summary-gate-agent-traversal-pattern]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

A knowledge base schema is being defined, or an existing schema is being audited, for a document store where agents navigate or retrieve documents. The schema has a frontmatter or metadata layer. Agents are expected to decide which documents to load based on metadata before reading full content.

Scope: applies to any document store an agent traverses, including research KBs, skill registries, tool catalogs, and file-system knowledge bases. Does not apply to transient working documents that agents produce and consume within a single session.

## Action

**Required:** Every knowledge node in an agent-navigable document store must carry a `summary` frontmatter field. The summary must satisfy three constraints:

1. **Length:** One sentence, ≤50 tokens.
2. **Content:** Answers "is this document relevant to the current query?" — substantive, discriminating. Not structural ("This document covers X") but comparative ("X differs from Y because Z" or "X is the approach when Y is true").
3. **Currency:** Updated whenever the document body changes materially.

**Forbidden:** Omitting the summary field on documents in an agent-navigable store. Writing summaries that describe document structure rather than document content. Allowing summaries to drift from body content without a correction mechanism.

## Boundary

Enforced at schema definition time and at schema audit time. Applies to the document schema itself (declaring summary as required) and to individual documents at write/update time. Does not govern how agents use summaries at runtime — that is the summary-gate traversal pattern, of which this rule is the prerequisite.

## Enforcement

- **Mechanism:** Frontmatter validation script or pre-commit hook that checks every document in the store for (a) presence of `summary` field, (b) sentence count ≤1, (c) approximate token length ≤50.
- **Check (deterministic):** `summary_present AND sentence_count(summary) == 1 AND token_count(summary) <= 50`.
- **Violation response:**
  - Missing summary → document is flagged as unindexed; agent KB audit surfaces it as a gap.
  - Summary too long → truncate to one discriminating sentence.
  - Summary structurally vague → rewrite to answer "is this relevant?" for a typical query.
  - Summary stale after body change → trigger summary audit for the affected document.
- **Backfill:** When rule is adopted for an existing corpus, all documents without a compliant summary field are backfilled before the rule is enforced. Backfill is a one-time migration.

## Rationale

An agent navigating a knowledge base without summaries faces a binary choice per document: load everything (expensive — hundreds to thousands of tokens per document) or skip (risks missing relevant content). The summary gate creates a cheap intermediate decision: read one sentence (~50 tokens) and decide whether to load the full document (~500+ tokens).

The practitioner evidence: combining summary-gate traversal with typed edges reduced token consumption from ~9,000 to ~600 for equivalent queries — a ~93% reduction. The summary is the filtering layer that makes this possible.

The one-sentence constraint is not cosmetic. A two-sentence summary doubles the scan cost across a large corpus. The triage-optimized writing guidance addresses a failure mode unique to agent consumers: summaries written for human readers often describe document structure ("This section covers X, Y, Z"), which gives the agent no signal about relevance. Summaries written for agent triage answer the relevance question directly.

For MetaSystem: IL research findings already carry a `summary` frontmatter field. This rule formalizes that convention, adds the ≤50-token constraint, and establishes the triage-optimized writing expectation.

## Failure Modes

- **Summary drift.** Body changes; summary is not updated. Agent skips a now-relevant document (false negative) or loads a now-irrelevant one (false positive). Mitigation: summary currency is an invariant; update summaries on every material body change.
- **Summary quality variance.** Some nodes have crisp discriminating summaries; others have vague structural descriptions. Inconsistency degrades the pattern's reliability across the corpus. Mitigation: enforce triage-optimized writing guidance at write time; retroactively rewrite vague summaries during audits.
- **False negatives from lexical gaps.** Agent may skip a relevant document because the summary does not mention the aspect the query targets. Mitigation: this is a known limitation of one-sentence summaries; for high-stakes retrieval, supplement with typed edges or secondary index.
- **Overhead for small KBs.** For stores under ~50 nodes, reading all summaries may cost more tokens than loading all documents. Mitigation: the rule applies to schemas with agent-navigable intent; for trivially small stores, the overhead is negligible and the schema consistency benefit remains.

## Contract

### Preconditions
A knowledge base schema is being defined or audited. Agents are expected to navigate or retrieve documents from this store. The schema has a frontmatter or metadata layer where fields are declared.

### Invariants
Every knowledge node in an agent-navigable document store has a summary field containing exactly one sentence (≤1 sentence, ≤50 tokens). The summary is written to maximize agent triage utility and updated whenever the document body changes materially.

### Governance
Schema owner for any agent-navigable document store. The summary field must be declared as required in the schema. Frontmatter validation checks presence, sentence count, and token length. Backfill required when rule is adopted for an existing corpus.

### Recovery
If summary is absent → document is treated as unindexed; agent KB audit surfaces it as a gap. If summary is stale → trigger a summary audit. If summary is too long or structurally vague → rewrite to one discriminating sentence that answers relevance for a typical query.
