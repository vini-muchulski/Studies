def birthday(s, d, m):
    count = 0
    # Percorre a lista de números
    for t1 in range(len(s)-m+1):
        num = 0
        # Para cada sublista de tamanho m
        for t2 in range(m):
            # Soma os números na sublista
            num += s[t1+t2]
        # Se a soma for igual a d
        if num == d:
            # Incrementa a contagem
            count += 1
    # Retorna a contagem
    return count

