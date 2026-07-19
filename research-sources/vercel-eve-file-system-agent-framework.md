---
name: "This Completely Changes the Way We Build Production AI Agents (Vercel Eve)"
source_type: "Video"
status: "Done"
key_takeaways: |-
  Plain English: Vercel's new open-source framework Eve treats an entire AI agent as
  one folder — instructions, agent definition, skills, tools, sandbox, channels (Slack/
  Discord), MCP connections, sub-agents, and schedules each get their own named
  subfolder, and a compile step at build/deploy time discovers everything and wires it
  into one manifest with no hand-written imports. Layered on that folder convention are
  three production-reliability defaults: durable, checkpointed sessions that survive
  crashes/redeploys (every turn and tool call persisted); isolated sandboxing for code
  execution; human-in-the-loop approval for risky steps (shown live via a Slack
  approve/deny button); and an evals folder that gates deployment ("green check marks
  across the board before you deploy"). Vercel ships a companion coding-agent plugin
  (Claude Code/Cursor) bundling an Eve skill plus MCP server, so the coding agent — not
  the human — carries the folder-convention knowledge; scaffolding, building, and
  deploying an agent is done through natural-language prompts to the coding agent.
  DISCLOSED SPONSORSHIP: the presenter states he "worked with Vercel on this video...
  to make sure I framed everything right for you" — a paid/coordinated launch demo, not
  independent coverage. No third-party production usage is demonstrated; the only demo
  shown is the presenter's own single "Eve analyst" agent. Upstream repo independently
  verified: github.com/vercel/eve, "The Framework for Building Agents," TypeScript,
  3,853 stars, active.
relevance: "High"
added_by: "Nick"
tags:
  - "agent-framework"
  - "agent-design"
  - "vercel"
  - "eve"
  - "folder-convention"
  - "durable-execution"
  - "evaluation"
  - "sponsored-content"
url: "https://www.youtube.com/watch?v=m8VC2SV2igM"
authority:
  - "cole-medin.md"
findings:
  - "agent-as-folder-compiled-to-manifest.md"
  - "durable-checkpointed-sessions-as-framework-default.md"
  - "evals-folder-as-first-class-deploy-gate.md"
date_added: "2026-07-18"
date_processed: "2026-07-18"
date_published: "2026-07-16"
---

# This Completely Changes the Way We Build Production AI Agents (Vercel Eve)

Cole Medin's walkthrough of Vercel's newly open-sourced Eve framework, a "file-system
first" agent framework that structures an entire agent as one folder of markdown and
TypeScript. The video covers the primitive-per-folder structure and its implicit compile
step (no explicit wiring/imports required), the bundled production-reliability defaults
(durable checkpointed sessions, isolated sandboxing, human-in-the-loop approval, an
evals-as-deploy-gate folder, and Vercel-scale hosting), and a live build-and-deploy demo
of a custom "Eve analyst" agent (database tools, a revenue-rules skill, an investigator
subagent, Slack channel integration) built using Vercel's companion Claude Code/Cursor
plugin. The presenter explicitly discloses he worked with Vercel to produce the video —
this is a sponsored/coordinated framework-launch demo, not independent reporting, and is
graded accordingly (Medium evidence strength on all three extracted findings per the
KB's sponsorship-calibration rule: a framework-launch demo by a sponsored reviewer is
Medium at best unless production usage is independently demonstrated). The upstream
repository (github.com/vercel/eve) was independently verified: real, active, TypeScript,
3,853 GitHub stars, matching the structure described in the video — corroborating that
the framework exists and is a genuine release, though not corroborating any
production-scale third-party adoption claims made in the video itself.

Three findings extracted, one per major mechanic: the folder-as-agent compile-to-
manifest pattern (the flagship pattern, most directly relevant to the engine's
asset-description-language design work), durable/checkpointed sessions as a framework
default rather than bolt-on infrastructure, and evals as a first-class folder gating
deployment. All three cross-link to existing, more evidenced KB findings on the same
underlying problems (declarative agent construction, durable execution, eval-gated
deploys) — this source's contribution is a fresh, verifiable industry data point on how
those problems are being packaged as framework defaults, not a first discovery of any of
the underlying techniques.
