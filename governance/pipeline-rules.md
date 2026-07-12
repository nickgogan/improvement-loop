---
title: "Pipeline Rules — IL Governance"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-19"
updated: "2026-07-12"
author: "agent"
source_governance:
  - "CHARTER.md"
  - "systems/improvement-loop/knowledge/reference/dbdo-pipeline.md"
source_sections:
  - "Design Philosophy"
  - "The Pipeline"
  - "The Feedback Loop"
  - "DD-116 (session-ops spine)"
tags:
  - "governance"
  - "improvement-loop"
  - "pipeline"
  - "human-gate"
  - "telemetry"
---

# Pipeline Rules — IL Governance

> Derived from: Charter (`CHARTER.md`), DBDO Pipeline (`systems/improvement-loop/knowledge/reference/dbdo-pipeline.md`), DD-116 (session-ops spine)
> Last reconciled: 2026-07-12

## Rules

1. **Human gate at every stage boundary.** The IL pipeline has four stages: Research Intake, Identification, Extraction, Deployment. No artifact crosses a stage boundary without human review. Specifically: Researcher outputs are reviewed before Codifier processes them; Codifier outputs are reviewed before deployment.
   - *Source:* Constitution — Design Philosophy ("Spec before build"); DD-29

2. **Stage before deploying.** Extracted artifacts (patterns, rules, templates, skills, agents) stage in `extracts/` before deployment to enforcement locations in the engine's `knowledge/` or `.claude/`. Nick owns the deployment step — now an in-engine promotion from `extracts/` to `knowledge/`, still human-gated.
   - *Source:* Constitution — Design Philosophy; DD-119 (originally DD-39), DD-80

3. **Spec before build.** New skills, agents, or structural changes require a specification (proposal, skill definition, or agent constitution) before implementation. The Owner produces specs; Nick approves them.
   - *Source:* Constitution — Design Philosophy ("Spec before build"); DBDO Pipeline steps 3-4

4. **Handoffs are file-mediated.** Agents do not communicate directly in conversation. The Researcher writes findings with `pipeline_status: raw`. The Codifier reads findings with `pipeline_status` indicating readiness. The handoff is the file state, not a message.
   - *Source:* DBDO Pipeline (design-wisdom, `knowledge/reference/`); `agents/handoff-protocol.md`

5. **System evolution via periodic research, not ad-hoc.** Changes to the IL system flow through the structured pipeline (research → identify → extract → deploy). Exception: on-demand research via `/research-query` (DD-83) and Owner-initiated structural proposals.
   - *Source:* Constitution — Design Philosophy; DD-36

6. **Learn and improve every cycle.** Every research scan, every audit, every feedback triage produces learnings. Learnings route by shape (DD-116): decision-shaped → a DD, pattern-shaped → `knowledge/`, work-shaped → an IB item; git + `HISTORY.md` carry the event record. The Owner detects patterns. The pipeline should get faster and more accurate over time.
   - *Source:* DBDO Pipeline step 6 ("Learn and Improve"); DD-116

7. **Session tracking rides the three-artifact spine.** Sessions are recorded by git (Conventional Commits with a `Refs:` scope footer) + `HISTORY.md` (Keep-a-Changelog, newest-first); `PROGRESS.md` is the sole forward control surface, reconciled by `/session-handoff`. The former per-entry SL telemetry block (DD-90) retired with the SL producer — its harness-portable requirement layer remains Phase-4 feedstock (DD-118).
   - *Source:* DD-116 (session-ops spine); DD-118 (DD-90 closure)

## Applicability Notes

These rules govern the flow of work through the IL system. The Researcher owns Stage 1, the Codifier owns Stages 2-3, and Nick owns Stage 4. The Owner oversees pipeline health but does not execute pipeline stages — the Owner is a steward, not a participant in the research pipeline.
