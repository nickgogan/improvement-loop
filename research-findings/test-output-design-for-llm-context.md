---
name: Test Output Design for LLM Context Windows
summary: 'Design test output for agent consumption: limit console to a few summary lines, log details to files for agent grep, format errors as single-line greppable strings, pre-compute aggregate stats.
  Prevents context window pollution from verbose test output.'
implementation_notes: Directly applicable to MetaSystem's eval and testing infrastructure. Test harnesses should emit LLM-friendly output by default.
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- anthropic-building-c-compiler.md
related_findings:
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: extracted
consumed_by: ["patterns/test-output-design-for-llm-context.md"]
---

## What It Is

Two complementary patterns for test infrastructure in agent-driven development. (1) **Context-friendly output**: Limit console output to a few summary lines; log full details to files that the agent can grep/process selectively. Format errors as single-line "ERROR reason" strings for easy pattern matching. Pre-compute aggregate stats (pass rates, failure counts) so the agent doesn't waste tokens recomputing them. (2) **Fast-mode subset testing**: Provide a `--fast` flag that runs a small random deterministic subsample (1-10%) of the test suite per agent. The subsample is deterministic per-agent but random across VMs, so collectively all tests are covered. This addresses "time blindness" -- agents lack time sense and will run full test suites for hours without realizing the cost.

## Why It Matters

Verbose test output is one of the most common sources of context window pollution in agent-driven development. A failing test suite that dumps 10,000 lines of output consumes the agent's context budget on noise rather than actionable information. Fast-mode testing prevents agents from spending hours on full test runs when incremental feedback would suffice.

## Why People Are Using It

Anthropic documented these patterns from building a C compiler with parallel Claude agents. The test design changes were critical for enabling autonomous multi-hour sessions where agents could self-verify without context exhaustion.

## Potential Improvements

Adaptive test subsample size based on recent failure rates (more failures = larger sample). Test result diffing between runs so agents see only new failures.

## Potential Failure Modes

Overly terse output may hide important context for debugging complex failures. Fast-mode subsample may miss interacting failures that only manifest when specific tests run together. Deterministic subsamples may systematically miss certain failure categories.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[test-output-design-for-llm-context.md]] in `extracts/patterns/`
