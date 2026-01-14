# Private Implementations (How to plug in)
Implement a PdfToTextLoader in a private repo and import the public interfaces from `patentx`.

# Recommended Repo Layout
patent-private-impl/                 (private repo)
  src/
    patent_private_impl/
      __init__.py
      pdf_loader.py                 
      register.py                   
  pyproject.toml
  README.md
