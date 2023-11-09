    import math

    class Ponto2D:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def distance(self, *args):
            if len(args) == 0:
                return math.sqrt(self.x**2 + self.y**2)
            elif len(args) == 1:
                if isinstance(args[0], Ponto2D):
                    dx = self.x - args[0].x
                    dy = self.y - args[0].y
                else:
                    raise TypeError("Argumento inválido")
            elif len(args) == 2:
                dx = self.x - args[0]
                dy = self.y - args[1]
            else:
                raise TypeError("Número inválido de argumentos")

            return math.sqrt(dx**2 + dy**2)

        def __str__(self):
            return f"({self.x}, {self.y})"