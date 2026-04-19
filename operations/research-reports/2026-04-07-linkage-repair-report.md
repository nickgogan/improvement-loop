---
name: Linkage Repair Report
date: "2026-04-07"
type: repair-report
---

# Linkage Repair Report — 2026-04-07

## Pre-Repair State
| Metric | Count |
|--------|-------|
| Total sources | 73 |
| Total findings | 220 |
| Orphaned findings (sources: []) | 25 |
| Unlinked sources (findings: []) | 32 |
| Asymmetric links | 12 |
| Sources with only Notion refs | 25 |
| Findings with only Notion refs | 108 |

## Repairs Executed

### Category A: Notion URL → Filename Resolution
- **71** source→finding Notion URLs resolved to filenames (across 24 sources)
- **71** finding→source Notion URLs resolved to filenames (across 68 findings)
- 30 source→finding Notion refs unresolvable (finding not in KB or no notion_id)
- 46 finding→source Notion refs unresolvable (source not in KB or no notion_id)

### Category B: Known Fixes + HIGH-Confidence Content Matches (15 pairs)
All 8 handoff-documented fixes applied:
1. `tool-shaped-objects.md` ↔ `tool-shaped-object-evaluation-lens.md`
2. `agentic-context-engineering-ace-iclr-2026-poster.md` ↔ `ace-agentic-context-engineering-evolving-playbook.md`
3. `agentic-context-engineering-ace-iclr-2026-poster.md` ↔ `ace-agentic-context-engineering-rag-based.md`
4. `artist-agentic-reasoning-and-tool-integration-via.md` ↔ `rl-trained-autonomous-tool-selection-artist-pattern.md`
5. `introducing-gpt-54-openai.md` ↔ `gpt-54-tool-search-deferred-tool-loading.md`
6. `google-a2a-protocol-guide-digital-applied.md` ↔ `google-a2a-protocol-agent-to-agent-interoperabilit.md`
7. `human-on-the-loop-ai-hotl-torry-harris.md` ↔ `human-on-the-loop-hotl-autonomy-tiering-framework.md`
8. `intent-engineering-pathmode-glossary.md` ↔ `intent-engineering-framework-seven-part-agent-inten.md`

Plus 7 HIGH-confidence content matches:
9. `openclaude-build-a-claude-code-agent-with-long-ter.md` ↔ `claude-code-long-term-memory-via-pre-prompt-recall.md`
10. `how-to-build-self-improving-ai-skills-with-binary.md` ↔ `claude-code-skills-20-four-mode-skill-lifecycle-wi.md`
11. `4-layer-memory-stack-for-2026-enterprise-agents-al.md` ↔ `four-layer-enterprise-memory-stack.md`
12. `intent-engineering-framework-for-ai-agents-product.md` ↔ `intent-engineering-framework-seven-part-agent-inten.md`
13. `prompting-after-feb-2026-prompt-craft-context-inten.md` ↔ `spec-first-agent-briefs-prompt-craft-context-inten.md`
14. `llm-benchmark-2026-38-actual-tasks-ian-l-paterson.md` ↔ `task-specific-model-routing-table-march-2026-bench.md`
15. `intent-engineering-framework-for-ai-agents-product.md` ↔ `spec-first-agent-briefs-prompt-craft-context-inten.md`

### Category C: MEDIUM-Confidence Content Matches (4 pairs)
1. `every-ai-prompting-technique-that-works-on-reasoni.md` ↔ `emergent-internal-self-debate-reasoning-models-spo.md`
2. `agent-orchestrators-are-bad.md` ↔ `l-d-hypothesis-information-loss-across-agent-bound.md`
3. `ai-agent-prompt-engineering-best-practices-inflect.md` ↔ `prompt-as-policy-version-control-and-cicd-for-agen.md`
4. `every-ai-prompting-technique-that-works-on-reasoni.md` ↔ `reasoning-model-anti-pattern-prescribed-reasoning.md`

### Category D: Asymmetric Link Fixes
- **12** asymmetric links repaired (all were finding→source present, source→finding missing)

## Post-Repair State
| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Sources with filename-based findings | ~16 | 56 | +40 |
| Sources with only Notion refs | 25 | 1 | -24 |
| Sources with zero findings | 32 | 16 | -16 |
| Findings with filename-based sources | ~87 | 168 | +81 |
| Findings with only Notion refs | 108 | 43 | -65 |
| Findings with zero sources | 25 | 9 | -16 |
| Asymmetric links (filename) | 12 | 0 | -12 |

## Remaining Issues

### Unresolvable Notion References
- 30 source→finding Notion URLs point to Notion IDs with no matching `notion_id` in any finding file (likely pre-migration findings that were deleted or consolidated)
- 46 finding→source Notion URLs point to Notion IDs with no matching `notion_id` in any source file (likely pre-migration sources that were consolidated)

### Remaining Orphaned Findings (9)
These findings have `sources: []` and no confident match was found:
1. `claude-code-auto-mode-ai-driven-permission-classif.md` — likely from Perplexity search
2. `claude-code-loop-in-session-cron-scheduling.md` — likely from Perplexity search
3. `context-aware-routing-skill-classifier-sub-skill.md` — LOW match only
4. `context-enrichment-for-task-clarity.md` — LOW match only
5. `domain-specific-intelligence-from-historical-busi.md` — LOW match only
6. `fundamental-limits-of-single-vector-embedding-retr.md` — no match
7. `iterative-refinement-loop-with-quality-gate.md` — LOW match only
8. `skill-as-new-employee-mental-model.md` — LOW match only
9. `transformer-functional-anatomy-layer-circuit-archi.md` — no match

### Remaining Unlinked Sources (16)
These sources have `findings: []` post-repair — they need extraction (Goal 2 addresses most of these):
Tier 1/2 extraction targets, plus: `cursor-ai-mcp-server-configuration-setup-auth-best.md`, `deepeval-mcp-evaluation-quickstart.md`, `gemini-vs-gpt-vs-claude-benchmark-comparison-lorka.md`, `hitl-agentic-ai-strataio-2026-guide.md`, `openai-self-evolving-agents-cookbook.md`, `prompting-best-practices-nick-gogan.md`

## Files Modified
129 files across research-sources/ and research-findings/
