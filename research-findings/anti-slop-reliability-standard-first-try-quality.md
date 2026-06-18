---
name: "Anti-Slop Reliability Standard: First-Try or Not Good Enough"
summary: "Rejecting the normalization of non-determinism and low reliability in agentic products. The standard is: if an agent product does not work reliably on the first attempt, it is not good enough to ship. 'Usually works' (3-5 out of 10 tries) should not be an acceptable product bar."
implementation_notes: null
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P2
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "problem-with-ai-agents-utori-compound-errors.md"
related_findings:
  - file: "march-of-nines-compounding-reliability-math-for-m.md"
    rel: "same-problem"
  - file: "specialized-harness-engineering-deterministic-rail.md"
    rel: "enables"
  - file: "agent-self-reporting-unreliability-independent-eval.md"
    rel: "same-problem"
  - file: "review-obsolescence-as-design-goal.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
tags:
  - "session-95-reextract"
pipeline_status: "synthesized"
consumed_by:
  - "agent-design-patterns.md"
  - "rules/first-try-reliability-as-product-bar.md"
---

# Anti-Slop Reliability Standard: First-Try or Not Good Enough

## What It Is

A product philosophy that explicitly rejects the emerging norm of tolerating non-determinism and low reliability in agentic products. Abhishek Das (Utori): "I push back on that getting normalized, especially with agentic products. If it's not good enough to work on the first try, it's not good enough."

The argument: the current ecosystem has developed a tolerance for "it usually works" -- users try an agent 10 times and maybe 3-5 times it succeeds. This is being normalized as acceptable. The anti-slop standard says this is not acceptable: agents should work reliably on the first attempt, and products that don't meet this bar should not be shipped.

## Why It Matters

This is the philosophical companion to the compound error math (March of Nines). The math shows why unreliable agents fail at scale; the anti-slop standard is the product discipline that follows from that math. Without this discipline, teams ship agents that demo well but fail in production, eroding user trust in the entire agent category.

For MetaSystem, this applies to skill reliability. Skills that "usually work" but sometimes produce incorrect output are not good enough. The standard argues for investing in harness engineering, evals, and guardrails until first-try reliability is achieved -- rather than shipping and hoping users will retry.

## Why People Are Using It

Utori's founders are AI researchers building consumer-facing agents. They see the competitive landscape as a race to the bottom on reliability ("a hundred different agent products that say they can do anything on the web, and you try it once and it doesn't really work"). Their differentiation strategy is reliability, not feature breadth.

## Potential Improvements

Define quantitative first-try reliability targets per workflow type. Track first-attempt success rate as a primary product metric rather than eventual success rate. Gate shipping on first-try reliability thresholds.

## Potential Failure Modes

Taken too literally, this standard prevents shipping anything -- models are inherently stochastic. The practical interpretation is: design for first-try success through scope constraint, guardrails, and error recovery, while acknowledging that statistical perfection is impossible. The risk is analysis paralysis: never shipping because nothing meets the "first try" bar.
