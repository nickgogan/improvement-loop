---
name: "A field guide to Claude Fable 5: Finding your unknowns"
source_type: "Blog Post"
status: "Done"
key_takeaways: |-
  Anthropic first-party guide (Thariq Shihipar, MTS, Claude Code team) arguing
  that work quality with frontier agents is bottlenecked by the human's ability
  to clarify unknowns, not by model capability. Map-vs-territory framing; the
  four-quadrant unknowns matrix (known/unknown x knowns/unknowns); phase-anchored
  techniques with exact suggested wordings — blind spot pass, brainstorm/
  prototype-to-react, interview-me (architecture-changing questions first),
  references-as-spec, decision-led implementation plans, implementation-notes.md
  deviation logging, fresh-context handoff, pitch/explainer packaging, and a
  quiz-me comprehension gate before merging. Primary source behind the
  pw79ro49CzU REJECT (secondhand walkthrough).
relevance: "High"
added_by: "Nick"
tags:
  - "prompt-engineering"
  - "claude-code"
  - "intent-engineering"
url: "https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns"
authority:
  - "anthropic.md"
findings:
  - "frontier-model-as-unknown-unknown-elicitor.md"
  - "unknowns-reduction-phase-anchored-technique-set.md"
date_added: "2026-07-12"
date_processed: "2026-07-12"
date_published: "2026-07-06"
---

# A field guide to Claude Fable 5: Finding your unknowns

Anthropic blog, 2026-07-06, by Thariq Shihipar. Fetched as the primary source
behind the rejected secondhand walkthrough video (pw79ro49CzU). Session-136
extraction notes:

- Core claim: "Fable's bottleneck" — output quality is constrained by the
  human's ability to surface and articulate unknowns, a learnable skill.
- Four unknowns quadrants with a technique mapped to each; techniques are
  phase-anchored (before / during / after implementation) and each carries
  exact suggested prompt wording (e.g., use the literal phrases "blind spot
  pass" and "unknown unknowns").
- Instructional balance principle: over-specification blocks pivots,
  under-specification forces assumptions.
- During-implementation: implementation-notes.md with a Deviations section
  (conservative option + log + keep going), then fresh-context handoff carrying
  spec + prototype + notes.
- After: package artifacts for reviewer buy-in; quiz-me gate ("a quiz at the
  bottom on the changes that I must pass") before merge.
