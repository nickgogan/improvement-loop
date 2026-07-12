---
name: CareerBuddy meta-skill-author reference layer — superset-spec, decision-sequence, audit-rubric, platform-matrix, skill-smells
source_type: "Repository"
status: Done
key_takeaways: The reference layer of CareerBuddy's meta-skill-author toolchain, synthesized from the same research inventory as the IL KB — every atomic claim it cites already exists as an IL finding, so intake targeted the synthesis-level patterns. Five new patterns extracted (superset-spec author-then-port-down, two-path authoring with hard promotion gates, skill-smells triage layer, rubric carve-outs for subjective/script-core skills, platform capability matrix with explicit unknowns) and three existing findings enriched with its production operationalizations (adapter-strategy selection, enhancement handoff block + deploy thresholds, three-stage verification sequencing).
relevance: High
added_by: Nick
tags: [skill-authoring, cross-platform, portability, audit-rubric, anti-patterns, evaluation]
url: https://github.com/nickgogan/CareerBuddy (.github/skills/meta-skill-author/references/)
authority: []
findings:
- superset-spec-for-cross-platform-skill-authoring.md
- two-path-skill-authoring-with-hard-promotion-gates.md
- skill-smells-triage-layer-before-full-audit.md
- eval-rubric-carve-outs-subjective-and-script-core-skills.md
- platform-capability-matrix-with-explicit-unknowns.md
- cross-platform-context-file-strategy.md
- four-discipline-prompt-evaluator.md
- two-level-verification-agent-run-plus-harness-inte.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-07-12'
---

# CareerBuddy meta-skill-author reference layer

The five reference documents backing CareerBuddy's meta-skill-author toolchain (superset-spec.md, decision-sequence.md, audit-rubric.md, platform-matrix.md, skill-smells.md) — the L3 depth layer of a production cross-platform skill-authoring system spanning Claude Code, Cursor, GitHub Copilot, OpenAI Codex, and Perplexity. The toolchain itself was imported into the engine as /meta-skill-author on 2026-07-12; this intake covers its reference docs as research sources. Notably, every finding slug the docs cite resolves to an existing IL KB finding, confirming the layer was synthesized from the same research corpus — the durable new material is its compositions: an authoritative field superset with per-field portability tags, a two-path authoring procedure terminating in hard gates, a scored audit rubric with deploy thresholds and class-aware carve-outs, a five-platform capability matrix that treats "Unknown" as a first-class cell value, and a symptom-to-cause smells table layered in front of the full audit. Overlap between this toolchain and the engine's /design-skill + /assess-skill remains a flagged open question for the restructure program's Phase 2 audit.
