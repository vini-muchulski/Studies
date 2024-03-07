from PIL import Image
import os

#abrir o arquivo
lista_arquivos = os.listdir("imagens")


for arquivo in lista_arquivos:
    imagem = Image.open(f"imagens/{arquivo}").convert("RGB")
    if "jfif" in arquivo:
        imagem.save(arquivo.replace("jfif","jpeg"))
        
    if "webp" in arquivo:
        imagem.save(arquivo.replace("webp","jpeg"))
        
    if "jpg" in arquivo:
        imagem.save(arquivo.replace("jpg","jpeg"))
        
    

#salvar o arquivo com o outro formato
