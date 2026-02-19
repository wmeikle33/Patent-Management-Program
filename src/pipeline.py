from __future__ import annotations
from typing import Iterable
from .interfaces import Loader, Extractor, Sink, Record

def run_pipeline(loader: Loader, extractor: Extractor, sink: Sink) -> None:
    rows: Iterable[Record] = (extractor.extract(doc) for doc in loader.load())
    sink.write(rows)
