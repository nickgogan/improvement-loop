---
name: "arXiv 2605.19576 — Skill-Library Drift in Self-Evolving LLM Agents (Ratchet Recipe)"
source_type: "Research Paper"
status: "Done"
key_takeaways: |-
  Names and reproduces "library drift": unbounded skill accumulation in self-evolving skill
  libraries degrades retrieval and stagnates performance. Headline: human-curated skills gave
  +16.2pp while ungoverned LLM-authored skills gave +0.0pp. Verified fix lifted pass@1 0.258 →
  0.584 (MBPP+ hard-100, Claude Opus 4.7, 3 seeds); the meta-skill authoring prior alone
  accounts for 57% of the gain, making explicit dedup mechanisms unnecessary; costs 43% more
  LLM calls. Ratchet Recipe: outcome-driven skill retirement with evidence floor (Nmin=100,
  threshold 0.10) and bounded active-skill cap (C=50). Candidate governance rule for the
  engine's own roster; feeds the evals-for-skills + assets-catalog direction. Per-skill
  contribution scoring is a candidate telemetry pattern. Est. 4 novel findings.
relevance: "High"
added_by: "Agent (Link-Intake Triage)"
tags:
  - skill-design
  - self-improvement
  - governance
  - evals
url: "https://arxiv.org/html/2605.19576v2"
authority:
  - "library-drift-paper-team.md"
findings:
  - "skill-library-drift-failure-mode.md"
  - "ratchet-recipe-skill-retirement.md"
  - "meta-skill-authoring-prior-dominance.md"
  - "per-skill-contribution-scoring-telemetry.md"
date_added: "2026-07-11"
date_processed: "2026-07-11"
---

Queued for `/research-loop` extraction by the 2026-07-11 link-intake triage
(`operations/research-reports/2026-07-11-link-intake-triage.md`, link #2).
