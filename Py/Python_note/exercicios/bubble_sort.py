""" Escreva uma função que implemente de um Bubble Sort. Dica: o algorítimo Bubble
 Sort possui complexidade O(n2)."""


lista = [6,8,4,1,2]
aux = 0
for contador in range(1,len(lista)):
    for i in range(0,len(lista)-1):
        if(lista[i]>lista[i+1]): # realiza a troca de elementos, desloca o maior para a frente e puxa o menor
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux


print(lista)
