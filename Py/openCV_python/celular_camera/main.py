import cv2

# Este script conecta-se a uma câmera IP, exibe o vídeo em tempo real
# e permite encerrar o programa pressionando 'q'

ip = "http://192.168.1.115:8080/video"
video = cv2.VideoCapture(ip)

if not video.isOpened():
    print("Erro ao conectar com a câmera IP. Verifique o endereço e a conexão.")
else:
    print("Conexão com a câmera IP estabelecida com sucesso.")

    while True:
        ret, frame = video.read()
        if not ret:
            break

        cv2.imshow("Camera IP", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()