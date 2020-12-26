#Damiano Delbiaggio, G3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):                     #Konstruktor
        super().__init__()

        self.setWindowTitle("Übung 6")

        layout = QFormLayout()

        self.vornameInput = QLineEdit()
        self.nameInput = QLineEdit()
        self.geburtstagInput = QDateEdit()
        self.adresseInput = QLineEdit()
        self.postleitzahlInput = QLineEdit()
        self.ortInput = QLineEdit()
        self.landInput = QComboBox()
        self.landInput.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.savebutton = QPushButton("Save")

        layout.addRow("Vorname:", self.vornameInput)
        layout.addRow("Name:", self.nameInput)
        layout.addRow("Geburtstag:", self.geburtstagInput)
        layout.addRow("Adresse:", self.adresseInput)
        layout.addRow("PostLeitzahl:", self.postleitzahlInput)
        layout.addRow("Ort:", self.ortInput)
        layout.addRow("Land:", self.landInput)
        layout.addRow(self.savebutton)

        self.savebutton.clicked.connect(self.savefunc)    #Wenn die Knopf "Save" gedrückt wird, ist die Funktion "savefunc" verbunden


        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        quit = QAction("Quit", self)

        save.triggered.connect(self.savefunc)    #Wenn die "Save und Quit" gedrückt werden, sind die Funktion "savefunc" bzw. closefunc verbunden
        quit.triggered.connect(self.closefunc)

        filemenu.addAction(save)
        filemenu.addAction(quit)

    def savefunc(self):               #Funktion zum Drucken und Speichern der eingegebenen Daten
        file = open("Outputdaten.txt", "w", encoding="utf-8")

        vorname = self.vornameInput.text()
        name = self.nameInput.text()
        geburtstag = self.geburtstagInput.date()
        adresse = self.adresseInput.text()
        postleitzahl = self.postleitzahlInput.text()
        ort = self.ortInput.text()
        land =self.landInput.currentText()

        output = f"{vorname}, {name}, {geburtstag.day()}.{geburtstag.month()}.{geburtstag.year()}, {adresse}, {postleitzahl}, {ort}, {land}"

        print(output)

        file.write(output)
        file.close()

    def closefunc(self):            #Funktion, um das ganze Fenster zu schliessen, wenn man auf File --> Quit
        self.close()
#-----------------------------------------------------------

app = QApplication([])
fenster = MyWindow()
app.exec()
