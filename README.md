## Architecture

- **Loaders**  
  Turn PDF / TXT into raw text or intermediate objects.

- **Extractors**  
  Parse metadata via regex/rules/ML.

- **Models**  
  Dataclasses / Pydantic models for patent metadata.

- **Sinks**  
  Write results to CSV / JSONL / DB, etc.

- **CLI**  
  Argument parsing and wiring the pipeline together.
  
# Patent PDF Extractor (Sample / Redacted)

This repository is a **public, redaction‑safe sample** of a company program that extracts
structured metadata from **patent PDFs**. It demonstrates sample code without exposing any proprietary logic.

> ✅ You can share this repo publicly. Proprietary parsing rules, vendor/OCR config, and corp data are **not** included.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
pip install -r requirements-dev.txt

# Demo (TXT loader + regex extractor)
python -m patentx.cli --input sample_data --out sample_data/out.csv --sink csv

# Run tests
pytest -q
```
- CLI tool to batch-extract metadata from patent PDFs / TXT exports
- Pure-Python package (`pip install -e .`) with a simple `patentx.cli` entrypoint
- Sample patents in `sample_data/` plus unit tests in `tests/`
- Designed as a redaction-safe public sample of production IP tooling

## What Fields are Extracted

-Date
-Financial Information

## Extension Guide

-Add a New Loader

-Add a New Sink

Sinks should not mutate records.
Sinks should accept any iterable (list, generator).
Use UTF-8 everywhere.
For file sinks, create parent dirs if needed (optional but nice).
If writing fails, raise a clear error (e.g., OutputWriteError(out_path, reason)).

-Add a New Extractor

Return None for missing fields (don’t use "N/A").
Keep parsing pure: no file I/O inside extractors.
Normalize consistently:
strip whitespace
collapse internal whitespace
keep original capitalization unless you have a reason to normalize
Prefer explicit failures for malformed required fields (raise ParseError) vs silently wrong data.


## Limitations

This project is intended as a lightweight demonstration of a modular patent text extraction pipeline. It is not a production-grade patent analytics system.
Input format sensitivity: Extraction works best on born-digital PDFs. Scanned/image-only PDFs are not supported without external OCR preprocessing.
Layout variability: Patent formats vary across jurisdictions and publication years. Extraction rules were developed against a limited sample and may fail on unusual layouts.
Heuristic-based extraction: Most fields are extracted using rule-based methods (regex and section heuristics). Accuracy depends on formatting consistency.
Incomplete metadata handling: Multiple assignees, nested applicant structures, and edge-case date formats may not be handled correctly.
No legal validation: Extracted data should not be used for legal or regulatory decisions.
Limited evaluation: No large-scale precision/recall benchmarking has been performed.
Not optimized for scale: The pipeline has not been tested on large (>10k document) corpora or distributed environments.
