---
notion_id: 3311e08b-9b34-819c-a910-f7db162bbcec
name: 'Dynamic Discovery Architecture: Self-Updating CLI from API Schemas'
summary: The GWS CLI demonstrates a 'dynamic discovery' pattern where the tool reads API schema documents at runtime and builds its entire command surface automatically -- meaning the tool never goes stale
  when the underlying API adds new endpoints or methods.
implementation_notes: Interesting architectural pattern for any tool that wraps a versioned API. Not immediately actionable for our systems but worth tracking as a design principle for future tool integrations.
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- googleworkspace-cli-one-cli-for-all-of-google-work.md
proposals: []
date_discovered: '2026-03-28'
last_updated: '2026-04-08'
related_findings:
- file: cli-anything-meta-tool-for-creating-cli-wrappers.md
  rel: same-problem
- file: gws-cli-full-google-workspace-control-from.md
  rel: enables
pipeline_status: raw
consumed_by: []
---
# Dynamic Discovery Architecture: Self-Updating CLI from API Schemas

## What It Is
A tool architecture pattern demonstrated by the GWS CLI where the command-line interface is dynamically generated from an API's schema document at runtime. GWS CLI reads Google's Discovery Service, builds a clap::Command tree from the document's resources and methods. The result: when Google adds a new API endpoint, gws picks it up automatically.

## Why It Matters
Static API wrappers are perpetually out of date. Dynamic discovery inverts this: the tool is always as current as the API it wraps.

## Why People Are Using It
GWS CLI supports 11 Google Workspace services with 100+ skills from a single codebase.

## Potential Alternatives
Static command generation from API specs at build time, manual CLI construction, MCP server auto-generation from OpenAPI specs.

## Potential Improvements
Could be generalized into a meta-tool that takes any Discovery/OpenAPI document and produces a CLI.

## Potential Failure Modes
Runtime dependency on the schema endpoint. Schema changes could introduce breaking behavioral changes silently.
