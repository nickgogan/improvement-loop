---
title: "Review Obsolescence as Design Goal"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "review-obsolescence-as-design-goal"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "A review process exists that produces recurring comments. Review comment history is accessible for pattern analysis. The team has authority to introduce automated checks (linters, schema constraints, CI rules)."
  invariants: "Every review comment triggers an explicit 'how do I make this comment impossible?' analysis. Automation targets entire classes of comments, not individual instances. Judgment-dependent review (architecture, design, naming) is never automated away."
  governance: "Review comment categories are tracked and prioritized by frequency. New automated checks require review before enforcement. The set of automatable vs. judgment-dependent categories is revisited quarterly."
  recovery: "If an automated check produces false positives that block legitimate work, disable the check immediately, file it for revision, and revert to manual review for that category until the check is fixed."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Review Obsolescence as Design Goal

**Source:** [[review-obsolescence-as-design-goal]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Review layers accumulate over time and each one adds approximately 10x wall-clock delay. Reviewers catch the same categories of issues repeatedly -- formatting, schema violations, missing fields, structural inconsistencies -- but the system never learns from the repetition. The review pipeline becomes a bottleneck not because individual reviews are slow, but because the volume of reviewable issues never decreases.

## Forces

- **Thoroughness vs. speed:** Comprehensive review catches more issues but multiplies cycle time. Removing review entirely risks quality collapse.
- **Automation rigidity vs. judgment flexibility:** Automated checks eliminate mechanical review but can block legitimate innovation if over-applied. Not all review categories are automatable.
- **Upfront investment vs. ongoing cost:** Building a linter or schema constraint takes time now but saves unbounded review time later. Teams default to the cheaper immediate option (just review it again).
- **Reviewer identity vs. system improvement:** Reviewers who see their role as "catching errors" resist automation that eliminates their work. The pattern requires reframing the reviewer as a system designer whose goal is to make their own review unnecessary.

## Solution

Treat every review comment as a system design signal, not a one-time correction. For each comment:

1. **Classify the comment category.** Is this formatting, schema compliance, structural consistency, naming convention, architectural judgment, or something else?

2. **Ask: "How do I make this entire category of comment impossible?"** Not "how do I fix this instance" but "what tool, rule, or constraint would prevent any future instance of this class?"

3. **For automatable categories, build the check.** Examples: `go fmt` eliminates all formatting debates. A YAML schema validator eliminates all frontmatter field errors. A CI linter eliminates all import ordering comments. The check runs before review, so the reviewer never sees the issue.

4. **For judgment-dependent categories, document the decision criteria.** Architecture, design tradeoffs, and naming require human evaluation. Document the principles that guide these judgments so reviewers apply them consistently, but do not attempt to automate them.

5. **Track category elimination over time.** Measure which categories of review comments have been eliminated and which persist. The shrinking set of remaining categories represents the genuine value of human review.

The canonical example is Go's `go fmt` tool, which ended all whitespace and formatting debates in the Go community permanently by making them structurally impossible.

## Consequences

**Positive:**
- Review volume decreases over time as entire comment categories are eliminated
- Remaining review focuses on high-value judgment calls where human expertise matters
- Review cycle time decreases because fewer issues need human attention
- The system accumulates prevention infrastructure (linters, schemas, CI checks) that benefits all contributors
- Aligns with Toyota's quality-at-source principle: prevent defects rather than inspect for them

**Negative:**
- Requires upfront investment to build automated checks for each category
- Over-automation risk: rigid checks can block legitimate exceptions and novel approaches
- Category classification requires judgment -- some comments span automatable and judgment-dependent territory
- Teams must accept that the reviewer's role changes from error-catcher to system-designer, which can meet cultural resistance

## Known Uses

- Go community's `go fmt` tool -- eliminated all formatting review comments across the entire ecosystem
- Tailscale engineering practices (Avery Pennarun, CEO) -- production-tested at scale
- Toyota Production System quality-at-source philosophy -- manufacturing equivalent with decades of evidence
- MetaSystem Review Gates -- when a review gate catches an issue, the fix should include a constraint that prevents recurrence (implementation_notes from the finding)
- AI agents analyzing review comment history to propose automated checks -- emerging practice for closing the feedback loop

## Contract

### Preconditions
A review process exists that produces recurring comments. Review comment history (or institutional memory) is accessible for pattern analysis. The team has authority to introduce automated checks such as linters, schema constraints, or CI rules into the pipeline.

### Invariants
Every review comment triggers an explicit analysis of how to eliminate that entire category of comment. Automation targets classes of issues, never individual instances. Judgment-dependent review categories (architecture, design, naming) are explicitly preserved and never automated away. Automated checks run before human review, not after.

### Governance
Review comment categories are tracked and prioritized by frequency for automation. New automated checks require human review before enforcement to prevent over-constraint. The boundary between automatable and judgment-dependent categories is revisited periodically as tooling evolves. Category elimination progress is measured to validate the pattern's effectiveness.

### Recovery
If an automated check produces false positives that block legitimate work, disable the check immediately, revert to manual review for that category, and file the check for revision. If a category previously classified as judgment-dependent becomes automatable due to new tooling, reclassify and build the check. If review volume increases despite automation, audit whether new comment categories have emerged that need classification.
