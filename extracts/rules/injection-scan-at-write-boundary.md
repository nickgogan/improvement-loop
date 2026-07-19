---
title: "Injection Scan at the Write Boundary"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "dr-research-to-skill-gated-pipeline"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "building-agentic-systems.harvest-queue"
identification_report: "building-agentic-systems.harvest-queue.md::dr-research-to-skill-gated-pipeline::rule::injection-scan-at-write-boundary"
deployed: false
deployed_to: null
context:
  applies_to:
    - "research pipelines that ingest external web or document content and persist it into an installed knowledge base, skill tree, or similarly agent-consumed artifact store"
    - "teams building an autonomous or semi-autonomous content-to-artifact pipeline where no human reviews every source before it is written"
    - "security reviewers auditing where untrusted external text could reach a location an agent later treats as trusted instruction"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "secure"
  reversibility: "trivial — the scan is a standalone check inserted at one control point; removing it is a deletion with no migration cost, though it immediately reopens the injection risk it closed"
  auditability: "high — scan invocation and result can be logged per write, so any written artifact traces back to a specific pass/fail scan record"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented as a non-negotiable security boundary in one production research-to-skill pipeline; flagged by the source finding as directly adoptable for research-intake pipelines generally, but not yet adopted."
contract:
  preconditions: "A pipeline ingests content originating outside the system's own trust boundary — web pages, fetched documents, transcripts, third-party research output — and that content is destined for a durable, agent-consumed location such as a knowledge base, skill tree, or other installed artifact store."
  invariants: "Every piece of researched or externally sourced content is treated as untrusted data, never as instructions, regardless of its apparent source credibility. An injection scan runs on that content at the write boundary — the point where it transitions from working or staging material into a persisted, agent-consumed artifact — before the write occurs. No content reaches the installed tree unscanned, regardless of which other quality gates (citation checks, trigger-accuracy evals, collision checks) it has already passed; passing an unrelated gate never substitutes for the injection scan."
  governance: "Owner: whoever operates the research-to-artifact pipeline's write path. The scan is a mandatory pipeline stage, not an optional or judgment-based step — it cannot be skipped by pipeline configuration, urgency, or source trust level. Any new ingestion route into the same durable artifact store (a new source type, a new content format) inherits the same write-boundary scan requirement by default; exempting a route requires an explicit, reviewed decision."
  recovery: "If the scan flags content as containing directive-like or injected material: strip or quarantine the flagged portion and re-scan before writing; never write flagged content and manually 'trust' it through. If a write is later discovered to have bypassed the scan (a pipeline defect or a manual override): treat everything written through that path since the bypass as unverified, re-scan it in place or re-derive it from source, and fix the bypass before resuming ingestion through that route. If the scan itself is unavailable or broken: halt writes to the artifact store rather than writing unscanned content — a broken gate is not a reason to skip the gate."
tags:
  - "extracted-artifact"
  - "rule"
  - "security"
  - "prompt-injection"
  - "research-pipeline"
---

# Injection Scan at the Write Boundary

**Source:** [[dr-research-to-skill-gated-pipeline]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A pipeline is about to write researched or externally sourced content — from web pages, fetched documents, transcripts, or third-party research output — into a durable, agent-consumed artifact store: a knowledge base, an installed skill tree, or an equivalent location that a running agent later reads as trusted context.

## Action

**Required:** Treat all researched and web-sourced content as data, never as instructions, no matter how credible the source appears. Run an injection scan over the content at the write boundary — the transition point from working/staging material to a persisted artifact — before the write happens. Require the scan to pass (or the flagged portion to be stripped/quarantined and re-scanned) before any content reaches the installed tree.

**Forbidden:** Writing unscanned external content directly into the installed knowledge or skill tree. Treating a piece of content as safe because it already passed an unrelated quality gate (a citation check, a trigger-accuracy eval, a collision check) — none of those gates substitute for the injection scan. Granting any source an exemption from the scan on the basis of perceived trustworthiness or urgency.

## Boundary

Enforced at the **write boundary**: the specific point in the pipeline where content stops being working/staging material and becomes a persisted, agent-consumed artifact. This is a distinct control point from earlier pipeline stages (source fetching, synthesis, citation checking) — the scan fires immediately before persistence, catching content regardless of which upstream stage it came from or how it was transformed en route.

## Enforcement

- **Mechanism:** A content-scanning check inspects the researched/extracted text for embedded directive-like language — imperative instructions, role-assignment clauses, tool-invocation strings, or other patterns indicating the content is attempting to act as instructions rather than describe facts — immediately before the write call that persists it.
- **Check (deterministic):** `(scan_was_run == true) AND (scan_result == clean OR flagged_content_was_stripped == true)`. Either branch false → the write is blocked.
- **Violation response:**
  - *Scan flags content:* strip or quarantine the flagged portion, re-scan, and only write once clean.
  - *Write bypassed the scan (defect or override discovered after the fact):* treat everything written through that path since the bypass as unverified; re-scan in place or re-derive from source; fix the bypass before resuming ingestion through that route.
  - *Scan unavailable or broken:* halt writes to the artifact store until the scan is restored — do not write unscanned content to keep the pipeline moving.

## Rationale

Research pipelines ingest arbitrary web and document content by design — that is the entire point of automated research. Without a dedicated scan at the exact point content becomes a persisted, agent-consumed artifact, an injection-scan gap becomes a live vulnerability: external text can carry embedded directive-like language that a later agent session reads as trusted instruction rather than as the untrusted data it actually is, the same class of risk documented for MCP tool-description metadata and other untrusted-content-in-context surfaces. Locating the check at the write boundary — rather than at ingestion or synthesis — means it catches every route into the artifact store, including content that has already been transformed, summarized, or passed through unrelated quality gates that were never designed to detect injected instructions.

## Contract

### Preconditions
A pipeline ingests content originating outside the system's own trust boundary — web pages, fetched documents, transcripts, third-party research output — and that content is destined for a durable, agent-consumed location such as a knowledge base, skill tree, or other installed artifact store.

### Invariants
Every piece of researched or externally sourced content is treated as untrusted data, never as instructions, regardless of its apparent source credibility. An injection scan runs on that content at the write boundary — the point where it transitions from working or staging material into a persisted, agent-consumed artifact — before the write occurs. No content reaches the installed tree unscanned, regardless of which other quality gates (citation checks, trigger-accuracy evals, collision checks) it has already passed; passing an unrelated gate never substitutes for the injection scan.

### Governance
Owner: whoever operates the research-to-artifact pipeline's write path. The scan is a mandatory pipeline stage, not an optional or judgment-based step — it cannot be skipped by pipeline configuration, urgency, or source trust level. Any new ingestion route into the same durable artifact store (a new source type, a new content format) inherits the same write-boundary scan requirement by default; exempting a route requires an explicit, reviewed decision.

### Recovery
If the scan flags content as containing directive-like or injected material: strip or quarantine the flagged portion and re-scan before writing; never write flagged content and manually "trust" it through. If a write is later discovered to have bypassed the scan (a pipeline defect or a manual override): treat everything written through that path since the bypass as unverified, re-scan it in place or re-derive it from source, and fix the bypass before resuming ingestion through that route. If the scan itself is unavailable or broken: halt writes to the artifact store rather than writing unscanned content — a broken gate is not a reason to skip the gate.
