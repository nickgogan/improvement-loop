---
name: Headless Multi-Pass Iterative Review
summary: Run N review iterations using `claude -p` (headless mode), each spawning 5-7 fresh-context sub-agents on the same target. Each pass produces independent findings; all passes aggregate into a single final report. Combines `/loop` for iteration control with headless execution for fresh context per pass.
implementation_notes: 'Implemented as a shell script: a prompt stored in an .md file is passed to `claude -p` N times. Each invocation spins up sub-agents (split-and-merge within each pass). Results are aggregated by the orchestrator after all passes complete.'
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- five-claude-code-agent-patterns.md
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
related_findings:
- file: iterative-refinement-loop-with-quality-gate.md
  rel: same-problem
- file: claude-p-headless-mode-as-openclaw-replacement.md
  rel: enables
- file: builder-validator-chain-pattern.md
  rel: same-problem
- file: two-stage-sequential-review.md
  rel: same-problem
- file: orchestrated-competition-n-sub-agents-solve-same.md
  rel: same-problem
pipeline_status: "extracted"
consumed_by:
  - "skills/headless-multi-pass-iterative-review.md"
---
## What It Is

An iterative review pattern that executes N review passes, each in a completely fresh context window, then aggregates all findings into a single report. The implementation:

1. A skill (e.g., `iterative-review`) is invoked with a PR URL or branch name and an iteration count (e.g., 5)
2. A shell script loops N times, each time calling `claude -p "<prompt>"` where the prompt is stored in an `.md` file
3. Each `claude -p` invocation is headless (non-interactive), gets a fresh context window, and internally spawns 5-7 sub-agents via the split-and-merge pattern
4. Each pass produces independent findings on the target
5. After all N passes complete, findings are aggregated into a single consolidated report

The `/loop` skill provides the iteration control and breakpoint logic. The headless flag (`-p`) ensures each pass has no memory of previous passes — every review is genuinely independent.

## Why It Matters

Standard single-pass review suffers from reviewer bias: the reviewing agent was present during (or at least aware of) the implementation and may unconsciously rationalize decisions. Fresh-context review eliminates this by giving each reviewing agent no prior knowledge.

Multiple independent passes also sample the review space more thoroughly. A single review agent may miss an issue due to attention limits or context window constraints. N independent reviewers each reviewing with fresh attention catches more issues.

The aggregation step combines insights from all passes: if 3 out of 5 passes flag the same issue, it appears in the final report as a high-confidence finding.

## Why People Are Using It

Speaker (ex-Amazon/Microsoft AI engineer) named this their most-used pattern and packaged it as an `iterative-review` skill. The speaker explicitly invokes this for PR review before merging. The speaker's specific numbers: 5 iterations, each spawning 5-7 sub-agents — 25-35 review agents total per PR review session.

## Differentiation from Related Patterns

| Pattern | Key Difference |
|---------|----------------|
| Iterative Refinement Loop with Quality Gate | Same agent refines its own output in-context; no fresh context per iteration |
| Builder-Validator Chain | Single validator pass, not N independent passes |
| Orchestrated Competition | N agents solve the same problem; only the winner is selected, no aggregation of all |
| Two-Stage Sequential Review | Spec compliance then quality, each once; not N independent sweeps |

## Potential Improvements

- Weighted aggregation: flag issues that appear in M-of-N passes at higher severity
- Pass specialization: instead of identical prompts per pass, rotate reviewer personas (security, performance, readability) across passes
- Breakpoint logic: if a pass finds zero issues, terminate early rather than running all N
- Cost monitoring: with 5 iterations × 7 sub-agents, token costs multiply rapidly — add a cost estimate gate before execution

## Potential Failure Modes

- **Token cost explosion**: 5 iterations × 7 sub-agents = up to 35 agent invocations per review; costs can exceed the value of review on small PRs
- **Aggregation noise**: N passes on a subjective target will produce N different opinions; aggregation without weighting may produce a confusing "everything is flagged" report
- **Shell script fragility**: the loop is implemented in bash; failure handling, timeouts, and partial completion are the developer's responsibility
- **Context freshness degradation**: if the prompt references a PR URL, each pass must re-fetch the PR state — rate limits or API changes can break fresh-context guarantees

## Extraction Note — 2026-05-25
Extracted as **skill**: [[headless-multi-pass-iterative-review]] in `extracts/skills/`
