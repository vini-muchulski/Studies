import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

st.write('Hello, world!')

if "data" not in st.session_state:
    df_data = pd.read_csv("CLEAN_FIFA23_official_data.csv")
    
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.now().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    df_data = df_data.drop(['Unnamed: 0','ID'], axis=1)
    
    st.session_state["data"] = df_data
    
    
st.write("# FIFA 23 Dataset ⚽️")
#st.write(st.session_state['data'].head())

st.dataframe(st.session_state["data"],
             column_config={
                 "Overall": st.column_config.ProgressColumn("Overall",format="%d",min_value=0,max_value=100),
                 "Value(£)": st.column_config.NumberColumn(),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn()  
             })


st.sidebar.markdown("## Github")
st.sidebar.write("Desenvolvido pelo [Vini](ttps://github.com/vini-muchulski)")

btn = st.button("Acesse os dodos no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
    
    
st.markdown("""
            O conjunto de dados de jogadores de futebol de **2017** a **2023** é uma coleção abrangente de informações sobre jogadores de futebol profissionais. 
            
            Inclui detalhes como dados demográficos dos jogadores, características físicas, estatísticas de jogo, 
            detalhes de contratos, afiliações de clubes, valores de mercado, salários, posições preferenciais, taxas de trabalho, 
            classificações de habilidades e desenvolvimento de jogadores.
            """)
