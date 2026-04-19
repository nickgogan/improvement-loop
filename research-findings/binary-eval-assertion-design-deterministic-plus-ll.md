---
name: Binary Eval Assertion Design -- Deterministic + LLM-as-Judge Dual Layer
summary: 'Effective binary eval suites combine two assertion types: deterministic checks (string matching, word counts, schema validation) for structural requirements, and LLM-as-judge evals for semantic
  quality (tone, coherence, hallucination detection). Each assertion returns exactly true or false. The dual layer ensures both structural correctness and semantic quality without scored metrics.'
implementation_notes: 'Directly applicable to MetaSystem skill eval suites. Current skills lack formal assertion libraries. Pattern: write deterministic assertions first (fast, cheap), then add LLM-as-judge
  assertions for qualities that resist programmatic checking. Lock eval files from agent modification.'
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- how-to-build-self-improving-ai-skills-with-binary.md
related_findings:
- file: three-tier-grading-hierarchy.md
  rel: same-problem
- file: karpathy-autoresearch-self-improvement-loop.md
  rel: enables
- file: eval-driven-development-autonomous-quality.md
  rel: enables
- file: four-layer-agent-evaluation-architecture.md
  rel: enables
- file: multidimensional-success-criteria-smart.md
  rel: same-problem
- file: ace-execution-feedback-no-labels-required.md
  rel: same-problem
- file: claude-code-skills-20-four-mode-skill-lifecycle-wi.md
  rel: enables
- file: success-rate-eval-over-binary-pass-fail.md
  rel: same-problem
- file: test-input-coverage-design-15-30-sweet-spot.md
  rel: enables
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: "synthesized"
consumed_by:
  - "building-agent-evaluation-suites.md"
---
## What It Is

A two-layer assertion architecture for binary eval suites:

**Layer 1 -- Deterministic checks:** String matching for structural requirements -- section headers present, word count within range, markdown validity, forbidden phrases absent, required fields with dates/owners. These are fast, cheap, and unambiguous.

**Layer 2 -- LLM-as-judge evals:** For semantic quality that resists programmatic checking -- tone consistency, coherence, hallucination detection, actionability of recommendations. Each LLM judge call returns a binary yes/no decision, not a score.

The key insight: binary (true/false) assertions provide clarity, automability, and debuggability that scored metrics (1-10 scales) cannot. A failing assertion points directly to the problem; a score of 6.2 tells you nothing actionable.

## Why It Matters

Most eval systems either use only deterministic checks (missing semantic quality) or only LLM-as-judge (expensive, slow, hard to debug). The dual-layer pattern catches both structural and semantic failures while keeping individual assertions debuggable. When a self-improvement loop makes a change, the binary pass/fail signal tells the agent exactly which requirement it broke.

## Why People Are Using It

MindStudio documents this as the standard pattern for overnight autonomous skill improvement loops. Anthropic's Skills 2.0 Grader sub-agent implements the same dual-layer architecture. The pattern scales to 15-30 test inputs with diverse coverage (typical cases, edge cases, assertion-targeted examples).

## Potential Improvements

- Build a reusable assertion library for common MetaSystem patterns (frontmatter validation, markdown structure, evidence citation)
- Add assertion conflict detection -- verify that all assertions are mutually satisfiable before running the improvement loop
- Track assertion pass rates over time to identify which requirements are hardest for agents to satisfy

## Potential Failure Modes

- **Evals too easy:** Assertions that always pass don't drive improvement -- they create false confidence
- **Conflicting assertions:** Mutually unsatisfiable requirements create infinite improvement loops
- **LLM-as-judge drift:** The judge model may shift its threshold over time, creating inconsistent pass/fail decisions
- **Eval file modification:** If the agent can modify its own eval files, it will "fix" the tests rather than the skill -- eval files must be locked

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[binary-eval-assertion-design-deterministic-plus-llm]] in `extracts/patterns/`
