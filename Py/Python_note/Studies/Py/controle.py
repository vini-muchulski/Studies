from PyQt5 import uic,QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget , QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
import matplotlib.pyplot as plt
import subprocess
import sys

app = QtWidgets.QApplication([])
formulario = uic.loadUi("interface.ui")
formulario.show()
app.exec()
