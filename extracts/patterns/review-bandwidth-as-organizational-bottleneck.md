---
title: "Review Bandwidth Bottleneck Management"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "review-bandwidth-as-organizational-bottleneck"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Agent-produced output volume exceeds human review capacity. A human gate exists in the pipeline (no fully autonomous deployment)."
  invariants: "No agent output bypasses human review unless an automated pre-screen has verified it against defined acceptance criteria. Review cost is tracked per artifact type."
  governance: "Changes to review delegation (what gets auto-screened vs. human-reviewed) require explicit authorization. Review quality metrics are maintained to detect depth erosion."
  recovery: "If review quality degrades (detected via downstream failures of approved artifacts), reduce throughput and tighten review criteria until quality stabilizes. Do not increase volume to compensate for a quality problem."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Review Bandwidth Bottleneck Management

**Source:** [[review-bandwidth-as-organizational-bottleneck]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

AI agents produce output at roughly 100x human speed, but human reviewers can only increase their review throughput to approximately 3x normal rate. This 100x/3x asymmetry means the binding constraint on agentic productivity is not production capacity but review capacity. Unreviewed output accumulates as a liability -- it cannot be trusted, deployed, or built upon. The organization's investment in agent tooling yields diminishing returns because the review queue grows faster than it drains.

## Forces

- **Throughput vs. quality.** Speeding up review risks shallow approval of subtly flawed work. Maintaining review depth limits throughput to a fraction of production capacity.
- **Automation vs. trust.** Automated pre-screening can filter low-risk output, but the screening criteria themselves need validation. Bad filters create false confidence.
- **Parallelism vs. coordination.** Multiple reviewers working in parallel increase bandwidth, but require coordination to maintain consistent standards and avoid duplicated or conflicting reviews.
- **Skill elevation vs. availability.** Higher-skilled reviewers process larger diffs faster and catch architectural issues, but such reviewers are scarce and expensive.
- **Production pressure vs. review backlog.** Agents keep producing while review queues grow. Pausing production feels wasteful; continuing production inflates the backlog.

## Solution

Treat review capacity as the primary planning constraint, not production capacity. Design the pipeline to match review bandwidth, not agent output speed:

1. **Measure review cost per artifact type.** Different outputs have vastly different review costs (a finding summary vs. a schema migration vs. a governance document). Track average review time per type to make capacity planning concrete.

2. **Triage before review.** Use automated pre-screening to sort agent output into tiers:
   - **Auto-approvable:** Output that meets verifiable acceptance criteria (tests pass, schema validates, linting clean). Requires spot-check review, not full review.
   - **Standard review:** Requires human judgment but is well-scoped (single finding, single artifact).
   - **Deep review:** Architectural decisions, cross-system changes, governance modifications. These consume the most review bandwidth and must be prioritized.

3. **Batch and pace production to review rhythm.** Rather than continuous agent production, run agents in batches sized to the reviewer's capacity. Produce a batch, review it, then produce the next. This prevents backlog accumulation.

4. **Elevate reviewer capability.** Invest in tools and training that make review faster without sacrificing depth: structured diffs, summary-first presentation, automated consistency checks, and comparison views against prior approved artifacts.

5. **Track review quality separately from review speed.** Monitor downstream failure rates of approved artifacts. If failures increase, the review process is degrading and throughput must be reduced.

## Consequences

**Positive:**
- Reframes the ROI conversation: the real investment for agentic adoption is review infrastructure, not agent tooling.
- Prevents accumulation of unreviewed output that becomes stale and needs re-review.
- Explicit triage reduces review burden on low-risk output without eliminating oversight.
- Batch-pacing keeps production and review synchronized.

**Negative:**
- Pacing production to review speed means agents are idle much of the time, which feels wasteful.
- Automated pre-screening criteria must themselves be reviewed and maintained -- a meta-review burden.
- Review cost measurement adds overhead to the review process itself.
- The 100x/3x framing oversimplifies: different output types have vastly different production and review cost ratios.

## Known Uses

- MetaSystem's human gate model (DD-29) enforces review at every pipeline stage boundary. The review bottleneck is already operational -- the research pipeline produces findings faster than Nick can review them.
- Teams adopting agentic workflows report three common responses: parallel review tracks, automated pre-screening, and elevated reviewer skill requirements.
- The MetaSystem pipeline's priority-based triage of proposals and findings partially addresses this through structured filtering.

## Contract

### Preconditions
Agent-produced output volume exceeds human review capacity (the queue grows faster than it drains). A human gate exists in the pipeline -- there is no fully autonomous deployment path. Review cost per artifact type is measurable or estimable.

### Invariants
No agent output bypasses human review unless an automated pre-screen has verified it against defined, explicit acceptance criteria. Review cost is tracked per artifact type and used for capacity planning. Review quality metrics (downstream failure rate of approved artifacts) are maintained to detect depth erosion.

### Governance
Changes to review delegation -- specifically, what categories of output get auto-screened vs. requiring full human review -- require explicit authorization (Design Decision level). Review quality metrics are reported alongside throughput metrics; throughput without quality data is not a valid report.

### Recovery
If review quality degrades (detected via increased downstream failures of approved artifacts, or via spot-check audits revealing missed issues), reduce production throughput and tighten review criteria until quality metrics stabilize. Do not increase review volume to compensate for a quality problem -- that amplifies the problem. Investigate root cause: were screening criteria too loose? Was review too shallow? Did artifact complexity increase?
