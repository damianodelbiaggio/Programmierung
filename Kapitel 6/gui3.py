from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *


def buttonclick():
    print("Hello World")


app = QApplication([])
window = loadUi("test2.ui")

window.Button1.clicked.connect(buttonclick)

window.show()
app.exec()

