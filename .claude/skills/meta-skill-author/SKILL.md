---
name: meta-skill-author
description: >
  Creates, evaluates, improves, and ports cross-AI agent skills (SKILL.md files)
  that work across Claude Code, Cursor, GitHub Copilot, OpenAI Codex, and
  Perplexity. Use when designing a new skill, auditing an existing one, optimizing
  triggering accuracy, evaluating skill quality across the four disciplines
  (Prompt Craft, Context Engineering, Intent Engineering, Specification
  Engineering), or packaging a skill for multi-platform deployment. Includes four
  operating modes: Design (create spec-first), Eval (score + optimize), Improve
  (iterate with generator-assessor separation), Port (two-stage: generalize to a
  harness-neutral generic, then adapt to a target platform via its adapter).
  Make sure to use this skill whenever you need to produce a well-formed,
  portable SKILL.md — trigger phrases: "write a skill", "author a skill",
  "create a SKILL.md", "audit this skill", "port this skill", "make this skill
  generic", "improve this skill", "optimize description", "evaluate skill quality".
license: MIT
compatibility: >-
  Requires an interactive human-approval channel (the spec-first gate is the
  method; unattended runs need a pre-approved spec). Works best with script
  execution (deterministic validator + evals), a separate assessor context for
  grading, versioned storage, and reference attachment — each optional
  capability carries a named degradation in capability-contract.yaml.
allowed-tools: Read, Write, Bash(python*), Bash(bash*), Bash(skills-ref*)
metadata:
  distribution-scope: "exportable"
  version: "1.14.0"
  upstream: "nickgogan/CareerBuddy .github/skills/meta-skill-author @ 1.15.0 (CHANGELOG; upstream SKILL.md metadata lags at 1.14.0)"
  imported: "2026-07-12 — engine adaptation notes in ADAPTATION.md; body kept upstream-diffable"
---

## §0 Orientation

A skill is the AI equivalent of an SOP: encode once, invoke reliably. Skill
authorship is **distillation, not specification** — iterate on one challenging
task first, then encode what bridged the gap. The description **is** the skill
at runtime: a body that never triggers is dead capability
[skill-md-frontmatter-as-discovery-trigger-primitive]. Anthropic's four
orientations: start with evaluation · structure for scale · think from the model's
perspective · iterate during real work. Four modes — **Design** (§1), **Eval**
(§2), **Improve** (§3), **Port** (§4) — hand-offs in `WORKFLOW.md`. But first:

### §0.5 Is a skill the right primitive? (check first)

The most common authoring mistake: building a skill for what should be a plainer
primitive [skill-as-new-employee-mental-model]. Rule out cheaper options:

| Reach for this instead when… | Primitive |
|------------------------------|-----------|
| A single well-scoped request the base model already handles in one shot | **Plain prompt** — skills only trigger for tasks the model cannot do alone |
| The logic is fully deterministic (parsing, formatting, validation, math) | **Script / code tool** — encode as code; do not ask an LLM to simulate determinism |
| You need a persistent identity, long-horizon autonomy, or orchestration of many sub-tasks | **Agent / subagent** — a skill is loaded *by* an agent; it is not the agent itself |
| You only need to expose an external capability (API, DB, service) | **MCP tool** — skills and MCP are complementary, not substitutes |
| You're tempted to wrap a framework to add structure | Prefer the platform-native primitive — frameworks carry an abstraction tax |

If none fits and the task is reusable expertise that triggers by description, author
a skill (`GETTING-STARTED.md` is a 30-min path); otherwise use the simpler primitive.

## §1 Design Mode: Spec-First, Gate-Before-Generate

### 1.1 Start with one task (required first step)

Work through **one** challenging representative task with the model until it
succeeds; distill the winning approach into SKILL.md; then expand to coverage
testing [iterate-on-single-task-then-extract-skill].

### 1.2 Elicit tacit knowledge before drafting

Senior expertise "compiles" into judgment practitioners cannot articulate. Run
the five-layer elicitation (~45 min) before generating any SKILL.md:
(1) Operating rhythms · (2) Recurring decisions · (3) Required inputs · (4) Recurring
friction points · (5) Success criteria — via YAML templates with embedded
elicitation prompts, never a one-shot dump.

### 1.3 Spec-first gate (human must approve before generating SKILL.md)

Implicit training-data assumptions cause most cascading failures in long agentic
runs; lock the spec first [spec-first-agent-briefs-prompt-craft-context-inten].
Eight spec primitives: Objective+why · Success metrics · Authoritative inputs ·
Deliverables+format · Acceptance criteria (verifiable) · Constraints
(must/must-not/escalate-if) · Workflow+checkpoints · Escalation triggers. Confirm
the seven-part intent structure: Objective · Desired Outcomes · Health Metrics ·
Strategic Context · Constraints · Decision Types/Autonomy · **Stop Rules** (most
commonly omitted — always confirm present). Declare execution mode: **interactive**
(outcome-based) or **scheduled/unattended** (numbered SOP, completion signal).

Declare **distribution scope** — ask the human; never assume:

| Scope | Layout consequence |
|-------|--------------------|
| **Internal** — lives and dies in this workspace | Lean: SKILL.md + only the `references/`/`scripts/` it actually runs. No README/CHANGELOG/SOURCES — git + the workspace changelog are its version history. May bind to workspace paths and sibling skills freely |
| **Exportable** — will leave the workspace (marketplace, another harness, a work tenant) | Full distribution package (§6): README, CHANGELOG (semver), explicit versioning, source traceability if research-derived, and the separability bar from day one — zero user/workspace-specific content, environment bindings expressed as a capability contract, `capability-contract.yaml` at the skill root from day one (§4.0) |

Scaffolding scales with **distribution distance**, not importance. Declaring late is the
expensive failure: an internal skill promoted to exportable needs a §4.0 generalize pass
+ retrofitted versioning, so an undeclared scope defaults to **internal** and any later
export must run stage-1 Generalize first. Record the answer as
`metadata.distribution-scope: "internal" | "exportable"` in the SKILL.md frontmatter —
the declaration travels with the skill, not a registry.

### 1.4 Frontmatter authoring

`name`: 1–64 chars, `[a-z0-9-]`, matches directory, no reserved words.
`description`: ≤1,024 chars; [What] + [When] + [Key capabilities], key use case
first; include trigger phrases; "a little bit pushy" combats undertriggering
[skill-md-frontmatter-as-discovery-trigger-primitive]. Use open-standard fields
unless Claude Code-specific invocation control is needed; declare `compatibility`
if non-portable. Full rules: `references/superset-spec.md`. Pre-validate habit
(run-observed 2026-07-06/07): char-count the description and confirm the body
carries `[finding-name]` citations *before* the first `validate.sh` run — the
1,024 cap and the citation check are the two recurringly-failed first-draft rules.

### 1.5 Body authoring

**Format default**: outcome-based (declarative) for interactive skills — ~50%
token reduction over procedural; survives model upgrades. Before publishing, audit
for prescribed-reasoning anti-patterns and remove them (§4.4)
[reasoning-model-anti-pattern-prescribed-reasoning].

**Writing discipline**:
- Explain the WHY behind every constraint; ALL-CAPS MUST/ALWAYS/NEVER are yellow flags.
- Express behavioral rules as negative constraints, not positive aspirations.
- Pointers over copies: link to `references/` by relative path; never embed context that lives elsewhere.
- Context files add 14–22% reasoning overhead (ETH Zurich, 438 tasks); omit anything the model can discover itself.

**Size and structure**: keep SKILL.md under 500 lines; front-load critical content
(5K post-compaction budget; LRU drop after 6+ skills)
[skill-content-lifecycle-context-budget]. Include L0 abstract (~100 tokens) and L1
description (~2K tokens) as named sections; L3+ lives in `references/`.

**Mandatory fields**: Stop Rules (explicit halt conditions) · reversibility class
per side-effect (fully reversible / with effort / practically irreversible /
irreversible) · HITL tier per action (Full Autonomy / Guarded / Proposal-first /
Human-required).

## §2 Eval Mode: Description Optimization + Four-Discipline Scoring

### 2.1 Description optimization loop

Triggering accuracy is measurable, not heuristic
[skill-description-optimization-loop-held-out-test]: build ~20 realistic eval
queries (8–10 should-trigger paraphrases + 8–10 should-not-trigger near-miss
keyword matches), split 60/40 train/test, iterate up to 5 times, select by
**TEST score** to prevent overfitting. Harness (blind administration, §3.1 roles):
`scripts/prep_eval_loop.py --skills-dir <dir> --out-dir <eval-workspace>` builds the
roster, answer key, and shuffled blind batches (opaque ids — no source-skill signal);
Executor subagents return `qid -> verdict` lines; `scripts/score_run.py <verdicts>…`
scores them (majority rule across re-runs). After any roster change, re-run
seam-scoped via `--skills` (edited + adjacent siblings) — collisions are born at
boundary edits.

**Exportable skills: the set graduates into the package.** Iteration residue stays
in the sibling eval workspace (target-skill-clean rule, `scripts/eval.sh`), but for
skills declared exportable the finished set is distilled into **`evals/trigger-eval.md`**
inside the package — each query paired with its expected verdict (trigger / abstain,
plus the expected routing when the near-miss belongs to a sibling skill) so a receiving
agent can self-administer it as the install acceptance check, no harness required.

**Generic by construction.** An exportable skill's eval set is written
user-content-free from the first draft — the internal set and the shipped set are the
same file, so there is no sanitization step to miss. Real invocation phrasings (a live
capture corpus, where the host workspace keeps one) are the *seed*: they reveal true
intent shapes, including unphrased ones (bare artifact names, router-mediated calls) —
but they never travel verbatim. Write specific-but-fictional equivalents: invented
names, paths, and projects keep queries realistic without carrying user facts.

### 2.2 Four-discipline rubric

Score in dependency order — Prompt Craft → Context → Intent → Specification —
with binary pass/fail assertions; run any graded judge in a separate Grader
context, never the author's [generator-assessor-separation-in-skill-iteration].
Full rubric, levels, and handoff block: `references/audit-rubric.md`.

### 2.3 Functional & regression testing

Three tiers: triggering (90% target, positive + negative cases) · functional
(valid outputs, errors, edge cases) · performance (skill vs. baseline).
Capability evals graduate to regression near 100%; regression evals alert on any drop.

### 2.5 Deterministic structural validation

Run `scripts/validate.sh ./skill-directory` (portable 19-rule Level 1 validator;
exit 0 = PASS) or `skills-ref validate ./skill-directory` BEFORE any LLM review,
never instead of it [bmad-deterministic-skill-validator]. Behavioral pre-check: `references/skill-smells.md`.

## §3 Improve Mode: Generator-Assessor + Critic-Verifier + Lessons Log

### 3.1 Five-role architecture (enforce always)

The skill-creator never both generates and assesses the same artifact in the same
context [generator-assessor-separation-in-skill-iteration]. Roles: **Generator**
(author session) · **Executor** (subagent per eval) · **Grader**, **Comparator**,
**Analyzer** (separate contexts — specs in `agents/`). Convenience erosion is the
primary risk: `references/anti-patterns.md` AP-01.

### 3.2 Sandbox-first modification validation

Sandbox isolation → statistical significance gate (p < 0.05) → held-out
re-validation → automatic rollback on regression → versioned audit log
[sandbox-first-modification-validation].

### 3.3 Lessons log

After any invocation that produced correction, token waste, or lost work,
append a concise entry (what went wrong · fix · rule); prune beyond ~10.

### 3.4 Critic-verifier loop with termination

Generate → critique (stricter constraints, independent retrieval) → patch →
terminate at iteration cap OR confidence threshold. Critic fails closed.

## §4 Port Mode: Portable Layer vs. Harness-Specific

### 4.0 Two-stage port: Generalize → Apply

Porting is two separable stages; **stage 1 is a valid stopping point** (mirrors the
workspace-scale `meta-harness-author` generalize → adapt arc at single-skill scale).

**Stage 1 — Generalize** → deliverable `ports/generic.md` inside the skill's directory:
the workspace- and harness-neutral canon of the skill. Classify every binding in the body:

| Binding | Fate in the generic |
|---|---|
| User/workspace facts (names, paths, targets, profile pointers) | **Strip** — same separability bar as any export; the generic must pass the audit standalone |
| Environment services (filesystem, git, scripts, memory scopes, sibling skills, validators) | **Abstract into a capability contract** — a list of what any host must supply, each item a controlled-vocabulary capability ID (`references/capability-vocabulary.md`) with a degradation note for hosts that lack it |
| Invocation context (active user, project, document locations) | **Parameterize** — declare as explicit inputs the host provides at invocation |
| Method content (operating model, stop rules, HITL tiers, output formats) | **Keep** — this is the skill |

The generic carries the bundled-file manifest (§4.2) with platform-neutral fates and is
written as a valid open-standard SKILL.md body (Goal + Constraints + Context, §4.4-clean).
For **exportable** skills stage 1 also emits **`capability-contract.yaml`** at the skill
root — the canonical, machine-readable contract (schema + vocabulary:
`references/capability-vocabulary.md`). The generic's contract table, the SKILL.md
`compatibility` prose, and every port's capability block are **derived** from the sidecar,
never hand-maintained separately; authors who skip the declaration ship non-portable
skills as if they're portable [skills-as-open-portable-standard]. Known limitation:
this is authoring-time declaration only — behavioral conformance checking (does the
skill *do* what it declares?) is a deliberate gap until a preflight checker exists.

**Stage 2 — Apply** → deliverable `ports/<platform>-*.md`: mechanical mapping of the
generic's capability contract onto one platform via its `adapters/<platform>.md` profile.
Each contract item maps to a platform feature or is dropped-with-reason in the manifest.
No adapter for the target yet → author the platform profile first, then apply. When a
platform port exists without a generic (stage fusion under time pressure), backfill the
generic before the second platform — two fused ports diverge; one generic + two applies
don't.

### 4.1 Open standard vs. Claude Code extensions

Portable fields: `name`, `description`, `license`, `compatibility`, `metadata`,
`allowed-tools` [skills-as-open-portable-standard]; all other fields are silently
Claude Code-only. Full inventory: `references/superset-spec.md`.

### 4.2 Three-layer portable architecture

(1) Canonical harness-agnostic instruction source in `references/`; (2) thin
per-platform wrapper (<40 lines, frontmatter/packaging only); (3) runtime delegation
from wrapper to canonical source. 3+ platforms: template-generate from a `.tmpl` source.

**Directory convention — adapters vs ports.** `adapters/<platform>.md` (in this package)
= the reusable platform *profile*: native format, discovery model, and the mapping recipe
for porting *any* skill to that platform — one file per platform. `ports/generic.md`
(inside each ported skill's own directory) = the stage-1 harness-neutral canon;
`ports/<platform>-*.md` = the stage-2 per-platform *deliverable*, marked with source
skill + version and re-derived when the source
changes. Adapter = recipe; generic = base sauce; port = dish. Every port must carry a
**bundled-file manifest**
naming the fate of every file in the source skill — attach-as-resource / inline / convert
(script → checklist or tool) / drop-with-reason — including bundled helper skills; a port
that silently ignores `references/`, `templates/`, `scripts/`, or a helper is incomplete.

**Requires × provides mapping (stage 2).** Each `adapters/<platform>.md` carries a
`## Provides` inventory: every controlled-vocabulary **skill-capability** ID → `native`
(satisfier named) / `partial` (note) / `absent`; wiring/activation IDs (the v2 list,
owned by `meta-harness-author` since MV23) are graded at the adapter's next refresh,
not required retroactively. Applying a port
maps each row of the source skill's
`capability-contract.yaml` against it: unmet **required** ⇒ the port states "do not
install without X"; unmet **optional** ⇒ the port carries the contract's degradation
note. Every stage-2 port renders the outcome as a **"Host capabilities required"** prose
block — the only form that reaches paste-only platforms.

### 4.3 Context-file taxonomy

Which context files auto-load where (`CLAUDE.md`, `AGENTS.md`, `SOUL.md`, …) and
per-platform sensitivity: `references/platform-matrix.md`.

### 4.4 Reasoning-model anti-patterns (breaking change)

Remove explicit chain-of-thought, few-shot examples, self-consistency, least-to-most
decomposition, and skeleton-of-thought — they degrade frontier reasoning models
[reasoning-model-anti-pattern-prescribed-reasoning]. Replacement:
**Goal + Constraints + Context**. Audit any body before porting.

### 4.5 Cross-surface compatibility declaration

Custom skills do NOT sync across surfaces; declare surface requirements in
`compatibility`. Per-surface capability table: `references/platform-matrix.md`.

## §5 Security & HITL

### 5.1 Three attack surfaces

Audit all three before publishing [skill-security-audit-obligation]:
1. **Static SKILL.md instructions** — visible at audit time; review thoroughly.
2. **Bundled scripts** — visible but harder to evaluate; test before trusting; use `${CLAUDE_SKILL_DIR}` for paths.
3. **Dynamic external content fetching** — NOT visible at audit time; a URL may turn malicious after audit; establish trust at the domain level, not the URL.

Principle of Lack of Surprise: a skill's contents should not surprise the user in
their intent if described. `allowed-tools` grant inflation (e.g. `Bash(*)`) is a named risk.

### 5.2 Autonomy gradient

Assign an autonomy tier per side-effect action via the 2×2 matrix [autonomy-gradient-not-binary-delegation]:

| Blast radius / Reversibility | Reversible | Irreversible |
|------------------------------|-----------|-------------|
| **Low** | Full Autonomy | Proposal-first |
| **High** | Guarded | Human-required |

Hard rule: persistent mutations of governance docs, schemas, or MCP server
configs are **Human-required** regardless of track record. Progressive autonomy
ramp applies only within the reversible / low-blast-radius quadrant. Operating
note for always-on harnesses (e.g., GitHub Copilot): tool permissioning is
weaker and there is no per-skill side-effect gate at runtime, so this skill must
never commit, push, deploy, or delete without the user's explicit approval —
that guard lives here in the body. Truly irreversible actions (legal commitments,
regulatory filings) must not be delegated to skills at all.

### 5.3 Permission declaration & gate outputs

Declare all resource access in `allowed-tools` or a `## Permissions` section;
sub-skills receive strict subsets of parent scope (monotonic narrowing);
multi-system skills emit a permission manifest before deployment. At gates, prefer
HTML output humans will actually read, with a Veto Protocol (what action? why
optimal? projected impact?). Full 16 HITL primitives: `references/safety-gates.md`.

## §6 Distribution & Lifecycle

- Applies to skills declared **exportable** at the §1.3 spec gate; internal skills skip
  this section by design — do not retrofit its ceremony onto them.
- Directory name must match `name`; validate via `scripts/validate.sh ./skill-dir`
  (portable, no network) or `skills-ref validate ./skill-dir`. Standard layout:
  `SKILL.md` + optional `references/`, `scripts/`, `assets/` — plus, for exportable
  skills, `evals/trigger-eval.md` (§2.1) and `capability-contract.yaml` (§4.0);
  claude.ai upload = folder + zip.
- **Install acceptance**: the shipped `evals/trigger-eval.md` is the receiving side's
  triggering-conformance check — a receiving-agent protocol (e.g. an onboarding
  ADAPTATION step) administers it after install and compares observed against expected
  verdicts. Triggering only: behavioral conformance remains the declared §4.0 gap. The
  eval file is part of the export surface — the separability audit covers it; the
  capability sidecar may point to it but never restates it.
- Inheritance: `specializes: <core-skill-name>`; core skills live in a shared repo
  with `skills-lock.json` versioning (pinned reinstall = rollback).
- Every modification goes through §3.2 sandbox-first validation before commit; full
  CI + distribution guide: `references/git-integration.md`.
- **Description drift**: after any substantive body change, re-run the §2.1 loop
  and confirm TEST score does not regress.
- **Level 2 harness verification**: when this meta-skill's own configuration
  changes, verify all previously-working skills still pass acceptance criteria.

## §7 Quick Reference: Field Constraints

Full field-constraint table (caps, character classes, portability, examples):
`references/superset-spec.md`. Non-negotiables: body ≤ 500 lines, front-load
critical content, Goal+Constraints+Context on reasoning models.
