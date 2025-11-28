class TextFolderLoader:
    def __init__(self, folder: str, encoding: str = "utf-8", pattern: str = "*.txt") -> None:
        self.folder = Path(folder)
        self.encoding = encoding
        self.pattern = pattern
