---
name: "Dark Code — Spec-Driven Dev, Comprehension Gates, Context Eng for Legibility"
source_type: "Video"
status: "Done"
key_takeaways: "Dark code (AI-generated code nobody understands) is an organizational capability problem, not a tooling problem. The three-layer fix is: spec-driven development to force comprehension before code exists, self-describing codebases via structural and semantic context layers, and AI-assisted comprehension gates at PR review. The spec becomes the eval — a clearly written spec is the test the agent iterates against."
relevance: "High"
added_by: "Nick"
tags:
  - "dark-code"
  - "spec-driven-development"
  - "context-engineering"
  - "comprehension-gate"
  - "codebase-legibility"
  - "eval-driven-development"
url: "https://www.youtube.com/watch?v=E1idsrv79tI"
authority:
  - "dark-code-channel.md"
findings:
  - "dark-code-organizational-capability-problem.md"
  - "self-describing-codebase-structural-semantic-context.md"
  - "spec-as-source-of-truth-for-agent-construction.md"
  - "eval-driven-development-autonomous-quality.md"
date_added: "2026-04-20"
date_processed: "2026-04-20"
---

# Dark Code — Spec-Driven Dev, Comprehension Gates, Context Eng for Legibility

YouTube video covering the "dark code" problem (AI-generated code that passed tests but was never understood by anyone), why the obvious responses (observability, better pipelines, accepting dark code) don't solve the root cause, and a three-layer organizational response: spec-driven development, self-describing codebases, and AI-assisted comprehension gates.

Key supporting evidence: Amazon rebuilt their AI coding tool Kira after a December 2025 outage to lead with spec-driven development — turning prompts into requirements and task lists before code generation. The spec-becomes-eval insight bridges spec-driven development and eval-driven development as complementary practices.
