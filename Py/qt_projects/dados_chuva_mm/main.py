import pandas as pd
import numpy as np
import streamlit as st

dados = pd.read_csv("dados_chuva_mm.csv")
dados['Data'] = pd.to_datetime(dados['Data'], format='%d/%m')

st.write("## Dados de chuva")

st.line_chart(dados, x="Data", y="Chuva (mm)") 

st.write("#### Chuva registrada na cidade de Camaquã - RS")

