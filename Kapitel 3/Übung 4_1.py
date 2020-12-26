#Damiano Delbiaggio
class Vector3:
 #Konstruktor
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

#Methode
    def __str__(self):
        return f"[{self.x},{self.y},{self.z}]"

#Addition
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x + other, self.y + other, self.z + other)
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x + other, self.y + other, self.z + other)
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

#Subtraktion
    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x - other, self.y - other, self.z - other)
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __rsub__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x - other, self.y - other, self.z - other)
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

#Multiplication Komponentenweise
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

#Skalarprodukt
    def dot(self, other):
        return(self.x * other.x + self.y * other.y + self.z * other.z)

#Vektorprodukt
    def cross(self, other):
        return Vector3(self.y * other.z - self.z * other.y,self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

#Normalisierung
    def normalize(self):
        return Vector3(self.x / ((self.x**2+self.y**2 +self.z**2)**(1/2)), self.y /((self.x**2+self.y**2 +self.z**2)**(1/2))/ self.z /((self.x**2+self.y**2 +self.z**2)**(1/2)))


#Instanzen
a = Vector3(3,4,2)
b = Vector3(2,1,0)

c = a * b
print(c)
d = a.dot(b)
print(d)
e = a.cross(b)
print(e)
f = a.normalize()
print(f)