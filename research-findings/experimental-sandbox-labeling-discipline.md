---
name: "Experimental-Sandbox Labeling Discipline"
summary: "When a vendor publishes a benchmark claim that isn't backed by the shipping product, they explicitly label it as experimental — 'highly experimental,' 'not our main production engine (yet),' even 'social experiment / parody' — in the same artifact as the headline number. Readers get the architectural insight without mistaking the sandbox for the product. Plain English: the 99% score is the research prototype; the 85% score is what you actually get. Say so, up front, in big letters."
implementation_notes: null
category: "Governance"
evidence_strength: "Low (single-vendor-documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - "General"
adopted_in: []
sources:
  - "supermemory-99-sota-blog.md"
related_findings:
  - file: retraction-log-as-governance-artifact.md
    rel: same-problem
  - file: tool-enforced-dev-heldout-split.md
    rel: same-problem
  - file: production-configuration-baseline-discipline.md
    rel: extends
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-24"
pipeline_status: classified
consumed_by: []
---

## What It Is

A proactive-labeling governance pattern for benchmark claims that aren't backed by the production configuration. Instead of retracting after the fact ([[retraction-log-as-governance-artifact]]) or shipping a stripped-down benchmark config as the headline ([[production-configuration-baseline-discipline]] anti-pattern), the vendor labels the claim at publication time with phrases like:

- *"Highly experimental."*
- *"Not our main production Supermemory engine (yet)."*
- *"A social experiment to create a new standard."*
- *"Parody."*

The labeling has to meet three criteria to be load-bearing:

1. **Colocated with the headline number.** Not in a footnote, not on a separate page — in the same paragraph, ideally in the same sentence as the score.
2. **Unambiguous.** "Experimental" alone can drift to mean "cutting-edge"; explicit "not in production" / "not our real product" leaves no ambiguity.
3. **Architecturally precise.** Specify what the experimental configuration includes (e.g., "3 parallel reader agents, 8-variant ensemble, Gemini 2.0 Flash orchestration + GPT-4o-mini decision forest") so readers can distinguish it from the production system.

This is a positive-space alternative to rejection-list governance. Rather than prohibit unusual benchmark configurations, make them welcome — but require they be labeled.

## Why It Matters

Benchmark inflation is a known governance problem. The standard mitigation is retraction ([[retraction-log-as-governance-artifact]]) — correct after the fact. Retraction is reactive; by the time you retract, the stale number is already cited. Proactive sandbox labeling shifts the trust surface earlier: the vendor signals at publication time which number is load-bearing for product decisions vs which is research exploration.

For MetaSystem's future IL artifacts: any `/assess-*` skill result, any Perplexity-driven research comparison, any internal eval of a new prompt pattern — these are all susceptible to "we got a great number in the sandbox, ship the sandbox" pressure. A sandbox-labeling discipline separates "we proved this is possible" (research value) from "this is what you get if you use it" (product claim). Both are valuable; conflating them is the failure mode.

For positive-space governance per `feedback_positive_space_governance.md`: rather than maintaining a rejection list of forbidden benchmark configurations, maintain a positive invariant — "any claim not in the production config carries an experimental label." The positive invariant is bounded; the rejection list would be countably infinite.

## Why People Are Using It

Observed in [Supermemory's 99% SOTA blog post](https://supermemory.ai/blog/we-broke-the-frontier-in-agent-memory-introducing-99-sota-memory-system/) 2026-03-22 — see [[supermemory-99-sota-blog]] for the source entry. The post describes ASMR (Agentic Search and Memory Retrieval) producing ~99% on LongMemEval_s, then in the same document states:

- *"This is not our main production Supermemory engine (yet)."*
- *"Highly experimental."*
- *"A social experiment to create a new standard"* (the vendor's own framing).

The architectural description is precise enough that a reader can distinguish the ASMR sandbox from the shipping product (which was benchmarked at 85% on the same dataset — see [[supermemory-research-page]]). Both numbers are in the KB; both are usable; the labeling keeps the interpretive load low.

Counter-example — MemPalace published 96.6% recall_any@5 as a headline and the shipping product uses a different configuration (features on, scoring drops 12.4pp per [[production-configuration-baseline-discipline]]). No proactive sandbox label. The retraction in [[retraction-log-as-governance-artifact]] came later. That's the reactive pattern; this finding is its proactive alternative.

## Potential Alternatives

- **Retract after the fact** ([[retraction-log-as-governance-artifact]]). Works for errors caught post-publication. Doesn't help readers who already acted on the uncorrected number.
- **Publish only production numbers.** Conservative; loses the research-exploration surface. Forces incremental publication of capability.
- **Separate research-page and product-page.** Architectural separation; many vendors do this (Supermemory's research page vs product page). Doesn't solve the problem if a single blog post mixes both.
- **Append severity tiers to every claim** (production / beta / experimental / research). More structured; requires publication infrastructure most vendors lack.
- **No labeling; let the reader figure it out.** Industry default. Produces the 99% → 85% confusion this finding addresses.

## Potential Improvements

- **Labeling vocabulary standardization.** "Experimental" / "beta" / "research preview" / "not for production" are not interchangeable; a shared vocabulary across the agent-memory or agent-harness space would reduce interpretation cost.
- **Machine-readable labels.** `x-maturity: experimental` in the paper/blog frontmatter; leaderboards and aggregators could then filter / annotate automatically.
- **Sandbox-to-production migration logs.** When an experimental feature reaches production, link back to the original sandbox claim and note which aspects did / didn't carry over.
- **Sandbox reproducibility requirements.** Even experimental claims should be reproducible — otherwise the labeling is a "we don't have to back this up" escape hatch.

## Potential Failure Modes

- **Labels weaken over time.** First time "highly experimental" appears, readers treat it seriously; fifth time, it becomes boilerplate. Mitigation: combine with reproducibility requirements and standardized severity levels.
- **Labels used as marketing.** "Experimental SOTA!" becomes a headline-optimization trick — the label is technically correct but structurally misleading. Mitigation: prohibit top-line (above-the-fold) placement of experimental-labeled numbers.
- **Experimental-to-production drift without re-labeling.** An experimental feature ships to production; the original sandbox number is still cited without update. Mitigation: require label-update protocol when features graduate.
- **Sandbox as refuge for bad methodology.** "It's just a sandbox, we didn't have to be rigorous." Undermines the distinction between exploratory research and careless research. Mitigation: rigorous experimental claims still require methodology disclosure ([[ensemble-eval-majority-required-for-success]] applies to the sandbox too).
