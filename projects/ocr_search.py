import os
import re
import fitz
import pytesseract
import cv2
import numpy as np
from PIL import Image
from unidecode import unidecode

pasta_raiz = r"C:\Users\Elisangela\Documents\OCR"
pasta_ativas = os.path.join(pasta_raiz, "NFSE - Ativas")
pasta_canceladas = os.path.join(pasta_raiz, "NFSE - Canceladas")
pasta_debug = os.path.join(pasta_raiz, "temp_ocr")

os.makedirs(pasta_ativas, exist_ok=True)
os.makedirs(pasta_canceladas, exist_ok=True)
os.makedirs(pasta_debug, exist_ok=True)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
config = r'--oem 3 --psm 4'

def extrair_numero_nota(texto):
    texto_limpo = unidecode(texto).lower()
    texto_limpo = texto_limpo.replace("\r", "").replace("\n", " ").replace("  ", " ")

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

    return "sem-numero"

def gerar_pdf_ocr(pil_img):
    pdf_bytes = pytesseract.image_to_pdf_or_hocr(pil_img, extension='pdf', lang='por', config=config)
    return fitz.open("pdf", pdf_bytes)

def ensure_unique_path(path):
    base, ext = os.path.splitext(path)
    i = 1
    new = path
    while os.path.exists(new):
        new = f"{base}_{i}{ext}"
        i += 1
    return new

for nome_arquivo in os.listdir(pasta_raiz):
    if not nome_arquivo.lower().endswith(".pdf"):
        continue

    caminho_pdf = os.path.join(pasta_raiz, nome_arquivo)
    print(f"\n📄 Processando: {nome_arquivo}")

    try:
        doc = fitz.open(caminho_pdf)
        pdf_out = fitz.open()
        texto_total = ""
        numero_nota = "sem-numero"

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap(dpi=300, alpha=False)
            mode = "RGB" if pix.n >= 3 else "L"
            pil_img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)

            gray = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2GRAY)
            gray = cv2.medianBlur(gray, 3)
            processed = cv2.adaptiveThreshold(
                gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 10
            )

            processed = cv2.convertScaleAbs(processed, alpha=1.5, beta=10)

            text = pytesseract.image_to_string(processed, lang='por', config=config)
            texto_total += text + "\n"

            if page_num == 0:
                numero_nota = extrair_numero_nota(text)

            ocr_pdf = gerar_pdf_ocr(pil_img)
            pdf_out.insert_pdf(ocr_pdf)

        doc.close()

        texto_busca = unidecode(texto_total).lower().replace(" ", "")
        palavras_cancel = ["cancelada", "cancelamento", "foicancelada", "notacancelada"]
        is_cancelada = any(p in texto_busca for p in palavras_cancel)

        pasta_dest = pasta_canceladas if is_cancelada else pasta_ativas
        novo_nome = f"nfse-{numero_nota}.pdf"
        caminho_destino = ensure_unique_path(os.path.join(pasta_dest, novo_nome))

        pdf_out.save(caminho_destino)
        pdf_out.close()

        print(f"✅ Salvo como: {caminho_destino} | Cancelada={is_cancelada} | Número={numero_nota}")

    except Exception as e:
        print(f"⚠️ Erro ao processar {nome_arquivo}: {e}")

print("\n🎯 Processo concluído.")
