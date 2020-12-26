from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np

class myWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        figure = plt.figure(figsize=(15,8),dpi=150)
        self.canvas = FigureCanvas(figure)

        self.addToolBar(NavigationToolbar(self.canvas, self))

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        layout.addWidget(self.canvas)
        layout.addWidget(button1)
        layout.addWidget(button2)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        button1.clicked.connect(self.show1)
        button2.clicked.connect(self.show2)

        self.show()

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
window = myWindow()
app.exec()