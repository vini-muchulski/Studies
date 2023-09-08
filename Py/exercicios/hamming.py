def distance(fita_a, fita_b):
    if(len(fita_a) != len(fita_b)):
        raise ValueError("Strands must be of equal length.")
    
    tamanho = len(fita_a)
    erros = 0

    for indice in range(0,tamanho):

        if (fita_a[indice] != fita_b[indice]):
            erros+=1

    return erros

