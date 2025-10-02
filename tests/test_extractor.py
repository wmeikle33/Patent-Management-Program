from patentx.extractors import RegexPatentExtractor
from patentx.interfaces import Document

def test_regex_extractor_basic():
    txt = (
        "Patent Number: US-1234567-B2\n"
        "Title: Widget for Efficient Data Processing\n"
        "Assignee: Acme Corp\n"
        "Filing Date: 2021-05-12\n"
        "\n"
        "Abstract: A widget that processes data efficiently across diverse\n"
        "computing environments.\n"
    )
    rec = RegexPatentExtractor().extract(Document(content=txt, meta={"path": "sample"}))
    assert rec["patent_number"] == "US-1234567-B2"
    assert rec["title"].startswith("Widget for")
    assert rec["assignee"] == "Acme Corp"
    assert rec["filing_date"] == "2021-05-12"
    assert "processes data efficiently" in rec["abstract"]
