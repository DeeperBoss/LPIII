          class Circulo:
            def __init__(self, x=0, y=0, r=1):
                self.x = x
                self.y = y
                self.r = r

            def __str__(self):
                return f"({self.x}, {self.y}, {self.r})"