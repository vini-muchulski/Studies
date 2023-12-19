
from PyQt5 import uic,QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget

import wget


def baixar():
    link = formulario.input_link.text()
    #formato = link
    wget.download(link)


app = QtWidgets.QApplication([])
formulario = uic.loadUi("interface_wget.ui")



formulario.setWindowIcon(QtGui.QIcon('logo.jpg'))
#formulario.setWindowTitle("Interface")
formulario.btn_download.clicked.connect(baixar)

formulario.show()
app.exec()
