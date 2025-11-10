import os
import shutil
import ocrmypdf

tesseract_folder = r"C:\Program Files\Tesseract-OCR"
os.environ["PATH"] = tesseract_folder + os.pathsep + os.environ.get("PATH", "")

entrada = r"C:\Users\Elisangela\Documents\OCR\nfse.pdf"
saida = r"C:\Users\Elisangela\Documents\OCR\nfse_ocr_skiptext.pdf"

try:
    ocrmypdf.ocr(
        input_file=entrada,
        output_file=saida,
        language="por",
        skip_text=True,    
        force_ocr=False, 
        redo_ocr=False,
        optimize=0,
        clean=False,
        deskew=True,
        progress_bar=True,
        use_threads=True
    )
    print("✅ OCR concluído (skip_text). Arquivo:", saida)

except Exception as e:
    print("❌ Erro ao processar OCR:", e)

