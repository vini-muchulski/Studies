import requests

#https://www.youtube.com/watch?v=WWVEymSt1iI

link = "https://1012dffc-d1f7-412d-a8ee-5a566e72cd67-00-1fmod1dknydvp.janeway.replit.dev/pegarvendas"

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())