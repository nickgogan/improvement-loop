---
name: GSD Prompt Injection Scanner Hardening
summary: 'Proactive prompt injection scanner with four detection layers: invisible Unicode, encoding obfuscation, structural validation, and entropy analysis.'
implementation_notes: null
category: Sandboxing
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General / Cross-System
adopted_in: []
sources:
- gsd-v1340-v1342-changelog.md
related_findings:
- file: gstack-four-layer-prompt-injection-defense.md
  rel: same-problem
- file: prompt-injection-risk-from-trusted-vs-untrusted.md
  rel: extends
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
pipeline_status: synthesized
consumed_by:
- skills/prompt-injection-scanner-hardening.md
- agent-safety-and-permissions.md
---

## What It Is

A proactive prompt injection scanner that runs as a hook or guard before content reaches agents. It implements four detection layers: invisible Unicode character detection (zero-width chars, invisible markers), encoding obfuscation detection (base64, hex-encoded payloads), structural validation (content structure checks), and entropy analysis (flagging statistically anomalous text blocks). This is a *scanner* — proactive detection and blocking — not just a risk awareness checklist or post-hoc audit.

## Why It Matters

Agentic systems that process external content (user input, file contents, web fetches) are vulnerable to prompt injection at every input boundary. A multi-layered scanner that catches different attack vectors — from invisible Unicode tricks to encoded payloads to statistically anomalous text — provides defense in depth. Running as a pre-processing hook means malicious content is intercepted before it enters the agent's context window, not detected after damage is done.

## Why People Are Using It

As agents gain more capabilities (file access, code execution, web browsing), the attack surface for prompt injection grows. Invisible Unicode characters and encoding tricks are among the most common injection vectors because they bypass naive text-based filters. Teams building production agent systems need automated scanning that catches these vectors without requiring manual review of every input.

## Potential Improvements

The scanner could maintain a threat signature database that updates as new injection techniques are discovered. Detection layers could carry confidence scores, with configurable thresholds per deployment context (strict for production, lenient for development). A feedback loop from false positives would help tune the entropy analysis layer, which is the most likely to over-trigger on legitimate but unusual content.

## Potential Failure Modes

False positives on legitimate content — entropy analysis may flag compressed data, code snippets, or non-Latin text as anomalous. Over-aggressive Unicode filtering could break internationalized content. The scanner provides a false sense of security if it only catches known attack patterns — novel injection techniques that don't match any of the four layers will pass through undetected. Performance overhead from running four detection layers on every input could also become a bottleneck in high-throughput agent workflows.

## Extraction Note — 2026-04-19
Extracted as **skill**: [[prompt-injection-scanner-hardening]] in `extracts/skills/`
