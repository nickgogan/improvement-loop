---
title: "Pipeline Rules — IL Governance"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-19"
updated: "2026-04-22"
author: "agent"
source_governance:
  - "systems/meta-system/governance/constitution.md"
  - "systems/meta-system/governance/principles.md"
source_sections:
  - "Design Philosophy"
  - "The Pipeline"
  - "The Feedback Loop"
  - "DD-90 (session telemetry)"
tags:
  - "governance"
  - "improvement-loop"
  - "pipeline"
  - "human-gate"
  - "telemetry"
---

# Pipeline Rules — IL Governance

> Derived from: Constitution (`systems/meta-system/governance/constitution.md`), Principles (`systems/meta-system/governance/principles.md`), DD-90 (session telemetry)
> Last reconciled: 2026-04-22

## Rules

1. **Human gate at every stage boundary.** The IL pipeline has four stages: Research Intake, Identification, Extraction, Deployment. No artifact crosses a stage boundary without human review. Specifically: Researcher outputs are reviewed before Codifier processes them; Codifier outputs are reviewed before deployment.
   - *Source:* Constitution — Design Philosophy ("Spec before build"); DD-29

2. **Stage before deploying.** Extracted artifacts (patterns, rules, templates, skills, agents) stage in `extracts/` before deployment to enforcement locations in `meta-system/knowledge/` or `.claude/`. Nick owns the deployment step.
   - *Source:* Constitution — Design Philosophy; DD-39, DD-80

3. **Spec before build.** New skills, agents, or structural changes require a specification (proposal, skill definition, or agent constitution) before implementation. The Owner produces specs; Nick approves them.
   - *Source:* Constitution — Design Philosophy ("Spec before build"); Principles — DBDO Pipeline steps 3-4

4. **Handoffs are file-mediated.** Agents do not communicate directly in conversation. The Researcher writes findings with `pipeline_status: raw`. The Codifier reads findings with `pipeline_status` indicating readiness. The handoff is the file state, not a message.
   - *Source:* Principles — DBDO Pipeline; `agents/il-agent-handoff-protocol.md`

5. **System evolution via periodic research, not ad-hoc.** Changes to the IL system flow through the structured pipeline (research → identify → extract → deploy). Exception: on-demand research via `/research-query` (DD-83) and Owner-initiated structural proposals.
   - *Source:* Constitution — Design Philosophy; DD-36

6. **Learn and improve every cycle.** Every research scan, every audit, every feedback triage produces learnings. SL entries capture events. The Owner detects patterns. The pipeline should get faster and more accurate over time.
   - *Source:* Principles — DBDO Pipeline step 6 ("Learn and Improve")

7. **SL entries carry session telemetry.** Every SL entry written at session close includes a `telemetry:` block with these fields: `model`, `tokens_consumed`, `context_window_size`, `context_window_pct_peak`, `turns`, `tool_calls`, `subagents[]`, `capture_quality` (`measured` / `estimated`), and `harness`. `"unknown"` is a first-class value when a field is neither measurable nor reasonably estimable — entries are not held back waiting for unknown data. Nick is not a telemetry source. When evaluating a harness substitution, the prior harness's capture-layer disclosures become the baseline against which the candidate's observability is judged.
   - *Source:* DD-90 (session telemetry) — requirement layer (harness-portable) + capture layer (harness-specific)

## Applicability Notes

These rules govern the flow of work through the IL system. The Researcher owns Stage 1, the Codifier owns Stages 2-3, and Nick owns Stage 4. The Owner oversees pipeline health but does not execute pipeline stages — the Owner is a steward, not a participant in the research pipeline. Rule 7 (telemetry) applies to every agent disposition at session close — whoever is authoring the SL entry populates the `telemetry:` block.
