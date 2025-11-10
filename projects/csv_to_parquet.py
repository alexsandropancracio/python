import pandas as pd
import os

# === Caminho dos arquivos ===
# Altere o caminho abaixo para o local do seu CSV
caminho_csv = r"C:\Users\Elisangela\Documents\AdminDashboard\dados\relatorio_adm.csv"
caminho_parquet = r"C:\Users\Elisangela\Documents\AdminDashboard\dados\relatorio_adm.parquet"

# === Cria a pasta caso não exista ===
os.makedirs(os.path.dirname(caminho_parquet), exist_ok=True)

print("📂 Lendo arquivo CSV...")
df = pd.read_csv(caminho_csv)

# === Exibe informações básicas ===
print(f"✅ CSV lido com sucesso. Linhas: {len(df)}, Colunas: {len(df.columns)}")

# === Converte para Parquet ===
df.to_parquet(caminho_parquet, index=False)

print(f"🎯 Arquivo convertido com sucesso!")
print(f"💾 Caminho do Parquet: {caminho_parquet}")
