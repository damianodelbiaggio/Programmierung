import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")

        layout = QGridLayout()
        nameLabel = QLabel("Name:")
        nameInput = QLineEdit()
        adresseLabel = QLabel("Adresse:")
        adresseInput = QLineEdit()

        layout.addWidget(nameLabel, 0, 0)               #coordinate cartesiane
        layout.addWidget(nameInput, 0, 1)
        layout.addWidget(adresseLabel, 1, 0)
        layout.addWidget(adresseInput, 1, 1)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

#-----------------------------------------------------------

app = QApplication([])
fenster = MyWindow()
app.exec()
