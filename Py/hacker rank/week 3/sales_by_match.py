def sockMerchant(n, ar):
    # Write your code here
    
    numero_valores_unicos = set(ar)
    total_pares = 0
    
    for numero in numero_valores_unicos:
        qtd = ar.count(numero)
        
        total_pares += qtd // 2
        
    return total_pares


ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

print(sockMerchant(len(ar),ar))