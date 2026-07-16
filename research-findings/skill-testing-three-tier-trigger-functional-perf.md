---
name: Skill Testing — Three-Tier (Triggering, Functional, Performance)
summary: 'Anthropic''s Complete Guide PDF prescribes three test tiers for skills: (1) Triggering tests — does the skill load at the right times (positive and negative cases). (2) Functional tests — does
  the skill produce correct outputs. (3) Performance comparison — does the skill beat baseline on tool calls, error rate, tokens, user effort. Each tier has named test-case shapes and a baseline-vs-skill
  comparison format. Three levels of rigor available: manual testing in Claude.ai (fast iteration), scripted testing in Claude Code (repeatable validation), programmatic testing via API (systematic eval
  suites).'
implementation_notes: 'Per-tier guidance from PDF: Triggering — should-trigger + should-NOT-trigger sets, covering paraphrased requests and adjacent-but-distinct queries. Functional — valid outputs, API
  call success, error handling, edge cases. Performance — baseline (without skill) vs. with-skill: back-and-forth messages, failed API calls, tokens consumed, user clarifying questions. Concrete example:
  ''Without skill: 15 messages, 3 failed API calls, 12,000 tokens. With skill: 2 clarifying questions, 0 failed calls, 6,000 tokens.'' Aspirational targets named: skill triggers on 90% of relevant queries;
  0 failed API calls; consistent results across sessions.'
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-complete-guide-building-skills-pdf.md
- anthropic-skills-repo.md
related_findings:
- file: skill-description-optimization-loop-held-out-test.md
  rel: extends
- file: generator-assessor-separation-in-skill-iteration.md
  rel: same-problem
- file: machine-framework-for-agentic-coding-skill-asses.md
  rel: same-problem
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---

# Skill Testing — Three-Tier (Triggering, Functional, Performance)

## What It Is

Anthropic's Complete Guide PDF prescribes a three-tier testing approach for skills:

### Tier 1: Triggering Tests
**Goal:** Does the skill load at the right times?
**Test cases:**
- ✅ Triggers on obvious tasks
- ✅ Triggers on paraphrased requests
- ❌ Doesn't trigger on unrelated topics

Example suite: a ProjectHub skill should trigger on "Help me set up a new ProjectHub workspace", "I need to create a project in ProjectHub", "Initialize a ProjectHub project for Q4 planning" — and not on "What's the weather in San Francisco?", "Help me write Python code", "Create a spreadsheet" (unless ProjectHub skill handles sheets).

### Tier 2: Functional Tests
**Goal:** Does the skill produce correct outputs?
**Test cases:** Valid outputs generated, API calls succeed, error handling works, edge cases covered.

Example: "Test: Create project with 5 tasks. Given: Project name 'Q4 Planning', 5 task descriptions. When: Skill executes workflow. Then: Project created in ProjectHub, 5 tasks created with correct properties, all tasks linked to project, no API errors."

### Tier 3: Performance Comparison
**Goal:** Prove the skill improves results vs. baseline.
**Format:** Baseline (without skill) vs. with-skill comparison.

Example baseline:
> Without skill: User provides instructions each time, 15 back-and-forth messages, 3 failed API calls requiring retry, 12,000 tokens consumed.
> With skill: Automatic workflow execution, 2 clarifying questions only, 0 failed API calls, 6,000 tokens consumed.

### Rigor levels (orthogonal to tier):
- **Manual in Claude.ai** — fast iteration, no setup
- **Scripted in Claude Code** — repeatable validation across changes
- **Programmatic via API** — systematic eval suites against defined test sets

### Aspirational targets:
- Skill triggers on 90% of relevant queries
- 0 failed API calls per workflow
- Consistent results across sessions

## Why It Matters

The three-tier framing separates concerns that are often conflated. A skill that triggers but doesn't work fails tier 2. A skill that triggers AND works but doesn't beat baseline fails tier 3 (the skill is a no-op). A skill that beats baseline but triggers unreliably fails tier 1.

Each tier has its own failure mode and its own measurement. Combining them into a single "skill quality" metric loses signal.

The baseline-vs-skill comparison in tier 3 is the most practically valuable. It answers the question that determines whether a skill is worth maintaining: does it actually help? The named metrics (message count, failed calls, token count, clarifying questions) are concrete and measurable.

The progression from manual → scripted → programmatic rigor maps to skill maturity: early iteration is manual; mature skills get programmatic test suites.

## Why People Are Using It

Codified in Anthropic's Complete Guide PDF. Operationalized in the skill-creator skill's iteration loop, which spawns with-skill and baseline subagents in parallel for each test case. The benchmark.json schema in skill-creator/references/schemas.md is the persistent format for these comparisons.

## Potential Alternatives

Single-tier "does it work" testing (conflates triggering, function, and performance). User acceptance testing only (qualitative; doesn't catch triggering issues at scale). Author self-evaluation (rejected by generator-assessor separation). Production telemetry only (reactive — bugs ship to users before being caught).

## Potential Improvements

Per-tier test-case templates for common skill categories. Cross-tier diagnostics — when a test fails, which tier did it fail at and what's the remedy. Continuous performance baselines (skill is compared not just to no-skill but to last version's skill). Skill-vs-skill benchmarks (multiple skills competing for the same trigger).

## Potential Failure Modes

**Tier 1 overfits the trigger eval.** A skill tuned to trigger on the eval queries but no others — addressed by the held-out test set in description optimization loop.

**Tier 2 with bad assertions.** Functional tests that check the wrong thing pass on bugs and fail on correct behavior. Authoring the right assertions is hard; skill-creator's grader.md tries to help.

**Tier 3 measurement noise.** Token counts and message counts vary across runs even with the same skill. Few-run baselines may be misleading. skill-creator runs each query 3 times to handle this; manual testing usually doesn't.

**Tier rigor mismatch.** Manually testing a skill targeted at programmatic API consumers leaves the actual deployment untested. Choose the rigor that matches the deployment.

**Tiers run sequentially.** Authors who test tier 1 then move to tier 2 may not revisit tier 1 after changing the description. Triggering can regress silently while functional behavior is stable.

**Tier 3 baseline is unfair.** If the baseline is "Claude with no context at all," the skill always looks great. The honest baseline is "Claude with whatever context the user would otherwise provide" — harder to measure but more truthful.
