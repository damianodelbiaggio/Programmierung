from figur import *
from punkt import *
import math



class Kreis(Figur):
    def __init__(self, m, r, farbe):
        super().__init__("Kreis", farbe)
        self.m = m
        self.r = r

    def flaeche(self):
        return self.r**2*math.pi

    def __str__(self):
        return f"{self.name}: {self.m}, {self.r}"

k = Kreis(Punkt(5,4), 3.2, "Grün")
print(k.getName())
print(k.flaeche())