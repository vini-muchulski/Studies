from numerizer import numerize
from deep_translator import GoogleTranslator
# o codigo faz a conversao de texto para numero
# o texto pode ser escrito de forma numerica ou escrita

texto = "ola, eu sou o vini e tenho vinte anos"
texto_eng = GoogleTranslator(source="pt",target="en").translate(texto)
print("Texto via tradutor = ", texto_eng)


texto_numerizado = numerize(texto_eng)
print("Texto numerizado = ", texto_numerizado)