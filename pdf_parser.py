import io
import pdfplumber


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    if not pdf_bytes:
        raise ValueError("Empty PDF file")

    text = ""
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    if not text.strip():
        raise ValueError("No readable text found in PDF")

    return text.lower()
