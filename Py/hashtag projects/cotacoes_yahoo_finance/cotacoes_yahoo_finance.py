# -*- coding: utf-8 -*-
"""cotacoes yahoo finance

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UiVzzQpa-Xqwzhzhp1PRZExSnity5fpi
"""

!pip install pandas-datareader yfinance pandas numpy matplotlib

import pandas as pd
import pandas_datareader.data as pdr
import yfinance

yfinance.pdr_override()

ativos = ["ITUB3.SA", "BPAC11.SA","VALE3.SA","^BVSP"]

                                    #ticker, data_inicial, data_final
data_inicial = "2023-01-01"
data_final="2023-12-31"

tabela_cotacoes = pdr.get_data_yahoo(ativos,data_inicial,data_final)

tabela_cotacoes = tabela_cotacoes["Adj Close"]

display(tabela_cotacoes)