---
title: "Artifact Audit — meta-skill-author (1.20.0 sync) + meta-skill-eval (2.0.0 import)"
type: "artifact-audit"
target_system:
  - "improvement-loop"
created: "2026-07-22"
author: "librarian"
stage: "final"
tags:
  - "artifact-audit"
  - "assess-skill"
  - "rule-10"
source_dd:
  - "DD-78"
  - "DD-82"
  - "DD-92"
  - "DD-109"
  - "DD-122"
---

# Audit — SKILL.md × 2 (fresh-context, rule-10 pass)

Run via `/assess-skill` contract (`operations/references/librarian/audit.md` ×
`skill.md`). Fresh Librarian context per generator-assessor separation — this
session did not author either package.

**Substrate-composition note (affects both audits below).** `audit.md` and
`skill.md`'s composition table both still name **G3b** ("Agent Workflow and
Execution") as the Tier-1 guide for the workflow/execution aspect of a skill
audit. G3b was deprecated and archived in session 152 (DD-122), split into
**G3c** (Production Agent Execution — supervised) and **G3d** (Autonomous and
Scheduled Agent Operation). Both target skills run under human supervision
(never scheduled), so **G3c** is the correct substitute; I read G3c's
Contract in place of the archived G3b. This is a Librarian-substrate gap
(`audit.md` line 110, `skill.md`'s Composition table), not a finding against
either target skill — flagged here as a boundary-case encounter (type:
stale-reference / missing-concept-variant) per assess-skill's Boundary-Case
Encounter Surfacing clause. **Follow-up for the Librarian reference layer
(not this audit's subject):** update `audit.md`/`skill.md`'s composition
table from G3b → G3c post-DD-122.

---

## Audit 1 — `meta-skill-author/SKILL.md`

**Artifact:** `systems/improvement-loop/.claude/skills/meta-skill-author/SKILL.md` (v1.20.0, upstream-synced 2026-07-22 from CareerBuddy 1.15.0→1.20.0)
**Classification: safety-critical** (trigger: `allowed-tools` includes `Write`; procedure includes cross-system writes (new SKILL.md packages), publication (Port mode), and a commit workflow (§3.2, §6)). G9.I6 fires unconditionally.
**Composed guides:** G1 (spec quality), G3c (substituted for stale G3b — workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft), G9 (safety-critical — G9.I6 forced)
**Rubric size:** 9 file-verifiable findings surfaced below (2 new, 4 carried-forward-still-open from the 2026-07-12 pass, 3 upstream-convention/no-action); 2 follow-ups; DD-92 ContextSpec — N/A (no `context:` frontmatter block; informational note only, no findings)

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery | Tier | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Stop rules / termination | "Stop rules include at least one halt condition, one escalation trigger, and one completion criterion" | G1.I5 | **[upstream-convention] accepted, no rewrite** | No `## Stop Rules`/`## Boundary conditions` heading for the skill itself (§1.3 discusses Stop Rules only as a field the skill *authors into other specs*); this is the same "topic-mode section structure" deviation already dispositioned 2026-07-12 (ADAPTATION.md #6–#10). Not re-flagged as actionable per that disposition. | — | 1 | High |
| 2 | Cost controls on iterative fan-out | "Cost controls (budgets, pre-turn projection, termination rules, caching, fast-fail) are in place before execution scales" | G3c.I6 | **Violated — still open** | §3.1 Improve-mode fan-out (Grader/Comparator/Analyzer, parallel subagents) has no stated cost ceiling or `--max-runs`-equivalent cap; ADAPTATION.md's own rule-10 history records this as "#7 no cost ceiling on Improve-mode fan-out — real gap, upstream-inheritable" — still unresolved in the 1.20.0 body I read. Carried forward, not new. | G3c §Recovery: "add per-step budgets, pre-turn projection, and loop termination rules" | 1 | High |
| 3 | Subagent model attribution | "Every subagent dispatch names its model explicitly; the session model is pinned" | G8.I | **Missing** | Grepped all three subagent specs (`agents/grader.md`, `agents/comparator.md`, `agents/analyzer.md`) plus SKILL.md body for a `model` field or explicit model name at dispatch — none found. `grader.md`'s "How to invoke" names an agent-type suggestion (`Explore`, thoroughness: thorough) but not a model. **New finding, not previously flagged.** | G8 §Recovery: "Check dispatches for missing model parameters... Make the model explicit per dispatch" | 1 | High |
| 4 | Structural (not prompt-only) enforcement of the destructive-action gate | "Safety-critical constraints are enforced structurally, not via prompt instructions alone" | G6.I2 / G9.I6 | **Partial — still open** | §5.2 states a hard rule in prose ("governance mutations are Human-required") and §6 gates commits on §3.2 sandbox validation, but ADAPTATION.md's own history records this exact gap as open: "#3 ... structural gate for commit/push, Improve-mode local auto-commit vs DD-29 ... Nick's call; queued as gates. Interim posture: this harness's permission prompts + the workspace push-gate stand in front of the prose guard." Confirmed still true of the 1.20.0 body — no new structural gate was added by the eval-sophistication sync. Carried forward, not new. | G6 §Recovery: "treat as a security incident... investigate the enforcement mechanism failure" | 1 | Medium |
| 5 | Tool-grant minimality | "List the tools the procedure actually needs — not the tools it might want" | G5 (Scoping/anti-patterns) | **Unverified — still open** | `allowed-tools: Read, Write, Bash(python*), Bash(bash*), Bash(skills-ref*)` — identical to the set flagged 2026-07-12 (#4 tool over-grant, #5 `Bash(python*)` no-colon-prefix syntax question). ADAPTATION.md's own note: "runtime verification pending... Do not narrow grants until B is answered; record outcome here" — no outcome is recorded. Still open. | G5 §Recovery: n/a (verification item, not a design defect) | 1 | Medium |
| 6 | Description length cap | Skill's own §1.4 rule: description ≤ 1,024 chars | G8 (self-consistency) | **Satisfied** | Measured 990 chars (folded scalar, joined). | — | 1 | High |
| 7 | Packaging-bar completeness | Skill's own §1.3 universal bar: README.md, CHANGELOG.md + semver, capability-contract.yaml, evals/eval-cases.yaml | G1 (spec completeness) | **Satisfied** | All four present at skill root; version 1.20.0 matches CHANGELOG and frontmatter. | — | 1 | High |
| 8 | Boundary statement vs. sibling | "author owns method / eval executes" | Cross-package consistency (task-specific check) | **Satisfied** | ADAPTATION.md: "Sibling seam: `/meta-skill-author` §2 owns the eval method; this skill only executes." — matches §2's actual scope (Eval-mode description optimization + four-discipline rubric) and matches `meta-skill-eval`'s own "Boundaries (owner map)" statement verbatim in intent. No contradiction found. | — | 1 | High |
| 9 | `[finding-name]` citations resolve in KB | Body cites `[skill-md-frontmatter-as-discovery-trigger-primitive]`, `[generator-assessor-separation-in-skill-iteration]`, etc. | G1 (evidence grounding) | **Not re-verified this pass** | 2026-07-12 pass recorded "12/12 spot-checked citation slugs resolve"; this pass did not re-spot-check citations (out of scope for the eval-method-upgrade delta, and no citation text changed per ADAPTATION's "nothing else was modified" note). Recorded as not-reverified rather than silently assumed. | — | 1 | Low (scope-limited, not ambiguity) |

### Follow-ups (system/process-verifiable)

| # | Invariant | Source | Question | Evidence expected |
|---|---|---|---|---|
| a | `Bash(python*)` prefix-glob scoping | G5/G6 | Does the installed Claude Code CLI version actually scope `Bash(python*)` to commands starting with `python` (vs. requiring `Bash(python:*)` colon syntax)? This is the same open question (#5/follow-up B) from 2026-07-12 — still unanswered. | A runtime test: attempt a non-python Bash command under this skill's grant and confirm denial. |
| b | Self-modification guard | G9.I6 | When Improve mode targets the meta-skill-author package itself, is there an explicit gate distinct from the general governance-mutation rule? (ADAPTATION's follow-up E, still open.) | A dry-run of Improve mode against its own SKILL.md, observed for a distinct halt/approval prompt. |

### Aspects out of scope

None — G1/G5/G6/G8/G9 preconditions are all satisfied (Write-capable, multi-step, side-effecting skill).

### Summary

Structurally solid and (per the prior pass) citation-grounded, but three items from the 2026-07-12 rule-10 pass remain genuinely open — not resolved by the 1.15.0→1.20.0 eval-sophistication sync, which touched eval-execution routing, not safety/cost architecture: (2) no cost ceiling on Improve-mode subagent fan-out, (4) the destructive-action gate for commit/push still lives in prose + harness permission prompts rather than a structural check inside the skill, (5) the `Bash(python*)` scoping question is still unverified. New this pass: (3) none of the three grading subagents (Grader/Comparator/Analyzer) name an explicit model, which is a direct G8 violation and a latent cost/consistency risk now that the package has grown eval-sophistication machinery. The upstream-convention items (missing canonical Stop-Rules/Boundary-conditions headings) are correctly out of scope per the standing 2026-07-12 disposition — not re-flagged.

---

## Audit 2 — `meta-skill-eval/SKILL.md`

**Artifact:** `systems/improvement-loop/.claude/skills/meta-skill-eval/SKILL.md` (v2.0.0, newly imported 2026-07-22 from CareerBuddy 2.0.0, backend ported `codex exec` → `claude -p`)
**Classification: safety-critical** (trigger: procedure spends real, irreversible tokens via CLI subprocess in `run` mode and performs cross-system writes to `operations/evals/ledger.jsonl` + transcripts — this fires independent of the narrow `allowed-tools: Read, Bash(python*)` grant, per skill.md's construction-time classification criterion 2, "procedure steps include... cross-system writes"). G9.I6 fires unconditionally.
**Composed guides:** G1 (spec quality), G3c (substituted for stale G3b), G5 (tool use), G6 (safety/permissions), G8 (prompt craft), G9 (safety-critical — G9.I6 forced)
**Rubric size:** 6 file-verifiable findings surfaced below (1 real gap, 5 satisfied); 2 follow-ups (both explicitly self-declared by the package's own ADAPTATION.md, confirmed correctly characterized as open verify-at-first-paid-run items, not misdeclared); DD-92 ContextSpec — N/A (no `context:` block; informational note only)

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery | Tier | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Stop rules / termination | "Stop rules include at least one halt condition, one escalation trigger, and one completion criterion" | G1.I5 | **Satisfied** | Explicit `## Stop rules` section (max-runs exceeded, CLI missing, auth failure, sandbox-relaxation mismatch, repeated timeouts) plus `## Acceptance (per engagement, binary)` as the completion criterion. | — | 1 | High |
| 2 | Destructive-action HITL gating | "Destructive or irreversible actions always require human approval regardless of trust level" | G9.I6 | **Satisfied** | `## Reversibility & HITL tiers` table explicitly marks `run` as "Irreversible spend, reversible files — Guarded: human names the skill or approves the plan" and raising `--max-runs`/multi-skill sweeps as "Human-required." `## Constraints`: "nothing is ever scheduled (no CI loops — G9 declined)" — an explicit, self-aware citation of this exact guide's governance principle. | — | 1 | High |
| 3 | Capability-contract tier vs. stated purpose (internal consistency) | Machine-readable contract must not understate a required HITL gate | G9.I6 (contract-level) | **Violated** | `capability-contract.yaml`: the `human-approval-channel` capability's `purpose` states it is "required before any token spend," but its `tier` field is set to **`optional`** — the opposite of what the sibling package does for the functionally analogous gate (`meta-skill-author/capability-contract.yaml` marks `human-approval-channel` as `tier: required`). A downstream consumer reading only the `tier` field (as the port/apply mechanics in `meta-skill-author` §4.2 describe — "unmet required ⇒ do not install without X") would treat this gate as skippable, contradicting the prose and the Reversibility table on the same package. **New finding.** | Align `tier: required` for `human-approval-channel`, or restate the purpose text to match an intentionally-optional read (e.g., "downgrades run to dry-run only without it" — which is in fact what the degradation note already says, suggesting `tier` is the field that's wrong, not the prose). | 1 | High |
| 4 | Tool-grant minimality | "List the tools the procedure actually needs — not the tools it might want" | G5 (Scoping/anti-patterns) | **Satisfied** | `allowed-tools: Read, Bash(python*)` — no `Write` despite the package writing a ledger and transcripts; all mutation is routed through the deterministic `eval_runner.py` subprocess, not a direct Write/Edit grant. Tighter than the sibling package's grant for a comparable safety profile — a positive contrast worth preserving as the pattern. | — | 1 | High |
| 5 | Subagent/dispatch model attribution | "Every subagent dispatch names its model explicitly" | G8.I | **Satisfied** | `run` mode's `[--model M]` is required in effect: "policy v4 semantics unchanged: no repo-owned default model — every paid run names `--model` or the eval set pins one" (ADAPTATION.md, confirmed consistent with the mode-contract table in SKILL.md). Ledger rows carry model + harness-version attribution per the Acceptance criteria. | — | 1 | High |
| 6 | `Bash(python*)` prefix-glob scoping (shared open question) | Same as Audit 1 finding 5 | G5/G6 | **Unverified — same open question, first instance for this package** | Identical `Bash(python*)` grant syntax as the sibling package; the underlying CLI-scoping question (colon vs. no-colon prefix form) applies equally here and has not been separately verified for this package. Not a new class of finding, but a new instance. | See Audit 1, follow-up (a). | 1 | Medium |

### Follow-ups (system/process-verifiable)

| # | Invariant | Source | Question | Evidence expected |
|---|---|---|---|---|
| a | `--effort` flag support on installed Claude CLI | G5 (tool interface conformance) | Does the installed Claude Code CLI build accept `--effort {low,medium,high}`? ADAPTATION.md declares this as an explicit open item ("if rejected, the run errors loudly... drop the flag and record `cli-default`"). **Confirmed correctly declared** — this is a genuine unverified-at-import item, not a misdeclaration; it is honestly stated as unresolved rather than assumed working. | First paid `run` invocation's exit behavior. |
| b | Stream event shapes (`system`/`init`, `Skill` tool_use, `result` subtypes) | G5/G1 (evidence fidelity) | Do the installed CLI's actual `stream-json` event shapes match what the deterministic tests encode? ADAPTATION.md declares this open and Nick-gated at first paid run. **Confirmed correctly declared** — same disposition as (a): an honestly-flagged verification gap, not a misdeclaration passed off as resolved. | A saved transcript from the first real run, diffed against `test_claude_backend.py` fixtures. |

### Aspects out of scope

None — all composed guides' preconditions are satisfied.

### Summary

This package explicitly encodes the G9.I6 discipline in its own prose (Stop rules, Reversibility & HITL tiers, an explicit "G9 declined" citation against scheduling) — stronger, more legible safety documentation than its sibling. The one real defect is internal to the machine-readable layer: `capability-contract.yaml` marks the human-approval gate `optional` while its own purpose text and the prose Reversibility table treat it as mandatory before token spend — an inconsistency a downstream automated consumer could act on incorrectly. The two "verify-at-first-paid-run" items in ADAPTATION.md (`--effort` support, stream-event shapes) are correctly declared as open, not resolved-but-misdeclared; no misrepresentation found there.

---

## Cross-package check: boundary-statement consistency

Requested check: "author owns method / eval executes" mutual consistency.

**Consistent, no contradiction.** `meta-skill-author`'s ADAPTATION.md states: "Sibling seam: `meta-skill-author` §2 owns the eval method; this skill only executes." `meta-skill-eval`'s own SKILL.md "Boundaries (owner map)" states: "Eval-case authoring and skill-quality scoring — `meta-skill-author` §2 owns the method; this skill only executes what exists." Both packages name the same owning section (§2 Eval Mode) and the same split (authoring/method vs. execution), from both directions. No misalignment found.

---

## Overall verdicts

| Package | Classification | Findings (file-verifiable) | Follow-ups | Verdict |
|---|---|---|---|---|
| `meta-skill-author` 1.20.0 | Safety-critical | 9 (1 Violated, 1 Partial, 2 Unverified/still-open, 2 Missing/new, 3 Satisfied, 1 not-reverified) | 2 | Deployable as-is (already in production use); two carried-forward gaps (fan-out cost ceiling, commit-gate structural enforcement) remain genuinely open and are Nick's call per the 2026-07-12 disposition — this pass adds one new, concrete finding (unattributed subagent models) that should be fixed cheaply. |
| `meta-skill-eval` 2.0.0 | Safety-critical | 6 (1 Violated, 5 Satisfied) | 2 (both correctly self-declared, not misdeclared) | Strong G9.I6 posture in prose; one concrete fix needed before the first paid run — `capability-contract.yaml`'s `human-approval-channel` tier should read `required`, matching its own purpose text and the sibling package's convention. |

Three most important findings across both packages:
1. `meta-skill-eval/capability-contract.yaml` marks the mandatory pre-spend human-approval gate as `tier: optional`, contradicting its own purpose text and the Reversibility table — fix before first paid run.
2. `meta-skill-author`'s three grading subagents (Grader/Comparator/Analyzer) dispatch with no explicit model named — a direct G8 violation, new this pass.
3. `meta-skill-author`'s Improve-mode subagent fan-out still has no cost ceiling (carried forward from 2026-07-12, unresolved by the 1.20.0 sync) — real, upstream-inheritable gap.

## Substrate follow-up (not a finding against either package)

`operations/references/librarian/audit.md` (line 110) and `skill.md` (Composition table) still route skill audits to the archived **G3b**. Recommend updating both to **G3c** (with a note to consult **G3d** for skills that *do* run unattended/scheduled) now that DD-122 has landed. This is Owner/Codifier-scoped reference-layer maintenance, out of scope for this read-only audit.
