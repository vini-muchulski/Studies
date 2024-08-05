def kidsWithCandies( candies, extraCandies):
    max_value = max(candies)
    lista = []
    for i in range(0,len(candies)):
        
        if (candies[i] + extraCandies>= max_value):
            lista.append(True)
            
        else:
            lista.append(False)
            
    return lista
    #print(lista)

#kidsWithCandies([12,1,12],10)

