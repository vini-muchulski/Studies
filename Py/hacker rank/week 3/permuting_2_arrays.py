def twoArrays(k, A, B):
    # Write your code here
    resultado = "YES"
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        if A[i] + B[i] < k:
            resultado = "NO"
    
                
                
    return resultado

#A = [2, 1, 3]
#B = [7, 8, 9]

A = [1, 2, 2, 1]
B = [3, 3, 3, 4]

x = twoArrays(5,A,B)

print(x)
                