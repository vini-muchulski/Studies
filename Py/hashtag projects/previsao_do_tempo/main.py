#from keys import api_key

import requests
import json
from keys import api_key


city_name = "ararangua"
lang = "pt_br"
#city_name = "Porto Alegre"
#link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang={lang}"


requisicao = requests.get(link)

requisicao_dic = requisicao.json()

descricao = requisicao_dic["weather"][0]['main']  + " -> description : " + requisicao_dic["weather"][0]['description']
temperatura = requisicao_dic['main']['temp']
temperatura = round(float(temperatura)-273.15, 2) 
temperatura = f"\nTemperatura -> {temperatura} °C"

print(requisicao_dic)
print(descricao, temperatura)