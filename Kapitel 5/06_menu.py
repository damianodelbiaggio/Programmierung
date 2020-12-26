import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def openfunc(self):             #questa funzione può essere scritta anche in fondo
        print("Open triggered")

    def closefunc(self):            #funzione per chiudere tutta la finestra quando si preme file --> exit
        self.close()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        editmenu = menubar.addMenu("Edit")
        viewmenu = menubar.addMenu("View")

        open = QAction("Open", self)

        save = QAction("Save", self)
        quit = QAction("Exit", self)

        open.triggered.connect(self.openfunc)           #collegare click alle funzioni sopra
        quit.triggered.connect(self.closefunc)

        filemenu.addAction(open)
        filemenu.addAction(save)
        filemenu.addAction(quit)

        layout_top = QVBoxLayout()
        layout_bottom = QHBoxLayout()

        button1 = QPushButton("Ok")                     # bottoni
        button2 = QPushButton("Questo è un bottone")
        button3 = QPushButton("Apply")
        button4 = QPushButton("Ciao")
        button5 = QPushButton("Ugo")

        layout_top.addWidget(button1)
        layout_bottom.addWidget(button2)
        layout_bottom.addWidget(button3)
        layout_bottom.addWidget(button4)

        layout_top.addLayout(layout_bottom)

        layout_top.addWidget(button5)

        center = QWidget()
        center.setLayout(layout_top)

        self.setCentralWidget(center)
        self.show()

#-----------------------------------------------------------

app = QApplication([])
fenster = MyWindow()
app.exec()
