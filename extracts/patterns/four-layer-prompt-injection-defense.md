---
title: "Four-Layer Prompt Injection Defense"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "gstack-four-layer-prompt-injection-defense"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The system includes AI agents that read untrusted external content (web pages, user-submitted documents, API responses from third parties). A trust boundary exists between agent instructions and external content."
  invariants: "All untrusted content passes through every active layer before reaching the agent's reasoning context. No layer is bypassed, even if a previous layer reports clean. Layer ordering is fixed: envelope -> strip -> datamark -> filter."
  governance: "Nick owns the filter configuration and blocklist policy. Layer additions or removals require a Design Decision. Content filter mode (off/warn/block) is a deployment-time configuration, not a runtime agent decision."
  recovery: "If a layer fails to process content (crash, timeout), the content is blocked by default — fail closed, not open. If watermarked content is detected in agent output, trigger an incident review to trace the leakage path. If over-filtering blocks legitimate content, switch the affected layer to warn mode and review false positives before restoring block mode."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Four-Layer Prompt Injection Defense

**Source:** [[gstack-four-layer-prompt-injection-defense]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

AI agents that read untrusted external content (web pages, documents, API responses) are vulnerable to prompt injection attacks embedded in that content. A single defense layer is insufficient because attackers can craft content that escapes any individual boundary mechanism. The agent cannot reliably distinguish between its instructions and injected instructions when they arrive in the same content stream.

## Forces

- **Openness vs. safety.** Agents need to read external content to be useful, but every piece of external content is a potential attack vector.
- **Defense depth vs. latency.** Each additional defense layer adds processing time and complexity. Too many layers slow the agent; too few leave gaps.
- **Strictness vs. usability.** Aggressive filtering blocks attacks but also blocks legitimate content. Permissive filtering lets agents work freely but increases risk.
- **Traceability vs. content integrity.** Watermarking enables leakage detection but modifies the content, potentially breaking formatting or downstream processing.
- **Static vs. dynamic threats.** Blocklists catch known exfiltration endpoints but miss novel ones. Heuristic detection catches novel attacks but produces false positives.

## Solution

Apply defense-in-depth with four distinct layers, each addressing a different attack vector. All untrusted content must pass through every layer in sequence before reaching the agent's reasoning context.

**Layer 1 — Content Envelope Wrapping:**
Bracket untrusted content with explicit boundary markers (`BEGIN UNTRUSTED WEB CONTENT` / `END UNTRUSTED WEB CONTENT`). Inject zero-width spaces into any content that attempts to reproduce the boundary markers, preventing boundary escape attacks. This is the semantic layer — it tells the model where trusted instructions end and untrusted content begins.

**Layer 2 — Hidden Element Stripping:**
Detect and remove CSS-hidden content (opacity: 0, font-size: 0, position: absolute with off-screen coordinates, clip-path, visibility: hidden) and ARIA label injection attempts. Operate on a DOM clone — never mutate the original source. This is the steganographic layer — it removes content designed to be invisible to humans but visible to models.

**Layer 3 — Datamarking with Session-Scoped Watermarks:**
Encode a 4-character random watermark as zero-width characters in the text output, scoped to the current session. If agent output later contains watermarked text, the leakage source can be traced. This is the forensic layer — it does not prevent attacks but enables post-incident investigation.

**Layer 4 — Content Filter Pipeline:**
An extensible filter pipeline with a built-in URL blocklist (requestbin, pipedream, webhook.site, and similar exfiltration endpoints) and support for custom filter registration. Configurable via environment variable with three modes: off, warn, block. This is the policy layer — it enforces organizational rules about what content is acceptable.

## Consequences

**Positive:**
- Defense-in-depth ensures that bypassing one layer does not compromise the system — each layer catches a different class of attack.
- Session-scoped watermarks enable post-incident forensics without requiring real-time detection of all attacks.
- The extensible filter pipeline allows organizations to add domain-specific rules without modifying core layers.
- Configurable strictness (off/warn/block) allows tuning the tradeoff between safety and usability per deployment.

**Negative:**
- Zero-width space injection in Layer 1 may break legitimate content that uses those characters.
- Hidden element stripping (Layer 2) via DOM cloning adds memory overhead for large pages.
- The 4-character watermark space (~1.7M combinations) may be insufficient for high-volume, multi-tenant systems.
- Over-aggressive block mode can prevent agents from accessing legitimate content, requiring manual override workflows.
- Four layers add latency to every external content fetch — measurable overhead for real-time browsing agents.

## Known Uses

- **gstack** implements this architecture for its pair-agent browsing capability, with 47 security tests covering adversarial scenarios.
- **Anthropic's "Trustworthy Agents in Practice"** guidance reinforces the principle that agents reading untrusted content require layered defenses, though it does not prescribe this specific four-layer stack.

## Contract

### Preconditions

- The system includes AI agents that read untrusted external content (web pages, user-submitted documents, third-party API responses).
- A trust boundary is explicitly defined between agent instructions and external content.
- The runtime environment supports zero-width character manipulation and DOM parsing (for web content).

### Invariants

- All untrusted content passes through every active layer before reaching the agent's reasoning context.
- No layer is bypassed, even if a previous layer reports the content as clean.
- Layer ordering is fixed: envelope wrapping, then hidden element stripping, then datamarking, then content filtering.
- Watermark seeds are unique per session and not predictable from previous sessions.

### Governance

- Nick owns the filter configuration and URL blocklist policy.
- Layer additions or removals require a Design Decision.
- Content filter mode (off/warn/block) is a deployment-time configuration, not a runtime agent decision.
- Blocklist updates follow the same review process as any security policy change.

### Recovery

- If any layer fails to process content (crash, timeout, unexpected format), the content is **blocked by default** — fail closed, not open.
- If watermarked content is detected in agent output, trigger an incident review to trace the leakage path through the layer stack.
- If over-filtering blocks legitimate content, switch the affected layer to warn mode, review false positives, and restore block mode only after the filter is tuned.
- If a novel attack bypasses all four layers, add a targeted filter to Layer 4 and evaluate whether a new layer is needed.
