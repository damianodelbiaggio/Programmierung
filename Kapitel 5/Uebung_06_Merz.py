import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Übung 6")

        layout = QFormLayout()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        quit = QAction("Exit", self)

        save.triggered.connect(self.savefunc)
        quit.triggered.connect(self.closefunc)

        filemenu.addAction(save)
        filemenu.addAction(quit)

        self.prenameInput = QLineEdit()
        self.nameInput = QLineEdit()
        self.birthdayInput = QDateEdit()
        self.addressInput = QLineEdit()
        self.postcodeInput = QLineEdit()
        self.townInput = QLineEdit()
        self.countryInput = QComboBox()
        self.countryInput.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.savebutton = QPushButton("Save")

        layout.addRow("Vorname:", self.prenameInput)
        layout.addRow("Name:", self.nameInput)
        layout.addRow("Geburtstag:", self.birthdayInput)
        layout.addRow("Adresse:", self.addressInput)
        layout.addRow("Postleitzahl:", self.postcodeInput)
        layout.addRow("Ort:", self.townInput)
        layout.addRow("Land", self.countryInput)
        layout.addRow(self.savebutton)

        self.savebutton.clicked.connect(self.savefunc)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

    def savefunc(self):
        file = open("output.txt", "w", encoding="utf-8")

        prename = self.prenameInput.text()
        name = self.nameInput.text()
        birthday = self.birthdayInput.date()
        address = self.addressInput.text()
        postcode = self.postcodeInput.text()
        town = self.townInput.text()
        country = self.countryInput.currentText()

        output = f"{prename},{name},{birthday.day()}.{birthday.month()}.{birthday.year()},{address},{postcode},{town},{country}"

        print(output)

        file.write(output)
        file.close()

    def closefunc(self):
        self.close()

# -----------------------------------------------------------------------------

app = QApplication([])
fenster = MyWindow()
app.exec()