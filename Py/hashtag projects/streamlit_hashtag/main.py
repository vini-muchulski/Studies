import streamlit as st
import pandas as pd

@st.cache_data
def carregar_dados():
    return pd.read_csv("resultados.csv")

st.set_page_config(page_title="Meu App", page_icon=":shark:", layout="wide")

with st.container():
    st.subheader("# meu app - by vini")
    st.title("Dashboard de contratos")
    st.write("Aqui você encontra informações sobre contratos")
    st.write("GitHub [vini](https://github.com/vini-muchulski)")
    
with st.container():
    st.write("---")
    qtd_dias = st.selectbox("Quantidade de dias", [7, 15, 30])
    data = carregar_dados()
    data = data.tail(qtd_dias)
    st.area_chart(data,x="Data",y="Contratos")