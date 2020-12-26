class Kurs:
    def __init__(self, name, semester, zeit):
        self.name = name
        self.semester = semester
        self.zeit = zeit
        self.klasse = []

    def __str__(self):
        return f"{self.name}, {self.semester}, {len(self.klasse)}"

    def helloworld(self):
        print("Ciao ciao")