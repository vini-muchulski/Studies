from PIL import Image, ImageFilter

imagem = Image.open("img2.png")


#imagem.show()

#converter formato da imagem
img_rgb = imagem.convert("RGB")



tamanho = (600,400)

img_rgb.thumbnail(tamanho)
img_rgb.save("img.jpg")



#editar imagens

#rotacionar
img_rgb.rotate(90).save("img_rotacionado.jpg")


#editar cores
img_rgb.convert("L").save("img_pb.jpg")



#filtros
img_rgb.filter(ImageFilter.FIND_EDGES).save("img_FILTRO.jpg")

