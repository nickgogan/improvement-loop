---
title: "Adversarial Verification Agent Prompt Patterns"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "verification-agent-seven-prompt-patterns"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "A builder agent has produced an artifact (code, config, document) that requires verification. A separate verification agent can be instantiated with its own system prompt and tool permissions."
  invariants: "The verifier is adversarial -- its job is to break, not confirm. The verifier cannot edit the artifact under review. All verdicts are binary pass/fail with no partial credit except genuine environment limitations. The verifier generates its own tests independently from the builder."
  governance: "Verification prompt patterns are versioned and auditable. The 'environment limitation' escape hatch is reviewed periodically to prevent misuse. Token cost of verification is tracked against the value of bugs caught."
  recovery: "If the verifier consistently passes artifacts that later fail in production, review and strengthen the edge-case prerequisites and anti-skip prompting. If token cost is prohibitive, apply verification selectively to high-risk changes only."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Adversarial Verification Agent Prompt Patterns

**Source:** [[verification-agent-seven-prompt-patterns]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

LLMs are poor at self-assessment. A builder agent asked to verify its own work will almost always declare success -- it has already "decided" the code is correct during generation and lacks the adversarial stance needed to find flaws. Even when a separate agent is used for verification, without specific prompt engineering the verifier defaults to a confirmatory posture ("looks good to me") rather than genuinely testing for failures. The result is a verification step that consumes tokens without catching bugs.

## Forces

- **Confirmatory bias vs. adversarial stance:** LLMs naturally lean toward agreement and confirmation. Overcoming this requires explicit, forceful framing.
- **Coverage vs. token cost:** Thorough adversarial verification (generating independent tests, running edge cases) doubles the token cost of every build step. Shallow verification is cheap but worthless.
- **Flexibility vs. gaming:** Allowing partial credit or subjective assessments gives the model room to avoid hard verdicts. But removing all flexibility means genuine environmental limitations (test environment unavailable) are reported as failures.
- **Independence vs. context:** The verifier needs enough context to understand the artifact but must not share the builder's reasoning, which would contaminate the verification.

## Solution

Apply seven specific prompt patterns to the verification agent's system prompt. These patterns are complementary and should be used together as a set.

**Pattern 1: Adversarial Framing**
Explicitly state that the agent's job is to try to break the code, not confirm it works. Use language like "Your role is adversarial. You succeed when you find failures, not when you confirm correctness."

**Pattern 2: Read-Only Permissions**
The verification agent cannot edit, write, or create files. It can only read the artifact and run tests. This prevents the verifier from "fixing" issues instead of reporting them, and maintains separation of concerns.

**Pattern 3: Structured Logging**
All verification steps are logged in a consistent format: what was tested, what the expected outcome was, what the actual outcome was, and the verdict. This creates an auditable trail.

**Pattern 4: Edge-Case Test Prerequisites**
Tests must cover four mandatory edge-case categories before a pass verdict can be issued:
- Concurrency (race conditions, deadlocks)
- Boundary values (empty inputs, max values, off-by-one)
- Idempotency (repeated operations produce the same result)
- Orphan operations (cleanup after partial failures)

**Pattern 5: Independent Test Generation**
Tests are written by the verifier, not copied or adapted from the builder's tests. This prevents confirmation bias where the builder's tests only test the happy path the builder had in mind.

**Pattern 6: Binary Pass/Fail Criteria**
This is the most important pattern. The verdict is binary: PASS or FAIL. No partial credit, no "mostly works," no "looks reasonable." The only exception is PARTIAL, which is reserved exclusively for genuine environment limitations (e.g., a required service is unavailable for testing) -- not for ambiguous quality assessments. Binary criteria force the model to commit to a verdict rather than hedging.

**Pattern 7: Anti-Skip Prompting**
Explicit instructions prevent the agent from declaring "looks good" without actually running tests. Target the specific LLM failure mode where models "get lazy and decide to skip things." Example: "You MUST run at least one test for each function under review. Declaring PASS without test execution is a protocol violation."

## Consequences

**Positive:**
- Binary pass/fail eliminates "vibe-based" verification that plagues both human and AI code review.
- Independent test generation catches bugs the builder's tests were designed to miss.
- Edge-case prerequisites ensure coverage of the failure modes most commonly missed by LLMs (concurrency, boundary values).
- Read-only permissions enforce clean separation between building and verifying.
- Anti-skip prompting directly addresses a documented LLM failure mode.

**Negative:**
- Doubles token cost for every verified build step.
- The "environment limitation" escape hatch in Pattern 6 can be gamed by the model to avoid reporting real failures.
- The verifier's test quality is bounded by the model's understanding of edge cases -- domain-specific failure modes may be missed.
- Anti-skip prompting may lead to minimal, check-the-box tests that technically satisfy the requirement without meaningful verification.

## Known Uses

- Claude Code's unreleased verification agent (feature-flagged, codename "Bug Hunter") implements all seven patterns in its system prompt, as discovered through binary analysis of the Claude Code codebase.
- The pattern set generalizes beyond code review to specification validation, governance compliance checks, and any scenario where a builder-verifier separation is needed.

## Contract

### Preconditions
A builder agent has produced an artifact (code, configuration, document) that requires independent verification. A separate verification agent can be instantiated with its own system prompt and restricted tool permissions (read-only for the artifact under review).

### Invariants
The verifier's framing is adversarial -- its explicit goal is to find failures. The verifier cannot modify the artifact under review. All verdicts are binary (PASS/FAIL) with PARTIAL reserved exclusively for genuine environment limitations. The verifier generates its own tests independently from the builder's test suite. All verification steps are logged in a structured, auditable format.

### Governance
The seven prompt patterns are versioned and reviewed as a set. The "environment limitation" escape hatch (Pattern 6) is audited periodically to ensure it is not being used to avoid reporting real failures. Token cost of verification is tracked against the value of bugs caught to validate the cost-benefit ratio.

### Recovery
If the verifier consistently passes artifacts that later fail in production, strengthen the edge-case prerequisites (Pattern 4) and anti-skip prompting (Pattern 7) based on the specific failure modes observed. If token cost is prohibitive, apply the full seven-pattern verification selectively to high-risk changes and use a lighter-weight check for low-risk changes. If the "environment limitation" escape hatch is being gamed, remove it and require explicit environment setup as a precondition.
