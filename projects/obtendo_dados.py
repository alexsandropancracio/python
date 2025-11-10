import os
import re
import csv
from PyPDF2 import PdfReader
from unidecode import unidecode

# Caminhos
pasta_pdf = r"C:\Users\Elisangela\Desktop\contratos"
pasta_planilha = os.path.join(pasta_pdf, "planilha")
os.makedirs(pasta_planilha, exist_ok=True)
arquivo_saida = os.path.join(pasta_planilha, "contratos_extraidos.csv")

# Função para extrair texto do PDF
def extrair_texto_pdf(caminho_pdf):
    texto = ""
    try:
        reader = PdfReader(caminho_pdf)
        for pagina in reader.pages:
            texto += pagina.extract_text() or ""
    except Exception as e:
        print(f"❌ Erro ao ler {caminho_pdf}: {e}")
    return texto

# Função para limpar texto - CORRIGIDA
def limpar_texto(t):
    # Primeiro remove espaços extras e converte para maiúsculo
    texto_limpo = re.sub(r"\s+", " ", t).strip().upper()
    # Corrige espaços no meio de palavras comuns
    correcoes = {
        r'NOV\s+ACAO': 'NOVACAO',
        r'PROCESSA\s+O': 'PROCESSO',
        r'PROCESSA\s+MENSA': 'PROCESSAMENTO',
        r'CONTRATA\s+CAO': 'CONTRATACAO',
        # NOVAS CORREÇÕES:
        r'CONTRA\s+TO': 'CONTRATO',
        r'NAO\s+NOVADO': 'NAO NOVADO',
        r'NAO\s+NOV\s+ADO': 'NAO NOVADO',
        r'CONTRATO\s+BAIXADO': 'CONTRATO BAIXADO',
        r'BAIXA\s+DO': 'BAIXADO',
        # CORREÇÃO ESPECÍFICA PARA "NOV ADO"
        r'NOV\s+ADO': 'NOVADO'
    }
    
    for padrao, substituicao in correcoes.items():
        texto_limpo = re.sub(padrao, substituicao, texto_limpo)
    
    return texto_limpo

# Função para extrair campos com base nos rótulos específicos
def extrair_campos(texto):
    texto_original = unidecode(texto.upper())
    campos = {}

    # Expressões regulares ajustadas
    padroes = {
        # Pega o nome completo até antes de "CPF" ou outro campo
        "Mutuário": r"MUTU[ÁA]RIO[:\s]+([A-Z\s]+?)(?=\sCPF|AGENTE|SIT|CONTRATO|$)",
        "CPF": r"CPF[:\s]+([\d\.-]+)",
        "Agente": r"AGENTE[:\s]+([0-9\s\-A-Z\/\.]+)",
        # CORREÇÃO: Captura TODOS os números/barras até o final, ignorando espaços
        "Contrato/Hip.": r"CONTRATO\/HIP\.?[:\s]*([0-9\/\.\-\s]+)",
        # CORREÇÃO: Para antes de "CAMPO CONTROLE" ou até o final
        "Sit. Novação": r"SIT\.?\s*NOVAC[AÃ]O[:\s]+([A-Z\s]+?)(?=\s*CAMPO CONTROLE|$)"
    }

    for campo, regex in padroes.items():
        m = re.search(regex, texto_original)
        if m:
            valor = m.group(1)
            if campo == "Contrato/Hip.":
                # Para contrato, apenas remove espaços mas mantém TODOS os caracteres
                campos[campo] = re.sub(r"\s+", "", valor).strip()
            else:
                campos[campo] = limpar_texto(valor)
        else:
            campos[campo] = ""

    return campos

# Criação do CSV - ORDEM AJUSTADA
with open(arquivo_saida, "w", newline="", encoding="utf-8-sig") as csvfile:
    # Ordem dos campos ajustada: Contrato/Hip. vem antes de Sit. Novação
    campos = ["Mutuário", "CPF", "Agente", "Contrato/Hip.", "Sit. Novação"]
    writer = csv.DictWriter(csvfile, fieldnames=campos)
    writer.writeheader()

    arquivos = [f for f in os.listdir(pasta_pdf) if f.lower().endswith(".pdf")]
    if not arquivos:
        print("Nenhum PDF encontrado em:", pasta_pdf)

    for arquivo in arquivos:
        caminho = os.path.join(pasta_pdf, arquivo)
        texto = extrair_texto_pdf(caminho)
        dados = extrair_campos(texto)
        writer.writerow(dados)
        print(f"✅ {arquivo} → Mutuário: {dados['Mutuário'] or 'NÃO ENCONTRADO'}")
        print(f"   Sit. Novação: {dados['Sit. Novação'] or 'NÃO ENCONTRADO'}")

print("\n📄 Planilha criada em:", arquivo_saida)