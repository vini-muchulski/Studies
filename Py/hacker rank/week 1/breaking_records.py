def breaking_records(scores):
    pontuacao = scores
    maior=0
    menor = 0
    count = [0,0]

    for i in range(0,len(pontuacao)):
        if(i == 0):
            maior = pontuacao[0]
            menor = pontuacao[0]

        if(pontuacao[i]>maior):
            maior = pontuacao[i]
            count[0]+=1

        if(pontuacao[i]<menor):
            menor = pontuacao[i]
            count[1]+=1

    return count