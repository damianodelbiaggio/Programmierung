class Vektor3:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def len(self):
        self.l = (((self.x)**2+(self.y)**2+(self.z)**2)**0.5)
        print(f"Der Vektor ist{self.l} lang")


a = Vektor3(1.0, 2.0, 3.0)
a.len()