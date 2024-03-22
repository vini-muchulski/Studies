from gtts import gTTS
import os

from PyQt5 import uic,QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget

#https://www.youtube.com/watch?v=fEL8ihL-GXg&list=PLP_dh3S9H39kSv9Ke0Ezie8HAlm5zfVhc&index=1


def get_texto():
    texto = formulario.input_texto.toPlainText()
    return texto
    

def audio_ler():
    texto = get_texto()

    linguagem = "pt"

    tts = gTTS(texto, lang=linguagem)

   
    tts.save("audio.mp3")
    os.system('ffplay -autoexit -nodisp audio.mp3')

def salvar_audio():
    texto = get_texto()

    linguagem = "pt"

    tts = gTTS(texto, lang=linguagem)

   
    tts.save("audio_salvo.mp3")
    
    
app = QtWidgets.QApplication([])
formulario = uic.loadUi("interface.ui")



#formulario.setWindowIcon(QtGui.QIcon('logo.png'))
formulario.setWindowTitle("Text To Speech")
formulario.btn_speak.clicked.connect(audio_ler)
formulario.btn_save.clicked.connect(salvar_audio)

formulario.show()
app.exec()




