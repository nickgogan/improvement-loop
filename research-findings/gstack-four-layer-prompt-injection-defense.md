---
name: "Four-Layer Prompt Injection Defense"
summary: "Defense-in-depth for AI agents reading untrusted web content: content envelope, hidden element stripping, datamarking, and extensible content filter pipeline."
implementation_notes: null
category: "Sandboxing"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: "P1 (Implement Now)"
applicability:
  - "General / Cross-System"
adopted_in: []
sources:
  - "gstack-v01590-v015160-changelog.md"
  - "anthropic-trustworthy-agents-in-practice.md"
related_findings:
  - file: "gsd-prompt-injection-scanner-hardening.md"
    rel: "same-problem"
  - file: "prompt-injection-risk-from-trusted-vs-untrusted.md"
    rel: "extends"
proposals: null
date_discovered: "2026-04-07"
last_updated: "2026-04-09"
pipeline_status: "synthesized"
consumed_by:
  - "agent-safety-and-permissions.md"
---
# Four-Layer Prompt Injection Defense

## What It Is
A four-layer defense-in-depth architecture for when AI agents read untrusted web content via a pair-agent browsing pattern:

1. **Content envelope wrapping.** Untrusted content is bracketed with `BEGIN UNTRUSTED WEB CONTENT` / `END UNTRUSTED WEB CONTENT` markers. Boundary escape prevention injects zero-width spaces into any content that attempts to reproduce the markers.
2. **Hidden element stripping.** Detects and removes CSS-hidden content (opacity, font-size, position, clip-path, visibility) and ARIA label injection attempts. Operates on a DOM clone — never mutates the original DOM.
3. **Datamarking with session-scoped watermarks.** A 4-character random watermark is encoded as zero-width characters in text output, scoped to the session. Enables tracing content leakage if agent output contains watermarked text.
4. **Content filter hooks.** An extensible filter pipeline with built-in URL blocklist (requestbin, pipedream, webhook.site) and custom filter registration support.

The system includes 47 security tests and is configurable via the `BROWSE_CONTENT_FILTER` environment variable (off/warn/block).

## Why It Matters
AI agents that browse the web are vulnerable to prompt injection attacks embedded in page content. A single-layer defense (e.g., just content wrapping) is insufficient because attackers can craft content that escapes any single boundary. Defense-in-depth ensures that even if one layer is bypassed, subsequent layers catch the attack.

## Why People Are Using It
gstack implements this for its pair-agent browsing capability. The layered approach reflects real-world attack vectors: hidden elements are used for invisible prompt injection, content boundaries can be spoofed, and exfiltration attempts target webhook endpoints. The 47-test suite suggests significant adversarial testing.

## Potential Improvements
Layer 3 datamarking could be extended to support per-page watermarks (not just per-session) for finer-grained leakage tracing. The URL blocklist could be updated dynamically from a threat intelligence feed. Content Security Policy (CSP) integration could add a fifth layer at the network level.

## Potential Failure Modes
Zero-width space injection may break legitimate content that contains those characters. The DOM clone-and-remove approach for hidden element stripping adds memory overhead for large pages. The 4-char watermark space (36^4 = ~1.7M combinations) may be insufficient for high-volume systems. Over-aggressive filtering (block mode) may prevent agents from accessing legitimate content.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[four-layer-prompt-injection-defense.md]] in `extracts/patterns/`
