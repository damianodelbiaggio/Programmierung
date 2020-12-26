from PyQt5.QtWidgets import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("gui.ui", self)

        figure = plt.figure(figsize=(16, 9), dpi=200)
        self.canvas = FigureCanvas(figure)

        self.verticalLayout.removeWidget(self.widget)
        self.verticalLayout.insertWidget(0, self.canvas)

        self.show()

        self.button1.clicked.connect(self.show1)
        self.button2.clicked.connect(self.show2)

    def show1(self):
        plt.clf()
        x = np.linspace(0, 2 * np.pi, 25)
        y = np.sin(x)
        plt.title("Sinuskurve")
        plt.plot(x, y, 'ro-')
        plt.axis('equal')

        self.canvas.draw()

    def show2(self):
        plt.clf()
        x = np.linspace(0, 2 * np.pi, 25)
        y = np.cos(x)
        plt.title("Cosinuskurve")
        plt.plot(x, y, 'bo-')
        plt.axis('equal')

        self.canvas.draw()


app = QApplication([])
window = MyWindow()
app.exec()