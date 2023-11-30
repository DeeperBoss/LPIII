from abc import ABC, abstractmethod
import math

class Figura3D(ABC):
    def __init__(self, raio, altura):
        self.raio = raio
        self.altura = altura

    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def area_superficial(self):
        pass

    def __str__(self):
        return f'Raio: {self.raio}, Altura: {self.altura}'

class Cilindro(Figura3D):
    def volume(self):
        return math.pi * (self.raio ** 2) * self.altura

    def area_superficial(self):
        return 2 * math.pi * self.raio * (self.raio + self.altura)

class Cone(Figura3D):
    def volume(self):
        return (1/3) * math.pi * (self.raio ** 2) * self.altura

    def area_superficial(self):
        return math.pi * self.raio * (self.raio + math.sqrt((self.altura ** 2) + (self.raio ** 2)))

# Programa de exemplo
cilindro = Cilindro(3, 5)
cone = Cone(3, 5)

print(cilindro)
print(f'Volume: {cilindro.volume()}, Área Superficial: {cilindro.area_superficial()}')

print(cone)
print(f'Volume: {cone.volume()}, Área Superficial: {cone.area_superficial()}')