"""
In Python, @property is a built-in decorator that allows us to define 
a method that behaves like an attribute. It provides a convenient way to 
encapsulate the access to an object's attributes, allowing us to control 
how they are accessed or modified.
"""

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

p = Person("Alice", 25)

print(p.name)  # output: Alice
print(p.age)  # output: 25

p.age = 30
print(p.age)  # output: 30

p.age = -1  # raises ValueError: Age cannot be negative
