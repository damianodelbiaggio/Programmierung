#Klassendefinition:
class Punkt:
    def __init__(self,x, y, id=0, name=""): #Konstruktor
        self.x = x
        self.y = y
        self.id = id
        self.name = name

    def __del__(self):
        print("Die Klasse wird gelöscht!")

    def sety(self, y):
        self.y = y

    def setx(self, x):
        self.x = x

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    #Methode
    def ausgabe(self):
        print("Der Punkt hat die Attribute:")
        print(f"x={self.x} y={self.y} id={self.id} name ={self.name}")

    def transform(self):
        self.x = self.x +1.0
        self.y = self.y +2.0


    xvalue = property(getx, setx)
    yvalue = property(gety, sety)

#---------------------------------------------------------------------------------

#Instanz
p0 = Punkt(10.0, 15.2, 1, "Punkt 1")
p1 = Punkt(5.1, 3.2)
p2 = Punkt(9.8, 7.4)

p0.ausgabe()
p0.transform()
p0.transform()
p0.ausgabe()

del p0
p1 = 0

input("Bitte Namen eingeben>")


