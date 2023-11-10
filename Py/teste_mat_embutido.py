from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg , NavigationToolbar2QT 
from matplotlib.figure import Figure
import sys


class Janela(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.resize(800, 600)
        self.move(400, 200)
        self.setWindowTitle('Teste Matplotlib Embutido')
        layout = QVBoxLayout()
        self.setLayout(layout)

        canvas = FigureCanvasQTAgg(fig)
        layout.addWidget(canvas)

        toolbar = NavigationToolbar2QT(canvas, self)
        layout.addWidget(toolbar)
        

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]   

fig = Figure()
ax = fig.add_subplot()
ax.plot(x, y)


app = QApplication(sys.argv)
window = Janela()
window.show()
sys.exit(app.exec_())