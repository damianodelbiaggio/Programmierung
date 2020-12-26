from PyQt5.QtWidgets import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np


class myWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("uebung_09_delbiaggio.ui", self)

        figure = plt.figure(figsize=(16, 9), dpi=140)
        self.canvas = FigureCanvas(figure)

        self.verticalLayout.removeWidget(self.widget)
        self.verticalLayout.insertWidget(0, self.canvas)
        self.comboBoxColor.addItems(["red","green","blue"])
        self.show()

        self.showbutton.clicked.connect(self.darstellung)
        self.pSlider.valueChanged.connect(self.input)
        self.spinBoxMin.valueChanged.connect(self.input)
        self.spinBoxMax.valueChanged.connect(self.input)
        self.comboBoxColor.currentTextChanged.connect(self.input)

    def input(self):
        self.darstellung()

    def darstellung(self):
        plt.clf()
        koef = self.koefEdit.text()
        koeflist = koef.split(",")
        newlist = []
        points = self.pSlider.value()
        min_x = self.spinBoxMin.value()
        max_x = self.spinBoxMax.value()
        color = self.comboBoxColor.currentText()
        for i in koeflist:
            try:
                newlist.append(int(i))
            except:
                QMessageBox.critical(self, "Fehler", "Ganze Zahlen eingeben bitte")
        f = np.poly1d(newlist)
        x = np.linspace(min_x, max_x, points)
        y = f(x)
        plt.title("Polynom")
        plt.plot(x, y, color,marker='o',linestyle='-')
        plt.axis('auto')
        self.canvas.draw()


app = QApplication([])
window = myWindow()
app.exec()