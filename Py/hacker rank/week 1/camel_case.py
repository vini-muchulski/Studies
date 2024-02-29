# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys

def camelCase(frases):
   frases = frases.split("\n")
   for frase in frases:
    #print(frase)
   
    acao = frase[:1]
    tipo = frase[2:3]

    if(acao == "S"):
        texto = frase[4:]
        palavras = re.findall('[a-zA-Z][^A-Z]*', texto)
        texto_quebrado = ' '.join(palavras)
        texto_quebrado = texto_quebrado.lower()

        if("(" or ")" in texto_quebrado):
          texto_quebrado =   texto_quebrado.replace('(', '').replace(')', '')
          
        print(texto_quebrado)


    if(acao == "C"):
       if(tipo == "V"):
          texto = frase[4:]
          palavras = texto.split()
          texto = palavras[0]

          for i in range(1,len(palavras)):
             palavras[i] = palavras[i].capitalize()
             texto += palavras[i]

          print(texto)

        
       if(tipo == "C"):
            texto = frase[4:]
            palavras = texto.split()
            texto = ""

            for i in range(0,len(palavras)):
             palavras[i] = palavras[i].capitalize()
             texto += palavras[i]

            print(texto)

       if(tipo == "M"):
          texto = frase[4:]
          palavras = texto.split()
          texto = palavras[0]
          
          for i in range(1,len(palavras)):
             palavras[i] = palavras[i].capitalize()
             texto += palavras[i]

          texto+="()"
          print(texto)
          
texto = sys.stdin.read()
camelCase(texto)
