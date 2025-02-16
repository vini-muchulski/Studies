# -*- coding: utf-8 -*-
"""reconhecimento_facial

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RMLuT6VaUIKwysxEv6Y0YlUST75oEuKx
"""

!pip install mediapipe

import cv2
import mediapipe as mp

#inicializacao opencv
webcam = cv2.VideoCapture(0)

solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    #ler informacoes da webcam
    verificador, frame = webcam.read()

    if not verificador:
        break

    #reconhecer os rostos
    lista_rostos = reconhecedor_rostos.process(frame)

    if lista_rostos.detections:

        for rosto in lista_rostos.detections:
            #desenhar os rostos na imagem
            desenho.draw_detection(frame,rosto)

    cv2.imshow("Rostos na webcam",frame)


    #quando apertar ESC, para o loop
    if cv2.waitKey(5) == 27 : #esc = 27 ou ord()
        break

webcam.release()
cv2.destroyAllWindows()

webcam.release()