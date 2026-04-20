---
name: 'Inter-Agent Web Contamination: Persistent Eval Artifacts from Agent Queries'
summary: Agent search queries during evaluations create persistent web artifacts (auto-generated e-commerce pages, cached query trails) that contaminate future eval runs by embedding prior agents' hypotheses
  in indexable web content.
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General / Cross-System
sources:
- anthropic-eval-awareness-browsecomp.md
related_findings:
- file: eval-awareness-autonomous-benchmark-identification.md
  rel: enabled-by
- file: context-pollution-same-window-verification-bias.md
  rel: extends
- file: benchmark-signal-mismatch-optimization-gap.md
  rel: extends
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---
# Inter-Agent Web Contamination: Persistent Eval Artifacts from Agent Queries

## What It Is

During BrowseComp evaluation runs, Anthropic discovered that agents' search queries created persistent, indexable web pages on e-commerce and content aggregation sites. Retailers auto-generated product/market pages from search query strings (e.g., `[retailer].com/market/anonymous_8th_grade_first_blog_post_exact_date_...`), embedding prior agents' hypotheses and search terms in URLs without actual content matches. One agent explicitly noted: "Multiple AI agents have previously searched for this same puzzle, leaving cached query trails on commercial websites that are NOT actual content matches."

This creates a growing web record of evaluation runs that can influence future agents running the same eval -- a novel form of cross-run contamination distinct from traditional benchmark data leakage.

## Why It Matters

Traditional benchmark contamination comes from answer leakage into training data or publicly accessible datasets. This pattern is different: the act of running an evaluation on the open web actively creates new contamination for future runs. Each eval run leaves traces that make subsequent runs more likely to encounter evaluation-related content, potentially biasing results. This is a compounding problem -- it gets worse with each run.

For any system that evaluates agents using web search, this means eval scores may degrade over time not because models get worse, but because the web accumulates artifacts from prior runs. This is invisible without explicit monitoring.

## Why People Are Using It

Anthropic documented this as an unintended side effect discovered during BrowseComp analysis. No one is intentionally using this pattern -- it is a warning about a novel failure mode in web-based agent evaluation.

## Potential Improvements

Eval environments that route web searches through proxies that prevent query-based page generation. Rotating eval question sets to avoid repeated queries creating cumulative contamination. Monitoring for eval-artifact URLs appearing in search results during runs. Using cached/snapshot web data for evals rather than live web access.

## Potential Failure Modes

Attempting to clean up contaminated web pages is impractical at scale. Restricting web access during evals may invalidate the eval's purpose (testing web search capability). The pattern may also affect non-eval agent deployments -- production agents leave similar query trails that could influence other agents' searches.
