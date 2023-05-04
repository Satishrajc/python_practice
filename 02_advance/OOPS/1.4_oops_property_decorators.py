"""
In Python, @property is a built-in decorator that allows us to define 
a method that behaves like an attribute. It provides a convenient way to 
encapsulate the access to an object's attributes, allowing us to control 
how they are accessed or modified.
"""

class MyClass:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "String representation for end user"

    def __repr__(self):
        return "String representation for debugging"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @fullname.setter
    def fullname(self, name):
        self.first_name, self.last_name = name.split(' ')

    # self.last_name = last_name

    @fullname.deleter
    def fullname(self):
        print("In deleter")

        self.first_name = None
        self.last_name = None


# ------------------------------------------
obj2 = MyClass("Mama", 50)
print(obj2)
# If we dont have __str__ then Python automatically calls __repr__
# reverse is not possible

# print(repr(obj2))
# print(str(obj2))
# -------------------------------------

# fullname can be called as a variable
print(obj2.fullname)

obj2.fullname = "Kaka 55"
print(obj2.fullname)

del obj2.fullname
