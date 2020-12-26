class Kurs:
    def __init__(self, name, semester, zeit):
        self.name = name
        self.semester = semester
        self.zeit = zeit
        self.klasse = []

    def __str__(self):
        return f"{self.name}, {self.semester}, {len(self.klasse)}"




Programmierkurs = Kurs("Programmieren 2", 3, "13:30-15:15", "Python")
MatheKurs = Kurs("Mathematik 1", 1, "Mittwoch 08:30-12:15", "R")
SoftSkills = Kurs("Softskills 2", 2, "Fr 16:30-18:15", "")