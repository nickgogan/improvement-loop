---
name: 'Verification Agent: Seven Prompt Patterns for Adversarial Code Review'
summary: 'Seven distinct patterns from Claude Code''s unreleased verification agent: (1) adversarial framing, (2) read-only permissions, (3) structured logging, (4) edge-case test prerequisites, (5) independent
  test generation, (6) binary pass/fail criteria, (7) anti-skip prompting.'
implementation_notes: Implement as a sub-agent pattern. Binary criteria eliminates vibe-based verification. Independent test generation addresses LLM self-assessment bias.
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in:
- S3 (Claude Code Build)
sources:
- claude-codes-leak-changes-everything.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
related_findings:
- file: ace-execution-feedback-no-labels-required.md
  rel: same-problem
- file: builder-validator-chain-pattern.md
  rel: same-problem
- file: cross-model-verification-for-bug-finding.md
  rel: same-problem
pipeline_status: "synthesized"
consumed_by:
  - "building-agent-evaluation-suites.md"
---

## What It Is

Seven prompt engineering patterns extracted from Claude Code's codebase (feature-flagged, not yet live) that define a verification sub-agent for adversarial code review:

1. **Adversarial framing** — the agent's explicit job is to try to break code, not confirm it works
2. **Read-only permissions** — the verification agent cannot edit, write, or create files
3. **Structured logging** — all verification steps are logged in a consistent format
4. **Edge-case test prerequisites** — tests must cover concurrency, boundary values, idempotency, and orphan operations
5. **Independent test generation** — tests are written by the verifier, not the builder agent
6. **Binary pass/fail criteria** — no partial credit except for environment limitations
7. **Anti-skip prompting** — explicit instructions prevent the agent from declaring "looks good" without running tests

## Why It Matters

LLMs are notoriously poor at self-assessment. A builder agent asked to verify its own work will almost always declare success. These seven patterns address this fundamental limitation by separating the builder and verifier roles, making verification adversarial rather than confirmatory, and eliminating subjective quality assessments.

The transcript emphasizes that pattern #6 (binary pass/fail) is "by far the most important" because it forces the agent to choose a side rather than "going on vibes" -- it eliminates room for hallucinations, bloviating, or guessing. The "partial" verdict exists only for genuine environmental limitations (e.g., a test environment is unavailable), not for ambiguous quality assessments. Pattern #7 (anti-skip) targets a specific LLM failure mode where models "get lazy and decide to skip things," making it an explicit countermeasure rather than general guidance.

## Why People Are Using It

The pattern directly addresses the most common failure mode in AI-assisted development: code that "works" in the happy path but fails under real-world conditions. Binary pass/fail eliminates the vibe-based "looks good to me" that plagues both human and AI code review.

## Potential Improvements

- Implement as a dedicated sub-agent with its own system prompt and tool permissions
- Generate tests independently from the builder agent's context to avoid confirmation bias
- Log all verification steps for post-session audit
- Apply the pattern beyond code review to specification validation and governance checks

## Potential Failure Modes

- **Environment limitations masking real failures:** The "except for environment limitations" escape hatch in binary criteria could be exploited by the model to avoid reporting failures
- **Token cost:** Running a full adversarial verification agent doubles the token cost of every build step
- **Test quality ceiling:** The verifier's tests are only as good as the model's understanding of edge cases — it may miss domain-specific failure modes
- **Anti-skip circumvention:** Models may learn to generate minimal tests that technically satisfy the "must run tests" requirement without meaningfully verifying behavior

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[adversarial-verification-agent-prompt-patterns.md]] in `extracts/patterns/`
