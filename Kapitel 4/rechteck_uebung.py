#Damiano Delbiaggio, G3

from figur_uebung import *
from punkt_uebung import *

class Rechteck(Figur_uebung):
    def __init__(self, p1, p2):
        super().__init__("Rechteck")
        self.p1 = p1
        self.p2 = p2

    def umfang(self):
        print("Der Umfang ist:")
        return (abs(self.p2.x - self.p1.x) + abs(self.p2.y - self.p1.y))*2

    def __str__(self):
        return f"{self.name}: Punkt 1= {self.p1}, Punkt 2= {self.p2}"

r = Rechteck(Punkt_uebung(3,5), Punkt_uebung(9,2))

print(r)
print(r.umfang())