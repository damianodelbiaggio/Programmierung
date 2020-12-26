import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")

        layout = QHBoxLayout()                              #in orizzontale

        button1 = QPushButton("Ok")                         #bottoni
        button2 = QPushButton("Questo è un bottone")
        button3 = QPushButton("Apply")

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

#-----------------------------------------------------------

app = QApplication([])
fenster = MyWindow()
app.exec()
