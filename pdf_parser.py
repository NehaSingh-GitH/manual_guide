"""PDF text extraction module."""

import fitz  # pymupdf


class PDFDocument:
    """Represents a parsed PDF document with extracted text."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.pages: list[dict] = []
        self.total_pages = 0
        self._load()

    def _load(self):
        """Load and extract text from the PDF."""
        doc = fitz.open(self.file_path)
        self.total_pages = len(doc)

        for page_num in range(self.total_pages):
            page = doc[page_num]
            text = page.get_text()
            self.pages.append({
                "page_number": page_num + 1,
                "text": text.strip()
            })

        doc.close()

    def get_full_text(self) -> str:
        """Get all text with page markers."""
        sections = []
        for page in self.pages:
            if page["text"]:
                sections.append(
                    f"[Page {page['page_number']}]\n{page['text']}"
                )
        return "\n\n".join(sections)

    def get_page_text(self, page_number: int) -> str | None:
        """Get text from a specific page (1-indexed)."""
        if 1 <= page_number <= self.total_pages:
            return self.pages[page_number - 1]["text"]
        return None


def load_pdf(file_path: str) -> PDFDocument:
    """Load a PDF file and return a PDFDocument object."""
    return PDFDocument(file_path)
