---
name: "Default Workflow Library as Adoption Accelerator"
summary: "Archon ships with a curated library of pre-built workflows (fix GitHub issue, create PRD with human-in-loop, PR review, adversarial dev, Ralph loop, idea-to-PR, workflow builder) that are immediately usable on any registered project. These defaults serve as adoption accelerators (immediate value before custom workflows), reference implementations (templates for custom workflow creation), and best-practice codification (encoding community-tested patterns as runnable DAGs)."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "archon-open-source-harness-builder.md"
related_findings:
  - file: "archon-yaml-defined-harness-workflows.md"
    rel: "extends"
  - file: "bmad-v6-builder-custom-agent-workflow-creation.md"
    rel: "same-problem"
  - file: "gsd-get-shit-done-plugin.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
---

## What It Is

Archon ships with a library of default workflows bundled into the CLI, available to all registered projects immediately after installation:

- **Fix GitHub Issue** — classifies issue (bug vs. feature), researches, investigates or plans, implements, validates (loops on test failure), creates PR. Cole Medin's "most-used" workflow.
- **Interactive PRD** — human-in-loop ideation to create a product requirements document, pausing at nodes for user feedback.
- **Idea to PR** — comprehensive workflow from raw idea through to merged pull request.
- **PR Review/Validation** — automated review of existing pull requests.
- **Adversarial Dev** — an adversarial development harness (previously demonstrated in a separate live stream).
- **Ralph Loop** — the community's Ralph loop pattern encoded as an Archon workflow.
- **Issue Creator** — investigates a problem and creates a well-structured GitHub issue.
- **Workflow Builder** — meta-workflow that creates new workflows from natural-language descriptions.

These defaults serve three functions:
1. **Adoption acceleration** — users get immediate value without authoring a single YAML file
2. **Reference implementations** — each default workflow is a readable YAML file that teaches Archon's node system, branching, model selection, and command file patterns by example
3. **Best-practice codification** — community-tested patterns (investigate before implement, validate before PR, classify before route) are encoded as runnable configurations

## Why It Matters

The cold-start problem kills many developer tools: users install, see an empty canvas, and abandon. Default workflows solve this by providing immediate utility. The user's first experience is running a powerful multi-step workflow, not writing one. Custom workflow authoring becomes an optimization step, not a prerequisite.

The defaults also establish a quality floor. When a team adopts Archon, even users who never customize anything benefit from workflows that encode validation, review, and human gates — patterns they might skip in a manual process.

## Why People Are Using It

Cole Medin's setup demonstration shows the workflow library listed during verification: all defaults available immediately. The fix-GitHub-issue workflow is demonstrated end-to-end, producing a real PR from a real issue. The web UI shows all available workflows in a dropdown, mixing defaults with custom workflows.

## Potential Improvements

- Workflow ratings/metrics from the community to surface the most effective defaults
- Domain-specific workflow packs (e.g., a "data engineering" pack, a "frontend" pack)
- A/B testing of workflow variations to empirically determine the most effective patterns

## Potential Failure Modes

- Default workflows may not match a team's specific development culture (e.g., no code review step in teams that pair-program instead)
- Over-reliance on defaults without customization — the defaults are general-purpose and may miss project-specific requirements
- Default workflow updates in Archon may conflict with user customizations if both modify the same file
