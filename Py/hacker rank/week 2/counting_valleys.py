def countingValleys(steps, path):
    # Write your code here
    base = 0
    altura = 0
    last_path = 0
    cont_vales = 0

    
    for i in range(0,steps):
        letra = path[i]
        
       
        if letra == "U":
            altura += 1
            
            
        if letra == "D":
            altura -=1

            
        if altura == 0 and last_path < 0:
            #print("nivel do mar")
            cont_vales+=1
            #if last_path == "D":
                
        #print(altura)
        last_path = altura
    
    
    return cont_vales
    
    
#print(countingValleys(8,"UDDDUDUU"))
#print(countingValleys(X,"DUDDUUUUDDD"))
print(countingValleys(12,"DDUUDDUDUUUD"))
    