def divisibleSumPairs(n, k, ar):
    # Write your code here
    numero_de_pares = 0
    soma = 0
    for i in range(0,n):
        for j in range(i+1, n):  # Garante que j seja sempre maior que i

            
            soma = ar[i] + ar[j]

            if(soma % k == 0):
                numero_de_pares+=1

    return numero_de_pares