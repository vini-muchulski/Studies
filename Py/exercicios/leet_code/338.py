# https://www.youtube.com/watch?v=7jdGytv9YD0&list=PLP_dh3S9H39kSv9Ke0Ezie8HAlm5zfVhc&index=4

def count_bits(n):
    lista = []
    
    for i in range(0,n+1):
       lista.append(get_binario(i))
       
       
    print(lista)
   

def get_binario(numero):
    res = []
    cont = 0
    
    while numero>0:
    
      resto =  numero % 2
      res.append(resto)
      numero = numero // 2
      
      if resto == 1:
          cont+=1
            
     
    #print(cont)  
    #print(res[::-1])
    
    return cont
    
#get_binario(4)

count_bits(5)