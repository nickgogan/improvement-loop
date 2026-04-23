---
name: "Session 58 Delta Report — Researcher Backlog Sweep (Partial): Buckets A + B Complete"
session: 58
date: "2026-04-23"
actor: "Claude (Researcher disposition)"
type: "research-report"
target_system:
  - "improvement-loop"
tags:
  - "delta-report"
  - "backlog-sweep"
  - "researcher"
  - "session-58"
---

# Session 58 Delta Report — Researcher Backlog Sweep

## Scope as Run

Planned: four-bucket sweep (A carry-forward sources, B LongMemEval cluster, C Still Deferred locates, D MemoryBench evaluation).

Actual: Buckets A and B closed cleanly. Buckets C and D deferred to session 59+ at context-budget breakpoint (user-initiated stop at ~40% context window utilization). Delta-report-first close discipline per handoff requirements.

## Sources Processed

### Bucket B — LongMemEval cluster (6 sources)

1. `research-sources/arxiv-longmemeval-wu-et-al-2024.md` — UC Santa Barbara team's canonical paper (CC BY 4.0).
2. `research-sources/huggingface-longmemeval-dataset.md` — dataset distribution; flagged as deprecated in favor of longmemeval-cleaned.
3. `research-sources/rem-labs-benchmarks-aggregator.md` — most-referenced third-party leaderboard; captured composition shift since session 56 snapshot (MemPalace no longer listed).
4. `research-sources/vectorize-mempalace-benchmarks-article.md` — third-party adjudication surfacing feature-disabled-baseline and metric-mismatch issues.
5. `research-sources/supermemory-research-page.md` — ~85% production-configuration result.
6. `research-sources/supermemory-99-sota-blog.md` — ~99% experimental ASMR sandbox; documents union-of-successes aggregation.

`mempalace.tech` intentionally skipped as confirmed scam-domain per session 57's correction.

### Bucket A — Session-45 carry-forward sources (8 sources)

1. `research-sources/simon-willison-subagents-chapter.md` — processed; content largely captured by Anthropic canonical docs.
2. `research-sources/simon-willison-anti-patterns.md` — one anti-pattern (unreviewed-code-inflicted-on-collaborators); covered by existing KB findings.
3. `research-sources/simon-willison-hoard-things.md` — high-yield chapter; one finding promoted.
4. `research-sources/simon-willison-red-green-tdd.md` — high-yield chapter; one finding promoted.
5. `research-sources/simon-willison-first-run-the-tests.md` — minor pattern; covered by existing test-first findings.
6. `research-sources/simon-willison-interactive-explanations.md` — high-yield chapter; one finding promoted.
7. `research-sources/anthropic-claude-code-subagents-docs.md` — canonical Anthropic docs; six findings promoted.
8. `research-sources/nate-jones-five-layers-ai-cannot-replace.md` — batch-1 deferred video `ib2m9HVX7as`, existing transcript identified as Nate B. Jones' "5 Layers AI Cannot Replace"; two findings promoted.

## Authorities Added (3)

1. `research-authorities/uc-santa-barbara-longmemeval-team.md` — Tier 1 institution (Wu, Wang, Yu, Zhang, Chang, Yu).
2. `research-authorities/rem-labs.md` — Tier 3 vendor with disclosed conflict-of-interest.
3. `research-authorities/vectorize.md` — Tier 3 vendor (Hindsight developers), critiquing competitor benchmarks.

## Findings Promoted (16 total)

### Bucket B — Memory / Benchmarking / Governance (6)

1. `external-benchmark-hosting-as-trust-mechanism.md` — REM Labs / benchlist.ai pattern.
2. `benchmark-dataset-deprecation-lifecycle.md` — HuggingFace longmemeval → longmemeval-cleaned.
3. `experimental-sandbox-labeling-discipline.md` — Supermemory ASMR labeling.
4. `ensemble-eval-majority-required-for-success.md` — union-of-successes anti-pattern, positive frame.
5. `production-configuration-baseline-discipline.md` — MemPalace 12.4pp feature-disabled gap.
6. `agentic-search-memory-retrieval-architecture.md` — 4th architectural pole in memory design space (complements verbatim / single-store / triple-store).

### Bucket A — Simon Willison chapters (3)

7. `confirm-failure-first-tdd-agent-discipline.md` — red-verification non-negotiable for agents.
8. `personal-knowledge-hoard-as-agent-substrate.md` — distributed personal corpus as AI recombination substrate.
9. `interactive-explanations-extend-linear-walkthroughs.md` — companion documentation pattern.

### Bucket A — Anthropic subagent canonical docs (6)

10. `subagent-scope-priority-ladder.md` — 5-level override resolution.
11. `inline-scoped-mcp-servers-per-subagent.md` — token-cost-bounded MCP scoping.
12. `subagent-persistent-memory-directory.md` — ~/.claude/agent-memory with auto-curation.
13. `capability-restricted-agent-spawning-via-allowlist.md` — Agent(agent_type) syntax.
14. `subagent-isolation-contract.md` — fresh context, explicit skills, no nesting.
15. `foreground-vs-background-subagent-permission-models.md` — upfront vs pass-through.

### Bucket A — Nate B. Jones video (2)

16. `five-durable-verticals-ai-cannot-replace.md` — Trust / Context / Distribution / Taste / Liability strategic framework.
17. `agent-native-app-store-emerging-category.md` — emerging distribution category thesis.

**Count correction:** 17 findings promoted in total (Bucket B = 6, Bucket A = 11 per count above).

## Reciprocal Link Updates

Applied reciprocal `related_findings` entries to the following existing findings:

**From Bucket B's cross-links:**
- `retraction-log-as-governance-artifact.md` — 4 new reciprocal links.
- `tool-enforced-dev-heldout-split.md` — 5 new.
- `benchmark-operating-contract.md` — 3 new.
- `cross-provider-benchmarking-framework.md` — 2 new (external-benchmark-hosting + agent-native-app-store).
- `verbatim-storage-thesis-for-memory.md` — 2 new.
- `triple-storage-memory-architecture.md` — 1 new.
- `mongodb-single-store-polymorphic-evidence-memory.md` — 2 new.
- `typed-relationship-memory-graph.md` — 1 new.
- `query-decomposition-sub-query-rrf-merge.md` — 1 new.
- `independent-convergence-retrieval-ceiling.md` — 1 new.

**From Bucket A's cross-links:**
- `agent-generated-codebase-walkthrough-for-onboarding.md` — 1 new (interactive-explanations extended-by).
- `agent-architecture-layer-impermanence.md` — 1 new (subagent-isolation-contract).
- `six-layer-agent-infrastructure-stack.md` — 1 new (five-durable-verticals).
- `agent-management-tool-landscape-2026.md` — 1 new (agent-native-app-store).

Plus internal cross-links among the 17 new findings (captured at promotion time).

## Index Updates

- `research-findings/_index.md` — two session-58 append blocks (Bucket B, Bucket A).
- `research-sources/_index.md` — two session-58 append blocks.
- `research-authorities/_index.md` — one session-58 append block (3 new rows).

## Deferred to Session 59+

### Bucket C — Still Deferred list (not completed)

13 locate-only items documented in `next-scan-notes.md` under "Still Deferred — carry forward to session 59":
- Playwright DOM selector update
- Dark Code channel identity
- Agentic OS dimension registry update
- Nate B Jones agentic harness skill (download + evaluate)
- Claude Code leaked source
- Token budget pre-turn projection implementations
- Superpowers + GSD tension resolution
- Garry Tan direct commentary on gstack
- Stripe Projects for agent billing
- E2B vs Daytona sandbox comparison
- Obsidian Web Clipper + Local Images Plus
- Video 4 misattribution
- /usage slash command canonical doc (session-58 deferred with reason)

### Bucket D — MemoryBench evaluation run

Standalone-scope item requiring environment setup (bun, framework clone). Deferred as a separate session.

### Low-yield Simon Willison chapters

8 chapters deprioritized (definitional / opinion / project-specific); catalog in `next-scan-notes.md`.

## Observations

### What went well

- **Plain-English-first framing** (per `feedback_findings_plain_english.md`) applied consistently across all 17 findings — every summary leads with "why it matters for us" or an everyday-English reformulation before technical framing.
- **Positive-space governance** (per `feedback_positive_space_governance.md`) applied to Bucket B findings that could have been written as rejection lists: production-configuration-baseline-discipline, ensemble-eval-majority-required-for-success, experimental-sandbox-labeling-discipline are all positive invariants.
- **No new file types, frontmatter fields, status enums, or directory conventions introduced.** Surface-before-shaping discipline honored; every finding uses existing frontmatter shape. No escalation to Nick required.
- **Scam-domain discipline honored** (carried from session 57): mempalace.tech intentionally skipped across every Bucket B operation.
- **Dedup check rigor**: 17 findings promoted with no near-duplicates against existing KB content. Cross-links made all new findings discoverable from the existing memory-architecture and governance clusters.
- **Leaderboard volatility captured**: REM Labs snapshot shift between session 56 and session 58 (~3 weeks) was not predicted in session 57's scope; this session documented it as evidence for the benchmark-hosting finding.

### What could have gone better

- **Context budget breakpoint at ~40% was earlier than hoped** — Bucket A's depth (especially Anthropic's 900-line subagent docs) consumed more context than session 57's intake cadence. Hit-rate for Bucket A findings was high (11 from 8 sources) but context cost per source was also high.
- **Read-before-edit hook fires false positives across the session.** Every `_index.md` edit, every edit on a file read earlier via Bash (awk/grep) fired warnings despite Read tool confirming the content. The edits all succeeded; the warning cadence is noise that doesn't reflect actual compliance. Reported in session 57 SL; confirmed persistent in session 58.
- **`/usage` slash command not locatable** despite directed search of code.claude.com/docs. Either a release-notes-only command or an unreleased feature referenced prematurely in the session-management blog. Could represent a low-signal carry-forward item worth periodic re-check.

### Help Researcher could use

- **A context-budget estimator for the research-loop skill.** "This source is ~50KB of transcript + likely 4 findings at ~5KB each = ~30-40% of a 1M context per source" would have let me plan Bucket A/B/C/D allocation more realistically up front. Today the estimation is intuitive.
- **Source-triage skill applied to remaining backlog.** Bucket C's 13 items would benefit from `/source-triage` pre-screening to separate "5-minute locate" items from "genuinely dead / skip" items before investing in full research-loop on each.
- **Dedicated handoff for Bucket D.** MemoryBench is a 1-session-scope item (env setup, benchmark runs, report). Carries cleanly as its own future session rather than mixing with locate sweeps.
