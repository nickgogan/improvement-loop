---
title: "Default to File Search Before RAG"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "file-search-outperforms-rag-for-small-corpora"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agents and workflows that access knowledge bases, document stores, or codebases via retrieval"
    - "KB architecture decisions for any agent system under ~1000 documents"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "low — switching from file search to RAG requires adding vector DB infrastructure and embedding pipelines; reversing is infrastructure removal"
  auditability: "high — retrieval mechanism is explicit in agent tooling (grep/glob vs. vector DB client); auditable at build time"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Partially Adopted"
    notes: "Claude Code and Cursor adopted file-search-only architectures in 2025. LlamaIndex published a study confirming file search outperforms RAG for small corpora. MetaSystem IL knowledge base already uses file-based navigation, validating current state."
contract:
  preconditions: "An agent system is being designed or audited that requires external knowledge retrieval. The corpus size is known or estimable. File search tooling (grep, glob, file traversal) is available in the agent SDK or runtime."
  invariants: "For knowledge bases below the scale threshold (~100–1000 documents, to be benchmarked per system), file search is the default retrieval mechanism. Semantic search (vector DB, embeddings) is introduced only when the corpus exceeds the threshold or when lexical mismatch is documented as a retrieval failure mode. Both conditions must be evaluated before RAG infrastructure is added."
  governance: "Owner of any agent specification that includes a retrieval step. The spec must state which retrieval mechanism is used and justify it against this rule if RAG is chosen for a small corpus. KB architecture audits flag vector DBs serving fewer than 100 documents as requiring justification."
  recovery: "If retrieval quality degrades as corpus grows → benchmark file search latency and accuracy against a RAG baseline at current scale before migrating. If lexical mismatch causes false negatives (conceptually related content not found) → document the gap as a named failure mode; this is a valid trigger for hybrid retrieval. If grep-heavy search becomes slow → introduce caching or indexing before adding RAG complexity."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
  - "retrieval"
  - "kb-architecture"
---

# Default to File Search Before RAG

**Source:** [[file-search-outperforms-rag-for-small-corpora]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent system design or architecture audit includes a retrieval step where the agent accesses an external knowledge base, document store, or codebase. The designer is deciding between file search tooling (grep, glob, directory traversal) and semantic search infrastructure (vector databases, embedding pipelines, RAG).

Scope: applies at design time (spec-before-build) and at audit time (reviewing existing architectures). Does not govern retrieval decisions made at agent runtime based on query characteristics.

## Action

**Default to file search.** Use grep, glob, and file-traversal tools as the retrieval mechanism. Do not introduce vector databases, embedding pipelines, or semantic search infrastructure unless one of two conditions is explicitly met:

1. **Scale threshold:** Corpus size exceeds the scale threshold for the system (baseline: ~100–1000 documents; benchmark per system to confirm).
2. **Lexical mismatch:** Documented retrieval failure mode where conceptually related content is not found because it does not share lexical terms with queries.

**Forbidden:** Adding RAG infrastructure as a default or precaution for small corpora. Adding semantic search because it is perceived as more sophisticated. Migrating from file search to RAG without benchmarking file search accuracy and latency at current scale.

## Boundary

Applies to the retrieval-mechanism decision in agent system specifications and architecture audits. Does not apply at query routing time (runtime decisions about which tool to use for a given query). Does not apply when the corpus size is already above the scale threshold.

## Enforcement

- **Mechanism:** Architecture audit checklist item — any agent specification with a retrieval step must explicitly state its retrieval mechanism and, if RAG is chosen, document which condition triggered the departure from the file-search default.
- **Check (deterministic):** `(corpus_size < threshold AND no lexical_mismatch_documented) → retrieval_mechanism == file_search`. If this condition is violated, the spec requires justification.
- **Violation response:**
  - RAG for small corpus without justification → request justification or replace with file search.
  - Scale threshold exceeded without migration → treat as an optimization gap, not a violation; flag for next architecture review.
  - Lexical mismatch claimed without evidence → treat as insufficient justification; require documented retrieval failures before approving RAG.
- **Audit tooling:** KB architecture audits flag vector DBs serving fewer than 100 documents as requiring written justification.

## Rationale

In 2024, RAG was the default retrieval mechanism for AI agents. In 2025, the coding agent ecosystem (Claude Code, Cursor) demonstrated that file search tools outperform vector databases for small corpora: exact text matching beats approximate vector similarity when the corpus is small enough for exhaustive search to be fast. LlamaIndex published a study confirming this reversal.

The mechanism is straightforward: embedding-based retrieval introduces lossy compression at the chunking and embedding stage. For small document sets, this compression loses more signal than it saves in compute. File search preserves full fidelity at zero infrastructure cost.

The threshold is real. For corpora with thousands of documents, exhaustive grep-scan costs exceed vector similarity lookups, and semantic search's ability to find conceptually related content (not just lexically matched) becomes the dominant factor.

The default-first framing matters: start simple, migrate when evidence demands it. Adding RAG infrastructure speculatively creates maintenance burden (embedding model upgrades, re-indexing, chunking strategy tuning) for no accuracy gain at small scale.

## Failure Modes

- **Scaling past threshold without migration.** Corpus grows silently; file search latency and false-negative rate degrade. Mitigation: define the scale threshold explicitly in the spec; monitor corpus size.
- **Lexical mismatch false negatives.** File search misses conceptually related content. Mitigation: this is a documented trigger condition for introducing hybrid or semantic search — not an argument against file search as the default.
- **"RAG is dead" over-interpretation.** Removing semantic capabilities from agents that will eventually need them. Mitigation: treat this as a default rule, not an architectural prohibition.
- **Grep-heavy patterns on large file systems.** Exhaustive search becomes expensive before the corpus threshold is reached. Mitigation: add indexing or caching rather than RAG; RAG is the last resort.

## Contract

### Preconditions
An agent system is being designed or audited that requires external knowledge retrieval. The corpus size is known or estimable. File search tooling (grep, glob, file traversal) is available in the agent SDK or runtime.

### Invariants
For knowledge bases below the scale threshold (~100–1000 documents, to be benchmarked per system), file search is the default retrieval mechanism. Semantic search is introduced only when the corpus exceeds the threshold or when lexical mismatch is documented as a retrieval failure mode. Both conditions must be evaluated before RAG infrastructure is added.

### Governance
Owner of any agent specification that includes a retrieval step. The spec must state which retrieval mechanism is used and justify it against this rule if RAG is chosen for a small corpus. KB architecture audits flag vector DBs serving fewer than 100 documents as requiring justification.

### Recovery
If retrieval quality degrades as corpus grows → benchmark file search latency and accuracy against a RAG baseline at current scale before migrating. If lexical mismatch causes false negatives → document the gap as a named failure mode; this is a valid trigger for hybrid retrieval. If grep-heavy search becomes slow → introduce caching or indexing before adding RAG complexity.
