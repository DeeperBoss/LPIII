import math


class Triangulo:

  def __init__(self, P1, P2, P3):
    self.P1 = P1
    self.P2 = P2
    self.P3 = P3

  def imprimeTriangulo(self):
    return f'Triângulo com pontos P1({self.P1.x}, {self.P1.y}), P2({self.P2.x}, {self.P2.y}), P3({self.P3.x}, {self.P3.y})'

  def isTrianguloRetangulo(self):
    distancias = sorted([
        self.P1.distance(self.P2),
        self.P2.distance(self.P3),
        self.P3.distance(self.P1)
    ])
    return math.isclose(distancias[0]**2 + distancias[1]**2, distancias[2]**2)

  def isTrianguloIsosceles(self):
    distancias = [
        self.P1.distance(self.P2),
        self.P2.distance(self.P3),
        self.P3.distance(self.P1)
    ]
    return distancias.count(distancias[0]) == 2 or distancias.count(
        distancias[1]) == 2

  def isTrianguloEquilatero(self):
    distancias = [
        self.P1.distance(self.P2),
        self.P2.distance(self.P3),
        self.P3.distance(self.P1)
    ]
    return distancias.count(distancias[0]) == 3
