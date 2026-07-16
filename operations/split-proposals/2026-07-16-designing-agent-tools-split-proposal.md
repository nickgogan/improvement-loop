---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-07-16"
source_guide: "designing-agent-tools"
finding_count: 37
practitioner_question_count: 2
session: 147
sl: "session-147 (SL retired as producer per session-138 ruling; git is the session record)"
---

# Split Proposal — Designing Agent Tools

## Source guide identity

- **Guide stem:** `designing-agent-tools`
- **Current title:** "Designing Agent Tools"
- **Finding count:** 37 (post-resolution; ≥25)
- **Routing-table row:** G5 in `operations/references/guide-routing-table.md`

## Practitioner-question analysis

The source cluster covers 2 distinct practitioner questions:

1. **Q1:** "How do I design and integrate tools that agents invoke correctly and efficiently?"
   - Core concern: the non-deterministic contract, registries and capability tiers, poka-yoke interfaces, discovery/loading and cache-stable surfaces, transport choice (CLI/MCP/headless), multi-tool orchestration, background watching, output design, middleware/hooks, infrastructure economics, pruning.
   - Findings clustering against Q1: [[gpt-54-tool-search-deferred-tool-loading]], [[mcp-as-code-api-progressive-tool-discovery]], [[poka-yoke-error-proof-tool-interfaces]], [[programmatic-tool-calling-code-orchestrated-tool-use]], [[tool-registry-metadata-first-design]], [[think-tool-scratchpad-for-mid-chain-reasoning]], [[anthropic-managed-agents-platform]], [[tool-use-examples-sample-calls-in-definitions]], [[non-deterministic-tool-contract-model]], [[sdk-vs-framework-decision-for-agent-building]], [[mcp-ecosystem-critical-mass-97m-installs]], [[gsd-queryable-codebase-intelligence-store]], [[search-over-list-tool-design-pattern]], [[tool-call-event-interception-pattern]], [[cli-first-tool-integration-less-overhead-than-mcp]], [[claude-p-headless-mode-as-openclaw-replacement]], [[cursor-claude-code-ide-composition]], [[html-pr-explainer-with-margin-annotations]], [[playwright-cli-for-browser-automation]], [[ide-first-claude-code-with-deterministic-hooks]], [[tiered-capability-registry-engine-behavior-branching]], [[stateful-mcp-subprocess-vs-cli-shell-out]], [[monitor-vs-loop-event-driven-vs-time-driven]], [[claude-code-monitor-tool-event-driven-background]], [[static-tool-set-mode-changes-as-callable-tools]], [[subscription-tos-single-user-boundary-for-agent-sdks]], [[html-artifact-as-skill-output-design-variations]], [[bun-hot-reload-interactive-html-artifact-feedback-loop]], [[mdx-visual-plans-with-reusable-components]]

2. **Q2:** "How do I package, distribute, and manage skills as the agent's capability layer?"
   - Core concern: skill wrapping, bundled scripts, lock-file dependency hygiene, workspace scoping, cross-framework and cross-surface portability, skill/MCP boundary.
   - Findings clustering against Q2: [[skill-as-script-wrapper-for-complex-pipelines]], [[skills-lock-portable-agent-skills]], [[skills-inside-workspace-contextual-skill]], [[skills-portability-across-sdk-and-framework-boundaries]], [[skill-cross-surface-portability-with-constraints]], [[code-as-deterministic-tool-inside-skills]]

## Proposed bifurcation

Destination guide names (working draft; per-split DD codifies finals):

- **Destination A:** `designing-agent-tools` — practitioner question: "How do I design and integrate tools that agents invoke correctly and efficiently?" (retains stem)
- **Destination B:** `building-and-managing-agent-skills` — practitioner question: "How do I package, distribute, and manage skills as the agent's capability layer?"

Per-finding routing (every finding routed; no implicit handling per DD-98 §Rules #4):

| Finding | Disposition |
|---------|-------------|
| [[gpt-54-tool-search-deferred-tool-loading]] | A |
| [[mcp-as-code-api-progressive-tool-discovery]] | A |
| [[poka-yoke-error-proof-tool-interfaces]] | A |
| [[programmatic-tool-calling-code-orchestrated-tool-use]] | A |
| [[tool-registry-metadata-first-design]] | A |
| [[think-tool-scratchpad-for-mid-chain-reasoning]] | A |
| [[anthropic-managed-agents-platform]] | A |
| [[tool-use-examples-sample-calls-in-definitions]] | A |
| [[non-deterministic-tool-contract-model]] | A |
| [[sdk-vs-framework-decision-for-agent-building]] | A |
| [[mcp-ecosystem-critical-mass-97m-installs]] | A |
| [[gsd-queryable-codebase-intelligence-store]] | A |
| [[search-over-list-tool-design-pattern]] | A |
| [[tool-call-event-interception-pattern]] | A |
| [[cli-first-tool-integration-less-overhead-than-mcp]] | A |
| [[claude-p-headless-mode-as-openclaw-replacement]] | A |
| [[cursor-claude-code-ide-composition]] | A |
| [[html-pr-explainer-with-margin-annotations]] | A |
| [[playwright-cli-for-browser-automation]] | A |
| [[ide-first-claude-code-with-deterministic-hooks]] | A |
| [[tiered-capability-registry-engine-behavior-branching]] | A |
| [[stateful-mcp-subprocess-vs-cli-shell-out]] | A |
| [[monitor-vs-loop-event-driven-vs-time-driven]] | A |
| [[claude-code-monitor-tool-event-driven-background]] | A |
| [[static-tool-set-mode-changes-as-callable-tools]] | A |
| [[subscription-tos-single-user-boundary-for-agent-sdks]] | A |
| [[html-artifact-as-skill-output-design-variations]] | A |
| [[bun-hot-reload-interactive-html-artifact-feedback-loop]] | A |
| [[mdx-visual-plans-with-reusable-components]] | A |
| [[skill-as-script-wrapper-for-complex-pipelines]] | B |
| [[skills-lock-portable-agent-skills]] | B |
| [[skills-inside-workspace-contextual-skill]] | B |
| [[skills-portability-across-sdk-and-framework-boundaries]] | B |
| [[skill-cross-surface-portability-with-constraints]] | B |
| [[code-as-deterministic-tool-inside-skills]] | B |
| [[skills-mcp-recipes-kitchen-complementarity]] | shared (route to both — defines the tool/skill boundary each destination needs) |
| [[tool-pruning-as-harness-maintenance]] | shared (route to both — explicitly covers tool surfaces and skill piles) |

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture.

## Routing-table impact

- **Source guide:** retains G5 identity and stem (Destination A); no deprecation needed if A keeps the stem.
- **New rows:**
  - `building-and-managing-agent-skills` — practitioner question: "How do I package, distribute, and manage skills as the agent's capability layer?", dimension: Tool Integration (skills sub-theme), stage: build, lifecycle stage = `draft`.
- **Dimension → Guide mapping changes:** Tools dimension would map to G5 (primary) + new skills guide (secondary) — the current "Clean 1:1 mapping" note would need revision. Trigger keywords: `skill authoring, skill distribution, skill portability, SKILL.md, bundled scripts, lock file, compatibility field` → new guide.

## Codifier recommendation

**Recommendation:** defer pending more findings

**Rationale:** Bifurcation is clean (94.6% single-destination, 2 shared, 0 contested), but Destination B is thin at 6 findings (+2 shared) and the split leaves Destination A at 31 findings — still over the ≥25 volume threshold, so the split does not resolve the source's volume condition. The skills sub-cluster is growing fast (3 of its 6 findings arrived since 2026-06-11 from the Anthropic skills-doc wave); re-evaluate at the next regen when B reaches ~10-12 findings, at which point the split pays for itself.

## Notes

The two shared findings are boundary-definers rather than routing failures: skills-mcp-recipes is the connectivity/knowledge distinction both guides must state, and tool-pruning explicitly names both tool and skill surfaces as its object. If the split executes, duplicate both by design.
