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

        button1.pressed.connect(self.helloworld)        #pressed ogni volta che si clicca
        button2.clicked.connect(self.calculate)         #clicked al rilascio del tasto

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

    def calculate(self):
        print("Calculate")

    def helloworld(self):
        print("Hello World")
#-----------------------------------------------------------

app = QApplication([])
fenster = MyWindow()
app.exec()
