---
name: "Cross-Provider Benchmarking Framework as Trust Mechanism"
summary: "Ship an open-source benchmarking harness that includes your competitors as first-class subcommand arguments. Anyone — you, your competitors, an independent auditor — can run the same suite against any supported provider. Published results are verifiable because the apparatus is public and competitor-inclusive. Long-term trust mechanism that trades short-term comparative risk for long-term claim credibility."
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: null
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: tool-enforced-dev-heldout-split.md
    rel: same-problem
  - file: benchmark-operating-contract.md
    rel: same-problem
  - file: external-benchmark-hosting-as-trust-mechanism.md
    rel: extended-by
  - file: agent-native-app-store-emerging-category.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-23"
pipeline_status: raw
consumed_by: []
---

## What It Is

An open-source benchmarking harness designed from the start to support multiple vendors — including the publisher's direct competitors — as first-class subcommand arguments. Invocation shape:

```bash
bun run src/index.ts run -p <provider> -b <benchmark> -j <judge-model> -r <run-id>
# e.g., -p supermemory / mem0 / zep
# -b longmemeval / locomo / convomem
```

Also distributable as an agent skill:

```bash
npx skills add supermemoryai/memorybench
# Then: /benchmark-context in any supporting harness
```

Three mechanics make this a trust mechanism rather than a marketing artifact:

1. **Competitor support is first-class** — not a toggle, not a "coming soon." Competitors are supported on the same code path as the publisher's own system.
2. **Reproducibility is public.** The judge model, the benchmark dataset, the run ID, and the provider adapter are all public code; anyone can rerun.
3. **Distribution is low-friction.** Available as both CLI (for rigorous runs) and agent skill (for casual cross-comparison inside any MCP-compatible harness).

Contrasts with closed leaderboards (publisher-controlled, black-box judge), self-reported numbers on product pages, and methodology-opaque claims. Complementary to [[tool-enforced-dev-heldout-split]] (MemPalace's internal benchmark discipline): that finding covers *how you measure yourself honestly*; this finding covers *how you let others measure you against peers*.

## Why It Matters

For MetaSystem's long-term posture: if we ever ship anything with competitors (Household OS has existing competitors; eventual Claude Build releases may), the default move is to publish our own benchmarks. That works until someone asks "can I verify this against alternatives?" — at which point closed-benchmark credibility collapses. A competitor-inclusive harness avoids that failure mode from day one.

For the IL specifically: any future IL "evaluate my prompt against these 10 references" or "score this SKILL.md against these rubrics" pattern benefits from the same trust architecture. We have the beginnings of this in `/prompt-evaluator` and `/assess-skill`, but they operate only on our content. Pattern extension: publish the rubric, let external authors submit their own prompts/skills for the same evaluation.

For short-term: the pattern is also a distribution mechanism. Supermemory's MemoryBench is installable as a skill — they've turned benchmarking into a viral vector. Any user who runs `/benchmark-context` learns about Supermemory *and* sees the comparative data. The skill format does the work of ten blog posts.

## Why People Are Using It

Observed in [Supermemory](https://github.com/supermemoryai/supermemory) latest — see [[supermemory-analysis]] for structural details. The framework is named "MemoryBench" in the README (§"Benchmarks" block). Invocation is documented under "Benchmarking your own memory solution": `npx skills add supermemoryai/memorybench`. Supports Supermemory, Mem0, Zep, and "others" as provider arguments. Delivered in two forms: (a) as a Bun CLI runnable from the repo (rigorous, scriptable), (b) as an agent skill installable into any MCP-compatible harness (casual, discoverable). The framework is explicitly framed as an auditable eval layer for the memory-provider ecosystem, not just a Supermemory marketing surface.

Cross-links to [[retraction-log-as-governance-artifact]]: MemPalace's `docs/HISTORY.md` retracts a previous table that mixed retrieval recall with QA accuracy across providers — the kind of error a competitor-inclusive framework with a declared judge model prevents at write time.

## Potential Alternatives

- **Self-reported numbers on a product page.** Easy to publish, easy to drift, easy to dispute. Standard industry practice; weakest trust signal.
- **Closed leaderboard controlled by the publisher.** Better than self-reporting; still publisher-dominated. Competitors can be excluded, re-tested on favorable configs, etc.
- **Third-party leaderboards.** REM Labs for memory, LMSYS for LLMs. Independent of any one provider; slow to update, coverage gaps.
- **Academic benchmarks only.** UC Santa Barbara's LongMemEval, Salesforce's ConvoMem. Rigorous; not provider-agnostic by default.
- **Blog-post comparisons.** Publisher writes "we beat X, Y, Z." Opinion, not measurement. No reproducibility.

## Potential Improvements

- **Pin the judge model version** and rotate it on a published cadence. If the judge is "gpt-4o" and OpenAI silently changes behavior, historical comparisons break. Version-pinning + scheduled re-runs maintain integrity.
- **Community-contributed providers.** Open the provider-adapter interface for community PRs. New providers add themselves; framework author reviews for conformance.
- **Held-out splits per benchmark.** Combine with [[tool-enforced-dev-heldout-split]] — the framework itself enforces dev/held-out splits so providers can't over-iterate against published prompts.
- **Publish per-question result JSONLs** (MemPalace's BENCHMARKS.md pattern) so readers can inspect individual cases.

## Potential Failure Modes

- **Provider-adapter bias.** A provider might be implemented suboptimally in the framework's adapter (vs optimally on their own infra). The adapter becomes a source of benchmark noise. Mitigation: provider authors submit their own adapters; framework author reviews.
- **Judge-model drift.** If the judge is "gpt-4o," its behavior changes over time; historical comparisons across provider updates are contaminated by judge drift. Mitigation: version-pinning and scheduled re-runs.
- **Competitive-weaponization.** A competitor sees the framework, hand-tunes against its specific questions, publishes a PR tuning "their" adapter. Framework now scores their tuned version against the publisher's baseline. Mitigation: held-out splits + independent-run discipline.
- **Coverage gaming.** Framework supports 5 benchmarks; a provider that specializes in a different dimension doesn't score well on any of them. Looks weak on the dashboard even though they're strong in their actual use case. Mitigation: broaden benchmark coverage; surface dimension-by-dimension results, not aggregate scores.
- **Trust costs on the publisher.** Publishing the framework commits you to transparency even when your numbers dip. A competitor beats you on one benchmark — your own framework surfaces that. Short-term reputational pain; pattern depends on you trusting the long-game.
