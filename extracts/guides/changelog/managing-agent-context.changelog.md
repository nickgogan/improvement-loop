# Changelog — Managing Agent Context

## 2026-05-25 — Session 104 — guide-split

- Findings: 64 (final; guide deprecated)
- Structural: Guide bifurcated into G2a (`structuring-agent-context`, 34 findings) and G2b (`defending-agent-context`, 29 findings), plus 1 shared (`bounded-tiered-memory-inference-driven-curation`). Split proposal at `operations/split-proposals/2026-05-24-managing-agent-context-split-proposal.md`. Source guide deprecated; routing table updated to point at G2a + G2b.
- Preserved: none
- SL: [[session-104-owner-g2-bifurcation]]

## 2026-05-25 — Session 97 — staleness-threshold

- Findings: 64 (+16, -0 since last synthesis)
- Added: [[claude-code-context-management-decision-matrix-five-tools]], [[proactive-compaction-before-intelligence-degradation]], [[inline-scoped-mcp-servers-per-subagent]], [[token-economics-as-architecture-driver]], [[agentic-rag-multi-strategy-retrieval-2026]], [[file-search-outperforms-rag-for-small-corpora]], [[hybrid-retrieval-pattern-semantic-lexical-graph]], [[summary-gate-agent-traversal-pattern]], [[personal-knowledge-hoard-as-agent-substrate]], [[ai-as-primary-reader-design-principle]], [[agent-memory-architecture-multi-agent-layered]], [[html-output-as-human-in-the-loop-restorer]], [[format-constrained-improvisation-tax]], [[interactive-explanations-extend-linear-walkthroughs]], [[output-format-token-cost-reframed-by-context-window-size]], [[environment-grounded-context-as-output-quality-multiplier]]
- Structural: Added Step 9 (Engineer Your Output Format, 4 sub-steps); Step 4e restructured as Anthropic's canonical 5-tool decision matrix; Step 7 expanded with agentic RAG, summary-gate, personal knowledge hoards; Step 8g added multi-agent shared memory architecture; Key Concepts 8-10; Pitfalls 18-20; 1 new template (Output Format Decision).
- Preserved: none
- SL: [[session-97-codifier-guide-resynthesis]]

## 2026-05-24 — Session 93 — staleness-threshold

- Findings: 48 (+4, -0 since last synthesis)
- Added: [[bounded-tiered-memory-inference-driven-curation]], [[session-tree-as-first-class-abstraction]], [[write-time-vs-query-time-synthesis-kb-poisoning]], [[orchestrator-headless-dispatch-context-isolation]]
- Structural: Added Step 3f (hard ceilings on memory files, hot/warm/cold tiering, Curator step); Step 4g (session-as-tree model, branching/compaction/navigation/labels); Step 5 defense #7 (headless subprocess dispatch for rot prevention at process level, renumbering prior #7 to #8); Step 7a (KB poisoning, query-time vs write-time synthesis, three integrity principles). Added Key Concept #7 (LLM-authored KB contamination). Added Pitfalls #16 (KB re-indexing contamination) and #17 (unbounded memory files). Expanded "When to Use" with 3 new trigger conditions. Context Audit Checklist extended with 4 new Rot Defense checks.
- Preserved: none
- SL: [[session-93-codifier-synthesize-guides]]

## 2026-04-26 — Session 78 — staleness-threshold

- Findings: 44 (+18, -0 since last synthesis)
- Added: [[five-context-management-techniques-in-claude-code]], [[progressive-tiered-context-loading-convergence]], [[catastrophic-context-collapse-risk-during-claudemd]], [[claudemd-context-rot-from-indiscriminate-rule-accu]], [[context-file-taxonomy-claudemd-soulmd-agentsmd]], [[cross-platform-context-file-strategy]], [[global-vs-project-level-skill-and-context]], [[model-native-context-window-awareness]], [[monorepo-context-distribution-three-strategies]], [[progressive-skill-loading]], [[self-describing-codebase-structural-semantic-context]], [[session-atomicity-single-issue-scope-quadratic-cost-reduction]], [[three-layer-folder-as-workspace-architecture]], [[three-tier-progressive-context-loading]], [[three-tier-vault-architecture-global-shared-local]], [[progress-md-session-bridge]], [[skills-as-pointers-to-second-brain-files]], [[trajectory-engineering-non-linear-session-forking]]
- Structural: Added Step 8 (Architect Context Across Tools, Tiers, and Sessions; 6 sub-steps: vault tiering, folder-as-workspace, skill scoping, cross-platform portability, monorepo distribution, PROGRESS.md bridge). 2 new templates (Module Manifest; Multi-Tool Context Mirror Map). 4 new pitfalls (#12-15: CLAUDE.md self-compaction collapse, monorepo single-file scaling, skill embedded copies, multi-tool drift). Step 3 +2 sub-steps (content-granularity L0/L1/L2 tiers; progressive skill loading). Step 4 +3 sub-steps (technique-selector preference order; /re trajectory engineering; harness+model layered awareness). Step 5 +2 defenses (atomic session scoping; never let Claude compact CLAUDE.md). Key Concepts 5 → 6.
- Preserved: none
- SL: [[session-78-codifier-g2-re-synthesis]]

## 2026-04-19 — Session 44 — initial-synthesis

- Findings: 26
- Structural: initial synthesis; no prior version
- Preserved: none
- SL: [[session-44-codifier-extraction-run]]
