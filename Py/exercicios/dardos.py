def score(x, y):
    distancia = (x*x + y*y)**(1/2)

    if (distancia <= 1):
        return 10
    
    elif (distancia <= 5):
        return 5
    
    elif (distancia <= 10):
        return 1
    
    else:
        return 0
    

    
