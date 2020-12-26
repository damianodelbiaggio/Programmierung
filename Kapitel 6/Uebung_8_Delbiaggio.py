from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("showmap_delbiaggio.ui", self)           #vererbt das file aus Designer

        self.pushButton.clicked.connect(self.buttonfunc)    #Wenn "Auf Karte zeigen..." gedrückt wird, ist die Funktion verbunden
        self.show()


    def buttonfunc(self):

        laenge = self.lineEditLaenge.text()             #LineEditLaenge kommt von Designer aus
        breite = self.lineEditBreite.text()             #LineEditBreite kommt von Designer aus

        deflink = f"https://www.google.ch/maps/place/{laenge},{breite}"

        self.webEngineView.load(QUrl(deflink))         #Variante 1: Direkt in Fenster zeigen (braucht QWebEngineView)
        print(deflink)
        #QDesktopServices.openUrl(QUrl(deflink))         #Variante 2: In browser öffnen (braucht PyQt5.QtGui)


app = QApplication([])
window = MyWindow()
app.exec()