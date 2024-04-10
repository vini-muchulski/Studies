
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget , QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
import matplotlib.pyplot as plt
import subprocess
import sys

class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.setWindowTitle('Interface')
        self.setGeometry(100, 100, 1000, 1000)





aplicacao = QApplication(sys.argv)
janela = Interface()
sys.exit(aplicacao.exec_())

