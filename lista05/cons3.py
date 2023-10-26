from math import pi, sqrt


class Circulo:

  def __init__(self, x, y, r):
    self.x = x
    self.y = y
    self.r = r

  def validaCirculo(self):
    return self.r > 0

  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def getR(self):
    return self.r

  def setX(self, x):
    self.x = x

  def setY(self, y):
    self.y = y

  def setR(self, r):
    self.r = r

  def imprimirCirculo(self):
    print(f"Centro: ({self.x}, {self.y}), Raio: {self.r}")

  def isInnerPoint(self, ponto):
    return sqrt((ponto.getX() - self.x)**2 +
                (ponto.getY() - self.y)**2) < self.r

  def area(self):
    return pi * self.r**2

  def perimeter(self):
    return 2 * pi * self.r

  def isBiggerThan(self, circulo):
    return self.area() > circulo.area()
