class Vector3: #Klassendefinition
    def __init__(self, x, y, z):    #Konstruktor
        self.x = x
        self.y = y
        self.z = z

    def ausgabe(self):     #Methode
        print("Der Vektor hat die Länge:")

    def __len__(self):
        print(((self.x)**2+(self.y)**2+(self.z)**2)**0.5)

#---------------------------------------------------------------------

v0 = Vector3(10,3,5)     #Instanz

v0.ausgabe()
v0.__len__()

