import duckdb
import kagglehub
import pandas as pd
import streamlit as st
import plotly.express as px
print(duckdb.__version__)


# Download latest version
path = kagglehub.dataset_download("yusufdelikkaya/online-sales-dataset")
print("Path to dataset files:", path)

con = duckdb.connect('.db')

caminho_csv = '/home/usuario/.cache/kagglehub/datasets/yusufdelikkaya/online-sales-dataset/versions/1/online_sales_dataset.csv'

con.execute(f"""
    CREATE TABLE IF NOT EXISTS online_sales AS SELECT * FROM read_csv_auto('{caminho_csv}')
""")

#banco para dataframe pandas
type(con)
df_sales = con.execute("SELECT * FROM online_sales").fetchdf()

# Configuração da página
st.set_page_config(
    page_title="Relatório Interativo",
    layout="wide",
)

# Título do relatório
st.title("Relatório de Vendas")
st.sidebar.header("Configurações")

# Gráfico de barras
fig_bar = px.bar(df_sales, x="Description", y="ShippingCost", title="Gráfico de Barras")

# Gráfico de linhas
fig_line = px.line(df_sales, x="InvoiceDate", y="UnitPrice", title="Gráfico de Linhas")

# Exibindo os gráficos
st.plotly_chart(fig_bar, use_container_width=True)
st.plotly_chart(fig_line, use_container_width=True)
