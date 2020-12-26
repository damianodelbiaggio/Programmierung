from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialoge")

        layout = QVBoxLayout()

        button_info = QPushButton("Show Information Dialog 01")
        button_about = QPushButton("Show About Dialog")
        button_aboutQt = QPushButton("About Qt")
        button_warning = QPushButton("Warning")
        button_critical = QPushButton("Critical")
        button_question = QPushButton("Question")
        button_open = QPushButton("Open Dialog")
        button_openmany = QPushButton("Open Multiple Files")
        button_save = QPushButton("Save Dialog")
        button_input = QPushButton("Input Dialogs")
        self.button_color = QPushButton("Color")

        layout.addWidget(button_info)
        layout.addWidget(button_about)
        layout.addWidget(button_aboutQt)
        layout.addWidget(button_warning)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_open)
        layout.addWidget(button_openmany)
        layout.addWidget(button_save)
        layout.addWidget(button_input)
        layout.addWidget(self.button_color)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

        button_info.clicked.connect(self.info)
        button_about.clicked.connect(self.about)
        button_aboutQt.clicked.connect(self.aboutqt)
        button_warning.clicked.connect(self.warning)
        button_critical.clicked.connect(self.critical)
        button_question.clicked.connect(self.question)
        button_open.clicked.connect(self.open)
        button_openmany.clicked.connect(self.openmany)
        button_save.clicked.connect(self.save)
        button_input.clicked.connect(self.input)
        self.button_color.clicked.connect(self.color)

    def info(self):
        link = "http://www.fhnw.ch"
        QDesktopServices.openUrl(QUrl(link))

        text = "Hier steht Informationstext<br/>Neue Zeile<br/><b>Ciao</b></br>"
        QMessageBox.information(self, "Information", text)

    def about(self):
        text = "Dieses Program wurte mit <b>Python</b> entwickelt"
        QMessageBox.about(self, "About", text)

    def aboutqt(self):
        QMessageBox.aboutQt(self)

    def warning(self):
        QMessageBox.warning(self, "Titel", "Vaffanculo!.")



    def critical(self):
        QMessageBox.critical(self, "Titel", "Die Konfigurationsdatei konnte nicht gelesen werden")
        exit(-1)

    def question(self):
        antwort = QMessageBox.question(self, "Titel", "Ist Python eine gute Sprache?", QMessageBox.Yes, QMessageBox.No)


        if antwort == QMessageBox.Yes:
            QMessageBox.information(self, "Titel", "Korrekt!")
        else:
            QMessageBox.critical(self, "Titel", "Hai ragione!")
            exit(842)

    def open(self):
        dir = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)

        filename, filter = QFileDialog.getOpenFileName(self, "Datei öffnen", dir, "Alle Dateien (*.*);;Vektor (*.shp, *.gpx)")

        if filename !="":
            print("Filename", filename)

            file = open(filename, encoding="utf-8")
            for zeile in file:
                print(zeile)
            file.close()
        else:
            QMessageBox.warning(self, "Warnung", "Kein Filename angegeben")

    def openmany(self):
        dir = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)

        filenames, filter = QFileDialog.getOpenFileNames(self, "Messdatei öffnen", dir,
                                                       "Alle Dateien (*.*);;Vektor (*.shp, *.gpx);;Python Datei (*.py)")

        if len(filenames)>0:
            for filename in filenames:
                print(filename)

        print()
        print(filter)

    def save(self):
        dir = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)

        filename, filter = QFileDialog.getSaveFileName(self, "Messdatei speichern", dir,
                                                         "Text (*.txt *.csv);;Vektor (*.shp, *.gpx);;Python Datei (*.py)")

        if filename !="":
            print(filename)
        else:
            print("Abbruch")

    def input(self):
        '''

        resultat, ok = QInputDialog.getInt(self, "Titel", "Was gibt 5+3", 0, 0, 10, 1)         #Anfangswert, min, max, Schritt

        if ok:
            if resultat == 8:
                QMessageBox.information(self, "Richtig", "Sie können rechnen")
            else:
                QMessageBox.warning(self, "Falsch", "Sie sollten in die Primarschule züruck")
        else:
            QMessageBox.warning(self, "?", "Sie geben sich leicht geschlagen!")

        #QInputDialog.getDouble(self, "Float (Double)", "Was gibt 5/2", 0, 0, 10, 0.5)



        resultat, ok = QInputDialog.getItem(self, "Computertyp", "Wie nehmen Sie am Unterricht teil?",
                             ["Laptop", "Tablet", "Smartphone", "Mehrere"], 2, False)

        if ok:
            print(resultat)
        '''

        resultat, ok = QInputDialog.getText(self, "Titel", "Ihr Password", QLineEdit.Password)

        if ok and resultat == "12345":
            print("Sie haben das Password erraten")
        else:
            print("FALSCH PASSWORD")

    def color(self):
        c = QColorDialog.getColor(QColor(255,0,0), self)

        print(c.red(), c.green(), c.blue())
        print(c.name)

        self.button_color.setColor(c)

        print(c.red(), c.green(), c.blue())


app = QApplication([])
win = MyWindow()
app.exec()