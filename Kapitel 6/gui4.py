from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("test2.ui", self)
        self.show()

        self.Button1.clicked.connect(self.button1click)

    def button1click(self):
        s = self.lineEdit.text()
        QMessageBox.information(self, "Info", s)

app = QApplication([])
window = MyWindow()
app.exec()