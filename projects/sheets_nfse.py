import os
import re
import csv
import fitz
from unidecode import unidecode

pasta_ativas = r"C:\Users\Elisangela\Documents\OCR\nfse_ocr"
pasta_planilhas = os.path.join(pasta_ativas, "Planilhas")
os.makedirs(pasta_planilhas, exist_ok=True)

arquivo_saida = os.path.join(pasta_planilhas, "relatorio_nfse.csv")

def limpar_texto(texto):
    if not texto:
        return ""
    t = unidecode(texto)
    t = t.replace("\r", " ").replace("\n", " ")
    t = re.sub(r"\s+", " ", t)
    return t.strip()

def extrair_numero_nota(texto):
    texto_limpo = unidecode(texto).lower()
    texto_limpo = texto_limpo.replace("\r", " ").replace("\n", " ").replace("  ", " ")

    padroes = [
        r"(?:numero\s*da\s*nota)[^\d\n]{0,30}([a-z]{0,3}\s*\d{1,12})",
        r"(?:nota\s*fiscal)[^\d\n]{0,30}([a-z]{0,3}\s*\d{1,12})",
        r"\b[a-z]{0,3}\s*\d{6,12}\b"
    ]

    for p in padroes:
        m = re.search(p, texto_limpo)
        if m:
            try:
                numero_bruto = m.group(1) if m.lastindex and m.lastindex >= 1 else m.group(0)
                numero = re.sub(r"\D", "", numero_bruto)
                if numero and not re.match(r"20\d{2}$", numero):
                    return numero.zfill(8)
            except Exception as e:
                print(f"⚠️ Erro ao processar padrão '{p}': {e}")

    m2 = re.search(r"\b(?!20\d{2})\d{5,12}\b", texto_limpo)
    if m2:
        return m2.group(0).zfill(8)

    return "sem-numero"


def extrair_valor(texto):
    txt = limpar_texto(texto).upper()
    m = re.search(r"(?:VALOR\s*(?:TOTAL\s*(?:DO|DOS)?\s*SERVI[CÇ]OS?|DO\s*SERVI[CÇ]O)[^\dR$]{0,12}(?:R\$)?\s*=?\s*([\d\.\s]+,\d{2}))", txt)
    if not m:
        m = re.search(r"R\$\s*([\d\.\s]+,\d{2})", txt)
    if m:
        val = m.group(1).replace(" ", "").replace(".", "").replace(",", ".")
        try:
            return f"{float(val):.2f}"
        except:
            return val
    return ""

def extrair_cpf_cnpj(texto):
    txt = limpar_texto(texto)
    m = re.search(r"(\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}|\d{3}\.\d{3}\.\d{3}\-\d{2}|\d{14}|\d{11})", txt)
    return m.group(0) if m else ""

def extrair_nome_razao(texto):
    txt = limpar_texto(texto).upper()
    m = re.search(r"(?:NOME\/RAZAO\s*SOCIAL[:\s]*|RAZAO\s*SOCIAL[:\s]*|NOME[:\s]*)([A-Z0-9\.\,\-\&\s]{3,200})", txt)
    if m:
        return m.group(1).strip()
    m2 = re.search(r"\b([A-Z]{3}[A-Z0-9\.\,\-\&\s]{3,150})\b", txt)
    return m2.group(1).strip() if m2 else ""

def extrair_endereco(texto):
    txt = limpar_texto(texto).upper()
    m = re.search(r"(?:ENDEREC[COO]|ENDEREÇO)[:\s]*([A-Z0-9\.\,\-\º\ª\/\s]+?CEP[:\s]*\d{5}-\d{3})", txt)
    if m:
        return m.group(1).strip()
    m2 = re.search(r"([A-Z0-9\.\,\-\º\ª\/\s]+CEP[:\s]*\d{5}-\d{3})", txt)
    return m2.group(1).strip() if m2 else ""

def extrair_municipio_uf(texto):
    txt = limpar_texto(texto).upper()

    m = re.search(r"(?:MUNICIPIO|MUNIC[IÍ]PIO)[:\s]*([A-Z\-\s]+)", txt)
    municipio = m.group(1).strip() if m else ""
    municipio = re.sub(r'^\s*DE\s+', '', municipio, flags=re.IGNORECASE).strip()

    uf = ""
    m_uf = re.search(r"(?:UF[:\s]*|-\s*|,)([A-Z]{2})(?:\b|$)", txt)
    if m_uf:
        uf = m_uf.group(1)
    else:
        if municipio:
            padrao = re.escape(municipio) + r"[\s\,\-\/]{1,4}([A-Z]{2})(?:\b|$)"
            m_uf2 = re.search(padrao, txt)
            if m_uf2:
                uf = m_uf2.group(1)

    if not uf and municipio in ["SAO PAULO", "SÃO PAULO"]:
        uf = "SP"

    return municipio.title().strip(), uf.upper().strip()

linhas_result = []

arquivos = sorted([f for f in os.listdir(pasta_ativas) if f.lower().endswith(".pdf")])
if not arquivos:
    print("⚠️ Nenhum PDF encontrado na pasta:", pasta_ativas)

for nome_arquivo in arquivos:
    caminho_pdf = os.path.join(pasta_ativas, nome_arquivo)
    print(f"📄 Processando: {nome_arquivo}")

    try:
        doc = fitz.open(caminho_pdf)
        texto_total = ""
        for page in doc:
            texto_total += page.get_text("text") + "\n"
        doc.close()

        texto_l = limpar_texto(texto_total)

        nº_nota = extrair_numero_nota(texto_l)
        cpf_cnpj = extrair_cpf_cnpj(texto_l)
        nome_razao = extrair_nome_razao(texto_l)
        endereco = extrair_endereco(texto_l)
        municipio, uf = extrair_municipio_uf(texto_l)
        valor = extrair_valor(texto_l)

        nome_razao = nome_razao.upper()
        endereco = endereco.upper()
        municipio = municipio.title()
        uf = uf.upper()

        linhas_result.append({
            "Nº Nota": nº_nota,
            "CPF/CNPJ": cpf_cnpj,
            "Nome Razao": nome_razao,
            "Endereco": endereco,
            "Municipio": municipio,
            "UF": uf,
            "Valor": valor
        })

    except Exception as e:
        print(f"❌ Erro processando {nome_arquivo}: {e}")

campos = ["Nº Nota", "CPF/CNPJ", "Nome Razao", "Endereco", "Municipio", "UF", "Valor"]
with open(arquivo_saida, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    for row in linhas_result:
        writer.writerow(row)

print(f"\n✅ Relatório salvo em: {arquivo_saida}")
