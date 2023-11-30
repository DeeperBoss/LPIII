import math

class Shape2D:
    def __init__(self):
        pass

    def draw(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape2D):
    def __init__(self, radius=1):
        self.radius = radius

    def draw(self):
        return f'Circle with radius {self.radius}'

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape2D):
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def draw(self):
        return f'Rectangle with width {self.width} and height {self.height}'

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side=1):
        super().__init__(side, side)

    def draw(self):
        return f'Square with side {self.width}'

class Triangle(Shape2D):
    def __init__(self, base=1, height=1):
        self.base = base
        self.height = height

    def draw(self):
        return f'Triangle with base {self.base} and height {self.height}'

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.base + 2 * math.sqrt((self.base / 2) ** 2 + self.height ** 2)

class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw_all(self):
        for shape in self.shapes:
            print(shape.draw())

    def calculate_total_area(self):
        return sum(shape.calculate_area() for shape in self.shapes)

    def calculate_total_perimeter(self):
        return sum(shape.calculate_perimeter() for shape in self.shapes)

# Programa de exemplo
shapes = ShapeCollection()
shapes.add_shape(Circle(5))
shapes.add_shape(Rectangle(4, 6))
shapes.add_shape(Square(3))
shapes.add_shape(Triangle(4, 5))
shapes.draw_all()
print('Total area:', shapes.calculate_total_area())
print('Total perimeter:', shapes.calculate_total_perimeter())