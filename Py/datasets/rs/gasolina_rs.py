# -*- coding: utf-8 -*-
"""gasolina rs

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n5jhYYESa6UyKIcqV9rxP0t68dXUosLt
"""

import pandas as pd
import numpy as np

pip install folium

import folium

df = pd.read_csv("dee-2424.csv",encoding="latin1",skiprows=1)
df

df.info()

brasil = folium.Map(
    location=[-30.3852768,-52.315788], #coordenadas
    zoom_start=7
)
brasil

for indice, municipio in df.iterrows():
  folium.Marker(
      location=[municipio["latitude"],municipio["longitude"]],
      icon=folium.map.Icon(color="green")
  ).add_to(brasil)

brasil
