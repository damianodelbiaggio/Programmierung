import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumWidth(640)
        self.setMinimumHeight(480)
        self.setWindowTitle("Questa è una finestra")
        self.show()

#-----------------------------------------------------------

app = QApplication([])
fenster = MyWindow()
app.exec()
