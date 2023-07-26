class ShapeMeta(type):
    def __init__(cls, name, bases, attrs):
        cls.sides = 0

    def area(cls):
        raise NotImplementedError

class Shape(metaclass=ShapeMeta):
    pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    sides = 4

    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

class Triangle(Shape):
    sides = 3

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


obj = Circle(10)

print(obj.sides)