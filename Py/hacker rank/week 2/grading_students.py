valor = 84

conta = round((84/5) ,0)*5

print(conta)

import math
def gradingStudents(grades):
    # Write your code here
    notas = []
    
    for grade in grades:
        
        multiplo_5 = math.ceil(grade / 5) * 5
        
        if(grade < 40):
            if((multiplo_5 - grade) < 3 and grade >=38):
                notas.append(int(multiplo_5))
                
            else: 
                notas.append(int(grade))
            
            
        elif((multiplo_5 - grade) < 3):
            notas.append(int(multiplo_5))
            
        
        elif((multiplo_5 - grade) >= 3):
             notas.append(int(grade))
             
    return notas

print(gradingStudents([4,73,67,38,33]))
        