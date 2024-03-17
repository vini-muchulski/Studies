def migratoryBirds(arr):
    # Write your code here
    conjunto = set(arr)
    contagem = {}
    
    
    
    for numero in conjunto:
        contagem[numero] = arr.count(numero)
    
    
            
            
    contagem = dict(sorted(contagem.items()))
    
    print(contagem)
    
    valor = (max(contagem, key=contagem.get))
    print(valor)
    return valor
    
    
migratoryBirds([1, 4 ,4 ,4 ,5 ,3])