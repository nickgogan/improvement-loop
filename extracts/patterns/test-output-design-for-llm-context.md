---
title: "Test Output Design for LLM Context Windows"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "test-output-design-for-llm-context"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "A test suite exists that will be consumed by an LLM agent. The agent has a finite context window and no ability to sense elapsed wall-clock time."
  invariants: "Console output never exceeds a defined line budget per test run. Full details are always available in log files. Errors are single-line and greppable."
  governance: "Output format changes require review against the agent's parsing expectations. Fast-mode subsample percentage is documented and adjustable."
  recovery: "If terse output masks a real failure, the agent falls back to reading the full log file. If fast-mode misses a regression, the next full-suite run catches it."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Test Output Design for LLM Context Windows

**Source:** [[test-output-design-for-llm-context]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent-driven development tools run test suites and consume their output as part of a build-verify loop. Standard test output is designed for human developers scrolling a terminal -- verbose, unstructured, and often thousands of lines long. When this output enters an LLM's context window, it consumes the token budget on noise (stack traces, passing test confirmations, framework boilerplate) rather than actionable signal (which tests failed and why). Additionally, agents lack time sense and will run a full test suite for hours without realizing the cost.

## Forces

- **Completeness vs. context budget:** Full test output contains every detail needed for debugging, but overwhelms the agent's context window. Terse output fits in context but may hide information needed for complex failures.
- **Speed vs. coverage:** Running the full test suite guarantees coverage but may take hours. Running a subset is fast but risks missing regressions.
- **Structured vs. flexible:** Rigid output formats (single-line errors, pre-computed stats) are easy for agents to parse but harder for humans to read and harder to extend for new test types.
- **Agent time-blindness:** Agents cannot sense elapsed time, so they cannot make cost-aware decisions about whether to run full or partial test suites.

## Solution

Design test infrastructure with two complementary patterns that make test output agent-consumable by default.

**Pattern 1: Context-Friendly Output**

1. **Line-budget console output.** Limit console output to a small number of summary lines (e.g., 5-10 lines). Include: total tests, passed, failed, and a one-line summary per failure.
2. **Detail-to-file.** Write full stack traces, verbose logs, and per-test details to log files that the agent can selectively grep when investigating a specific failure.
3. **Single-line greppable errors.** Format each failure as a single line: `ERROR <test_name> <reason>`. No multi-line stack traces in the summary stream.
4. **Pre-computed aggregate stats.** Output pass rate, failure count, and duration as structured data (e.g., JSON or key-value pairs) so the agent does not waste tokens computing them.

**Pattern 2: Fast-Mode Subset Testing**

1. **Provide a `--fast` flag** that runs a small deterministic subsample (1-10%) of the test suite.
2. **Deterministic per-agent, random across agents.** Each agent's subsample is seeded by agent ID, so individually it is reproducible but collectively all tests are covered across parallel agents.
3. **Default to fast mode in agent loops.** Full suite runs are reserved for pre-commit or CI gates.

## Consequences

**Positive:**
- Agents spend context tokens on actionable failure information rather than noise.
- Fast-mode enables rapid iteration loops without exhausting time or compute budgets.
- Greppable error format enables targeted investigation without loading full output.
- Pre-computed stats eliminate redundant token-consuming computation by the agent.

**Negative:**
- Overly terse output may obscure complex failures that require multi-line context to diagnose. The agent must know to fall back to log files.
- Fast-mode subsamples may miss interacting failures that only manifest when specific tests run together.
- Deterministic subsamples may systematically exclude certain failure categories if the seeding is poorly distributed.
- Requires upfront investment in test infrastructure that many teams skip.

## Known Uses

- Anthropic used both patterns when building a C compiler with parallel Claude agents. The test design changes were described as critical for enabling autonomous multi-hour coding sessions where agents could self-verify without context exhaustion.

## Contract

### Preconditions
A test suite exists that will be consumed by an LLM agent operating within a finite context window. The agent has no built-in sense of elapsed wall-clock time.

### Invariants
Console output from a test run never exceeds a defined line budget. Full diagnostic details are always written to log files accessible via grep or file read. Every error in the summary stream is a single greppable line.

### Governance
Changes to the output format are reviewed against the consuming agent's parsing logic. The fast-mode subsample percentage is documented, adjustable, and reviewed when test suite composition changes significantly.

### Recovery
If terse console output masks a real failure, the agent falls back to reading the full detail log file for the failing test. If fast-mode misses a regression, it is caught by the next full-suite run (pre-commit gate or CI). If subsampling is found to systematically miss a failure category, the seeding strategy is revised.
