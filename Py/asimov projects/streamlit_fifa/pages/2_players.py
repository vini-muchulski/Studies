import streamlit as st

st.set_page_config(page_title="FIFA STATS", page_icon=":soccer:", layout="wide")

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Selecione um clube", clubes)


df_players = df_data[df_data["Club"] == club]

player = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Selecione um jogador", player)


player_stats = df_data[df_data["Name"] == player].iloc[0]


st.image(player_stats["Photo"])
st.title(f" {player_stats['Name']}")

st.markdown(f"**Clube** {player_stats['Club']}")
st.markdown(f"**Posicao** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"**Idade** {player_stats['Age']}")
col2.markdown(f"**Altura** {player_stats['Height(cm.)']/100}")
col3.markdown(f"**Peso** {player_stats['Weight(lbs.)']*0.453:.2f}")

st.divider()

st.subheader(f"**Overall** {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))


col1, col2, col3 = st.columns(3)
col1.metric(label="valor de mercado", value=f"£{player_stats['Value(£)']:,}")
col2.metric(label="Salario semanal", value=f"£{player_stats['Wage(£)']:,}")