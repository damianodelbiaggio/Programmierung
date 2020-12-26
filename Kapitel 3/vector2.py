class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2(self.x + other, self.y + other)
        return Vector2(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2(self.x + other, self.y + other)
        return Vector2(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

a = Vector2(3,4)
b = Vector2(4,5)

c = a + b
d = c+a+b+a+c

e = -a
print(e)