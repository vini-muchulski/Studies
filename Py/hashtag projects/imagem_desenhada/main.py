import cv2

# https://www.youtube.com/watch?v=8sGSJD01WEg
# transformar foto em desenho com Python, tipo aqueles filtros que você tem nas redes sociais 

img = cv2.imread("foto.jpg")

img_pb = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_invertida = cv2.bitwise_not(img_pb)
                                        #quantidade de filtro
qtd_filtro = 95 #valor deve ser impar

img_blur = cv2.GaussianBlur(img_invertida,(qtd_filtro,qtd_filtro),0)

img_blur_invertida = cv2.bitwise_not(img_blur)

img_desenhada = cv2.divide(img_pb,img_blur_invertida,   scale=256.0) # 0 - 255 / 0 - 255 -> cores mt proximas, valores entre 0 e 1

cv2.imshow("foto show", img_desenhada)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("foto_desenhada.jpg",img_desenhada)