#Damiano Delbiaggio, G3

from figur_uebung import *
from punkt_uebung import *

class Dreieck(Figur_uebung):
    def __init__(self, p1, p2, p3):
        super().__init__("Dreieck")
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def umfang(self):
        print("Der Umfang ist:")
        return (((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)**0.5)+ \
               (((self.p3.x - self.p2.x)**2 + (self.p3.y - self.p2.y)**2)**0.5)+ \
               (((self.p1.x - self.p3.x)**2 + (self.p1.y - self.p3.y)**2)**0.5)

    def __str__(self):
        return f"{self.name}: Punkt 1= {self.p1}, Punkt 2= {self.p2}, Punkt 3= {self.p3}"

d = Dreieck(Punkt_uebung(5,1), Punkt_uebung(3,6), Punkt_uebung(5, 4))

print(d)
print(d.umfang())