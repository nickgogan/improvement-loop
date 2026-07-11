# Delta Report — 2026-07-11 (Session 131 Research Sweep, Extraction Pass)

## Scan Summary
- **Mode:** targeted extraction pass over the queued sources from the two 2026-07-11 link-intake triage runs — not a dimension scan. Plus one narrow intake (Anthropic RSI essay stats) executed for the model-capability-registry refresh.
- **Sources processed:** the 8 queued `Not started` entries (3 arXiv papers, Osmani/Google SDLC whitepaper, Claude Code prompt-caching post, thermo-nuclear skill exemplar, ast-grep outline post, MemoryDemo) + 1 narrow-intake source (RSI essay).
- **New findings:** see table below (all dated 2026-07-11; filter `date_discovered: "2026-07-11"` for the authoritative list).
- **Existing findings updated:** 8 (evidence corroboration, crosslinks, reference implementations).
- **Previous report:** `2026-07-11-link-intake-triage-run2.md` (triage, same date); last delta-style report predates the triage protocol.

## New Findings

| Finding | Category | Priority | Evidence |
|---|---|---|---|
| `append-only-context-updates-system-reminder-injection` | Context Engineering | P2 | Strong (first-party production) |
| `no-mid-session-model-switching-subagent-handoff` | Model Selection | P2 | Strong (first-party production) |
| `static-tool-set-mode-changes-as-callable-tools` | Tool Integration | P2 | Strong (first-party production) |
| `cache-safe-compaction-forked-prefix-buffer` | Context Engineering | P2 | Strong (first-party production) |
| `cache-hit-rate-as-slo` | Agentic Systems | P3 | Strong (first-party production) |
| `attention-closure-goal-accessibility-collapse` | Context Engineering | P2 | Medium (empirical benchmarks) |
| `windowed-attention-parametric-failure-timing` | Context Engineering | P3 | Medium (empirical benchmarks) |
| `skill-library-drift-failure-mode` | Governance | P2 | Medium (empirical benchmarks) |
| `ratchet-recipe-skill-retirement` | Governance | P2 | Medium (empirical benchmarks) |
| `meta-skill-authoring-prior-dominance` | Agent Design | P2 | Medium (empirical benchmarks) |
| `per-skill-contribution-scoring-telemetry` | Evaluation | P3 | Medium (empirical benchmarks) |
| `strictness-escalation-skill-architecture` | Prompt Craft | P2 | Medium (practitioner-documented) |
| `code-judo-review-posture` | Agent Design | P2 | Medium (practitioner-documented) |
| `context-partition-as-versioned-architectural-decision` | Governance | P2 | Medium (practitioner-documented) |
| `dual-verification-trajectory-vs-output-correctness` | Evaluation | P2 | Medium (practitioner-documented) |
| `conductor-vs-orchestrator-operating-modes` | Orchestration | P3 | Medium (practitioner-documented) |
| `structural-outline-before-read-agent-navigation` | Context Engineering | P2 | Medium — **Partially Adopted** (session-130 `/repo-analyzer` ENHANCE) |
| `index-free-local-code-intelligence-parallel-worktrees` | Tool Integration | P3 | Medium (practitioner-documented) |
| `four-module-agent-memory-decomposition` | Context Engineering | P3 | Medium (empirical benchmarks) |
| `no-single-memory-architecture-workload-alignment` | Context Engineering | P3 | Medium (empirical benchmarks) |
| `localized-memory-maintenance-over-global-reorganization` | Context Engineering | P3 | Medium (empirical benchmarks) |
| `typed-shared-memory-handoff-slots` | Context Engineering | P3 | Weak (single-author demo — cite only if corroborated) |
| `anthropic-first-party-capability-trend-stats` | Model Selection | P3 | Medium (first-party, self-reported) |

## Updated Findings

| Finding | What changed |
|---|---|
| `skill-invocation-control-side-effect-guard` (P1) | Second use case: `disable-model-invocation: true` for intentionally harsh opt-in modes, not just side-effect workflows |
| `gpt-54-tool-search-deferred-tool-loading` (P1) | Claude Code `defer_loading`-stub production corroboration added — now three independent instances (OpenAI, Anthropic API, Claude Code). Already Strong; triage's conditional evidence upgrade didn't fire |
| `context-rot-attention-budget-depletion` | Reciprocal `extended-by` crosslink to attention-closure finding (the queued crosslink) |
| `prompt-cache-stability-as-correctness` | Reciprocal link to append-only-context-updates |
| `converged-memory-substrate-vs-patchwork` | MemoryDemo added as weak-evidence five-type single-stack reference implementation |
| `four-layer-agent-evaluation-architecture` | Bidirectional `same-problem` link to dual-verification (trajectory axis is parallel, not an extension) |
| `worktree-isolation-for-parallel-agent-sessions` | `enabled-by` link toward index-free code intelligence |
| `frontier-release-compression-march-2026` | `same-problem` link to the first-party capability-trend stats |

## Already Captured
Osmani/Google whitepaper's harness 10/90, progressive disclosure, and complexity-based model routing (existing findings left untouched — article restates without new evidence); basic stable-context prompt caching; static-first prompt layering (folded into append-only finding; pattern-level duplicate of `layered-prompt-assembly-stable-segment-caching`).

## Corrections to Triage Premises

1. **Re-injection countermeasure does not survive the paper.** Triage takeaway for arXiv 2605.12922 said periodic re-injection/re-anchoring "restores" goal accessibility. The paper's Appendix H reports periodic user-role goal re-injection as an explicit **negative result** ("repeating or retaining text is not equivalent to preserving goal information"; one scheme tested). Recorded inside the closure finding. **Flag for Nick:** practitioner lore commonly recommends exactly this failed remedy — our own re-anchoring habits may warrant a look once corroborating work appears.
2. **`disable-model-invocation` was not novel** — already canonical in `skill-invocation-control-side-effect-guard`; folded as a second use case rather than duplicated.
3. **ast-grep headline range is narrower than triaged:** "35–55%" is cost reduction on the three large repos; Tokio showed 38% *more* tokens yet 12% cheaper; small repos went costlier. Per-repo numbers recorded in the finding.

## Recommendations

### Priority 1 (existing P1s strengthened)
- `gpt-54-tool-search-deferred-tool-loading` — three independent production instances; deferred-loading stubs are now the best-evidenced tool-scaling pattern in the KB.

### Priority 2 (for `/identify-artifacts` when next run)
- The five first-party prompt-caching mechanics (cluster) — direct harness-usage guidance; `no-mid-session-model-switching` feeds skill↔model-coupling metadata (agentic-OS direction).
- `skill-library-drift-failure-mode` + `ratchet-recipe-skill-retirement` + `meta-skill-authoring-prior-dominance` — candidate governance input for the engine's own roster lifecycle and the evals-for-skills thread; the meta-skill result (authoring prior = 57% of gain) is empirical backing for the `/design-skill` template bet.
- `dual-verification-trajectory-vs-output-correctness` — missing eval axis; relevant to `/assess-*` criteria design.
- `context-partition-as-versioned-architectural-decision` — candidate DD-style practice for the engine's own context files.

### Priority 3 (Monitor)
- Memory-survey trio (four-module decomposition, workload alignment, localized maintenance) — comparative 1.C substrate; `verbatim-storage-thesis-for-memory` may deserve an evidence bump at next `/reassess-priorities` (independently corroborated by the survey's RQ1).
- `typed-shared-memory-handoff-slots` — weak evidence; watch for corroboration.

## Dimension Gaps
None. All findings fit registered dimensions/sub-dimensions (1.C absorbed the memory trio; 11.A untouched this pass).

## Evaluation Handoff
None this pass — extraction only; no prompt/config changes proposed.
