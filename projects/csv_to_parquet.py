import pandas as pd
import os
import sys

caminho_csv = r"C:\Users\Elisangela\Documents\OCR\nfse_ocr\Planilhas\relatorio_adm.csv"
caminho_parquet = r"C:\Users\Elisangela\Documents\OCR\nfse_ocr\Planilhas\relatorio_adm.parquet"

os.makedirs(os.path.dirname(caminho_parquet), exist_ok=True)

print("📂 Verificando existência do CSV...")

if not os.path.exists(caminho_csv):
    print(f"❌ Arquivo não encontrado: {caminho_csv}")
    pasta = os.path.dirname(caminho_csv)
    print(f"\n🗂 Conteúdo da pasta {pasta}:")
    try:
        for f in os.listdir(pasta):
            print("  -", f)
    except FileNotFoundError:
        print("  -> A pasta não existe. Verifique o caminho indicado.")
    print("\nDicas:")
    print(" - Confirme o nome do arquivo e a extensão (.csv).")
    print(" - Copie o caminho do Explorer (Shift+Botão Direito -> 'Copiar como caminho').")
    sys.exit(1)

print("✅ CSV encontrado. Tentando ler...")

read_options = [
    {"sep": ",", "encoding": "utf-8"},
    {"sep": ";", "encoding": "utf-8"},
    {"sep": ",", "encoding": "latin-1"},
    {"sep": ";", "encoding": "latin-1"},
]

df = None
last_error = None
for opts in read_options:
    try:
        print(f"  -> tentando pd.read_csv(..., sep='{opts['sep']}', encoding='{opts['encoding']}') ...")
        df = pd.read_csv(caminho_csv, sep=opts["sep"], encoding=opts["encoding"], low_memory=False)
        print("  ✅ Leitura bem-sucedida com essas opções.")
        break
    except Exception as e:
        last_error = e
        print(f"  ❌ falhou: {e}")

if df is None:
    print("\n❌ Não foi possível ler o CSV com as opções testadas.")
    print("Último erro:")
    print(last_error)
    print("\nSugestões:")
    print(" - Abra o CSV num editor (Bloco de notas / VSCode / Excel) e verifique o separador e encoding.")
    print(" - Se for Excel (.xlsx), use pd.read_excel em vez de read_csv.")
    sys.exit(1)

print(f"\n✅ CSV lido com sucesso. Linhas: {len(df):,}, Colunas: {len(df.columns)}")
print("Colunas:", list(df.columns)[:20])

print("\n📦 Convertendo para Parquet...")
try:
    df.to_parquet(caminho_parquet, index=False)
    print(f"🎯 Arquivo convertido com sucesso!")
    print(f"💾 Caminho do Parquet: {caminho_parquet}")
except Exception as e:
    print("❌ Erro ao salvar Parquet:", e)
    print("\nDica: instale 'pyarrow' (recomendado) ou 'fastparquet':")
    print("  pip install pyarrow")
    print("ou")
    print("  pip install fastparquet")
    sys.exit(1)
