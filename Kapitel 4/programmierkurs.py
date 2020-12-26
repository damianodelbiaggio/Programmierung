from kurs import *

class Programmieren(Kurs):
    def __init__(self, name, semester, zeit, programmiersprache):
        super().__init__(name, semester, zeit)
        self.programmiersprache = programmiersprache


PR2 = Programmieren("Programmierung 2", 3, "13:30-15:15", "Python")
print(PR2)
PR2.helloworld()