import requests
import bs4
#https://www.youtube.com/watch?v=e3oaQQ6IJ10&list=PLP_dh3S9H39kSv9Ke0Ezie8HAlm5zfVhc&index=4

url = "https://g1.globo.com/mundo/videos/"

requisicao = requests.get(url)

#print(requisicao.text)

pagina = bs4.BeautifulSoup(requisicao.text,"html.parser")


#pegar os elementos a com classe feed-post-link
noticias_lista = pagina.find_all("a",class_="feed-post-link",)

#print(noticias_lista)
for noticia in noticias_lista:
    print(noticia.get("href"))
    print(noticia.text)
    print("\n")

