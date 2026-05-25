---
name: "Foreground vs Background Subagent Permission Models (Upfront vs Pass-Through)"
summary: "Foreground subagents block the main conversation until complete and pass permission prompts through to the user interactively. Background subagents run concurrently — Claude Code prompts for all tool permissions upfront before launching, and anything not pre-approved is auto-denied during execution. Two distinct permission semantics for two distinct orchestration modes. Plain English: foreground = 'ask each time'; background = 'ask once, deny anything else silently.'"
implementation_notes: "Environment variable CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1 disables all background functionality. If a background subagent fails due to missing permissions, user can restart as foreground to retry interactively."
category: "Governance"
evidence_strength: "Strong (documented, first-party Anthropic canonical spec)"
adoption_status: "Not Yet Started"
priority: P2
applicability:
  - "General"
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "anthropic-claude-code-subagents-docs.md"
related_findings:
  - file: tiered-permission-system-bash-safety.md
    rel: same-problem
  - file: claude-code-auto-mode-ai-driven-permission-classif.md
    rel: same-problem
  - file: capability-restricted-agent-spawning-via-allowlist.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-24"
pipeline_status: synthesized
consumed_by:
  - "agent-governance-and-trust.md"
---

## What It Is

Claude Code subagents run in one of two execution modes with distinct permission behaviors:

**Foreground** (default):
- Blocks the main conversation until the subagent completes.
- Permission prompts pass through to the user in real-time.
- Clarifying questions (like `AskUserQuestion`) are answerable interactively.
- Failure mode: user sees the prompt, user decides.

**Background**:
- Runs concurrently while the user continues other work.
- BEFORE launching, Claude Code prompts for all tool permissions the subagent will need.
- Once running, the subagent inherits these pre-approved permissions and auto-denies anything not pre-approved.
- Clarifying questions (AskUserQuestion) fail mid-execution, but the subagent continues with whatever it can do without the answer.
- Failure mode: subagent silently fails on unapproved tools; user checks completion status later.

Control mechanisms:
- Claude decides foreground vs background based on the task.
- User override: ask "run this in the background" or press Ctrl+B to background a running task.
- Recovery: if a background subagent fails due to missing permissions, start a new foreground subagent for the same task.
- Global disable: `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` env var disables background mode entirely.

## Why It Matters

Permission models are usually a single dimension (strict vs permissive). Two-mode design separates "user is available to answer" from "user is away from keyboard." Different safety envelopes apply:

- **Foreground** is safe because the user gates every non-pre-approved action. Risk is bounded by attention span.
- **Background** requires upfront approval of everything the subagent might need, so there's no runtime surprise. Risk is bounded by the correctness of the initial permission inventory.

For MetaSystem:
- **Long-running IL skills.** `/research-loop` and `/repo-analyzer` can take 10-15 minutes. Running them in background mode with pre-approved tool scope frees Nick to work on other things. Running them in foreground blocks the session and requires Nick's interactive approval cadence.
- **Safety envelope per skill.** Skills that touch destructive operations should default to foreground (interactive approval per action). Skills that are strictly read-only (`/research-query` without persistence, `/system-health`) can default to background (pre-approved Read/Grep/Glob).
- **Combines with [[tiered-permission-system-with-destructive-command-safety-architecture]].** That finding covers the tier model for dangerous commands; this one covers the mode (interactive vs batch) governing those tiers.
- **Complements [[claude-code-auto-mode-safer-way-to-skip-permissions]].** Auto-mode has a background classifier reviewing commands; background subagents pre-approve at launch. Both address "user not available" but at different layers.

## Why People Are Using It

Documented canonically at [Anthropic's Claude Code subagents docs](https://code.claude.com/docs/en/sub-agents) — see [[anthropic-claude-code-subagents-docs]] for the source. Key behaviors from the docs:

- Foreground: *"Permission prompts and clarifying questions (like AskUserQuestion) are passed through to you."*
- Background: *"Before launching, Claude Code prompts for any tool permissions the subagent will need, ensuring it has the necessary approvals upfront. Once running, the subagent inherits these permissions and auto-denies anything not pre-approved."*
- Recovery: *"If a background subagent fails due to missing permissions, you can start a new foreground subagent with the same task to retry with interactive prompts."*

The design choice is pragmatic: it acknowledges that interactive approval is the safer default but becomes infeasible for long-running tasks. Rather than forcing "skip all permissions" (bypassPermissions) as the alternative, background mode inserts a bulk-approval gate at launch time — the user sees the full capability list once, makes one decision, and the subagent proceeds within that envelope.

## Potential Alternatives

- **Foreground only.** All tasks block the user; simple permission model; impractical for long-running work.
- **Background only with skip-all.** Runs concurrent; user never sees permissions; catastrophic safety profile.
- **Interactive but non-blocking.** User gets prompts as notifications while continuing other work. Requires UI support; not a current Claude Code pattern.
- **Role-based permission bundles.** Pre-approved "test-runner" or "doc-writer" bundles; subagents request a bundle rather than individual tools. Coarser grain; simpler UX.
- **Time-boxed auto-approval.** After user approves once, subsequent identical prompts auto-approve for N minutes. Convenience-biased; requires careful scoping.

## Potential Improvements

- **Pre-approval inspection UI.** Background launch surfaces not just a tool list but the specific bash commands / URL patterns the subagent is authorized for. Finer-grained gating.
- **Foreground-with-replay.** User answers permission prompts via a dashboard async; subagent waits for answers rather than failing. Blends foreground safety with background concurrency.
- **Per-subagent default mode.** Subagent frontmatter declares `defaultMode: foreground | background`. Default honored unless user overrides.
- **Partial-success reporting.** Background subagent that hit a permission wall should surface exactly which tool was denied and what the intended action was, so the user can pre-approve next time.
- **Permission upgrade mid-run.** User spots a pending denial via notification; approves inline; subagent retries without restart. Requires stateful permission-exchange protocol.

## Potential Failure Modes

- **Background-with-under-inventory.** Launch pre-approves Read, Grep, Glob. Subagent discovers it needs Bash mid-run. Fails silently. Mitigation: thorough tool-inventory at launch; foreground retry as documented.
- **Background-with-over-approval.** User approves everything the subagent might need "just in case"; capability surface becomes broad; safety properties erode. Mitigation: principle of least permission; explicit review of each launched subagent's approval set.
- **Foreground interruption storms.** Long-running foreground subagent hits 20 permission prompts in sequence; user approves them all to get through. Mitigation: consolidate related prompts; batch-approve via skill-level `allowed-tools` pre-declaration.
- **User-elsewhere-during-foreground.** Foreground subagent blocks on a prompt; user is AFK; session idle. Mitigation: notification integration; timeout-to-background conversion.
- **Mode mismatch vs skill design.** Skill designed for interactive mode runs in background; clarifying questions fail and the skill degrades. Mitigation: skill metadata declaring required mode (`requires: foreground | either`).
- **Permission-reset on restart.** Foreground retry after background failure requires the user to re-answer all permission prompts that the background run already answered. Mitigation: persist approval state across retries for the same task identity.
