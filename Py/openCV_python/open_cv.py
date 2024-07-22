import cv2

carregar_algoritmo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread("fotos/img1.jpg")
img_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = carregar_algoritmo.detectMultiScale(img_cinza,scaleFactor=1.07,minNeighbors=15)
                                                    # o scale factor é o quanto a imagem vai ser reduzida
                                                    # o minNeighbors é o número de vizinhos que cada retângulo candidato deve ter para retê-lo

print(faces)

for (x, y, l, a) in faces:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)
    
    
cv2.imshow("Faces", imagem)
cv2.waitKey()


