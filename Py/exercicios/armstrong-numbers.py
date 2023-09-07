def armstrong_numbers(number):
    num_str = str(number)
    tamanho = len(num_str)

    somatorio = 0

    for algarismo in num_str:
        somatorio += int(algarismo)**tamanho

    
    if(somatorio == number):
        return True
    
    else:
        return False



