#Damiano Delbiaggio, G3

from figur_uebung import *
from punkt_uebung import *
import math

class Kreis(Figur_uebung):
    def __init__(self, m, r):
        super().__init__("Kreis")
        self.m = m
        self.r = r

    def umfang(self):
        print("Der Umfang ist:")
        return (self.r + self.r)*math.pi

    def __str__(self):
        return f"{self.name}: Mittelpunkt= {self.m}, Radius= {self.r}"

k = Kreis(Punkt_uebung(5.6, 1.3), 3.2)
print(k)
print(k.umfang())



