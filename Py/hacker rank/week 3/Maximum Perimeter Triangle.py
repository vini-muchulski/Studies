def triangulo_existe(a, b, c):


  if a + b <= c:
    return False
  elif a + c <= b:
    return False
  elif b + c <= a:
    return False
  else:
    return True


def maximumPerimeterTriangle(sticks):
    # Write your code here
    triangulos_ = []
    triangulo = []
    
    #sticks = sorted(sticks)
    
    for i in range(0,len(sticks)-2):
        perimetro = 0
        triangulo = []
        
        if(triangulo_existe(sticks[i],sticks[i+1],sticks[i+2])):
            perimetro  = sticks[i]+sticks[i+1]+sticks[i+2]
            triangulo.append(sticks[i])
            triangulo.append(sticks[i+1])
            triangulo.append(sticks[i+2])
            triangulos_.append(triangulo)
    
    #pegar maior perimetro
    indice_maior = 0
    perimetro_maior = 0
    perimetro = 0
    for i in range(0,len(triangulos_)):
        for j in range (0,3):
            perimetro += triangulos_[i][j]
            
        if(perimetro > perimetro_maior):
            perimetro_maior = perimetro
            indice_maior = i
      
    
    
          
    if(len(triangulos_) == 0):
        return -1
    
    else:
        return triangulos_[indice_maior]
    
    
print(maximumPerimeterTriangle([1,2,3,4,5,10]))
print(maximumPerimeterTriangle([1, 2 ,3]))
            

            
        