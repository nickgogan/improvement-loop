---
name: "CI/CD Is Dead, Agents Need Continuous Compute and Computers"
source_type: "Video"
status: "Done"
key_takeaways: |-
  Hugo Santos (CEO, Namespace) and Madison Faulkner (partner, NEA) argue traditional
  PR-based CI/CD breaks down at agent-authored change volume — their own team's PR-
  equivalent volume is already 4x the pre-agent baseline. They propose a pre-merge
  reconciliation queue that serializes concurrent agent changes before the git ledger,
  and a shift in human review from reading diffs to approving intent-vs-result on
  semantically grouped batches of changes, with automated critics (security-focused,
  API-conformance-focused LLMs) validating changes before a human ever sees them.
relevance: "High"
added_by: "Nick"
tags:
  - "orchestration"
  - "ci-cd"
  - "tools"
url: "https://www.youtube.com/watch?v=VktrqzQgytY"
authority:
  - "namespace.md"
  - "ai-engineer.md"
findings:
  - "pre-merge-reconciliation-queue.md"
  - "review-outcome-not-diff-for-agent-changes.md"
date_added: "2026-07-18"
date_processed: "2026-07-18"
date_published: "2026-05-13"
---

Session-151 Pass 2 deep extraction (link-intake triage 2026-07-18, KB-ONLY verdict,
Nick-accepted, batch-b2). Transcript:
`app/transcript-fetcher/transcripts/VktrqzQgytY.md`. AI Engineer conference talk,
18:37, ~4.1k transcript tokens.

Evidence register per the triage report's own framing: "weight Medium (vision
register)" — a pitch/vision talk from a compute-infrastructure vendor and a VC partner,
not a documented production teardown. The one hard number in the source (4x PR-volume
increase at Namespace's own team) is the strongest concrete anchor; the rest is
forward-looking ("weeks to months, not years") architecture description. Two findings
extracted, matching the ~2 prior — the mechanism (reconciliation queue) and the review-
philosophy shift (outcome vs. diff) are kept separate since each is independently
actionable and they target different decisions (infra architecture vs. human-gate
design), linked enables/enabled-by.

**Cross-link candidate (flag for orchestrator, not assumed):** the "external validation
no longer has humans — other agents evaluate the change" idea in this source is
same-problem, different-layer versus Factory's creator-verifier pattern reportedly
staged by batch-b1 (`ow1we5PzK-o`, "The Multi-Agent Architecture That Actually Ships") —
this source's adversarial validation sits at the git/CI plumbing layer (does the diff
pass build/test/security/conformance checks), Factory's sits at the mission/task
lifecycle layer (does the agent's overall output satisfy the task). Batch-b2 does not
have batch-b1's staged filename to link directly; the orchestrator should reconcile.
