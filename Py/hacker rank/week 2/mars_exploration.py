def marsExploration(s):
    # Write your code here
    tamanho = len(s)
    cont_letras = 0
    
    for i in range(0,tamanho):
        if (i % 3 == 0):
            if( s[i] == "S"):
                pass
            
            else:
                cont_letras +=1
            
        if (i % 3 == 1):
            if( s[i] == "O"):
                pass
            
            else:
                cont_letras +=1
            
        if (i % 3 == 2):
            
            if( s[i] == "S"):
                pass
            
            else:
                cont_letras +=1
                
    return cont_letras

print(marsExploration("SOSSOT"))
            
        
    