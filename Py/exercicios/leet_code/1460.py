def canBeEqual( target, lista):
    target.sort()
    
    lista.sort()
    
    tamanho = len(target)
    tamanho_b = len(lista)
    
    print(lista)
    print(target)
    
    if(tamanho != tamanho_b):
        return False
    
    
    
    for i in range(0,tamanho):
        if(target[i] != lista[i]):
            return False
    
    return True
    
print(canBeEqual([3,7,9],[3,7,11]))
     
    