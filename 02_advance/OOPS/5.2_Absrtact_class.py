from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Attempting to create an instance of the abstract class will raise an error
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())


# If a child class inherits from an abstract class and does not implement all the abstract 
# methods defined in the abstract class, then the child class itself becomes an abstract class.
# This means that the child class cannot be instantiated directly, and it must be subclassed 
# further to provide concrete implementations for the remaining abstract methods.
