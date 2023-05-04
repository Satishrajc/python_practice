from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Create objects of the Rectangle and Circle classes
rect = Rectangle(5, 10)
circ = Circle(7)

# Call the area() method on the objects
print(rect.area())
print(circ.area())

"""
In this example, we use abstraction to define the Shape abstract class, 
which defines the common interface for the Rectangle and Circle classes. 
The Shape class has an abstract area() method, which is implemented by the subclasses.
"""