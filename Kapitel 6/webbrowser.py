from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("test3.ui", self)
        self.show()


        html = "<h1>Clicca load per procedere</h1>"
        self.webEngineView.setHtml(html)
        #self.webEngineView.load(QUrl('http://maps.google.com'))

        self.pushButton.clicked.connect(self.loadWebPage)

    def loadWebPage(self):
        self.webEngineView.load(QUrl('http://www.fhnw.ch'))

app = QApplication([])
window = MyWindow()
app.exec()