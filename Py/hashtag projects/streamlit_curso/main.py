#importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf

#criar funcoes que carregam os dados
@st.cache_data
def carregar_dados(empresas):
    dados = pd.DataFrame()

    for empresa in empresas:
        acao = yf.Ticker(empresa)
        cotacoes = acao.history(period="1d", start="2015-01-01")["Close"]
        dados[empresa] = cotacoes
        
    
    return dados

@st.cache_data
def carregar_tickers():
    base = pd.read_csv("IBOV.csv",sep=";")
    tickers = list(base["Código"])
    tickers = [ticker+ ".SA" for ticker in tickers]
    return  tickers

def carregar_ibov():
    ibov = yf.Ticker("^BVSP")
    cotacoes = ibov.history(period="1d", start="2015-01-01")["Close"]
    
    return cotacoes


#criar interface do streamlit
st.write(""" 
         # App Invest
         O gráfico abaixo representa a evolução do indice IBOVESPA""") #markdown


acoes = carregar_tickers()
dados = carregar_dados(acoes)
dados_ibov = carregar_ibov()

#prepara as visualizacoes = FILTRO
st.sidebar.header("Ações - Filtros")

#filtro de acoes
lista_acoes = st.sidebar.multiselect("Lista de ações", dados.columns)

if lista_acoes:
    dados = dados[lista_acoes]
    
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica:"Close"})
    
#filtro de datas
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()

intervalo_datas = st.sidebar.slider("Selecione o periodo",min_value=data_inicial, 
                  max_value=data_final,
                    value=(data_inicial, data_final)
                  )


     
dados =dados.loc[intervalo_datas[0]:intervalo_datas[1]]  
dados_ibov = dados_ibov.loc[intervalo_datas[0]:intervalo_datas[1]]
performance_ibo = dados_ibov.iloc[-1]/dados_ibov.iloc[0] -1
performance_ibo = float(performance_ibo)
texto_ibov = " "
if performance_ibo > 0:
    texto_ibov += f"  \nIBOV:      :green[{performance_ibo:.1%}]  "

elif performance_ibo <= 0:
    texto_ibov += f"  \nIBOV:      :red[{performance_ibo:.1%}]  "


#criar grafico
st.write(texto_ibov)
st.line_chart(dados_ibov)


st.line_chart(dados)

#calcular a performance
texto = ""

if len(lista_acoes)== 0:
    lista_acoes = list(dados.columns)

elif len(lista_acoes) == 1:    
    dados = dados.rename(columns={"Close":acao_unica})
    
    
carteira = [1000 for acao in lista_acoes]
total_inicial_carteira = sum(carteira)
    
for i,acao in enumerate(lista_acoes):
        performance_ativo = dados[acao].iloc[-1]/dados[acao].iloc[0] -1 # calculo da performance é o ultimo valor dividido pelo primeiro valor
        performance_ativo = float(performance_ativo)
        
        carteira[i] = carteira[i] * (1+performance_ativo)
        
        
        if performance_ativo > 0:
            texto += f"  \n{acao}:      :green[{performance_ativo:.1%}]  "
        
        elif performance_ativo <= 0:
            texto += f"  \n{acao}:      :red[{performance_ativo:.1%}]  "
  

total_final_carteira = sum(carteira)
performance_carteira = total_final_carteira/total_inicial_carteira -1
texto_performance_carteira = ""


if performance_carteira > 0:
    texto_performance_carteira += f"  \n  Performance da carteira =     :green[{performance_carteira:.1%}]  \n  "
        
elif performance_carteira <= 0:
    texto_performance_carteira += f"  \n  Performance da carteira =     :red[{performance_carteira:.1%}]  \n  "     
         
st.write(f""" 
         ### Performance dos ativos
         O gráfico representa a evolução do preço das ações no periodo
         {texto_performance_carteira}
         
         {texto}
         
         
         
         """) #markdown

