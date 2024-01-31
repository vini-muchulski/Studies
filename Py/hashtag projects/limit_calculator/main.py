from PyQt5 import uic,QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget , QVBoxLayout
import sympy as sp


def calculate_limit():
    sym = sp.symbols(formulario.simbolo_input.text())
    expression = formulario.expressao_input.text()
    limite_valor = formulario.limite_input.text()
    limite = sp.limit(expression,sym,limite_valor)

    print(limite)





app = QtWidgets.QApplication([])
formulario = uic.loadUi("limite_calc.ui")

formulario.setWindowIcon(QtGui.QIcon('logo.jpg'))
formulario.setWindowTitle("Calculadora de limites")
formulario.btn_calcular.clicked.connect(calculate_limit)



formulario.show()
app.exec()