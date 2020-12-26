import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")

        layout = QVBoxLayout()              #in verticale

        label = QLabel("Hello World")       #aggiungi etichetta
        lineedit = QLineEdit()              #aggiungi testo 1 riga
        textedit = QTextEdit()              #aggiungi testo su più righe
        button3 = QPushButton("Apply")
        calendar = QCalendarWidget()        #aggiungi calendario

        layout.addWidget(label)
        layout.addWidget(lineedit)
        layout.addWidget(textedit)
        layout.addWidget(button3)
        layout.addWidget(calendar)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

#-----------------------------------------------------------

app = QApplication([])
fenster = MyWindow()
app.exec()
