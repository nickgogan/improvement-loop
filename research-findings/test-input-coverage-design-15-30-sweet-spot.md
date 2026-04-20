---
name: Test Input Coverage Design -- 15-30 Input Sweet Spot for Eval Suites
summary: For binary eval suites driving self-improvement loops, 15-30 test inputs is the practical sweet spot. Below 10 risks overfitting; above 30 adds cost without proportional coverage. Inputs must cover
  typical cases, clear edge cases, and assertion-targeted examples. Diverse input variations (length, complexity, formatting) prevent the agent from gaming a narrow distribution.
implementation_notes: 'When building eval suites for MetaSystem skills, design test inputs deliberately: cover happy path, edge cases, and at least one input per assertion. Review coverage after first 5-10
  improvement iterations before running unattended.'
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- how-to-build-self-improving-ai-skills-with-binary.md
related_findings:
- file: eval-driven-development-autonomous-quality.md
  rel: enabled-by
- file: multidimensional-success-criteria-smart.md
  rel: same-problem
- file: ace-execution-feedback-no-labels-required.md
  rel: same-problem
- file: binary-eval-assertion-design-deterministic-plus-ll.md
  rel: enabled-by
- file: claude-code-skills-20-four-mode-skill-lifecycle-wi.md
  rel: enabled-by
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---
## What It Is

A test input design methodology for binary eval suites:

**Coverage requirements:**
- Typical/common cases (the 80% path)
- Clear edge cases (unusual length, complexity, formatting)
- Assertion-targeted examples (at least one input designed to exercise each specific assertion)
- Diverse input variations to prevent the agent from learning a narrow distribution

**Quantity guidance:** 15-30 inputs is the practical sweet spot. Under 10 risks overfitting where the agent learns to pass specific tests rather than generalize. Over 30 adds evaluation cost and iteration time without proportional improvement in coverage.

**Guard rails:**
- Review first 5-10 iterations of the improvement loop before running unattended
- Use git version control to track all changes
- Set iteration maximums (40-50 cycles) to prevent cost overruns

## Why It Matters

Test input design is the most under-discussed component of self-improvement loops. The quality of test inputs determines whether the improvement loop produces genuinely better skills or merely overfitted ones. Poor test design is the primary reason improvement loops converge without meaningful improvement.

## Why People Are Using It

MindStudio documents this methodology alongside their binary eval pattern. The 15-30 range is validated by production overnight improvement runs. Karpathy's autoresearch pattern uses a similar coverage-first approach.

## Potential Failure Modes

- **Insufficient diversity:** If all test inputs are similar, the agent learns surface patterns rather than the underlying skill
- **Missing edge cases:** The improvement loop converges but the skill fails on real-world inputs outside the test distribution
- **No iteration cap:** Without a maximum iteration limit, improvement loops can run indefinitely, consuming compute without convergence
