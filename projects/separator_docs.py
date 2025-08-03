import os
import shutil
from PyPDF2 import PdfReader
from unidecode import unidecode

pasta_raiz = r"C:\Users\Alex\Documents\exe"

pasta_destino = os.path.join(pasta_raiz, "PROCESSO DE NOVACAO")
os.makedirs(pasta_destino, exist_ok=True)

erros = []

for nome_subpasta in os.listdir(pasta_raiz):
    if nome_subpasta == "PROCESSO DE NOVACAO":
        continue

    caminho_subpasta = os.path.join(pasta_raiz, nome_subpasta)
    if not os.path.isdir(caminho_subpasta):
        continue

    arquivos_na_pasta = os.listdir(caminho_subpasta)

    for nome_arquivo in arquivos_na_pasta:
        caminho_arquivo = os.path.join(caminho_subpasta, nome_arquivo)

        if nome_arquivo.lower().endswith(('.lnk', '.html')):
            continue

        if not os.path.isfile(caminho_arquivo):
            continue

        try:
            reader = PdfReader(caminho_arquivo)
            texto_pdf = ""
            for pagina in reader.pages:
                texto_pdf += pagina.extract_text() or ""

            texto_pdf = unidecode(texto_pdf).lower().replace(" ", "")

            if "processodenovacao" in texto_pdf:
                print(f'Encontrado "PROCESSO DE NOVACAO" no arquivo: {caminho_arquivo}')

                nome_destino = f"{nome_subpasta}.pdf"
                caminho_destino = os.path.join(pasta_destino, nome_destino)

                shutil.copy2(caminho_arquivo, caminho_destino)

        except Exception as e:
            print(f"Erro ao processar {caminho_arquivo}: {e}")

print("Processo concluído.")

if erros:
    print("\nArquivo com erro: ")
    for erro in erros:
        print(erro)

