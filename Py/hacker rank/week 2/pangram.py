import string

def pangrams(s):
    # Write your code here
    tamanho = len(s)
    letras = string.ascii_lowercase
    dicionario_letras = {letra: 0 for letra in letras}
    pangram = True

    s = s.lower()
    
    for letra in s:
        if letra in dicionario_letras:
            dicionario_letras[letra]+= 1
            
    
    for letra in dicionario_letras.keys():
        if (dicionario_letras[letra] == 0):
            pangram = False
            
    if (pangram):
        return "pangram"
    
    else: 
        return "not pangram"
    
    
print(pangrams("We promptly judged antique ivory buckles for the prize"))
    
        
