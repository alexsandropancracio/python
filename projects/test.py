import fitz  # PyMuPDF
import pytesseract
import cv2
from PIL import Image
import os
import re

# Caminho do PDF
pdf_path = r"C:\Users\Elisangela\Documents\OCR\nfse.pdf"

# Caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Diretório temporário para imagens
temp_dir = r"C:\Users\Elisangela\Documents\OCR\temp"
os.makedirs(temp_dir, exist_ok=True)

# Abrindo PDF
doc = fitz.open(pdf_path)

# Dicionário de correções específicas
correcoes = {
    "Nimero da Nota": "Número da Nota",
    "FEmissão": "Emissão",
    "Socíal?": "Social",
    "Inserição Municipal": "Inscrição Municipal",
    "Endoreço": "Endereço",
    "NES-e foí": "NFS-e foi",
    "crêdito": "crédito",
    "6 RPS": "o RPS",
    "&": "@",
    "E ”:faâv A": "",
    "o | |": "",
    "Folder. L": "Folder:",
    "Vl": "Valor"
}

print("🧠 Iniciando OCR e correções...")

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    pix = page.get_pixmap(dpi=300, alpha=False)
    img_path = os.path.join(temp_dir, f"page_{page_num + 1}.png")
    pix.save(img_path)

    # Leitura e pré-processamento da imagem
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    processed = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31, 10
    )
    processed = cv2.convertScaleAbs(processed, alpha=1.5, beta=10)
    treated_path = os.path.join(temp_dir, f"treated_{page_num + 1}.png")
    cv2.imwrite(treated_path, processed)

    # OCR
    config = r'--oem 3 --psm 4'
    texto_ocr = pytesseract.image_to_string(Image.open(treated_path), lang='por', config=config)

    # Aplicando correções específicas
    for erro, certo in correcoes.items():
        texto_ocr = texto_ocr.replace(erro, certo)

    # Limpeza extra de caracteres estranhos
    texto_ocr = re.sub(r"[^a-zA-Z0-9À-ú\s.,:;@%-/]", "", texto_ocr)

    # Exibindo resultado no terminal
    print(f"\n--- Página {page_num + 1} ---")
    print(texto_ocr.strip() or "(sem texto reconhecido)")

doc.close()
print("\n✅ OCR concluído com sucesso!")
