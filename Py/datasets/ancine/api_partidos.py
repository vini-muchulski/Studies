# -*- coding: utf-8 -*-
"""api partidos

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sZSyn5DOmxy7dYbC09g9bbsMMDXK--H1
"""

# Importando a biblioteca
import pandas as pd
import requests

# URL de acesso aos dados via api
url = 'https://dadosabertos.camara.leg.br/api/v2/partidos?itens=100'

# Obtendo os dados
resposta = requests.get(url)

# Vamos verificar o texto de retorno da requisicao
resposta.text

df = pd.DataFrame(resposta.json()['dados'])

df.head()

df["sigla"].count()

df["nome"]

"""# O iloc retorna um campo com base no seu índice [linha, coluna]

# O loc retorna o campo com base no nome das colunas
"""

df.iloc[0,3]

df.loc[0, "uri"]