import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(lista):
    # Write your code here
    lonely_integer= 0
    for valor in lista:
        rep = lista.count(valor)
        
        if(rep == 1):
            lonely_integer = valor
    
    return lonely_integer


a = [1,2,3,4,3,2,1]

print(lonelyinteger(a))


