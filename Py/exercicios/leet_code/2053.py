def kthDistinct( arr, k: int) -> str:
    lista_unicos = []
    contador = 0
    
    for i in range(0,len(arr)):
        elemento = arr[i]
        for j in range(0,len(arr)):
            if(arr[j] == elemento):
                contador = contador + 1
                
        if(contador == 1):
            lista_unicos.append(elemento)
            
        contador = 0
    
    print(lista_unicos)
    
    if(k > len(lista_unicos)):
        return ""
    
    
    k = k-1
    
    return lista_unicos[k]
    
    
    
    
    
    
print(kthDistinct(["d","b","c","b","c","a"],2))
            
            
    