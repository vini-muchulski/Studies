import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    matriz = np.array(list).reshape(3,3)
    valor_max = matriz.max()
    valor_min = matriz.min()
    sum_hori = np.array([0, 0, 0])
    sum_vertical =np.array([0, 0, 0])
    sum_total = 0
    
    indice_maximo = np.argmax(matriz)
    linha_maximo, coluna_maximo = np.unravel_index(indice_maximo, matriz.shape)
    linha_valor_maximo = matriz[linha_maximo]
    

    coluna_valor_maximo = matriz[:, coluna_maximo]
    

     
    index_min = np.argmin(matriz)
    lin_min,coluna_min = np.unravel_index(index_min, matriz.shape)
    linha_valor_min = matriz[lin_min]
    coluna_valor_min = matriz[:, coluna_min]

    
    variancia_h = np.zeros(3)
    variancia_v = np.zeros(3)
    variancia = np.var(matriz)

    media_h = np.zeros(3)
    media_v = np.zeros(3)
    media = np.mean(matriz)

    dp_h =np.zeros(3)
    dp_v = np.zeros(3)
    dp = np.std(matriz)


    for i in range(0,3): 
        for j in range(0,3):
           sum_hori[i]+= matriz[i][j]
           sum_vertical[i] += matriz[j][i]

        sum_total+= sum_hori[i]
        variancia_h[i] = np.var(matriz[i])
        variancia_v[i] = np.var(matriz[:,i])
        media_h[i] = np.mean(matriz[i])
        media_v[i] = np.mean(matriz[:,i])

        dp_v[i] = np.std(matriz[i])
        dp_h[i] =np.std(matriz[:,i])

    print(variancia_h)
    print(variancia_v)
    print(media_h)
    print(media_v)
    print(dp_h)
    print(dp_v)
    print(sum_hori)
    print(sum_vertical)
    print(sum_total)

    print("Linha com valor máximo:", linha_valor_maximo)
    print("Coluna com valor máximo:", coluna_valor_maximo)

    print("Linha com valor  minimo:", linha_valor_min)
    print("Coluna com valor  minimo:", coluna_valor_min)



    calculations = {
  'mean': [media_v, media_h, media],
  'variance': [variancia_v, variancia_h, variancia],
  'standard deviation': [dp_h, dp_v, dp],
  'max': [linha_valor_maximo, coluna_valor_maximo, valor_max],
  'min': [linha_valor_min, coluna_valor_min, valor_min],
  'sum': [sum_vertical, sum_hori, sum_total]
}
    return calculations

calculate([0,1,2,3,4,5,6,7,8])


