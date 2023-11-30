import math

class Ponto2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def toString(self):
        return f'({self.x}, {self.y})'

    def inAxisX(self):
        return self.y == 0

    def inAxisY(self):
        return self.x == 0

    def inAxis(self):
        return self.inAxisX() or self.inAxisY()

    def isOrigin(self):
        return self.x == 0 and self.y == 0

    def distance(self, x, y=None):
        if isinstance(x, Ponto2D):
            return math.sqrt((self.x - x.x)**2 + (self.y - x.y)**2)
        else:
            return math.sqrt((self.x - x)**2 + (self.y - y)**2)

# Programa de exemplo
p1 = Ponto2D(3, 4)
p2 = Ponto2D(6, 8)

print(p1.toString())
print(p1.inAxisX())
print(p1.inAxisY())
print(p1.inAxis())
print(p1.isOrigin())
print(p1.distance(p2))
print(p1.distance(6, 8))