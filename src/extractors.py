from __future__ import annotations
import re
from typing import Dict, Any
from .interfaces import Extractor, Document, Record

class RegexPatentExtractor(Extractor):
    _re_num = re.compile(r"(?im)^\s*Patent\s+Number\s*:\s*(?P<num>[A-Za-z0-9\-/]+)")
    _re_title = re.compile(r"(?im)^\s*Title\s*:\s*(?P<title>.+)")
    _re_assignee = re.compile(r"(?im)^\s*Assignee\s*:\s*(?P<assignee>.+)")
    _re_date = re.compile(r"(?im)^\s*Filing\s+Date\s*:\s*(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2}|[A-Za-z]{3,9}\s+\d{1,2},\s*\d{4})")
    _re_abstract = re.compile(r"(?is)Abstract\s*:\s*(?P<abs>.+?)(?:\n\s*\n|\Z)")

    def extract(self, doc: Document) -> Record:
        txt = doc.content or ""
        rec: Dict[str, Any] = {"source_path": doc.meta.get("path")}
        m = self._re_num.search(txt)
        if m: rec["patent_number"] = m.group("num").strip()
        m = self._re_title.search(txt)
        if m: rec["title"] = m.group("title").strip()
        m = self._re_assignee.search(txt)
        if m: rec["assignee"] = m.group("assignee").strip()
        m = self._re_date.search(txt)
        if m: rec["filing_date"] = m.group("date").strip()
        m = self._re_abstract.search(txt)
        if m:
            rec["abstract"] = re.sub(r"\s+", " ", m.group("abs").strip())
        return rec
