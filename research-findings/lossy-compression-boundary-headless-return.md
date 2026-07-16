---
name: Lossy Compression Boundary at Headless Session Return
summary: In the orchestrator-headless dispatch pattern, each completed headless session returns only a condensed output to the orchestrator, not the full execution log or code changes. The orchestrator
  ingests only this compressed result, keeping its context lean. This creates an explicit lossy compression boundary at every phase return, trading detail for orchestrator longevity.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- gstack-gsd-superpowers-orchestrator-headless.md
related_findings:
- file: orchestrator-headless-dispatch-context-isolation.md
  rel: extends
- file: l-d-hypothesis-information-loss-across-agent-bound.md
  rel: same-problem
- file: context-curation-over-context-stuffing.md
  rel: same-problem
- file: phase-queue-state-file-as-orchestrator-memory.md
  rel: enables
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
tags:
- session-95-reextract
---

# Lossy Compression Boundary at Headless Session Return

## What It Is

An information architecture pattern at the boundary between headless worker sessions and the orchestrator session. When a headless session completes a phase, it produces a condensed result of what it accomplished. The orchestrator reads ONLY this condensed result, not the full execution log, not the detailed conversation history, not the code diffs. The condensed result is the sole information that crosses the headless-to-orchestrator boundary.

In the demonstrated workflow, each headless session executes a full phase (potentially using Superpowers TDD, gstack role decisions, multiple file edits). On completion, it produces a result describing what was done, what files changed, and whether verification passed. The orchestrator reads this (a few hundred tokens) rather than the full session transcript (potentially tens of thousands of tokens). It uses this only for dispatch decisions (is this phase done? what is next?), not for downstream work.

This is what enables the observed sub-10-percent context utilization after 100+ dispatched sessions. If the orchestrator ingested full execution details from every session, it would have filled its context window long before reaching 100 sessions.

## Why It Matters

This is a deliberate compression boundary. It acknowledges that the orchestrator does not NEED full execution detail. It needs only enough information to determine if the phase succeeded, decide what to dispatch next, and optionally adjust subsequent phase prompts based on results.

This maps directly to the L/D hypothesis (information loss across agent boundaries): every boundary between agents is a lossy channel. This pattern makes the loss EXPLICIT and DESIGNED rather than implicit and accidental. By designing the result format, the system controls what information survives the boundary crossing.

For MetaSystem, this has direct application to the IL pipeline handoff protocol (Researcher to Codifier). Currently, findings carry full detail. But if MetaSystem adopted orchestrator-style automation, the inter-phase channel would need deliberate compression design.

## Why People Are Using It

Demonstrated in the 16-phase overnight build (Eric Tech). The orchestrator ran 100+ headless sessions and stayed at sub-10-percent context because it only ingested condensed results, not full execution histories.

The pattern also appears implicitly in GSD artifacts (the phase output read by subsequent phases) and in the Anthropic harness pattern's progress.md (a compressed state record for session handoff).

## Potential Improvements

- Structured result format with mandatory fields (phase_id, status, files_changed, tests_passed, issues_encountered) so the orchestrator can parse programmatically
- Graduated compression: brief result for successful phases, detailed result for failed phases (so the orchestrator has enough context to decide on retry strategy)
- Result validation: check that the condensed account accurately reflects the phase actual output before the orchestrator ingests it

## Potential Failure Modes

- **Critical detail loss.** A phase may encounter an issue that the condensed result omits (e.g., a test was skipped rather than failed, a temporary workaround was used). Downstream phases proceed without knowing about the issue.
- **Result quality depends on the same model that did the work.** A model that made a mistake during execution may also produce an inaccurate account of that execution because it does not know what it got wrong.
- **No forensic trail in the orchestrator.** If something goes wrong at phase 14, the orchestrator context only has condensed results of phases 1-13, not enough detail to diagnose where the root cause was.
- **Orchestrator cannot course-correct.** With only condensed results, the orchestrator cannot detect subtle drift across phases (e.g., phases 3, 5, and 7 each made slightly wrong architectural choices that compound). Full detail would make the drift visible; condensed results hide it.
