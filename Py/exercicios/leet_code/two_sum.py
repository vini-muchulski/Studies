target = 9
lista = [11,15,2,7]

for i in range(0,len(lista)):
    for j in range(0,len(lista)):
        if(lista[i]+ lista[j] == target):
            print(f"{lista[i]} +  {lista[j]}")
            break
        


lista = sorted(lista)
print(lista)

            
            