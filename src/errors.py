from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


class PatentXError(Exception):
    """Base class for expected (non-bug) errors in the pipeline."""


@dataclass
class UnsupportedFormatError(PatentXError):
    path: str
    detected: Optional[str] = None

    def __str__(self) -> str:
        msg = f"Unsupported input format: {self.path}"
        if self.detected:
            msg += f" (detected={self.detected})"
        return msg


@dataclass
class ParseError(PatentXError):
    field: str
    reason: str
    path: Optional[str] = None

    def __str__(self) -> str:
        loc = f" in {self.path}" if self.path else ""
        return f"ParseError{loc}: field={self.field} reason={self.reason}"


@dataclass
class OutputWriteError(PatentXError):
    out_path: str
    reason: str

    def __str__(self) -> str:
        return f"Failed to write output to {self.out_path}: {self.reason}"
