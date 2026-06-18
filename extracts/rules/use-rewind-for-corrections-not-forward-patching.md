---
title: "Use Rewind for Corrections, Not Forward-Patching"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "claude-code-context-management-decision-matrix-five-tools"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "Claude Code sessions where an agent or user has taken a wrong path and wants to correct course"
  platform_coupling: "specific:claude-code"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — /rewind is itself the reversal mechanism; adopting or removing this rule requires no migration"
  auditability: "medium — /rewind drops context by design, so the abandoned path is not inspectable after the fact; session logs prior to /rewind remain in cold storage"
  evidence_strength: "Strong (production-tested)"
  adoption:
    status: "Partially Adopted"
    notes: "Anthropic-canonical guidance from Thariq Shihipar (Anthropic MTS), April 2026. Adopted as general cross-system guidance; no CLAUDE.md enforcement at time of extraction."
contract:
  preconditions: "The current Claude Code session contains a failed attempt (wrong file edits, incorrect reasoning path, stale debugging turns) that is not worth carrying forward. The useful context from before the failure (file reads, confirmed facts) should be preserved. /rewind (Esc+Esc) is available in the Claude Code session."
  invariants: "Forward-patching ('that didn't work, try X') is not used as the primary correction mechanism when /rewind is available. /rewind is applied before adding new instructions that contradict or repair a prior failed attempt."
  governance: "This rule applies to all Claude Code sessions. It should be declared in any CLAUDE.md section on context management. It overrides the default user instinct to continue the conversation and describe what went wrong — that instinct produces forward-patching. The rule does not prohibit all follow-up messages; it prohibits carrying a failed attempt forward as context for the next attempt."
  recovery: "If /rewind is not available (e.g., in an API context without session state) → /compact with a hint is the fallback; explicitly instruct the agent to disregard the failed attempt. If the wrong path was partially correct and partially incorrect → /rewind to before the failure point, then selectively re-introduce the useful parts in a clean message."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-management"
  - "claude-code"
  - "context-rot"
---

# Use Rewind for Corrections, Not Forward-Patching

**Source:** [[claude-code-context-management-decision-matrix-five-tools]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

A Claude Code session contains a failed attempt — an edit that introduced a bug, a plan that went in the wrong direction, a sequence of debugging turns that reached a dead end — and the next step is to try a different approach.

The decision point: do you describe what went wrong and ask for a correction (forward-patching), or do you rewind to before the failure (context reset)?

## Action

**Required:** Use `/rewind` (Esc+Esc) to return the context to the state before the failed attempt. Then issue the corrected instruction from the clean context.

**Permitted:** Continue the session without /rewind only when the failed attempt contains useful intermediate context that is genuinely load-bearing for the next step.

**Forbidden:** "That didn't work, try X" as the default correction pattern when /rewind is available. Adding an instruction that contradicts or repairs a prior failed attempt without removing the failed attempt from context first.

## Boundary

Applies at every correction decision point in a Claude Code session: when an edit is wrong, when a plan has been abandoned, when a debugging sequence has gone stale.

Does not apply to continuations (same task, everything in context is still relevant), or to cases where the failed attempt contains partial progress that is load-bearing. For those, use Continue or /compact.

## Enforcement

- **Mechanism:** The rule is embedded in CLAUDE.md or equivalent session-start instructions. The agent is primed to recognize correction decision points and invoke /rewind rather than drafting a repair instruction.
- **Check (heuristic):** Scan the session for turns that begin with "that didn't work," "that's not right," "actually, try," or equivalent correction phrases followed by a new attempt. Each such pattern is a candidate forward-patch — evaluate whether /rewind was the better choice.
- **Check (mechanistic):** A session analysis hook can flag turns where the model acknowledges a failure AND proceeds with a continuation rather than a rewind invocation.
- **Violation response:**
  - *Forward-patch detected mid-session:* if the accumulated context is still manageable, continue; note the violation for end-of-session review. If context has become bloated from multiple forward-patches, run /compact with a hint that describes the successful direction, then re-establish clean context.
  - *Agent self-reports a failed attempt without offering /rewind:* prompt the user to consider /rewind before continuing.

## Rationale

Forward-patching accumulates both the failed attempt and the correction in the context window. The model carries the failed reasoning and must actively disregard it — which it doesn't do reliably. After two or three forward-patches, the context contains multiple competing attempts, and the model's responses begin reflecting the noise.

/rewind drops the failed attempt cleanly. The useful file reads and confirmed facts from before the failure are retained; the wrong path is gone. This produces a correction that costs zero additional context rather than adding a correction instruction on top of a failure.

Anthropic's formulation: "Rewind is the default correction, not forward-patching." This is the single most actionable rule from the five-tool context management matrix — it changes the default instinct (keep talking) to a context-hygiene operation (remove the noise before continuing).

## Failure Modes

- **Overuse of /rewind.** User rewinds to before a file read that was correct and useful. Mitigation: /rewind is targeted — rewind to just before the failure, not to session start. Re-read confirmed files in the clean context if needed.
- **Rewind not available.** API usage, non-interactive context, or session type doesn't support /rewind. Mitigation: /compact with an explicit hint naming the direction to preserve; or /clear and reinject load-bearing context manually.
- **Failure is ambiguous.** The failed attempt was partially correct and the correct parts are mixed into the wrong parts. Mitigation: rewind anyway; reconstruct the correct parts in a clean message rather than trying to surgically separate them in context.
- **User habit overrides the rule.** The instinct to describe what went wrong and ask for a fix is strong. Mitigation: embed the rule in CLAUDE.md with a trigger phrase ("when something goes wrong, consider /rewind before continuing") so the model surfaces the option.

## Contract

### Preconditions
The current Claude Code session contains a failed attempt (wrong file edits, incorrect reasoning path, stale debugging turns) that is not worth carrying forward. The useful context from before the failure (file reads, confirmed facts) should be preserved. /rewind (Esc+Esc) is available in the Claude Code session.

### Invariants
Forward-patching ("that didn't work, try X") is not used as the primary correction mechanism when /rewind is available. /rewind is applied before adding new instructions that contradict or repair a prior failed attempt.

### Governance
This rule applies to all Claude Code sessions. It should be declared in any CLAUDE.md section on context management. It overrides the default user instinct to continue the conversation and describe what went wrong — that instinct produces forward-patching. The rule does not prohibit all follow-up messages; it prohibits carrying a failed attempt forward as context for the next attempt.

### Recovery
If /rewind is not available (e.g., in an API context without session state) → /compact with a hint is the fallback; explicitly instruct the agent to disregard the failed attempt. If the wrong path was partially correct and partially incorrect → /rewind to before the failure point, then selectively re-introduce the useful parts in a clean message.
