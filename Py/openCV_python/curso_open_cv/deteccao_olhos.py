import cv2

carregar_face = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
carregar_olho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

imagem = cv2.imread("fotos/img3.jpg")
img_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = carregar_face.detectMultiScale(img_cinza,scaleFactor=1.1,minNeighbors=15)
                                                    # o scale factor é o quanto a imagem vai ser reduzida
                                                    # o minNeighbors é o número de vizinhos que cada retângulo candidato deve ter para retê-lo

                                                  

print(faces)

for (x, y, l, a) in faces:
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)
    local_olho = imagem[y:y+a, x:x+l]
    local_olho_cinza = cv2.cvtColor(local_olho, cv2.COLOR_BGR2GRAY)
    
    detectado = carregar_olho.detectMultiScale(local_olho_cinza, scaleFactor=1.09)
    for (ox, oy, ol, oa) in detectado:
        cv2.rectangle(local_olho, (ox, oy), (ox + ol, oy + oa), (255, 0, 0), 2)
    
    
    
cv2.imshow("Detecta face e olhos", imagem)
cv2.waitKey()


