#Damiano Delbiaggio, G3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import urllib.parse

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
        self.kartebutton = QPushButton("Auf Karte zeigen")
        self.ladenbutton = QPushButton("Laden")
        self.savebutton = QPushButton("Speichern")

        layout.addRow("Vorname:", self.vornameInput)
        layout.addRow("Name:", self.nameInput)
        layout.addRow("Geburtstag:", self.geburtstagInput)
        layout.addRow("Adresse:", self.adresseInput)
        layout.addRow("PostLeitzahl:", self.postleitzahlInput)
        layout.addRow("Ort:", self.ortInput)
        layout.addRow("Land:", self.landInput)
        layout.addRow(self.kartebutton)
        layout.addRow(self.ladenbutton)
        layout.addRow(self.savebutton)

        self.savebutton.clicked.connect(self.savefunc)    #Wenn die Knopfe gedrückt werden, sind die Funktionen verbunden
        self.kartebutton.clicked.connect(self.kartefunc)
        self.ladenbutton.clicked.connect(self.ladenfunc)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        viewmenu = menubar.addMenu("View")


        save = QAction("Save", self)
        quit = QAction("Quit", self)
        karte = QAction("Karte", self)
        laden = QAction("Laden", self)

        save.triggered.connect(self.savefunc)    #Wenn die "Save, Quit, Karte und Laden" gedrückt werden, sind die dazugehörige Fuktionen verbunden
        quit.triggered.connect(self.closefunc)
        karte.triggered.connect(self.kartefunc)
        laden.triggered.connect(self.ladenfunc)


        filemenu.addAction(save)
        filemenu.addAction(quit)
        filemenu.addAction(laden)
        viewmenu.addAction(karte)

    def savefunc(self):               #Funktion zum Speichern der eingegebenen Daten in txt in eine bestimmte Verzeichnis
        dir = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        filename, filter = QFileDialog.getSaveFileName(self, "Textdatei speichern", dir, "Textdatei (*.txt);;Text (*.txt")

        if filename !="":

            file = open(filename, "w", encoding="utf-8")

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

    def kartefunc(self):

        adresse = self.adresseInput.text()
        postleitzahl = self.postleitzahlInput.text()
        ort = self.ortInput.text()

        land = self.landInput.currentText()
        link1 = "https://www.google.ch/maps/place/"         # Link Google Maps ohne Adresse usw.
        link2 = f"{adresse}+{postleitzahl}+{ort}+{land}"    # Adresse, PLZ, Ort und Land Teil
        link3 = link2.replace(" ", "+")                     # Leerzeichen -> +

        deflink = f"{link1}+{urllib.parse.quote(link3)}"                        # Zusammensetzung links

        QDesktopServices.openUrl(QUrl(deflink))

        self.show()

    def ladenfunc(self):                                    #Funktion zum öffnen einer txt aus eine bestimmte Verzeichnis + drucken
        dir = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        filename, filter = QFileDialog.getOpenFileName(self, "Öffnen", dir, "Nur Text Dateien (*.txt*);;Text (*.txt)")

        if filename != "":

            file = open(filename,"r",  encoding="utf-8")
            for zeile in file:
                daten = zeile.split(",")
                vorname = daten[0]
                name = daten[1]
                geburtstag = daten[2]
                adresse = daten[3]
                postleitzahl = daten[4]
                ort = daten[5]
                land = daten[6]
                self.vornameInput.setText(vorname)
                self.nameInput.setText(name)
                self.geburtstagInput.setDate((QDate.fromString(geburtstag, "dd/MM/yyyy")))
                self.adresseInput.setText(adresse)
                self.postleitzahlInput.setText(postleitzahl)
                self.ortInput.setText(ort)
                self.landInput.setCurrentText(land)

                print(filename)
            file.close()
        else:
            QMessageBox.warning(self, "Warnung", "Kein Filename angegeben")



    def closefunc(self):            #Funktion, um das ganze Fenster zu schliessen, wenn man auf File --> Quit
        self.close()
#-----------------------------------------------------------

app = QApplication([])
fenster = MyWindow()
app.exec()
