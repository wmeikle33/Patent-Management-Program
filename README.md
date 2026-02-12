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

## Extension Guide

-Add a New Loader

-Add a New Sink

Sinks should not mutate records.
Sinks should accept any iterable (list, generator).
Use UTF-8 everywhere.
For file sinks, create parent dirs if needed (optional but nice).
If writing fails, raise a clear error (e.g., OutputWriteError(out_path, reason)).

-Add a New Extractor

## Limitations
