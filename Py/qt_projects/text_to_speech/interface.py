# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 630)
        MainWindow.setStyleSheet(" background-color: rgb(34, 40, 49);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 971, 181))
        self.frame.setMinimumSize(QtCore.QSize(971, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 30, 871, 131))
        self.label.setObjectName("label")
        self.input_texto = QtWidgets.QTextEdit(self.centralwidget)
        self.input_texto.setGeometry(QtCore.QRect(50, 230, 521, 321))
        self.input_texto.setMinimumSize(QtCore.QSize(521, 321))
        self.input_texto.setStyleSheet(" background-color: rgb(238, 238, 238);")
        self.input_texto.setObjectName("input_texto")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(668, 280, 311, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.btn_speak = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_speak.setMinimumSize(QtCore.QSize(161, 71))
        self.btn_speak.setStyleSheet("    background-color: rgb(118, 171, 174);\n"
"    \n"
"\n"
"    color: rgb(34, 40, 49); /* Cor do texto */\n"
"    border: 2px solid white; /* Borda com 2px de largura e cor branca */\n"
"    padding: 10px 20px; /* Espaçamento interno */\n"
"    border-radius: 5px; /* Raio da borda */\n"
"    cursor: pointer; /* Mudar o cursor para indicar que é clicável *")
        self.btn_speak.setObjectName("btn_speak")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_speak)
        self.btn_save = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_save.setMinimumSize(QtCore.QSize(161, 71))
        self.btn_save.setStyleSheet("    background-color: rgb(118, 171, 174);\n"
"    \n"
"\n"
"    color: rgb(34, 40, 49); /* Cor do texto */\n"
"    border: 2px solid white; /* Borda com 2px de largura e cor branca */\n"
"    padding: 10px 20px; /* Espaçamento interno */\n"
"    border-radius: 5px; /* Raio da borda */\n"
"    cursor: pointer; /* Mudar o cursor para indicar que é clicável *")
        self.btn_save.setObjectName("btn_save")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.btn_save)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#76abae;\">TEXT TO SPEECH</span></p></body></html>"))
        self.input_texto.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p></body></html>"))
        self.btn_speak.setText(_translate("MainWindow", "Speak"))
        self.btn_save.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
