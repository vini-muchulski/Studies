import cv2

# Este script conecta-se a uma câmera IP, exibe o vídeo em tempo real
# e permite encerrar o programa pressionando 'q'

ip = "http://192.168.0.107:8080/video"
video = cv2.VideoCapture(ip)
classificador_video_face = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')


while True:
    camera, frame = video.read()
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detecta = classificador_video_face.detectMultiScale(cinza)
    
    for (x, y, l, a) in detecta:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 255, 0), 2)
        
        
    cv2.imshow("WebCamera IP", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()