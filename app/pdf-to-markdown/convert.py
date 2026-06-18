#!/usr/bin/env python3
"""Convert PDF files to LLM-optimized markdown using pymupdf4llm."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

import pymupdf
import pymupdf4llm

SCRIPT_DIR = Path(__file__).parent
DEFAULT_OUTPUT = SCRIPT_DIR / "output"
DOWNLOADS_DIR = SCRIPT_DIR / "_downloads"


def is_url(path: str) -> bool:
    return path.startswith("http://") or path.startswith("https://")


def download_pdf(url: str) -> Path:
    """Download a PDF from a URL to a temp location. Returns local path."""
    DOWNLOADS_DIR.mkdir(exist_ok=True)
    # Extract filename from URL, fall back to hash
    url_path = url.split("?")[0].split("#")[0]
    filename = url_path.rstrip("/").split("/")[-1]
    if not filename.lower().endswith(".pdf"):
        filename = f"{abs(hash(url)) % 10**10}.pdf"
    dest = DOWNLOADS_DIR / filename
    print(f"  Downloading {url}...")
    urllib.request.urlretrieve(url, dest)
    return dest


def slugify_filename(source: str) -> str:
    """Generate a safe output filename from a source path or URL."""
    if is_url(source):
        url_path = source.split("?")[0].split("#")[0]
        name = url_path.rstrip("/").split("/")[-1]
        name = Path(name).stem if name else str(abs(hash(source)) % 10**10)
    else:
        name = Path(source).stem
    # Sanitize: keep alphanumeric, hyphens, underscores
    name = re.sub(r"[^\w\-]", "_", name)
    return name


def check_existing(slug: str, output_dir: Path) -> Path | None:
    """Return existing markdown path if already converted, None otherwise."""
    candidate = output_dir / f"{slug}.md"
    if candidate.exists() and candidate.stat().st_size > 0:
        return candidate
    return None


def convert_pdf(pdf_path: Path) -> dict:
    """Convert a PDF to markdown. Returns dict with markdown, page_count, word_count."""
    doc = pymupdf.open(str(pdf_path))
    page_count = len(doc)
    doc.close()

    md_text = pymupdf4llm.to_markdown(str(pdf_path))

    words = len(md_text.split())
    return {
        "markdown": md_text,
        "page_count": page_count,
        "word_count": words,
    }


def validate_markdown(md_text: str, page_count: int) -> dict:
    """Validate converted markdown quality. Returns {passed: bool, issues: list}."""
    issues = []
    stripped = md_text.strip()

    if not stripped:
        return {"passed": False, "issues": ["Output is empty"]}

    word_count = len(stripped.split())
    min_words = max(page_count * 20, 10)
    if word_count < min_words:
        issues.append(
            f"Low word count: {word_count} words for {page_count} pages "
            f"(expected >= {min_words})"
        )

    alpha_chars = sum(1 for c in stripped if c.isalpha())
    if alpha_chars == 0:
        issues.append("No alphabetic characters found")

    total_chars = len(stripped)
    if total_chars > 0:
        special = sum(1 for c in stripped if not c.isalnum() and not c.isspace())
        ratio = special / total_chars
        if ratio > 0.3:
            issues.append(f"High special character ratio: {ratio:.0%}")

    return {"passed": len(issues) == 0, "issues": issues}


def write_markdown(md_text: str, slug: str, metadata: dict, output_dir: Path) -> Path:
    """Write markdown with YAML frontmatter to output directory."""
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"{slug}.md"
    frontmatter = (
        "---\n"
        f'source: "{metadata["source"]}"\n'
        f'pages: {metadata["page_count"]}\n'
        f'words: {metadata["word_count"]}\n'
        f'converted: "{date.today().isoformat()}"\n'
        "---\n\n"
    )
    out_path.write_text(frontmatter + md_text, encoding="utf-8")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="Convert PDFs to markdown")
    parser.add_argument(
        "--paths", nargs="+", required=True, help="PDF file paths or URLs"
    )
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT, help="Output directory"
    )
    args = parser.parse_args()

    results = {"ok": [], "skipped": [], "failed": []}
    downloaded = []
    total = len(args.paths)

    for i, source in enumerate(args.paths, 1):
        prefix = f"[{i}/{total}]"
        slug = slugify_filename(source)

        try:
            # Idempotency check
            existing = check_existing(slug, args.output)
            if existing:
                print(f"{prefix} {slug} -- already exists, skipping")
                results["skipped"].append(source)
                continue

            # Resolve to local path
            if is_url(source):
                pdf_path = download_pdf(source)
                downloaded.append(pdf_path)
            else:
                pdf_path = Path(source)
                if not pdf_path.exists():
                    raise FileNotFoundError(f"File not found: {source}")

            # Convert
            print(f"{prefix} Converting {pdf_path.name}...")
            data = convert_pdf(pdf_path)

            # Validate
            validation = validate_markdown(data["markdown"], data["page_count"])
            if not validation["passed"]:
                warnings = "; ".join(validation["issues"])
                print(f"  WARNING: {warnings}")

            # Write output
            metadata = {
                "source": source,
                "page_count": data["page_count"],
                "word_count": data["word_count"],
            }
            out_path = write_markdown(
                data["markdown"], slug, metadata, args.output
            )

            status = "OK" if validation["passed"] else "OK (with warnings)"
            print(
                f"  {status} -- {data['page_count']} pages, "
                f"{data['word_count']} words -> {out_path.name}"
            )
            results["ok"].append(source)

        except Exception as e:
            print(f"  FAILED: {e}")
            results["failed"].append(source)

    # Cleanup downloads
    for p in downloaded:
        try:
            p.unlink()
        except OSError:
            pass
    if DOWNLOADS_DIR.exists():
        try:
            DOWNLOADS_DIR.rmdir()
        except OSError:
            pass

    # Summary
    print(f"\n--- Summary ---")
    print(f"Converted: {len(results['ok'])}  Skipped: {len(results['skipped'])}  Failed: {len(results['failed'])}")
    if results["failed"]:
        print(f"Failed sources:")
        for s in results["failed"]:
            print(f"  - {s}")

    sys.exit(1 if results["failed"] else 0)


if __name__ == "__main__":
    main()
