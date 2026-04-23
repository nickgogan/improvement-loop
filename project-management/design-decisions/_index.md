---
title: "Improvement Loop Design Decisions"
id: "il-dd-index"
type: "governance"
category: "design-decision"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-05"
updated: "2026-04-05"
author: "claude"
source_dd:
  - "DD-47"
tags:
  - "design-decisions"
  - "moc"
  - "improvement-loop"
aliases: []
---

# Improvement Loop — Design Decisions

Design Decisions governing the Improvement Loop pipeline.

| ID | Decision | Status |
|----|----------|--------|
| DD-29 | No autonomous modification of any live system. Human-gated at every stage boundary. | Binding |
| DD-30 | Two-phase, two-skill agent model with strict read/write boundaries. | Binding |
| DD-31 | Scoped assessment model: Applicability determines which documents to read. | Binding |
| DD-36 | System evolution driven by periodic external research, not ad-hoc decisions. | Binding |
| DD-39 | Approved proposals are codified as governing knowledge before system-specific application. | Binding |
| DD-41 | AI Research and Improvement Proposals are IL-owned operational data, not independent sections. | Binding |
| DD-67 | Two-pass extraction model: Pass 1 (summary triage) for all sources, Pass 2 (transcript deep extraction) for P1/P2 sources. | Binding |
| DD-68 | Research dimensions as externalized, typed registry in `knowledge/research-dimensions.md`. | Binding |
| DD-69 | Bidirectional linkage invariant between sources and findings. Zero-link entries are structural defects. | Binding |
| DD-70 | Finding cross-reference model with four relationship types: enables, contradicts, extends, same-problem. | Binding |
| DD-71 | Source triage verdict taxonomy: EXTRACT, SKIP, DEFER, LINK-ONLY via fixed decision tree. | Binding |
| DD-89 | Four-zone architecture for IL design-and-governance artifacts: design-notes/, governance/proposals/, governance/, operations/. | Binding |
