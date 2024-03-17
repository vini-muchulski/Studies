def caesarCipher(s, k):
    # Write your code here
    #letra = ord(s[0])  # Obtem o codigo Unicode da letra em minusculo
    #print(letra)
    #print(chr(letra))
    #print(chr(letra+k)) # Converte o codigo Unicode de volta para uma letra
    #s = s.lower()
    
    frase_encriptada = ""
    
    for l in s:
        if(l.isalpha()):
            if l.islower():
                base = ord('a')
            elif l.isupper():
                base = ord('A')
            
            letra = ord(l)
            letra = (letra - base + k) % 26 + base
            
            letra = chr(letra)
            frase_encriptada+= letra
    
        else:
            frase_encriptada+= l
            
    #print(frase_encriptada)
    return frase_encriptada
    
    
    
caesarCipher("Ciphering.",26)