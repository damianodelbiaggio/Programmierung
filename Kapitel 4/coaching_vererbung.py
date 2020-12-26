class Punkt_uebung:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt({self.x}, {self.y})"

    def distanz(self, other):
        return((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

def als_punkt(p):
    if isinstance(p, Punkt_uebung):
        return Punkt_uebung(p.x, p.y)

    #(x,y), [x,y] -> Punkt
    elif isinstance(p, (list, tuple)) and len(p) == 2:
        return Punkt_uebung(p[0], p[1])
    else:
        raise ValueError(f"Kann keinen Punkt aus {p} erstellen")

class Figur_uebung:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def umfang(self):
        #return 0.0
        raise NotImplementedError

class Dreieck(Figur_uebung):
    def __init__(self, p1, p2, p3):
        super().__init__("Dreieck")
        self.p1 = als_punkt(p1)
        self.p2 = als_punkt(p2)
        self.p3 = als_punkt(p3)

    def __str__(self):
        return super().__str__() + f"({self.p1}, {self.p2}, {self.p3})"

    def umfang(self):
        # summe der Distanzen: p1-p2, p2-p3, p3-p1
        return self.p1.distanz(self.p2) + self.p2.distanz(self.p3) + self.p3.distanz(self.p1)

class Polygon(Figur_uebung):
    def __init__(self, punkte):
        super().__init__("Polygon")
        if len(punkte) < 3:
            raise ValueError("Ein Polygon muss mindestens aus 3 Punkten bestehen (p1 != pn)")
        self.punkte = [als_punkt(p) for p in punkte]

    def __str__(self):
        return super().__str__() + f"({[str(p)for p in self.punkte]})"

    def umfang(self):
        #summe der Distanzen: p1-p2, p2-p3,..... pn-p1
        for i in range(len(self.punkte)):
            j = (i + 1) % len(self.punkte)
            pi = self.punkte[i]
            pj = self.punkte[j]
            u += pi.distanz(pj)
        return u

#d = Dreieck(Punkt_uebung(0,0), Punkt_uebung(1,0), Punkt_uebung(0,1))
#print(d)
#print(d.umfang())
#d = Dreieck("A", "B", "C")
#print(d)
#print(d.umfang())
#d = Dreieck((0,0), (1,0), (0,1))
#print(d)
#print(d.umfang())
#p1 = Punkt_uebung()
#p2 = (1,1)
#p3 = [1,4]
#p4 = "A"
#for p in (p1, p2, p3, p4):
   # print(als_punkt(p))

p = Polygon([(0,0), (1,0), (1,1), (0,1)])
print(p)
print(p.umfang())
