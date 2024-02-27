def plusMinus(arr):
    qtd_positivos = 0
    qntd_negativos = 0
    zeross = 0
    tamanho = len(arr)

    for x in range (0,len(arr)):
        if(arr[x]== 0):
            zeross+=1

        if(arr[x]< 0):
            qntd_negativos+=1
        
        if(arr[x]> 0):
            qtd_positivos+=1


    print(qtd_positivos/tamanho)
    print(qntd_negativos/tamanho)
    print(zeross/tamanho)


lista = [1,1,0,-1,-1]
plusMinus(lista)



