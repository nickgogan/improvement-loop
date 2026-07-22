# Engine adaptation — meta-skill-eval in MetaSystem

> **Ported copy (backend port, not a pure import).** Upstream source:
> `nickgogan/CareerBuddy` `.github/skills/meta-skill-eval` @ **2.0.0** per its
> CHANGELOG (imported 2026-07-22, queue item 2 "eval sophistication" — Nick-ruled
> scope "sync + executor port"). Unlike the sibling `meta-skill-author` (kept
> upstream-diffable), this package's run backend is **ported**: upstream drives
> the Codex CLI; this copy drives the Claude Code CLI. Upstream 1.20.0 of the
> sibling introduced the neutral `agent-cli-subprocess` capability ID for exactly
> this seam. Re-derive check before adopting upstream releases: diff, then
> re-apply the port deltas below (all backend-touching).

## Backend port (codex exec → claude -p) — complete delta list

`scripts/eval_runner.py`:

1. **Command builder** — `build_codex_command` → `build_claude_command`:
   `claude -p --verbose --output-format stream-json --setting-sources project
   --model M [--permission-mode default --disallowedTools Write,Edit,NotebookEdit |
   --permission-mode acceptEdits] [--effort E] "query"`. Isolation semantics:
   `--setting-sources project` ignores user config; the isolated workspace
   materializes no settings files, so no hooks fire. **Sandbox delta (weaker/
   stronger trade, declared):** Codex's `read-only` OS sandbox allowed shell
   reads; here read-only cases auto-deny Bash entirely (non-interactive print
   mode denies un-allowlisted tools) — stricter on shell, with reads flowing
   through Read/Grep/Glob instead. Write cases: `acceptEdits` in a copied
   workspace vs Codex `workspace-write`.
2. **Skill-load evidence** — `parse_skills_loaded` reads `Skill` tool_use blocks
   from assistant events; evidence is `available` once the stream's
   `system`/`init` event parses (that format carries every tool call, so absence
   of a Skill call is a genuine abstention — a real upgrade over Codex, where
   builds may emit no skill envelope at all). Legacy Codex envelopes still
   honored for fixture/ledger compatibility.
3. **Final output** — Codex's model-side `--output-schema` + `--output-last-message`
   have no Claude analog; `extract_final_response` takes the single
   `result`/`success` event from the transcript and the runner persists the
   `{"response": ...}` artifact itself (`references/codex-output-schema.json`
   deleted). `final_schema_valid` now means: exactly one successful string
   result event.
4. **Paths** — `REPO_ROOT` = workspace root (parents[6]); `ENGINE_ROOT` =
   `systems/improvement-loop`. Ledger + transcripts: `operations/evals/`
   (upstream `system/ops/evals/`). Corpus: `operations/self/eval-candidates.md`
   (supplier: `/self-improve`; absent = clean pass per upstream MV48
   portability). Session store for `report --efficiency --sessions`:
   `operations/self/session-store/` (absent on this host — skipped cleanly).
   Ban-terms probe: `.claude/export-ban-terms.txt` (absent = vacuous pass).
5. **Skill roster resolution** — `skill_dir` searches the engine roster
   (`systems/improvement-loop/.claude/skills`, DD-109) then the workspace
   roster (`.claude/skills`); `make_isolated_workspace` rebuilds **both**
   rosters minus the masked skill and never materializes
   `settings.json`/`settings.local.json`/`worktrees`.
6. **Attribution** — ledger rows carry `harness: "claude-code"`,
   `harness_version: "2.0.0-claude.1"`. `--codex-bin`/`CODEX_BIN` →
   `--claude-bin`/`CLAUDE_BIN`. `--effort` choices narrowed to
   low|medium|high (Codex's xhigh/max/ultra are not Claude CLI effort levels).
7. **Tests** — `test_codex_backend.py` → `test_claude_backend.py` (claude
   stream fixtures + legacy-envelope coverage); `test_paired_report.py`,
   `test_sync_drift.py` unchanged. All three green at import
   (`python3 scripts/test_*.py`).

Other files: SKILL.md Codex mentions localized (backend, sandbox wording, stop
rules, mode-contract path, `/self-improve` boundary); capability-contract.yaml
`agent-cli-subprocess` + `workspace-file-inventory` rows re-bound to this
harness; `evals/eval-cases.yaml` t01/t12 skill names localized
(`resume-render` → `transcript-fetcher`, `ops-self-improve` → `self-improve`);
model-policy.yaml comment generalized (policy v4 semantics unchanged: no
repo-owned default model — every paid run names `--model` or the eval set pins
one).

## Verify-at-first-paid-run (open items)

- **`--effort` flag support** on the installed Claude CLI build — if rejected,
  the run errors loudly (never silently ignored); drop the flag and record
  `cli-default` until supported.
- **Stream event shapes** (`system`/`init`, `Skill` tool_use, `result`
  subtypes) against the installed CLI version — the deterministic tests encode
  the expected shapes; a real transcript confirms them. First paid run is
  Nick-gated per the skill's own cost discipline.

## Rule-10 assess pass (2026-07-22) — finding dispositions

`/assess-skill` ran in a fresh Librarian context same-day (report:
`operations/artifact-audits/2026-07-22-eval-packages-assess.md`; 6 findings —
1 Violated, 5 Satisfied; safety-critical classification confirmed, G9.I6 posture
strong). Dispositions:

- **Violated — `capability-contract.yaml` human-approval-channel row
  self-contradiction** (tier `optional` vs purpose text "required before any
  token spend") — **fixed same-day**: purpose/degradation reworded so the row is
  a coherent optional-with-degradation — run mode (any spend) is out of scope
  without the channel, never self-approved; offline modes remain available. Tier
  stays `optional` deliberately: a host without a human channel can still run
  report/sync/dry-run.
- **Follow-ups (both pre-declared here as verify-at-first-paid-run):** `--effort`
  CLI support and stream event shapes — confirmed correctly declared, remain
  open until the first Nick-gated smoke run.

## Engine-context overlay

- **Home & registration:** engine-scoped at
  `systems/improvement-loop/.claude/skills/` (DD-109); registered in the engine
  CLAUDE.md Imported Toolchain table. New top-level skill directories register
  at next session start (hot-reload rule, per the sibling's import).
- **Ownership seam (mirrors upstream):** `meta-skill-author` §2 owns the eval
  *method* (authoring, carve-outs, graduation semantics); this skill only
  executes what exists. Generator-assessor separation (engine rule 10) is
  satisfied structurally: the eval set's author never grades — the runner does.
- **Cost discipline = DD-29 alignment:** run mode is human-scoped and never
  scheduled; Nick names the skill or approves the plan before token spend.
- **No repo-wide eval sets yet:** engine skills other than the two imported
  packages carry no `evals/eval-cases.yaml`; adopting per-skill eval sets
  engine-wide is a separate Nick ruling (candidate IB item), not implied by
  this import.
