# Engine adaptation — meta-skill-author in MetaSystem

> **Downstream copy.** Upstream source: `nickgogan/CareerBuddy`
> `.github/skills/meta-skill-author` @ **1.20.0** per its CHANGELOG (synced
> 2026-07-22; original import @ 1.15.0 on 2026-07-12, session 133; the 1.14.0
> SKILL.md version lag noted at first import was fixed upstream at 1.19.0).
> Import discipline: the skill's own §4.0 Port model — Claude Code is stage-2 target;
> per `adapters/claude.md`, Claude Code is the reference implementation and provides
> every `capability-contract.yaml` row natively, so the whole package imports intact.
> The SKILL.md body is kept **upstream-diffable**: engine-specific rules live here, not
> inline. Re-derive check: diff against upstream before adopting upstream releases.

## 2026-07-22 upstream sync (1.15.0 → 1.20.0) — the eval-sophistication arc

Adopted upstream releases 1.16–1.20 wholesale (queue item 2, Nick-ruled scope
"sync + executor port"). What arrived: **1.18** — eval *execution* routed to the
sibling `meta-skill-eval` harness skill; prose `evals/trigger-eval.md` retired in
favor of structured `evals/eval-cases.yaml` (schema in the sibling's references).
**1.19** — output-first eval doctrine: optional capability-uplift vs
encoded-preference classification, known-good oracle required where deterministic
artifact verification is feasible, typed output-failure categories,
trajectory/single-step evaluation as diagnostic only, paired skill-vs-masked
uplift via `meta-skill-eval report --paired`. **1.20** — neutral
`agent-cli-subprocess` capability ID for the eval backend (the seam this engine's
claude-CLI backend port plugs into). **1.16/1.17** — capability-vocabulary
additions only.

Engine mappings for the new body references (body left upstream-diffable):

- `meta-skill-eval` (sibling by name) = the engine's imported copy at
  `systems/improvement-loop/.claude/skills/meta-skill-eval/` (own ADAPTATION.md).
- `system/ops/evals/` (upstream ledger home) ↦ engine
  `systems/improvement-loop/operations/evals/`.
- Corpus supplier `eval-candidates.md` (upstream `ops-self-improve`) ↦ the engine's
  `/self-improve` store (`operations/self/`); absent corpus = clean pass until the
  engine starts capturing eval-candidate phrasings.
- The engine's prior prose eval set lives in git history before this sync commit.

## What was changed at import (complete list)

1. `agents/{grader,comparator,analyzer}.md` — the authoritative-rubric pointer
   `<REPO>/.github/skills/meta-skill-author/…` rewritten to
   `<REPO>/systems/improvement-loop/.claude/skills/meta-skill-author/…`.
2. `SKILL.md` frontmatter — `allowed-tools` gains `Bash(bash*)` (upstream's
   `Bash(python*)` never covered its own `scripts/validate.sh`, a bash script);
   `metadata.upstream` + `metadata.imported` provenance fields added.
3. This file.

Nothing else was modified. Platform mentions of GitHub Copilot / `.github/` layouts in
the body, adapters, and references are cross-platform method content, not workspace
bindings — left intact.

## Engine-context overlay (how this skill runs here)

- **Home & registration:** engine-scoped at
  `systems/improvement-loop/.claude/skills/` (DD-109). Registered in the engine
  CLAUDE.md skills listing.
- **Capability mapping (contract → this harness):** human-approval-channel = Nick
  inline (required — the spec-first gate is DD-29/human-gate aligned by construction);
  script-execution = Bash tool; fresh-context-scoring = subagents (`context: fork` /
  Agent tool); versioned-checkpoints = git; reference-bundle-attachment = L3
  progressive disclosure.
- **Generator-assessor separation (§3.1) meets engine rule 10:** the Grader/Comparator/
  Analyzer subagent specs in `agents/` satisfy rule 10 natively. Where the engine
  already has a dedicated assessor, prefer it: `/assess-skill` for Contract-derived
  audits of engine/consumer skills, `/prompt-evaluator` for the four-discipline rubric
  (§2.2's four disciplines are the same four — Prompt Craft, Context, Intent,
  Specification). This package's `references/audit-rubric.md` remains authoritative for
  its *own* modes' scoring anchors.
- **Frontmatter authoring here follows DD-114** (block-scalar convention; the pre-commit
  YAML linter enforces) on top of §1.4's rules.
- **Governance tier:** skills are executable policy; §5.2's hard rule (governance
  mutations = human-required) maps to the engine's Nick-gate. Local commits at
  checkpoints are fine; push is Nick-gated (workspace rule).

## Known overlap (flagged for the Phase 2 substrate audit — not resolved here)

`meta-skill-author` (Design/Eval/Improve/Port, platform-generalist, eval-loop tooling)
overlaps the Librarian pair `/design-skill` + `/assess-skill` (KB-grounded,
Contract-derived, engine-native). Both stand until the restructure program's Phase 2
audit rules on consolidation vs. composition (candidate ruling: meta-skill-author owns
eval/port tooling; Librarian pair owns KB-grounded design/audit; Design-mode drafts get
a `/assess-skill` pass). Do not merge or retire either side without Nick's gate.
Plan of record: `operations/plans/2026-07-12-engine-restructure-program.md`.

## Rule-10 assess pass (2026-07-12) — finding dispositions

`/assess-skill` ran in a separate Librarian context same-day (verdict: content strong
and self-consistent; 12/12 spot-checked citation slugs resolve in this KB; all 34
bundled files present). Dispositions:

- **#1 not in Skill-tool listing / #2 missing `user-invocable`** — #2 fixed (field
  added for sibling parity; harness default is `true`, so this was parity not cause).
  #1's actual cause: new top-level skill directories require session restart
  (per `adapters/claude.md` hot-reload rule). Registers next session.
- **#3 prompt-layer-only side-effect guard + follow-ups A/D/E** (structural gate for
  commit/push, Improve-mode local auto-commit vs DD-29, self-modification guard) —
  **Nick's call**; queued as gates. Interim posture: this harness's permission prompts
  + the workspace push-gate stand in front of the prose guard.
- **#4 tool over-grant / #5 `Bash(python*)` no-colon syntax + follow-up B** — runtime
  verification pending (does the prefix form actually enforce scoping in this Claude
  Code version?). Do not narrow grants until B is answered; record outcome here.
- **#6–#10 [upstream-convention]** (topic-mode section structure, folded-scalar
  description, bare-slug citations, no `argument-hint`) — **accepted, no rewrite**:
  the upstream-diffable-body principle outranks engine cosmetic parity for imported
  packages. Revisit only if the Phase 2 audit rules otherwise.
- **#7 no cost ceiling on Improve-mode fan-out** — real gap, upstream-inheritable;
  candidate upstream contribution alongside the two already queued.

## Rule-10 assess pass (2026-07-22, post-1.20.0 sync) — finding dispositions

`/assess-skill` ran in a fresh Librarian context after the sync (report:
`operations/artifact-audits/2026-07-22-eval-packages-assess.md`; 9 findings).
Dispositions:

- **New — Grader/Comparator/Analyzer subagent specs name no model** —
  engine-overlay rule (no body edit; upstream-diffable): subagent spawns from
  this package follow the workspace standing rule — if the model class isn't
  specified, ask Nick before fan-out (his session-146 ruling). Candidate
  upstream contribution alongside the two already queued.
- **Carried, still open — #7 Improve-mode fan-out cost ceiling** — unresolved by
  1.16–1.20; remains a queued upstream contribution. Interim posture unchanged
  (harness permission prompts + the workspace push-gate).
- **Carried, still open — #4/#5 tool-grant scoping runtime verification**
  (follow-up B) — unchanged by the sync; do not narrow grants until answered.
- Upstream-convention findings re-confirmed as **accepted, no rewrite**
  (the upstream-diffable-body principle outranks engine cosmetic parity).
- Boundary statement vs `meta-skill-eval` ("author owns method / eval
  executes") — assessed **consistent**; no action.

## First acceptance target

Redesign/improve the YouTube-intake capability (`/transcript-fetcher`, and its seam
with `/research-loop` Pass 2) via Design/Improve mode — Nick's directive, 2026-07-12.
