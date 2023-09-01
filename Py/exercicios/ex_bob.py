def bob(frase):
    frase_up = frase.upper()

    contem_letras = False

    for caractere in frase:
        if caractere.isalpha():
            contem_letras = True
            break

    if(frase.strip()==""):
        return "Fine. Be that way!"
    
    elif(frase_up == frase and frase[-1] == "?" and contem_letras == True):
        return "Calm down, I know what I'm doing!"
    
    elif(frase[-1] == "?" ):
        return "Sure."
    
    elif(frase[-1] == "?" and contem_letras == False):
        return "Sure."
    
    elif(frase_up == frase and contem_letras):
        return "Whoa, chill out!"
    
    
    
    else:

        return "Whatever."
    
print(bob("4?"))

"""
def response(hey_bob):
    frase = hey_bob.strip()
    frase_up = frase.upper()

    contem_letras = False

    for caractere in frase:
        if caractere.isalpha():
            contem_letras = True
            break

    if(frase.strip()==""):
        return "Fine. Be that way!"
    
    elif(frase_up == frase and frase[-1] == "?"):
        return "Calm down, I know what I'm doing!"
    
    elif(frase[-1] == "?" ):
        return "Sure."
    
    elif(frase_up == frase and contem_letras):
        return "Whoa, chill out!"
    
    
    
    else:

        return "Whatever."

        """
