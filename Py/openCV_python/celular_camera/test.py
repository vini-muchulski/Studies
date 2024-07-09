import cv2

video = cv2.VideoCapture()

# Endereço IP correto da sua câmera (ajuste conforme necessário)
ip = "https://192.168.0.115:8080/video"

video.open(ip)

while True:
    check, img = video.read()
    cv2.imshow("img", img)
    cv2.waitKey(1)