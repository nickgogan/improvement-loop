---
title: "Apply Hard Character Ceilings to Agent Memory Files"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "bounded-tiered-memory-inference-driven-curation"
extraction_date: "2026-05-25"
last_change_session: 103
last_change_sl: "session-103-codifier-complete-extract-artifacts-write-phase"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent loops that maintain persistent memory files loaded into every session"
    - "harness designers setting memory architecture for coding or task agents"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "low — raising a ceiling after enforcement is in place requires re-evaluating all eviction decisions already made; lowering is trivial"
  auditability: "high — character count is mechanically checkable at write time; ceiling violations produce deterministic diffs"
  evidence_strength: "Strong (production-tested)"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "The agent loop maintains one or more always-loaded memory files (e.g., MEMORY.md, USER.md) that are injected verbatim into the system prompt at session start. Character ceilings have been declared per file."
  invariants: "Each always-loaded memory file stays at or below its declared character ceiling at all times. On any write that would push a file over its ceiling, a Curator step runs before the write is committed — consolidating redundant entries and evicting low-confidence or stale facts. The Curator resolves conflicts in favor of the most-recent high-confidence fact. No write bypasses the ceiling check."
  governance: "Owner: the harness or prompt-assembly layer that loads memory files into the system prompt. The ceiling values (MEMORY.md ≤2,200 chars, USER.md ≤1,375 chars, or equivalent calibrated values) must be declared in configuration, not embedded in prose. The Curator step must be an explicit pipeline stage, not delegated to the model's implicit judgment mid-write. Ceiling changes require deliberate re-calibration against token budget targets — not ad-hoc raises."
  recovery: "If a memory file exceeds its ceiling: run the Curator immediately to consolidate/evict, then re-check. If the Curator cannot reduce to ceiling without losing load-bearing facts, escalate to human review before writing. If a write was committed that exceeded the ceiling (caught retrospectively): run the Curator, log the violation, and audit whether the overflow entry should be retained in a warm-tier (retrievable, not always-loaded) instead."
tags:
  - "extracted-artifact"
  - "rule"
  - "memory"
  - "context-engineering"
  - "agent-design"
---

# Apply Hard Character Ceilings to Agent Memory Files

**Source:** [[bounded-tiered-memory-inference-driven-curation]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent loop maintains always-loaded memory files — files injected verbatim into the system prompt at the start of every session. These files accumulate writes over time (from inference-driven persistence, explicit "remember" commands, or Curator consolidation). Without a ceiling, they grow unboundedly, consuming token budget across every future session.

Scope: **always-loaded (hot-tier) memory files only.** Warm-tier (retrieval-indexed) and cold-tier (archival) storage are explicitly exempt — they are not injected unconditionally and do not impose a fixed per-session token cost.

## Action

**Required:** Declare a hard character ceiling for each always-loaded memory file. Before any write that would push a file over its ceiling, run a Curator step: consolidate redundant entries, evict low-confidence or stale facts (most-recent high-confidence fact wins conflicts), and re-check. Commit the write only after the file is at or below ceiling.

**Forbidden:** Writing to an always-loaded memory file without checking against its ceiling. Raising a ceiling to accommodate a single overflow entry without re-calibrating the budget impact. Delegating ceiling enforcement to the model's in-context judgment (i.e., "be concise") without a mechanical check.

## Boundary

Enforced at every write operation targeting an always-loaded memory file. The boundary is the write commit point — the ceiling must hold after the write, not just before. The rule does not govern warm-tier or cold-tier storage, which are governed by retrieval cost rather than per-session injection cost.

## Enforcement

- **Mechanism:** The harness or write handler performs a character count after forming the candidate write. If `len(candidate) > ceiling`, the Curator runs as a mandatory pre-write step.
- **Check (deterministic):** `len(file_content_after_write) <= declared_ceiling`. Boolean — no discretion.
- **Violation response:**
  - *Overflow on write:* invoke Curator, re-check, then commit if within ceiling.
  - *Curator cannot reduce to ceiling:* escalate to human — do not commit the overflow write.
  - *Retrospective overflow discovered:* run Curator immediately; log violation; consider warm-tier migration for the evicted content.
- **Cannot be self-certified:** Ceiling enforcement must be implemented at the harness level (write handler, hook, or pre-commit gate), not as a model instruction. Model instructions alone ("keep this file short") are unreliable for load-bearing memory files.

## Rationale

Always-loaded memory files impose a fixed per-session token cost regardless of relevance. A single unchecked write today becomes a permanent tax on every future session. Without hard ceilings, memory files grow monotonically — each session adding entries, none evicting — until the always-loaded section dominates the context window.

The ceiling is not arbitrary: it is calibrated to the token budget allocated to always-loaded context. The Curator step converts a write-blocking constraint into a curation opportunity: the overflow forces a judgment about which facts are worth retaining.

The production-tested pattern (Hermes agent, NousResearch) demonstrates that hard ceilings combined with LLM curation produce a self-maintaining user model that degrades gracefully rather than growing unbounded. The key innovations — hard ceiling + inference-driven writes + Curator eviction — work together; the ceiling alone without the Curator produces write failures; the Curator alone without a ceiling never fires.

**Distinction from `token-budget-pre-turn-projection`:** That rule governs per-turn session budget projection (how much context the agent can consume in a given turn). This rule governs persistent file size across sessions (how large always-loaded files can become). Different enforcement boundary: file system write commit vs. session turn start.

## Failure Modes

- **Curator evicts the wrong entries.** LLM judgment on "low-confidence" may not align with user priorities. Mitigation: flag eviction candidates before committing; allow human review for high-value facts.
- **Ceiling calibrated too aggressively.** Important facts can't fit, so the Curator is permanently conflicted. Mitigation: calibrate ceiling against actual memory usage patterns before enforcement; start conservatively and tighten.
- **Inference-driven writes over-persist irrelevant observations.** The agent writes too many entries, triggering Curator on every turn. Mitigation: tune write-trigger criteria (confidence threshold, novelty threshold) to reduce write frequency.
- **Ceiling check bypassed.** A write path exists that doesn't pass through the check (e.g., direct file edit, migration script). Mitigation: enumerate all write paths; enforce at the file-level hook, not just in one call site.

## Contract

### Preconditions
The agent loop maintains one or more always-loaded memory files (e.g., MEMORY.md, USER.md) that are injected verbatim into the system prompt at session start. Character ceilings have been declared per file.

### Invariants
Each always-loaded memory file stays at or below its declared character ceiling at all times. On any write that would push a file over its ceiling, a Curator step runs before the write is committed — consolidating redundant entries and evicting low-confidence or stale facts. The Curator resolves conflicts in favor of the most-recent high-confidence fact. No write bypasses the ceiling check.

### Governance
Owner: the harness or prompt-assembly layer that loads memory files into the system prompt. The ceiling values (MEMORY.md ≤2,200 chars, USER.md ≤1,375 chars, or equivalent calibrated values) must be declared in configuration, not embedded in prose. The Curator step must be an explicit pipeline stage, not delegated to the model's implicit judgment mid-write. Ceiling changes require deliberate re-calibration against token budget targets — not ad-hoc raises.

### Recovery
If a memory file exceeds its ceiling: run the Curator immediately to consolidate/evict, then re-check. If the Curator cannot reduce to ceiling without losing load-bearing facts, escalate to human review before writing. If a write was committed that exceeded the ceiling (caught retrospectively): run the Curator, log the violation, and audit whether the overflow entry should be retained in a warm-tier (retrievable, not always-loaded) instead.
