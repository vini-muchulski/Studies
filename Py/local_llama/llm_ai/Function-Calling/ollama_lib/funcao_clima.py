import requests
import json
from keys import api_key

def get_current_weather(city):
    lang = "pt_br"
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang={lang}"
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    
    
    temperatura = round(float(requisicao_dic['main']['temp']) - 273.15, 2)
    descricao = requisicao_dic["weather"][0]['main']  + " --- " + requisicao_dic["weather"][0]['description']
    nome_cidade = requisicao_dic['name']
    
    resultado = f"Cidade: {nome_cidade} | Condição: {descricao} | Temperatura: {temperatura} °C"
    
    
    print(resultado)
    return resultado
    
    
    
get_current_weather("ararangua")