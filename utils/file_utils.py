import os
from ocr.pdf_extractor import PDFTextExtractor
from ocr.tesseract_engine import TesseractEngine

pdf_extractor = PDFTextExtractor()
ocr_engine = TesseractEngine()

def extract_text_from_upload(file_bytes: bytes, filename: str) -> str:
    ext = os.path.splitext(filename)[1].lower()

    if ext == ".pdf":
        # save temporarily
        temp_path = "data/uploads/temp.pdf"
        with open(temp_path, "wb") as f:
            f.write(file_bytes)

        text = pdf_extractor.extract_text(temp_path)

        # OCR fallback
        if not text or len(text.strip()) < 50:
            text = ocr_engine.extract_text(temp_path)

        return text

    else:
        # text / doc fallback
        try:
            return file_bytes.decode("utf-8")
        except:
            return file_bytes.decode("latin-1", errors="ignore")
