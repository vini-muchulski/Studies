import requests
import json
from keys import api_key_climatempo

tipo_consulta = 1
# "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token=your-app-token"

if tipo_consulta == 1:
    city = "ararangua"


link = f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token={api_key_climatempo}"
requisicao = requests.get(link)

print(requisicao.text)