
def flippingBits(n):
    # Write your code here
    n = bin(n)

    n = str(n)[2:].zfill(32)
    n = n.replace("1","*")
    n = n.replace("0","1")
    n = n.replace("*","0")
    
    
    
    #print(n)
    
    n = int(n,2)
    #print(n)
    
    return n
    
nm = "00000000000000000000000000001001"

flippingBits(9)