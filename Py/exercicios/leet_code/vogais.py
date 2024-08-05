def possui_vogal(palavra):
    palavra = palavra.upper()
    vogais = ["A","E","I","O","U"]
    
    existe_vogal = False
    
    for vogal in vogais:
        if vogal in palavra:
            existe_vogal = True
            print(vogal)
            
    print("Existe vogal: ",existe_vogal)
    
    
possui_vogal("abacaxi")
