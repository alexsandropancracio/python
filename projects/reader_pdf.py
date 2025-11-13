from PyPDF2 import PdfReader

caminho_pdf = r"C:\Users\Elisangela\Documents\OCR\nfse_ocr.pdf"
reader = PdfReader(caminho_pdf)
page = reader.pages[0]
print(page.extract_text())
