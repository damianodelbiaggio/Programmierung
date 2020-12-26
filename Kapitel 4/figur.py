#Ellipse, Kreis, Quadrat, Polygon

#gemeinsame ATTRIBUTE: Schwerpunkt, Fläche, Farbe, Strichart, Name

class Figur:
    def __init__(self, name, farbe):
        self.name = name
        self.farbe = farbe

    def getName(self):
        return self.name

    def flaeche(self):
        return 0.0