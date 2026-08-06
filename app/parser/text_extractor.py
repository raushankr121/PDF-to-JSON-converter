# pyrefly: ignore [missing-import]

class TextExtractor:
    def extract_text(self, page):
        return page.get_text().strip()
