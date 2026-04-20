---
notion_id: 32b1e08b-9b34-816e-a604-e4cd20f346a2
name: 'SKILL.md Format: YAML Front Matter Requirements'
summary: Anthropic's Claude Skill format requires a specific YAML front matter block (name in lowercase, description) between triple-dash delimiters at the top of a file named SKILL.md (uppercase), packaged
  inside a folder and zipped for upload. Missing either front matter or correct filename causes upload errors.
implementation_notes: null
category: Prompt Craft
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P3
applicability:
- Perplexity Skills
adopted_in: null
sources:
- claude-skills-vs-projects-how-i-use-them.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings: []
pipeline_status: raw
consumed_by: []
---
# SKILL.md Format: YAML Front Matter Requirements

## What It Is
Technical requirements for Claude Skills: (1) File must be named `SKILL.md` (all uppercase). (2) File must begin with YAML front matter: three dashes `---`, then `name: skill-name-lowercase` (no spaces, lowercase or numerals only), then `description: what this skill does`, then closing `---`. (3) The SKILL.md file must be placed inside a folder (not alone), then the folder is right-click -> Compress to create a zip file. (4) Upload via Claude -> Customize -> Skills -> + -> drag zip file. The skill name and description appear in Claude's skill browser; the rest of the file is the markdown instruction content. Claude when generating skills often omits the front matter or generates incorrect formatting — manual correction is required.

## Why It Matters
Without the correct format, skill uploads fail silently or throw errors. The YAML front matter is the machine-readable interface that Anthropic's system uses to identify, index, and surface skills. Understanding this format is prerequisite to the entire skill system. The specific requirement that SKILL.md be inside a folder (not just the file itself) is non-obvious and commonly missed.

## Why People Are Using It
Once understood, the format is simple and enables a library of reusable capabilities across all Claude interactions. The description field determines how Claude's skill auto-detection works — a clear description improves automatic invocation accuracy.

## Potential Alternatives
Claude Projects system instructions (no packaging required, not reusable across projects), API system prompts (no upload UI, requires API access).

## Potential Improvements
Claude should generate skills with correct front matter by default — it currently gets this wrong. A skill validation utility that checks format before upload would reduce friction. Anthropic could simplify to just a file upload (no folder+zip ceremony).

## Potential Failure Modes
Incorrect filename case (skill.md instead of SKILL.md). Missing front matter causes parsing failure. Name field with spaces or uppercase causes errors. Uploading the file directly without a folder wrapper fails.
