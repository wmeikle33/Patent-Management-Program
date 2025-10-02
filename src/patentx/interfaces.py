from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Dict, Any, Protocol, runtime_checkable

Record = Dict[str, Any]

@dataclass
class Document:
    content: str
    meta: Dict[str, Any]

@runtime_checkable
class Loader(Protocol):
    def load(self) -> Iterable[Document]:
        ...

@runtime_checkable
class Extractor(Protocol):
    def extract(self, doc: Document) -> Record:
        ...

@runtime_checkable
class Sink(Protocol):
    def write(self, rows: Iterable[Record]) -> None:
        ...
