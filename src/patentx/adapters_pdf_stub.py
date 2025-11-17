from __future__ import annotations
from .interfaces import Loader, Document

class PdfToTextLoader(Loader):
    def __init__(self, *args, **kwargs) -> None:
        raise NotImplementedError("PdfToTextLoader is intentionally omitted in the public sample.")
