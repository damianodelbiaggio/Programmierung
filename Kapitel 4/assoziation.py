class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Student: {self.name}, {self.id}"

#-----------------------------------------------------

class Programmierkurs:
    def __init__(self, name):
        self.name = name
        self.klasse = []

    def addStudent(self, s):
        self.klasse.append(s)

    def getStudents(self):
        for i in self.klasse:
            print(i)


    def __str__(self):
        return f"{self.name}, Anzahl Studierende: {len(self.klasse)}"

#-----------------------------------------------------
class Mathematikkurs:
    def __init__(self, name):
        self.name = name
        self.klasse = []

    def addStudent(self, s):
        self.klasse.append(s)

    def getStudents(self):
        for i in self.klasse:
            print(i)


    def __str__(self):
        return f"{self.name}, Anzahl Studierende: {len(self.klasse)}"
#------------------------------------------------------------------------

s1 = Student("Hans Muster", "20-323-435")
s2 = Student("Damiano Delbiaggio", "20-122-234")
s3 = Student("Gesu Bambino", "20-122-134")

PythonKurs = Programmierkurs("Python 1")
PythonKurs.addStudent(s1)
PythonKurs.addStudent(s2)
print(PythonKurs)
print(PythonKurs.getStudents())

print("*"*10)

MatheKurs = Mathematikkurs("Mathe 3. Semester")
MatheKurs.addStudent(s1)
MatheKurs.addStudent(s3)
print(MatheKurs)
MatheKurs.getStudents()

print("*"*10)

s1.id = "15-234-333"
MatheKurs.getStudents()