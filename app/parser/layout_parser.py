import fitz


class LayoutParser:

    def __init__(self, page):
        self.page = page

    def extract_layout(self):
        return self.page.get_text("dict")