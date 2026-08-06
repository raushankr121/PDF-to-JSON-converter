import fitz
from typing import List, Dict, Any
from app.models.page import Page
from app.models.document import Document



class PDFReader:
    """
    Handles all PDF-related operations.

    Responsibilities:
    - Open PDF
    - Inspect PDF
    - Extract page information
    """

    def __init__(self, pdf_path: str):
        """
        Initialize the PDF reader.

        Args:
            pdf_path (str): Path to the PDF file.
        """
        self.pdf_path = pdf_path

        try:
            self.doc = fitz.open(pdf_path)
        except Exception as e:
            raise Exception(f"Unable to open PDF: {e}")

    def total_pages(self) -> int:
        """
        Returns the total number of pages.
        """
        return len(self.doc)

    def get_page(self, page_number: int):
        """
        Returns a specific page.

        Args:
            page_number (int): Zero-based page index.

        Returns:
            fitz.Page
        """
        if page_number < 0 or page_number >= len(self.doc):
            raise IndexError("Invalid page number.")

        return self.doc.load_page(page_number)

    def inspect(self) -> None:
        """
        Prints information about every page.
        Useful for debugging.
        """

        print("=" * 60)
        print("PDF INFORMATION")
        print("=" * 60)

        print(f"File        : {self.pdf_path}")
        print(f"Total Pages : {self.total_pages()}")

        for i, page in enumerate(self.doc):

            text = page.get_text().strip()

            print("\n" + "-" * 60)
            print(f"Page {i + 1}")

            print(f"Width      : {page.rect.width}")
            print(f"Height     : {page.rect.height}")
            print(f"Rotation   : {page.rotation}")
            print(f"Characters : {len(text)}")

            if len(text) == 0:
                print("Type       : Likely Scanned PDF")
            else:
                print("Type       : Digital PDF")

            preview = text[:150].replace("\n", " ")

            print(f"Preview    : {preview}")

    def extract_pages(self) -> List[Page]:
        """
        Extracts all pages into a structured format using the Page model.

        Returns:
            List[Page]
        """

        pages = []

        for i, page in enumerate(self.doc):

            text = page.get_text().strip()

            page_obj = Page(
                page_number=i + 1,
                width=page.rect.width,
                height=page.rect.height,
                rotation=page.rotation,
                is_scanned=len(text) == 0,
                text=text,
            )

            pages.append(page_obj)

        return pages

    def extract_document(self):
        pages = self.extract_pages()

        document = Document(
            file_name=self.pdf_path,
            total_pages=self.total_pages(),
            pages=pages,
            metadata=self.get_metadata()
        )

        return document

    def get_metadata(self) -> Dict[str, Any]:
        """
        Returns PDF metadata.

        Returns:
            Dict
        """

        return self.doc.metadata

    def close(self):
        """
        Close the PDF document.
        """
        self.doc.close()