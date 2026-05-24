---
name: "Claude Code Context Management Decision Matrix — Five Tools"
summary: "Anthropic's official decision matrix for Claude Code context management: Continue, /rewind (Esc+Esc), /compact <hint>, /clear, Subagents. Each maps to a specific situation — Continue when everything in the window is load-bearing; /rewind when a wrong path was taken and file reads should be kept but the failed attempt dropped; /compact when the session is bloated with stale debugging and low effort is wanted; /clear when the task is genuinely new and the user wants full control over what carries forward; Subagents when the next step will generate excess output. This is the canonical framework as of April 2026."
implementation_notes: "Adopt this as the anchor framework for any Claude Code usage doc or CLAUDE.md section on context management. The 5-tool vocabulary (Continue / Rewind / Compact / Clear / Subagent) is now Anthropic-canonical and should be used in preference to ad-hoc language. Key rule worth enforcing: rewind is the default correction, not forward-patching with 'that didn't work, try X.'"
category: "Context Engineering"
evidence_strength: "Strong (production-tested)"
adoption_status: "Partially Adopted"
priority: "P1"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in:
  - "General / Cross-System"
sources:
  - "anthropic-claude-code-session-management-1m-context.md"
related_findings:
  - file: trajectory-engineering-non-linear-session-forking.md
    rel: extends
  - file: five-context-management-techniques-in-claude-code.md
    rel: extends
  - file: two-threshold-compaction-strategy.md
    rel: same-problem
  - file: context-rot-silent-killer-and-mitigations.md
    rel: enabled-by
  - file: fork-subagent-parallel-trajectory-exploration.md
    rel: same-problem
  - file: memory-decay-compaction-convergence.md
    rel: same-problem
  - file: proactive-compaction-before-intelligence-degradation.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: classified
consumed_by: []
---

## What It Is

Anthropic formalizes Claude Code context management as a decision matrix over five primitives:

| Situation | Tool | Rationale |
|-----------|------|-----------|
| Same task, relevant context | **Continue** | "Everything in the window is still load-bearing" |
| Wrong path taken | **/rewind** (Esc+Esc) | "Keep useful file reads, drop failed attempt" |
| Bloated session, stale debugging | **/compact `<hint>`** | "Low effort; Claude decides what mattered" |
| Genuinely new task | **/clear** | "Zero rot; you control exactly what carries forward" |
| Next step generates excess output | **Subagent** | "Intermediate noise stays in child's context" |

Each primitive is documented with an explicit rationale and the failure mode it's designed to prevent. The article names "context rot" as the underlying pressure and frames the matrix as the user-facing surface for managing it.

## Why It Matters

Before this matrix, Claude Code users had the primitives (`/rewind`, `/compact`, `/clear`, subagents) but no authoritative guidance on which to reach for when. The practical result was ad-hoc usage: `/compact` overused because it was the most visible; `/clear` underused because its tradeoffs weren't clear; `/rewind` underused entirely.

The matrix converts five overlapping tools into a decision tree with named situations. For teams building on Claude Code, this becomes the reference for internal usage guides, CLAUDE.md instructions, and harness design.

Two specific decisions the matrix crystallizes:
- **Rewind is the default correction**, not forward-patching. "That didn't work, try X" accumulates both the failed attempt and the correction in context. `/rewind` drops the failed attempt cleanly.
- **Subagent invocation is governed by a mental test**: "Will I need this tool output again, or just the conclusion?" — if only the conclusion, subagent.

## Why People Are Using It

Source: Anthropic product blog post by Thariq Shihipar (Member of Technical Staff), April 15, 2026. Official Anthropic framing. Related blog: "Subagents in Claude Code" (cross-referenced).

Roman's earlier "trajectory engineering" framing (see [[trajectory-engineering-non-linear-session-forking.md]]) covers the same primitive from a practitioner angle. This Anthropic post makes that practitioner practice the canonical product-level guidance.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Ad-hoc usage | Reach for whichever command you remember | For short sessions where context management isn't a bottleneck |
| Manual CLAUDE.md reinjection | Restart Claude Code and reload CLAUDE.md manually | When session state is corrupt beyond recovery |
| Alternative harnesses (Cursor, Codex) | Different tools with different primitives | Outside the Claude Code ecosystem |

## Potential Improvements

- **Auto-suggest**: Claude Code could surface which matrix cell applies based on context state (e.g., "you've been debugging for 20 turns; consider /compact").
- **Session-boundary enforcement**: treat the decision points as explicit state transitions, not human choice under pressure.
- **Extend the matrix**: the 5-tool matrix covers in-session tools. A sixth cell could cover cross-session handoffs (session-to-session persistence via PROGRESS.md / CLAUDE.md).

## Potential Failure Modes

- **Matrix simplification masks edge cases**: ambiguous situations ("I'm mostly continuing but need to drop one file read") don't map to a single cell.
- **Autocompaction still fires** regardless of matrix — a hit on the context hard cutoff forces compaction the user didn't choose. The article notes "bad compacts can happen when the model can't predict the direction your work is going."
- **`/compact` is still lossy** — the matrix endorses it but the underlying limitation remains: "model is at its least intelligent point when compacting."
- **Subagent conclusions can be wrong without the parent knowing** — isolation prevents parent-visibility into intermediate reasoning, which is a feature for context but a liability for trust.
