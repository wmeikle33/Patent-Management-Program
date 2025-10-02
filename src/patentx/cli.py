from __future__ import annotations
import argparse
from .adapters_text import TextFolderLoader, CSVSink, JSONLSink
from .extractors import RegexPatentExtractor
from .pipeline import run_pipeline

def main() -> None:
    p = argparse.ArgumentParser(description="Public sample CLI (TXT loader + regex extractor).")
    p.add_argument("--input", "-i", required=True, help="Folder with *.txt (public demo).")
    p.add_argument("--out", "-o", required=True, help="Output file path (csv/jsonl).")
    p.add_argument("--sink", choices=["csv","jsonl"], default="csv")
    args = p.parse_args()

    loader = TextFolderLoader(args.input)
    extractor = RegexPatentExtractor()
    sink = CSVSink(args.out) if args.sink == "csv" else JSONLSink(args.out)

    run_pipeline(loader, extractor, sink)

if __name__ == "__main__":
    main()
