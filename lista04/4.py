import math


class Ponto2D:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def setX(self, x):
    self.x = x

  def setY(self, y):
    self.y = y

  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def imprimirPonto(self):
    print("({0}, {1})".format(self.x, self.y))

  def isEixoX(self):
    return self.y == 0

  def isEixoY(self):
    return self.x == 0

  def isEixos(self):
    return self.x == 0 and self.y == 0

  def quadrante(self):
    if self.isEixos():
      return 0
    elif self.x > 0 and self.y > 0:
      return 1
    elif self.x < 0 and self.y > 0:
      return 2
    elif self.x < 0 and self.y < 0:
      return 3
    else:
      return 4

  def distancia(self, ponto2D):
    return math.sqrt((self.x - ponto2D.getX())**2 +
                     (self.y - ponto2D.getY())**2)
