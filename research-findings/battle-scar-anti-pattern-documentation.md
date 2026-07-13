---
name: Battle-Scar Anti-Pattern Documentation
summary: "Governance rules that cite specific git commit SHAs as evidence of historical failure — 'battle scars' that make the cost of violating each rule auditable. Creates a direct trail from 'don't do X' back to the incident where X caused a production issue."
implementation_notes: null
category: Governance
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - "S3 (Claude Code Build)"
  - General
adopted_in: []
sources: []
proposals: []
date_discovered: "2026-05-25"
last_updated: "2026-07-13"
related_findings:
  - file: immutable-system-log-with-append-only-entries.md
    rel: same-problem
  - file: controller-deauthorization-reviewer-independence.md
    rel: same-problem
  - file: pr-review-mined-rules-corpus-with-provenance.md
    rel: same-problem
pipeline_status: raw
consumed_by: []
---

# Battle-Scar Anti-Pattern Documentation

## What It Is

An ANTI-PATTERNS.md file where every "don't do X" rule links to the specific git commit SHA that introduced the failure being guarded against. Rules are grouped by category (backwards-incompatible changes, testing discipline, workflow discipline, dependency management, fictional data) with 15 total entries. Each entry follows a don't/do format — the anti-pattern with its commit evidence, then the correct approach.

## Why It Matters

Rules without evidence degrade into cargo-cult conventions that developers ignore or cargo-cult follow without understanding. Citing the exact commit makes the cost of each rule auditable — anyone can verify that the rule exists for a real reason by inspecting the referenced commit, and the rule earns credibility by proving it was born from actual production pain rather than theoretical caution.

## Why People Are Using It

Observed in [Langflow](https://github.com/langflow-ai/langflow) v1.9.3 — see [[langflow-analysis]] for structural details. Langflow's `docs/agents/ANTI-PATTERNS.md` documents 15 rules across 5 categories, each citing specific commit SHAs as evidence. AI coding agents are directed to read this file before claiming any task is done.

## Potential Alternatives

Inline code comments referencing the issue tracker. ADR (Architecture Decision Record) format with "context" sections that explain what went wrong. Git blame combined with commit message conventions that explain "why not" in the original fix commit.

## Potential Improvements

Automate link freshness — if a cited commit is reverted or the guarded code path is deleted, flag the rule for review. Add severity/blast-radius metadata so agents can prioritize which anti-patterns to check first. Include a "last validated" date to distinguish ancient rules that may no longer apply from recent hard-won lessons.

## Potential Failure Modes

SHA references become stale if the repo is rebased or squash-merged — the original commit disappears from history. Without periodic review, the file accumulates rules for codepaths that no longer exist. Over-reliance on historical incidents can miss novel failure modes — teams may feel safe because "we have anti-patterns documented" while new classes of error go unguarded.
