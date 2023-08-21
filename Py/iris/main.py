#codigo acessa banco de dados de tamanho de petalas de flores

bd = []

with open("iris.data", "r") as arquivo:
    
    for dado in arquivo.readlines():
        bd.append(dado.split(","))

#for posicao in bd:
   # print(posicao)