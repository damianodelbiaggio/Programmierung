import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")

        layout_top = QVBoxLayout()
        layout_bottom = QHBoxLayout()

        button1 = QPushButton("Ok")                     # bottoni
        button2 = QPushButton("Questo è un bottone")
        button3 = QPushButton("Apply")
        button4 = QPushButton("Ciao")
        button5 = QPushButton("Ugo")

        layout_top.addWidget(button1)
        layout_bottom.addWidget(button2)
        layout_bottom.addWidget(button3)
        layout_bottom.addWidget(button4)

        layout_top.addLayout(layout_bottom)

        layout_top.addWidget(button5)

        center = QWidget()
        center.setLayout(layout_top)

        self.setCentralWidget(center)
        self.show()

#-----------------------------------------------------------

app = QApplication([])
fenster = MyWindow()
app.exec()
