def diagonalDifference(matriz):
    # Write your code here
    
    tamanho = len(matriz)
    #print(matriz)
    #print(len(matriz))
    
    diag_principal = 0
    diag_sec = 0
    
    for i in range(0,len(matriz)):
        diag_principal += matriz[i][i]
        diag_sec += matriz[i][tamanho-1-i]
    
    #print(f"Principal = {diag_principal}  Sec = {diag_sec}")
    
    diferenca = abs((diag_principal-diag_sec))
    
    return diferenca
    
lista = [
    3,  # Número de linhas da matriz
    [
        [11, 2, 4],   # Primeira linha da matriz
        [4, 5, 6],    # Segunda linha da matriz
        [10, 8, -12]  # Terceira linha da matriz
    ]
]

diagonalDifference(lista)
