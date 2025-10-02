from __future__ import annotations
import csv, json, pathlib
from typing import Iterable, List
from .interfaces import Loader, Sink, Document, Record

class TextFolderLoader(Loader):
    def __init__(self, folder: str, encoding: str = "utf-8") -> None:
        self.folder = folder
        self.encoding = encoding

    def load(self) -> Iterable[Document]:
        root = pathlib.Path(self.folder)
        for p in sorted(root.glob("*.txt")):
            yield Document(content=p.read_text(encoding=self.encoding), meta={"path": str(p)})

class CSVSink(Sink):
    def __init__(self, path: str, encoding: str = "utf-8") -> None:
        self.path = path
        self.encoding = encoding

    def write(self, rows: Iterable[Record]) -> None:
        rows = list(rows)
        if not rows:
            open(self.path, "w", encoding=self.encoding).close()
            return
        fieldnames = sorted(set().union(*[r.keys() for r in rows]))
        with open(self.path, "w", newline="", encoding=self.encoding) as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            for r in rows:
                w.writerow(r)

class JSONLSink(Sink):
    def __init__(self, path: str, encoding: str = "utf-8") -> None:
        self.path = path
        self.encoding = encoding

    def write(self, rows: Iterable[Record]) -> None:
        with open(self.path, "w", encoding=self.encoding) as f:
            for r in rows:
                import json
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

class InMemorySink(Sink):
    def __init__(self) -> None:
        self.data: List[Record] = []
    def write(self, rows: Iterable[Record]) -> None:
        self.data = list(rows)
