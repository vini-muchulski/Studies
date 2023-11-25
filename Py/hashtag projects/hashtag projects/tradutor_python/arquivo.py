from deep_translator import GoogleTranslator
#https://www.youtube.com/watch?v=_HLyt8Rvx3Q&list=PLP_dh3S9H39kSv9Ke0Ezie8HAlm5zfVhc&index=5


tradutor = GoogleTranslator(source='pt', target='french')
#source: idioma de origem
#target: idioma de destino - nome da lingua escrito em ingles

texto = "o cavalo preto"
traducao = tradutor.translate(texto)
print(traducao)

texto = "eu sou uma maça"
traducao = tradutor.translate(texto)
print(traducao)
