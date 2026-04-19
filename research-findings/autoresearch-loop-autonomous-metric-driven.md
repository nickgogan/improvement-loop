---
notion_id: 32b1e08b-9b34-817b-9da7-f69e0dcca004
name: 'Autoresearch Loop: Autonomous Metric-Driven Experiment Cycles'
summary: An orchestrator agent runs a tight loop of hypothesis → experiment → measure → keep/discard → repeat, using an objective metric as the feedback signal and accumulating learnings in a persistent
  markdown file. Adapted from Karpathy's nanoGPT training loop for any measurable business process.
implementation_notes: null
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- karpathy-autoresearch-video.md
proposals: []
date_discovered: '2026-03-22'
last_updated: 2026-04-08
related_findings:
  - file: "agent-cost-blowup-mitigation-strategies.md"
    rel: "same-problem"
pipeline_status: "raw"
consumed_by: []
---
# Autoresearch Loop: Autonomous Metric-Driven Experiment Cycles

## What It Is
The autoresearch loop is a scheduling pattern where a Claude Code orchestrator agent runs fully autonomously on a fixed interval (e.g., every hour via GitHub Actions cron). Each cycle: (1) reads previous experiment results from a JSON/log store, (2) generates a new 'challenger' variant based on a resource.md of accumulated learnings, (3) deploys both baseline and challenger via API, (4) waits for measurement, (5) harvests the winning variant as the new baseline, and (6) appends new learnings to resource.md. The human only sets up the initial baseline and metric definition; after that the loop runs 24/7 without involvement.

## Why It Matters
Manual A/B testing has enormous friction — copy/pasting leads, setting up campaigns, waiting, comparing results. This eliminates all operational overhead so the improvement rate is bounded only by the feedback loop speed and infrastructure scale, not by human availability. The compounding resource.md means each future experiment benefits from all prior learnings.

## Why People Are Using It
Karpathy's public release legitimized the pattern for non-ML contexts. Nick demonstrates a working cold-email optimizer (with Instantly API) and enumerates at least 8 other verticals (landing pages, ad creatives, chatbot scripts, product descriptions, YouTube titles, newsletter subject lines, pricing pages). The 'wake up to a log of improvements' framing is extremely sticky for practitioners.

## Potential Alternatives
Manual A/B testing platforms (Optimizely, VWO), LLM-native evals frameworks (promptfoo, braintrust), or human-in-the-loop iteration. None run continuously without human scheduling.

## Potential Improvements
Adding a statistical significance gate before accepting a winner would reduce false positives. Connecting a vector store instead of a growing markdown file would scale the learnings store more gracefully beyond ~500 iterations.

## Potential Failure Modes
Without a clear objective metric, the loop has no signal to optimize against. Fast feedback loops (< 5 min) are better; slow ones (days) mean the loop can't compound meaningfully. If the measurement API has noise or lag, winners are selected on bad data. The resource.md file can grow too long after ~500-1000 runs and exceed context limits.
