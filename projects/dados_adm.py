import os
import random
import csv
from datetime import datetime, timedelta
import pandas as pd

# ----------------- CONFIG -----------------
OUT_DIR = r"C:\Users\Elisangela\Documents\AdminDashboard\dados"
OUT_FILE = os.path.join(OUT_DIR, "relatorio_adm.csv")
NUM_ROWS = 1200  # ajuste: quantas linhas você quer gerar
SEED = 42
# ------------------------------------------

random.seed(SEED)

# Listas exemplo
departments = ["Financeiro", "Comercial", "RH", "Administrativo", "TI", "Operações", "Jurídico", "Compras"]
categories_receita = ["Vendas", "Serviços", "Licenciamento", "Consultoria", "Receita Extra"]
categories_despesa = ["Aluguel", "Energia", "Marketing", "Salários", "Fornecedores", "TI - Infra", "Manutenção", "Transporte"]
vendors_customers = [
    "Apex Soluções Ltda", "Beta Distribuidora", "Gamma Serviços", "Delta Comércio", "Epsilon Tecnologia",
    "Zeta Consultoria", "Theta Holdings", "Iota Fornecimentos"
]
employees = [
    ("Ana Silva", "E001"), ("Bruno Costa", "E002"), ("Carla Mendes", "E003"), ("Diego Rocha", "E004"),
    ("Eduarda Lima", "E005"), ("Fábio Santos", "E006"), ("Gabriela Freitas", "E007"), ("Hugo Alves", "E008")
]
cost_centers = ["CC100", "CC200", "CC300", "CC400", "CC500"]

payment_statuses = ["Pago", "Pendente", "Vencido"]
payment_methods = ["Boleto", "PIX", "TED", "Cartão"]
contract_types = ["Recorrente", "One-off"]

# Cria pasta se não existir
os.makedirs(OUT_DIR, exist_ok=True)

# Funções auxiliares
def random_date(start_date, end_date):
    delta = end_date - start_date
    rand_days = random.randint(0, delta.days)
    return start_date + timedelta(days=rand_days)

def gen_invoice_number():
    return f"{random.randint(1000000, 9999999)}"

rows = []
start = datetime(2024, 1, 1)
end = datetime(2025, 12, 31)

for i in range(NUM_ROWS):
    # Decide receita ou despesa (ex.: 40% receita, 60% despesa)
    if random.random() < 0.40:
        ttype = "RECEITA"
        category = random.choice(categories_receita)
        # receitas tendem a ser maiores
        amount = round(random.uniform(2000, 80000), 2)
        vendor = random.choice(vendors_customers)
    else:
        ttype = "DESPESA"
        category = random.choice(categories_despesa)
        amount = round(random.uniform(50, 40000), 2)
        vendor = random.choice(vendors_customers)

    date = random_date(start, end)
    month_name = date.strftime("%B")
    year = date.year
    dept = random.choice(departments)
    emp, emp_id = random.choice(employees)
    cost_center = random.choice(cost_centers)
    invoice = gen_invoice_number()
    status = random.choices(payment_statuses, weights=[0.6, 0.25, 0.15])[0]  # mais pagos
    method = random.choice(payment_methods)
    contract = random.choice(contract_types)
    notes = ""
    # adiciona algumas anotações aleatórias
    if status == "Vencido" and ttype == "DESPESA":
        notes = "Atenção: atraso no pagamento"
    elif ttype == "RECEITA" and amount > 50000:
        notes = "Receita grande - verificar contrato"

    row = {
        "date": date.strftime("%Y-%m-%d"),
        "year": year,
        "month": month_name,
        "department": dept,
        "cost_center": cost_center,
        "employee": emp,
        "employee_id": emp_id,
        "transaction_type": ttype,
        "category": category,
        "vendor_customer": vendor,
        "invoice_number": invoice,
        "amount": f"{amount:.2f}",
        "currency": "BRL",
        "payment_status": status,
        "payment_method": method,
        "contract_type": contract,
        "notes": notes
    }
    rows.append(row)

# Salva como CSV com pandas (UTF-8 BOM)
df = pd.DataFrame(rows)
df.to_csv(OUT_FILE, index=False, encoding="utf-8-sig")

print(f"✅ CSV gerado com {len(rows)} linhas: {OUT_FILE}")
