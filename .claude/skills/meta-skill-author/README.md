# Cross-AI Skill Author

A meta-skill for authoring, auditing, and porting skills across Claude Code, Cursor, GitHub
Copilot, OpenAI Codex, and Perplexity.

Built on 219 research findings across 9 buckets. Every substantive claim cites a finding from
the improvement-loop corpus (`/research-findings/`). See `SOURCES.md` for upstream URLs.

---

## Quick Start

1. **Brand new?** Open `GETTING-STARTED.md` — a 30-minute path from "a task I keep doing"
   to a validated, triggering first skill. Come back here once you have a draft.
2. Open `SKILL.md` — it is the entry point for all four modes (Design, Eval, Improve, Port).
   For a high-level map of how the modes hand off, see `WORKFLOW.md` (diagram + when-to-split criteria).
3. New here? Read one of the worked walkthroughs in `examples/` first — they show what each
   mode actually produces, end to end, before you read the spec.
4. Suspect an existing skill is failing? Skim `references/skill-smells.md` for a 30-second
   symptom-to-cause triage before running a full audit.
5. Validate any skill structurally before use: `bash scripts/validate.sh ./your-skill-dir`
   (portable Level 1 deterministic check) or `skills-ref validate ./your-skill-dir`
   `[skill-frontmatter-validation-rules]` `[bmad-deterministic-skill-validator]`.
6. Choose a mode based on your task:
   - **Starting a new skill?** → Design mode (§1)
   - **Auditing an existing skill?** → Eval mode (§2)
   - **Iterating on a draft?** → Improve mode (§3)
   - **Deploying to a different AI platform?** → Port mode (§4)
7. When authoring, read `references/decision-sequence.md` first. It encodes the required gate
   before any SKILL.md is generated `[spec-first-agent-briefs-prompt-craft-context-inten]`.
   Start from `templates/skill-md-skeleton.md` to scaffold the file with embedded
   elicitation prompts.

---

## Modes

### Design — Author a new skill
Runs the tacit knowledge elicitation workflow `[tacit-knowledge-as-agent-delegation-barrier]`,
locks a spec before generating `[bidirectional-prompting-for-spec-creation]`, and produces a
compliant SKILL.md with all required intent engineering components
`[intent-engineering-framework-seven-part-agent-inten]`.

### Eval — Audit an existing skill
Scores the skill across the four-discipline rubric in dependency order
`[four-discipline-prompt-evaluator]`, runs the description optimization loop
`[skill-description-optimization-loop-held-out-test]`, and emits a structured handoff block
for the Improve mode.

### Improve — Iterate on a skill
Enforces generator-assessor separation across five named subagent roles
`[generator-assessor-separation-in-skill-iteration]`, applies the critic-verifier loop with
explicit termination conditions `[critic-verifier-loop-with-termination]`, and maintains the
capability/regression eval lifecycle `[capability-vs-regression-eval-lifecycle]`.

### Port — Adapt across platforms
Separates canonical instruction content from harness-specific packaging
`[shared-instructions-multi-harness-plugin-wrappers]`, selects the correct portability strategy
(symlink / plugin wrapper / template generation) for the target platform count
`[multi-ide-portability-via-installer-templates]`, and audits for per-model anti-patterns
`[reasoning-model-anti-pattern-prescribed-reasoning]`.

---

## What's Inside

### Core meta-skill

| File | Purpose |
|------|---------|
| `SKILL.md` | Canonical meta-skill — start here. Frontmatter triggers on skill authoring, auditing, or porting requests. |
| `references/superset-spec.md` | Every frontmatter field and body rule across all 5 platforms, with compatibility annotation. |
| `references/platform-matrix.md` | Side-by-side platform comparison: Claude Code, Cursor, GitHub Copilot, OpenAI Codex, Perplexity. |
| `references/decision-sequence.md` | Step-by-step authoring procedure with the hard design gate before generation. |
| `references/safety-gates.md` | 16 HITL primitives and the three skill attack surfaces. Required reading before publishing. |
| `references/anti-patterns.md` | 14 anti-patterns to avoid, each traced to a specific finding. |
| `references/audit-rubric.md` | Four-discipline scoring procedure in dependency order with per-dimension scoring tables. |
| `references/skill-smells.md` | Fast symptom-to-cause triage table; the 30-second pre-check before the full anti-patterns catalog and audit. |
| `references/git-integration.md` | Versioning, CI gating, and distribution: skill-as-policy artifact, repo layout, semver rules, cross-platform distribution. |
| `GETTING-STARTED.md` | 30-minute on-ramp: one real task → tacit elicitation → draft → validate → trigger gate. |
| `WORKFLOW.md` | High-level lifecycle map (Mermaid + ASCII) of the four modes, the two-skill family, and explicit criteria for when to split into a routine. |
| `adapters/claude.md` | Claude Code adapter: Claude Code extension fields, context budget constraints, hot-reload notes. |
| `adapters/cursor.md` | Cursor adapter: `.cursorrules` and MDC file integration notes. |
| `adapters/copilot.md` | GitHub Copilot adapter: `AGENTS.md` auto-load behavior, workspace trust model. |
| `adapters/codex.md` | OpenAI Codex adapter: Codex environment constraints, tool surface differences. |
| `adapters/perplexity.md` | Perplexity adapter: Perplexity skill frontmatter format, description trigger optimization, four-discipline prompt evaluator as native eval instrument. |
| `SOURCES.md` | Citation map: finding → upstream source URL. |
| `CHANGELOG.md` | Package version history (semantic versioning); the user-facing surface for snapshot freshness. |

### Examples (learn-by-doing)

| File | Purpose |
|------|---------|
| `examples/design-walkthrough.md` | One task → tacit elicitation → spec gate → SKILL.md → capability eval → ship. |
| `examples/eval-walkthrough.md` | Audit a deliberately weak skill across the four-discipline rubric; produce the enhancement handoff block. |
| `examples/port-walkthrough.md` | One canonical skill → five platform adapters from the portable layer + thin wrappers. |

### Templates (copy-paste starters)

| File | Purpose |
|------|---------|
| `templates/skill-md-skeleton.md` | Frontmatter + body scaffold with embedded per-section elicitation comments. |
| `templates/eval-query-set.md` | 20-query description optimization template (60/40 split, ≤5 iterations, select by TEST score). |
| `templates/change-manifest.md` | Refresher Detect-mode manifest starter. |
| `templates/proposal-log.md` | Refresher Propose-mode proposal-log starter. |

### Scripts (executable gates)

| File | Purpose |
|------|---------|
| `scripts/validate.sh` | Portable Level 1 deterministic validator (BMAD 19-rule / 6-category model). Exit 0 = PASS (warnings allowed), 1 = FAIL, 2 = usage error. No network, no platform-specific tooling. |
| `scripts/eval.sh` | Eval readiness gate + scaffolder. Runs validate.sh, then prepares a **sibling `<skill>-workspace/`** (eval artifacts + run outputs live there, never in the target). `--init` scaffolds the workspace; `--subjective` skips functional binary assertions for judgment-based skills (writing/voice/design); `--deterministic` skips them for script-core skills (renderer/parser/validator) verified by their own tests. Prints the Definition of Done + the ready-to-paste Grader invocation. Exit 0 = ready, 1 = not ready, 2 = usage error. |

### Agents (subagent prompts for generator-assessor separation)

| File | Purpose |
|------|---------|
| `agents/grader.md` | Independent four-discipline Grader prompt. Reads `references/audit-rubric.md`, scores in dependency order, emits the Enhancement Handoff Block. Run in a context separate from the author. |
| `agents/comparator.md` | Blind A/B comparator between two skill versions; defeats positional bias; reports the winner per criterion, not why. |
| `agents/analyzer.md` | Explains why the comparator's winner won (root cause + generalizable lesson); kept separate so "which won" never contaminates "why". |

### Refresher helper (bundled internal helper)

The meta-skill is a snapshot of the corpus at a point in time. As findings accumulate, platform docs change, and new best practices emerge, the snapshot drifts. The refresher is the maintenance counterpart that keeps the package current. It lives **inside** this package and is invoked only by `meta-skill-author` — never on its own.

| File | Purpose |
|------|---------|
| `helper-meta-skill-author/SKILL.md` | Internal helper — runs in three modes (Detect / Propose / Apply) with sandbox-first validation `[sandbox-first-modification-validation]` and required generator-assessor separation `[generator-assessor-separation-in-skill-iteration]`. |
| `helper-meta-skill-author/references/change-manifest-format.md` | Schema for the change manifest produced by Detect and consumed by Propose. |
| `helper-meta-skill-author/references/refresh-validation-pipeline.md` | Detailed 5-step sandbox-first validation pipeline with per-file rules, rollback procedure, and audit log schema. |
| `helper-meta-skill-author/references/source-watchlist.md` | Enumerated list of sources (corpus, 5 platform docs, academic, multiply-cited sources) with diff strategy and refresh cadence per source. |

The refresher is portable across all 5 target platforms — it depends only on file editing, URL fetching, diff computation, and an approval gate.

---

## Foundational Findings

The meta-skill rests on five load-bearing findings. If one of these changes, the meta-skill
must be updated:

- **`[the-four-discipline-prompting-stack-nate-b-jones]`** — The diagnostic spine. Every failure
  in a skill traces to one of four layers: Prompt Craft, Context Engineering, Intent Engineering,
  Specification Engineering. Without this taxonomy, every other rule in the meta-skill loses its
  organizing framework.

- **`[generator-assessor-separation-in-skill-iteration]`** — The governance rule. The skill author
  must never assess their own artifact in the same context. Five named subagent roles enforce this.
  Corroborated independently by Anthropic's production skill-creator and the improvement-loop's
  own architecture.

- **`[iterate-on-single-task-then-extract-skill]`** — The methodology. Work through ONE challenging
  task until success, then distill into SKILL.md. Upfront spec-driven authoring is the wrong
  sequence; practitioners systematically guess wrong before seeing the task.

- **`[intent-engineering-framework-seven-part-agent-inten]`** — The intent completeness checklist.
  Every skill must cover all seven components; Stop Rules are the most commonly omitted and the
  most consequential when missing. "Context without intent is noise."

- **`[reasoning-model-anti-pattern-prescribed-reasoning]`** — The breaking change. Explicit CoT,
  few-shot examples, self-consistency, least-to-most decomposition, and skeleton-of-thought degrade
  performance on all frontier reasoning model families (GPT-5.4, Claude 4.6, Gemini 3.1). Any
  skill body containing these techniques must be flagged for revision before deployment.

---

## Citation Conventions

- All substantive claims in `SKILL.md`, `references/`, and `adapters/` cite a finding via
  `[finding-filename]` notation.
- For upstream verification, look up `[finding-filename]` in `SOURCES.md`.
- The finding file at `/research-findings/[finding-filename].md` is the source of truth for the
  upstream citation chain.
- When no URL is available in `SOURCES.md`, the finding file itself contains the full provenance.
- Do not add claims without a finding citation. General-knowledge claims are not acceptable as
  justification for authoring rules.

---

## License and Contribution

The open-standard fields (`name`, `description`, `license`, `compatibility`, `metadata`,
`allowed-tools`) are aligned with the Agent Skills open standard at agentskills.io (Apache 2.0 /
CC-BY-4.0) `[skills-as-open-portable-standard]`. Platform-specific extension fields are marked
with `compatibility` annotations and are not part of the portable core.

To contribute a new finding: add it to the improvement-loop corpus at
`/research-findings/<finding-name>.md`, update the master inventory, and add a row to
`SOURCES.md`. Do not edit `SKILL.md` directly without updating the corresponding finding.

For ongoing maintenance — incorporating new findings, tracking platform doc changes,
or running scheduled refresh cycles — use the bundled refresher helper at
`helper-meta-skill-author/SKILL.md`. It encodes the validated update procedure with
sandbox isolation, regression eval gates, and human approval at the HITL tier
appropriate to each change.
