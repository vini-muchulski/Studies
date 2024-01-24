import requests
from bs4 import BeautifulSoup
import re


def baixar_img(url,nome_arquivo):
    requisicao = requests.get(url)

    if (requisicao.status_code == 200):
        with open(nome_arquivo,"wb") as arquivo:
            arquivo.write(requisicao.content)

        print("imagem baixada")
    
    else:
        print("erro ao baixar")


        
link = "https://apod.nasa.gov/apod/astropix.html"
headers =  {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}

requisicao = requests.get(link,headers=headers)


#print(requisicao)

#print(requisicao.text)

site = BeautifulSoup(requisicao.text, "html.parser")



imagem = site.find_all("img")
#print(imagem[0])

url_imagem = imagem[0]['src']
url_imagem = "https://apod.nasa.gov/apod/" + url_imagem
print(url_imagem)
baixar_img(url_imagem,"imagem.jpg")


    




titulo_da_imagem = site.find_all("b")
titulo_da_imagem = titulo_da_imagem[0].text.strip()
#print(titulo_da_imagem)



explicacao = site.find_all("p")
explicacao = str(explicacao[2].text.strip())
#busca a posicao onde termina a explicacao da imagem
try:
    posicao_fim_da_explicacao = explicacao.find("Explore Your Universe:")

except: 
    posicao_fim_da_explicacao = explicacao.find("Tomorrow's picture:")


explicacao = explicacao[:posicao_fim_da_explicacao].strip()
explicacao = explicacao.replace('\n', ' ')
#print(explicacao)



