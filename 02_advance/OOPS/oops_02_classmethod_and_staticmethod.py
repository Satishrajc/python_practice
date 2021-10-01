'''
Class method vs Static Method
A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take
some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a
static method in python.

* The class method can only access the class attributes but not the instance attributes.
* The class method can be called using ClassName.MethodName() and also using object.
* It can return an object of the class.

When to use what?
We generally use class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.
'''

# Python program to demonstrate
# use of a class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def age_form_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


person1 = Person('Satish', 21)
person2 = Person.age_form_birth_year('Niteen', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.is_adult(22))
print(person1.is_adult(15))
