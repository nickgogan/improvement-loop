---
name: Success-Rate Evaluation Over Binary Pass/Fail for Agent Systems
summary: 'For agent evaluation, the question should not be ''did this prompt work?'' but ''how often does the agent succeed?'' Single-pass evaluation hides instability. The pattern: run multiple trials
  per scenario, grade outcomes (not just paths), combine deterministic tests + rubrics + transcript reviews, and include adversarial coverage from the start.'
implementation_notes: 'Extends MetaSystem''s binary eval approach with a statistical lens. Current skill evals run single passes. Pattern: run each eval case multiple times (5-10), report success rates,
  track rates over time to detect regressions. Combine with adversarial test cases.'
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- ai-agent-prompt-engineering-best-practices-inflect.md
related_findings:
- file: volume-over-quality-eval-principle.md
  rel: same-problem
- file: factorial-design-eval-systematic-context-variati.md
  rel: extended-by
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
- file: binary-eval-assertion-design-deterministic-plus-ll.md
  rel: same-problem
- file: four-layer-agent-evaluation-architecture.md
  rel: extended-by
- file: claude-code-skills-20-four-mode-skill-lifecycle-wi.md
  rel: enabled-by
- file: cross-model-verification-for-bug-finding.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---
## What It Is

A shift in agent evaluation methodology from binary pass/fail on single runs to statistical success rates across multiple trials:

**Core principles:**
1. **Multiple trials per scenario:** One pass per scenario hides instability. Run the same eval case 5-10 times to measure consistency.
2. **Success rate over binary:** "This prompt works" is less useful than "this agent succeeds 87% of the time on this scenario." Track the rate, not the single result.
3. **Outcome grading over path grading:** The agent may take multiple valid paths to the correct result. Grade the outcome, not whether the agent followed the expected steps.
4. **Combined evaluation methods:** Deterministic tests (structural checks), rubrics (quality assessment), and transcript reviews (reasoning quality) each catch different failure modes.
5. **Adversarial coverage from the start:** Include jailbreak attempts, conflicts between user and system prompts, and edge cases in the eval suite from day one, not as an afterthought.

**Eval design recommendations:**
- Design tests around the actual jobs the agent performs and the steps it should take
- Run continuous, repetitive evaluations that evolve over time
- Track success rates per scenario to identify which tasks are most fragile

## Why It Matters

Binary pass/fail evaluation creates a false sense of reliability. An agent that passes a single eval run may fail 30% of the time in production due to non-deterministic model behavior. Success rate evaluation surfaces this instability before deployment and provides a meaningful metric for tracking improvement over time.

## Why People Are Using It

Inflectra documents this as the recommended evaluation methodology for production agent systems. The pattern is consistent with Anthropic's Skills 2.0 Benchmark mode which tracks Pass Rate as a primary metric. The shift from binary to statistical is driven by production experience with non-deterministic agent failures.

## Potential Failure Modes

- **Cost multiplication:** Running 5-10 trials per scenario increases eval cost proportionally; needs to be budgeted
- **Flaky pass threshold:** Setting the success rate threshold too low (e.g., 60%) normalizes unreliable behavior
- **Path-blind outcome grading:** Grading only outcomes may miss dangerous reasoning patterns that happen to produce correct results
