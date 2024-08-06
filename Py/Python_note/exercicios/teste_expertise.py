"""Escreva um loop que imprima de 1 a 100. Mas, se o número for divisível por 3,
 imprima Fizz no lugar do número; se o número for divisível por 5, imprima Buzz no
 lugar do número; e se o número for divisível por 3 e 5, imprima FizzBuzz"""

for i in range(1,101):

    if(i%3 == 0 and i%5 == 0):
        print("FizzBuzz")

    elif(i%3 == 0):
        print("Fizz")

    elif(i%5 == 0):
        print("buzz")

    else:
        print(i)