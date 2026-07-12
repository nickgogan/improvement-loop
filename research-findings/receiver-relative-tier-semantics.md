---
name: 'Receiver-Relative Tier Semantics — Same Declaration, Different Enforcement per Receiver'
summary: 'In a capability contract, tier declarations (required/optional) are fixed at the source, but what they mean operationally is computed receiver-side: each receiving platform grades its own capability inventory (native/partial/absent) and intersects it with the declared rows. The same required row is a no-op on one host, a native mechanism on another, and an explicit refusal-naming-the-satisfier on a third. Negotiation is declare-and-adapt — no live handshake anywhere in the surveyed ecosystem.'
implementation_notes: 'Queued by CareerBuddy explicitly as a corpus contribution to this engine. For the portable-governance-kernel: the engine should not write per-platform contracts — one declaration set, with enforcement resolved against each receiver''s capability map at install time. Practically: the kernel''s wiring rows declare capability IDs from a controlled vocabulary; a receiving harness (Claude Code, Cursor, a bare agents.md host) self-grades and either satisfies, degrades-and-records, or refuses naming the missing satisfier. This is also the model for how the engine''s /audit-artifacts could assess a consumer system''s install honesty.'
category: Agentic Systems
evidence_strength: Medium (practitioner-documented, single production system; cross-platform sweep evidence from staged adapters)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-improve-backlog-corpus-contributions.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: machine-readable-system-contract-with-wiring-rows.md
  rel: extends
pipeline_status: raw
consumed_by: []
tags:
- capability-contracts
- portability
- tier-semantics
- declare-and-adapt
---
# Receiver-Relative Tier Semantics — Same Declaration, Different Enforcement per Receiver

## What It Is

A semantics for capability tiers in installable agent systems: the source declares each
wiring row and skill capability once, with a tier (`required` = do not install without a
satisfier; `optional` = install and carry the degradation) — but enforcement of that
declaration is relative to the receiver. Each receiving platform inventories what it
natively provides, grades every declared capability ID `native` / `partial` / `absent`,
and computes the intersection. The declaration never changes; its operational consequence
is different on every host. Shipped in CareerBuddy's `system-contract.yaml` +
`ADAPTATION.md` (MV21) and exercised across six staged platform adapters.

## Why It Matters

Plain English: a portable system cannot know in advance what any given harness enforces,
so hard-coding enforcement into the contract would either overfit to one platform or
water down to the weakest. Making tiers receiver-relative keeps one contract honest
everywhere: "required" does not mean "this mechanism exists," it means "this receiver
must find *some* satisfier in its own capability map or refuse." The same declaration
produces native enforcement on a rich host and a documented prose fallback on a poor one
— without forking the contract.

## How It Works

- Receiver-side grading (ADAPTATION.md step 2): for every capability ID in the wiring
  rows and skill sidecars, the receiving agent grades its own platform — `native` (a
  platform mechanism satisfies it directly, named), `partial` (degraded guarantees or
  manual steps, gap described), `absent` (no mechanism, no reasonable emulation).
  "Grade honestly; a flattering inventory produces a broken install."
- Intersection semantics (step 3): required row absent on every listed capability →
  stop for that unit with "explicit refusal that names exactly what would satisfy it";
  optional row unsatisfied → proceed, apply the row's degradation exactly as written,
  record it in the install report; required *skill* capability unsatisfied → do not
  install that skill; platform exceeds the source → upgrade permitted, recorded.
- Correspondence note: staged source-side adapters use the same grade scale as
  target-side self-inventories (native ↔ native; prose-only/degraded/emulated ↔ partial;
  unsatisfiable ↔ absent) — two routes, one contract, one semantics.
- Concrete receiver-relativity, same rows: path-scoped rules are `native` on Cursor
  (`.cursor/rules/*.mdc` glob frontmatter) and VS Code Copilot (`applyTo` instructions
  files, verified live), but degrade to rules folded into the always-on file on hosts
  without conditional injection. Row 08's `native-permission-enforcement` is prose-only
  on Copilot (tool gates absent) yet enforceable on Cursor/Codex — one declaration,
  three enforcement realities.
- Declare-and-adapt, never a handshake: the MV21 Phase R survey (A2A, MCPB, MCP
  server.json, OASF, agents.md, Archon) found capability negotiation is
  "declare-and-adapt everywhere, never a handshake" — there is no live negotiation
  protocol to lean on, so receiver-side static intersection is the ecosystem norm this
  design makes explicit.

## How It Could Fail

The scheme is only as good as the receiver's honesty — self-graded inventories have no
external check, and a flattering grade converts a required-row refusal into a silent
broken install. Tier inflation at the source (marking everything required) destroys
portability; the shipped contract keeps the required set minimal (4 of 8 rows; the
skill-level required union is a single ID, `human-approval-channel`). And
receiver-relative semantics presuppose a controlled capability vocabulary — free-text
capability names make grading unanswerable.
