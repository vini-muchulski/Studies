def countSeniors(listas):
    contador = 0
    for lista in listas:
        age = int(lista[11:13])
        
        if(age>60):
            contador+=1
            
    #print(contador)
    return contador
    
    
countSeniors(["1313579440F2036","2921522980M5644"])
    
    