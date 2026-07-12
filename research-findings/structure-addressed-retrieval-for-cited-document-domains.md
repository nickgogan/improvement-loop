---
name: "Structure-Addressed Retrieval for Cited-Document Domains"
summary: |-
  Plain English: in domains where documents cite each other by section (insurance denials
  must cite the policy language they rely on), you don't need to search for anything — you
  already know the address of the text that matters, so vector search adds nothing. The
  agent retrieves by structure: denial reason -> the exact policy section it cites -> the
  deadline -> the document checklist. No vector database, no similarity search. First
  retrieval act is a sanity check with teeth: does the cited section actually say what the
  letter implies it says? Sometimes it doesn't — and that mismatch is finding number one
  of the appeal. Extends the file-search-beats-RAG line with a sharper claim: citation
  structure makes retrieval deterministic regardless of corpus size.
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3"
applicability:
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "i-pointed-my-agent-at-the-bills.md"
related_findings:
  - file: "file-search-outperforms-rag-for-small-corpora.md"
    rel: "extends"
  - file: "scale-threshold-heuristic-obsidian-vs-rag.md"
    rel: "same-problem"
  - file: "index-file-navigation-as-rag-replacement.md"
    rel: "same-problem"
  - file: "nine-primitive-document-agent-skeleton.md"
    rel: "enabled-by"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

# Structure-Addressed Retrieval for Cited-Document Domains

## What It Is

A retrieval strategy for domains whose documents carry explicit cross-references:
regulatory and policy documents, denial letters, contracts, legal filings, standards. The
ingest/chunk stages tag every piece as addressable (policy section IDs, claim numbers,
deadlines); retrieval then follows the citations rather than computing similarity. "You're
not searching for something you can't find — you already know the address of the thing
that's hurting you." The retrieval step doubles as verification: fetch the cited section
and check that it says what the citing document claims.

## Why It Matters

It refines the corpus-size framing of the file-search-vs-RAG debate. The existing KB
findings say lexical/file search wins for *small* corpora; this adds an orthogonal axis —
*citation density*. Where documents self-address, retrieval is deterministic at any corpus
size, and the lossy compression of embeddings is not merely unnecessary but actively
harmful (a similarity match to the *wrong* policy section is a case-losing error, and the
cited-vs-implied mismatch check only works with exact addressing). The engine's own KB
practice (frontmatter filenames as relations, rg on fields) is the same principle.

## Why People Are Using It

Demonstrated in the insurance-appeal build against a real insurer's published policy
documents. The cited-section sanity check surfacing real denial-letter/policy mismatches
is the concrete payoff.

## Potential Alternatives

Vector RAG (needed when queries are exploratory and documents don't self-address); hybrid
retrieval (structure-first, similarity fallback for uncited questions — mirrors the KB's
query-router findings from the OKF cluster).

## Potential Improvements

Formalize the address schema per domain (section IDs, claim numbers) at ingest time; add
the cited-vs-implied mismatch check as a standard verification primitive wherever sources
cite sources.

## Potential Failure Modes

Domains with sloppy or missing citations degrade to search anyway — the pattern needs a
fallback. OCR/ingest errors corrupt addresses silently, which is worse than fuzzy search
because the system *looks* deterministic. Address schemas differ per insurer/agency;
normalization cost is real.
