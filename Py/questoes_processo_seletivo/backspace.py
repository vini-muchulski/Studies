def compareStrings(s1, s2):
    # Write your code here
    
    frase_1 = trata_string(s1)
    
    frase_2 = trata_string(s2)
    
    if frase_1 == frase_2:
        return 1
    
    else:
        return 0
    
    

    
def trata_string(letras): # funcao que retira os caracteres especiais
    lista = []
    
    for letra in letras:
        if letra != "#":
            lista.append(letra)
            
        elif lista: # se ela nao for vazia entra aqui
            lista.pop()
            
    frase = "".join(lista)
    
    return lista



    