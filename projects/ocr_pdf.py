import os
import re
import shutil
import fitz  # PyMuPDF
import pytesseract
import cv2
import numpy as np
from PIL import Image
from unidecode import unidecode
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# ---------- CONFIGURAÇÕES ----------
PDF_ORIGINAL = r"C:\Users\Elisangela\Documents\OCR\nfse.pdf"
PDF_COPIA = r"C:\Users\Elisangela\Documents\OCR\nfse_copia.pdf"

# Caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
OCR_CONFIG = r'--oem 3 --psm 4'

# ---------- FLAN-T5 ----------
print("🧠 Carregando modelo Flan-T5...")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
print("✅ Modelo carregado.")

# ---------- FUNÇÕES ----------
def corrigir_texto_flant5(texto):
    prompt = f"Corrija pequenos erros de acentuação, espaçamento ou ortografia deste texto mantendo o conteúdo: {texto}"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_new_tokens=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def extrair_numero_nota(texto):
    texto_limpo = unidecode(texto).lower().replace("\r", "").replace("\n", " ").replace("  ", " ")
    padroes = [
        r"(?:numero\s*da\s*nota)[^\d\n]{0,15}(\d{1,12})",
        r"(?:numero\s*da\s*nota)[^\d]{0,15}\n\s*(\d{1,12})",
        r"nota\s*fiscal\s*[^\d]{0,10}(\d{1,12})"
    ]
    for p in padroes:
        m = re.search(p, texto_limpo)
        if m:
            numero = m.group(1)
            if not re.match(r"20\d{2}$", numero):
                return numero.zfill(8)
    m2 = re.search(r"\b(?!20\d{2})\d{6,8}\b", texto_limpo)
    if m2:
        return m2.group(0).zfill(8)
    return "SEM_NUMERO"

def gerar_pdf_ocr(pil_img):
    pdf_bytes = pytesseract.image_to_pdf_or_hocr(pil_img, extension='pdf', lang='por', config=OCR_CONFIG)
    return fitz.open("pdf", pdf_bytes)

# ---------- CRIA CÓPIA DO PDF ----------
shutil.copy2(PDF_ORIGINAL, PDF_COPIA)
doc = fitz.open(PDF_COPIA)
pdf_final = fitz.open()  # PDF que receberá as páginas OCR

numero_nota = "SEM_NUMERO"

for i in range(len(doc)):
    page = doc[i]
    pix = page.get_pixmap(dpi=300, alpha=False)
    mode = "RGB" if pix.n >= 3 else "L"
    pil_img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)

    # ---------- PROCESSAMENTO DE IMAGEM ----------
    img_array = np.array(pil_img)
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    gray = cv2.medianBlur(gray, 3)
    processed = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 10
    )
    processed = cv2.convertScaleAbs(processed, alpha=1.5, beta=10)

    # ---------- OCR EM TODO O DOCUMENTO ----------
    text_completo = pytesseract.image_to_string(processed, lang='por', config=OCR_CONFIG)

    # ---------- OCR NO CANTO SUPERIOR DIREITO ----------
    h, w = gray.shape

    # Ajuste fino do canto superior direito: 20% altura x 40% largura (modifique se precisar)
    canto_sup_dir = pil_img.crop((w*0.6, 0, w, h*0.2))

    # Converte para array e aplica processamento específico só para esse canto
    canto_array = np.array(canto_sup_dir)
    canto_gray = cv2.cvtColor(canto_array, cv2.COLOR_RGB2GRAY)
    canto_gray = cv2.medianBlur(canto_gray, 3)
    canto_processed = cv2.adaptiveThreshold(
        canto_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 5
    )
    canto_processed = cv2.convertScaleAbs(canto_processed, alpha=2.0, beta=20)

    # OCR só do canto com linha única (--psm 7)
    numero_texto = pytesseract.image_to_string(canto_processed, lang='por', config='--psm 7')

    # Corrige usando Flan-T5
    numero_texto_corrigido = corrigir_texto_flant5(numero_texto)

    # Extrai número da nota com Regex
    numero_nota = extrair_numero_nota(numero_texto_corrigido)

    # ---------- CORRIGE TÍTULO "Número da Nota" ----------
    text_completo_corrigido = re.sub(r"(?i)numero[^\n]*nota", "Número da Nota", text_completo)

    # ---------- GERA PDF OCR DA PÁGINA ----------
    pdf_page = gerar_pdf_ocr(pil_img)
    pdf_final.insert_pdf(pdf_page)

doc.close()
pdf_final.save(PDF_COPIA)
pdf_final.close()

print(f"\n📘 Processo concluído! Número da Nota = {numero_nota}")