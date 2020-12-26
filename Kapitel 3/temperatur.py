#Klassendefinition
class Temperatur:
    def __init__(self, v):
        self.settemp(v)

    def __str__(self):
        return str(self.value) + "°C"

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ne__(self, other):
        return self.value != other.value

    def settemp(self, value):
        if value<-273.15:
            raise ValueError("Temperatur ungültig!")
        else:
            self._value = value

    def gettemp(self):
        return self._value

    value = property(gettemp, settemp)

#----------------------------------------------------------------------------------------

t1 = Temperatur(14)
t2 = Temperatur(15)
t3 = Temperatur(15)
if t1 < t2:
    print("heute ist es kälter")

if t2 > t1:
    print("gestern war es wärmer")

if t2 >= t3:
    print("t2 und t3 sind grösser oder gleich")

if t2 >= t3:
    print("t2 und t3 sind grösser oder gleich")

if t2 <= t3:
    print("t2 und t3 sind kleiner oder gleich")

if t2 != t3:
    print("t2 und t3 sind ungleich")

print(t1, t2)