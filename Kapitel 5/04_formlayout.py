import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")

        layout = QFormLayout()

        nameInput = QLineEdit()
        adresseInput = QLineEdit()
        okbutton = QPushButton("Ok")

        layout.addRow("Name:", nameInput)
        layout.addRow("Adresse:", adresseInput)
        layout.addRow(okbutton)


        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

#-----------------------------------------------------------

app = QApplication([])
fenster = MyWindow()
app.exec()
