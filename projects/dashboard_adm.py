import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Dashboard Administrativo", layout="wide")
st.title("Dashboard Administrativo")

caminho_parquet = r"C:\Users\Elisangela\Documents\AdminDashboard\dados\relatorio_adm.parquet"

@st.cache_data(show_spinner=False)
def carregar_dados(path):
    if os.path.exists(path):
        return pd.read_parquet(path)
    else:
        return pd.DataFrame()

if st.sidebar.button("🔁 Atualizar / Limpar Cache"):
    st.cache_data.clear()
    st.success("✅ Cache limpo. Recarregue a página se necessário.")
    st.stop()

df = carregar_dados(caminho_parquet)

if df.empty:
    st.error("❌ Arquivo Parquet vazio ou não encontrado. Verifique o caminho.")
    st.stop()

df.columns = [c.strip() for c in df.columns]

col_valor = next((c for c in df.columns if any(k in c.lower() for k in ("valor", "amount", "value", "total"))), None)
col_data = next((c for c in df.columns if "data" in c.lower() or "date" in c.lower()), None)
col_categoria = next((c for c in df.columns if "categoria" in c.lower() or "category" in c.lower()), None)
col_ref = next((c for c in df.columns if c.lower() in ("regiao", "região", "cliente", "fornecedor", "department", "departamento")), None)

if col_valor:
    df[col_valor] = pd.to_numeric(df[col_valor], errors="coerce")

if col_data:
    df[col_data] = pd.to_datetime(df[col_data], errors="coerce")

st.sidebar.header("Filtros")

if col_data:
    st.sidebar.subheader("📅 Período")
    min_date = df[col_data].min()
    max_date = df[col_data].max()
    data_filtro = st.sidebar.date_input(
        "Selecione o período:",
        value=(min_date.date(), max_date.date()),
        min_value=min_date.date(),
        max_value=max_date.date()
    )
    if isinstance(data_filtro, tuple) and len(data_filtro) == 2:
        inicio, fim = pd.to_datetime(data_filtro[0]), pd.to_datetime(data_filtro[1])
        df = df[(df[col_data] >= inicio) & (df[col_data] <= fim)]

nomes_traduzidos = {
    "department": "Departamento",
    "cost_center": "Centro de Custo",
    "employee": "Funcionário",
    "categoria": "Categoria",
    "category": "Categoria",
    "transaction_type": "Tipo de Transação"
}

candidatas = [
    col for col in df.select_dtypes(include=["object", "category"]).columns
    if "month" not in col.lower()
    and "employee_id" not in col.lower()
    and col != col_categoria
    and col != col_data
]

for col in candidatas[:4]:
    nome_exibicao = nomes_traduzidos.get(col.lower(), col.capitalize())
    valores = sorted(df[col].dropna().unique())
    selecionados = st.sidebar.multiselect(f"{nome_exibicao}", options=valores)
    if selecionados:
        df = df[df[col].isin(selecionados)]

st.markdown("---")
col1, col2, col3 = st.columns(3)
if col_valor:
    soma = df[col_valor].sum()
    media = df[col_valor].mean()
    col1.metric("💰 Total (R$)", f"R$ {soma:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    col2.metric("📈 Média (R$)", f"R$ {media:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
else:
    col1.metric("Registros", len(df))
    col2.metric("Valores", "não detectado")
col3.metric("🧾 Registros", f"{len(df):,}".replace(",", "."))

st.markdown("---")

if col_categoria:
    st.markdown("### 📌 Totais por Categoria")
    categorias = sorted(df[col_categoria].dropna().unique())

    if "cat_sel" not in st.session_state:
        st.session_state["cat_sel"] = categorias.copy()

    selecionar_todas_cats = st.checkbox("Selecionar todas as categorias", value=False, key="checkbox_select_all_categories")

    if selecionar_todas_cats:
        st.session_state["cat_sel"] = categorias.copy()
        cat_sel = categorias.copy()
    else:
        cat_sel = st.multiselect(
            "Selecione uma ou mais categorias:",
            options=categorias,
            default=st.session_state.get("cat_sel", [])
        )
        st.session_state["cat_sel"] = cat_sel

    if cat_sel:
        df_cat = df[df[col_categoria].isin(cat_sel)]
    else:
        df_cat = df.copy()

    if col_valor:
        gb = df_cat.groupby(col_categoria, as_index=False)[col_valor].sum().sort_values(col_valor, ascending=False)
        fig = px.bar(
            gb,
            x=col_categoria,
            y=col_valor,
            title="Totais por Categoria",
            text_auto=True,
            color_discrete_sequence=["#1f77b4"]
        )
        fig.update_layout(xaxis_title="Categoria", yaxis_title="Valor (R$)")
        st.plotly_chart(fig, use_container_width=True)

if col_data and col_valor:
    st.markdown("### 📆 Evolução Diária dos Valores")
    df_time = df.groupby(pd.Grouper(key=col_data, freq="D"))[col_valor].sum().reset_index()
    fig2 = px.line(df_time, x=col_data, y=col_valor, title="Evolução ao longo do tempo", markers=True)
    fig2.update_layout(xaxis_title="Data", yaxis_title="Valor (R$)")
    st.plotly_chart(fig2, use_container_width=True)

if col_ref and col_valor:
    st.markdown("### 📊 Distribuição por Departamento")
    pie = df.groupby(col_ref, as_index=False)[col_valor].sum()
    fig3 = px.pie(pie, names=col_ref, values=col_valor, title="Proporção de Valores por Departamento")
    st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.subheader("📋 Tabela de Dados")
st.dataframe(df.reset_index(drop=True), use_container_width=True)

st.caption(f"🧠 Coluna de valores detectada: **{col_valor if col_valor else 'Nenhuma detectada'}**")
