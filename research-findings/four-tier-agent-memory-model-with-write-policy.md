---
name: Four-Tier Agent Memory Model with Write Policy
summary: 'Production agents need four distinct memory tiers: working (short-lived run state), episodic (task history with provenance), semantic (policy/docs as retrieval), and user (preferences requiring
  consent). Memory writes must be policy-governed: extract candidate -> classify type -> policy check -> attach provenance -> write with TTL/confidence. Never allow unrestricted model-authored long-term
  writes.'
implementation_notes: 'MetaSystem has working memory (PROGRESS.md) and semantic memory (CLAUDE.md, skills). Missing: episodic memory with provenance, user memory with consent, and most critically -- a write
  policy governing what agents can persist and for how long. The existing MEMORY.md is an unstructured append-only store without TTL, confidence scores, or provenance metadata.'
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- ai-agents-in-production-2026-nick-gupta-linkedin.md
related_findings:
- file: agent-memory-architecture-multi-agent-layered.md
  rel: extends
- file: memory-cross-layer-promotion-governance.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: gsd-global-learnings-store-cross-session-persistence.md
  rel: same-problem
- file: ace-agentic-context-engineering-rag-based.md
  rel: extends
- file: memory-cross-layer-promotion-governance.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: gsd-global-learnings-store-cross-session-persistence.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-27'
pipeline_status: synthesized
consumed_by:
- session-persistence-and-memory.md
---

# Four-Tier Agent Memory Model with Write Policy

## What It Is

A structured memory architecture for production agents with four tiers, each with distinct governance requirements:

1. **Working memory:** Short-lived run state, aggressively compacted. Exists only during task execution.
2. **Episodic memory:** Prior task history with full provenance (who did what, when, why). Enables learning from past runs.
3. **Semantic/organizational memory:** Policy documents, codebase knowledge, reference material. Best served through retrieval rather than context stuffing.
4. **User memory:** Preferences and personalization data requiring explicit consent and permission controls.

The critical companion pattern is **memory write policy**: agents cannot write freely to long-term memory. Every write follows: extract candidate memory -> classify type (working/episodic/semantic/user) -> policy check (is this agent authorized to write this type?) -> attach provenance (source, confidence, timestamp) -> write with TTL and confidence score. On read, re-rank using recency + source reliability + user relevance.

Gupta's key insight: "Long context is not memory. A vector store is not automatically memory either." Memory must be a deliberate read/write policy system, not a default persistence layer.

## Why It Matters

Without a write policy, agents pollute long-term memory with unvalidated, low-confidence, or hallucinated information. This creates a compounding reliability problem: future retrievals return polluted data, which produces worse outputs, which get persisted again. Memory pollution is a production failure mode distinct from context rot -- it affects future sessions, not just the current one.

## Why People Are Using It

Nick Gupta documents this as a core production architecture pattern. The four-tier model aligns with existing KB findings on layered agent memory but adds the critical write policy dimension. The pattern draws from database access control (read/write permissions) and data governance (provenance, TTL, classification).

## Potential Improvements

Automatic memory importance scoring based on task outcome (memories from successful tasks get higher confidence). Memory compaction that preserves provenance chains. Cross-agent memory sharing with access control (agent A can read but not write agent B's episodic memory).

## Potential Failure Modes

Overly restrictive write policies that prevent agents from learning. TTL too short causing loss of valuable episodic knowledge. Provenance tracking overhead slowing down fast-path operations. Classification errors routing working memory to long-term storage.
