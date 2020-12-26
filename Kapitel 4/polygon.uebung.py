#Damiano Delbiaggio, G3

from figur_uebung import *
from punkt_uebung import *

class Polygon(Figur_uebung):
    def __init__(self):
        super().__init__("Polygon")
        self.punkte = []
        self.umfang = 0

    def addPunkt(self, p):
        self.punkte.append(p)       #Beliebig viele Punkte (1, ...., n)


    def Umfang(self):
        for i in range(0, len(self.punkte)):
            self.umfang = self.umfang + (((self.punkte[i-1].x - self.punkte[i].x)**2 + (self.punkte[i-1].y - self.punkte[i].y)**2)**0.5)

        return f"Umfang: {self.umfang}"

    def __str__(self):
        return f"{self.name}: Anzahl Punkte: {len(self.punkte)}"

p1 = Punkt_uebung(1,2)
p2 = Punkt_uebung(3,6)
p3 = Punkt_uebung(9,2)
p4 = Punkt_uebung(8,1)
p5 = Punkt_uebung(5,4)

p = Polygon()

p.addPunkt(p1)
p.addPunkt(p2)
p.addPunkt(p3)
p.addPunkt(p4)
p.addPunkt(p5)

print(p)
print(p.Umfang())