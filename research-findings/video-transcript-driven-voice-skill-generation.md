---
notion_id: 32b1e08b-9b34-81d7-a247-e9f3ab9e05d7
name: Video Transcript-Driven Voice Skill Generation
summary: Using existing video transcripts as training material for Claude to generate a personalized voice/style skill produces a more comprehensive skill than manual writing — capturing idiosyncratic language
  patterns, sentence rhythm, and characteristic phrases that the author wouldn't consciously document.
implementation_notes: null
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- Perplexity Skills
adopted_in: []
sources:
- claude-skills-vs-projects-how-i-use-them.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Video Transcript-Driven Voice Skill Generation

## What It Is
Eamonn provides Claude with several video transcripts (his own recorded videos, ranging from short to 20-30 min) and prompts it to extract and document his voice characteristics into a skill file. The generated skill includes: purpose, who Eamonn is, voice context, core voice characteristics, specific language patterns (discovered idioms: 'bonkers', 'pretty darn', 'for crying out loud'), sentence structure patterns (short-medium-long rhythm with run-ons during explanations), how he opens and closes, what the voice is NOT, banned phrases (AI jargon), and content-specific notes. Claude produced a more thorough analysis than Eamonn would have written manually.

## Why It Matters
Voice consistency is a practical challenge for AI-assisted writing. Manually articulating one's own style is notoriously difficult — writers often can't describe their own patterns. Using actual speech/text samples as training data lets Claude infer patterns empirically rather than relying on self-description. This generalizes to any skill domain where examples are more informative than manual specification.

## Why People Are Using It
Lower barrier to skill creation: you don't need to be a prompt engineer or deeply self-aware about your style. Any collection of representative examples (transcripts, emails, past articles) can serve as training material. The AI does the pattern extraction work.

## Potential Alternatives
Manual style guides written by the author, fine-tuning on personal text (more effective but requires API access and compute), copyeditor-developed style guides.

## Potential Improvements
Iterative refinement loop: author reviews generated skill, flags inaccuracies, Claude updates. Multi-modal voice capture: include audio samples for prosody patterns beyond lexical features. Versioned skills that update as the author's style evolves.

## Potential Failure Modes
Skill captures idiosyncrasies but also errors/bad habits from transcripts. Short sample set produces biased pattern extraction. Claude identifies false patterns (correlation artifacts from small sample). The generated skill still required manual editing in Eamonn's case.
