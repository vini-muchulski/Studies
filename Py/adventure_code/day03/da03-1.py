mochilas = ["vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg","wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn","ttgJtRGJQctTZtZT","CrZsJsPPZsGzwwsLwLmpwMDw"]
items = []

#funcao para achar a letra que se repete em cada compartimento
def find_letra(moc1):
    
    tamanho = int(len(moc1)/2)
    moc2 = moc1[tamanho:]

    letra_repetida =""
    for i in range(0,len(moc1)):
        
        for l in range(0,len(moc2)):
            
            if(moc1[i] == moc2[l]):
                
                letra_repetida = moc1[i]
                return letra_repetida

    
contador = 1
dicionario = {}
#cria dicionario com cada letra correspondendo a um valor
for i in range(97,123):
    dicionario[chr(i)] = contador
    contador+=1

for i in range(65,91):
    dicionario[chr(i)] = contador
    contador+=1

#print(dicionario)

#itera sobre as coisas em cada mochila e adiciona o item repetido 
for elemento in mochilas:
    letra = find_letra(elemento)
    items.append(letra)

print(items)

somatorio=0

for item in items:
    
    somatorio += dicionario[item]

print(somatorio)




