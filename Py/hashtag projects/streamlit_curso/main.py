#importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np

#criar funcoes que carregam os dados
@st.cache_data
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes = dados_acao.history(period="1d", start="2015-01-01")
    cotacoes = cotacoes[["Close"]]
    
    # Resetar o índice para transformar a data em uma coluna
    cotacoes = cotacoes.reset_index()
    
    # Converter a coluna 'Date' para string (formato compatível com Arrow)
    cotacoes['Date'] = cotacoes['Date'].dt.strftime('%Y-%m-%d')
    
    # Converter 'Close' para float64 (para garantir compatibilidade)
    cotacoes['Close'] = cotacoes['Close'].astype(np.float64)
    
    # Definir 'Date' como índice novamente
    cotacoes = cotacoes.set_index('Date')
    
    return cotacoes


dados = carregar_dados("ITUB4.SA")
print(dados)

#prepara as visualizacoes


#criar interface do streamlit
st.write(""" 
         # App Invest
         O gráfico abaixo representa a evolução do preco das acoes""") #markdown

#criar grafico
grafico = st.line_chart(dados)


st.write(""" 
         # Fim""") #markdown

