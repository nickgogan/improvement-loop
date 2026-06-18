---
name: "anthropics/skills — Official skill examples + skill-creator"
source_type: "Documentation"
status: "Done"
key_takeaways: "Anthropic's official skills repository — 17 reference skill directories (algorithmic-art, brand-guidelines, claude-api, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx), a minimal template-skill (SKILL.md only), and a spec/agent-skills-spec.md that points to agentskills.io. The skill-creator skill is the meta-skill of record: codifies the full authorship loop including draft-test-review-improve iteration, eval-viewer with per-test feedback, quantitative benchmark.json schema, description-triggering optimization with held-out test set, blind A/B comparison, and Claude.ai/Cowork-specific adaptations. Distribution model: `/plugin marketplace add anthropics/skills` then install document-skills or example-skills plugin."
relevance: "High"
added_by: "Nick"
tags:
  - "skills"
  - "agent-design"
  - "evaluation"
  - "tools"
  - "claude-code"
url: "https://github.com/anthropics/skills"
authority:
  - "anthropic.md"
findings:
  - "meta-skill-for-skill-authorship.md"
  - "skill-description-optimization-loop-held-out-test.md"
  - "iterate-on-single-task-then-extract-skill.md"
  - "skill-authoring-explain-the-why-not-musts.md"
  - "generator-assessor-separation-in-skill-iteration.md"
  - "skill-plugin-marketplace-distribution.md"
date_added: "2026-06-11"
date_processed: "2026-06-11"
---

# anthropics/skills

Reference repository for Claude's skill ecosystem. Contains:
- `./skills/` — 17 production-grade and demonstration skill examples spanning creative, technical, enterprise, and document categories. Document skills (docx, pdf, pptx, xlsx) are source-available (not OSS) but ship in the Claude.ai paid product.
- `./template/` — minimal `SKILL.md` (frontmatter + body header), the bare starting point.
- `./spec/` — 87-byte pointer to agentskills.io/specification.

The `skill-creator/SKILL.md` (485 lines) is the substrate of record for skill authorship methodology. It encodes a deliberate generator-assessor separation: when grading test outputs, spawn a separate grader subagent reading `agents/grader.md`. When doing blind comparison between two skill versions, use a separate comparator subagent (`agents/comparator.md`) and a separate analyzer (`agents/analyzer.md`). Quantitative benchmarking lives in a `benchmark.json` schema explicitly versioned for an `eval-viewer/generate_review.py` HTML reviewer.

Plugin distribution: this repo is registerable as a Claude Code Plugin marketplace via `/plugin marketplace add anthropics/skills`, then `/plugin install document-skills@anthropic-agent-skills` or `example-skills@anthropic-agent-skills`.
