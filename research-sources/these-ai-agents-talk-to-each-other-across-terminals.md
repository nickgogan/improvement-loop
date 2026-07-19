---
name: "These AI Agents Talk to EACH OTHER Across Terminals!"
source_type: "Video"
status: "Done"
key_takeaways: |-
  Eric Michaud demos "Intercom" (a third-party Pi-harness extension) enabling fully
  flat, parentless, cross-model agent-to-agent messaging across independently launched
  terminal sessions — a genuinely different topology from this KB's existing
  hierarchical-side-channel agent-teams pattern. Self-acknowledged rough, single-run
  demo; its honest value is the reported failure-mode profile: a model-speed
  bottleneck, sycophantic false consensus absent explicit friction, and emergent
  informal leadership even without a designated hierarchy.
relevance: "Medium"
added_by: "Nick"
tags:
  - "orchestration"
  - "multi-agent"
url: "https://www.youtube.com/watch?v=-we7iVySwkM"
authority:
  - "eric-michaud.md"
findings:
  - "flat-parentless-cross-model-agent-communication.md"
  - "agent-teams-shared-communication-channel.md"
date_added: "2026-07-18"
date_processed: "2026-07-18"
date_published: "2026-05-21"
---

Session-151 Pass 2 deep extraction (link-intake triage 2026-07-18, KB-ONLY verdict,
Nick-accepted, batch-b2). Transcript:
`app/transcript-fetcher/transcripts/-we7iVySwkM.md`. Eric Michaud channel, 11:30,
~2.5k transcript tokens.

Per-channel calibration from the triage report: "Eric Michaud (2): hands-on but
unvetted solo creator — light monitoring only" — relevance and evidence weighted down
accordingly (single untested demo, no corroborating source).

**Extraction deviation from the triage prior:** triage estimated ~2 findings (the
communication mechanism, and its observed failure modes, listed separately). Extracted
as **one** finding instead — the failure modes (speed bottleneck, sycophancy, emergent
leadership) are folded into that finding's "Potential Failure Modes" section rather
than staged as a second finding, since they are observed characteristics of the single
demonstrated pattern, not a separate pattern in their own right, consistent with the
"group related patterns into one finding" rule and with how every other finding in the
KB handles its own failure-mode content. Flagging this explicitly per instructions
rather than silently deviating from the prior.

Dedup check against `agent-teams-shared-communication-channel.md` (the closest existing
finding, per triage's own flag as "close-cousin-not-duplicate") resolved as CREATE, not
UPDATE — genuinely different topology (fully flat/no parent vs. side-channel-under-a-
parent) — with a minimal surgical cross-link UPDATE staged on the existing finding
(`related_findings` addition only, no content change).

**Cross-link candidate (flag for orchestrator, not assumed):** this source's flat-mesh
"no bottleneck from the top hierarchy agent's perspective" claim is same-problem /
arguably contradicts Factory's reported "direct communication is hardest [part of
multi-agent coordination]" caution, if batch-b1 stages that claim from
`ow1we5PzK-o` ("The Multi-Agent Architecture That Actually Ships"). Batch-b2 does not
have batch-b1's staged filename to link directly; the orchestrator should reconcile.
