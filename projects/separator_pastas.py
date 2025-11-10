import os
import shutil
from PyPDF2 import PdfReader
from unidecode import unidecode

# Caminho da pasta onde estão as subpastas com PDFs
pasta_raiz = r"C:\Users\Alex\Documents\exe"

# Pasta destino da categoria
pasta_destino = os.path.join(pasta_raiz, "CONTRATO NOVADO")
os.makedirs(pasta_destino, exist_ok=True)

# Lista de erros (opcional)
erros = []

# Percorre todas as subpastas da pasta raiz
for nome_subpasta in os.listdir(pasta_raiz):
    if nome_subpasta == "CONTRATO NOVADO":
        continue  # Ignora a própria pasta de destino

    caminho_subpasta = os.path.join(pasta_raiz, nome_subpasta)
    if not os.path.isdir(caminho_subpasta):
        continue

    try:
        arquivos = os.listdir(caminho_subpasta)

        for nome_arquivo in arquivos:
            caminho_arquivo = os.path.join(caminho_subpasta, nome_arquivo)

            # Ignora atalhos, HTML e outros não-pdf
            if nome_arquivo.lower().endswith(('.lnk', '.html')):
                continue

            if not os.path.isfile(caminho_arquivo):
                continue

            if not nome_arquivo.lower().endswith(".pdf"):
                continue

            # Lê o PDF e extrai texto
            reader = PdfReader(caminho_arquivo)
            texto_pdf = ""
            for pagina in reader.pages:
                texto_pdf += pagina.extract_text() or ""

            texto_pdf = unidecode(texto_pdf).lower().replace(" ", "")

            if "contratonovado" in texto_pdf:
                print(f'📂 Movendo pasta: {nome_subpasta}')
                destino_final = os.path.join(pasta_destino, nome_subpasta)
                shutil.move(caminho_subpasta, destino_final)
                break  # Não precisa verificar mais arquivos dentro da pasta

    except Exception as e:
        print(f"❌ Erro na pasta {nome_subpasta}: {e}")
        erros.append(f"{nome_subpasta}: {e}")

print("\n✅ Processo concluído.")

if erros:
    print("\n❗ Pastas com erro:")
    for erro in erros:
        print(erro)
