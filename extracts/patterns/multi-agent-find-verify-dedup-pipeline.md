---
title: "Multi-Agent Find-Verify-Dedup Pipeline"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "ultra-review-multi-agent-bug-hunting-fleet"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "A corpus exists that is too large or complex for a single agent pass to find all issues. Multiple independent sub-agents can be spawned with different starting positions or perspectives."
  invariants: "Every candidate finding passes through an independent verification step before being reported. The verifier operates in a separate context from the finder. Duplicate findings are merged before final output."
  governance: "Fleet size is configurable and documented. Verification criteria are explicit (not 'looks reasonable'). False positive rate is tracked across runs."
  recovery: "If verification is too aggressive (high false negative rate), loosen verification criteria and re-verify rejected candidates. If dedup merges distinct issues, split them and re-verify independently."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Multi-Agent Find-Verify-Dedup Pipeline

**Source:** [[ultra-review-multi-agent-bug-hunting-fleet]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Multi-agent review systems that dispatch parallel sub-agents to find bugs, issues, or anomalies produce high volumes of candidates -- but without a verification step, a large fraction are false positives. Developers waste time triaging noise. Meanwhile, different sub-agents often find the same issue from different angles, producing duplicates that inflate the apparent issue count. The raw output of a multi-agent find operation is not trustworthy without post-processing.

## Forces

- **Coverage vs. precision:** More sub-agents find more real issues but also produce more false positives. Single-agent review has fewer false positives but misses issues that require different traversal paths to discover.
- **Context isolation vs. confirmation bias:** A verifier that shares context with the finder inherits the finder's reasoning and is biased toward confirmation. An independent verifier is more objective but may lack context needed to evaluate the finding.
- **Thoroughness vs. cost:** Verification and deduplication add compute time and token cost on top of the initial find pass. Skipping them is cheaper but produces unreliable results.
- **Diversity of perspective vs. coordination overhead:** Sub-agents starting from different codebase positions find different issues, but coordinating their outputs (dedup, conflict resolution) adds complexity.

## Solution

Structure multi-agent review as a four-stage pipeline where the verification stage is the critical innovation that separates this from naive parallel dispatch.

**Stage 1: Setup**
Define the review scope (PR, branch, file set). Configure fleet size (default 5, max 20). Assign each sub-agent a different starting position or persona (e.g., security-focused, performance-focused, correctness-focused) to maximize traversal diversity.

**Stage 2: Find**
Each sub-agent independently scans the scoped codebase, following different paths through the code. Sub-agents operate in isolated contexts -- they do not see each other's findings. This diversity of context ordering reveals issues that any single traversal might miss. Expect high candidate volume (e.g., 47-64 candidates from an 11,000-line PR).

**Stage 3: Verify**
An independent verifier sub-agent evaluates each candidate finding. The verifier:
- Operates in a fresh context, not the finder's context (prevents confirmation bias).
- Holds multiple relevant files in context simultaneously (catches cross-file issues like race conditions).
- Issues a binary verdict: confirmed or refuted. No "maybe" or "probably."
- Records the reasoning for each verdict.

This stage is the key differentiator. Without it, multi-agent find is just "more noise, faster."

**Stage 4: Dedup**
Merge findings where multiple sub-agents discovered the same issue from different angles. Group by affected code location and failure mode, not by description text. Retain the richest description from the merged set.

## Consequences

**Positive:**
- Dramatically reduces false positives compared to unverified multi-agent review.
- Catches cross-file issues (race conditions, lifecycle bugs) that single-agent review misses because the verifier holds multiple files in context.
- Dedup produces a clean, actionable issue list rather than an inflated count.
- Persona-based sub-agent assignment increases coverage diversity.

**Negative:**
- 3-5x more expensive than single-agent review (multiple finders + verifier + dedup).
- Slower than single-agent review (10-20 minutes vs. 3-4 minutes in the documented case).
- Verification may be too aggressive, rejecting subtle real issues as false positives.
- Dedup may incorrectly merge distinct-but-similar issues.

## Known Uses

- Claude Code's Ultra Review feature (codename "Bug Hunter") implements this exact four-stage pipeline. In testing on an 11,000-line PR, the find stage produced 47-64 candidates; the verify stage refuted many of them. The feature runs on Anthropic's cloud infrastructure with 5-20 sub-agents.
- The pattern generalizes beyond bug hunting to any multi-agent finding operation: security audits, compliance checks, documentation gap analysis.

## Contract

### Preconditions
A corpus (codebase, document set, configuration) exists that is too large or complex for a single-agent pass to reliably find all issues. The infrastructure supports spawning multiple independent sub-agents with isolated contexts.

### Invariants
Every candidate finding passes through an independent verification step before being reported to the user. The verifier operates in a separate context from the finder that produced the candidate. Duplicate findings are merged before the final output is presented. Verification verdicts are binary (confirmed/refuted) with recorded reasoning.

### Governance
Fleet size is configurable and documented with rationale. Verification criteria are explicit and auditable. False positive rate and false negative rate are tracked across runs to calibrate verification aggressiveness. Persona assignments (if used) are documented.

### Recovery
If verification is too aggressive (high false negative rate, real issues being rejected), loosen verification criteria and re-verify the rejected candidate set. If dedup incorrectly merges distinct issues, split them and re-verify each independently. If the overall pipeline cost is too high for the use case, reduce fleet size or switch to single-agent review with spot-check verification.
