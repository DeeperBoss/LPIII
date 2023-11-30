import math


class Ponto2D:

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def distance(self, other):
    return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


# Composição
class Ponto3D_Composicao:

  def __init__(self, x=0, y=0, z=0):
    self.ponto2d = Ponto2D(x, y)
    self.z = z

  def distance(self, other):
    return math.sqrt(
        self.ponto2d.distance(other.ponto2d)**2 + (self.z - other.z)**2)


# Agregação
class Ponto3D_Agregacao:

  def __init__(self, ponto2d, z=0):
    self.ponto2d = ponto2d
    self.z = z

  def distance(self, other):
    return math.sqrt(
        self.ponto2d.distance(other.ponto2d)**2 + (self.z - other.z)**2)


# Herança
class Ponto3D_Heranca(Ponto2D):

  def __init__(self, x=0, y=0, z=0):
    super().__init__(x, y)
    self.z = z

  def distance(self, other):
    return math.sqrt(super().distance(other)**2 + (self.z - other.z)**2)


# Programa de exemplo
p1 = Ponto3D_Composicao(3, 4, 5)
p2 = Ponto3D_Composicao(6, 8, 10)

print(p1.distance(p2))

p1 = Ponto3D_Agregacao(Ponto2D(3, 4), 5)
p2 = Ponto3D_Agregacao(Ponto2D(6, 8), 10)

print(p1.distance(p2))

p1 = Ponto3D_Heranca(3, 4, 5)
p2 = Ponto3D_Heranca(6, 8, 10)

print(p1.distance(p2))
