from numerizer import numerize
# o codigo faz a conversao de texto para numero
# o texto pode ser escrito de forma numerica ou escrita
# exemplo: 21 ou twenty one
#https://www.youtube.com/watch?v=ZkkIxJSLpr0

texto = "twenty one"
numero_texturizado = numerize(texto)
#print(numero_texturizado)
print(int(numero_texturizado))

#identifica o que no texto que é um numero e traduz esse numero para algarismos
frase = "twenty one pilots and five seconds of summer"
frase_texturizada = numerize(frase)
print(frase_texturizada) 