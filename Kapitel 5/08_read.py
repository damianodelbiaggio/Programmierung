import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")

        layout = QFormLayout()

        self.nameInput = QLineEdit()                               #self.nameInput = QLineEdit("Dies ist der Default text") funziona anche
        self.nameInput.setText("Dies ist der Default text")        #impostare testo di default
        self.adresseInput = QLineEdit()
        self.okbutton = QPushButton("Ok")

        layout.addRow("Name:", self.nameInput)
        layout.addRow("Adresse:", self.adresseInput)
        layout.addRow(self.okbutton)

        self.okbutton.clicked.connect(self.auswertung)             #scrivere qualcosa nella barra comandi quando si clicca "OK"


        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

    def auswertung(self):
        name = self.nameInput.text()
        adresse = self.adresseInput.text()

        print("Il nome è:", name)
        print("L'indirizzo è:", adresse)

#-----------------------------------------------------------

app = QApplication([])
fenster = MyWindow()
app.exec()
