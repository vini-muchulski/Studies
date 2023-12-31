# -*- coding: utf-8 -*-
"""py_geocoder

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lmhyy2UUAmL18bKxHT9-9MC2090x_xUq
"""

pip install geocoder

pip install folium

import geocoder
import folium

g = geocoder.ip("me")

print(g)
x = g.latlng
#print(x[0], x[1])

my_map1 = folium.Map(location = [-28.9357, -49.4954],
                                        zoom_start = 12 )

folium.CircleMarker(location = [-28.9357,-49.4954],radius = 50, popup = ' FRI ').add_to(my_map1)

my_map1